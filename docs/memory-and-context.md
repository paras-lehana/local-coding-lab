# RAM, VRAM, quantization and context

| Concept | Changes | Does not guarantee |
|---|---|---|
| Weight quantization | Stored parameter precision and footprint | Correct syntax or reasoning at Q6/Q8; automatic failure at 3-bit |
| KV/state precision | Representation of cached attention/recurrent state | Perfect recall of every file |
| Layer/expert placement | Which device stores and computes model components | A universal safe number of GPU layers |
| Context length | Maximum token workspace exposed to a request/slot | Permanent history or automatic instruction-file loading |
| Prompt/slot cache | Reuse of eligible computation/state | A durable searchable repository memory |
| GPU expert cache | Copies of CPU-resident experts cached in VRAM | Removal of the original CPU weights |

The Windows monitor also records **commit limit and available commit** through
`GlobalMemoryStatusEx`. These values can reflect a tighter limit on the calling
process; they are not a separate measurement of system-wide commit when such a
limit applies. See [Microsoft's field definitions](https://learn.microsoft.com/en-us/windows/win32/api/sysinfoapi/ns-sysinfoapi-memorystatusex).
Commit
is a separate allocation constraint from physical RAM and GPU VRAM; a machine
can have free physical memory while much of its commit allowance is reserved.
The later unexpected-shutdown heartbeat reported 92.1% commit, but did not
establish that commit exhaustion caused the failure. The new telemetry improves
future diagnosis; it is not evidence that the restart was fixed. WDDM shared
GPU memory overlaps system RAM and must not be added as independent capacity.

The actual Qwen3.6 32K diagnostic allocated **340 MiB attention KV** plus
**62.81 MiB recurrent state**. KV split was 68 MiB CPU / 272 MiB GPU. A simple
doubling gives 680 MiB attention KV at 64K; state does not necessarily scale
the same way. A generic claim that every model needs 16 GB KV at 32K is wrong.
Architecture, layers, heads, dimensions, precision, slots and backend all matter.

In the pinned runtime, `--no-kv-offload` requests host-side KV. GPU offload flags
do not mean "put KV in RAM." Moving this relatively small cache to RAM could
recover some VRAM but uses more host memory and may slow attention. It cannot
solve dense CPU matrix multiplication or a host-RAM shortage. The new dense
Gemma 31B trial **did measure RAM KV**: 1211 MiB q8 cache at 16K, about 5.98 GiB
dedicated process VRAM, peak sampled process RAM 14.57 GiB, and 0.95 generation
tok/s before its five-minute calibration deadline. The GPU-KV attempt stopped
at its VRAM guard, so this is not a completed A/B measurement of the cache move's
speed penalty. [Trial evidence](../reports/2026-10-15-campaign.md).

`--gpu-layers all --cpu-moe` completed the measured Qwen placement experiment:
offload eligible non-expert computation while keeping routed experts on CPU.
It may increase host memory
because experts previously on GPU move back to RAM. Shared experts, embeddings,
output tensors and compute buffers must be checked from actual loader logs.
Do not label all layers equally sized or reuse a 28-layer limit across families.
See [pinned flag definitions](https://github.com/ggml-org/llama.cpp/blob/b2f036c0f138414dedc987446f1d9d802f920275/common/arg.cpp).

The measured Gemma 26B balanced profile keeps experts from 24 blocks in RAM and
the final six on GPU. At 32K its active q8 KV is only **473 MiB on the GPU**,
while readiness dedicated process VRAM is **4.97 GiB**. Model host buffers are
10379 MiB; total resident RAM also includes runtime overhead and context
checkpoints. These figures are specific to this artifact and placement.
At 64K with the same placement, the measured cache is **813 MiB**: 680 MiB
global plus 133 MiB sliding-window, all on GPU. Readiness dedicated VRAM is
**5.31 GiB**. Doubling context did not double every cache component; recall
quality is being tested separately from successful allocation.

The pinned Gemma header has 25 sliding-window and five global-attention blocks.
Use those actual arrays and measured padded allocation, rather than the external
research's incorrect 26/four split, when estimating a larger context.

GLM-4.7-Flash's measured 32K MLA cache is **898.88 MiB**, reported as
K q8_0 = 898.88 MiB and V q8_0 = 0.00 MiB. MLA uses shared latent storage;
the zero separate V allocation is not evidence that the conversation was
discarded. Its first Q4 balanced load uses about 4.90 GiB dedicated process
VRAM and 13.40 GiB sampled process RAM. Do not apply the Gemma or Qwen cache
formula to this architecture, or add a second assumed value cache to the log.

Qwen3-Coder 30B at the same 32K context uses **1632 MiB q8 KV**: 816 MiB each
for K and V. Its measured balanced placement uses 5.80 GiB dedicated process
VRAM and a peak sampled 13.28 GiB process working set. A separate tokenizer
measurement finds **27,488 tokens** in the 15 actual instruction-source files
alone, excluding wrappers, tool declarations, chat history and the answer.
This supports the planned 64K private audit; it does not imply every task should
load every instruction file or that all those sources were delivered in a run.

`--cache-ram 0` does not disable every reuse buffer. This runtime separately
defaults to **32 context checkpoints per slot** (`--ctx-checkpoints`). Gemma's
logs show individual full sliding-window checkpoints of about 106 MiB, in host
memory. Do not call that additional allocation permanent chat memory, or assume
the active attention KV figure describes the whole process. Fewer checkpoints
can change cache reuse and prefill work; that tuning has not yet been measured.

Context remains useful only when the client actually sends the relevant files,
instructions and history. A CLAUDE import, a Copilot instruction rule and an
ordinary Markdown link have different loading behavior. The benchmark records
exact source delivery and successful reads. Opening a file tab is not proof its
contents reached the model. Editing a file requires a fresh read to avoid stale
answers. The separate `context-v1` scenarios now test changed-file re-reading
and earlier ledger facts; core `router-v1` does not. The larger case contains
43,228 Gemma ledger tokens before chat overhead. Its 64K follow-up recovered all
six final facts and the correct record count at a largest input of 52,231 tokens,
in 631.563 seconds. That is a two-phase long-document result, not an arbitrary
many-turn coding-session guarantee. Long-term project knowledge belongs in
versioned notes plus retrieval.

Native Qwen3.6 thinking on/off differs from llama.cpp's `reasoning_budget_tokens`.
The latter was locally verified as a ceiling of 0/512/2048 tokens; it is not a
trained "xhigh" level. A longer budget can improve a case and still miss files.
Always count prefill, thinking, tool rounds and final text toward the deadline.
