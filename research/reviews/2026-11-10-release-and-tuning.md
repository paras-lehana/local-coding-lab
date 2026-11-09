# Release checks and tuning decisions — 10 November 2026

The owner requests additional quantization, runtime and context experiments,
including Qwen4, Qwen3.8, Flint Max and Gemma. Availability was checked against
publisher accounts and official release assets, rather than model names in
third-party headlines.

| Source checked | Finding | Local decision and limits |
|---|---|---|
| [Qwen publisher](https://huggingface.co/Qwen) and its model API | Qwen3.8 dense27B and Flash-Next exist; the official Qwen4 search returns an empty list | Flash-Next's architecture preview is not a separate Qwen4 release; do not relabel its score |
| [Recursive publisher](https://huggingface.co/RecursiveSI) | Four public repositories: Flint, INT4, INT4-GGUF and NVFP4-GGUF; no Flint Max | Keep existing Flint results and evaluate useful available precision variants. Max remains unverified/unrun |
| [Strata0.2.13](https://github.com/Niko1221/Strata/releases/tag/v0.2.13) | Control/native engine0.1.59; release discusses Qwen4 groundwork | Side-install a pinned runtime; retain old failed engine/profile evidence |
| [Strata technical details](https://github.com/Niko1221/Strata/blob/v0.2.13/docs/DETAILS.md) | Host-KV streaming, GPU-KV growth, expert residency, routing modifications and drafting are separate controls | Start static/no-draft. Keep route prior/resident bias/tail skip off for accuracy baseline. CPU-share and cache changes need measured outputs; seed alone does not guarantee identical answers |
| [Google Gemma4 QAT12B](https://huggingface.co/google/gemma-4-12B-it-qat-q4_0-gguf) | Official Apache2 text weights6,975,879,296bytes, dense48layers,256K native context | New smaller candidate while apps stay open; native context is not proof this PC can serve it at256K |
| [Google thinking documentation](https://ai.google.dev/gemma/docs/capabilities/thinking) | Native enable_thinking switch; larger variants' nonthinking template includes an empty thought channel | Validate the embedded GGUF template; do not offer an unsupported ultra/xhigh knob |
| [Python Environments issue1989](https://github.com/microsoft/vscode-python-environments/issues/1989) | Version1.42.0 starts a whole-workspace search for each created/deleted Python marker without debounce | This host showed855matching rg children of one VSCode extension host during a vendor checkout. Installed source confirms the exact pattern; the burst ended itself. The vendor/runtime/raw-data exclusions added to the local lab window do not prove a fix: later window mapping identifies the search parent as the separate home/Code workspace. No app/process killed; trigger and permanent mitigation remain unproven |

The new native Strata archive is630,783,433bytes, SHA256
`3f071a7ccbbf3dcdefed8bff777896d8dd0b580417a078154a7d2c2402ec4158`.
Its BUILD.json reports source commit`712fec6b4297`, CUDA13.0, including sm86;
the release's frontend/source checkout is`d2f096475817d4666c364c820b0ca830f751cfc5`.
These are distinct identities. The native executable hash is
`12a21cddb83e3af14c36478590676e5749b0075dedd3568e8630848f20ad819f`.
First serving qualification deliberately uses the earlier isolated ACL-corrected
frontend, making compatibility itself a measured condition. It passes two
greetings, but no coding or long-context result follows from that.

## Useful experiment dimensions

| Dimension | Controls | Decision criterion |
|---|---|---|
| Engine | Retained llama builds; side Strata0.1.59 | Supported architecture, same identified weights where feasible, complete answers and normal cleanup |
| Expert/weight placement | Explicit GPU cache, CPU layers and bounded resident pages | Measured RAM/commit/VRAM, prefill and decode; do not maximize VRAM blindly |
| Prefill |64/128 and CPU-share off/on on Flash | Separate cold/repeated/edited-prefix timings; preserve output differences |
| Graph execution | Capture/default versus no-capture | A different scheduling control, not a proven repair for0x116 |
| KV | Static GPUint8, host streaming, supported lower precision, staged context sizes | Allocation plus beginning/middle/end recall and changed-source recovery; no implied permanent memory |
| Effort | Native low/medium/xhigh on Flash and dense Qwen; native thinking on/off elsewhere | Identical task/seed/budget, executable behavior and citations, not reasoning length |
| Weight quantization | Q2 versus higher Flash precision; dense Q4/Q6; official/distinct Flint quants; Gemma QAT versus higher precision | Whole workflow correctness with artifact and sampling identity; memory refusal is unscored |
| Drafting | Off baseline, then supported MTP/DFlash if headroom allows | Actual acceptance, total wall time, output and memory; do not transfer vendor hardware headlines |

No new full-suite winner is declared. Complete matched baseline components and
repeat finalists before promotion. Raw/private receipts stay outside Git.

## Standard llama route and runtime-specific switches

The retained b12069 source advertises qwen4exp, Q2_0 tensor type42 and lazy PLE
row reads. The actual installed executable's help includes CPU expert placement,
GPU expert cache and quantized KV, but **not** the newer
`--moe-cache-cpu-share` switch described in current upstream documentation.
Do not pass it silently or pretend it was tested on b12069. The standard llama
Flash profile is a new load/compatibility experiment, not a transfer of the
Strata result. Both automatic GGUF shards must be fully hash-verified.

[llama.cpp v0.9.0](https://github.com/ggml-org/llama.cpp/releases/tag/v0.9.0)
is the current stable release link, with assets under b12110; stable and nightly
names are distinct. It lists Gemma efficient-model prefill work and Qwen4exp
state-copy changes. Those release notes do not prove gains for this12B Gemma
or this PC. A future runtime comparison needs its own pinned files and the
same initial-prefetch policy; no new llama runtime result is claimed here.

Strata0.2.13's published model list includes Flash-Next, Qwen3.6 MoE and
DeepSeekV4.1. It does not establish a dense Qwen3.8-27B backend. Keep that
dense/Strata combination unsupported unless a compatible engine is verified.

## Higher Flash precision and storage

The pinned quantizer revision's IQ3_XXS first shard is47,039,860,096bytes
(SHA256219ea929900dfa9ef091f3aa473fdba6874b65fcb36526d7d851ac9e95856d15).
Its second shard is28,800,138,432bytes and shares the exact existing Q2 PLE
shard hash316b46f3a2dbd68c900f43136ab9449f9dcc3725dfd8c794847c204bc161e113.
Thus IQ3 totals75.84decimalGB on disk, not resident RAM. Reusing an independently
verified identical shard on the same volume can avoid a duplicate download;
that does not merge CPU and GPU address spaces or prove a fit. Finish and
preserve Q2 controls before retiring its distinct37.62GB first shard. Packing,
disk headroom, native quant support and full file hashes remain launch gates.
Source: [pinned quantizer files](https://huggingface.co/ISTA-DASLab/Qwen3.8-Flash-Next-GSQ-RCO-GGUF/tree/ed59f92082b1e93c0e96d60a8b11aab089b52f09).

## Additional source-based tuning decisions

Strata's documented zero-copy/file-read-ahead/decode-gate trio and host-memory
prefill planner are Linux paths; the same section explicitly says Windows is
unchanged. Do not apply those headline gains to this native Windows run or
record an ineffective environment variable as a tested optimization.

`STRATA_PF_FUSED_Q2N=1` is a separate available sm80+ native-Q2 prefill control.
It changes prompt arithmetic and can change generated text. The publisher's
Windows/Ampere coverage is unverified and an A4000 example regressed; our3080
needs its own trial. It is prepared as a labelled arithmetic variant, not a
transparent accuracy-preserving improvement. Resident8GiB is another prepared
control with12.5GiB admission and all original stop floors.

Keep routing bias/tail skipping off in the accuracy baseline: the documented
route-prior rollback followed worse long agent results. Drafting is a distinct
future control with extra memory and measured acceptance required. Sources:
[pinned technical details](https://github.com/Niko1221/Strata/blob/v0.2.13/docs/DETAILS.md),
installed0.1.59 help and the actual pinned template (high aliases xhigh;
none becomes native thinking-off, not an unknown effort string).


## Outcome boundary

The primary-source review generated a concrete queue, not a promise of speed.
Gemma12 residency, native thinking and CPU-KV controls ran and are reported
separately. Flash resident1 timing controls ran; resident3 triggered a new
NVIDIA FECS event during hi. The queue stopped. Fused-Q2, higher residency,
other KV formats, native effort, IQ3 and the ordinary llama route did not run.
See [campaign](../../docs/tasks/2026-11-10-tuning/2026-11-10-tuning-v0.12.0.md)
and [incident](../../reports/2026-11-10-flash-fecs-stop.md).
