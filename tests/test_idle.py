"""Check native idle launch boundaries without loading a model."""
import argparse
import contextlib
import io
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

import lab


class IdleLaunchTests(unittest.TestCase):
    """Idle controls must not bypass the existing profile and runtime plan."""

    def arguments(self, folder: str, seconds: int) -> argparse.Namespace:
        """Build a non-mutating launch plan against a temporary runtime."""
        return argparse.Namespace(
            profile="qwen36-mapped-editor128-cpukv", experimental=True,
            runtime_dir=folder, model_path=str(Path(folder)/"model.gguf"),
            port=8080, apply=False, idle_seconds=seconds,
        )

    def test_idle_plan_keeps_model_and_memory_settings(self) -> None:
        """Idle mode must preserve CPU KV, context and expert placement."""
        with tempfile.TemporaryDirectory(prefix="spaced runtime ") as folder:
            Path(folder, "llama-server.exe").touch()
            output = io.StringIO()
            with contextlib.redirect_stdout(output):
                lab.run_server(self.arguments(folder, 1800), Path(folder))
            command = output.getvalue()
            for setting in ("--sleep-idle-seconds 1800", "--no-kv-offload",
                            "--ctx-size 131072", "--n-cpu-moe 37"):
                self.assertIn(setting, command)
            self.assertFalse(Path(folder, "runs").exists())

    def test_invalid_idle_limits_stop_before_launch(self) -> None:
        """Zero and excessive intervals must not accidentally disable sleep."""
        for seconds in (0, -1, 86401):
            with self.subTest(seconds=seconds):
                with self.assertRaisesRegex(ValueError, "Idle timeout"):
                    lab.run_server(self.arguments("unused", seconds),
                                   Path("unused"))

    def test_duplicate_idle_setting_is_rejected(self) -> None:
        """A CLI override must not silently conflict with a frozen profile."""
        with patch.object(lab, "read_json", return_value={
                "args": ["--sleep-idle-seconds", "60"]}):
            with self.assertRaisesRegex(ValueError, "already specifies"):
                lab.run_server(self.arguments("unused", 1800), Path("unused"))
