# RAM, VRAM, quantization and context

## Measured capacity versus occupied tokens

The [16 October growth experiment](../reports/2026-10-16-context-growth.json)
distinguishes **configured capacity**, **occupied token cells** and **process
memory**. With 64K CPU q8 KV, the runtime reserves 680 MiB at load. Increasing input
from 1,995 to 59,955 tokens left this reservation unchanged and post-answer process
RAM near 17.88–17.89 GiB. All five requested source facts passed; the subsequent
changed-file/history answer also passed and reused 59,951 cached input tokens.

Increasing the server setting to 128K reserves 1360 MiB CPU KV at load. Recurrent
state remains 62.81 MiB, while GPU compute buffers increase 273→507 MiB. Thus
occupied context grows without a corresponding linear rise in the process
graph, but a larger configured capacity can increase multiple allocations.
At 119,943 input tokens, all-CPU KV completed in 733.063 seconds and default
mixed CPU/GPU placement in 610.016 seconds. Both recovered all five facts, but
both added a Markdown fence against the plain-JSON instruction. Updated-file
history follow-ups passed; omitting history returned UNKNOWN. These synthetic
inline probes do not certify autonomous retrieval of repository instructions.

The 128K CPU run used 18.580 GiB resident RAM and 5.104 GiB dedicated VRAM;
mixed placement used 17.477 and 6.199 GiB respectively. Private committed bytes
stayed near 24.15 GiB in both. These counters overlap different resources and
must not be added as three independent physical allocations. The GPU run left
775 MiB device VRAM free and about 1.76 GiB available commit at the reported
post-answer snapshot. Keep 64K as the working default until a larger profile
earns its place through actual workload tests.

The launcher also supports an optional `stop_min_commit_available_gib` guard.
Physical availability and Windows commit headroom are distinct constraints.
Experimental mmap profiles may set `working_set_limit_gib` to bound only the
owned server's resident pages. This is neither a commit limit nor extra memory;
it may cause page faults and slower inference. Actual guard/limit receipts are
saved beside each run. The existing working profile is unchanged.

With `working_set_reserve_gib`, the resolved cap is the smaller of the explicit
limit and currently available physical RAM minus that reserve. The new larger-model
initial trials reserve 5 GiB at preflight; the revised 80B profile reserves
7 GiB and additionally caps resident RAM at 14 GiB. These limits allow use of
more RAM only when it is actually available;
they do not assume that every process may consume the machine's full 64 GB.
The guard continues monitoring afterward because other applications can grow.

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

The selected configuration2.0 now confirms the64K allocation directly:
**680MiB attention KV =136MiB CPU +544MiB GPU**, with **62.81MiB recurrent
state =18.84MiB CPU +43.97MiB GPU**. Model buffers are4383.13MiB GPU and
16715.52MiB host; compute buffers273MiB GPU and22.36MiB host. Readiness uses
about17.0GiB processRAM/5.38GiB dedicatedVRAM; the finalist suite peaks at
18.09GiB processRAM. These are measured components, not numbers to add to an
already measured process total. Partial CPU/GPU state placement follows the
30GPU-layer profile; it does not use an all-RAM-KV flag.

In the pinned runtime, `--no-kv-offload` requests host-side KV. GPU offload flags
do not mean "put KV in RAM." Moving this relatively small cache to RAM could
recover some VRAM but uses more host memory and may slow attention. It cannot
solve dense CPU matrix multiplication or a host-RAM shortage. The new dense
Gemma 31B trial **did measure RAM KV**: 1211 MiB q8 cache at 16K, about 5.98 GiB
dedicated process VRAM, peak sampled process RAM 14.57 GiB, and 0.95 generation
tok/s before its five-minute calibration deadline. The GPU-KV attempt stopped
at its VRAM guard, so this is not a completed A/B measurement of the cache move's
speed penalty. [Trial evidence](../reports/2026-10-15-campaign.md).

The later **Qwen Q4 RAM-KV** probe also completed: 680 MiB attention KV and
62.81 MiB recurrent state on CPU, 2.43 GiB dedicated process VRAM, 21.04 GiB peak
sampled process RAM. Generation was about 13 tok/s; the coding/history prompts
took 408/242 seconds and passed their code/recall checks. The 1536 MiB expert-cache
GPU-KV profile generated about 38-39 tok/s but used 4.76 GiB dedicated VRAM and
20.34 GiB peak process RAM. The two profiles also differ in expert caching, so
this is a practical option comparison, not an isolated universal KV penalty.
For this architecture, keeping KV/state on GPU is currently preferable when it
fits. The expert cache still keeps the original host weights and does not make
context permanent.

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

Kimi Linear demonstrates a compatibility limit as well as different sizing.
The pinned runtime rejects q8 V because its value-head dimension72 is not
divisible by block32, then rejects differing K/V types. Matching f16 loads at
32K with **252 MiB KV**, **42.81 MiB recurrent state** and **949.13 MiB GPU
compute buffers**. Readiness dedicated VRAM is7.09GiB and peak process RAM
23.24GiB. Its510MiB minimum freeVRAM is too narrow to reuse that placement at
64K without a separate capacity adjustment/test. Quantized KV is not a
universally supported requirement, and active KV alone is not total memory.

Qwen3-Coder 30B at the same 32K context uses **1632 MiB q8 KV**: 816 MiB each
for K and V. Its measured balanced placement uses 5.80 GiB dedicated process
VRAM and a peak sampled 13.28 GiB process working set. A separate tokenizer
measurement finds **27,488 tokens** in the 15 actual instruction-source files
alone, excluding wrappers, tool declarations, chat history and the answer.
This supports the planned 64K private audit; it does not imply every task should
load every instruction file or that all those sources were delivered in a run.

The16October dense Gemma31 follow-up now measures **3251.25MiB CPU q8 KV at
64K**:2720MiB global plus531.25MiB sliding-window cache. Readiness dedicated
VRAM is5.648GiB; an early native-thinking snapshot has17.202GiB process RAM.
The GPU workspace alone is797.63MiB, illustrating why the old16K memory
estimate cannot be carried over unchanged. These are loading/early-run figures;
the completed public suite peaks at17.202GiB residentRAM. The private audit
peaks at19.218GiB before a documented reduction to17.202GiB and finishes normally.
[Measured dense setup](../reports/2026-10-16-gemma31.json).

`--cache-ram 0` does not disable every reuse buffer. This runtime separately
defaults to **32 context checkpoints per slot** (`--ctx-checkpoints`). The earlier
Gemma26 logs show individual full sliding-window checkpoints of about106MiB, in host
memory. Do not call that additional allocation permanent chat memory, or assume
the active attention KV figure describes the whole process. Fewer checkpoints
can change cache reuse and prefill work. Kimi uses four in the completed32K
suite, but there is no isolated checkpoint-count A/B result.

The16October Gemma31 run retains one checkpoint. Its logged serialized size
grows from3.322MiB to425.013MiB as the occupied prompt fills the sliding window,
while the active3251.25MiB KV allocation stays reserved. Old checkpoints are
replaced at the configured one-checkpoint limit. Thus some context-related
memory can grow with occupancy even though the primary KV buffers are fixed;
neither number alone is total process RAM.

Cache allocation also does not guarantee reuse. In the dense Gemma history
follow-up, the server explicitly reset cached tokens to zero and reprocessed
the prompt because its retained sliding-window checkpoint could not restore
the changed prefix. Actual template/tokenizer probes show why the default
`preserve_thinking=false` matters here: only137 leading tokens remain identical
between requests. Setting true retains10,021 identical leading tokens, adding
341 tokens to the follow-up. Counts exclude the automatically added BOS token.
The true setting has only been rendered/tokenized, not timed or quality-tested;
it is a concrete optimization hypothesis, not a measured speed improvement.
Both settings retain the source facts in the prompt. This is different from
forgetting files or running out of the configured64K capacity.

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
In the matched private audit, removing the2048 ceiling produced the exact same
answer and file-read sequence: delivered reasoning was only26-172tokens per
turn in either run. The ceiling was not reached. Raising it cannot by itself
force more reasoning; [the measured comparison](../reports/2026-10-15-campaign.md#qwen-private-reasoning-ceiling-identical-output)
retains the same25/36 score and errors.

Windows mmap has another distinction: virtual mapped size, resident process
working set and system-cached prefetched pages are different counters.
Microsoft documents that
[prefetched pages initially sit outside the process working set](https://learn.microsoft.com/en-us/windows/win32/api/memoryapi/nf-memoryapi-prefetchvirtualmemory).
Large prefetch ranges can still create system memory pressure. The16October
80B load demonstrated why limiting only process residency is insufficient:
its stock mapping attempt exhausted free memory before inference. An isolated
initial-prefetch opt-out subsequently loaded and began inference within the
same resource floors; see the [experiment](../experiments/llama-mmap-prefetch/README.md).
That trades startup pressure for demand paging. It does not turn a45GiB weight
file into a17GiB resident model or make storage as fast as RAM.

## Where the 64 GB goes with apps open

These are separate views of memory, not numbers to add together. At 19:51:50 IST
on 16 October, while the dense Gemma audit was generating:

| Counter | Observed value | Meaning |
|---|---:|---|
| Physical RAM usable by Windows | 63.91 GiB | Installed capacity after hardware reservations |
| Physical RAM available | 5.62 GiB | Headroom for Windows, apps and inference |
| Gemma process working set | 17.20 GiB | Resident process pages, including mapped weights and runtime buffers |
| Gemma private committed bytes | 10.02 GiB | A commitment counter; overlaps resident memory and is not extra RAM |
| Edge process working sets, summed | 7.97 GiB | Approximate browser footprint; shared pages can be counted more than once |
| VS Code process working sets, summed | 7.26 GiB | Approximate editor footprint, with the same shared-page caveat |
| WebView process working sets, summed | 1.59 GiB | Other embedded browser processes |
| Existing pagefile usage | 3.92 GiB | Storage backing, not additional physical RAM |

Windows therefore had about 58.29 GiB of physical memory unavailable for new
allocations in this snapshot. The process figures are not an exact partition of
that total: Windows, other applications, shared mappings and caches also consume
memory. The server's fixed 3.175 GiB active CPU KV allocation is already included
in its process footprint. Filling more tokens does not add that allocation a
second time. The owned server's resident cap was reduced during the private
audit; the intervention and unchanged commit counter are recorded separately in
[the dense result](../reports/2026-10-16-gemma31.json).

## Dense placement follow-up

At 32K capacity, Gemma31 reserves 1,360 MiB global plus 531.25 MiB sliding-window
q8 KV. A completed pair keeps that cache on CPU while changing weight placement:
all FFNs on CPU versus 14 complete repeating blocks plus output on GPU.
Short-answer generation rises from 1.18 to 1.56 tokens/s, but an 8,115-token
request stays about 7.7 minutes. Cache and weight locations are separate controls.

A third arm moves 408 + 116.88 MiB of KV onto GPU without changing weight
placement. Its 2,060-token request takes 146.109s versus 146.047s with CPU KV,
using 5.906 GiB dedicated process VRAM. The 8K attempt stops during prefill when
free device VRAM falls to 394 MiB; that answer is unscored. The additional consumer
is not identified by the available counters. GPU cache is therefore conditional
on measured benefit and headroom, not automatically preferable for every
architecture and placement. The completed CPU pair also returns UNKNOWN when
history is omitted; neither RAM nor VRAM cache supplies persistent cross-request
knowledge by itself. [Requests, buffers and outcomes](../reports/2026-10-16-dense-placement.json).
