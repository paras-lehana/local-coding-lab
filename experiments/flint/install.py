"""Install pinned Flint experiment assets without replacing a working runtime.

Downloads use the lab's bounded-memory, resumable and SHA256-checked path.
This script does not start inference, change editor settings or delete files.
"""
from __future__ import annotations

import argparse
from pathlib import Path
import sys
import time

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
import lab  # noqa: E402


def fetch(spec: dict, target: Path) -> None:
    """Retry a short transport failure; never retry a complete bad hash."""
    for attempt in range(1, 6):
        try:
            lab.download(spec, target)
            return
        except Exception as error:
            partial = target.with_name(target.name + ".part")
            if (target.exists() or (partial.exists()
                    and partial.stat().st_size >= spec["bytes"])):
                raise
            if attempt == 5:
                raise
            print(f"Attempt {attempt}: {error}; retrying", flush=True)
            time.sleep(5 * attempt)


def main() -> None:
    """Install only explicitly selected assets below the supplied data root."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--data-root", type=Path, required=True)
    parser.add_argument("--component", choices=("model", "runtime"), required=True)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    pins = lab.read_json(Path(__file__).with_name("pins.json"))
    root = args.data_root.resolve()
    if not args.apply:
        print(f"Plan: {args.component} under {root}; add --apply")
        return
    if args.component == "model":
        fetch(pins["model"], root / "models" / pins["model"]["filename"])
    else:
        runtime = root / "runtimes" / pins["runtime"]["tag"]
        if runtime.exists():
            raise FileExistsError(f"Preserving existing runtime: {runtime}")
        archives = []
        for spec in pins["runtime"]["assets"]:
            archive = root / "downloads" / spec["filename"]
            fetch(spec, archive)
            archives.append(archive)
        runtime.mkdir(parents=True, exist_ok=False)
        for archive in archives:
            lab.extract_zip(archive, runtime)
        lab.save_json(runtime / "flint-install-receipt.json", pins["runtime"])
        print(f"Installed verified archives: {runtime}")


if __name__ == "__main__":
    main()
