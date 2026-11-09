# Qwen3.8-Flash-Next: refreshed quant and engine investigation

10 November 02:27 IST: the resident3 control on native0.1.59 logs NVIDIA
event13 during its greeting; expanded postflight stops the tree and queue.
No new reboot. This control is interrupted/unscored, later controls unstarted.
It is separate from the earlier normal resident1 runs and the9Nov dynamic-KV
bugcheck. [Exact settings, telemetry and limits](../../../reports/2026-11-10-flash-fecs-stop.md).
No higher-precision, effort or long-context quality result is added.

## 10 November: changed-engine qualification and tuning

The owner explicitly renews autonomous testing. The failed9Nov dynamic64K
profile stays quarantined. A side-installed native0.1.59 engine, paired with
the previously isolated ACL-corrected frontend, completes static32K greetings
at a1GiB resident working-set limit: cold33.594s, warm13.266s,2.4/2.8decode
tokens/s. This changes both runtime and resident limit; it is not a clean
engine-only comparison against9Nov. Normal owned stop and no new event under
the expanded hardware checker. That does not establish long-run stability.

The first performance baseline uses2,462tokens and deliberately caps output32:
cold305.813s, repeated15.750s, changed-middle approximately302s. The repeated
request reuses2,457tokens; the middle edit reuses none. These reasoning-only
outputs are unscored. Native resident maximum1.000GiB, minimum whole-device
freeVRAM693MiB, minimum freeRAM5.280GiB, maxGPU51.91C. Logical expert bytes
reported by the engine are not measured SSD traffic.

CPU sharing, graph capture, prefill, resident memory, expert-cache slots,
host-KV placement and KV precision are distinct proposed controls. A separate
predeclared merge diagnostic compares none/low/medium/xhigh effort; the
frontend maps high to xhigh, so they are not two different levels. Current
state, exact identities and subsequent outcomes are in the
[10Nov campaign](../2026-11-10-tuning/2026-11-10-tuning-v0.12.0.md).
No higher-quant or standard llama result is assigned before it actually runs.

**9 November restart update:** Flash-Next Q2 / Strata 0.1.50's 64K
GPU-KV growth trial ended in a confirmed 0x116 NVIDIA timeout-recovery crash
at 10:10:57 IST. Its 8K/17K fact answers and allocation growth are observations;
the interrupted 33K case and unrun shrink/private audit have no score. The exact
configuration is quarantined, no engine is running, and production remains off.
See the [incident and configuration](../../../reports/2026-11-09-flash-q2-gpu-restart.md).
This records workload association, not a proven parameter-level cause.

## 9 November: Q2 serving now qualifies

The new Q2 completes two plain greetings after an isolated Windows frontend
permission correction: cold31.813s (first visible26.250s), warm9.437s
(first visible6.906s). Both return a complete greeting and stop normally.
This closes the static-serving gap, not coding quality or editor integration.
See the [reviewed measurement](../../../reports/2026-11-09-flash-q2-static-qualification.json).

| Control | Measured result / interpretation |
|---|---|
| Weight identity | Both Q2 shards and9pack artifacts pass fresh full hashes9Nov |
| Placement | 512expert-cache blobs, at most675MiB before rounding; mapped CPU experts, direct SSD PLE; int8 GPU KV32K, prefill64, six CPU workers, host logical14 |
| Thinking | Frontend high aliases xhigh; native budget0 means no ceiling. Projection, MTP, suffix drafts and route-tail skipping off; spec2 verifier required |
| Ready time | 82.953s including frontend preparation, versus a separate9.390s direct-native load-and-EOF probe; different loading paths |
| Cold greeting | 53fresh tokens,18.885s prefill,29generated/12.888s,2.3tok/s |
| Warm greeting | 48cached/5fresh tokens,1.042s prefill,34generated/8.320s,4.1tok/s |
| Memory | Native RSS peaks4.000GiB; process dedicated GPU5.243GiB/shared0.582GiB. Whole-machine minima5.989GiB freeRAM,13.305GiB freecommit,1294MiB freeVRAM; max58.03C |
| Failed attempts | Two pre-request WinError5 stops at OpenProcess, no score; direct native loading worked. The frontend put file-all permissions in a token default used for child processes |
| Correction | Separate checkout at4b9e05a2 plus the [token-default patch](../../../experiments/strata/windows-token-defaults.md); harmless controls reproduce failure/recovery.12Windows privacy tests pass, one POSIX case skips; guards unchanged |
| Cleanup | Explicit owned stop, no new hardware event; original frontend/runtime and failed evidence preserved |

Do not sum the WDDM shared counter with RSS or call the engine's printed
3947MiB freeVRAM the whole-device measurement. These greeting rates are
single observations, not a throughput distribution or instruction benchmark.
The0.1.50 sm86 switches/CPU sharing and new quant differ from the historical
IQ3 runs, so a future score is not a quantization-only comparison.

The separate64K GPU-VMM growth diagnostic starts9Nov09:10IST with8K,17K,
33K and shrinking8K inputs. Exact rendered counts8178/17356/33788/8178match
the real pinned encoder offline. Native startup reports16384of65536cells,
0.23of0.80GiB,512cache slots eligible below slot512. Two-hour request limits
and the same resource floors apply. At the original pre-crash checkpoint it was collecting:
no completed recall, growth/trim result or chat-history claim yet. The older
preparation paragraphs below are superseded only where stated here.

09:23IST observation during the same guarded engine: the8178-token prompt
finishes in723.859s, with651.817s prefill and71.957s generation of271tokens.
First visible content appears714.609s into the request. Its delivered JSON
contains the five requested source values; formal aggregation waits for
owned cleanup and review of all available answers. Before the17356-token
request, the native log reports growth to24576cells/0.33GiB, taking74expert
cache slots and leaving438of512resident. This is actual GPU allocation growth,
not merely a larger configured context. Longer inputs and shrinking remain
in progress. No chat-history or coding score is implied.

A separate15second passive observation during17K prefill records394.45–571.02
MiB/s whole-E: reads,0.139–0.157ms average read latency and queue1–4.
System page reads are7708–11941/s. The process sample has4GiB working set,
about8.487GiB private bytes and562887page faults/s, including soft faults.
Do not multiply that fault count by page size or equate the engine's logical
expert bytes with SSD traffic. These are not proof of storage saturation or
a matched speed comparison with Flint. [Observation](../../../reports/2026-11-09-flash-paging-observation.json).

Historical pre-serving checkpoint (superseded above): all fifteen Flint performance controls now finish normally.
The resident3/6/3GiB comparison gives cold wall123.016/117.203/113.735s,
cached-repeat5.297/3.500/5.391s and changed-input90.719/84.312/83.907s.
Extra residency helps cached repeat, but cold/changed improvement is smaller
than baseline drift; retain3GiB for matched quality follow-ups. No quality
score follows from these short32-token controls. Native private31/36 remains.
Flash Q2's11artifacts pass fresh full hashes. Direct guarded native loading
reaches READY32768 and exits normally on stdin EOF in9.390s; no questions.
Two serving attempts stop fail-closed before requests with WinError5 at
OpenProcess in the working-set guard. All descendants are cleaned up, no
new hardware event. A source lead is frontend adopt_user_defaults using file
access bits in the process token default ACL; harmless reproduction pending.
Guard now preserves traceback/error.json without changing floors or cleanup.
52offline tests and6harmless lifecycle checks pass. Four Flash growth inputs
8178/17356/33788/8178tokens match the real pinned frontend encoder offline;
no growth inference. Production remains off; no model retired or promotion.


26October2026. Active research/installation; no new quality score yet.
This is the model-specific continuation of the
[18October Strata measurements](../2026-10-18-strata/2026-10-18-strata-on-10gb-v0.6.0.md).
The [seven-article review](../../../research/reviews/2026-10-26-qwen-articles.md)
holds article summaries, source revisions and distinctions relevant to other PCs.

**9November pre-load checkpoint (superseded above):** the two Q2 shards and native-view pack were
fully verified/built on3November and are installed on E:. Fresh full verification
is queued after the active Flint engine stops; this new Q2 has not served a
request. The reviewed static32K plan explicitly limits the expert cache to
512blobs (at most675MiB before per-layer rounding), uses64-token prefill,
disables KV growth/drafts/projection/route-tail skipping, and preserves
8.5GiB RAM/14GiB commit/6000MiB VRAM admission plus minimum stop floors.
Nine actual packed-template/frontend marker checks and the revised native
identity/floor/owned-cleanup checks pass. These are preparation results,
not model fit, response quality or a dynamic-KV measurement. Earlier dated
installation statements below remain historical; the latest trial state is in
the [merged report](../2026-11-09-merged-research/2026-11-09-merged-models-articles-and-experiments-v0.11.0.md).

27October03:26IST: the separate pinned frontend environment is installed
under the experiment's E: directory. All15packages are frozen; pip check and
both native/Python server help return0. The executable and native library are
rehashed before the help probe. The CPU-affinity helper's harmless child really
inherits0xFFFC, and a relative executable is rejected. No Flash model, packed
template or inference has been loaded by these checks. The source checkout and
old working environment remain separate.
[Preparation receipt](../../../reports/2026-10-27-strata-environment.json).

## Why reopen it

The owner prioritizes precision, reasoning, linked instructions and long context,
and now permits extended coding diagnostics. Earlier20minute failures do not
prove the model cannot finish with a larger allowance. They remain failures in
their original cohort. A newer separately installed engine and a smaller
GSQ-RCO Q2_0 quant are explicit new variables. They need their own evidence.

### Native KV-growth qualification

9November next diagnostic design, conditional on the static greeting pass:
retain the same512-blob/mmap-expert placement and use64K maximum context,
`--kv-grow`, initial16384cells and8192-cell steps. Freeze deterministic
beginning/middle/end source-fact prompts near8K,17K and33K actual rendered
tokens, then return to an8K request and an omitted-history UNKNOWN probe.
Use the packed tokenizer and exact frontend rendering; this frontend does
not expose llama.cpp's `/tokenize` endpoint. Preserve xhigh, complete outputs,
actual usage and native grow/trim/slot-transfer logs. A separate follow-up
must test changed-file history, since independent larger prompts alone do
not demonstrate conversational retention. A dated request generator is now
prepared in ignored local evidence. It mirrors the pinned xhigh frontend and
packed tokenizer, with no engine creation or network inference. It has not
been executed: no generated requests, token-count validation, armed growth
plan or growth inference exists yet. The planned unknown/history probes are
separate from the generator's four independent allocation probes.

Source caveat for interpreting trim: `kvg_trim` also returns without shrinking
when no expert-cache slots have been given up (`lo >= top`). Fresh allocation
at the cache floor, trim hysteresis and parked-state policy can therefore
produce different memory curves. Record the native events rather than
assuming every smaller prompt immediately releases GPU memory. A direct
RAM-KV experiment is a separate placement trial, not this GPU-VMM test.

9November source follow-up: the second-stage elastic controller also needs
more than128eligible cache slots after the prefill loan. At the cache floor it
can request fresh VRAM, so growth is not guaranteed to keep total device usage
flat. Trimming waits for a two-step reduction and respects parked conversations.
The new static32K qualification has growth explicitly disabled; a later growth
trial must show native start/grow/trim events, input/output counts, RAM/commit/
VRAM and recovered facts. A VMM capability query alone does not pass this gate.

27October correction: native build`1aff6d14117b` excludes
`resident_cpu_experts` from KV growth, but does not explicitly exclude plain
`mmap_experts` or check that mapped pages are physically resident. The earlier
blanket RAM-residency conclusion was too broad. GPU VMM, one GPU, a profile,
GPU-only KV and adequate cache slots are additional conditions. Plain-mapping
growth remains untested; verify actual enable/grow/trim logs, memory and recall
after static qualification. Keep bounded-copy and host-streamed KV separate.
[Exact native source](https://github.com/Niko1221/Strata/blob/1aff6d14117b/src/program/generate.cpp#L5123).

The frontend's single-sequence `/slots` reports `n_prompt_tokens` from its
request status, not physically mapped KV cells or prompt-plus-output occupancy.
Use actual tokenizer/usage counts for input and native `K/V grown`/`K/V trimmed`
events for allocated cells, bytes and transferred expert slots. The existing
llama.cpp growth collector's `/tokenize` assumption must also be checked before
reuse with Strata. A context meter rising is insufficient evidence of dynamic
allocation. These are27October source findings; the new growth run is unrun.
[Frontend slot semantics](https://github.com/Niko1221/Strata/blob/4b9e05a2a806a3fe24f7b2560d98626c37dade35/serve/server.py#L6689).

## Historical result and limits

The previous artifact was **ISTA-DASLab GSQ-RCO IQ3_XXS**, two shards totalling
75,839,998,528bytes, not Unsloth's similarly named quant. Strata0.1.45 with
10/14GiB expert pools fit the10GB GPU but four coding attempts hit1200seconds.
Measured capped decode improved from5.9-6.7 to8.8-9.6tok/s with the larger pool;
that was not a completed-code result or a clean causal timing comparison.
128K int8KV with32K GPU cells allocated1.55GiB host KV; the51K-input workflow
returned an empty final. Two separate final-turn replays recovered6/6facts.
Full shards were retired20October; pins and transcripts remain.

## New artifact identities

Repository`ISTA-DASLab/Qwen3.8-Flash-Next-GSQ-RCO-GGUF`, revision
`ed59f92082b1e93c0e96d60a8b11aab089b52f09`:

| Q2_0 shard | Bytes | SHA256 |
|---|---:|---|
|Qwen3.8-Flash-Next-GSQ-RCO-Q2_0-00001-of-00002.gguf|37623740192|69820c02ec7d0b45ef2ebb19d6620299db749fe2aded7f39f93c6b88b199b720|
|Qwen3.8-Flash-Next-GSQ-RCO-Q2_0-00002-of-00002.gguf|28800138432|316b46f3a2dbd68c900f43136ab9449f9dcc3725dfd8c794847c204bc161e113|

Both are under`Q2_0/`. The second is byte-identical to the old dictionary shard.
That older copy was retired in October; both new Q2 shard copies are installed
and were fully verified on 3 November. Fresh full verification before the new
live loading was then pending; see the completed static and interrupted growth results above.
Q2 saves9.416GB of transformer storage versus oldIQ3XXS. Publisher coding
benchmarks favor IQ3XXS, so Q2 is a capacity/control candidate, not a declared
quality upgrade. IQ3_S is the later higher-precision option if resources allow.

Staged separate runtime: Strata Qwen engine0.1.50 from app release0.2.6,
Windows x86_64 CUDA13 archive581,368,579bytes, SHA256
`a9643e2f5dd5c62e734d2980484c320d41da0160fc4932bf638b7f34e38e74f5`.
Archive verified and safely extracted into a new directory; engine executable
SHA256`5745022e7c8f743cfee83544da7d3672cd86103c854f23600e2c69ddd6593bef`.
No new engine load or quality measurement yet. The old checkout/build is
preserved. App0.2.6's DeepSeek changes
do not imply a new Qwen engine versus app0.2.5.
The packaged BUILD record identifies native commit`1aff6d14117b`, CUDA13.0
and sm86 among its targets; this differs from the frontend source revision
`4b9e05a2a806a3fe24f7b2560d98626c37dade35`. Keep both identities. The component
manifest's minimum NVIDIA driver is580.65, below this PC's measured621.01;
no driver installation is needed for this qualification.

Current upstream QWEN36 documentation resolves the engine-name ambiguity:
the unified`strata`binary dispatches to`src/qwen35`from GGUF architecture;
it does not require the old standalone`strata-q36`filename. Its documented
Qwen3.6 files include MTP metadata. This does not establish that our retained
non-MTP GGUF loads, or that Flash-specific low-RAM/KV flags work on that path.
Do not silently reuse the older fork's compatibility assumptions.
[Pinned Qwen3.6 engine documentation](https://github.com/Niko1221/Strata/blob/4b9e05a2a806a3fe24f7b2560d98626c37dade35/docs/QWEN36.md).

Packing plan: current`tools/iq_pack.py`reads both verified shards and can use
native expert views without`--experts-bin`, avoiding a second expert-weight
copy. It still writes float-tensor/tokenizer metadata and a conversion record;
those outputs need disk allowance and inspection. The lookup table remains
in its original shard. Do not use`--compat-bf16`silently: that option can round
small projections and is a separate numerical change.
[Pinned packer](https://github.com/Niko1221/Strata/blob/4b9e05a2a806a3fe24f7b2560d98626c37dade35/tools/iq_pack.py).

## Profile and evaluation plan

- Source check27October: the server prefers the tokenizer pack's chat template
  over its bundled fallback. Hash and test the actual packed template before
  claiming a reasoning-history setting works. OpenAI normalization forwards
  `reasoning_content`, but arbitrary `preserve_thinking` template kwargs are
  not forwarded on that path. The bundled fallback preserves it by default;
  this alone does not establish the new GGUF's template behavior. The shared
  settings sidecar beside a config can also override its default effort. Use
  a fresh config path, verify no inherited sidecar, and save `/props` plus
  actual requests and rendered marker checks. These are pending validation
  steps, not a new observed live failure.
- Further source inspection finds a second settings layer: the server applies
  saved tuning presets even when given an explicit config. The new experiment
  will set `STRATA_NO_PRESET=1` and compare effective arguments with its frozen
  config. `STRATA_START_RETRIES=0` disables transient startup retries, but does
  not disable the distinct request-triggered restart path. The collector must
  stop on native-process exit/identity change before sending further tasks.
  No retry failure or settings contamination has been observed in a new live
  trial; these are source-derived controls. Explicitly disable the experimental
  projection in sampling as well as omitting its vector from engine arguments.
  [Pinned frontend source](https://github.com/Niko1221/Strata/blob/4b9e05a2a806a3fe24f7b2560d98626c37dade35/serve/server.py#L7869).
- 27October preparation adds a pure-mapping qualification before the resident
  pool: unchanged native expert values read from GGUF, no full RAM copy,
  proposed4GiB owned working-set ceiling,32K int8KV and3072MiB device reserve.
  This is an unrun plan; native help has passed, while shards, packing and fresh
  admission remain pending.
  Source distinguishes OS-cached mapping from a budgeted expert copy, which
  can change the file tier to unbuffered reads. Compare those modes explicitly
  rather than assuming a larger resident budget is always faster. The planned
  request controls disable automatic output shortening, early thinking wrap,
  recovery, drafts and the repeated-token stop; the collector still enforces
  its fixed deadline. No inference measurement or fit is claimed here.
- After mapping qualifies, compare a bounded expert-RAM pool sized from fresh physical and commit
  headroom, n-gram table on SSD, int8KV, one slot, and explicit device reserve.
- Concrete unrun controls now include a2GiB expert-copy pool with6.5GiB
  headroom and a separate PLE-dictionary mapping arm. They are not combined:
  the former changes hot-expert residency/cold reads; the latter changes only
  `--ple-io direct` to `mmap` from the static baseline. Neither requests the
  whole dictionary locked in RAM. Native source documents slow direct lookup
  reads on some Windows/NVMe systems; this is a reason to measure our drive,
  not proof of our bottleneck. The same source records Windows mapped reads
  stalling on serial cold page faults; mapping is not inherently faster.
  Compare whole cold/warm requests without purging the owner's cache.
  All four plans remain unlaunchable pending
  model/pack verification and fresh allocation-specific admission. A1GiB
  working-set ceiling must not be reused as a2GiB pinned-pool allowance.
- Keep `--adapt-async 0` explicit for the baseline and these controls. Native
  source says asynchronous adaptive swapping is not bit-exact across runs;
  its possible speed benefit needs a separate quality comparison. Explicit
  `STRATA_PLE_AUTO_MMAP=0` also keeps lookup mode from changing automatically.
  [Native placement and lookup source](https://github.com/Niko1221/Strata/blob/1aff6d14117b/src/program/generate.cpp).
- Disable the engine's additional parked-conversation cache for initial fit
  (`--conversation-cache-mib 0`). Its default can use up to8GiB more host memory;
  it is distinct from the live KV cache. Later prefix-reuse experiments get
  their own explicit budget. The container memory-limit flag governs parking,
  not a universal cap on model allocations or Windows commit.
- After fit qualification, a separately budgeted alternating-conversation
  control should compare cache0 against a small explicit host cache. Two
  editor workspaces or a helper request can replace the active prefix; a
  successful uninterrupted history test does not establish fast switching.
  Keep each conversation's markers and changed-file facts distinct, record
  cached versus newly processed tokens, and include the host cache in admission.
  This is a planned diagnostic, not an observed editor/cache failure here.
- No route-tail skipping or refusal projection in the accuracy baseline.
- Plain greeting/no files first, cold and warm;600second practical ceiling.
- Freeze native effort/output limits and compare public instruction routing,
  strict TS/SQLite, changed-file/history and private source-citation audit.
- Record frontend controls as well as engine flags: high is the model's
  default effort, and `answer_room` normally reserves a quarter of a finite
  output cap by closing thinking early. Keep this behavior explicit; budget0
  does not mean an unconstrained answer when answer_room remains enabled.
- Use the model's supported high effort explicitly. Strata documents low,
  medium and high; its Responses-compatible`xhigh`name maps to the high choice,
  not an additional trained ultra level. Verify the rendered template/request,
  not just a client label. Preserve historical thinking for the baseline and
  record the resulting context cost. A lower-effort control must include all
  extra tool turns/retries in total latency, not only its first response.
- Long diagnostics may exceed1200seconds; report exact duration and do not
  import those scores into the old leaderboard.
- Only then compare MTP and64K/128K KV placement, recording allocated capacity,
  occupied tokens, resident pages, I/O and delivered final answers separately.
- Compare the existing frontend opt-in`reasoning_close_retry` off/on for
  empty-final recovery. It appends a thinking-close marker and permits one
  continuation within the remaining output limit; this changes scaffolding,
  not model precision. It predates0.1.50 and is disabled by default. The old
  empty-final trace is compatible with the reported symptom, but the root
  cause remains unproven. Include normal answers and literal tags as controls.
  [Issue1053](https://github.com/Niko1221/Strata/issues/1053) and
  [pinned source](https://github.com/Niko1221/Strata/blob/4b9e05a2a806a3fe24f7b2560d98626c37dade35/serve/server.py).

## Pros, cons and current disposition

Pros: sparse compute, predictable dictionary offload, native long context and
an engine with explicit RAM/SSD controls. Prior fit and host-KV use are measured.
Cons: expert paging competes for scarce RAM and disk bandwidth; strong publisher
scores have not translated into completed local coding workflows. Lower quants
can reduce task accuracy. Greater context does not fix missing file retrieval.
Current recommendation: **retest, not promote**. Existing Qwen3.6 Q4 remains the
preserved baseline. New Q2 weights/load/quality are unrun at this checkpoint;
available disk is below the full two-shard download plus headroom, so finish
and record current candidates before exact-file retirement creates room.

The architecture paper strengthens the reason to test quality, while limiting
the long-context claim: its eight-needle MRCR score declines substantially at
512K/1M despite high RULER scores. Both retrieval difficulty and context length
matter. Its favorable comparison with dense27B concerns base models, so it
cannot decide the ranking of our quantized instruction-following deployments.
Keep source selection, changed-file recovery and conflicting instructions in
the local evaluation instead of replacing them with one successful needle.

### Refreshed source frontend prepared

The separate source checkout is now pinned to
`4b9e05a2a806a3fe24f7b2560d98626c37dade35`, preserving the old patched fork.
Its AGENTS, AI_SETUP, AI_REFERENCE and SOURCE_INSTALL guides were read.
This experiment deliberately uses the documented source route with the
separately verified native engine; it is not the default Terminal installer,
which chooses locations and versions outside this lab's pinned E-drive plan.
At that source-preparation checkpoint, no environment installation or help
invocation had run. The27October03:26 update above supersedes those two items:
environment/help checks now pass. Model loading and inference qualification
remain unrun.

The current low-RAM documentation distinguishes Linux-only file prefetch and
zero-copy from Windows' opt-in file-page trimming. The latter does not reduce
committed memory. The bounded expert pool, parked-conversation cache and live
KV need independent budgets. Engine stats can report file-read bytes/time and
RAM/GPU expert hits; capture those before crediting a cache strategy.
Pool-core placement also needs explicit inspection: its default host thread
uses logical processor0, whereas this PC's campaign excludes physical core0.
Record actual allowed processors and worker placement before load.

Source inspection finds an additional storage control worth measuring:
`--ple-io direct` performs sparse unbuffered reads of the lookup table. The
current code warns about slow reads; automatic fallback to mapped reads is
opt-in because some Windows/SATA reports became slower with mapping. Keep
direct reads explicit in the baseline and compare mapped reads separately,
recording lookup latency and whole-task time. Do not turn the broad advice
"put it on SSD" into a claim that every I/O mode is equivalent.
Native help must confirm these flags in the packaged engine before serving;
source inspection alone does not prove binary support.

The source still requires native packs to use `--spec` of at least2. This
does not by itself enable MTP: the draft checkpoint and suffix drafting are
separate. For the no-draft control, retain spec2, omit MTP and use suffix0.
The planned host placement is `--host-core last` with workers on logical
processors2,4,6,8,10,12, plus an inherited process affinity excluding0/1.
Confirm the packaged flags and logged placement before treating this as
implemented. The current source offers this without modifying a CUDA kernel.

Further source review of `src/core/expert_source.cpp` identifies how to report
the bounded pool: after the GPU cache loads, the native allocator uses the
smaller of available physical RAM and Windows commit, subtracts its headroom,
and reduces an oversized request with another256MiB margin. Thus a requested
4GiB pool can resolve smaller; record both values and the actual number of
resident experts. The frontend's later2GiB checkpoint/staging allowance is
also distinct from the parked-conversation budget. These are source findings,
not measurements of the staged binary.

A possible later optimization is an expert ranking learned from separate
development prompts using the supplied routing-trace/profile tools. With our
small GPU/host caches, changing which complete experts stay resident may be
more useful than assuming all installed RAM is available. Keep every routed
expert contribution enabled and use a disjoint development corpus; tuning on
the scored questions would contaminate that comparison. This remains an
optional follow-up after baseline fit and complete answers, not a claimed gain.
# 9 November continuation addendum

Both Q2 shards and the native-view pack completed3Nov; the previous download
queue is stale. No Q2 inference has happened yet. New proposal
`local-data/2026-11-09-merge/flash-q2-explicit512-static32.planned.json` replaces
automatic expert-cache sizing with512blobs (675MiB from48native rows of
1,382,400bytes), prefill64/static32K/int8, mmap experts and direct PLE.
It retains the4GiB engine working-set cap and proposes8.5GiB RAM /14GiB commit /
6000MiB VRAM admission, with2.5GiB/1GiB/400MiB runtime floors. This is a new
capacity hypothesis, not an observed allocation or faster profile.
It remains `launchable:false` pending shard/pack verification, packed-template
marker rendering and the changed guard's unit/harmless-process validation.

The source's KV-growth predicate excludes `kv_resident > 0`; it grows GPU
backing while trading expert slots, separately from pinned-host-KV streaming.
The3NovVMMcapability receipt reports support but no allocations/model run.
Actual native grow/trim logs plus retained facts remain required.

The new [article ledger](../../../articles.md) and
[merged report](../2026-11-09-merged-research/2026-11-09-merged-models-articles-and-experiments-v0.11.0.md)
track these distinctions. No prior timeout or empty final becomes a pass.
