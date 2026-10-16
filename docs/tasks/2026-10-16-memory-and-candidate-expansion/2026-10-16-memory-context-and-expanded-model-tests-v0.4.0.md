# Memory, growing context and the remaining candidates

Status: in progress, 16 October 2026 (Asia/Kolkata). This report extends the
15 October campaign; it does not change its historical results.

| Owner point | Status | Evidence and next step |
|---|---|---|
| RAM use and KV growth | Measured | 2K–120K occupancy, 64K/128K reservations, CPU/GPU placement, retained and omitted history. |
| Qwen3-Coder-Next 80B | Tested; private audit failed | Python6/6, TS4/6, SQL FK failure; history passes. Private audit reaches16 tool turns without a final answer. |
| Gemma 4 31B dense | Downloading | Native-thinking publisher sampling and revised64K RAM/GPU placement; quality collection pending. |
| Qwen3.6 Q6 | Queued | Attempt mapping/placement appropriate to current headroom, then matched quality checks. |
| Independent research and reasoning | In progress | Re-read supplied research and verify runtime behavior and publisher facts. |

## Decisions and constraints

The owner now accepts longer experiments. The former 1200-second practical
criterion remains historical and the default for ordinary runs; this campaign
may explicitly allow up to six hours per complete prompt. This is a collection
ceiling, not a claim that six-hour turns are desirable. Applications remain
open. One inference process runs at a time. Resource and hardware-event monitors
remain active. No driver, clock, BIOS or pagefile settings change.

The initial snapshot has 63.91 GiB physical RAM, about 21.15 GiB available and
42.76 GiB occupied, with no llama-server running. Device VRAM is 3266 MiB used,
6788 MiB free. These are time-specific observations, not model allocations.
E: is a WD_BLACK SN770 NVMe drive. Windows already has a 21 GiB pagefile;
file-backed model mapping and anonymous committed memory must be distinguished.

## Experimental reasoning

KV token occupancy need not equal dynamically allocated bytes. A server can
reserve capacity at load, then fill it as context grows. Recurrent state,
checkpoints, scratch buffers and mapped weights also affect process memory.
Measure these separately rather than infer context retention from RAM growth.

File-backed mapping is worth trying for the 80B and Q6 artifacts when resident
weights exceed available RAM. A slow page-faulting run is not the same as a
resident model, and a load failure is not a quality score. Dense Gemma requires
completed code and instruction checks under the expanded time allowance.

## Validation and raw evidence

### First measured context sweep

The unchanged Qwen Q4 weight placement with all KV/state on CPU allocated
680 MiB q8 attention KV for 65,536 cells and 62.81 MiB recurrent state at load.
The initial larger-context load allocates 1360 MiB for 131,072 cells while the
recurrent allocation remains 62.81 MiB. It also increases GPU compute buffers
from 273 to 507 MiB: KV is not the only context-dependent allocation.

| Actual input tokens | Whole prompt seconds | Process RAM GiB after answer | Dedicated VRAM GiB | Exact five-fact JSON |
|---:|---:|---:|---:|---|
| 1,995 | 15.312 | 17.881 | 4.875 | Pass |
| 15,928 | 88.500 | 17.884 | 4.875 | Pass |
| 31,936 | 178.531 | 17.889 | 4.875 | Pass |
| 59,955 | 345.984 | 17.893 | 4.875 | Pass |

The follow-up retained all three source markers and applied runtime revision2
and retryLimit0 in 15.047 seconds. The server reused 59,951 input tokens and
processed only 116 new tokens. That demonstrates reuse of delivered chat history,
not permanent memory of files that the client never supplied. After this follow-up
the process used about 18.02 GiB RAM.

At 128K configured capacity, the all-CPU KV profile completed119,943 input tokens
in 733.063 seconds (12m13s):709.020 seconds input processing,169.17 input tokens/s,
and2.69 generated tokens/s. All five facts were correct, but the answer included
a Markdown code fence despite the plain-JSON instruction. Recall passes;
strict formatting fails. The changed-revision follow-up completed in 26.563s
with correct facts and the same formatting mistake. Removing the supplied
history produced `UNKNOWN` in 1.094s, as requested. A cache is not independent,
permanent knowledge of a conversation the client omitted.

Resident process RAM stayed around 18.45–18.59 GiB during the long input. Free
physical memory remained above 4 GiB, while available Windows commit approached
1.28 GiB. These are separate constraints: sufficient free physical RAM does not
imply sufficient commit allowance. The existing pagefile was not changed.

The GPU-offloaded 128K counterpart completed too. Only cache/state placement
changes relative to CPU 128K; both use the same weights and layer placement.
Its GPU compute buffer is 507 MiB too. The default offload follows layer placement,
so this comparison is all-CPU KV versus mixed CPU/GPU KV. The latter allocates
272 MiB KV on CPU and 1088 MiB on GPU; recurrent state splits 18.84/43.97 MiB.

| At 119,943 input tokens | All KV/state on CPU | Default mixed placement |
|---|---:|---:|
| Whole request | 733.063s | 610.016s |
| Input processing | 709.020s /169.17 tok/s | 594.367s /201.80 tok/s |
| Generation | 2.69 tok/s | 4.15 tok/s |
| Resident process RAM after answer | 18.580 GiB | 17.477 GiB |
| Dedicated process VRAM | 5.104 GiB | 6.199 GiB |
| Private committed bytes | 24.150 GiB | 24.146 GiB |
| Correct source facts | 5/5 | 5/5 |
| Plain JSON instruction | Failed: code fence | Failed: code fence |
| Updated-file/history follow-up | 26.563s, correct facts | 17.141s, correct facts |
| History omitted | UNKNOWN | UNKNOWN |

The GPU follow-up reused 119,939 input tokens and processed 121 new ones. This
shows the benefit of a retained prefix, not permanent file memory. The updated
file was supplied inline in these probes; real tool discovery is assessed
separately. Recall requests used temperature 0 and reasoning budget 0 to isolate
memory behavior; these are not native-thinking coding scores. All three context
servers stopped cleanly. Raw measurements are summarized in
[the public result](../../../reports/2026-10-16-context-growth.json).

Private commit stayed almost unchanged while resident RAM moved to VRAM.
Do not add that commit counter to RAM and VRAM as another physical allocation.
The measured KV/state move predicts about 1.105 GiB less CPU allocation and
the observed resident difference is 1.103 GiB. The remaining model weights,
runtime and desktop applications are much larger than this cache trade-off.

My recommendation from this pair is to keep GPU cache placement when headroom
allows, and use CPU KV to recover VRAM when necessary. 128K is an optional long
input profile, not automatically a better everyday default. At 120K the GPU
run left only 775 MiB device VRAM free and about 1.76 GiB available commit, despite
6.44 GiB physical RAM available. 64K remains the conservative working profile
pending the remaining candidate and editor comparisons.

The much smaller change in resident RAM within a fixed context follows from
preallocation. Increasing the configured capacity changes the reservation;
filling that capacity changes occupied cells. The observed fixed buffer is
consistent with the [pinned runtime allocation code](https://github.com/ggml-org/llama.cpp/blob/b2f036c0f138414dedc987446f1d9d802f920275/src/llama-kv-cache.cpp).
Do not infer model weights, reserved capacity and token occupancy from a single
Task Manager number. WDDM shared memory overlaps RAM and is not added again.

Windows exposes physical and commit totals; process working sets overlap shared
pages and cannot simply be summed for an exact whole-system breakdown. Hyper-V
memory enumeration was denied by the current token, so no precise VM allocation
is claimed. No permissions, VM settings or apps were changed.

### Tooling validation checkpoint

25 offline tests passed in 11.147 seconds, including whole-request cancellation,
explicit longer-deadline propagation, commit-headroom rejection and a read-back
test of a resident-memory bound on an owned disposable child. Three PowerShell
scripts parsed successfully; public-content audit reported 0 findings in 125 files.
These development checks overlapped inference, so timings describe desktop use.

The resident-memory bound uses the Windows
[working-set API](https://learn.microsoft.com/en-us/windows/win32/api/memoryapi/nf-memoryapi-setprocessworkingsetsizeex)
only on the server process owned by the launcher. It does not cap total commit,
reserve extra RAM, modify other apps, or change the pagefile. This is an
experimental paging profile, not a speed or stability guarantee.

Before candidate inference, unloaded desktop RAM varied around 19–23 GiB.
The mapped candidate profiles therefore accept at least 16 GiB free, derive
their resident bound from current free RAM minus 5 GiB, and retain the 2.5 GiB
physical / 1 GiB commit stop floors. Dense Gemma also uses mapped CPU weights
to reduce anonymous weight commit; this differs from its old latency-only
calibration. Exact caps and buffer placement will be recorded per load.

Raw local evidence: `local-data/2026-10-16-expansion/`. Public aggregate results
will be added after reviewing complete answers. Existing working profiles and
baseline weights are retained. No new model is promoted merely for loading.

## Independent interpretation of the supplied research

### Coder-Next first load and isolated loader experiment

The full 48,528,320,544-byte Q4 artifact passed SHA256 verification after three
bounded download resumptions. Its first stock-runtime load did not reach
inference. Within about five seconds, free physical RAM fell to 0.115 GiB and
available commit to 0.125 GiB, while server working set was only 0.329 GiB.
The guard terminated the owned process and memory recovered immediately.
There was no new WHEA event in the inspected interval. This is an unscored load
failure, not evidence of a coding defect or a diagnosis of earlier restarts.

Source inspection identifies whole-file `PrefetchVirtualMemory` during Windows
mmap initialization as a plausible cause. The process working-set maximum did
not prevent that system-wide load peak. A six-line opt-in change at the same
pinned commit disables initial mmap prefetch; the original runtime is preserved.
Only `llama.dll` is rebuilt with MSVC; stock CUDA/CPU backends remain byte-identical.
An explicit runtime identity, DLL hash and environment receipt prevent treating
this experiment as a stock result. Startup monitoring now samples every second
for the first two minutes. All existing resource floors remain unchanged.

The isolated build compiles and recognizes CUDA. Tiny CPU/GPU greedy controls
produce byte-identical output across stock, modified-default and modified-opt-in
runtimes; verbose logs confirm the opt-in executes during mmap. These controls
are not a complete numerical-equivalence proof. A guarded Qwen control precedes
the next80B load. Candidate answers and grading remain pending; the working
model selection is unchanged.

The guarded Qwen control subsequently completed its API smoke in1.25seconds
and stopped normally. Coder-Next then loaded, completed its smoke, and started
the frozen coding suite. Its loader reports42,961.83MiB CPU-mapped weights,
4,455.58MiB GPU weights,816MiB CPU KV,75.38MiB recurrent state and519MiB GPU
compute buffer. Resident RAM is bounded around17.64GiB, leaving about6GiB free
in the early coding run; mapped size is not resident size. System telemetry
shows substantial paging/disk reads. The changed-runtime result supports the
prefetch explanation, but compiler and desktop-state differences prevent
claiming a fully isolated causal proof. Full answers and grades are pending.
The [patch and reproduction notes](../../../experiments/llama-mmap-prefetch/README.md)
are public; binaries and raw host logs remain local.

The first public Python/instruction answer completed in793.828seconds across
two tool turns. It read all seven fixture files, selected v2 rules, distinguished
links from supplied contents and did not invent absent service facts. Its
implementation subsequently passed all six independent Python contract groups.
One generated test incorrectly expects an empty dict
override to erase nested defaults, and the answer calls its nine test methods
seven. Diagnosis also omits an explicit original dict/scalar update failure.

For the final turn, uncached prefill was3.02tokens/s and generation5.28tokens/s.
Sampled whole-system reads averaged368MiB/s during that prefill and140MiB/s
during generation; these include other applications. GPU utilization samples
averaged14%/30%. This supports a paging bottleneck, not a theory that a larger
KV cache or artificial reasoning-effort label would fix the delay. Readiness
dedicated process VRAM was5.097GiB; desktop VRAM use is additional.

Before its first load, dense Gemma's prepared profile reduces context checkpoints
from four to one. Earlier dense logs measured531.25MiB of sliding-window state,
far more than Qwen's62.81MiB recurrent state. Fewer retained checkpoints avoid
potential extra host copies while keeping the active64K context; they can reduce
prefix-reuse opportunities. This is a reasoned preparation, not a measured speed
improvement. The Q4/Q6 pair keeps identical placement and modified runtime.

The TypeScript/SQLite answer completed in561.812seconds across seven turns and
honestly lists all six files read. Strict TypeScript compiles, but only4/6 behavior
groups pass: non-plain objects and fractional counts are accepted. SQLite fails
with a foreign-key constraint error while dropping the referenced table. Source
review also finds that it recreates global external_id uniqueness instead of
the required tenant/external composite constraint. A failed migration is not
six independently observed failed assertions.

The model's nine Python unittest methods pass8/9 when invoked. The initial direct
script run executed no tests because the provided block has no main entrypoint;
that original result is preserved. A separate execution adapter adds only
`unittest.main`, with assertions and implementation unchanged. This is normal
test invocation, not a repair of the wrong assertion. Isolation preflights pass;
generated code sees only the selected read-only files and no host drives, homes
or network. Grading briefly overlaps context-test prefill, which is recorded as
a timing caveat. These first answers do not establish an80B quality upgrade;
history and the actual-instruction audit remain pending.

At13:15:17 the physical-memory guard stopped the model with2.269GiB free RAM.
The history scenario was383.359seconds into collection and is unscored; the
controller correctly did not proceed to the private audit. The process working
set stayed17.638GiB and private allocation7.531GiB while available system memory
fell from9.6GiB to2.27GiB. This does not identify the responsible outside-process
allocation. WSL grading overlapped earlier in that interval and is a possible
contributor; no per-process history was available to assign causality. No new
WHEA event or reboot was found. A progress update based on a stale log line was
corrected after checking the actual stop receipt.

The new recovery profile limits resident RAM to the smaller of14GiB and current
free RAM minus7GiB. It keeps the same resource stop floors, moves one additional
expert block to CPU (46), moves KV/state to GPU and raises microbatch128to256.
This is a practical multi-variable recovery, not an isolated cache-speed claim.
It repeats only the interrupted history case before the frozen private audit.
No grading, builds or model downloads overlap this retry. The private observer
now records process-family memory totals as well as system I/O. Prior failed
and completed evidence remains intact; applications are not closed.

The recovery history case completed normally in1177.594seconds (19m38s), with
maximum input10,102tokens. `READY120` and all six final facts are correct;
the model re-reads runtime revision2/retries0 and honestly lists only that
follow-up read. It also recovers from a mistyped `.clude/CLAUDE.md` path by
requesting the correct path. It does not attempt the unavailable-ledger read,
so that separate failure-recovery behavior is not demonstrated. This10K case
does not establish52K/128K or permanent-memory performance.

The recovery loader records43,984.94MiB CPU-mapped weights,3459.58MiB GPU weights,
816MiB GPU KV,75.38MiB GPU recurrent state and885MiB GPU compute. The actual
public-run resident cap is12.331GiB and readiness dedicatedVRAM5.343GiB.
It stops normally before a fresh private-audit load. That load uses a14GiB
resident maximum derived from its own current preflight. The actual-instruction
audit is now running; its answer and36-point assessment remain pending.

The report is a useful hypothesis list, not a verified experiment log. Today's
measurements support its small Qwen cache estimate, but contradict the earlier
chat advice that 128K always requires tens of GiB of KV. Cache shape depends on
the architecture; dense versus MoE alone does not determine it. Native context
capacity also does not guarantee retrieval accuracy, instruction compliance,
or that an editor actually sends every referenced file.

The claim that Q4 cannot cause the remaining coding errors is unproven. So is
the opposite claim that a Q6 upgrade guarantees correct syntax or fixes all
bugs. Q6 and a matched Q4 control are scheduled with the same runtime, tasks,
sampling and placement policy. Different physical residency and desktop load
will still limit timing comparisons. These mixed quantization artifacts do
not represent a uniform four- versus six-bit change to every tensor.

Header inspection makes that concrete. The current Q4 artifact stores its
120 routed-expert tensors as 80 Q4_K, 37 Q5_K and 3 Q6_K tensors. The Q6 artifact
uses 78 Q6_K and 42 Q8_0 expert tensors. Most other quantized tensors are already
Q8_0 in the Q4 file; its output tensor changes from Q6_K to Q8_0 in Q6. Tensor
counts are not parameter counts, and this is not a quality score. The files are
20.61 versus 29.66 GiB, about 44% more storage for Q6. See the
[header evidence](../../../reports/2026-10-16-quantization-headers.json).

Coder-Next 80B has an explicit trial despite exceeding currently available
resident RAM. File-backed mapping can trade repeated storage reads for a lower
resident working set; it does not make all 80B weights resident or increase
available RAM. A launch rejection will be recorded separately from quality.
The pinned Coder-Next Instruct checkpoint is non-thinking: an effort flag
cannot turn it into a trained thinking model. Dense Gemma 31, by contrast,
will receive native thinking and a longer collection deadline; the earlier
five-minute calibration is not a completed quality evaluation.

The report's blanket GLM-Q5 failure prediction and incorrect Gemma/Kimi layer
counts were already corrected by the 15 October campaign. Its claim that an
8 GiB default prompt cache caused our stops also does not apply to the actual
launcher, which already used `--cache-ram 0`. Preserve those distinctions when
comparing the research with measurements.

### Remaining trials frozen before collection

The Q4/Q6 pair now has three Python seeds (73/74/75), the same TypeScript/SQLite
case, changed-file/history scenario, and frozen actual-instruction audit. The
runtime, placement policy, thinking mode and sampling match. Actual resident
caps depend on free RAM at each launch, so timing comparisons still include
that limitation. No outcome is claimed before collection.

For dense Gemma31, a separately named publisher-sampling profile changes the
prepared temperature from0.6 to1.0, with top_p0.95/top_k64 and native thinking.
The [publisher guidance](https://huggingface.co/google/gemma-4-31B-it#best-practices)
also retains thoughts during ongoing tool turns but excludes earlier thoughts
once a new user turn starts. The effective template must be checked; an accepted
flag alone is insufficient. The previous prepared0.6 profile remains unrun.
This is a family-appropriate practical trial, not a controlled cross-family
sampling comparison. Its longer deadline, CPU q8KV and one checkpoint remain.

The exact embedded Gemma template was then rendered offline with synthetic
markers in a sandboxed Jinja environment. `preserve_thinking=false` retains
current tool-sequence thoughts, removes thoughts from the previous user turn,
and preserves both earlier and current source contents. `true` additionally
retains old tool-call thoughts. The prepared publisher profile now uses false,
while retaining the runtime reasoning transport flag. This avoids conflating
old reasoning with file memory. The first preparation is preserved; neither
preparation has run inference yet. Actual runtime API rendering remains pending.
See the [template checks](../../../reports/2026-10-16-gemma-template.json).

A time-adjacent14:01 apps-open snapshot records63.91GiB physical capacity,
9.159GiB available and a14GiB server working set. Browser process working sets
are approximately8.3GiB and editor processes6.5GiB; those aggregates can count
shared pages twice and are not a complete additive physical-memory breakdown.
Windows, other applications, mappings and caches account for additional usage.
The existing pagefile is21GiB allocated and about5GiB used in that observation.
Neither allocated pagefile nor private commit is extra physical RAM.

The ongoing80B audit also exposes a separate allocation: runtime logs create
and replace context checkpoints of75.376MiB each, up to the configured four.
As input grows from14.5K to20K tokens, resident RAM remains capped at14GiB,
while private allocation changes from6.907 to6.984GiB. These snapshots alone
cannot assign every byte, but the logs directly establish bounded checkpoint
storage alongside the fixed816MiB active GPU KV buffer. Thus "KV reserves
capacity up front" does not mean every other runtime allocation stays fixed.

### Coder-Next private audit: completed attempt, failed workflow

The actual-instruction attempt ended at the16-tool-turn limit after4075.125s
(67m55s), with no final answer. All16 visible assistant content fields are empty;
only tool calls were delivered. Eleven distinct source files were supplied,
including the initial entry document. There were10 successful tool ranges and
15 failed reads:13 unavailable paths and two oversized ranges. The model
repeatedly added an extra policy-directory component to the Codex paths despite
the exact available inventory. It recovered one oversized read by requesting
100lines, but never successfully read the actual Codex guide or README.

This is a measured end-to-end tool-use failure. It is not a private code score
of zero, a timeout, or a memory stop. There is no private implementation to run
in isolation. The earlier completed public implementation and history results
remain valid. Do not promote this profile for instruction-heavy repository work.
A different sampling/scaffolding retry could be a separate future experiment;
this result does not prove every possible configuration will fail.

The run reached25,063 input tokens. Weighted uncached prefill was6.27tokens/s;
generation of tool calls was5.80tokens/s. Peak sampled resident RAM was14.000GiB,
minimum freeRAM6.466GiB, minimum availablecommit11.266GiB, minimum freeVRAM517MiB,
and maximum GPU core temperature48C. The launcher stopped normally after the
audit reported its limit. No new hardware error or restart was observed in this
run. [Aggregate evidence](../../../reports/2026-10-16-coder-next.json).

Across127 observations during the failed private audit, whole-system disk reads
averaged254.5MiB/s and GPU utilization18.4%. These samples include other apps;
page-fault counters include soft faults. They describe a paging-heavy run and
are not isolated storage/GPU benchmarks or proof of a universal speed ceiling.

### Dense placement revision before first load

After unloading80B, the desktop had22.99GiB freeRAM and6639MiB freeVRAM, below
the initially prepared6700MiB VRAM gate. The preceding run also observed roughly
600MiB of desktop VRAM variation. The revised unrun Gemma publisher profile
therefore places attention tensors from the first12blocks on CPU as well as all
dense FFNs. Their exact header spans total909.836MiB; the remaining48attention
blocks and output head stay eligible for GPU. This trades more host residency
and CPU work for GPU headroom. Actual loader buffers and speed remain pending.
The preflight gate becomes6400MiB for the smaller predicted GPU placement;
the400MiB runtime stop threshold is unchanged. All prior preparation revisions
are preserved, and this is not an isolated speed comparison with the old16K run.

## Source provenance

- [Supplied Gemini report](../../../research/raw/2026-10-14-gemini/report.txt)
- [Prior claim audit](../../../research/reviews/2026-10-14-gemini.md)
- [Prior campaign](../../../reports/2026-10-15-campaign.md)
- [Qwen Coder-Next publisher](https://huggingface.co/Qwen/Qwen3-Coder-Next)
- [Qwen3.6 publisher](https://huggingface.co/Qwen/Qwen3.6-35B-A3B)
- [Gemma dense publisher](https://huggingface.co/google/gemma-4-31B-it)

## Owner request

The unmodified request is retained in `owner-request.txt` beside this report.
