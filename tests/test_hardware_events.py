"""Regression checks for GPU crashes that do not generate WHEA records."""
import json
import subprocess
import unittest
from unittest.mock import patch

import lab


class HardwareEventTests(unittest.TestCase):
    """Exercise reboot/display evidence, unrelated IDs and unavailable data."""

    def setUp(self) -> None:
        """Mock the Windows launch flag when testing decisions on Linux CI."""
        flag = patch.object(lab.subprocess, 'CREATE_NO_WINDOW',
                            getattr(subprocess, 'CREATE_NO_WINDOW', 0),
                            create=True)
        flag.start()
        self.addCleanup(flag.stop)

    def check_records(self, rows: object) -> None:
        """Pass a simulated Event Log response through the real decision."""
        response = subprocess.CompletedProcess(
            [], 0, json.dumps(rows).encode('utf-8'), b'')
        with patch.object(lab.subprocess, 'run', return_value=response):
            lab.check_hardware_events('2026-11-09T09:00:00+05:30')

    def test_bugcheck_without_whea_is_rejected(self) -> None:
        """A real class of 0x116 failure must not depend on a WHEA event."""
        with self.assertRaisesRegex(ValueError, 'SystemErrorReporting:1001'):
            self.check_records({
                'provider': 'Microsoft-Windows-WER-SystemErrorReporting',
                'id': 1001, 'level': 2})

    def test_restart_and_recovered_gpu_timeout_are_rejected(self) -> None:
        """A hard reset or recovered GPU hang ends the qualified interval."""
        for provider, event_id, level in [
            ('Microsoft-Windows-Kernel-Power', 41, 1),
            ('EventLog', 6008, 2), ('Display', 4101, 3),
            ('nvlddmkm', 153, 2),
            ('Microsoft-Windows-WHEA-Logger', 19, 3),
        ]:
            with self.subTest(provider=provider), self.assertRaises(ValueError):
                self.check_records([{'provider': provider, 'id': event_id,
                                     'level': level}])

    def test_unrelated_ids_and_normal_startup_do_not_block(self) -> None:
        """Provider identity prevents false TPM/update/normal-boot alarms."""
        self.check_records([
            {'provider': 'TPM', 'id': 18, 'level': 4},
            {'provider': 'Microsoft-Windows-WindowsUpdateClient',
             'id': 19, 'level': 4},
            {'provider': 'EventLog', 'id': 6005, 'level': 4},
            {'provider': 'nvlddmkm', 'id': 0, 'level': 4},
        ])

    def test_missing_or_malformed_inventory_is_not_clean(self) -> None:
        """A broken query/decoder cannot become an empty event inventory."""
        for rows in [None, {'provider': 'Display'}, ['invalid']]:
            with self.subTest(rows=rows), self.assertRaises(ValueError):
                self.check_records(rows)
        response = subprocess.CompletedProcess([], 3, b'', b'Access denied')
        with patch.object(lab.subprocess, 'run', return_value=response):
            with self.assertRaisesRegex(ValueError, 'Could not check'):
                lab.check_hardware_events('2026-11-09T09:00:00+05:30')

    def test_no_matching_events_is_clean(self) -> None:
        """The explicit no-matching-events path needs no model launch."""
        response = subprocess.CompletedProcess([], 0, b'', b'')
        with patch.object(lab.subprocess, 'run', return_value=response):
            lab.check_hardware_events('2026-11-09T09:00:00+05:30')

    def test_invalid_date_is_rejected_before_shell(self) -> None:
        """Malformed input must not be interpolated into PowerShell code."""
        with patch.object(lab.subprocess, 'run') as query:
            with self.assertRaises(ValueError):
                lab.check_hardware_events("not-a-date'; exit 0")
        query.assert_not_called()


if __name__ == '__main__':
    unittest.main()
