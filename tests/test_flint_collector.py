"""Protocol-only checks: preserve evidence and enforce whole-request deadlines."""
from contextlib import contextmanager
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import threading
import time
import unittest

ROOT = Path(__file__).resolve().parents[1]


@contextmanager
def endpoint(delay: float, completed: bool = True):
    """Serve synthetic SSE only; no real inference or generated-code execution."""
    class Handler(BaseHTTPRequestHandler):
        def log_message(self, *args):
            """Silence request logging in offline tests."""

        def do_POST(self):
            """Reply after a controlled delay to exercise cancellation."""
            self.rfile.read(int(self.headers["Content-Length"]))
            self.send_response(200)
            self.send_header("Content-Type", "text/event-stream")
            self.end_headers()
            time.sleep(delay)
            events = [
                {"choices": [{"delta": {"reasoning_content": "reason"}}]},
                {"choices": [{"delta": {"content": "answer"}, "finish_reason": "stop"}],
                 "usage": {"completion_tokens": 2}},
            ]
            if not completed:
                events[-1] = {"choices": [{"delta": {"content": "partial answer"}}]}
            try:
                for event in events:
                    self.wfile.write(("data: " + json.dumps(event) + "\n\n").encode())
                if completed:
                    self.wfile.write(b"data: [DONE]\n\n")
                self.wfile.flush()
            except (BrokenPipeError, ConnectionResetError, ConnectionAbortedError):
                pass

    server = ThreadingHTTPServer(("127.0.0.1", 0), Handler)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    try:
        yield f"http://127.0.0.1:{server.server_port}/v1"
    finally:
        server.shutdown()
        server.server_close()
        thread.join(timeout=2)


class FlintCollectorTests(unittest.TestCase):
    def run_case(self, temporary: Path, url: str, deadline: str,
                 extra: tuple[str, ...] = ()):
        """Launch the real collector against an explicitly trusted tiny fixture."""
        suite = temporary / "suite.py"
        suite.write_text("TASKS = [{'id':'one', 'language':'python', 'prompt':'unchanged question'}]\n")
        output = temporary / "run"
        process = subprocess.run(
            [sys.executable, str(ROOT / "experiments/flint/collect_coding.py"),
             "--suite-file", str(suite), "--output", str(output),
             "--model", "fake", "--endpoint", url, "--deadline", deadline,
             *extra],
            capture_output=True, text=True, timeout=10)
        return process, output

    def test_completed_evidence(self):
        """Keep the question, request, reasoning and final answer separately."""
        with tempfile.TemporaryDirectory() as tmp, endpoint(0) as url:
            process, output = self.run_case(Path(tmp), url, "5")
            self.assertEqual(process.returncode, 0, process.stderr)
            request = json.loads((output / "requests/one.json").read_text())
            self.assertEqual(request["payload"]["messages"][0]["content"], "unchanged question")
            response = json.loads((output / "responses/one.json").read_text())
            self.assertEqual(response["choices"][0]["message"]["content"], "answer")
            self.assertEqual(response["choices"][0]["message"]["reasoning_content"], "reason")
            self.assertFalse((output / "grades.json").exists())

    def test_extended_allowance_requires_opt_in_and_records_cohort(self):
        """Prevent an unnoticed deadline change from contaminating old scores."""
        with tempfile.TemporaryDirectory() as tmp, endpoint(0) as url:
            process, output = self.run_case(Path(tmp), url, "21600")
            self.assertNotEqual(process.returncode, 0)
            self.assertFalse(output.exists())
            process, output = self.run_case(
                Path(tmp), url, "21600", ("--extended-diagnostic",))
            self.assertEqual(process.returncode, 0, process.stderr)
            record = json.loads((output / "collect.json").read_text())
            self.assertEqual(record["cohort"], "extended-diagnostic")
            self.assertEqual(record["deadline"], 21600)
            request = json.loads((output / "requests/one.json").read_text())
            self.assertEqual(request["payload"]["messages"][0]["content"],
                             "unchanged question")
            self.assertFalse((output / "grades.json").exists())

    def test_silent_response_hard_deadline(self):
        """A server that sends no body cannot extend the whole-task deadline."""
        with tempfile.TemporaryDirectory() as tmp, endpoint(3) as url:
            started = time.monotonic()
            process, output = self.run_case(Path(tmp), url, "0.5")
            self.assertLess(time.monotonic() - started, 3)
            self.assertEqual(process.returncode, 2, process.stderr)
            response = json.loads((output / "responses/one.json").read_text())
            self.assertEqual(response["benchmark"]["error"], "whole_prompt_deadline")
            self.assertNotIn("choices", response)

    def test_early_stream_close_preserves_partial_unscored(self):
        """EOF without a terminal finish cannot become a completed coding answer."""
        with tempfile.TemporaryDirectory() as tmp, endpoint(0, completed=False) as url:
            process, output = self.run_case(Path(tmp), url, "5")
            self.assertEqual(process.returncode, 2, process.stderr)
            response = json.loads((output / "responses/one.json").read_text())
            self.assertEqual(response["benchmark"]["error"], "unexpected_finish_reason")
            self.assertIsNone(response["benchmark"]["finish_reason"])
            self.assertEqual(response["choices"][0]["message"]["content"], "partial answer")
            self.assertFalse((output / "grades.json").exists())


if __name__ == "__main__":
    unittest.main()
