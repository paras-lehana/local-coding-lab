"""Summarize Flint placement estimates using the lab's existing GGUF parser.

Reads headers only, including from partial downloads. Tensor spans include
alignment padding and are estimates, not runtime memory measurements.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "scripts"))
from gguf_metadata import inspect  # noqa: E402


def main() -> None:
    """Save a header and weight-placement receipt without loading tensors."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("file", type=Path)
    parser.add_argument("--full-size", type=int, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if args.output.exists():
        raise FileExistsError(args.output)
    header = inspect(args.file, args.full_size)
    tensors = header["tensors"]
    by_type = {}
    for tensor in tensors:
        key = str(tensor["type"])
        by_type[key] = by_type.get(key, 0) + tensor["storage_span_bytes"]
    estimates = []
    total = args.full_size - header["tensor_data_start"]
    for blocks in (34, 36, 38, 40, 47, 49):
        cpu_bytes = sum(t["storage_span_bytes"] for t in tensors
                        if "_exps.weight" in t["name"]
                        and int(t["name"].split(".")[1]) < blocks)
        estimates.append({"cpu_moe_blocks": blocks,
                          "cpu_experts_gib": cpu_bytes / 2**30,
                          "other_weights_gib": (total - cpu_bytes) / 2**30})
    result = {"header": header, "padded_bytes_by_type": by_type,
              "placement_estimates": estimates,
              "note": "Weight-only estimates. KV, scratch and runtime costs are extra; embedding placement must be checked in loader logs."}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2), encoding="utf-8")
    print(json.dumps({k: result[k] for k in
                      ("padded_bytes_by_type", "placement_estimates")}, indent=2))


if __name__ == "__main__":
    main()
