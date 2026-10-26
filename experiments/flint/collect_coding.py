"""Collect the existing twelve coding questions with hard per-task deadlines.

The suite path is an explicitly trusted Python fixture, not model output.
Questions remain unchanged. Saves serialized requests and streamed evidence;
never executes answers or invokes a grader. Review outputs before isolation.
"""
from __future__ import annotations

import argparse
import importlib.util
import json
from pathlib import Path
import re
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
import benchmark  # noqa: E402
import lab  # noqa: E402


def worker(request_file: Path) -> int:
    """Stream one frozen request; only the parent enforces the wall deadline."""
    spec = lab.read_json(request_file)
    started = time.monotonic()
    result = benchmark.stream_turn(
        benchmark.validate_endpoint(spec["endpoint"]), spec["payload"],
        request_file.with_suffix(".events.jsonl"), started,
        timeout=spec["deadline"])
    error = None
    if result["finish_reason"] not in ("stop", "length"):
        error = "unexpected_finish_reason"
    elif result["finish_reason"] == "stop" and (
            not result["content"].strip() or result["tool_calls"]):
        error = "empty_or_tool_only_answer"
    response = {"choices": [{"finish_reason": result["finish_reason"],
                             "message": {"role": "assistant",
                                         "content": result["content"],
                                         "reasoning_content": result["reasoning_content"],
                                         "tool_calls": result["tool_calls"]}}],
                "usage": result["usage"], "timings": result["timings"],
                "benchmark": {"wall_seconds": time.monotonic()-started,
                              "finish_reason": result["finish_reason"],
                              "first_event_seconds": result["first_event_seconds"],
                              "first_content_seconds": result["first_final_seconds"],
                              "error": error}}
    lab.save_json(Path(spec["response_file"]), response)
    return 2 if error else 0


def collect(args: argparse.Namespace) -> int:
    """Freeze trusted tasks and stop collection after a timeout/transport error."""
    endpoint = benchmark.validate_endpoint(args.endpoint)
    # Longer owner-authorized diagnostics must not silently enter the scorecard.
    extended = args.extended_diagnostic
    maximum = 21600 if extended else 1200
    if not 0 < args.deadline <= maximum:
        raise ValueError(f"Whole-task deadline must be 1..{maximum} seconds; "
                         "longer runs require --extended-diagnostic")
    module_spec = importlib.util.spec_from_file_location("frozen_suite", args.suite_file)
    module = importlib.util.module_from_spec(module_spec)
    module_spec.loader.exec_module(module)
    tasks = module.TASKS
    if args.tasks:
        selected = set(args.tasks.split(","))
        if not selected <= {task["id"] for task in tasks}:
            raise ValueError("Unknown task identifier")
        tasks = [task for task in tasks if task["id"] in selected]
    run = args.output.resolve()
    run.mkdir(parents=True, exist_ok=False)
    (run / "responses").mkdir()
    (run / "requests").mkdir()
    summary = {"model": args.model, "endpoint": endpoint.removesuffix("/v1"),
               "cohort": "extended-diagnostic" if extended else "frozen-1200s",
               "max_tokens": args.max_tokens, "deadline": args.deadline,
               "temperature": args.temperature, "seed": args.seed,
               "collector_sha256": lab.digest(Path(__file__)),
               "suite_sha256": lab.digest(args.suite_file), "tasks": [],
               "questions": tasks, "grading": "Requires source review and isolated execution"}
    lab.save_json(run / "collect.json", summary)
    for task in tasks:
        task_id = task["id"]
        if not re.fullmatch(r"[a-z0-9_]+", task_id):
            raise ValueError("Unsafe task identifier")
        payload = {"model": args.model, "stream": True,
                   "stream_options": {"include_usage": True},
                   "max_tokens": args.max_tokens, "temperature": args.temperature,
                   "top_p": 0.95, "top_k": 20, "min_p": 0,
                   "seed": args.seed, "cache_prompt": False,
                   "messages": [{"role": "user", "content": task["prompt"]}]}
        response_file = run / "responses" / (task_id + ".json")
        request_file = run / "requests" / (task_id + ".json")
        lab.save_json(request_file, {"endpoint": endpoint, "payload": payload,
                                    "deadline": args.deadline,
                                    "response_file": str(response_file)})
        started = time.monotonic()
        with request_file.with_suffix(".worker.log").open("xb") as log:
            child = subprocess.Popen([sys.executable, str(Path(__file__)),
                                      "--worker", str(request_file)],
                                     stdout=log, stderr=log,
                                     creationflags=getattr(subprocess, "CREATE_NO_WINDOW", 0))
            error = None
            try:
                code = child.wait(timeout=args.deadline)
                if code:
                    error = f"worker_exit_{code}"
            except subprocess.TimeoutExpired:
                child.kill()
                child.wait(timeout=5)
                error = "whole_prompt_deadline"
            except BaseException:
                child.kill()
                child.wait(timeout=5)
                raise
        if error:
            partial = lab.read_json(response_file) if response_file.exists() else {}
            details = partial.setdefault("benchmark", {
                "wall_seconds": time.monotonic()-started, "finish_reason": None})
            details["error"] = details.get("error") or error
            lab.save_json(response_file, partial)
        body = lab.read_json(response_file)
        row = {"task": task_id, "language": task["language"],
               **body["benchmark"],
               "decode_tok_s": (body.get("timings") or {}).get("predicted_per_second")}
        summary["tasks"].append(row)
        lab.save_json(run / "collect.json", summary)
        print(task_id, row["wall_seconds"], row["finish_reason"], error or "", flush=True)
        if error:
            summary["not_run"] = [t["id"] for t in tasks[len(summary["tasks"]):]]
            summary["stop_reason"] = "Check server cancellation/liveness before another request"
            lab.save_json(run / "collect.json", summary)
            return 2
    return 0


def main() -> int:
    """Parse explicit collection inputs or one parent-owned worker request."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--worker", type=Path)
    parser.add_argument("--suite-file", type=Path)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--model")
    parser.add_argument("--endpoint", default="http://127.0.0.1:8081/v1")
    parser.add_argument("--temperature", type=float, default=1.0)
    parser.add_argument("--max-tokens", type=int, default=16384)
    parser.add_argument("--deadline", type=float, default=1200)
    parser.add_argument("--extended-diagnostic", action="store_true",
                        help="Allow up to six hours, outside the frozen scorecard")
    parser.add_argument("--seed", type=int, default=73)
    parser.add_argument("--tasks", help="Explicit comma-separated subset; recorded in the manifest")
    args = parser.parse_args()
    if args.worker:
        return worker(args.worker)
    if not all((args.suite_file, args.output, args.model)):
        parser.error("--suite-file, --output and --model are required")
    return collect(args)


if __name__ == "__main__":
    raise SystemExit(main())
