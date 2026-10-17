"""Run one explicitly configured Strata experiment in an owned Windows job.

Requires Strata's environment (psutil) and reviewed winjob helper. Keep its
configuration, logs and stop file private. Never changes drivers or clocks.
"""
from __future__ import annotations

import argparse
import datetime
import importlib.util
import json
import os
from pathlib import Path
import subprocess
import sys
import time

import psutil

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
import lab


def save(path: Path, data: dict) -> None:
    """Persist a checkpoint without exposing the parent environment."""
    path.write_text(json.dumps(data, indent=2), encoding="utf-8")


def run(config_path: Path, output: Path) -> int:
    """Own only the new process tree and terminate it on a guard or stop file."""
    config = json.loads(config_path.read_text(encoding="utf-8"))
    output.mkdir(parents=True, exist_ok=False)
    save(output / "config.json", config)
    command = config["command"]
    if not command or not Path(command[0]).is_absolute():
        raise ValueError("Use an explicit executable path")
    policy = config["guard"]
    try:
        lab.check_single_server()
        for process in psutil.process_iter(["pid", "name"]):
            if (process.info["name"] or "").lower() in {"strata.exe", "strata-q36.exe"}:
                raise ValueError(f"Another Strata engine exists (PID {process.info['pid']})")
        initial = lab.memory_snapshot()
        lab.check_memory(initial, policy, loading=True)
    except Exception as error:
        save(output / "result.json", {"reason": f"preflight: {type(error).__name__}: {error}",
                                      "code": 1, "seconds": 0, "started": False})
        return 1
    since = datetime.datetime.now(datetime.timezone.utc).isoformat()
    source = Path(config["strata_root"]) / "serve" / "winjob.py"
    spec = importlib.util.spec_from_file_location("strata_job", source)
    job = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(job)
    env = os.environ.copy()
    env.update(config.get("env", {}))
    env["PATH"] = os.pathsep.join(config.get("lib_dirs", [])) + os.pathsep + env["PATH"]
    started = time.monotonic()
    child = None
    reason = "process exited"
    code = 1
    stop_code = 0
    limited = set()
    try:
        with (output / "stdout.log").open("wb") as stdout, (output / "stderr.log").open("wb") as stderr:
            child = subprocess.Popen(command, cwd=config["strata_root"], env=env,
                                     stdin=subprocess.DEVNULL, stdout=stdout,
                                     stderr=stderr, creationflags=subprocess.CREATE_NO_WINDOW)
            if not job.contain(child):
                child.kill()
                child.wait(timeout=10)
                raise RuntimeError("Windows job ownership failed; child stopped")
            try:
                created = psutil.Process(child.pid).create_time()
            except psutil.NoSuchProcess:
                created = None
            save(output / "process.json", {"pid": child.pid, "created": created,
                                            "command": command, "initial": initial, "since": since})
            last_events = 0.0
            while child.poll() is None:
                if (output / "stop.request").exists():
                    reason = "explicit stop"
                    break
                if time.monotonic() - started > config.get("max_seconds", 3600):
                    reason = "experiment wall deadline"
                    stop_code = 124
                    break
                processes = [psutil.Process(child.pid)]
                processes.extend(processes[0].children(recursive=True))
                for proc in processes:
                    try:
                        identity = (proc.pid, proc.create_time())
                        maximum = config.get("working_set_limits_gib", {}).get(proc.name().lower())
                    except psutil.NoSuchProcess:
                        continue
                    if maximum is not None and identity not in limited:
                        receipt = lab.limit_owned_working_set(proc.pid, float(maximum))
                        receipt["created"] = identity[1]
                        with (output / "working-set.jsonl").open("a", encoding="utf-8") as log:
                            log.write(json.dumps(receipt) + "\n")
                        limited.add(identity)
                sample = lab.memory_snapshot()
                sample["owned"] = []
                for proc in processes:
                    try:
                        sample["owned"].append({"pid": proc.pid, "created": proc.create_time(),
                                                "name": proc.name(), "rss_gib": proc.memory_info().rss / lab.GIB})
                    except psutil.NoSuchProcess:
                        pass
                with (output / "telemetry.jsonl").open("a", encoding="utf-8") as log:
                    log.write(json.dumps(sample) + "\n")
                lab.check_memory(sample, policy, loading=False)
                if time.monotonic() - last_events > 20:
                    lab.check_hardware_events(since)
                    last_events = time.monotonic()
                time.sleep(1)
            code = child.poll() if child.poll() is not None else stop_code
    except psutil.NoSuchProcess as error:
        # A fast native loader failure can exit between poll() and telemetry.
        code = child.poll() if child is not None else None
        reason = "process exited during telemetry" if code is not None else f"guard/error: {error}"
        code = code if code is not None else 1
    except Exception as error:
        reason = f"guard/error: {type(error).__name__}: {error}"
        code = 1
    finally:
        # Closing our only job handle ends exactly this tree, including a
        # server's engine and any Windows venv launcher child.
        if getattr(job, "_job", None):
            import ctypes
            kernel = ctypes.WinDLL("kernel32", use_last_error=True)
            kernel.CloseHandle.argtypes = [ctypes.c_void_p]
            kernel.CloseHandle(job._job)
            job._job = None
        if child is not None:
            try:
                child.wait(timeout=15)
            except subprocess.TimeoutExpired:
                reason += "; owned root did not exit within 15 seconds"
                code = 1
        save(output / "result.json", {"reason": reason, "code": code,
                                      "seconds": time.monotonic() - started,
                                      "final": lab.memory_snapshot()})
    return int(code or 0)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    raise SystemExit(run(args.config, args.output))
