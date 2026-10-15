"""Pinned local-model setup, guarded Windows launches and offline-friendly CLI."""
from __future__ import annotations

import argparse
import base64
import ctypes
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import shutil
import socket
import stat
import subprocess
import sys
import tempfile
import time
from typing import Any
import urllib.request
import zipfile

ROOT = Path(__file__).resolve().parent
GIB = 1024 ** 3


def read_json(path: Path) -> Any:
    """Read UTF-8 JSON, tolerating PowerShell's BOM."""
    return json.loads(path.read_text(encoding="utf-8-sig"))


def save_json(path: Path, value: Any) -> None:
    """Write a readable evidence artifact without overwriting its parent tree."""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2) + "\n", encoding="utf-8")


def digest(path: Path) -> str:
    """Hash large files with bounded memory."""
    with path.open("rb") as stream:
        return hashlib.file_digest(stream, "sha256").hexdigest()


def verify(path: Path, spec: dict) -> None:
    """Reject both incomplete files and unexpected publisher content."""
    if path.stat().st_size != spec["bytes"]:
        raise ValueError(f"Size mismatch: {path.name}")
    if digest(path) != spec["sha256"]:
        raise ValueError(f"SHA256 mismatch: {path.name}")


def download(spec: dict, target: Path) -> None:
    """Resume a pinned download, then publish only verified bytes."""
    target.parent.mkdir(parents=True, exist_ok=True)
    if target.exists():
        verify(target, spec)
        print(f"Already verified: {target.name}")
        return
    partial = target.with_name(target.name + ".part")
    offset = partial.stat().st_size if partial.exists() else 0
    if offset > spec["bytes"]:
        raise ValueError("Oversized partial; inspect it before retrying")
    if offset == spec["bytes"]:
        verify(partial, spec)
        partial.rename(target)
        return
    needed = spec["bytes"] - offset + 512 * 1024 ** 2
    if shutil.disk_usage(target.parent).free < needed:
        raise ValueError("Insufficient disk space for download plus headroom")
    headers = {"User-Agent": "local-coding-lab/0.1"}
    if offset:
        headers["Range"] = f"bytes={offset}-"
    request = urllib.request.Request(spec["url"], headers=headers)
    with urllib.request.urlopen(request, timeout=60) as response:
        if offset and response.status == 206:
            expected = f"bytes {offset}-"
            if not response.headers.get("Content-Range", "").startswith(expected):
                raise ValueError("Server returned the wrong resume range")
            mode = "ab"
        elif response.status == 200:
            offset, mode = 0, "wb"
            if shutil.disk_usage(target.parent).free < spec["bytes"] + 512 * 1024 ** 2:
                raise ValueError("Server cannot resume; need full download space")
        else:
            raise ValueError(f"Unexpected download status {response.status}")
        with partial.open(mode) as stream:
            total, announced = offset, time.monotonic()
            while block := response.read(4 * 1024 ** 2):
                total += len(block)
                if total > spec["bytes"]:
                    raise ValueError("Download exceeds pinned size")
                stream.write(block)
                if time.monotonic() - announced > 5:
                    print(f"{target.name}: {total / spec['bytes']:.1%}", flush=True)
                    announced = time.monotonic()
    verify(partial, spec)
    partial.rename(target)


def extract_zip(archive: Path, destination: Path) -> None:
    """Extract only ordinary, contained files; reject path tricks and collisions."""
    with zipfile.ZipFile(archive) as bundle:
        members = bundle.infolist()
        for item in members:
            path = PurePosixPath(item.filename.replace("\\", "/"))
            mode = item.external_attr >> 16
            if (path.is_absolute() or ".." in path.parts
                    or any(":" in part for part in path.parts)
                    or stat.S_ISLNK(mode)):
                raise ValueError("Unsafe path or symlink in archive")
            target = destination.joinpath(*path.parts)
            if not target.resolve().is_relative_to(destination.resolve()):
                raise ValueError("Archive escapes installation directory")
            if target.exists() and not item.is_dir():
                raise ValueError("Overlapping runtime archive files")
        if sum(item.file_size for item in members) > 8 * GIB:
            raise ValueError("Unexpected runtime extraction size")
        for item in members:
            target = destination.joinpath(*PurePosixPath(
                item.filename.replace("\\", "/")).parts)
            if item.is_dir():
                target.mkdir(parents=True, exist_ok=True)
            else:
                target.parent.mkdir(parents=True, exist_ok=True)
                with bundle.open(item) as src, target.open("xb") as dst:
                    shutil.copyfileobj(src, dst)


def runtime_path(data: Path) -> Path:
    """Keep this installation independent from existing llama.cpp folders."""
    return data / "runtime" / "b11562-cuda12.4"


def install_runtime(data: Path, apply: bool) -> None:
    """Install both pinned runtime and CUDA DLL archives into a new directory."""
    spec = read_json(ROOT / "catalog/runtime.json")
    target = runtime_path(data)
    print(json.dumps({"destination": str(target), "assets": spec["assets"]}, indent=2))
    if not apply:
        print("Plan only. Add --apply to download and install.")
        return
    if target.exists():
        raise ValueError("Runtime destination exists; will not overwrite it")
    archives = []
    for asset in spec["assets"]:
        archive = data / "downloads" / asset["filename"]
        download(asset, archive)
        archives.append(archive)
    target.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="runtime-", dir=target.parent) as tmp:
        stage = Path(tmp) / "contents"
        stage.mkdir()
        for archive in archives:
            extract_zip(archive, stage)
        if not list(stage.rglob("llama-server.exe")):
            raise ValueError("Runtime archive lacks llama-server.exe")
        save_json(stage / "installation.json", spec)
        stage.rename(target)
    print(f"Installed {target}")


def model_spec(key: str) -> dict:
    """Resolve a model to an immutable publisher revision and file hash."""
    model = dict(read_json(ROOT / "catalog/models.json")["models"][key])
    model["url"] = (f"https://huggingface.co/{model['repo']}/resolve/"
                    f"{model['revision']}/{model['filename']}")
    return model


def memory_snapshot() -> dict:
    """Read Windows physical RAM and GPU 0; never count shared RAM as VRAM."""
    result: dict = {"time": time.time(), "platform": sys.platform}
    if sys.platform == "win32":
        class Memory(ctypes.Structure):
            _fields_ = [("length", ctypes.c_ulong), ("load", ctypes.c_ulong)] + [
                (name, ctypes.c_ulonglong) for name in (
                    "total", "free", "page_total", "page_free", "virt_total",
                    "virt_free", "extended")]
        memory = Memory()
        memory.length = ctypes.sizeof(memory)
        if not ctypes.windll.kernel32.GlobalMemoryStatusEx(ctypes.byref(memory)):
            raise OSError("Windows physical-memory query failed")
        result.update(ram_total_gib=memory.total / GIB, ram_free_gib=memory.free / GIB)
    try:
        command = ["nvidia-smi", "--id=0", "--query-gpu=memory.total,memory.free,temperature.gpu,name,driver_version", "--format=csv,noheader,nounits"]
        query = subprocess.run(command, capture_output=True, text=True,
                               timeout=5, check=True)
        values = [value.strip() for value in query.stdout.splitlines()[0].split(",")]
        result.update(vram_total_mib=float(values[0]), vram_free_mib=float(values[1]),
                      gpu_c=float(values[2]), gpu=values[3], driver=values[4])
    except (OSError, subprocess.SubprocessError, ValueError, IndexError):
        result["gpu_error"] = "Cannot read GPU 0 through nvidia-smi"
    return result


def check_memory(snapshot: dict, profile: dict, loading: bool) -> None:
    """Fail closed if telemetry is missing or the measured floor is crossed."""
    prefix = "load_min" if loading else "stop_min"
    for field in ("ram_free_gib", "vram_free_mib"):
        threshold = profile[f"{prefix}_{field}"]
        if field not in snapshot or snapshot[field] < threshold:
            raise ValueError(f"{field} below {threshold} or unavailable")
    if snapshot.get("gpu_c", 100) >= profile["stop_gpu_c"]:
        raise ValueError("GPU temperature reached the profile stop threshold")


def process_memory(pid: int) -> dict:
    """Measure resident/private bytes of the owned Windows server process."""
    if sys.platform != "win32":
        return {}
    from ctypes import wintypes

    class Counters(ctypes.Structure):
        _fields_ = [("cb", wintypes.DWORD), ("faults", wintypes.DWORD)] + [
            (name, ctypes.c_size_t) for name in (
                "peak_working", "working", "peak_paged", "paged",
                "peak_nonpaged", "nonpaged", "pagefile", "peak_pagefile",
                "private")]

    kernel = ctypes.WinDLL("kernel32", use_last_error=True)
    psapi = ctypes.WinDLL("psapi", use_last_error=True)
    kernel.OpenProcess.argtypes = [wintypes.DWORD, wintypes.BOOL, wintypes.DWORD]
    kernel.OpenProcess.restype = wintypes.HANDLE
    kernel.CloseHandle.argtypes = [wintypes.HANDLE]
    psapi.GetProcessMemoryInfo.argtypes = [wintypes.HANDLE,
                                          ctypes.POINTER(Counters), wintypes.DWORD]
    handle = kernel.OpenProcess(0x410, False, pid)
    if not handle:
        return {"process_memory_error": "Process exited or access unavailable"}
    try:
        counters = Counters()
        counters.cb = ctypes.sizeof(counters)
        if not psapi.GetProcessMemoryInfo(handle, ctypes.byref(counters), counters.cb):
            return {"process_memory_error": "GetProcessMemoryInfo failed"}
        return {"process_working_set_gib": counters.working / GIB,
                "process_private_gib": counters.private / GIB,
                "process_peak_working_set_gib": counters.peak_working / GIB}
    finally:
        kernel.CloseHandle(handle)


def build_command(exe: Path, model: Path, profile: dict, port: int) -> list[str]:
    """Build an argument array, never interpolate paths into shell commands."""
    return [str(exe), "-m", str(model), "--host", "127.0.0.1", "--port", str(port),
            "--alias", profile["alias"], "--parallel", "1", *profile["args"]]


def check_hardware_events(since: str) -> None:
    """Stop on newly logged WHEA events, without diagnosing their cause."""
    script = (
        "$ErrorActionPreference='Stop'; "
        f"$since=[DateTime]::Parse('{since}').ToLocalTime(); "
        "try { $events=@(Get-WinEvent -FilterHashtable @{LogName='System'; "
        "ProviderName='Microsoft-Windows-WHEA-Logger'; StartTime=$since} "
        "-ErrorAction Stop) } catch { "
        "if ($_.FullyQualifiedErrorId -like 'NoMatchingEventsFound*') { exit 0 }; exit 3 }; "
        "if ($events.Count -gt 0) { exit 2 }; exit 0"
    )
    encoded = base64.b64encode(script.encode("utf-16-le")).decode("ascii")
    result = subprocess.run(["powershell.exe", "-NoProfile", "-NonInteractive",
                             "-EncodedCommand", encoded], capture_output=True,
                            timeout=10, creationflags=subprocess.CREATE_NO_WINDOW)
    if result.returncode == 2:
        raise ValueError("New Windows WHEA hardware event; preserve logs before another load")
    if result.returncode:
        raise ValueError("Could not check Windows hardware events")


def check_single_server() -> None:
    """Reject an existing llama-server on any port; never stop another process."""
    script = ("$ErrorActionPreference='Stop'; try { "
              "$servers=@(Get-CimInstance Win32_Process -Filter \"Name='llama-server.exe'\"); "
              "if ($servers.Count) { exit 2 }; exit 0 } catch { exit 3 }")
    encoded = base64.b64encode(script.encode('utf-16-le')).decode('ascii')
    result = subprocess.run(['powershell.exe', '-NoProfile', '-NonInteractive',
                             '-EncodedCommand', encoded], capture_output=True,
                            timeout=10, creationflags=subprocess.CREATE_NO_WINDOW)
    if result.returncode:
        raise ValueError('Another llama-server exists or process inventory is unavailable')


def process_gpu_snapshot(pid: int) -> dict:
    """Capture WDDM dedicated/shared usage without treating shared RAM as VRAM."""
    if sys.platform != 'win32' or not isinstance(pid, int) or pid <= 0:
        return {'error': 'Windows process ID required'}
    script = ("$ErrorActionPreference='Stop'; "
              "@(Get-CimInstance Win32_PerfFormattedData_GPUPerformanceCounters_GPUProcessMemory | "
              f"Where-Object Name -like 'pid_{pid}_*phys_0' | "
              "Select-Object Name,DedicatedUsage,SharedUsage) | ConvertTo-Json -Compress")
    encoded = base64.b64encode(script.encode('utf-16-le')).decode('ascii')
    try:
        result = subprocess.run(['powershell.exe', '-NoProfile', '-NonInteractive',
                                 '-EncodedCommand', encoded], capture_output=True,
                                text=True, timeout=15, check=True,
                                creationflags=subprocess.CREATE_NO_WINDOW)
        value = json.loads(result.stdout)
        rows = value if isinstance(value, list) else [value]
        return {'time': time.time(), 'pid': pid, 'rows': rows,
                'dedicated_gib': sum(row['DedicatedUsage'] for row in rows)/GIB,
                'shared_gib': sum(row['SharedUsage'] for row in rows)/GIB,
                'note': 'Shared usage overlaps host RAM; do not add it to process working set.'}
    except (ValueError, TypeError, KeyError, OSError, subprocess.SubprocessError):
        return {'time': time.time(), 'pid': pid, 'error': 'WDDM counters unavailable'}


def run_server(args: argparse.Namespace, data: Path) -> None:
    """Own one foreground session, monitoring resources until it stops."""
    profile = read_json(ROOT / "profiles" / (args.profile + ".json"))
    if not profile["locally_tested"] and not args.experimental:
        raise ValueError("Untested profile: inspect it, then use --experimental")
    spec = model_spec(profile["model"])
    model = Path(args.model_path).resolve() if args.model_path else data / "models" / spec["filename"]
    if args.runtime_dir:
        runtime = Path(args.runtime_dir).resolve()
    else:
        runtime = runtime_path(data)
    executables = list(runtime.rglob("llama-server.exe"))
    if len(executables) != 1:
        raise ValueError("Expected exactly one llama-server.exe in runtime directory")
    command = build_command(executables[0], model, profile, args.port)
    print(subprocess.list2cmdline(command))
    if not args.apply:
        print("Plan only; --apply starts the server. Ctrl+C stops only this child.")
        return
    if sys.platform != "win32":
        raise ValueError("Guarded CUDA launcher currently supports Windows only")
    stop_file = Path(args.stop_file).resolve() if args.stop_file else None
    if stop_file and stop_file.exists():
        raise ValueError("Stop file already exists; choose a fresh experiment path")
    verify(model, spec)
    since = datetime.now(timezone.utc).isoformat()
    check_hardware_events(since)
    check_memory(memory_snapshot(), profile, loading=True)
    check_single_server()
    with socket.socket() as probe:
        probe.bind(("127.0.0.1", args.port))
    help_text = subprocess.run([str(executables[0]), "--help"], capture_output=True,
                               text=True, encoding="utf-8", errors="replace", timeout=30)
    for flag in profile["args"]:
        if flag.startswith("--") and flag not in help_text.stdout + help_text.stderr:
            raise ValueError(f"Runtime does not advertise {flag}")
    version = subprocess.run([str(executables[0]), "--version"], capture_output=True,
                             text=True, encoding="utf-8", errors="replace", timeout=30)
    if "b2f036c0f" not in version.stdout + version.stderr:
        raise ValueError("Runtime commit differs from pinned b11562; create a reviewed profile/catalog update")
    run_dir = data / "runs" / time.strftime("server-%Y%m%d-%H%M%S")
    run_dir.mkdir(parents=True, exist_ok=False)
    save_json(run_dir / "launch.json", {"command": command, "profile": profile})
    env = dict(os.environ)
    env["LLAMA_ARG_CHAT_TEMPLATE_KWARGS"] = json.dumps(profile["template_kwargs"])
    child = None
    next_events = time.monotonic() + 30
    outcome = {"status": "exited"}
    try:
        with (run_dir / "server.log").open("wb") as log:
            child = subprocess.Popen(command, stdout=log, stderr=log, env=env,
                                     creationflags=subprocess.CREATE_NO_WINDOW)
            save_json(run_dir / "process.json", {"pid": child.pid,
                      "launcher_pid": os.getpid(), "stop_file": str(stop_file) if stop_file else None})
            print(f"PID {child.pid}; loading. Logs: {run_dir}; health at localhost:{args.port}/health")
            with (run_dir / "memory.jsonl").open("a", encoding="utf-8") as telemetry:
                while child.poll() is None:
                    if stop_file and stop_file.exists():
                        outcome = {"status": "requested_stop"}
                        break
                    snapshot = memory_snapshot()
                    snapshot.update(process_memory(child.pid))
                    telemetry.write(json.dumps(snapshot) + "\n")
                    telemetry.flush()
                    check_memory(snapshot, profile, loading=False)
                    if time.monotonic() >= next_events:
                        check_hardware_events(since)
                        next_events = time.monotonic() + 30
                    time.sleep(5)
            if child.returncode:
                raise ValueError(f"llama-server exited {child.returncode}; see {run_dir}")
    except BaseException as exc:
        outcome = {"status": "stopped", "reason": str(exc) or type(exc).__name__}
        raise
    finally:
        if child is not None and child.poll() is None:
            child.terminate()
            try:
                child.wait(timeout=10)
            except subprocess.TimeoutExpired:
                child.kill()
                child.wait(timeout=10)
        save_json(run_dir / "stop.json", outcome)


def main() -> int:
    """Dispatch explicit lab operations; downloads and launches default to plans."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--data-dir", default=str(ROOT / "local-data"))
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("doctor", help="Read RAM/VRAM; does not load a model")
    sub.add_parser("list", help="List pinned downloadable candidates")
    runtime = sub.add_parser("install-runtime")
    runtime.add_argument("--apply", action="store_true")
    model = sub.add_parser("download-model")
    model.add_argument("model", choices=list(read_json(ROOT / "catalog/models.json")["models"]))
    model.add_argument("--apply", action="store_true")
    run = sub.add_parser("run")
    run.add_argument("--profile", choices=[p.stem for p in (ROOT / "profiles").glob("*.json")], required=True)
    run.add_argument("--model-path")
    run.add_argument("--runtime-dir")
    run.add_argument("--port", type=int, default=8080)
    run.add_argument("--apply", action="store_true")
    run.add_argument("--experimental", action="store_true")
    run.add_argument("--stop-file", help="Fresh file path; create it to stop only this session")
    args = parser.parse_args()
    data = Path(args.data_dir).resolve()
    try:
        if args.command == "doctor":
            print(json.dumps(memory_snapshot(), indent=2))
        elif args.command == "list":
            for key, value in read_json(ROOT / "catalog/models.json")["models"].items():
                print(f"{key:20s} {value['bytes'] / GIB:6.3f} GiB  {value['status']}")
        elif args.command == "install-runtime":
            install_runtime(data, args.apply)
        elif args.command == "download-model":
            spec = model_spec(args.model)
            print(json.dumps(spec, indent=2))
            if args.apply:
                download(spec, data / "models" / spec["filename"])
            else:
                print("Plan only. Add --apply to download.")
        elif args.command == "run":
            run_server(args, data)
    except (OSError, ValueError, KeyError, subprocess.SubprocessError) as exc:
        print(f"Stopped: {exc}", file=sys.stderr)
        return 1
    except KeyboardInterrupt:
        print("Stopped this lab session.")
        return 130
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
