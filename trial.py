"""Own one resumable model trial: monitored load, probes, tasks, explicit stop."""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import json
from pathlib import Path
import socket
import subprocess
import sys
import time
import urllib.error
import urllib.request

import benchmark
import lab


def request_json(endpoint: str, route: str, payload: dict | None = None,
                 timeout: int = 10) -> dict:
    """Send only to the explicitly validated loopback endpoint."""
    url = endpoint.removesuffix('/v1') + route
    request = urllib.request.Request(
        url, data=json.dumps(payload).encode() if payload is not None else None,
        headers={'Content-Type': 'application/json'})
    opener = urllib.request.build_opener(urllib.request.ProxyHandler({}),
                                        benchmark.NoRedirect())
    with opener.open(request, timeout=timeout) as response:
        return json.load(response)


def checkpoint(root: Path, state: dict) -> None:
    """Replace only this trial's state, preserving completed task directories."""
    state['updated_utc'] = datetime.now(timezone.utc).isoformat()
    temporary = root / 'trial.json.tmp'
    temporary.write_text(json.dumps(state, indent=2), encoding='utf-8')
    temporary.replace(root / 'trial.json')


def run(args: argparse.Namespace) -> int:
    """Run an explicit task list, retaining errors and never restarting blindly."""
    endpoint = benchmark.validate_endpoint(f'http://127.0.0.1:{args.port}/v1')
    profile = lab.read_json(lab.ROOT / 'profiles' / (args.profile + '.json'))
    tasks = lab.read_json(Path(args.tasks))
    root = Path(args.output).resolve()
    root.mkdir(parents=True, exist_ok=True)
    if (root / 'trial.json').exists():
        prior = lab.read_json(root / 'trial.json')
        print(f"Preserved prior trial: {prior.get('status')}. Use a new attempt directory.")
        return 2
    state = {'status': 'preflight', 'profile': args.profile,
             'profile_snapshot': profile, 'tasks': [],
             'preflight': lab.memory_snapshot()}
    checkpoint(root, state)
    try:
        lab.check_memory(state['preflight'], profile, loading=True)
        with socket.socket() as probe:
            probe.bind(('127.0.0.1', args.port))
    except (OSError, ValueError) as exc:
        state.update(status='capacity_rejected' if isinstance(exc, ValueError)
                     else 'port_rejected', reason=str(exc))
        checkpoint(root, state)
        print(json.dumps(state), flush=True)
        return 2
    stop = root / 'stop.request'
    command = [sys.executable, '-u', str(lab.ROOT / 'lab.py'),
               '--data-dir', str(root / 'server'), 'run',
               '--profile', args.profile, '--runtime-dir', args.runtime_dir,
               '--model-path', args.model_path, '--port', str(args.port),
               '--stop-file', str(stop), '--experimental', '--apply']
    launcher = None
    try:
        with (root / 'launcher.log').open('wb') as log:
            launcher = subprocess.Popen(command, stdout=log, stderr=log,
                                         creationflags=subprocess.CREATE_NO_WINDOW)
            state.update(status='loading', launcher_pid=launcher.pid)
            checkpoint(root, state)
            start = time.monotonic()
            while time.monotonic() - start < 300:
                if launcher.poll() is not None:
                    raise RuntimeError('Monitored launcher exited before ready')
                try:
                    health = request_json(endpoint, '/health', timeout=3)
                    models = request_json(endpoint, '/v1/models', timeout=3)
                    aliases = [m.get('id') for m in models.get('data', [])]
                    if health.get('status') == 'ok' and profile['alias'] in aliases:
                        break
                except (OSError, ValueError):
                    pass
                time.sleep(2)
            else:
                raise TimeoutError('Model load exceeded five minutes')
            lab.save_json(root / 'props.json', request_json(endpoint, '/props'))
            smoke = {'model': profile['alias'], 'messages': [
                {'role': 'user', 'content': 'Reply with exactly READY.'}],
                'max_tokens': 64, 'temperature': 0, 'seed': 73,
                'reasoning_budget_tokens': 0}
            started = time.monotonic()
            answer = request_json(endpoint, '/v1/chat/completions', smoke, 90)
            lab.save_json(root / 'smoke.json', {'request': smoke,
                          'response': answer, 'seconds': time.monotonic()-started})
            if not answer.get('choices', [{}])[0].get('message', {}).get('content'):
                raise RuntimeError('Smoke returned no final text')
            state['status'] = 'running'
            checkpoint(root, state)
            for task in tasks:
                if launcher.poll() is not None:
                    raise RuntimeError('Monitored launcher stopped; no further tasks')
                output = root / task['name']
                harness = ('benchmark.py' if task.get('scenario', 'router-v1') ==
                           'router-v1' else 'scenarios.py')
                command = [sys.executable, '-u', str(lab.ROOT / harness),
                           '--endpoint', endpoint, '--model', profile['alias'],
                           '--mode', task.get('mode', 'tools'),
                           '--deadline', str(task.get('deadline', 1200)),
                           '--seed', str(task.get('seed', 73)),
                           '--temperature', str(task.get('temperature', 0.6)),
                           '--max-tokens', str(task.get('max_tokens', 8192)),
                           '--output', str(output)]
                if task.get('budget') is not None:
                    command += ['--reasoning-budget', str(task['budget'])]
                if task.get('scenario', 'router-v1') != 'router-v1':
                    command += ['--scenario', task['scenario']]
                print('Starting', task['name'], flush=True)
                with (root / (task['name'] + '.log')).open('wb') as task_log:
                    completed = subprocess.run(command, stdout=task_log,
                                               stderr=task_log, timeout=1240)
                result = lab.read_json(output / 'result.json') if (
                    output / 'result.json').exists() else {'status': 'harness_error'}
                state['tasks'].append({'task': task, 'returncode': completed.returncode,
                                       'result': result})
                checkpoint(root, state)
                print(task['name'], json.dumps(result), flush=True)
                if result['status'] in ('deadline', 'worker_error', 'harness_error'):
                    state['status'] = 'stopped_after_failed_task'
                    break
            else:
                state['status'] = 'collected'
    except Exception as exc:
        state.update(status='failed', reason=f'{type(exc).__name__}: {exc}')
        print(state['reason'], flush=True)
    finally:
        if launcher is not None and launcher.poll() is None:
            stop.touch(exist_ok=False)
            try:
                launcher.wait(timeout=40)
            except subprocess.TimeoutExpired:
                state.update(status='cleanup_required',
                             reason='Owned launcher did not stop; do not load another model')
        state['postflight'] = lab.memory_snapshot()
        checkpoint(root, state)
    print('Trial', state['status'], flush=True)
    return 0 if state['status'] == 'collected' else 2


def main() -> int:
    """Require explicit model paths, tasks and output for every trial."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--profile', required=True)
    parser.add_argument('--runtime-dir', required=True)
    parser.add_argument('--model-path', required=True)
    parser.add_argument('--tasks', required=True)
    parser.add_argument('--output', required=True)
    parser.add_argument('--port', type=int, default=8081)
    parser.add_argument('--apply', action='store_true')
    args = parser.parse_args()
    if not args.apply:
        parser.error('This performs inference; --apply is required')
    if sys.platform != 'win32':
        parser.error('Monitored launcher requires Windows')
    return run(args)


if __name__ == '__main__':
    raise SystemExit(main())
