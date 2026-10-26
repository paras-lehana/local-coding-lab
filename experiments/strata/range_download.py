"""Bounded parallel HTTP ranges for the two pinned, public Flash-Next shards.

Keeps a completion journal next to each sparse working file; only the final
whole-file SHA256 check publishes a GGUF. Interrupted ranges are overwritten.
No inference, credentials, installer, or changes to another model directory.
"""
from __future__ import annotations

import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
import json
from pathlib import Path
import shutil
import sys
import threading
import time
import urllib.request

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
import lab

CHUNK = 64 * 1024 ** 2


def fetch(spec: dict, target: Path, connections: int) -> None:
    """Use independently checked ranges and verify the complete pinned artifact."""
    if target.exists():
        lab.verify(target, spec)
        return
    target.parent.mkdir(parents=True, exist_ok=True)
    working = target.with_name(target.name + '.ranges')
    journal = target.with_name(target.name + '.ranges.json')
    prefix = target.with_name(target.name + '.part')

    def save_state(state: dict) -> None:
        temporary = journal.with_suffix('.json.tmp')
        temporary.write_text(json.dumps(state), encoding='utf-8')
        temporary.replace(journal)

    if journal.exists():
        state = json.loads(journal.read_text())
        if state['sha256'] != spec['sha256'] or state['bytes'] != spec['bytes']:
            raise ValueError('Journal belongs to another artifact')
        if not state.get('allocating') and (not working.exists() or working.stat().st_size != spec['bytes']):
            raise ValueError('Working-file size differs from journal')
    else:
        if working.exists():
            raise ValueError('Unjournaled working file; inspect before retrying')
        offset = prefix.stat().st_size if prefix.exists() else 0
        if offset > spec['bytes']:
            raise ValueError('Oversized HTTP prefix')
        if shutil.disk_usage(target.parent).free < spec['bytes'] - offset + 512 * 1024 ** 2:
            raise ValueError('Insufficient free disk for working file')
        state = {'sha256': spec['sha256'], 'bytes': spec['bytes'], 'prefix_bytes': offset,
                 'chunk_bytes': CHUNK, 'done': [], 'allocating': True}
        # Windows may spend minutes extending a large ordinary file. Journal
        # BEFORE that operation so a reboot can recover the recorded HTTP prefix.
        save_state(state)
    if state.get('chunk_bytes') != CHUNK:
        raise ValueError('Unsupported journal chunk size')
    offset = state['prefix_bytes']
    if not isinstance(offset, int) or not 0 <= offset <= spec['bytes']:
        raise ValueError('Invalid recorded prefix')
    if state.get('allocating'):
        if not working.exists() and prefix.exists():
            if prefix.stat().st_size != offset:
                raise ValueError('Recorded HTTP prefix changed')
            prefix.rename(working)
        size = working.stat().st_size if working.exists() else 0
        if not offset <= size <= spec['bytes'] or state['done']:
            raise ValueError('Invalid interrupted allocation')
        if shutil.disk_usage(target.parent).free < spec['bytes'] - size + 512 * 1024 ** 2:
            raise ValueError('Insufficient space to finish allocation')
        with working.open('ab') as handle:
            handle.truncate(spec['bytes'])
        state['allocating'] = False
        save_state(state)
    ranges = [(start, min(start + CHUNK, spec['bytes']))
              for start in range(offset, spec['bytes'], CHUNK)]
    completed = set(state['done'])
    if not completed.issubset({start for start, _ in ranges}):
        raise ValueError('Invalid completed range')
    lock = threading.Lock()

    def download_range(bounds: tuple[int, int]) -> None:
        start, end = bounds
        for attempt in range(5):
            try:
                request = urllib.request.Request(spec['url'], headers={
                    'Range': f'bytes={start}-{end - 1}',
                    'User-Agent': 'local-coding-lab/0.6'})
                with urllib.request.urlopen(request, timeout=60) as response:
                    expected = f'bytes {start}-{end - 1}/{spec["bytes"]}'
                    if response.status != 206 or response.headers.get('Content-Range') != expected:
                        raise ValueError('Server did not honor the exact pinned range')
                    remaining = end - start
                    with working.open('r+b') as handle:
                        handle.seek(start)
                        while remaining:
                            block = response.read(min(1024 ** 2, remaining))
                            if not block:
                                raise ConnectionError('Truncated HTTP range')
                            handle.write(block)
                            remaining -= len(block)
                with lock:
                    completed.add(start)
                    state['done'] = sorted(completed)
                    save_state(state)
                    count = offset + sum(b - a for a, b in ranges if a in completed)
                    print(f'{target.name}: {count / spec["bytes"]:.1%}', flush=True)
                return
            except (OSError, ConnectionError):
                if attempt == 4:
                    raise
                time.sleep(2 ** attempt)

    with ThreadPoolExecutor(max_workers=connections) as pool:
        futures = [pool.submit(download_range, r) for r in ranges if r[0] not in completed]
        for future in as_completed(futures):
            future.result()
    lab.verify(working, spec)
    working.rename(target)
    state['verified'] = time.time()
    save_state(state)
    print(f'{target.name}: SHA256 verified', flush=True)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--data-dir', type=Path, required=True)
    parser.add_argument('--connections', type=int, default=8, choices=range(1, 65))
    parser.add_argument('--artifact-key', default='flash_next_candidate',
                        choices=('flash_next_candidate', 'flash_next_q2_candidate'),
                        help='Explicit quant selection; the original IQ3 default is unchanged')
    args = parser.parse_args()
    artifact = json.loads(Path(__file__).with_name('artifacts.json').read_text())[args.artifact_key]
    destination = args.data_dir.resolve()
    destination.mkdir(parents=True, exist_ok=True)
    started = time.time()
    # One shard at a time: bounded total connections and no duplicate full copy.
    for item in artifact['files']:
        target = (destination / item['file']).resolve()
        if not target.is_relative_to(destination):
            raise ValueError('Artifact path escapes destination')
        spec = {**item, 'url': f'https://huggingface.co/{artifact["repo"]}/resolve/{artifact["revision"]}/{item["file"]}'}
        fetch(spec, target, args.connections)
    lab.save_json(destination / 'verified-download.json', {
        'repo': artifact['repo'], 'revision': artifact['revision'], 'files': artifact['files'],
        'artifact_key': args.artifact_key,
        'started': started, 'verified': time.time(), 'method': 'bounded HTTP ranges and full SHA256'})
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
