"""Check Windows job cleanup with harmless children; never load a model.

Run using Strata's Python environment, with --strata-root and a new --output.
Requires an NVIDIA memory query, and refuses any running inference server.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import shutil
import subprocess
import sys

import guard


def main() -> int:
    """Exercise a preflight refusal and an owned-child stop without touching peers."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--strata-root", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    root = args.output.resolve()
    root.mkdir(parents=True, exist_ok=False)
    impossible = guard.lab.memory_snapshot()["ram_total_gib"] + 1
    config = {
        "strata_root": str(args.strata_root.resolve()),
        "command": [sys.executable, "-c", "import time; time.sleep(60)"],
        "lib_dirs": [],
        "guard": {"load_min_ram_free_gib": impossible,
                  "load_min_vram_free_mib": 0,
                  "load_min_commit_available_gib": 2,
                  "stop_min_ram_free_gib": impossible,
                  "stop_min_commit_available_gib": 1,
                  "stop_min_vram_free_mib": 0, "stop_gpu_c": 100},
        "max_seconds": 20,
    }
    path = root / "config.json"
    guard.save(path, config)
    code = guard.run(path, root / "preflight")
    result = json.loads((root / "preflight/result.json").read_text())
    assert code == 1 and result.get("started") is False, result
    assert "ram_free_gib" in result["reason"], result
    assert not (root / "preflight/process.json").exists()
    config["guard"]["load_min_ram_free_gib"] = 0
    guard.save(path, config)
    peer = subprocess.Popen([sys.executable, "-c", "import time; time.sleep(60)"],
                            creationflags=subprocess.CREATE_NO_WINDOW)
    try:
        code = guard.run(path, root / "owned-stop")
        result = json.loads((root / "owned-stop/result.json").read_text())
        assert code == 1 and "ram_free_gib" in result["reason"], result
        assert (root / "owned-stop/process.json").exists()
        assert peer.poll() is None, "Unrelated child was stopped"
        assert "did not exit" not in result["reason"], result
        config["guard"]["stop_min_ram_free_gib"] = 2.5
        config["max_seconds"] = 0.05
        guard.save(path, config)
        code = guard.run(path, root / "deadline")
        result = json.loads((root / "deadline/result.json").read_text())
        assert code == 124 and result["reason"] == "experiment wall deadline", result
        assert peer.poll() is None, "Deadline cleanup stopped an unrelated child"
        # Keep a harmless frontend alive after its mock native process exits.
        # The guard must close its owned tree instead of waiting for a retry.
        native = shutil.which("powershell.exe")
        if not native or not Path(native).is_absolute():
            raise RuntimeError("Absolute Windows PowerShell path unavailable")
        config["stable_native_executable"] = native
        config["native_start_timeout_seconds"] = 0.05
        config["max_seconds"] = 30
        guard.save(path, config)
        code = guard.run(path, root / "native-missing")
        result = json.loads((root / "native-missing/result.json").read_text())
        assert code == 1 and "native engine did not start" in result["reason"], result
        assert not (root / "native-missing/native-process.json").exists()
        assert peer.poll() is None, "Missing-native cleanup stopped a peer"
        native_command = [native, "-NoProfile", "-NonInteractive", "-Command",
                          "Start-Sleep -Seconds 4"]
        frontend = (
            "import subprocess,time; "
            f"subprocess.Popen({native_command!r}, "
            "creationflags=subprocess.CREATE_NO_WINDOW).wait(); "
            "time.sleep(60)"
        )
        config["command"] = [sys.executable, "-c", frontend]
        config["stable_native_executable"] = native
        config["native_start_timeout_seconds"] = 15
        config["max_seconds"] = 30
        guard.save(path, config)
        code = guard.run(path, root / "native-exit")
        result = json.loads((root / "native-exit/result.json").read_text())
        assert code == 1 and "native engine exited" in result["reason"], result
        assert (root / "native-exit/native-process.json").exists()
        assert "did not exit" not in result["reason"], result
        assert peer.poll() is None, "Native-exit cleanup stopped a peer"
        guard.save(root / "checks.json", {"preflight_receipt": "pass",
                                          "owned_job_stop": "pass",
                                          "deadline_nonzero": "pass",
                                          "native_missing_is_bounded": "pass",
                                          "native_exit_stops_frontend": "pass",
                                          "unrelated_child_survives": "pass"})
        print("PASS: preflight, owned stop, deadline, native exit, peer survives")
        return 0
    finally:
        if peer.poll() is None:
            peer.terminate()
        peer.wait(timeout=10)


if __name__ == "__main__":
    raise SystemExit(main())
