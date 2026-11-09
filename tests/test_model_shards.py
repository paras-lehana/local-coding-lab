"""Split-artifact integrity must fail before model loading or partial downloads."""
import hashlib
from pathlib import Path
import tempfile
from types import SimpleNamespace
import unittest
from unittest.mock import patch

import lab


def spec():
    """Two tiny inert files stand in for publisher-pinned GGUF shards."""
    return {"repo": "publisher/model", "revision": "pinned-revision",
            "filename": "model-00001-of-00002.gguf", "remote_filename": "Q2/model-00001-of-00002.gguf",
            "bytes": 5, "sha256": hashlib.sha256(b"first").hexdigest(),
            "additional_files": [{"filename": "model-00002-of-00002.gguf",
                "remote_filename": "Q2/model-00002-of-00002.gguf", "bytes": 6,
                "sha256": hashlib.sha256(b"second").hexdigest()}]}


class ModelShardTests(unittest.TestCase):
    def test_missing_or_corrupt_second_shard_rejects(self):
        with tempfile.TemporaryDirectory() as temporary:
            directory = Path(temporary)
            metadata = spec()
            first = directory / metadata["filename"]
            first.write_bytes(b"first")
            with self.assertRaises(FileNotFoundError):
                lab.verify_model_files(first, metadata)
            second = directory / metadata["additional_files"][0]["filename"]
            second.write_bytes(b"broken")
            with self.assertRaisesRegex(ValueError, "SHA256"):
                lab.verify_model_files(first, metadata)
            second.write_bytes(b"second")
            lab.verify_model_files(first, metadata)

    def test_local_escapes_duplicates_and_missing_pin_reject(self):
        for name in ("../escape", "..\\escape", "C:escape", "/escape", "bad.",
                     "MODEL-00001-OF-00002.GGUF"):
            with self.subTest(name=name):
                metadata = spec()
                metadata["additional_files"][0]["filename"] = name
                with self.assertRaises(ValueError):
                    lab.model_artifacts(metadata)
        metadata = spec()
        del metadata["additional_files"][0]["sha256"]
        with self.assertRaises(KeyError):
            lab.model_artifacts(metadata)

    def test_remote_subdirectory_and_both_downloads_preserved(self):
        with tempfile.TemporaryDirectory() as temporary, patch("lab.download") as download:
            lab.download_model_files(spec(), Path(temporary))
            self.assertEqual(download.call_count, 2)
            for call in download.call_args_list:
                artifact, target = call.args
                self.assertIn("/pinned-revision/Q2/", artifact["url"])
                # Windows may expand an 8.3 TEMP alias while resolving siblings.
                # Compare the actual directory, not two spellings of its path.
                self.assertTrue(target.parent.samefile(temporary))

    def test_whole_set_capacity_refuses_before_first_download(self):
        with tempfile.TemporaryDirectory() as temporary, patch("lab.download") as download:
            with patch("lab.shutil.disk_usage", return_value=SimpleNamespace(free=512*1024**2+7)):
                with self.assertRaisesRegex(ValueError, "whole model set"):
                    lab.download_model_files(spec(), Path(temporary))
            download.assert_not_called()

    def test_existing_first_and_partial_second_reduce_required_capacity(self):
        with tempfile.TemporaryDirectory() as temporary, patch("lab.download") as download:
            directory = Path(temporary)
            metadata = spec()
            (directory / metadata["filename"]).write_bytes(b"first")
            (directory / (metadata["additional_files"][0]["filename"] + ".part")).write_bytes(b"sec")
            with patch("lab.shutil.disk_usage", return_value=SimpleNamespace(free=512*1024**2+3)):
                lab.download_model_files(metadata, directory)
            self.assertEqual(download.call_count, 2)


if __name__ == "__main__":
    unittest.main(verbosity=2)
