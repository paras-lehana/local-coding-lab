"""Failure boundaries and changing-file transport for the campaign tooling."""
import argparse
import contextlib
import io
import importlib.util
import json
from pathlib import Path
import socket
import subprocess
import sys
import tempfile
import time
import unittest
from unittest import mock

import lab
import scenarios
import trial
from test_lab import LocalServer, QuietHandler


class CampaignTests(unittest.TestCase):
    """Test boundaries without loading models or executing generated code."""

    def test_sql_transaction_comments_and_boundaries(self) -> None:
        """Comments cannot hide real transactions or invent missing ones."""
        spec = importlib.util.spec_from_file_location(
            'sql_contract_checks', lab.ROOT / 'benchmarks/checks/ts_sql_v1.py')
        checks = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(checks)
        valid = ['-- migration\n/* preserve */ BEGIN TRANSACTION;',
                 '-- build\nCREATE TABLE next_jobs(id INTEGER);',
                 '/* done */ COMMIT;']
        self.assertTrue(checks.transaction_encloses_writes(valid))
        self.assertFalse(checks.transaction_encloses_writes(
            ['-- BEGIN\nCREATE TABLE jobs(id INTEGER);', '-- COMMIT']))
        self.assertFalse(checks.transaction_encloses_writes(
            ['CREATE TABLE outside(id INTEGER);', *valid]))
        self.assertFalse(checks.transaction_encloses_writes(
            [*valid, 'DELETE FROM next_jobs;']))
        self.assertFalse(checks.transaction_encloses_writes(
            ['BEGIN;', "SELECT 'CREATE TABLE fake';", 'COMMIT;']))

    def test_stale_file_and_transient_error_transport(self) -> None:
        """Phase two returns the update, preserves prior text and hides checks."""
        payloads = []

        def fake_turn(endpoint, payload, output, started):
            payloads.append(json.loads(json.dumps(payload)))
            index = len(payloads)
            calls = []
            if index in (1, 3):
                paths = (['docs/archive-ledger.md'] if index == 1 else
                         ['docs/runtime.md', 'docs/archive-ledger.md'])
                calls = [{'id': f'{index}-{n}', 'type': 'function',
                          'function': {'name': 'read_file',
                                       'arguments': json.dumps({'path': p})}}
                         for n, p in enumerate(paths)]
            return {'content': '' if calls else 'READY',
                    'reasoning_content': 'retained thought',
                    'tool_calls': calls,
                    'finish_reason': 'tool_calls' if calls else 'stop'}

        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            lab.save_json(root / 'case.json', scenarios.case('context-v1'))
            lab.save_json(root / 'manifest.json', {
                'model': 'fake', 'endpoint': 'http://127.0.0.1:1/v1',
                'seed': 73, 'temperature': 0.6, 'max_tokens': 100,
                'reasoning_budget': 32})
            with mock.patch('scenarios.benchmark.stream_turn', side_effect=fake_turn):
                self.assertEqual(scenarios.worker(root), 0)
            reads = lab.read_json(root / 'tools.json')
            self.assertIn('retryLimit: 0', reads[1]['response']['content'])
            self.assertIn('error', reads[2]['response'])
            self.assertEqual(reads[1]['phase'], 1)
            self.assertIn('bramble-east', json.dumps(payloads[-1]))
            self.assertIn('retained thought', json.dumps(payloads[-1]))
            self.assertNotIn('"checks"', json.dumps(payloads))

    def test_scenario_deadline_covers_both_phases(self) -> None:
        """A second user turn cannot reset the whole-scenario deadline."""
        class Handler(QuietHandler):
            requests_seen = 0

            def do_POST(self) -> None:
                """Allow the expected client cancellation during headers/body."""
                self.rfile.read(int(self.headers['Content-Length']))
                type(self).requests_seen += 1
                # Each phase fits 3.25 seconds separately; their total does not.
                # Leave ample first-turn margin for Windows CI process startup.
                time.sleep(0.5 if self.requests_seen == 1 else 3.0)
                data = {'choices': [{'delta': {'content': 'READY'},
                                     'finish_reason': 'stop'}]}
                try:
                    self.send_response(200)
                    self.end_headers()
                    self.wfile.write(('data: '+json.dumps(data)+'\n\n').encode())
                except (BrokenPipeError, ConnectionResetError):
                    pass
        with LocalServer(Handler) as url, tempfile.TemporaryDirectory() as temporary:
            output = Path(temporary) / 'run'
            result = subprocess.run([
                sys.executable, str(lab.ROOT / 'scenarios.py'),
                '--scenario', 'context-v1', '--endpoint', url+'/v1',
                '--output', str(output), '--deadline', '3.25'],
                capture_output=True, timeout=10)
            self.assertEqual(result.returncode, 124)
            self.assertTrue((output / 'answer-00.txt').exists())
            self.assertEqual(lab.read_json(output/'result.json')['status'], 'deadline')

    def test_occupied_port_never_launches(self) -> None:
        """A different server's port cannot be mistaken for this trial's model."""
        with socket.socket() as listener, tempfile.TemporaryDirectory() as temporary:
            listener.bind(('127.0.0.1', 0))
            listener.listen()
            root = Path(temporary)
            lab.save_json(root/'tasks.json', [])
            args = argparse.Namespace(port=listener.getsockname()[1],
                                      profile='qwen36-reference',
                                      tasks=str(root/'tasks.json'),
                                      output=str(root/'trial'))
            telemetry = {'ram_free_gib': 40, 'vram_free_mib': 8000, 'gpu_c': 40}
            with mock.patch('trial.lab.memory_snapshot', return_value=telemetry), \
                    mock.patch('trial.subprocess.Popen') as process, \
                    contextlib.redirect_stdout(io.StringIO()):
                self.assertEqual(trial.run(args), 2)
            process.assert_not_called()
            self.assertEqual(lab.read_json(root/'trial/trial.json')['status'],
                             'port_rejected')


if __name__ == '__main__':
    unittest.main()
