"""Download only the pinned Flash-Next shards, with bounded buffers and resume.

No installer, automatic model launch, credentials or cross-install file moves.
Uses the lab's byte-count/SHA256-verified HTTP downloader instead of Xet buffers.
"""
from __future__ import annotations

import argparse
from concurrent.futures import ThreadPoolExecutor
import json
from pathlib import Path
import shutil
import sys
import time
import urllib.error

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
import lab


def main() -> int:
    """Resume exact artifacts and expose a final receipt only after verification."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--data-dir", type=Path, required=True)
    args = parser.parse_args()
    destination = args.data_dir.resolve()
    destination.mkdir(parents=True, exist_ok=True)
    artifact = json.loads(Path(__file__).with_name("artifacts.json").read_text())["flash_next_candidate"]
    jobs = []
    needed = 512 * 1024 ** 2
    for item in artifact["files"]:
        target = (destination / item["file"]).resolve()
        if not target.is_relative_to(destination):
            raise ValueError("Artifact path escapes destination")
        partial = target.with_name(target.name + ".part")
        size = target.stat().st_size if target.exists() else partial.stat().st_size if partial.exists() else 0
        if size > item["bytes"]:
            raise ValueError("Oversized existing artifact; inspect before retrying")
        needed += item["bytes"] - size
        spec = {**item, "url": f"https://huggingface.co/{artifact['repo']}/resolve/{artifact['revision']}/{item['file']}"}
        jobs.append((spec, target))
    if shutil.disk_usage(destination).free < needed:
        raise ValueError("Insufficient space for BOTH remaining shards and512MiB headroom")

    def fetch(job: tuple[dict, Path]) -> None:
        spec, target = job
        for attempt in range(4):
            try:
                lab.download(spec, target)
                return
            except (urllib.error.URLError, TimeoutError, ConnectionError):
                if attempt == 3:
                    raise
                print(f"Retrying {target.name} from its retained prefix", flush=True)
                time.sleep(5)

    started = time.time()
    with ThreadPoolExecutor(max_workers=2) as workers:
        # Consume every result so an exception cannot masquerade as completion.
        for _ in workers.map(fetch, jobs):
            pass
    lab.save_json(destination / "verified-download.json", {
        "repo": artifact["repo"], "revision": artifact["revision"],
        "files": artifact["files"], "started": started, "verified": time.time(),
        "method": "bounded HTTP range resume, byte count and SHA256"})
    print("Both pinned shards verified", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
