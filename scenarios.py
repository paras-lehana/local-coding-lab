"""Frozen long-file/stale-file and held-out TypeScript/SQL model tasks."""
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


def case(name: str) -> dict:
    """Build deterministic public inputs; expected checks never enter messages."""
    entry = ('Read .claude/CLAUDE.md and follow relevant links explicitly. '
             'Prefer current v2 rules. Do not invent absent settings. '
             'File tools are read-only; do not claim test execution.\n')
    if name in ('context-v1', 'context-extended-v1'):
        record_count = 120 if name == 'context-v1' else 320
        records = []
        for i in range(record_count):
            record = (f'Record {i:03d}: synthetic service inventory for zone '
                      f'{(i*17)%113}. This historical note describes a completed '
                      'documentation review. It does not override current '
                      'runtime settings or instruction precedence. Retain '
                      'the original audit trail, inspect current files before '
                      'describing configuration, and distinguish unknown '
                      f'deployment facts from local records. Ticket LAB-{i*31+200}.')
            if i == 0:
                record += '\nAuthoritative region marker: bramble-east.'
            if i == record_count//2:
                record += '\nAuthoritative audit-owner marker: Sable-732.'
            if i == record_count-1:
                record += '\nAuthoritative release marker: Kite-184.'
            records.append(record)
        sources = {
            'AGENTS.md': entry,
            '.claude/CLAUDE.md': ('Current runtime rules: rules/v2/runtime.md. '
                                'Historical file: rules/runtime-v1.md. '
                                'Read docs/archive-ledger.md and docs/runtime.md. '
                                'A link is not loaded content.'),
            'rules/runtime-v1.md': 'Superseded: use a default retry limit of 9.',
            'rules/v2/runtime.md': ('Use the current file version. Zero is valid; '
                                    'never replace it using truthiness. Missing '
                                    'deployment facts must be null, not guesses.'),
            'docs/archive-ledger.md': '\n\n'.join(records),
            'docs/runtime.md': 'Revision: 1\nretryLimit: 4\nNo Redis sentinel port is specified.\n'}
        return {'sources': sources, 'phases': [
            {'question': 'Start with AGENTS.md. Follow its router and read the relevant rules, complete ledger, and runtime file. Preserve this information for the next message. Do not summarize marker values. Reply only READY and the number of ledger records after inspecting them.'},
            {'question': 'The runtime file has changed since your previous reply. Re-read it. Using the earlier ledger and current runtime, return one JSON object with keys region, auditOwner, release, retryLimit, runtimeRevision, redisSentinelPort. Give the absent port as null. List actual paths read this turn separately. The earlier ledger may be temporarily unavailable to the file tool; use its previously delivered contents, not invented values.',
             'updates': {'docs/runtime.md': 'Revision: 2\nretryLimit: 0\nNo Redis sentinel port is specified.\n'},
             'unavailable': ['docs/archive-ledger.md']}],
            'checks': {'region': 'bramble-east', 'auditOwner': 'Sable-732',
                       'release': 'Kite-184', 'retryLimit': 0,
                       'runtimeRevision': 2, 'redisSentinelPort': None},
            'note': 'Two user turns; large file spans beginning/middle/end, with a changed file and a transient read error. Not a 64K recall claim.'}
    if name == 'ts-sql-v1':
        sources = {
            'AGENTS.md': entry,
            '.claude/CLAUDE.md': ('Read rules/v2/typescript-sql.md and docs/contract.md. '
                                'Implementation: src/normalize.ts. Current database: schema.sql.'),
            'rules/v2/typescript-sql.md': ('Use TypeScript without packages and SQLite SQL. '
                                         'Do not use PostgreSQL-only syntax. Preserve data and foreign keys. '
                                         'Do not invent deployment connection strings.'),
            'docs/contract.md': (
                'Export normalizeJobs(input: unknown). Input must be an array of plain job objects. '
                'Each id must be a string whose trimmed value is nonempty. Reject duplicate trimmed ids. '
                'count defaults to 1 ONLY when undefined; otherwise require a finite integer >=0. '
                'enabled defaults to true ONLY when undefined; otherwise require boolean. '
                'tags defaults to [] ONLY when undefined; otherwise require an array of strings. '
                'Return fresh objects {id,count,enabled,tags} in input order, with copied tags, '
                'no argument mutation and no mutable aliases. Reject invalid inputs with TypeError.\n'
                'SQLite migration runs once against schema.sql with foreign_keys initially ON. '
                'Preserve all job ids, payloads and referencing job_events. Replace the global '
                'external_id uniqueness with UNIQUE(tenant_id,external_id). Make attempts INTEGER '
                'NOT NULL DEFAULT 0 CHECK(attempts>=0), converting existing NULL to 0. '
                'Restore foreign_keys ON and leave foreign_key_check empty. Use a transaction. '
                'The schema has no deployment database URL; do not invent one.'),
            'src/normalize.ts': (
                'export function normalizeJobs(input: any[]): any[] {\n'
                '  return input.map(x => ({id: x.id, count: x.count || 1,\n'
                '    enabled: x.enabled || true, tags: x.tags || []}));\n}\n'),
            'schema.sql': (
                'PRAGMA foreign_keys=ON;\n'
                'CREATE TABLE jobs(id INTEGER PRIMARY KEY, tenant_id TEXT NOT NULL, '
                'external_id TEXT NOT NULL UNIQUE, payload TEXT NOT NULL, attempts INTEGER);\n'
                'CREATE TABLE job_events(id INTEGER PRIMARY KEY, job_id INTEGER NOT NULL '
                'REFERENCES jobs(id), message TEXT NOT NULL);\n')}
        return {'sources': sources, 'phases': [{'question': (
            'Start with AGENTS.md and discover the applicable linked files. Identify the code and '
            'schema bugs against the documented contract, citing actual paths. Provide a complete '
            'corrected TypeScript implementation in one typescript code fence and a complete '
            'SQLite migration in one sql code fence. Explain concrete tests for zero/false, '
            'invalid inputs, nested aliasing, data preservation, tenant uniqueness and foreign '
            'keys. State the deployment database URL only if a source supplies it. Finish with '
            'actual files read and tests actually run; this harness cannot execute code.')}],
            'checks': {'behavior': 'independent TypeScript and SQLite execution required'},
            'note': 'Held-out language/task relative to router-v1; freeze before collecting any answers.'}
    raise ValueError('Unknown scenario')


def worker(root: Path) -> int:
    """Collect all phases with updated allowlisted sources and preserved traces."""
    manifest = lab.read_json(root / 'manifest.json')
    frozen = lab.read_json(root / 'case.json')
    sources = dict(frozen['sources'])
    messages = [{'role': 'system', 'content': 'Answer from the provided project. Tools are read-only. Do not invent missing facts.'}]
    tool = {'type': 'function', 'function': {'name': 'read_file',
            'description': 'Read an exact project-relative path discovered from AGENTS.md and its links.',
            'parameters': {'type': 'object', 'properties': {'path': {'type': 'string'}},
                           'required': ['path'], 'additionalProperties': False}}}
    turns, reads, answers = [], [], []
    started = time.monotonic()
    for phase_index, phase in enumerate(frozen['phases']):
        sources.update(phase.get('updates', {}))
        messages.append({'role': 'user', 'content': phase['question']})
        for _ in range(16):
            index = len(turns)
            payload = {'model': manifest['model'], 'messages': messages,
                       'tools': [tool], 'stream': True,
                       'stream_options': {'include_usage': True},
                       'seed': manifest['seed'], 'temperature': manifest['temperature'],
                       'max_tokens': manifest['max_tokens']}
            if manifest['reasoning_budget'] is not None:
                payload['reasoning_budget_tokens'] = manifest['reasoning_budget']
            lab.save_json(root / f'request-{index:02d}.json', payload)
            turn = benchmark.stream_turn(manifest['endpoint'], payload,
                                         root / f'stream-{index:02d}.jsonl', started)
            turn['phase'] = phase_index
            turns.append(turn)
            lab.save_json(root / 'turns.json', turns)
            if turn['finish_reason'] not in ('stop', 'tool_calls'):
                lab.save_json(root / 'result.json', {'status': 'incomplete', 'scored': False,
                              'reason': turn['finish_reason'], 'wall_seconds': time.monotonic()-started})
                return 2
            message = {'role': 'assistant', 'content': turn['content']}
            if turn['reasoning_content']:
                message['reasoning_content'] = turn['reasoning_content']
            if turn['tool_calls']:
                message['tool_calls'] = turn['tool_calls']
            messages.append(message)
            if not turn['tool_calls']:
                if not turn['content'].strip():
                    lab.save_json(root / 'result.json', {'status': 'empty', 'scored': False})
                    return 2
                answers.append(turn['content'])
                (root / f'answer-{phase_index:02d}.txt').write_text(turn['content'], encoding='utf-8')
                break
            for call in turn['tool_calls']:
                try:
                    if call['function']['name'] != 'read_file':
                        raise ValueError('Unknown tool')
                    path = json.loads(call['function']['arguments']).get('path')
                    response = (json.dumps({'error': 'Temporarily unavailable; use the earlier delivered version.'})
                                if path in phase.get('unavailable', []) else
                                benchmark.read_fixture(path, sources))
                except (ValueError, TypeError, AttributeError):
                    response = json.dumps({'error': 'Invalid read_file call'})
                reads.append({'phase': phase_index, 'call': call, 'response': json.loads(response)})
                lab.save_json(root / 'tools.json', reads)
                messages.append({'role': 'tool', 'tool_call_id': call['id'], 'content': response})
        else:
            lab.save_json(root / 'result.json', {'status': 'tool_turn_limit', 'scored': False})
            return 2
    (root / 'answer.txt').write_text(answers[-1], encoding='utf-8')
    lab.save_json(root / 'result.json', {'status': 'completed', 'scored': False,
                  'wall_seconds': time.monotonic()-started, 'turn_count': len(turns),
                  'phase_count': len(answers)})
    return 0


def main() -> int:
    """Freeze the complete case before starting a deadline-owned network worker."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--scenario', choices=['context-v1', 'context-extended-v1', 'ts-sql-v1'])
    parser.add_argument('--endpoint', default='http://127.0.0.1:8081/v1')
    parser.add_argument('--model', default='qwen36-lab')
    parser.add_argument('--output', type=Path)
    parser.add_argument('--deadline', type=float, default=1200)
    parser.add_argument('--seed', type=int, default=73)
    parser.add_argument('--temperature', type=float, default=0.6)
    parser.add_argument('--max-tokens', type=int, default=8192)
    parser.add_argument('--reasoning-budget', type=int)
    parser.add_argument('--mode', default='tools', choices=['tools'])
    parser.add_argument('--prepare-only', action='store_true')
    parser.add_argument('--worker', type=Path)
    args = parser.parse_args()
    if args.worker:
        return worker(args.worker)
    if not args.scenario or not args.output or not 0 < args.deadline <= 1200:
        parser.error('Scenario/output and deadline <=1200 seconds required')
    if not 1 <= args.max_tokens <= 32768:
        parser.error('max-tokens must be 1..32768')
    frozen = case(args.scenario)
    root = args.output.resolve()
    root.mkdir(parents=True, exist_ok=False)
    lab.save_json(root / 'case.json', frozen)
    manifest = {'scenario': args.scenario,
                'endpoint': benchmark.validate_endpoint(args.endpoint),
                'model': args.model, 'seed': args.seed, 'temperature': args.temperature,
                'max_tokens': args.max_tokens, 'reasoning_budget': args.reasoning_budget,
                'deadline_seconds': args.deadline,
                'case_sha256': hashlib.sha256(json.dumps(frozen, sort_keys=True).encode()).hexdigest()}
    lab.save_json(root / 'manifest.json', manifest)
    if args.prepare_only:
        print('Frozen', args.scenario, manifest['case_sha256'])
        return 0
    started = time.monotonic()
    with (root / 'worker.log').open('wb') as log:
        child = subprocess.Popen([sys.executable, str(Path(__file__).resolve()),
                                  '--worker', str(root)], stdout=log, stderr=log)
        try:
            code = child.wait(timeout=args.deadline)
        except subprocess.TimeoutExpired:
            child.kill()
            child.wait(timeout=5)
            lab.save_json(root / 'result.json', {'status': 'deadline', 'scored': False,
                          'wall_seconds': time.monotonic()-started})
            code = 124
        except BaseException:
            child.kill()
            child.wait(timeout=5)
            raise
    if not (root / 'result.json').exists():
        lab.save_json(root / 'result.json', {'status': 'worker_error', 'scored': False,
                      'exit_code': code, 'wall_seconds': time.monotonic()-started})
    print(json.dumps(lab.read_json(root / 'result.json')))
    return code


if __name__ == '__main__':
    raise SystemExit(main())
