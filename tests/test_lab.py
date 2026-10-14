"""Offline checks for installer integrity, boundaries and bounded collection."""
import contextlib
import hashlib
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import io
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import threading
import time
import unittest
from unittest import mock
import zipfile

import benchmark
import lab


class LocalServer:
    """Serve deterministic fake data without loading any inference model."""

    def __init__(self, handler: type) -> None:
        self.server = ThreadingHTTPServer(("127.0.0.1", 0), handler)
        self.thread = threading.Thread(target=self.server.serve_forever, daemon=True)

    def __enter__(self) -> str:
        self.thread.start()
        return f"http://127.0.0.1:{self.server.server_port}"

    def __exit__(self, *args: object) -> None:
        self.server.shutdown()
        self.server.server_close()
        self.thread.join(timeout=3)


class QuietHandler(BaseHTTPRequestHandler):
    """Suppress HTTP access noise in offline tests."""

    def log_message(self, *args: object) -> None:
        """Do not log test request payloads."""


class LabTests(unittest.TestCase):
    """Exercise failure boundaries, not a duplicate of model implementations."""

    def test_archive_traversal_rejected(self) -> None:
        """Reject Windows and POSIX archive escapes before extraction."""
        for name in ("../outside", "C:/outside", "/outside", "..\\outside", "x:stream"):
            with self.subTest(name=name), tempfile.TemporaryDirectory() as tmp:
                root = Path(tmp)
                archive = root / "bad.zip"
                with zipfile.ZipFile(archive, "w") as bundle:
                    bundle.writestr(name, "bad")
                with self.assertRaises(ValueError):
                    lab.extract_zip(archive, root / "install")
                self.assertFalse((root / "outside").exists())

    def test_archive_symlink_and_collision(self) -> None:
        """Refuse symlinks and overwriting files from an earlier archive."""
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            archive = root / "bad.zip"
            item = zipfile.ZipInfo("link")
            item.create_system = 3
            item.external_attr = 0o120777 << 16
            with zipfile.ZipFile(archive, "w") as bundle:
                bundle.writestr(item, "outside")
            with self.assertRaises(ValueError):
                lab.extract_zip(archive, root)
            with zipfile.ZipFile(archive, "w") as bundle:
                bundle.writestr("exists.txt", "replacement")
            (root / "exists.txt").write_text("original")
            with self.assertRaises(ValueError):
                lab.extract_zip(archive, root)
            self.assertEqual((root / "exists.txt").read_text(), "original")

    def test_download_resume_and_hash(self) -> None:
        """Resume actual HTTP bytes into a spaced path and verify their digest."""
        body = b"small pinned artifact"

        class Handler(QuietHandler):
            def do_GET(self) -> None:
                offset = int(self.headers.get("Range", "bytes=0-")[6:-1])
                self.send_response(206 if offset else 200)
                self.send_header("Content-Range", f"bytes {offset}-{len(body)-1}/{len(body)}")
                self.end_headers()
                self.wfile.write(body[offset:])

        with LocalServer(Handler) as url, tempfile.TemporaryDirectory(prefix="space path ") as tmp:
            target = Path(tmp) / "model.bin"
            target.with_suffix(".bin.part").write_bytes(body[:5])
            spec = {"url": url, "bytes": len(body), "sha256": hashlib.sha256(body).hexdigest()}
            lab.download(spec, target)
            self.assertEqual(target.read_bytes(), body)
            with self.assertRaises(ValueError):
                lab.verify(target, {**spec, "sha256": "0" * 64})

    def test_download_bad_hash_not_published(self) -> None:
        """A checksum failure must never create the final model file."""
        class Handler(QuietHandler):
            def do_GET(self) -> None:
                self.send_response(200)
                self.end_headers()
                self.wfile.write(b"bad")

        with LocalServer(Handler) as url, tempfile.TemporaryDirectory() as tmp:
            target = Path(tmp) / "model.bin"
            with self.assertRaises(ValueError):
                lab.download({"url": url, "bytes": 3, "sha256": "0" * 64}, target)
            self.assertFalse(target.exists())
            self.assertTrue(target.with_suffix(".bin.part").exists())

    def test_plan_is_read_only(self) -> None:
        """Planning must neither call the network nor create a data directory."""
        with tempfile.TemporaryDirectory() as tmp, mock.patch("lab.download") as download:
            target = Path(tmp) / "not-created"
            with contextlib.redirect_stdout(io.StringIO()):
                lab.install_runtime(target, False)
            download.assert_not_called()
            self.assertFalse(target.exists())

    def test_memory_and_paths(self) -> None:
        """Memory gates fail closed and model paths stay single arguments."""
        profile = lab.read_json(lab.ROOT / "profiles/qwen36-reference.json")
        for sample in ({}, {"ram_free_gib": 2, "vram_free_mib": 7000, "gpu_c": 40}):
            with self.assertRaises(ValueError):
                lab.check_memory(sample, profile, loading=True)
        command = lab.build_command(Path("C:/space dir/server.exe"), Path("E:/model dir/a.gguf"), profile, 8080)
        self.assertEqual(command[2], str(Path("E:/model dir/a.gguf")))
        self.assertIn("127.0.0.1", command)

    def test_fixture_tool_boundary(self) -> None:
        """A tool cannot escape through traversal, absolute paths or unknown names."""
        sources = benchmark.fixture_snapshot()
        self.assertIn("content", json.loads(benchmark.read_fixture("AGENTS.md", sources)))
        for name in ("../secrets/key", "C:/Users/EXAMPLE/.env", "rubric.md", None):
            self.assertIn("error", json.loads(benchmark.read_fixture(name, sources)))

    def test_endpoint_boundary(self) -> None:
        """Keep benchmark requests on explicit loopback without credentials."""
        for value in ("https://example.org/v1", "http://127.0.0.1.evil/v1",
                      "http://user:secret@localhost/v1", "http://localhost/v1?q=x"):
            with self.assertRaises(ValueError):
                benchmark.validate_endpoint(value)

    def test_redirect_is_refused(self) -> None:
        """A local redirect cannot export prompts to a remote endpoint."""
        class Handler(QuietHandler):
            def do_POST(self) -> None:
                self.rfile.read(int(self.headers["Content-Length"]))
                self.send_response(302)
                self.send_header("Location", "https://example.org/collect")
                self.end_headers()

        with LocalServer(Handler) as url, tempfile.TemporaryDirectory() as tmp:
            with self.assertRaises(ValueError):
                benchmark.stream_turn(url + "/v1", {"messages": []},
                                      Path(tmp) / "events.jsonl", time.monotonic())

    def test_manifest_and_profiles(self) -> None:
        """Every profile refers to a pinned artifact and explicit stop thresholds."""
        models = lab.read_json(lab.ROOT / "catalog/models.json")["models"]
        for value in models.values():
            self.assertRegex(value["revision"], r"^[a-f0-9]{40}$")
            self.assertRegex(value["sha256"], r"^[a-f0-9]{64}$")
            self.assertGreater(value["bytes"], 0)
        for path in (lab.ROOT / "profiles").glob("*.json"):
            profile = lab.read_json(path)
            self.assertIn(profile["model"], models)
            self.assertGreater(profile["load_min_ram_free_gib"], profile["stop_min_ram_free_gib"])
            self.assertGreater(profile["load_min_vram_free_mib"], profile["stop_min_vram_free_mib"])

    @unittest.skipUnless(sys.platform == "win32", "Windows lifecycle API")
    def test_owned_server_stop_file(self) -> None:
        """A stop request terminates only the owned fake child and records why."""
        import argparse
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            runtime = root / "runtime"
            runtime.mkdir()
            (runtime / "llama-server.exe").write_bytes(b"placeholder")
            stop = root / "stop"
            args = argparse.Namespace(profile="qwen36-reference", experimental=False,
                                      model_path=str(root / "model.gguf"),
                                      runtime_dir=str(runtime), port=0, apply=True,
                                      stop_file=str(stop))
            child = mock.Mock(pid=123, returncode=None)
            child.poll.return_value = None
            def stopped() -> None:
                """Simulate child exit after its handle receives termination."""
                child.poll.return_value = 0
            child.terminate.side_effect = stopped
            profile = lab.read_json(lab.ROOT / "profiles/qwen36-reference.json")
            advertised = " ".join(profile["args"]) + " b2f036c0f"
            result = subprocess.CompletedProcess([], 0, advertised, "")
            telemetry = {"ram_free_gib": 40, "vram_free_mib": 8000, "gpu_c": 40}
            with mock.patch("lab.verify"), mock.patch("lab.check_hardware_events"), \
                    mock.patch("lab.memory_snapshot", return_value=telemetry), \
                    mock.patch("lab.process_memory", return_value={}), \
                    mock.patch("lab.subprocess.run", return_value=result), \
                    mock.patch("lab.subprocess.Popen", return_value=child), \
                    mock.patch("lab.time.sleep", side_effect=lambda _: stop.touch()), \
                    contextlib.redirect_stdout(io.StringIO()):
                lab.run_server(args, root / "data")
            child.terminate.assert_called_once()
            child.kill.assert_not_called()
            records = list((root / "data/runs").glob("*/stop.json"))
            self.assertEqual(len(records), 1)
            self.assertEqual(lab.read_json(records[0])["status"], "requested_stop")

    def test_truncated_answer_unscored(self) -> None:
        """A token-limit finish is not silently reported as a completed solution."""
        class Handler(QuietHandler):
            def do_POST(self) -> None:
                self.rfile.read(int(self.headers["Content-Length"]))
                self.send_response(200)
                self.end_headers()
                event = {"choices": [{"delta": {"content": "def unfinished("}, "finish_reason": "length"}]}
                self.wfile.write(("data: " + json.dumps(event) + "\n\n").encode())

        with LocalServer(Handler) as url, tempfile.TemporaryDirectory() as tmp:
            output = Path(tmp) / "run"
            result = subprocess.run([sys.executable, str(lab.ROOT / "benchmark.py"),
                                     "--endpoint", url + "/v1", "--output", str(output),
                                     "--deadline", "5"], capture_output=True, timeout=10)
            self.assertEqual(result.returncode, 2, result.stderr)
            self.assertEqual(lab.read_json(output / "result.json")["status"], "incomplete")
            self.assertFalse(lab.read_json(output / "result.json")["scored"])

    def test_silent_stream_whole_deadline(self) -> None:
        """A server that never sends bytes must not evade the parent deadline."""
        class Handler(QuietHandler):
            def do_POST(self) -> None:
                self.rfile.read(int(self.headers["Content-Length"]))
                self.send_response(200)
                self.send_header("Content-Type", "text/event-stream")
                self.end_headers()
                self.wfile.flush()
                time.sleep(4)

        with LocalServer(Handler) as url, tempfile.TemporaryDirectory() as tmp:
            output = Path(tmp) / "run"
            start = time.monotonic()
            result = subprocess.run([sys.executable, str(lab.ROOT / "benchmark.py"),
                                     "--endpoint", url + "/v1", "--deadline", "1",
                                     "--output", str(output)], capture_output=True, timeout=8)
            self.assertEqual(result.returncode, 124, result.stderr)
            self.assertLess(time.monotonic() - start, 5)
            self.assertEqual(lab.read_json(output / "result.json")["status"], "deadline")

    def test_tool_round_trip(self) -> None:
        """A fake model reads an allowed file, then returns an unscored answer."""
        payloads = []

        class Handler(QuietHandler):
            def do_POST(self) -> None:
                payload = json.loads(self.rfile.read(int(self.headers["Content-Length"])))
                payloads.append(payload)
                if len(payloads) == 1:
                    delta = {"tool_calls": [{"index": 0, "id": "read-1", "type": "function",
                             "function": {"name": "read_file", "arguments": '{"path":"AGENTS.md"}'}}]}
                    finish = "tool_calls"
                else:
                    delta, finish = {"content": "Read AGENTS.md. No tests executed."}, "stop"
                event = {"choices": [{"delta": delta, "finish_reason": finish}]}
                self.send_response(200)
                self.send_header("Content-Type", "text/event-stream")
                self.end_headers()
                self.wfile.write(("data: " + json.dumps(event) + "\n\ndata: [DONE]\n\n").encode())

        with LocalServer(Handler) as url, tempfile.TemporaryDirectory() as tmp:
            output = Path(tmp) / "run"
            result = subprocess.run([sys.executable, str(lab.ROOT / "benchmark.py"),
                                     "--endpoint", url + "/v1", "--output", str(output),
                                     "--deadline", "5"], capture_output=True, timeout=10)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual(len(payloads), 2)
            self.assertEqual(payloads[1]["messages"][-1]["role"], "tool")
            evidence = lab.read_json(output / "result.json")
            self.assertEqual(evidence["status"], "completed")
            self.assertFalse(evidence["scored"])


if __name__ == "__main__":
    unittest.main()
