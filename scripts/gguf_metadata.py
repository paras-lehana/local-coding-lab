"""Inspect GGUF metadata without importing a model or loading weight tensors."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import struct
from typing import BinaryIO, Any

FORMATS = {0: 'B', 1: 'b', 2: 'H', 3: 'h', 4: 'I', 5: 'i',
           6: 'f', 7: '?', 10: 'Q', 11: 'q', 12: 'd'}


def read_number(stream: BinaryIO, fmt: str) -> Any:
    """Read one little-endian numeric field, failing on a truncated header."""
    size = struct.calcsize('<' + fmt)
    data = stream.read(size)
    if len(data) != size:
        raise ValueError('Truncated GGUF metadata')
    return struct.unpack('<' + fmt, data)[0]


def read_value(stream: BinaryIO, kind: int, retain: bool) -> Any:
    """Skip large tokenizer arrays while retaining selected scalar metadata."""
    if kind in FORMATS:
        return read_number(stream, FORMATS[kind])
    if kind == 8:
        size = read_number(stream, 'Q')
        if size > 32 * 1024**2:
            raise ValueError('Unexpected metadata string size')
        if not retain:
            stream.seek(size, 1)
            return None
        data = stream.read(size)
        if len(data) != size:
            raise ValueError('Truncated GGUF string')
        return data.decode('utf-8', errors='replace')
    if kind == 9:
        subtype, count = read_number(stream, 'I'), read_number(stream, 'Q')
        if count > 2_000_000 or subtype == 9:
            raise ValueError('Unexpected metadata array')
        for _ in range(count):
            read_value(stream, subtype, False)
        return {'array_type': subtype, 'length': count} if retain else None
    raise ValueError(f'Unknown GGUF metadata type {kind}')


def inspect(path: Path, total_bytes: int | None = None) -> dict:
    """Return architecture/template fields while leaving tensor bytes unread."""
    with path.open('rb') as stream:
        if stream.read(4) != b'GGUF':
            raise ValueError('Not a GGUF file')
        version = read_number(stream, 'I')
        if version not in (2, 3):
            raise ValueError('Unsupported GGUF version')
        tensors, count = read_number(stream, 'Q'), read_number(stream, 'Q')
        if count > 10000:
            raise ValueError('Unexpected metadata count')
        result = {'gguf_version': version, 'tensor_count': tensors}
        for _ in range(count):
            key = read_value(stream, 8, True)
            kind = read_number(stream, 'I')
            keep = not key.startswith('tokenizer.') or 'chat_template' in key
            value = read_value(stream, kind, keep)
            if keep:
                result[key] = value
        if stream.tell() > path.stat().st_size:
            raise ValueError('Metadata extends beyond available bytes')
        result['metadata_end_bytes'] = stream.tell()
        if tensors > 100000:
            raise ValueError('Unexpected tensor count')
        inventory = []
        for _ in range(tensors):
            name = read_value(stream, 8, True)
            dimensions = read_number(stream, 'I')
            if dimensions > 8:
                raise ValueError('Unexpected tensor dimensions')
            shape = [read_number(stream, 'Q') for _ in range(dimensions)]
            kind, offset = read_number(stream, 'I'), read_number(stream, 'Q')
            inventory.append({'name': name, 'shape': shape, 'type': kind, 'offset': offset})
        alignment = result.get('general.alignment', 32)
        data_start = (stream.tell()+alignment-1)//alignment*alignment
        result['tensor_data_start'] = data_start
        if total_bytes is not None:
            ordered = sorted(inventory, key=lambda item: item['offset'])
            for i, item in enumerate(ordered):
                end = ordered[i+1]['offset'] if i+1 < len(ordered) else total_bytes-data_start
                item['storage_span_bytes'] = end-item['offset']
                if item['storage_span_bytes'] < 0:
                    raise ValueError('Tensor inventory exceeds declared file size')
            result['tensor_storage_note'] = 'Spans include alignment padding; not runtime allocation measurements.'
        result['tensors'] = inventory
        return result


def main() -> None:
    """Save selected metadata as an evidence file, not a model-load claim."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('model', type=Path)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--total-bytes', type=int)
    args = parser.parse_args()
    if args.output.exists():
        parser.error('Output already exists')
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(inspect(args.model, args.total_bytes), indent=2),
                           encoding='utf-8')


if __name__ == '__main__':
    main()
