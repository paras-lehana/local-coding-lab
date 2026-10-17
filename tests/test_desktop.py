"""Exercise controller refusal paths with fake process discovery, never real stops."""
import base64
import ctypes
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


@unittest.skipUnless(sys.platform == "win32", "Windows controller")
class DesktopControlTests(unittest.TestCase):
    """An unrelated inference server must survive every controller request."""

    def run_fixture(self, action: str, unrelated: bool,
                    scenario: str = "") -> str:
        """Isolate discovery in a fresh PowerShell process and temporary root."""
        with tempfile.TemporaryDirectory(prefix="desktop spaced ") as folder:
            root = Path(folder)
            (root / "widget").mkdir()
            (root / "runtime-config.json").write_text(
                '{"runtime_executable":"expected.exe",'
                '"model":"expected.gguf","alias":"fixture"}')
            script = Path(__file__).resolve().parents[1]/"desktop/control.ps1"
            mock = (
                "[pscustomobject]@{ExecutablePath='unrelated.exe';"
                "CommandLine='unrelated --port8080';ProcessId=999999}"
                if unrelated else "return @()"
            )
            if scenario == "stale":
                mock = ("[pscustomobject]@{ExecutablePath='expected.exe';"
                        "CommandLine='expected.gguf --port 8080';"
                        "ProcessId=999999}")
                (root/"server-settings.json").write_text(json.dumps({
                    "pid":123456,"model":"expected.gguf",
                    "run_directory":str(root/"logs/session/runs/server"),
                    "stop_file":str(root/"logs/session/stop.request"),
                }))
            # Literal PS single-quoted strings double embedded apostrophes.
            quoted_root = str(root).replace("'", "''")
            quoted_script = str(script).replace("'", "''")
            source = (
                f"function Get-CimInstance {{ {mock} }}; "
                "function Stop-Process { throw 'Stop-Process must never run' }; "
            )
            if scenario == "stale":
                source += ("function Invoke-RestMethod { "
                           "[pscustomobject]@{model_alias='fixture';"
                           "is_sleeping=$false} }; ")
            if scenario == "failed_start":
                (root/"start-server.ps1").write_text(
                    "throw 'Fixture start capacity rejected'\n")
            source += f"& '{quoted_script}' -Root '{quoted_root}' -Action {action}"
            encoded = base64.b64encode(source.encode("utf-16-le")).decode()
            result = subprocess.run(
                ["powershell.exe", "-NoProfile", "-NonInteractive",
                 "-EncodedCommand", encoded], capture_output=True,
                timeout=20, creationflags=subprocess.CREATE_NO_WINDOW,
            )
            text = (root/"widget/action.ini").read_text(encoding="utf-16")
            self.assertEqual(result.returncode, 1 if unrelated or scenario else 0)
            self.assertFalse((root/"logs").exists())
            return text

    def test_stop_when_already_off_is_idempotent(self) -> None:
        """No state receipt or fake process should be required to report Off."""
        self.assertIn("status=stopped", self.run_fixture("Stop", False))

    def test_all_actions_refuse_unrelated_server(self) -> None:
        """Start, Stop and Toggle must reject a foreign process before any action."""
        for action in ("Start", "Stop", "Toggle"):
            with self.subTest(action=action):
                text = self.run_fixture(action, True)
                self.assertIn("status=error", text)
                self.assertIn("unrelated or ambiguous", text)

    def test_start_failure_is_not_reported_as_ready(self) -> None:
        """A launcher rejection must survive as an actionable error result."""
        text = self.run_fixture("Start", False, "failed_start")
        self.assertIn("status=error", text)
        self.assertIn("capacity rejected", text)

    def test_stale_receipt_cannot_stop_a_process(self) -> None:
        """Matching model text alone must not authorize stopping a reused PID."""
        text = self.run_fixture("Stop", False, "stale")
        self.assertIn("Saved ownership receipt does not match", text)

    def test_concurrent_controller_is_refused(self) -> None:
        """A second controller must report busy without spawning a model."""
        kernel = ctypes.windll.kernel32
        kernel.CreateMutexW.argtypes = [ctypes.c_void_p, ctypes.c_int,
                                       ctypes.c_wchar_p]
        kernel.CreateMutexW.restype = ctypes.c_void_p
        kernel.WaitForSingleObject.argtypes = [ctypes.c_void_p, ctypes.c_uint]
        kernel.ReleaseMutex.argtypes = [ctypes.c_void_p]
        kernel.CloseHandle.argtypes = [ctypes.c_void_p]
        handle = kernel.CreateMutexW(None, False, "Local\\LocalCodingLabControl")
        if not handle:
            self.fail("Could not create controller test mutex")
        acquired = kernel.WaitForSingleObject(handle, 0) == 0
        try:
            if not acquired:
                self.skipTest("Owner model action is active")
            text = self.run_fixture("Start", False, "busy")
            self.assertIn("already in progress", text)
        finally:
            if acquired:
                kernel.ReleaseMutex(handle)
            kernel.CloseHandle(handle)
