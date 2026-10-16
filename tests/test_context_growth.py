"""Failure boundaries for extended experiments and token-growth collection."""
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest import mock

import context_growth
import lab
from test_lab import LocalServer, QuietHandler


class GrowthTests(unittest.TestCase):
    """Exercise collection cancellation and explicit longer-deadline metadata."""

    def test_extended_deadline_is_explicit_and_frozen(self) -> None:
        """Allow a six-hour opt-in without changing the default or calling a server."""
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary) / 'prepared'
            command = [sys.executable, str(lab.ROOT / 'benchmark.py'),
                       '--output', str(root), '--prepare-only',
                       '--deadline', '21600']
            result = subprocess.run(command, capture_output=True, timeout=10)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual(lab.read_json(root / 'manifest.json')[
                'deadline_seconds'], 21600)
            rejected = subprocess.run(command[:-1] + ['21601'],
                                      capture_output=True, timeout=10)
            self.assertNotEqual(rejected.returncode, 0)

    def test_optional_commit_floor_fails_closed(self) -> None:
        """Free physical memory cannot hide an exhausted commit allowance."""
        profile = lab.read_json(lab.ROOT / 'profiles/qwen36-instructions-64k.json')
        profile['stop_min_commit_available_gib'] = 1.0
        snapshot = {'ram_free_gib': 10, 'vram_free_mib': 2000, 'gpu_c': 50}
        with self.assertRaises(ValueError):
            lab.check_memory(snapshot, profile, loading=False)
        snapshot['commit_available_gib'] = 0.9
        with self.assertRaises(ValueError):
            lab.check_memory(snapshot, profile, loading=False)
        snapshot['commit_available_gib'] = 2
        lab.check_memory(snapshot, profile, loading=False)

    def test_resident_bound_preserves_requested_headroom(self) -> None:
        """More available RAM may help a mapped model without consuming the floor."""
        profile = {'working_set_limit_gib': 20, 'working_set_reserve_gib': 5,
                   'stop_min_ram_free_gib': 2.5}
        self.assertEqual(lab.working_set_cap(profile, {'ram_free_gib': 22}), 17)
        self.assertEqual(lab.working_set_cap(profile, {'ram_free_gib': 40}), 20)
        with self.assertRaises(ValueError):
            lab.working_set_cap(profile, {'ram_free_gib': 4})

    @unittest.skipUnless(sys.platform == 'win32', 'Windows working-set API')
    def test_working_set_bound_on_owned_child(self) -> None:
        """Read back the hard maximum on a disposable idle Python process."""
        child = subprocess.Popen(
            [sys.executable, '-c', 'import time; time.sleep(20)'],
            creationflags=subprocess.CREATE_NO_WINDOW)
        try:
            receipt = lab.limit_owned_working_set(child.pid, 0.125)
            self.assertEqual(receipt['maximum_bytes'], 128 * 1024**2)
            self.assertTrue(receipt['flags'] & 4)
        finally:
            child.terminate()
            child.wait(timeout=5)

    def test_growth_silent_stream_is_cancelled(self) -> None:
        """A stalled response cannot hold the caller beyond its whole deadline."""
        import time

        class Handler(QuietHandler):
            def do_POST(self) -> None:
                """Simulate a server whose prefill never sends an event."""
                self.rfile.read(int(self.headers['Content-Length']))
                time.sleep(2)

        with LocalServer(Handler) as url, tempfile.TemporaryDirectory() as temporary:
            with mock.patch('context_growth.snapshot', return_value={}):
                result = context_growth.collect_request(
                    Path(temporary) / 'request', url + '/v1', 123,
                    {'messages': [], 'stream': True}, 0.5)
            self.assertEqual(result['status'], 'deadline')
            self.assertFalse(result['scored'])

    def test_document_has_three_distinct_positions(self) -> None:
        """Recall probes retain all anchors and a separate current revision."""
        text = context_growth.document(100)
        self.assertLess(text.index('region ='), text.index('auditOwner ='))
        self.assertLess(text.index('auditOwner ='), text.index('release ='))
        self.assertIn('runtimeRevision = 1; retryLimit = 4', text)
        self.assertNotIn('runtimeRevision = 2', text)


if __name__ == '__main__':
    unittest.main()
