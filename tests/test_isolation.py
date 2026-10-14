"""Fail-closed checks for optional grading; never execute model output here."""
import contextlib
import io
import json
from pathlib import Path
import tempfile
import unittest
from unittest import mock

from scripts import run_isolated


class IsolationTests(unittest.TestCase):
    """Protect the no-host-fallback and probe-before-execution boundaries."""

    def test_windows_has_no_execution_fallback(self) -> None:
        """Unsupported hosts fail before launching any submitted code."""
        with mock.patch.object(run_isolated.sys, 'platform', 'win32'), \
                mock.patch.object(run_isolated.sys, 'argv', [
                    'run_isolated.py', '--directory', '.',
                    '--output', 'unused.json']), \
                mock.patch.object(run_isolated, 'bounded') as execute, \
                contextlib.redirect_stderr(io.StringIO()):
            with self.assertRaises(SystemExit) as raised:
                run_isolated.main()
        self.assertEqual(raised.exception.code, 2)
        execute.assert_not_called()

    def test_failed_probe_does_not_execute_candidate(self) -> None:
        """A failed namespace check preserves evidence and runs no test files."""
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            for name in ['candidate.py', 'behavior_checks.py', 'model_tests.py']:
                (root / name).write_text('raise RuntimeError("must not run")')
            output = root / 'result.json'
            failed = {'status': 'exited', 'returncode': 1,
                      'stdout': '', 'stderr': 'probe rejected'}
            with mock.patch.object(run_isolated.sys, 'platform', 'linux'), \
                    mock.patch.object(run_isolated.sys, 'argv', [
                        'run_isolated.py', '--directory', str(root),
                        '--output', str(output)]), \
                    mock.patch.object(run_isolated.shutil, 'which',
                                      return_value='/usr/bin/bwrap'), \
                    mock.patch.object(run_isolated.os, 'readlink',
                                      return_value='net:[123]'), \
                    mock.patch.object(run_isolated, 'bounded',
                                      return_value=failed) as execute, \
                    contextlib.redirect_stdout(io.StringIO()):
                self.assertEqual(run_isolated.main(), 1)
            execute.assert_called_once()
            self.assertEqual(json.loads(output.read_text())['runs'], {})


if __name__ == '__main__':
    unittest.main()
