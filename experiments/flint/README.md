# Recursive Flint experiment

Status: installation and first trial in progress, 23 October 2026. The selected
UD-IQ3_XXS is a mixed quantization, not uniform three-bit weights and not the
publisher's distilled NVFP4 release. See the [standalone report](../../docs/tasks/2026-10-23-flint/2026-10-23-recursive-flint-v0.8.0.md).

## Install without touching production

Use Python 3.11+ and an NVIDIA driver compatible with CUDA 12.4. This installs
only the selected GGUF and a separate Windows x64 runtime; no driver changes,
editor changes, process termination or inference occurs here.

```powershell
python experiments/flint/install.py --data-root E:\llm --component runtime --apply
python experiments/flint/install.py --data-root E:\llm --component model --apply
```

Remove `--apply` to preview. Downloads resume short partial files and verify
the pinned full SHA256 before publishing a weight file. An existing runtime
directory is preserved and rejected. About 18 GiB free disk is needed for the
model, downloaded runtime archives, extraction and modest headroom; use more
for results and subsequent variants. This is not the RAM requirement.

## Proposed collection

The profile is experimental. Inspect live free RAM/commit/VRAM first and run
one model at a time. Do not lower stop gates just to make a candidate score.

```powershell
python trial.py --profile flint-iq3xxs-moe36-cpukv64 --runtime-dir E:\llm\runtimes\b11838 --model-path E:\llm\models\flint-UD-IQ3_XXS.gguf --tasks experiments/flint/public-tasks.json --output local-data/flint-public-attempt1 --load-timeout 300 --smoke-timeout 90 --apply
```

Every rerun needs a fresh output directory. This collects the three unchanged
public v2 workflows at publisher temperature 1.0; the older Qwen baseline used
0.6. Native reasoning is preserved. Runtime parsing and CPU q8 KV compatibility
must pass smoke before relying on any reported output. Profile text is not
proof of actual allocation. The separate private36/coding12 suites remain
private; the report records their runner/input hashes and actual results.

`inspect_header.py` reads metadata without loading weights and saves padded
tensor-span estimates. Its figures exclude runtime/compute/cache overhead and
are not a hardware measurement. Installed file integrity is still required.

## Comparisons

- [Current comparison](../../docs/model-comparison.md)
- [Report requirements](../../docs/model-reporting.md)
- [Methodology](../../docs/methodology.md)
- [Isolated grading](../../docs/grading.md)

Preserve vendor claims separately from measured results. Mac/RTX Spark decode
numbers, especially with prefill excluded, do not predict this RTX3080's
whole-workflow latency. No production promotion without completed comparative
evidence, repeated finalist checks, and separate editor validation.
