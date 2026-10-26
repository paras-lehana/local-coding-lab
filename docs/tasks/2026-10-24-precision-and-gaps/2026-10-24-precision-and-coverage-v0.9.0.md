# Precision, tuning research and missing benchmark coverage

Started 24 October 2026 (Asia/Kolkata). Status: active; Qwen IQ3_S public/private
graded; higher Flint Q4 controls deadline; IQ3 cached/capped coding6/12;
IQ4 bounded-resident public55/60 and private29/36 after a separate RAM stop;
its native coding controls fail completion. Q4 native now attempts all12
questions across an original run and JavaScript resume:9 frozen passes,2
failures,1 output limit; two additional JS defects remain.
This continues the completed [Flint trial](../2026-10-23-flint/2026-10-23-recursive-flint-v0.8.0.md).

## Request and constraints

Test higher Flint precision, research practical improvements, and complete
missing Qwen/other-model work. Apps remain open, one engine at a time, 1200
seconds per whole prompt, no editor typing or clock/driver changes. Preserve
incomplete answers, capacity failures and old trials. Review code before
isolated grading. No cloud inference or exposed historical key is used.

## Execution order and coverage audit

| Candidate / gap | Next action | State |
|---|---|---|
| Qwen Q4 twelve coding tasks | Original native64K/.6/seed73, then separately declared cache/general32K control |All12 attempted across original+resume:9frozen passes,2failures,TTL output limit. OriginalRAM interruption and two extraJS defects retained. Separate resident7/cache/general32K interval deadline; original larger-resident profile unrun |
| Plain Qwen Q6_K higher precision |Distinct artifact pinned/header inspected; full download then guarded quality and long-file work |Resident7 and resident10 router deadlines1200.016/1200.031s, seven successful reads each; incomplete/unscored. Fresh original18GiB gates reject at actual launch/decision snapshots. Exact file rehashed/retired22:46; later suites unrun after qualification failure. Old XL scores do not transfer |
| Qwen IQ3_S interrupted public / missing private and coding |38 CPU expert blocks; conservative stop floors | Native public52/60, private29/36; separate cap4096/cache1536 coding6/12, all twelve complete; no mixed composite |
| Qwen IQ4_XS interrupted public / missing private and coding |CPU35 with bounded resident memory after fresh RAM stop |Public55/60; private29/36 in725.4s; native interval1200s deadline and presence1.5 control16K output limit; subsequent unchanged coding cases interrupted/unrun. Exact weights retired21:07 after fresh full hash |
| Gemma26 fallback missing latest public/coding | Collect missing suites under its recorded template and sampling |CPU28 partial retained. CPU26 public57/60 and private23/36 complete; private798.6s,15/2/6. Instruction/citation and public code/test defects remain. Direct coding rejects26October2.169GiB freeRAM; no historical score transfer. [Report](../2026-10-24-gemma26-coverage/2026-10-24-gemma26-v0.9.0.md) |
| K2 MoVA / Nemotron Bolt downloaded but untested | Verify identity; calculate placement and gates; trial if capacity permits | Pending |
| Flint higher precision | Pinned Unsloth Q4 first, Q3_K_XL fallback; isolated opt-in mmap build | Both Q4 CPU44 and CPU48/cache1536 router trials deadline; exact Q4 retired after fresh full hash. Q3XL partial download checkpointed, NVFP4 still queued |
| Flint CSV / history output limits | Separate 32768-output diagnostic with unchanged 1200-second deadline | Original8K history diagnostic already passes8/8 separately; original CSV32K diagnostic pending. Q4 router deadlines prevent full-workflow qualification |
| Flint file-driven TS/SQL | Check template/parser provenance, rerun native tool workflow before trying a separately labeled scaffold change | Pending |
| Old dense,80B,Bonsai,LFM gate failures | Reopen only where a specific runtime/template/budget change addresses the measured failure; otherwise record unresolved quality coverage and exact gate | Audit recorded below; unchanged configurations remain excluded, missing newer scores explicitly identified |
| Qwen full scorecard / finalists | Do not invent missing values or merge incompatible profiles; repeat eligible finalists on seeds74/75 | Pending earlier components |

Capacity exclusions are not completed quality tests. A benchmark can finish
with a demonstrated bug or deadline: completing coverage does not mean making
every candidate pass. No historical failed answer will be replaced by a retry.

The separately frozen Gemma26 and K2 `resident8-calibration` profiles are
fallbacks if their original18GiB profiles remain inadmissible. Each fixes the
owned resident maximum at8GiB, reserves6.5GiB and requires14.5GiB freeRAM;
original commit/VRAM admission and runtime stop floors remain. Model-specific
GPU placement, KV and actual request settings stay as documented in each
profile. These smaller resident sets deliberately allow paging, do not bound
total allocations, and are not proven fits. A short smoke must complete before
quality collection; no baseline score transfers. They are unrun at22:10IST.

### Audit of older candidates,24October

The [complete inventory](../2026-10-17-complete-model-inventory/2026-10-17-all-models-gemini-and-availability-v0.4.1.md)
and [current comparison](../../model-comparison.md) preserve these older
measurements. The new twelve-question coding suite was introduced later;
its absence is not permission to label old models as never tested.

| Older candidate | Actual barrier / evidence | Disposition in this campaign |
|---|---|---|
| Qwen3.8 dense Q6/Q8/TQ3 |Very slow long-input processing, roughly1–2tok/s decode; separate restart and VRAM stops |No unchanged reload. The current higher-quant MoE work does not establish a remedy for dense CPU bandwidth or the hardware interruption |
| Gemma31 dense |Private26/36 takes7234seconds; public code/history also exceed1200seconds |No unchanged twelve-task collection; quality evidence exists, but this profile fails the owner's current deadline |
| Coder-Next80B Q4 |Mapped load and some public cases finish; private repeats bad paths and has no final answer after16turns/4075seconds |Preserve the measured tool failure. The initial-prefetch fix was already tried; repeating it is not a new rescue |
| Coder30B UD-Q4_K_XL |Non-thinking model, public bugs and private1200second deadline |No native high-effort flag to enable. Q6/Q8 remain distinct untested artifacts, not failures inherited from Q4 |
| Kimi-Linear48B Q4 |Some public results complete;64K private capacity gate rejects; q8 V-cache dimensions unsupported |No claimed private score. Current apps-open headroom is lower than its recorded requirement; do not relax the load gate or copy Qwen's KV flags |
| GLM4.7Flash Q4/Q5/Q6 |Completed instruction audits27/21/24; code/data-loss defects despite higher precision |Prior precision work is complete, newer twelve-case suite remains unrun. No demonstrated new recipe justifies a duplicate full download yet |
| BonsaiPQ2/PTQ1 |PQ2 manually stopped at2.3tok/s; PTQ1 full-GPU router deadline |These are performance/completion observations, not twelve-task correctness scores. No unchanged retry |
| LFM2.5 |Public48, private reasoning deadline, six completed coding passes of twelve |Latest suite already attempted; preserve two incomplete and four failed answers separately. No unchanged retry |
| Flash-Next125B/Strata |Repeated direct-code deadlines and empty history final despite larger memory/MTP controls |Historical parameter controls were exercised; newer Strata release is research-only until separately installed/tested |
| Original Qwen3-Next80B IQ3_M |Python syntax parsed; interval semantics failed; original broader campaign interrupted by crashes |Distinct from Coder-Next. No evidence for a universal three-bit syntax failure; no unchanged high-memory reload |

These dispositions close the audit of unchanged old configurations, not all
possible model/quant/engine combinations. Candidate-specific lower-memory or
new-template experiments must have their own justification and receipts.
Qwen Q4/IQ4, Gemma26, K2, Bolt and Flint follow-ups remain live work above.

## Initial research findings

- [Recursive's model card](https://huggingface.co/RecursiveSI/flint) recommends
  at least32768 output tokens for hard tasks and preserving reasoning history.
  The earlier CSV case used16384; raising this may help, but wall time remains
  bounded and there is no guarantee of a final answer.
- [Unsloth's guide](https://unsloth.ai/docs/models/flint) lists UD-Q4_K_XL at
  25.05GB and UD-Q3_K_XL at18.50GB. Exact API metadata is pinned before fetch.
  Precision is a separate variable from cache placement and output budget.
- [Tere Labs](https://huggingface.co/terelabs/flint-GGUF) describes calibration
  on tool/code data, higher precision for always-active tensors, and a template
  escape fix for an early llama.cpp commit. Their reported300-task comparison
  does not establish significant BFCL differences among the tested4/5-bit
  files. Check whether the template issue applies to our newer runtime before
  patching anything; successful previous structured calls already matter.
- [llama.cpp issue31000](https://github.com/ggml-org/llama.cpp/issues/31000)
  describes tool XML appearing only inside reasoning in another user's setup.
  Its root cause is unresolved; it is not proof of our path-guessing failure.
- [Recursive's announcement](https://recursive.com/updates/introducing-recursive-flint)
  uses different hardware and multi-attempt, long-deadline agent evaluations.
  Its distilled NVFP4 and optimized engines are distinct from our GGUF recipe.
  Advertised throughput is not an RTX3080 measurement.

## Evidence

New raw evidence belongs in ignored `local-data/2026-10-24-precision/`.
Public receipts and reviewed results will be linked here after collection.
Existing production settings and baseline weights are preserved.

## Research corrections and next practical controls

The often-repeated Flint hexadecimal-template workaround is already in our
runtime. GitHub's comparison shows b11838 is40commits ahead of
[`9febe63`](https://github.com/ggml-org/llama.cpp/commit/9febe63d5a379f8568bae7116a5b2ba844a4a4a6),
with zero commits behind. The saved runtime template retains the hexadecimal
filter and initializes successfully. Its previous TS/SQL stream delivered all
six required sources, then attempted26 nonexistent paths. Removing that filter
is therefore not a demonstrated remedy for this local failure.

[PR31040](https://github.com/ggml-org/llama.cpp/pull/31040) proposes handling
mixed required/optional XML argument permutations. It remains unmerged as
checked today. Our frozen read_file has only one required parameter, so the
described multi-argument failure does not explain this benchmark. It may be
relevant to editor edit tools; do not replace production with it without a
separate regression on the actual tool schema.

[PR30594](https://github.com/ggml-org/llama.cpp/pull/30594) proposes parallel CPU
miss computation and GPU expert caching. Its published improvements vary by
model and cache fraction, and its own Flint example is slower. It changes
single-token decoding, not prompt processing; speculative batches are a known
limitation. Treat it as a candidate engine experiment with accuracy checks,
not a promised speedup or a way to eliminate host weight storage.

The [rec engine](https://github.com/recursive-oss/rec) currently requires
specific Apple Silicon systems with48GB unified memory. It is not the Windows
RTX3080 installation path. The [vLLM recipe](https://recipes.vllm.ai/RecursiveSI/flint)
documents different parser requirements and Blackwell-oriented kernels; those
flags are not interchangeable with llama.cpp's reasoning parser. Keep the
existing Windows GGUF engine until a supported alternative is measured here.

## Weight-only estimates, before downloading

All values below are GiB, derived from pinned GGUF headers (including tensor
padding). These are not measured process memory. GPU KV at64K additionally
needs about0.96GiB for Flint, plus scratch, runtime and desktop headroom.

| Artifact | File | CPU expert threshold | CPU expert weights | Other weights |
|---|---:|---:|---:|---:|
| Unsloth UD-Q4_K_XL | 23.33 | 42 | 18.64 | 4.69 |
| Unsloth UD-Q3_K_XL | 17.23 | 40 | 12.69 | 4.53 |
| Official distilled NVFP4 | 21.29 | 42 | 16.88 | 4.41 |

The official artifact changes the quantization/training recipe, not just bit
width. It merits a distinct comparison if compatible and capacity permits.
Q4 needs materially more free RAM than the current14-15GiB desktop. Q3_K_XL is
a higher precision recipe than the previous mixed IQ3_XXS but is not4-bit;
that distinction must remain explicit if it becomes the practical fallback.

13:23IST: production was verified asleep and stopped by its exact configured
launcher. Q4's fresh preflight found15.118GiB free and rejected its16GiB gate.
IQ3_S passed its new12GiB gate with38CPU expert blocks and the conservative
2.5GiB RAM/1GiB commit/400MiB VRAM stop floors. It completed the router in
338.984seconds; source review is saved, executable grading awaits shutdown.
This does not yet establish a score or a complete candidate evaluation.

13:38IST: IQ3_S finishes all public cases: router338.984s, file-driven
TypeScript/SQLite346.515s, and history176.000s. Reviews were saved before
execution. The history recovers all six requested values and correctly lists
the changed-file read. TypeScript appears to miss prototype validation; SQL
appears to drop a referenced table with foreign keys enabled. Those are
source-review findings until isolated execution. Private collection is active.

## Further tuning research

The consolidated [engineering review](../../../research/reviews/2026-10-24-precision-and-offload.md)
separates measured results, upstream claims and practical controls. The local
runtime reference was also corrected: historical cache/placement comparisons
do not prove an intrinsic accuracy penalty, and the tested dense/MTP outcomes
are not universal statements about those architectures. Existing Codex/Claude
adapters already route to these sources and need no duplicate policy copies.

[Qwen's own card](https://huggingface.co/Qwen/Qwen3.6-35B-A3B) recommends
temperature0.6 for precise coding and a32768-token output allowance. These
trials use0.6 but retain the frozen16K direct-coding limit for comparison;
any output-limit follow-up will explicitly use32K with the same20minute wall
deadline. A larger output allowance is not a higher reasoning-effort setting.

[moe-cache](https://github.com/IbrahimSiddiqui007/moe-cache/tree/bb9315345eea6fbed5c7826a452c5864788ef758)
targets CPU experts that exceed available RAM, using a bounded RAM cache and
SSD reads. Its current plugin requires Linux x86-64 and matching shared ggml
libraries; it is not a native Windows flag. The author's results show it can
lose to stock when the model already fits. Its faster approximate mode also
changes output equivalence. This is a possible separate WSL/backend experiment,
not a production upgrade established here.

[This experimental fork](https://github.com/mateusoro/llama-cpp-perf/tree/191121669732e6fbac9577528912b5df328a2553)
combines GPU expert caching, asynchronous CPU computation, and optional
page-locked host transfers. It reports Qwen/GLM speedups on a12GB3060; its listed
cache architectures do not include Flint. Page-locking large host tensors would
conflict with our current RAM-constrained paging strategy. Larger prefill batches,
MTP, and expert slots compete for the same VRAM. Benchmark prompt processing,
first usable answer and correctness before applying its decode-rate claims.

The [expert-pool RFC](https://github.com/ggml-org/llama.cpp/discussions/28248)
also documents an invalid verification run that hit the old server and a stale
mapping bug that selected incorrect experts. This reinforces our existing
requirements: prove process identity, record cache state, and compare actual
outputs. An experimental engine producing plausible prose is insufficient.

## Qwen IQ3_S: reviewed results

[Public receipt](../../../reports/2026-10-24-qwen-iq3s-coverage.json).
This new placement completes the workflows that previously stopped under
memory pressure. It has not completed the twelve coding tasks or editor tests.

| Component | Result | What it shows |
|---|---:|---|
| Public instruction router |39/40,338.984s | Correct source discovery and deep-copy merge; self-tests omit some cases |
| Changed-file/history |8/8,176.000s | Correct earlier markers, current revision, zero and unknown fact; correct read inventory |
| File-driven TypeScript |5/6, strict compilation passes | Accepts nonplain objects because prototype validation is missing |
| File-driven SQLite |0/6; combined TS/SQL346.515s | Migration aborts with FOREIGN KEY constraint failed |
| Public total |52/60 | Three completed workflows, with real behavior defects |
| Private instruction audit |29/36,638.6s |20/24 semantics,4/6 citations,5/6 code; missing instruction details and mutable-default alias |
| Exact smoke |Failed formatting | Returned READY. rather than READY; API and subsequent real tool reads work |
| Twelve coding tasks |Pending | No composite or promotion claimed |

All generated code was reviewed before the sequential WSL/bubblewrap checks.
The public merge passes all six independent groups and seven model self-tests.
The self-tests redefine the function, so independent checks are the reliable
validation of the selected implementation. The private merge instead copies
only local data and aliases values added from base. Passing the public version
does not certify the private one.

Maximum sampled process working set was13.32GiB, private bytes4.81GiB; these
are different memory measures. Minimum free system RAM was5.07GiB across the
public tasks and6.07GiB during the private audit. Free device VRAM never fell
below2941MiB; that includes other desktop GPU activity. Logs report2196.81MiB
GPU weights,680MiB GPU KV,268MiB GPU compute and11969.61MiB CPU-mapped weight
buffers. The process reached58.22C GPU temperature; no new hardware event was
reported. Both owned servers stopped normally. No maximum-context claim follows
from the smaller history fixture.

Historical Q4 also scored52/60 public and31/36 private. The new IQ3_S is a
useful smaller-memory candidate, but this is an observational comparison across
different runs/conditions. The real bugs are logical and contract-related;
these results do not support a rule that all sub4-bit code loses syntax.

## Higher Flint runtime and installation

The six-line optional prefetch patch was ported to exact b11838 commit
4231b23dc2c46661d01157aac5245bdcf03ce4b1. The opt-in changes only initial mmap
prefetch; later demand paging and all model math remain. Scope/security/general
checks from upstream's code-review skill were applied to this local experiment;
no upstream contribution is being submitted. The built DLL is
10331e86ab5bd3f8c08c486f42d900f1dd09dbab218ce54a8684b7ec7b65c35f.

[Compatibility receipt](../../../reports/2026-10-24-b11838-prefetch-control.json):
54 stock binaries remain byte-identical; CPU and GPU greedy small-model output
match across stock, modified-default and modified-opt-in. Only the opt-in logs
disabled initial prefetch. This is compatibility evidence, not full-model
numerical equivalence.42 offline lab tests pass, including catalog pin rejection
for an unreviewed runtime. A further four private downloader-control checks pass;
the live download now reuses the existing tested Strata range downloader, avoiding
a second maintained implementation. Production b11562 is unchanged.

The retained Bolt file was fully rehashed and exactly removed to make room for
Q4: [rotation receipt](../../../reports/2026-10-24-bolt-disk-rotation.json).
Its quality remains untested and queued; disk rotation is not model rejection.
Production Qwen Q4 and Gemma fallback files remain. The Q4 download was switched
from a slow single HTTP stream to bounded parallel ranges, preserving its
contiguous prefix. Separate range bookkeeping prevents treating a preallocated
file as downloaded data; full SHA256 is required before the final filename/load.

## Priority optimization found in installed runtimes

[Upstream PR29887](https://github.com/ggml-org/llama.cpp/pull/29887) merged the
`--moe-cache-mib` GPU expert cache on7October. Local source inspection confirms
the flag in both b11562 and b11838. This is a more immediate test than adopting
an unmerged fork. It caches selected host experts on the GPU, with separate
banks for differing tensor layouts. Large prefill batches use a different
path; a decode speedup is not automatically a shorter full workflow.

The older records already include a2GiB Qwen Q4 cache experiment: private
27/36 in402.703s, versus31/36 on the selected profile, with a strict TypeScript
failure. Its GPU/layer placement and non-mapped load differ from the selected
configuration. That result is not proof the cache intrinsically reduces model
accuracy: it copies the same weights, and different kernels plus stochastic
generation can change an answer. The new tests target previously unmeasured
IQ3_S/Flint configurations and preserve this existing evidence.

Plan: retain the uncached controls and compare a1536MiB Qwen IQ3_S cache under
the same64K GPU-q8-KV, CPU38 placement and frozen prompts. For Flint Q4, first
measure the uncached bounded-paging profile; if paging is the limiting factor,
move a few additional complete expert blocks to CPU and spend the released
VRAM on a1536MiB cache. Record both changes explicitly. Keep400MiB free-VRAM
and2.5GiB free-RAM stop floors. No cache result is measured yet.

[PR30449](https://github.com/ggml-org/llama.cpp/pull/30449) improves non-mapped
Windows expert transfers by splitting pinned host allocations. It is relevant
to `--load-mode none`, but pinning an oversized model would conflict with this
apps-open paging experiment. Do not enable it as an assumed universal fix.

The new private IQ3_S run's final request has37,447 prompt tokens and4,483
generated tokens,41,930 total. This is actual context occupancy evidence;
32K would be insufficient for that recorded conversation. Its allocation still
remains a680MiB64K GPU KV arena, not a freshly growing680MiB per-file allocation.

## Higher-precision live trial

14:35IST: Flint Q4 XL completes and matches full SHA256. The downloader exits
before inference. Available desktop memory falls to16.26GiB RAM and6108MiB
VRAM; original CPU42 profile rejects its6400MiB load gate. A second recorded
preflight also rejects6398MiB. Neither rejection is an inference/quality result.

14:36IST: separately named `flint-q4xl-cpu44-paging64` starts its first guarded
public trial. CPU44 reduces non-CPU-expert weight spans from4.690 to3.893GiB
before actual embedding placement, with the same64K GPU q8 KV. Its VRAM load
gate is5800MiB;2.5GiB RAM/400MiB VRAM/1GiB commit stop floors remain. The process
working-set maximum retains5GiB of initial freeRAM as reserve, so substantial
paging is expected. Public prompts use temperature1 and the frozen16K/4K output
allowances. Load/smoke limits are300/120seconds; whole workflows remain1200.
Raw record: `local-data/2026-10-24-precision/flint-q4xl-cpu44-a-public/`.

The fallback loads in about6seconds of engine time and returns exact READY
in2.547seconds. Actual CUDA allocations:3675.22MiB weights,979.89MiB KV,
299.85MiB compute, plus20.35MiB host compute. The effective resident working-set
maximum is10.915GiB, derived from the launch's freeRAM minus5GiB. Initial
completed router turns show5.24/7.42 prompt tokens per second and6.67/7.14
decode tokens per second. The workflow remains in progress; these are not
completed quality scores. Page-fault counts increase rapidly, but that counter
includes soft faults and must not be presented as disk I/O alone. A whole-disk
sample also shows about96MB/s reads on the shared D:/E: disk; it is not isolated
per-process attribution.

Two additional controls are frozen, not run: CPU48 plus1536MiB GPU expert cache
(same approximate GPU budget, two placement changes), and CPU44 with ubatch256
instead of128. The latter tests whether more prompt tokens can reuse weights
per processing batch under paging; it may need more GPU scratch. Neither
control relaxes the stop floors, changes the questions or increases the deadline.

14:57IST: the uncached CPU44 router hits1200.031seconds after seven valid
reads and no final-content characters. [Sanitized outcome](../../../reports/2026-10-24-flint-q4xl-cpu44.json).
No quality score is assigned. Minimum freeRAM5.153GiB, commit9.291GiB,
VRAM663MiB; maximum GPU53.62C, working set10.915GiB, private bytes5.940GiB.
The server stops normally and no new hardware event is found. Other suites
are not run on this failed profile. This is a latency rejection, not an OOM
or evidence that the final code would have been incorrect.

14:57:41IST: `flint-q4xl-cpu48-cache1536-paging64` starts the same public
questions in a fresh owned server. It allocates1531.39MiB native GPU expert
cache for21574MiB host experts. Exact READY takes3.219seconds. The new initial
freeRAM permits a12.627GiB working-set cap versus10.915GiB in the control;
that change in desktop headroom is an additional confound. Do not attribute
the entire eventual timing difference to the cache. Raw run:
`local-data/2026-10-24-precision/flint-q4xl-cache-a-public/`.

15:18IST: the cache trial also hits1200.031seconds, with seven valid reads.
It emits2130 visible characters near the end but no completed answer.
[Outcome](../../../reports/2026-10-24-flint-q4xl-cache1536.json). Minimum free
RAM4.724GiB, commit10.103GiB, VRAM828MiB; peak GPU55.19C, resident12.627GiB,
private bytes5.823GiB. Both controls stop normally without new hardware events.
This cache allocation does not produce a usable workflow win. The source logs
cache hit statistics only on destruction; the ownership guard terminates the
process, so no measured hit-rate claim is available.

15:21IST: start `qwen-iq3s-coding-a` with the same CPU38 profile, native.6
sampling,64K GPU-q8 KV and16K per-answer limit as the completed IQ3 suites.
The collector enforces1200seconds per question and never executes answers.
Source review and sequential isolated grading follow shutdown. New header-only
inspection also prepares `qwen36-iq4xs-cpu35-coverage64`:12.240GiB CPU expert
weights and4.262GiB other spans before embedding placement. Its18GiB RAM and
6000MiB VRAM load gates reserve capacity for runtime and desktop use. It is
not yet measured; the CPU38 proposal and older stopped profiles remain intact.

15:38IST: IQ3_S coding `intervals` reaches16384 output tokens in1011.172s,
all in reasoning, with no delivered implementation. Decode is16.241tok/s;
initial94-token prompt takes2.340s. This is an output-limited, unscored answer,
not a measured syntax failure. The saved reasoning repeatedly revisits touching
interval cases. The collector proceeds to TTL/LRU with unchanged controls.
Preserve the native result before separate32K-output or4096-reasoning-ceiling
diagnostics; both retain the1200second wall deadline. A reasoning ceiling is
an engine control, not Qwen's native high/xhigh setting.

15:49IST: prepared three new, unmeasured follow-ups. IQ3 budget4096 changes
only the runtime reasoning ceiling. Gemma26 CPU28 reserves additional GPU
headroom for64K q8 KV, with18GiB physical/16GiB commit load gates; its topK20
matches the frozen collector rather than the publisher's64. K2 Horizon64K
uses explicit CPU placement for attention-value experts as well as FFN experts,
GPU q4 KV and bounded paging. Source inspection shows `--n-cpu-moe` alone
does not move its3.955GiB attention-value experts. Corrected estimates are
saved separately; the earlier all-expert sums were not predictions of that
flag's actual placement. The IFM model is not Kimi K2. No profile has loaded yet.

15:57IST: native IQ3 coding is intentionally stopped after TTL/LRU also emits
16384 reasoning tokens with no code (1072.656s). DAG is interrupted at46.735s;
nine later native cases remain unrun on this rejected configuration. The
owned server stops normally, hardware check clear. Its wrapper finalizer raises
FileExistsError on the already-created stop marker; the stale manifest/error
are preserved and an independent reconciled-stop receipt confirms shutdown.
Future wrapper stop-marker creation is now idempotent. No hardware or model
failure is attributed to this maintenance error.

15:58IST:42 offline tests pass in18.594s between loads. A fresh IQ3 twelve-task
suite starts with only the runtime reasoning ceiling changed to4096. Native
public/private scores remain separate. The original two output failures and
all intervention/resource evidence are in the
[native coding receipt](../../../reports/2026-10-24-qwen-iq3s-native-coding.json).

16:07/08IST: the4096-budget interval request completes in517.141seconds,
7734 output tokens,15.025tok/s. Its reasoning shares14,157 leading characters
with the native answer; actual budget exhaustion/forced termination is logged.
Visible source starts273.703seconds. Source review sees two code fences and
redundant quadratic work in the first implementation selected by the frozen
grader. No executable score yet; TTL/LRU and remaining questions continue.

16:14IST update: the uncached4096 control is deliberately stopped after two
completed answers to grade them and begin the expert-cache comparison. Interval
passes105/105 frozen checks; TTL/LRU passes34/34. TTL finishes307.172seconds,
4656 generated tokens,15.233tok/s. Its source also accepts NaN TTL; this is a
post-review diagnostic outside the frozen checks, not yet executed. DAG is
intentionally interrupted125.86seconds into its request; nine later uncached
cases remain unrun. The owned server stops normally and no new hardware event
occurs. [Control receipt](../../../reports/2026-10-24-qwen-iq3s-budget-control.json).

16:15IST: start the full twelve-question collection using the same IQ3 weights,
CPU38 placement,64K GPU-q8 KV,4096 reasoning ceiling and sampling, adding only
1536MiB native GPU expert cache. Raw evidence:
`local-data/2026-10-24-precision/qwen-iq3s-budget4096-cache1536-coding-a/`.
Process identity and current collection are verified after resuming. The first
two tasks finish145.344/140.390seconds at32.414/33.408 decode tok/s. Outputs
differ from the uncached control despite the same seed: the interval answer
omits merging touching spans. Thus whole-task speed differences include changed
output lengths, and speed is not a correctness claim. All twelve tasks continue;
source review precedes isolated grading after the owned server stops.

16:41IST: eleven cached coding requests have completed, each under151seconds;
JavaScript deep merge remains. Source review now identifies additional monetary
unit, strict-TypeScript and worker-scheduling defects. These are not yet
executable grades and cannot be attributed to cache/quantization alone from
one seed. Two separate NaN TTL diagnostic inputs are prepared from reviewed
uncached/cached source, outside frozen scoring. Next planned load is IQ4_XS
CPU35, followed by the Q4 coding baseline. Production remains stopped.

Prepared but unrun: Bolt CPU88/native thinking,64K q8KV, with its real
`medium_effort=false` and `truncate_history_thinking=false` template keys.
Gemma CPU28 gets a separately named mmap fallback if its stock non-mapped
profile fails commit preflight. The original needs a stock runtime; the fallback
explicitly names the reviewed b11562 prefetch variant. No memory floor is
relaxed, and no new profile inherits an older quality result.

16:43–16:47IST: all twelve cached IQ3 answers finish; median133.8595s,
range121.266–150.312s, decode31.051–36.763tok/s. After source review and
shutdown, isolated checks give six passes and six failures. The worker-pool
grader first falsely rejects its local `process()` identifier; a hash-scoped
recheck keeps the unchanged answer, all behavior checks and isolation, then
observes duplicate scheduling (10/11). Preserve both results; do not call this
an external-capability attempt. Both TTL variants fail the separate NaN test,
outside frozen scoring. [Cached coding receipt](../../../reports/2026-10-24-qwen-iq3s-cached-coding.json).
Minimum RAM6.151GiB/commit8.389GiB/VRAM1037MiB, peak GPU59.94C; normal shutdown,
no new hardware event. Offline42tests pass again in19.108s between loads.

16:48IST: begin IQ4_XS CPU35 public workflow collection with its frozen native
profile,64K GPUq8KV,.6 temperature and1200second workflow deadlines. Current
RAM headroom recovered from17.08 to18.49GiB between post-grading snapshots;
the original18GiB load gate is retained. No application is stopped. Full
integrity and fresh launcher gates still apply. Raw:
`local-data/2026-10-24-precision/qwen-iq4xs-cpu35-a-public/`.

16:52IST: IQ4's uncapped process trips the2.5GiB RAM floor at2.436GiB free,
interrupting the router after190.25seconds. Peak resident RAM16.662GiB,
minimum freeVRAM475MiB; no new hardware event. This is unscored, not a code
failure. A separately frozen CPU35 paging profile starts16:53 with the same
settings/floors plus a13.356GiB resident maximum (initial freeRAM minus5GiB).
The matched bounded retry is collecting; no application was closed.

17:13–17:16IST: IQ4 bounded public trial finishes and stops normally. Source
review and isolated checks give55/60: router39,TS5,SQL3,history8. Workflow
times536/406.843/195.375seconds. The migration runs but lacks tenant uniqueness
and leaves foreign keys disabled; TypeScript misses plain-object validation.
FreeRAM minimum3.862GiB, commit7.300GiB, VRAM794MiB; peakGPU54.84C and
processresident13.356GiB. No new hardware event. A short-lived private-controller
argument-quoting error occurs before loading and is retained separately; the
corrected controller starts the same18GiB-gated profile after freeRAM recovers
to19.16GiB. No application is closed. Private audit collecting; coding next.

17:36-17:46 IST: bounded IQ4 private audit is reviewed and isolated-graded:
29/36 (19 semantic,4 citation,6 code),725.4seconds,15 actual file reads. Four
retained alias/local-key diagnostics also pass. Contradictory policy mapping,
missing routing steps and an unsupported installer-branch explanation remain.
Minimum freeRAM4.340GiB/VRAM841MiB; peak processresident14.048GiB/GPU58.06C.
Normal stop, no hardware event. Receipt: reports/2026-10-24-qwen-iq4xs-private.json.
IQ4 native direct coding starts17:36:45; the first case is still reasoning at
nine minutes. A separately frozen presence1.5 diagnostic retains all original
settings, including repeat_last_n64; it is unrun and inherits no quality score.

Progress checkpoint d90e41b is pushed to experiment/flint-precision-20261024.
CI40093080544 passes both Windows and Ubuntu. This is an in-progress checkpoint;
remaining coding/candidates and production restoration are still required.

17:57-17:58IST: IQ4 native interval coding hits1200.016s without visible code; eleven later tasks unrun. Normal owned stop, no hardware event. RAM minimum3.927GiB/commit6.988GiB/VRAM914MiB; resident13.105GiB. Separate presence1.5 native-thinking control starts17:58; actual sampler value verified, repeat_last_n64 unchanged. No native score inherited. Raw/controller identity and report saved.

18:19-18:20IST: IQ4 presence1.5 control exhausts16384reasoning tokens in1187.703s without code. TTL deliberately stopped47.875s; ten later tasks unrun. Normal owned stop, hardware clear; resource receipt saved. PlainQ6 header fetched only between engines: CPU40 experts24.791GiB, embeddings0.503GiB, otherweights1.991GiB. Full download not done. Q4 native twelve-task collection begins with original CPU37 profile; fresh gates/identity remain enforced.

18:25IST follow-up frozen, not yet run: Q4 CPU40/cache2048/general32K.
This combines the publisher's general-thinking temperature1/presence1.5 recipe
with native reasoning,32K coding output and2GiB GPU expert cache. It is a joint
usability configuration, not an isolated quant/cache experiment. Header-only
estimates put CPU experts18.225GiB, embeddings0.503GiB and otherweights1.876GiB;
cache/KV/runtime allocations still need measurement. The native Q4 baseline
runs first. Its results do not transfer to this new configuration. All physical
RAM, commit, VRAM, hardware and1200second gates stay unchanged.

The distinct plain Q6 artifact is now catalog-pinned and header-inspected,
with full download/load pending. It has24.791GiB CPU expert spans atCPU40;
substantial paging is expected with apps open. Before calling it unusable,
a changed placement/cache profile may be tested, but decode-only gains do not
address the slow prefill observed in the historical larger XL artifact.

18:33-18:44IST: Q4 native interval request completes623.235seconds,
9636generated tokens,15.629decode tok/s; visible source starts604.047seconds.
Source review saves two defects before execution: the merge aliases/mutates
the first input interval, and subtraction omits the surviving final tail.
No isolated score yet. TTL/LRU and subsequent questions continue in the same
owned server. Q4 native results remain separate from the queued CPU40/cache2GiB
publisher-general/32K-output configuration. No other model or grader is active.

19:25IST Q4 native coding midpoint: five of six attempted questions deliver
code. Intervals623.235s has input-mutation and missing-tail source defects;
TTL1052.078s exhausts16384 reasoning tokens without code, unscored. DAG370.609s,
scheduling349.921s and inventory317.844s appear contract-consistent on source
review, with executable checks pending. CSV911.640s delivers source but treats
quoted commas as separators and mishandles quoted CR/CRLF characters. Every
completed visible implementation has a hash-linked review; none executed on
the host or while inference is active. The two-file money task is collecting.

19:57IST Q4 native coverage: eight of nine tasks have delivered implementations;
TTL remains an unscored16K reasoning-only limit. Money finishes503.921s,
SQL report557.828s and SQL interval union577.562s. Visible source reviews
are saved before execution; TypeScript is still collecting. Windows dedicated
GPU counter19:52:40 reports4.679GiB for the known server PID and13.861GiB
resident RAM. Device-wide8268MiB includes applications, not only the model.
The sampled link is PCIe4.0x16; no clock/hardware settings changed. No score
is assigned until shutdown and isolated grading.

20:04?20:08IST Q4 native collection stops at2.449GiB availableRAM; no hardware event. Nine completed answers isolated-graded: seven passes, intervals31/105 andCSV69/120 failures. TTL16K output-limited, worker pool resource-interrupted415.547s, deep mergeunrun. Complete-answer median557.828s. New receipt reports/2026-10-24-qwen-q4-native-coding.json. Post-grading freeRAM15.029GiB misses16GiB next-load gate; no app closed. Remaining native JavaScript and separate cache/general32K trials remain pending.

20:10?20:12IST: Flint Q4 XL exact-file retirement succeeds after full hash recheck; two failed router profiles preserved. FreeRAM recovers16.639GiB after grading with apps unchanged. Resume only Q4 native js_pool/js_merge in fresh guarded server using original profile and fresh smaller resident-cap resolution; original RAM interruption remains. Raw qwen-q4-native-coding-js-resume-a, controller21556. No concurrent download or grading.

20:34?20:37IST: Q4 native JavaScript resume completes, normal stop/no new hardware event. Frozen workerpool11/11 andmerge8/8 pass; separate post-review checks expose synchronous-second-worker scheduling and array-to-object replacement bugs (11/12 and8/9 with original checks retained). All12 native questions now attempted across runs:9frozen task passes,2failures,1output limit. First RAM interruption remains. Updated authoritative docs/grading.md and projectAGENTS; Claude importsAGENTS, both shared routers already cover it, adapters unchanged. Cache/general32K and plainQ6 remain pending.

20:40IST progress checkpoint: native Q4 completes all12 question attempts
across original/resumed runs:11 delivered answers,9 frozen task passes,2
failures,1 output limit. Two passing JavaScript answers also fail separately
recorded post-review diagnostics. Original RAM interruption remains preserved.
IQ4 native/presence controls fail completion. Flint Q4 exact-file retirement
after full hash frees space for the distinct plain Q6 download, now active.
42 offline tests pass in18.925s; four existing PowerShell files parse; public
audit283files/zero findings and whitespace check pass. An initial parse command
named a nonexistent install.ps1; corrected enumeration checks install-widget.ps1.
This is an in-progress checkpoint, with cached Qwen, higher Q6, other candidates
and production restoration still pending. No completed-campaign claim.

21:02IST recovery: Q6 range downloader57548 remains active after a bounded
DNS-failure restart (4 to8 workers); completed ranges are flushed, with full
SHA256 still required before publishing the final file. Prior checkpoint
1a2ba5d passes Windows/Ubuntu CI40105882029. No inference engine is running.
Desktop availableRAM falls to13.213GiB, commit12.621GiB, VRAM6243MiB.
Original cache profiles reject16/18GiB admission. Separate resident7 calibration
profiles preserve those originals, cap resident pages at7GiB, increase reserve
to6.5GiB and retain every runtime stop floor;13.5GiB admission also rejects
this snapshot. No load is attempted. This is a reduced-residency hypothesis,
not a fit claim; fresh checks follow download/hash. Source inspection also
confirms the native cache's32-token small-batch boundary, so ubatch32 is a
possible distinct prefill experiment, not a measured speedup. No apps closed,
clock changes, system-cache flush or concurrent grading.

21:07–21:17IST: IQ4 exact-file retirement follows fresh full hash; no baseline
weights removed. FlintQ3XL download starts. At21:11 RAM recovers13.7GiB;
both bounded downloaders are explicitly stopped through verified child PIDs
76200/80032, preserving252/437 Q6 ranges and10/276 Flint ranges. Their wrappers
57548/81572 are not inference engines. Resume from checkpoints only after
inference stops; final file length is not completed-download evidence.

Q4 resident7 smoke completes6.187s with READY. (exact-format miss), normal
owned stop and no hardware event. MinRAM6.870GiB/commit6.404GiB/VRAM1193MiB;
maxresident7GiB/private6.455GiB, GPU52.22C. Actual weights1921.34MiB GPU,
expertcache2046.59MiB, attentionKV680MiB, recurrent62.81MiB, compute408MiB.
The CPU_Mapped20699.72MiB value is a mapped span, not resident RAM.
Receipt reports/2026-10-24-qwen-resident7-smoke.json. A fresh same-profile
interval/TTL coding diagnostic starts21:12 (controller44780), native reasoning,
temperature1, presence1.5,32K output and1200s each. Early generation4–7tok/s
is slower than unconstrained cached runs; memory remains above stop floors.
No answer/quality score yet. Downloads, hashing and isolated grading stay off.

Research additionally inspects five pinned ik_llama.cpp source files' memory
paths: Windows device buffers disable bulk prefetch, and a separate pinned
allocator cap exists. No engine installation or local speed claim. New community
Flint recipe reviews distinguish creator-reported coding/perplexity tradeoffs,
two-GPU fork-specific KV settings and preview metadata from our measurements.

21:33–21:37IST: fixed7GiB Q4 cache/general32K interval reaches1200.016s,
26016 reasoning characters and no visible code. Last intermediate7929tokens,
6.69tok/s; TTL unrun after abort. Normal stop/no hardware event, minRAM5.700,
commit5.234GiB, VRAM504MiB, peak53.88C. Report and hash-linked incomplete
review saved; no grader execution or score. Both downloads resume after
engine exit: Q6 wrapper21792, FlintQ3XL18004. Postflight RAM15.578GiB.
42offline tests pass19.594s with captured subprocess exit0, four PowerShell
scripts parse, public audit289files/zero findings. Original PowerShell stderr
pipeline returned1 despite42/OK; preserved log and direct capture retry resolve
the wrapper ambiguity. No inference overlap. This remains in progress.


## Resume 26 October

Original prompt: ?continue? ? continues higher quantization, deep optimization
research and unfinished Qwen/other-model tests; no cancellation or new scope.

Preflight: project local-coding-lab; branch experiment/flint-precision-20261024;
apps remain open, one engine,1200second whole-prompt deadlines and no editor
input. Current dated resume follows a completed25October private collection.

08:04?08:10IST: source-reviewed Gemma audit23/36 (15semantic,2citation,6code),
798.6seconds. Final corrected code fence selected unchanged and all six frozen
checks pass in existing WSL isolation after engine exit. Raw private sources
remain outside Git. Public57/60 and private23 use topK64 versus20 respectively;
no direct-coding/composite result or promotion. Actual next-load RAM falls from
3.722 to2.169 then1.379GiB; all six queued profiles reject and download is
withheld. No new hardware event/boot. Apps and production settings untouched.
Research rechecks open hybrid-cache PR30594 head9177f03 and its unchanged
prefill/multi-token limitation; newer Strata terminal notes do not update Qwen
engine packages. Remaining collection/production restoration stay pending.
