"""A frontend retry must not silently replace the measured native engine."""
import importlib.util
from pathlib import Path
import sys
import unittest


SOURCE = Path(__file__).resolve().parents[1] / "experiments/strata/guard.py"
SPEC = importlib.util.spec_from_file_location("strata_guard", SOURCE)
guard = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(guard)


class NativeIdentityTests(unittest.TestCase):
    """Exercise lifetime boundaries without creating an inference process."""

    def setUp(self) -> None:
        """Use portable absolute paths for Windows and Linux CI."""
        self.exe = str(Path(sys.executable).resolve())
        self.engine = {"pid": 41, "created": 100.0, "exe": self.exe}

    def test_delayed_start_then_stable(self) -> None:
        """Frontend startup can precede the first unchanged engine."""
        self.assertIsNone(guard.track_native_identity([], self.exe, None))
        first = guard.track_native_identity([self.engine], self.exe, None)
        self.assertEqual(first, self.engine)
        again = guard.track_native_identity([self.engine], self.exe, first)
        self.assertEqual(again, first)

    def test_exit_is_not_a_new_startup_window(self) -> None:
        """Once observed, losing the native process fails the run."""
        with self.assertRaisesRegex(RuntimeError, "exited"):
            guard.track_native_identity([], self.exe, self.engine)

    def test_pid_replacement_and_reuse_fail(self) -> None:
        """Neither a new PID nor a reused PID may inherit benchmark state."""
        for change in ({"pid": 42}, {"created": 101.0}):
            with self.subTest(change=change):
                replacement = self.engine | change
                with self.assertRaisesRegex(RuntimeError, "changed"):
                    guard.track_native_identity(
                        [replacement], self.exe, self.engine
                    )

    def test_simultaneous_engines_fail(self) -> None:
        """An overlapping restart also invalidates process attribution."""
        replacement = self.engine | {"pid": 42, "created": 101.0}
        with self.assertRaisesRegex(RuntimeError, "Multiple"):
            guard.track_native_identity(
                [self.engine, replacement], self.exe, self.engine
            )

    def test_same_filename_elsewhere_does_not_qualify(self) -> None:
        """Executable identity uses the whole path, not its basename."""
        peer = self.engine | {
            "exe": str(Path(self.exe).parent / "other" / Path(self.exe).name)
        }
        self.assertIsNone(guard.track_native_identity([peer], self.exe, None))
        with self.assertRaisesRegex(RuntimeError, "exited"):
            guard.track_native_identity([peer], self.exe, self.engine)


if __name__ == "__main__":
    unittest.main()
