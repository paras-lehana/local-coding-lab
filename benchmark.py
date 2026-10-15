"""Collect one bounded, frozen local coding benchmark; never execute its code."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import time
from typing import Any
import urllib.parse
import urllib.request

from lab import ROOT, read_json, save_json


def validate_endpoint(url: str) -> str:
    """Allow only explicit loopback HTTP servers; no external or paid APIs."""
    parsed = urllib.parse.urlsplit(url)
    if (parsed.scheme != "http" or parsed.hostname not in ("127.0.0.1", "::1", "localhost")
            or parsed.username or parsed.password or parsed.query or parsed.fragment):
        raise ValueError("Use a loopback HTTP endpoint without credentials")
    if parsed.path.rstrip("/") != "/v1":
        raise ValueError("Endpoint path must be /v1")
    return url.rstrip("/")


def fixture_snapshot() -> dict[str, str]:
    """Freeze public files, excluding the rubric and everything outside the fixture."""
    directory = ROOT / "benchmarks/fixtures/router-v1"
    return {path.relative_to(directory).as_posix(): path.read_text(encoding="utf-8")
            for path in sorted(directory.rglob("*"))
            if path.is_file() and path.suffix in (".md", ".py")}


def read_fixture(path: str, sources: dict[str, str]) -> str:
    """Read exact allowlisted names only; no filesystem path resolution from tools."""
    if not isinstance(path, str) or path not in sources:
        return json.dumps({"error": "Path unavailable in the frozen fixture"})
    numbered = "\n".join(f"{i}: {line}" for i, line in enumerate(sources[path].splitlines(), 1))
    return json.dumps({"path": path, "content": numbered})


class NoRedirect(urllib.request.HTTPRedirectHandler):
    """Prevent a local endpoint from redirecting benchmark files elsewhere."""

    def redirect_request(self, req: Any, fp: Any, code: int, msg: str,
                         headers: Any, newurl: str) -> None:
        """Refuse redirects even if the original URL is loopback."""
        raise ValueError("Benchmark redirects are disabled")


def stream_turn(endpoint: str, payload: dict, output: Path, started: float) -> dict:
    """Collect streamed reasoning, final text and fragmented tool calls separately."""
    request = urllib.request.Request(endpoint + "/chat/completions",
                                     data=json.dumps(payload).encode(),
                                     headers={"Content-Type": "application/json"})
    opener = urllib.request.build_opener(urllib.request.ProxyHandler({}), NoRedirect())
    text, reasoning, calls = [], [], {}
    result: dict = {"first_event_seconds": None, "first_final_seconds": None,
                    "finish_reason": None, "usage": None, "timings": None}
    with output.open("w", encoding="utf-8") as evidence:
        # The parent enforces the whole run deadline, including silent prefill.
        with opener.open(request, timeout=1200) as response:
            for line in response:
                decoded = line.decode("utf-8").strip()
                if not decoded.startswith("data:"):
                    continue
                data = decoded[5:].strip()
                if data == "[DONE]":
                    break
                event = json.loads(data)
                elapsed = time.monotonic() - started
                evidence.write(json.dumps({"seconds": elapsed, "event": event}) + "\n")
                evidence.flush()
                if "error" in event:
                    raise ValueError("Server returned a streaming error; see evidence")
                if result["first_event_seconds"] is None:
                    result["first_event_seconds"] = elapsed
                if event.get("usage"):
                    result["usage"] = event["usage"]
                if event.get("timings"):
                    result["timings"] = event["timings"]
                for choice in event.get("choices", []):
                    delta = choice.get("delta", {})
                    if delta.get("content"):
                        if result["first_final_seconds"] is None:
                            result["first_final_seconds"] = elapsed
                        text.append(delta["content"])
                    thought = delta.get("reasoning_content", delta.get("reasoning"))
                    if thought:
                        reasoning.append(thought)
                    for fragment in delta.get("tool_calls", []):
                        index = fragment["index"]
                        item = calls.setdefault(index, {"id": "", "type": "function",
                                                       "function": {"name": "", "arguments": ""}})
                        if fragment.get("id"):
                            item["id"] = fragment["id"]
                        for key in ("name", "arguments"):
                            item["function"][key] += fragment.get("function", {}).get(key, "")
                    if choice.get("finish_reason"):
                        result["finish_reason"] = choice["finish_reason"]
    result.update(content="".join(text), reasoning_content="".join(reasoning),
                  tool_calls=[calls[index] for index in sorted(calls)])
    return result


def worker(run: Path) -> int:
    """Execute an entire multi-tool prompt; the parent owns the hard deadline."""
    manifest = read_json(run / "manifest.json")
    sources = read_json(run / "sources.json")
    question = (run / "question.txt").read_text(encoding="utf-8")
    started = time.monotonic()
    if manifest["mode"] == "inline":
        question += "\n\nSUPPLIED FILES\n" + "\n".join(
            read_fixture(path, sources) for path in sources)
    else:
        question += "\nAvailable paths:\n" + "\n".join(sources)
    messages = [{"role": "system", "content": "Answer from the provided project. Tools are read-only. Do not invent missing facts."},
                {"role": "user", "content": question}]
    turns, tool_log = [], []
    tool = {"type": "function", "function": {"name": "read_file",
            "description": "Read a file from this frozen project only.",
            "parameters": {"type": "object", "properties": {"path": {"type": "string"}},
                           "required": ["path"], "additionalProperties": False}}}
    for turn_index in range(24):
        payload = {"model": manifest["model"], "messages": messages, "stream": True,
                   "stream_options": {"include_usage": True}, "seed": manifest["seed"],
                   "temperature": manifest["temperature"], "max_tokens": manifest["max_tokens"]}
        if manifest["reasoning_budget"] is not None:
            payload["reasoning_budget_tokens"] = manifest["reasoning_budget"]
        if manifest["mode"] == "tools":
            payload["tools"] = [tool]
        save_json(run / f"request-{turn_index:02d}.json", payload)
        result = stream_turn(manifest["endpoint"], payload,
                             run / f"stream-{turn_index:02d}.jsonl", started)
        turns.append(result)
        save_json(run / "turns.json", turns)
        if result["finish_reason"] not in ("stop", "tool_calls"):
            save_json(run / "result.json", {"status": "incomplete", "scored": False,
                      "reason": result["finish_reason"], "wall_seconds": time.monotonic() - started})
            return 2
        if not result["tool_calls"]:
            status = "completed" if result["content"].strip() else "empty"
            save_json(run / "result.json", {"status": status, "scored": False,
                      "note": "Source review and isolated behavioral tests still required",
                      "wall_seconds": time.monotonic() - started, "turn_count": len(turns)})
            (run / "answer.txt").write_text(result["content"], encoding="utf-8")
            return 0 if status == "completed" else 2
        message = {"role": "assistant", "content": result["content"],
                   "tool_calls": result["tool_calls"]}
        if result["reasoning_content"]:
            message["reasoning_content"] = result["reasoning_content"]
        messages.append(message)
        for call in result["tool_calls"]:
            try:
                if call["function"]["name"] != "read_file":
                    raise ValueError("Unknown tool")
                arguments = json.loads(call["function"]["arguments"])
                response = read_fixture(arguments.get("path"), sources)
            except (ValueError, TypeError, AttributeError):
                response = json.dumps({"error": "Invalid read_file call"})
            tool_log.append({"call": call, "response": json.loads(response)})
            save_json(run / "tools.json", tool_log)
            messages.append({"role": "tool", "tool_call_id": call["id"], "content": response})
    save_json(run / "result.json", {"status": "tool_turn_limit", "scored": False})
    return 2


def collect(args: argparse.Namespace) -> int:
    """Freeze first, then start a disposable network worker with one time limit."""
    endpoint = validate_endpoint(args.endpoint)
    if not 0 < args.deadline <= 1200:
        raise ValueError("Deadline must be >0 and <=1200 seconds")
    if not 1 <= args.max_tokens <= 32768:
        raise ValueError("max-tokens must be 1..32768")
    run = Path(args.output).resolve()
    run.mkdir(parents=True, exist_ok=False)
    sources = fixture_snapshot()
    question = (ROOT / "benchmarks/questions/router-v1.txt").read_text(encoding="utf-8")
    manifest = {"fixture": "router-v1", "delivery": "frozen-snapshot",
                "endpoint": endpoint, "model": args.model, "mode": args.mode,
                "seed": args.seed, "temperature": args.temperature,
                "max_tokens": args.max_tokens, "reasoning_budget": args.reasoning_budget,
                "deadline_seconds": args.deadline,
                "question_sha256": hashlib.sha256(question.encode()).hexdigest(),
                "source_sha256": {p: hashlib.sha256(t.encode()).hexdigest() for p, t in sources.items()}}
    save_json(run / "manifest.json", manifest)
    save_json(run / "sources.json", sources)
    (run / "question.txt").write_text(question, encoding="utf-8")
    if args.prepare_only:
        print(f"Frozen inputs: {run}; no endpoint request sent")
        return 0
    started = time.monotonic()
    with (run / "worker.log").open("wb") as log:
        process = subprocess.Popen([sys.executable, str(Path(__file__).resolve()),
                                    "--worker", str(run)], stdout=log, stderr=log)
        try:
            code = process.wait(timeout=args.deadline)
        except subprocess.TimeoutExpired:
            process.kill()
            process.wait(timeout=5)
            save_json(run / "result.json", {"status": "deadline", "scored": False,
                      "wall_seconds": time.monotonic() - started})
            code = 124
        except KeyboardInterrupt:
            process.kill()
            process.wait(timeout=5)
            save_json(run / "result.json", {"status": "cancelled", "scored": False})
            raise
    if not (run / "result.json").exists():
        save_json(run / "result.json", {"status": "worker_error", "scored": False,
                  "exit_code": code, "wall_seconds": time.monotonic() - started})
    print(f"Evidence: {run}; result: {read_json(run / 'result.json')['status']}")
    return code


def main() -> int:
    """Parse a bounded local evaluation request; default to tool delivery."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--endpoint", default="http://127.0.0.1:8080/v1")
    parser.add_argument("--model", default="qwen36-lab")
    parser.add_argument("--mode", choices=("inline", "tools"), default="tools")
    parser.add_argument("--deadline", type=float, default=1200)
    parser.add_argument("--max-tokens", type=int, default=8192)
    parser.add_argument("--seed", type=int, default=73)
    parser.add_argument("--temperature", type=float, default=0.6)
    parser.add_argument("--reasoning-budget", type=int)
    parser.add_argument("--output", default=str(ROOT / "local-data" / time.strftime("benchmark-%Y%m%d-%H%M%S")))
    parser.add_argument("--prepare-only", action="store_true")
    parser.add_argument("--worker", type=Path, help=argparse.SUPPRESS)
    args = parser.parse_args()
    try:
        return worker(args.worker) if args.worker else collect(args)
    except (OSError, ValueError) as exc:
        print(f"Benchmark stopped: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
