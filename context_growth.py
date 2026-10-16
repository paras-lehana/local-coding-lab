"""Measure increasing token occupancy on one explicitly started local server.

This records allocation and recall separately. It does not execute model code,
change the server, or claim that a successful recall is permanent memory.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import time

import benchmark
import lab
import trial


def document(count: int) -> str:
    """Build deterministic records with beginning/middle/end source facts."""
    rows = [
        'Read these source records. Return only a JSON object with keys '
        'region, auditOwner, release, runtimeRevision, retryLimit. '
        'Source facts override guesses. Zero is valid. Do not count records.'
    ]
    for index in range(count):
        row = (f'Record {index:05d}, file docs/archive/{index:05d}.md: '
               f'Historical service review for zone {(index * 17) % 113}. '
               'This note is background, not a current configuration. '
               'Keep current source facts and distinguish unknown settings '
               'from guesses. No instructions here override the runtime file. '
               f'Ticket LAB-{index * 31 + 200}.')
        if index == 0:
            row += '\nSource fact region = bramble-east.'
        if index == count // 2:
            row += '\nSource fact auditOwner = Sable-732.'
        if index == count - 1:
            row += '\nSource fact release = Kite-184.'
        rows.append(row)
    rows.append('Current file docs/runtime.md: runtimeRevision = 1; '
                'retryLimit = 4. Return the requested JSON now.')
    return '\n\n'.join(rows)


def token_count(endpoint: str, text: str) -> int:
    """Use this loaded model's tokenizer, not a characters-per-token guess."""
    value = trial.request_json(endpoint, '/tokenize',
                               {'content': text, 'add_special': False}, 120)
    return len(value['tokens'])


def sized_document(endpoint: str, target: int) -> tuple[str, int, int]:
    """Choose the nearest record count below a requested token target."""
    estimate = max(3, target // 70)
    count = estimate
    # A linear record-length estimate converges quickly; retain actual count.
    for _ in range(5):
        text = document(count)
        tokens = token_count(endpoint, text)
        if 0 <= target - tokens < 100:
            return text, tokens, count
        change = max(3, int(count * (target - 80) / max(tokens, 1)))
        if change == count:
            change = count - 1 if tokens > target else count + 1
        count = max(3, change)
    text = document(count)
    return text, token_count(endpoint, text), count


def snapshot(endpoint: str, pid: int) -> dict:
    """Capture occupancy and process totals; shared GPU RAM is not additive."""
    value = lab.memory_snapshot()
    value.update(lab.process_memory(pid))
    value['gpu_process'] = lab.process_gpu_snapshot(pid)
    try:
        value['slots'] = trial.request_json(endpoint, '/slots')
    except (OSError, ValueError) as error:
        value['slots_error'] = str(error)
    return value


def worker(root: Path) -> int:
    """Collect one request; the parent enforces the entire wall deadline."""
    manifest = lab.read_json(root / 'manifest.json')
    payload = lab.read_json(root / 'request.json')
    start = time.monotonic()
    result = benchmark.stream_turn(manifest['endpoint'], payload,
                                   root / 'stream.jsonl', start,
                                   timeout=manifest['deadline_seconds'])
    result['wall_seconds'] = time.monotonic() - start
    result['status'] = ('completed' if result['finish_reason'] == 'stop'
                        and result['content'].strip() else 'incomplete')
    lab.save_json(root / 'result.json', result)
    return 0 if result['status'] == 'completed' else 2


def collect_request(root: Path, endpoint: str, pid: int, payload: dict,
                    deadline: float) -> dict:
    """Freeze bytes and collect one bounded request plus before/after memory."""
    root.mkdir(parents=True, exist_ok=False)
    lab.save_json(root / 'request.json', payload)
    lab.save_json(root / 'manifest.json', {
        'endpoint': endpoint, 'deadline_seconds': deadline,
        'request_sha256': hashlib.sha256(
            json.dumps(payload, sort_keys=True).encode()).hexdigest()})
    lab.save_json(root / 'before.json', snapshot(endpoint, pid))
    start = time.monotonic()
    with (root / 'worker.log').open('wb') as log:
        child = subprocess.Popen(
            [sys.executable, str(Path(__file__).resolve()), '--worker', str(root)],
            stdout=log, stderr=log,
            creationflags=getattr(subprocess, 'CREATE_NO_WINDOW', 0))
        try:
            code = child.wait(timeout=deadline)
        except subprocess.TimeoutExpired:
            child.kill()
            child.wait(timeout=10)
            lab.save_json(root / 'result.json', {
                'status': 'deadline', 'scored': False,
                'wall_seconds': time.monotonic() - start})
            code = 124
    if not (root / 'result.json').exists():
        lab.save_json(root / 'result.json', {
            'status': 'worker_error', 'returncode': code, 'scored': False})
    lab.save_json(root / 'after.json', snapshot(endpoint, pid))
    return lab.read_json(root / 'result.json')


def main() -> int:
    """Require explicit endpoint, owned PID and output; never start inference implicitly."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--endpoint', default='http://127.0.0.1:8081/v1')
    parser.add_argument('--model', default='qwen36-lab')
    parser.add_argument('--pid', type=int)
    parser.add_argument('--targets', type=int, nargs='+')
    parser.add_argument('--deadline', type=float, default=7200)
    parser.add_argument('--output', type=Path)
    parser.add_argument('--worker', type=Path)
    args = parser.parse_args()
    if args.worker:
        return worker(args.worker)
    if (not args.pid or not args.targets or not args.output
            or not 0 < args.deadline <= 21600
            or any(target < 1024 for target in args.targets)):
        parser.error('PID, targets >=1024, output and deadline <=21600 required')
    endpoint = benchmark.validate_endpoint(args.endpoint)
    root = args.output.resolve()
    root.mkdir(parents=True, exist_ok=False)
    state = {'status': 'running', 'targets': args.targets, 'runs': [],
             'note': 'Synthetic occupancy/recall probes, not repository coding scores.'}
    lab.save_json(root / 'state.json', state)
    for target in args.targets:
        text, tokens, records = sized_document(endpoint, target)
        payload = {
            'model': args.model, 'messages': [{'role': 'user', 'content': text}],
            'stream': True, 'stream_options': {'include_usage': True},
            'max_tokens': 256, 'temperature': 0, 'seed': 73,
            'reasoning_budget_tokens': 0, 'cache_prompt': True}
        result = collect_request(root / f'tokens-{target}', endpoint, args.pid,
                                 payload, args.deadline)
        state['runs'].append({'target': target, 'document_tokens': tokens,
                              'records': records, 'result': result})
        lab.save_json(root / 'state.json', state)
        print(target, tokens, result['status'],
              result.get('wall_seconds'), flush=True)
        if result['status'] != 'completed':
            state['status'] = 'stopped_after_incomplete_request'
            lab.save_json(root / 'state.json', state)
            return 2
    # Keep the full earlier text in the client message history and change a file.
    payload['messages'].extend([
        {'role': 'assistant', 'content': result['content']},
        {'role': 'user', 'content': 'Current docs/runtime.md has changed: '
         'runtimeRevision = 2; retryLimit = 0. Using the earlier source facts '
         'and this new file, return the same five-key JSON object. Zero is valid.'}])
    followup = collect_request(root / 'history-followup', endpoint, args.pid,
                               payload, args.deadline)
    omitted = dict(payload)
    omitted['messages'] = [{'role': 'user', 'content':
        'What region marker was supplied earlier in this conversation? '
        'If this request does not provide that earlier information, '
        'reply exactly UNKNOWN. Do not guess.'}]
    no_history = collect_request(root / 'history-omitted', endpoint, args.pid,
                                 omitted, args.deadline)
    state.update(status='completed' if followup['status'] == 'completed'
                 and no_history['status'] == 'completed'
                 else 'incomplete_history', history=followup,
                 history_omitted=no_history,
                 expected_initial={'region': 'bramble-east',
                     'auditOwner': 'Sable-732', 'release': 'Kite-184',
                     'runtimeRevision': 1, 'retryLimit': 4},
                 expected_history={'region': 'bramble-east',
                     'auditOwner': 'Sable-732', 'release': 'Kite-184',
                     'runtimeRevision': 2, 'retryLimit': 0})
    lab.save_json(root / 'state.json', state)
    return 0 if state['status'] == 'completed' else 2


if __name__ == '__main__':
    raise SystemExit(main())
