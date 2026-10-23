# Recursive Flint experiment

Status: evaluated 23–24 October 2026; tested weights retired, evidence and
reproducible installer retained. The selected
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

## Collection and observed limits

The profile is experimental. Inspect live free RAM/commit/VRAM first and run
one model at a time. Do not lower stop gates just to make a candidate score.

```powershell
python trial.py --profile flint-iq3xxs-moe38-gpukv64 --runtime-dir E:\llm\runtimes\b11838 --model-path E:\llm\models\flint-UD-IQ3_XXS.gguf --tasks experiments/flint/public-tasks.json --output local-data/flint-public-attempt1 --load-timeout 300 --smoke-timeout 90 --apply
```

Every rerun needs a fresh output directory. This collects the three unchanged
public v2 workflows at publisher temperature 1.0; the older Qwen baseline used
0.6. Native reasoning is preserved. Runtime parsing and the selected q8 KV placement
must pass smoke before relying on any reported output. Profile text is not
proof of actual allocation. The separate private36/coding12 suites remain
private; the report records their runner/input hashes and actual results.

The original CPU-KV profile and its 2,048-token reasoning-cap variant both
reach the router's 20-minute deadline. The cap produces visible planning text;
it does not establish a usable final answer. The GPU-KV profile above allocates
about 0.96 GiB of q8 KV on GPU and moves two additional expert blocks to CPU to
make room. Its router finishes in 523 seconds and scores 39/40 after isolated
checks, but TS/SQL reaches the tool limit and history exhausts its output budget.
It is a reproducible experiment, not a recommended production replacement.

The private audit scores 29/36. Eleven of twelve direct coding tasks produce
complete answers and pass all 374 frozen checks; CSV reaches its output limit
without code. An additional post-review check exposes acceptance of NaN TTL.
Passing the frozen tests is not a bug-free guarantee.

`history-diagnostic-tasks.json` is a separately declared follow-up to the
4,096-output-token history failure: identical questions, 8,192 output tokens,
same 1,200-second whole-workflow deadline. Use a fresh output directory. Its
result remains separate from the frozen scorecard. The fresh-server diagnostic
completes in 328.016 seconds and scores 8/8, without exercising the unavailable
ledger error. It does not establish maximum-context or editor performance.

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
