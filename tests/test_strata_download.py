"""The experimental downloader must never publish unchecked range contents."""
import hashlib
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import importlib.util
import json
from pathlib import Path
import tempfile
import threading
import unittest
from unittest.mock import patch

SOURCE = Path(__file__).resolve().parents[1] / 'experiments/strata/range_download.py'
SPEC = importlib.util.spec_from_file_location('strata_ranges', SOURCE)
ranges = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(ranges)


class RangeDownloadTests(unittest.TestCase):
    def test_explicit_q2_selection_preserves_original_default(self):
        """A Q2 request must not silently fetch the historical IQ3 shards."""
        manifest = json.loads(SOURCE.with_name('artifacts.json').read_text())
        for key in ('flash_next_candidate', 'flash_next_q2_candidate'):
            with self.subTest(key=key), tempfile.TemporaryDirectory() as folder:
                argv = ['range_download.py', '--data-dir', folder,
                        '--connections', '4']
                if key != 'flash_next_candidate':
                    argv += ['--artifact-key', key]
                with patch.object(ranges.sys, 'argv', argv), \
                        patch.object(ranges, 'fetch') as fetch:
                    self.assertEqual(ranges.main(), 0)
                artifact = manifest[key]
                self.assertEqual(fetch.call_count, 2)
                for call, expected in zip(fetch.call_args_list, artifact['files']):
                    spec, destination, connections = call.args
                    self.assertEqual(spec['sha256'], expected['sha256'])
                    self.assertIn(artifact['revision'], spec['url'])
                    self.assertTrue(destination.is_relative_to(Path(folder).resolve()))
                    self.assertEqual(connections, 4)
                receipt = json.loads((Path(folder) / 'verified-download.json').read_text())
                self.assertEqual(receipt['artifact_key'], key)

    def test_resume_and_integrity(self):
        data = bytes(range(256)) * 32
        mode = {'wrong_range': False}

        class Handler(BaseHTTPRequestHandler):
            def do_GET(self):
                start, end = map(int, self.headers['Range'][6:].split('-'))
                self.send_response(206)
                self.send_header('Content-Range', 'wrong' if mode['wrong_range'] else
                                 f'bytes {start}-{end}/{len(data)}')
                self.send_header('Content-Length', str(end - start + 1))
                self.end_headers()
                self.wfile.write(data[start:end + 1])

            def log_message(self, *_args):
                pass

        server = ThreadingHTTPServer(('127.0.0.1', 0), Handler)
        thread = threading.Thread(target=server.serve_forever, daemon=True)
        thread.start()
        original = ranges.CHUNK
        ranges.CHUNK = 1024
        spec = {'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest(),
                'url': f'http://127.0.0.1:{server.server_port}/model'}
        try:
            with tempfile.TemporaryDirectory() as folder:
                target = Path(folder) / 'model.gguf'
                target.with_name(target.name + '.part').write_bytes(data[:777])
                mode['wrong_range'] = True
                with self.assertRaisesRegex(ValueError, 'exact pinned range'):
                    ranges.fetch(spec, target, 2)
                self.assertFalse(target.exists())
                mode['wrong_range'] = False
                ranges.fetch(spec, target, 2)
                self.assertEqual(target.read_bytes(), data)
                receipt = json.loads(target.with_name(target.name + '.ranges.json').read_text())
                self.assertEqual(receipt['prefix_bytes'], 777)
                self.assertIn('verified', receipt)
                interrupted = Path(folder) / 'allocation.gguf'
                interrupted.with_name(interrupted.name + '.ranges').write_bytes(data[:777] + b'\0' * 200)
                interrupted.with_name(interrupted.name + '.ranges.json').write_text(json.dumps({
                    'sha256': spec['sha256'], 'bytes': len(data), 'prefix_bytes': 777,
                    'chunk_bytes': 1024, 'done': [], 'allocating': True}))
                ranges.fetch(spec, interrupted, 2)
                self.assertEqual(interrupted.read_bytes(), data)
                bad = Path(folder) / 'bad.gguf'
                with self.assertRaisesRegex(ValueError, 'SHA256 mismatch'):
                    ranges.fetch({**spec, 'sha256': '0' * 64}, bad, 2)
                self.assertFalse(bad.exists())
        finally:
            ranges.CHUNK = original
            server.shutdown()
            server.server_close()
            thread.join()
