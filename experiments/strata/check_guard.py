"""Check Windows job cleanup with harmless children; never load a model.

Run using Strata's Python environment, with --strata-root and a new --output.
Requires an NVIDIA memory query, and refuses any running inference server.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
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
                  "stop_min_ram_free_gib": impossible,
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
        config["guard"]["stop_min_ram_free_gib"] = 0
        config["max_seconds"] = 0.05
        guard.save(path, config)
        code = guard.run(path, root / "deadline")
        result = json.loads((root / "deadline/result.json").read_text())
        assert code == 124 and result["reason"] == "experiment wall deadline", result
        assert peer.poll() is None, "Deadline cleanup stopped an unrelated child"
        guard.save(root / "checks.json", {"preflight_receipt": "pass",
                                          "owned_job_stop": "pass",
                                          "deadline_nonzero": "pass",
                                          "unrelated_child_survives": "pass"})
        print("PASS: preflight recorded; owned job stopped; deadline nonzero; unrelated child survived")
        return 0
    finally:
        if peer.poll() is None:
            peer.terminate()
        peer.wait(timeout=10)


if __name__ == "__main__":
    raise SystemExit(main())
