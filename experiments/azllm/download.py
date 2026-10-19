"""Fetch a pinned TQ3_4S target or DFlash2 draft with bounded, verified transfers."""
from __future__ import annotations

import argparse
import importlib.util
import json
from pathlib import Path


def main() -> None:
    """Download into an explicit directory; never start inference."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--data-dir", required=True, type=Path)
    parser.add_argument("--artifact", choices=("model", "dflash"), default="model")
    parser.add_argument("--connections", type=int, default=8, choices=range(1, 65))
    args = parser.parse_args()
    root = Path(__file__).resolve().parent
    spec = json.loads((root / "artifacts.json").read_text())[args.artifact]
    module_spec = importlib.util.spec_from_file_location(
        "bounded_ranges", root.parent / "strata" / "range_download.py")
    module = importlib.util.module_from_spec(module_spec)
    module_spec.loader.exec_module(module)
    module.fetch(spec, args.data_dir.resolve() / spec["file"], args.connections)


if __name__ == "__main__":
    main()
