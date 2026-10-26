# Recursive Flint on RTX 3080 10 GB

Current evidence at27October03:22IST:

Next fallback is a separate resident1/40K/output32K profile because available
RAM after shutdown falls to7.7-7.8GiB. It reduces the owned working-set ceiling
from4to1GiB while retaining the6.5GiB startup reserve; physical admission is
7.5GiB. Commit7.5GiB,VRAM5500MiB and runtime floors are unchanged. A hard
working-set limit does not cap private allocations or standby pages. Expect
more paging; a600second plain-greeting qualification must pass before the
1024/8192/native reasoning controls. These are planned diagnostic conditions,
not a measured improvement or a budget-only comparison with B.

| Artifact / trial | Measured result | Disposition |
|---|---|---|
| UD-IQ3_XXS,23–24October | Router39/40; private29/36;11completed coding passes of12; separate8K-output history8/8 | Historical partial components, no full composite; exact weights retired |
| UD-Q4_K_XL,24October | Two router attempts hit1200seconds; seven source reads each | Incomplete/unscored; exact weights retired; extended retry remains queued |
| UD-Q3_K_XL,26–27October,32K/resident4/cache512 | Greetings50.328/38.000s; router4095.422s and TS/SQL5039.500s both exhaust16384 last-turn output tokens with no visible answer; history8/8 in3380.750s | Router/TS incomplete/unscored; all required files delivered; history is extended-only, no full public total |
| Official distilled NVFP4 | Identity pinned; no local model load or quality test | Queued, a distinct artifact; not a demonstrated precision upgrade |

The [capped-router receipt](../../../reports/2026-10-27-flint-q3xl-router-limit.json)
preserves all turn timings and evidence hashes. The collection has now closed
with an owned requested stop and no new hardware event. Its
[complete receipt](../../../reports/2026-10-27-flint-q3xl-file-workflows.json)
includes the separately reviewed history grading; no model code was executed.

The [TS/SQL receipt](../../../reports/2026-10-27-flint-q3xl-ts-limit.json)
records six turns, all six required sources including the nested v2 rule,
and eight unavailable extra reads. Every turn has zero visible characters.
The last turn reports1508prompt plus16384generated tokens,17892total, below
the32768context capacity. Its generation takes4640.045seconds at3.531tokens/s.
The83m59.5s whole-case failure is an output limit, not an observed TypeScript
syntax or SQLite execution failure. No generated code exists to execute.
History completes afterward under the unchanged profile. It passes all six
facts, READY120 and the exact last-phase source inventory:8/8 in3380.750s.
Phase0 first displays READY at2639.093s; the8273new-token ledger prefill alone
takes1728.395s. Phase1 rereads the revised runtime file, retains earlier markers
and correctly returns null for the absent port. It never attempts the now
unavailable ledger, so this establishes retained-history use, not recovery
from an actually observed tool error. The120-record case is not50K/128K recall.
No partial full-suite score is synthesized from this one completed component.

Across2516telemetry samples, minimum available RAM/commit/VRAM is
3.760GiB/1.719GiB/803MiB; peak owned working set4.000GiB/private3.593GiB
and GPU50.66C. Working set and private commit overlap and cannot be added.
Poststop available capacity is8.705GiB RAM/10.380GiB commit/5725MiB VRAM,
then changes with desktop activity. Engine/controller liveness checks confirm
cleanup; no Ollama model is loaded. No native cache destructor counters were
printed, so cache hit rates remain unmeasured.

Read-only source inspection of both saved last-turn reasoning traces at02:36
finds repeated revision of the solution and proposed final structure. They do
not look like a network stream that stopped without generation: the server
delivered16384tokens and reported length in both cases. This is a qualitative
completion diagnosis, not an automatic repetition score or proof of its cause.
Code discussed inside reasoning is not a user-delivered implementation and is
not extracted as a replacement answer for grading. A larger output control can
test whether more room completes it; sampler caps test a different intervention.
Neither control has run yet, and neither can erase these native failures.

The [saved-input comparison](../../../reports/2026-10-27-flint-router-input-comparison.json)
confirms identical first serialized requests, question/source hashes and
served chat-template text between the older successful IQ3XXS router and the
new Q3XL attempt. The changed result is not explained by a changed opening
question or template text. It is still not a controlled quant-only comparison:
placement, context, batch sizes, residency, later tool turns and the allowance
also differ. Tokenizer-array equivalence has not been established.

The output-limited router used17902reported total tokens in a32768-token
context. Its missing answer is not evidence of a full context window or lost
input files. Current measured GPUq8 KV is476MiB global plus27.89MiB sliding
window. Global-cache sizing follows14full-attention layers,4KV heads,
128dimensions, separate K/V and34bytes per32values inq8_0:15232bytes/token.
At40960tokens that global component is595MiB; at131072 it would be1904MiB.
Those latter two figures are calculations, not measured Q3XL long-context
loads. Sliding-window rounding, workspaces and driver allocations are separate.
Allocated KV capacity, occupied tokens and resident process pages must not
be equated with each other or with persistent knowledge of omitted files.

A live history snapshot records10841retained tokens in the32768slot, while
the startup KV buffers are476+27.89MiB onGPU. The `/slots` field named
`n_prompt_tokens` is the current sequence length in this runtime, including
appended generation; it is not just the original request's input. The metrics
endpoint's16346cached-token counter is cumulative reuse across requests,
not live cache occupancy. These source-checked distinctions prevent double
counting. The run also creates bounded context checkpoints separately. This
snapshot does not establish recall accuracy, RAM-KV growth or128K operation.
[Sanitized occupancy receipt](../../../reports/2026-10-27-flint-context-occupancy.json).

The CPU49 label describes host placement of routed-expert weights, not an
assertion that every expert operation runs on the CPU. b11838's MoE cache
uploads selected missing experts into GPU banks and routes supported small
batches through those banks. Its source bypasses that cache when a batch's
worst-case selection exceeds a group's slots or the32-token cache threshold.
This profile allocates383slots across five layout groups (7/73/173/7/123);
each decoding token selects6experts per MoE layer, whereas a16-token prefill
can require96distinct experts in a layer. Cache use can therefore differ
between prefill and decoding. Slot counts alone are not a hit-rate measurement.
The source prints hit/upload counters during cache destruction, but this lab's
Windows launcher calls `terminate()` on its owned engine at cleanup. That does
not guarantee native destructor output; the completed short smoke contains no
such counters. Record their absence if B also lacks them rather than inferring
a hit rate from occupancy or claiming a successful measurement. This limits any claim
that the short low-CPU-use observation proves a particular bottleneck.
[Pinned cache implementation](https://github.com/ggml-org/llama.cpp/blob/4231b23dc2c46661d01157aac5245bdcf03ce4b1/src/llama-moe-cache.cpp).

**27 October continuation:** the first UD-Q3_K_XL file collection is closed.
Its smaller-buffer32K profile loads and answers plain greetings; router and
TS/SQL are length-limited, while history passes8/8 only with an extended
allowance. Native32K output and capped-reasoning controls remain pending. The completed
23–24 October scores below belong to UD-IQ3_XXS; they are not scores for the
new artifact. Only those older weights were retired. See the later dated
sections for capacity rejections, the measured admission profile and results.

A separate `flint-q3xl-cpu49-cache512-resident6-measured32` control is prepared,
not run: resident cap4 to6GiB, original6.5GiB reserve,12.5GiB physical admission
and5500MiB VRAM admission. The preliminary unrun10.5GiB/4.5GiB-reserve proposal
was superseded before launch after914 B samples showed minimum RAM4.540GiB,
commit1.719GiB andVRAM803MiB. This explicitly accounts for desktop variation;
all inference arguments,7.5GiB commit admission and runtime stop floors stay
fixed. Additional mapped-page residency may help, but page-fault counts alone
cannot prove disk traffic. Qualify plain greetings before sustained use.
Do not relabel the active4GiB run as this new profile.

The publisher's32768-token hard-task output recommendation was rechecked on
27October. A separate `flint-q3xl-cpu49-cache512-output32k-ctx40k` control is
prepared before the current router finishes:40960 context/32768 output,
otherwise the measured32K inference profile unchanged. Scaling measured476MiB
globalKV predicts119MiB additional allocation. Its initial unrun4500MiB gate
is revised to5500MiB using B's4351MiB maximum observed device decline, including
desktop variation:1030MiB remains after that decline plus119MiB moreKV,
630MiB above the unchanged400MiB runtime floor. This is a conditional follow-up
if the frozen16K-output answer is truncated, not a changed live request or a
new long-history claim. Verify actual allocation and input/output room before
collection. Native private24K and coding budgets retain their own identities.

The27October private-audit preflight review finds a concrete context constraint:
the earlier IQ3XXS audit's last request had41305input and9736output tokens,
51041total. Its third request already had35086input tokens. Therefore the
current32K file-workflow profile and the40K small-router output control cannot
establish that same full instruction audit. The unrun private controller now
refuses contexts below64K and requires explicit no-context-shift. A72K profile
would leave room for that observed41K input plus the full24K output allowance;
this is sizing, not a new allocation or a universal bound on future tool turns.
The actual request must still fit. Do not silently prune source history or
borrow the older private29/36 score. The larger private profile is not yet
qualified against the apps-open memory budget.
[Historical token-count evidence](../../../reports/2026-10-27-private-context-sizing.json).

`flint-q3xl-cpu49-cache512-private72k` is now a concrete unrun profile:
73728context,24576output, explicit no-context-shift, otherwise CPU49/cache512/
b64/u16/q8/resident4. Estimated globalKV1071MiB adds595MiB over measured32K.
Admission requires10.5GiB physicalRAM,8.5GiB commit and6000MiB freeVRAM;
all runtime floors remain unchanged. The device estimate retains1054MiB after
the prior4351MiB whole-device decline plus595MiB extraKV,654MiB above the
400MiB floor. Fresh admission and measured loader/greeting evidence are still
required. The prepared private controller's new context gate is untested until
the current inference ends; no private load has occurred.

At00:50:30–00:50:42IST, three read-only Windows counter samples show about
107–166MiB/s reads and87–91MiB/s writes on physical disk1, which serves both
D: and E:. System transition faults are89–136thousand/s, with25–46thousand
pages/s input. These are host-wide, non-simultaneous counter observations,
not an SSD benchmark or unique Flint I/O attribution. A later per-process
logical-I/O snapshot cannot identify which process caused those earlier
physical writes. Keep the private receipt and this concurrent-load caveat;
do not infer either a pure CPU bottleneck or exclusively hard-page-fault
traffic from the model's page-fault count. No cache flush or app stop occurred.

The01:18IST CPU observation spans10.073seconds and6.953CPU-seconds, or about
0.69logical cores busy on average for the owned engine. It does not isolate
storage, faults, GPU waits or thread scheduling. Normal process priority and
theFFFF process mask are observed; worker masks are configured separately.
Do not infer that raising the thread count will accelerate this profile.
The sanitized memory receipt includes this observation and its scope limits.

A later8.75second observation during history input processing finds the owned
engine using24.406CPU-seconds, about2.79logical cores busy on average. Whole-
device GPU utilization samples range25-43%, with7148-7165MiB occupied VRAM.
These are concurrent desktop readings, not model-exclusive GPU counters or a
causal bottleneck test. They show why occupied VRAM, GPU utilization and CPU
work need separate measurements; they do not justify filling the remaining
VRAM without budgeting the transient allocation already observed in B.
The read-only sampler used the existing Strata Python environment after the
lab Python lacked psutil; no dependency was installed during inference.

A separate8192-token reasoning-budget router control is prepared, unrun,
for the same40K-context/32768-output profile as the native larger-output
follow-up. Only the request's reasoning budget changes. Source inspection
of installed b11838 confirms a budget sampler that forces the reasoning end
sequence and can re-arm for another reasoning block. Therefore8192 is not
necessarily a whole-workflow or whole-answer ceiling. Verify actual request
fields, parser behavior, final delivery and correctness before crediting it.
This is runtime-imposed closure, not Flint's native high/xhigh effort; the
saved template reports no native effort support. The active native B run is
unchanged. Frozen16K failure and any later32K/budget results stay separate.

27October primary community reports supply two distinct leads. A b11838/Q4
Windows4060-laptop user reports empty finals when thinking consumes the
output budget, and improvement with a1024-token reasoning cap. Their experts
occupy about21.4GB host RAM; our4GiB residency and desktop load differ. Their
20-27tok/s and short tool checks are not our coding/long-history results.
An additional1024-budget control is prepared, unrun, with the same32768
output allowance. It tests the completion/accuracy tradeoff, not maximum
native reasoning. [Original firsthand report](https://github.com/ggml-org/llama.cpp/discussions/31093).

Separately, issue31000 describes literal tool XML trapped in reasoning with
`finish_reason=stop` on NVFP4/b11823/OpenCode. The author explicitly lacks the
original raw SSE and a deterministic reproduction. Our router ends`length`,
so this is a parser-integrity lead, not a diagnosis or confirmed duplicate.
Do not promote hidden reasoning into a final answer or execute embedded XML.
[Original issue](https://github.com/ggml-org/llama.cpp/issues/31000).

The publisher's own `rec` engine was also checked on 27 October. Its published
requirements are Apple Silicon M4/M5 Pro or Max and at least 48 GB unified
memory. Its reported speedup excludes prefill and comes from an M4 Pro, so it
is not an available Windows/RTX 3080 replacement or evidence for our throughput.
No `rec` installation was attempted. [Official repository](https://github.com/recursive-oss/rec).

Recursive's current generation guide says Flint always reasons and advises
against unsupported effort/disable-thinking controls. It recommends inspecting
`finish_reason` and raising the output allowance after a length stop. That
supports the separate native 32K-output control. The 8192/1024 controls instead
use an explicitly supported llama.cpp sampler intervention; neither is a
publisher-trained effort level or guaranteed improvement. All keep the supplied
template and parser, with no custom stop strings. [Generation guide](https://docs.recursive.com/guides/generation-settings),
[troubleshooting](https://docs.recursive.com/resources/troubleshooting).

23–24 October 2026. Installation and all three scorecard collections are
complete: GPU-KV router 39/40, private audit 29/36, and 11 completed coding
passes of 12. Public tool/history failures prevent an overall score or
production promotion. A separate larger-output history diagnostic passes 8/8.
The tested Flint weights were retired after preserving evidence and verifying
their full hash again; Qwen remains the selected production model.

## Requested work and status

| Requirement | Status | Evidence |
|---|---|---|
| Review Claude's new campaign | Done | Private 20 October campaign, local-llm skill, 21 October records; aggregate comparison |
| Install and evaluate Flint on latest metrics | Done, incomplete answers preserved | Pinned Unsloth GGUF and llama.cpp b11838; three components attempted |
| Update comparison and make standalone report | Done | This report, component JSON receipts and current comparison |
| Make reporting mandatory for future models | Done | Public reporting policy, project adapters and private local-llm skill |

## Selection and frozen plan

Production Qwen Q4 is retained. The first Flint configuration is Unsloth
UD-IQ3_XXS, 14,535,427,520 bytes (13.537 GiB), because the initial snapshot has
only about 13 GiB physical RAM and 6.5 GiB dedicated VRAM free with apps open.
This is a constrained quantization trial, not evidence about BF16 or the
publisher's NVFP4 model. The Q4 alternatives are larger than today's prudent
memory budget. Do not infer quality from the bit count alone.

Use the existing scorecard v2 questions and grading: private instructions /36,
public router/history/TypeScript/SQLite /60, twelve coding cases /12. Report
components separately. A weighted composite requires all three; partial
coverage is not comparable to a complete score. Each prompt has a 1200-second
whole-workflow deadline. Preserve reasoning, final text and actual requests.
Publisher sampling is temperature 1.0, top-p 0.95, top-k 20; old baseline uses
temperature 0.6. That difference must remain explicit. No promotion from one
seed, one partial suite or API readiness alone.

The Mac-only rec engine is inapplicable to this Windows/CUDA machine. Install
llama.cpp b11838 separately, leaving the production binary untouched. Check
native Flint support, chat parsing, actual weight/KV allocation and hardware
events before sustained evaluation. Do not weaken memory guards to obtain a score.

## Initial machine snapshot

- GPU: RTX 3080, 10,240 MiB total; 3,439 MiB used, 6,615 MiB free;
  driver 621.01 (different from Claude's 617.42).
- RAM: 63.91 GiB total, approximately 13.08 GiB available.
- Commit: approximately 21.03 GiB available.
- E: approximately 7.81 GiB free before exact-file retirement.
- No llama/Strata/Python experiment process found; Ollama service exists.
  Its loaded-model list was subsequently confirmed empty before launch.
- Boot: 23 October 00:14 local. Subsequent checks report RAM at 3000 MT/s;
  no hardware settings were changed and no new hardware event appeared in
  the completed trials.

## Sources

- [Recursive announcement](https://recursive.com/updates/introducing-recursive-flint)
- [Original checkpoint and architecture](https://huggingface.co/RecursiveSI/flint)
- [Selected GGUF publisher](https://huggingface.co/unsloth/flint-GGUF)
- [rec supported hardware](https://github.com/recursive-oss/rec)
- [Pinned runtime release](https://github.com/ggml-org/llama.cpp/releases/tag/b11838)

Vendor benchmark scores and speed claims are not measurements on this machine.
Pin identities are in experiments/flint/pins.json. Raw local evidence is kept
under ignored local-data/2026-10-23-flint/.

## Validation and findings

Pre-inference findings:

- Both b11838 runtime archives pass full SHA256 checks; installed executable
  reports commit 4231b23dc. No production binary was replaced.
- Header inspected independently without loading weights. Architecture is
  flint, 49 blocks, 14 full-attention/35 sliding-window layers, 4 KV heads of
  dimension128. GGUF configured context is262144; the announcement's512K claim
  is not a tested capacity of this artifact/profile.
- Weight spans:8,082,423,808 bytes IQ2_S;4,829,741,056 IQ3_XXS;
  1,567,641,600 Q6_K;49,283,072 BF16;867,456 F32. Labels describe a mixed
  recipe; do not treat UD-IQ3_XXS as uniform3bit or the publisher's NVFP4.
- 36 CPU-MoE blocks estimate8.699GiB CPU expert spans and4.833GiB other
  weights before token-embedding placement and runtime costs. Compact64K
  q8 KV is estimated near1GiB, not the generic16GiB from earlier advice.
- Inspected b11838 source: lazy-mode affects only TENSOR_READ_LAZY tensors;
  Flint's expert tensors are not flagged. Initial lazy-mmap proposal was
  corrected before any run. Selected load-mode none avoids Windows whole-file
  prefetch; 13GiB physical/18GiB available-commit launch gates,2.5GiB RAM and
  400MiB free-VRAM stop floors. No guard was lowered during a measured run.
- Latest private collector uses24576 output tokens; public router/TS-SQL
  use16384 and history4096; coding uses16384. These are retained for comparison,
  below the publisher's suggested32768 hard-task output allowance. The strict
  1200second wall gate remains. Higher-budget diagnostics must be separate.
- Existing lab baseline:38 offline tests pass. Public audit at this checkpoint
  scans223 files with0findings; this is not a final post-change validation.

Raw header receipts: local-data/2026-10-23-flint/header.json and header-v2.json.
The latter reuses the maintained scripts/gguf_metadata.py parser and agrees
on spans. These were pre-inference receipts; measured results follow below.

## Measured installation and smoke

The complete model SHA256 matches the pinned publisher artifact. No change to
production Qwen weights or runtime. The independent b11838 server reaches ready
in12.85seconds and answers exactly READY in0.937seconds. This four-token probe
only validates loading and response plumbing, not coding performance.

| Smoke measurement | Observed |
|---|---:|
| Peak server working set |10.377GiB|
| Peak server private commit |15.612GiB|
| Loaded process dedicated GPU memory |5.097GiB|
| Minimum system RAM available |4.410GiB|
| Minimum available commit |4.329GiB|
| Minimum whole-device VRAM free |1459MiB|

WDDM shared GPU memory overlaps host memory; adding it to process RAM double
counts allocations. Context capacity, allocated cache and actual occupied tokens
are different quantities. This profile requests64K context and q8 K/V on CPU;
the smoke does not validate long-history recall or64K prompt processing.
The template supports preserved reasoning/tool calls but reports no native
reasoning-effort control. Do not label this an xhigh-effort measurement.

Public attempt a made seven valid source reads, then was interrupted with no
finished answer. The controller/server disappeared without a stop receipt.
On resume, Windows still reported the same00:14boot; no new WHEA, bugcheck,
unclean-restart or application-crash event was found during the interval.
Cause remains unknown. The original running manifest is preserved with a
separate recovery receipt; the attempt is unscored. Attempt b uses a fresh
directory, identical frozen settings and a detached hidden controller.

### Uncapped reasoning result

Fresh attempt b reaches the hard deadline at **1200.031 seconds**. It completes
seven source reads, emits50,287 reasoning characters across its turns, and
delivers **zero final-content characters**. It is unscored. Owned shutdown
completes normally; no new hardware event is reported. Peak process working set
10.601GiB, private commit15.821GiB; minimum system RAM available2.581GiB,
available commit5.837GiB, free device VRAM1414MiB. This is an answer-completion
failure, not an observed OOM or syntax failure.

Remaining uncapped cases are not run after that gate failure. The follow-up
`flint-iq3xxs-moe36-cpukv64-b2048` changes only the runtime reasoning budget
from unlimited to2048 per turn. Same questions, sampling, output limits,
placement and resource gates; fresh evidence directory. This is a measured
follow-up only after collection completes, not a claimed native effort level.
See reports/2026-10-23-flint-native.json for the sanitized outcome.

**Live follow-up interpretation:** the2048 budget stops growth of the API
reasoning channel and visible content begins near the budget boundary. Reviewing
that content shows continued planning/revisions, not a completed final answer.
Do not equate a channel transition with an effective end to deliberation or a
usable response. The early progress interpretation was corrected before scoring.
Only the finished workflow can establish a latency/quality improvement.

The capped attempt also reaches the deadline: **1200.016seconds**,10,547
reasoning characters and52,945 content characters. Content starts181.406seconds
into the workflow but continues planning/revisions. Clean owned stop, no new
hardware event. It is unscored; remaining capped-CPU cases are not run.

### GPU-KV follow-up

Keep native reasoning,64K context, q8 K/V and the frozen sampling/questions.
Remove `--no-kv-offload`, increase `--n-cpu-moe` from36to38, and enable verbosity4
for allocation evidence. The expert threshold counts initial transformer blocks;
Flint's first two are dense. Moving two more expert blocks to CPU makes room
for GPU KV. This is a feasible placement bundle, not a cache-only intervention.

Measured loader allocations: CUDA model4184.29MiB, CUDA_Host model9672.56MiB;
full-attention KV952MiB (65536cells,14layers), sliding-window KV27.89MiB
(768cells,35layers). Total GPU KV979.89MiB, about0.957GiB. CUDA scratch157.35MiB,
host scratch20.35MiB. These arenas allocate at load; occupied token slots grow
later. Context checkpoints are separate from the primary KV arena.

The public router completes in **522.985seconds** across three turns, with
seven successful source reads. First final-tool-free-turn content arrives at
432.578seconds; earlier4.375second visible text is only a plan before tool calls.
Native decode during its longer turn stays near21tokens/second. Source review
finds correct precedence, honest absent settings and a plausible deep merge.
Tests omit explicit zero and deeper list/dictionary aliasing checks. After
source review, the isolated WSL/bubblewrap grader passes6/6independent behavior
groups and8/8model tests. Codex-assessed router score **39/40**, deducting one
point for incomplete test coverage. This is a single-seed case study.

The TypeScript/SQLite task hits16tool rounds after41.6seconds: six valid source
reads followed by26unavailable-path reads, with no delivered implementation.
It is unscored, not an observed SQL or syntax defect. The history workflow hits
its4096-token output limit after226.719seconds, without completing phase0.
It has no retained-history or changed-file quality score. Only1of3public
workflows completed; no valid public /60total or weighted composite exists.

Measured across the GPU-KV public trial: peak process RAM10.194GiB, private
commit15.779GiB, dedicated GPU memory at ready5.444GiB; minimum available system
RAM6.198GiB, available commit2.316GiB, free device VRAM1247MiB. Long router-turn
decode21.368tokens/second over10,907generated tokens; initial/tool-result
prefill198–252tokens/second. These are observational comparisons with changing
desktop load, not numerical equivalence or a controlled cache-only speedup.

Latest validation:41offline tests pass18.871seconds, including early stream EOF
preservation as incomplete. The coding collector has not changed the twelve
questions/rubrics. Its revised hash is frozen separately before coding inference.
Private and coding outcomes follow below. Production Qwen's configuration
has not been changed or promoted away.

### Private instruction audit

The GPU-KV profile completes the unchanged private audit in **692.5 seconds**,
four assistant turns, with all fifteen frozen instruction sources delivered.
One oversized read is rejected and successfully retried with a valid range.
The source snapshot is the existing 13 October corpus, evaluated under the
current scorecard; it is not a refreshed copy of today's instructions.

| Component | Score | Observed behavior |
|---|---:|---|
| Instruction semantics | 19/24 | Correct host distinctions and missing-service honesty; omissions in required reading, Windows adapters and the requested KV explanation |
| Grounded citations | 4/6 | Credential claim cites an unrelated header; installer guard citation does not support its ambiguous ahead-of-remote guidance |
| Isolated merge implementation | 6/6 | Preserves local values and recursively copies nested data |
| Total | **29/36** | Single seed, agent assessment, no independent human review |

Citations were checked against the bytes and line ranges actually delivered,
accepting both `path:line` and `path:Lline`. No points were lost merely for
citation formatting. The Python function omits the requested type hints and
docstring; those are a separate style finding outside the frozen behavior score.

After source review and the frozen isolated checks, four existing additional
diagnostics also pass: retained nested lists, inserted nested dictionaries,
local-only nested keys, and an independent copy with an empty base. These
post-review checks do not add points to the 36-point score. This is a concrete
strength over historical merge answers with aliasing or lost-key defects.

At one live observation the occupied sequence contains **48,035 tokens**;
the configured capacity is 65,536 and the allocated GPU KV remains **979.89 MiB**.
That observation is not a maximum-context or long-chat recall certification.
The primary KV arena reserves capacity when loading; occupied cells increase
as input and output arrive. Neither cache placement nor a larger window reads
an instruction file automatically or provides permanent memory after unloading.

In these llama.cpp builds, `--no-kv-offload` selects CPU cache placement;
removing it permits GPU KV for GPU layers. `--cache-type-k q8_0` and
`--cache-type-v q8_0` select precision, not location. Larger context capacity
does not ensure that an editor sends every instruction or that the model
faithfully uses every delivered file. Flint's measured arena is small because
of its actual attention layout, not a universal bytes-per-token rule.

Raw private answers stay in the external instruction-audit directory; the
public aggregate is `reports/2026-10-23-flint-private.json`. The server stops
normally with no new hardware event. The unchanged twelve-case coding suite
starts next in a fresh owned process, with a separately frozen collector hash.

Private-run memory telemetry: peak process working set 10.195 GiB, private
commit 15.760 GiB; minimum system RAM available 8.959 GiB, available commit
6.160 GiB and whole-device VRAM free 1,263 MiB. Maximum GPU temperature is
61.16 degrees C. Commit is not resident physical RAM, and WDDM shared GPU
memory must not be added again to those host allocations.

### Standalone coding results

All twelve unchanged cases were attempted in one loaded GPU-KV session.
Eleven complete answers pass **all 374 frozen checks**, including strict
TypeScript compilation. CSV reaches 16,384 output tokens after 760.860 seconds
with empty final content and remains unscored. No reasoning draft is substituted
for delivered code. Every output was reviewed before isolated grading, which
ran only after the owned server stopped. No new hardware event was reported.

| Task | Whole request seconds | Frozen checks | Outcome |
|---|---:|---:|---|
| Interval subtraction | 502.984 | 105/105 | Pass |
| TTL/LRU cache | 225.625 | 34/34 | Pass; separate NaN diagnostic fails |
| Dependency ordering | 159.891 | 64/64 | Pass |
| Streaming CSV | 760.860 | Not graded | Output limit, no delivered code |
| Weighted scheduling | 124.844 | 61/61 | Pass |
| Atomic inventory fix | 156.859 | 10/10 | Pass |
| Two-file exact-money fix | 276.797 | 15/15 | Pass |
| SQL customer report | 100.625 | 20/20 | Pass |
| SQL nested/touching intervals | 130.953 | 20/20 | Pass |
| Strict TypeScript validation | 372.953 | 26/26 | Pass |
| JavaScript worker pool | 688.110 | 11/11 | Pass |
| Defensive JavaScript deep merge | 384.312 | 8/8 | Pass |

Report this as **11 completed passes of 12 tasks**, with **11/11 correctness
among completed answers**. It is not twelve completed correctness grades.
All requests report zero cached input tokens; they share one loaded process,
not twelve cold model starts. Median completed-request time is 225.625 seconds;
the twelve requests total 3,884.813 seconds. Decode spans 20.98–22.72 tokens/s.

Peak process RAM is 10.105 GiB, private commit 15.638 GiB. Minimum system RAM
available is 6.828 GiB, available commit 4.598 GiB and whole-device VRAM free
1,149 MiB. A live sample during the final task measures 5.467 GiB dedicated
GPU memory; it is an observation, not a measured peak. Shared GPU memory is
not added to RAM. Maximum recorded GPU temperature is 44.59 degrees C.

**Additional observed bug:** source review identified that the TTL constructor
accepts `float('nan')` because its `ttl <= 0` comparison is false. A separately
prepared post-review isolated test confirms that no ValueError is raised.
The resulting expiry comparisons never expire entries normally. This is
outside the frozen suite and does not change its score; it is evidence that
passing the suite does not establish bug-free code. Candidate source was
neither repaired nor replaced before recording the result.

Evidence: `reports/2026-10-23-flint-coding.json`; raw collection, reviews and
isolated grades remain under ignored `local-data/2026-10-23-flint/coding-gpukv-a/`.

The interval response generates 11,020 tokens; its delivered code only starts
at 487.390 seconds of the 502.984-second workflow. This illustrates why decode
throughput alone is a poor proxy for response latency in this setup.

### Larger-output history diagnostic

The same two-phase history questions, native GPU-KV profile, seed 73 and
temperature 1.0 were run in a fresh server with **8,192 output tokens** per
turn instead of 4,096. The whole workflow still had a 1,200-second deadline.
It completes in **328.016 seconds** over seven assistant turns and scores
**8/8**: all six final facts, exact `READY 120` acknowledgement, and accurate
last-phase read inventory. It retains beginning/middle/end ledger markers,
reads runtime revision 2 with retry value zero, and gives the absent port as null.

Only `docs/runtime.md` was read in the final phase and the answer lists that
path correctly. No attempt to read the unavailable ledger occurred then, so
transient tool-error recovery was not demonstrated. Final-turn input is 12,703
tokens (12,662 cached), with 2,392 generated at 22.10 tokens/s. This is neither
a maximum-context nor a real-editor test. Fresh process/cache state differs
from the original public task sequence; this is not an isolated causal proof
that doubling output always fixes history behavior.

Peak process RAM 10.180 GiB, private commit 15.747 GiB; minimum available
system RAM 6.147 GiB, commit 1.282 GiB, free device VRAM 1,247 MiB. The server
stops normally and a post-run event check finds no new hardware event.
The original 4K-output failure remains unscored. Do not substitute this result
into its public /60 total. See `reports/2026-10-24-flint-history8192.json`.

## Artifact identity and reproduction

The original model is Apache-2.0 licensed. This experiment uses the separately
published Unsloth mixed GGUF, not Recursive's distilled NVFP4 weights. Full
download hashes were checked before inference; neither the production runtime
nor Qwen weights was replaced.

| Artifact | Pinned identity |
|---|---|
| Quantizer repository | `unsloth/flint-GGUF` |
| Revision | `20468edfc38ab43d6914cc88b08cbecb05d0fc62` |
| File | `flint-UD-IQ3_XXS.gguf`, 14,535,427,520 bytes |
| Model SHA256 | `7a0a095dde1d931063a5d571e19497d997edbc783eb1ed6b86529bfab9d94804` |
| Runtime | llama.cpp b11838, CUDA 12.4, commit `4231b23dc2c46661d01157aac5245bdcf03ce4b1` |
| Archive hashes | [Pinned assets](../../../experiments/flint/pins.json), both verified in full |
| Coding fixture SHA256 | `d69a90527dc9939d32c7a7751bb080064fcc24acfeeef97ab8c1fada84bceea5` |
| Coding evaluator SHA256 | `bf64b9d20732ba3dba8caf4a48012fad0d77719d5b44058790077b1738dd217c` |
| Coding collector SHA256 | `e6c1d8e4c9afa38aa8916ad0401d2ab6f507aa31d56f45d32d0bffdfded9a16e` |

The experiment uses loopback port 8081 and one slot. The GPU-KV recipe has
all eligible layers on GPU, `--n-cpu-moe 38`, 65,536 context, q8 K/V,
4 generation / 8 prompt threads, 512/128 batches, flash attention, native
reasoning and preserved history. CPU masks are `0x5554` and `0xFFFC`.
`--load-mode none --no-repack` is explicit; no lazy-loading or patched-runtime
speedup is claimed. The CPU-expert threshold includes Flint's two initial
dense blocks: 38 means 36 MoE blocks' routed experts go to CPU.

The load gates require 13 GiB free physical RAM, 18 GiB available commit and
6,500 MiB free VRAM. Runtime stop floors are 2.5 GiB RAM, 1 GiB commit,
400 MiB VRAM and 84 degrees C. Desktop applications stay open. The 3000 MT/s
RAM reading is recorded, not changed; CPU affinity is a precaution following
historical hardware events, not a diagnosis or demonstrated repair.

Use the [installation and trial commands](../../../experiments/flint/README.md)
with a new output directory for every attempt. The four frozen profile files
retain their pre-run proposal metadata; the measured reports, not those old
labels, describe their outcomes. The private frozen plan records all public
task/rubric/profile hashes; `coding-plan-v2.json` records the EOF-handling fix
before the first coding request. No task question or grading expectation changed.

## Interpretation and limits

**Measured strengths:** bounded apps-open fit, native tool support, correct
deep-copy merge behavior, honest handling of absent service facts, and a large
speed improvement from the feasible GPU-KV placement bundle. This can be useful
for supervised, explicit coding tasks whose outputs are independently checked.

**Measured weaknesses:** excessive deliberation, unsupported citations, omitted
instruction requirements and failed recovery from unavailable tool paths.
Neither a high router score nor fast token generation establishes reliable
autonomous work across many instruction files. The retained Qwen reference
still has the better private score and more complete public evidence.

**Decision:** retain Qwen Q4 as the default for the owner's instruction-heavy
workflow. Flint is promising for supervised Python utilities, exact-money
changes, SQL queries, TypeScript validation and JavaScript utilities when the
contract is supplied directly. Its direct coding results are substantially
better than the reviewed LFM run, but there is no matched twelve-task Qwen
result. Do not claim a universal coding winner. Prioritize a matched Qwen
coding baseline, then consider a separately pinned higher-precision Flint
trial if resource gates permit; more bits cannot be assumed to fix tool use.

Changing CPU/GPU placement also changes numerical execution and desktop load
varies; the 523-second GPU router versus two CPU deadlines is not a clean
single-variable speed ratio. Flint uses publisher temperature 1.0, whereas
the historical Qwen baseline used 0.6. Quantizers, runtime builds, driver
versions and cache states differ. No full Qwen three-suite baseline exists.

The template reports no native reasoning-effort control. An unlimited runtime
reasoning budget is not an `xhigh` setting; the 2,048-token cap moved continued
planning into the content channel without delivering a usable answer in time.
Higher quantization might change quality, but this experiment cannot establish
that it would fix missing instructions or tool loops.

| Variant or validation | Status / reason |
|---|---|
| CPU KV, native reasoning | Smoke passes; one interrupted router; fresh router deadlines; remaining suites not run after failure |
| CPU KV, 2,048 reasoning cap | Router deadlines; remaining suites not run after failure |
| GPU KV, native reasoning | All three components attempted; 11 completed coding passes, no complete public total |
| GPU KV, 2,048 reasoning cap | Prepared only; native suite prioritized after the CPU cap failed to improve completion |
| IQ2_XXS | Header inspected only during low free RAM; no full download or inference |
| Q4 or higher Flint quant | Not loaded: larger than the initial prudent apps-open memory/commit budget |
| 128K/256K/512K serving | Not tested; 48,035 occupied tokens is not a maximum-context test |
| Repeated seeds / held-out promotion | Not yet justified: incomplete public workflows fail the promotion gate |
| Actual Copilot/Continue Flint UI | Not run; owner no-typing constraint persists, and candidate is not promoted |
| Vendor rec engine | Supported Apple hardware differs from this Windows CUDA installation |

No new hardware event was reported during the completed owned trials. The
first controller disappearance has no established cause and remains unscored.
Historical PC crashes are not evidence that Flint caused a restart.

## Cleanup and production availability

Following the existing autonomous campaign's retirement policy, the exact
13.537 GiB Flint GGUF was removed at 01:09 IST on 24 October after a fresh
full SHA256/size check, resolved-path validation and confirmation that no
inference engine was running. No directory tree was deleted. The report,
raw evidence, model pins, reproducible installer and separate b11838 runtime
remain. Qwen Q4 and Gemma fallback weights are preserved. E: has 18.643 GiB
free immediately afterward. See `reports/2026-10-24-flint-retirement.json`.
The earlier LFM retirement is separately recorded; no other model was removed.

Production was already off at task start. Its unchanged Qwen Q4 configuration
2.3 passes a fresh preflight (18.601 GiB RAM, 24.460 GiB commit and 6,829 MiB
VRAM available) and the existing launcher restores it. Live health/model
responses verify alias `qwen3.6-35b-a3b-q4`, one slot and **131,072 context**.
The harmless request returns `READY.` in **15.641 seconds**, finish `stop`.
API availability passes, but the extra period fails the exact `READY` request;
that formatting failure is retained rather than normalized into a pass.

The healthy endpoint stays running at `http://localhost:8080/v1` with its
existing 1,800-second idle sleep and resource/hardware guards. No editor
settings, model selection, clock/driver, boot startup or retry loop changed.
No fresh Copilot/Continue UI test was performed under the owner's no-typing
constraint. API availability is not proof of editor latency or long-context
quality. Receipt: `reports/2026-10-24-production-restored.json`.

## Maintainer record

Source files actually read include the project AGENTS/CLAUDE/README,
methodology, grading and task/prompt logs; parent installation AGENTS/CLAUDE;
shared Codex guide, Claude router/Windows adapter, host facts, platform rules,
mandatory logging, coding/documentation, Git, Python and testing guidance;
the agent-context-maintenance and local-llm skills; Claude's evaluation,
runtime, hardware, candidate and leaderboard references; the 20 October
campaign and 21 October raw stop receipts. Frozen source snapshots were read
as benchmark evidence, not as new maintainer instructions.

| Files changed in the public task | Purpose |
|---|---|
| `AGENTS.md`, `CLAUDE.md` | Current campaign routing and shared standalone-report policy |
| `README.md`, `CHANGELOG.md`, `VERSION` | v0.8.0 status and documentation entry points |
| `catalog/models.json`, `catalog/runtime.json` | Reviewed Claude candidate pins and new Flint/runtime identities |
| `lab.py` | Preserve reviewed Claude runtime-flag allowlist support |
| `docs/model-comparison.md`, `docs/model-reporting.md` | Component-level comparison and future evidence requirements |
| `docs/tasks.md`, `docs/prompts.md`, `docs/tasks/README.md` | Progress, canonical closeout and report index |
| This report, `owner-request.txt` | One forwardable report and the preserved owner request |
| `experiments/flint/install.py`, `pins.json` | Explicit hash-verified bounded installer, separate runtime |
| `experiments/flint/inspect_header.py` | Metadata/tensor-span inspection without loading weights |
| `experiments/flint/collect_coding.py`, `tests/test_flint_collector.py` | Hard per-request deadline and incomplete-stream preservation; regression tests |
| `experiments/flint/README.md`, `public-tasks.json`, `smoke-tasks.json`, `history-diagnostic-tasks.json` | Reproduction and separately declared collections |
| `profiles/flint-iq3xxs-moe36-cpukv64.json`, `profiles/flint-iq3xxs-moe36-cpukv64-b2048.json` | Native and capped CPU-KV profiles |
| `profiles/flint-iq3xxs-moe38-gpukv64.json`, `profiles/flint-iq3xxs-moe38-gpukv64-b2048.json` | Native GPU-KV trial and unrun capped recipe |
| `reports/2026-10-23-flint-smoke.json`, `reports/2026-10-23-flint-native.json`, `reports/2026-10-23-flint-cap2048.json` | Sanitized smoke and unsuccessful CPU-profile outcomes |
| `reports/2026-10-23-flint-gpukv-public.json`, `reports/2026-10-23-flint-private.json` | Reviewed public/private outcomes and separate diagnostic checks |
| `reports/2026-10-23-flint-coding.json` | All twelve coding outcomes, timings, resources and separate NaN TTL defect |
| `reports/2026-10-24-flint-history8192.json` | Separate two-phase history diagnostic and its limits |
| `reports/2026-10-24-flint-retirement.json`, `reports/2026-10-24-production-restored.json` | Exact artifact retirement and live production availability/formatting evidence |
| `reports/2026-10-23-retirement.json` | Exact LFM artifact deletion after identity/evidence preservation |

Private updates outside Git: parent `CLAUDE.md`, local-llm `SKILL.md`,
`reference/evaluation.md`, `reference/leaderboard.json`, `reference/leaderboard.md`,
`scripts/scorecard.py` (coverage wording only), parent `docs/tasks.md` and
`install-log.txt`, campaign section 8, and ignored plans/controllers,
review receipts and raw evidence. Existing shared adapters already route to
their maintained sources; no duplicate global policy copy was created.
Unrelated Claude candidate profiles and retirement receipts remain untouched.

Actual command families: explicit installer `--apply`, header inspection,
`llama-server --version`, guarded `trial.py` public profiles, the private
instruction collector, detached owned coding collection, and reviewed
`wsl ... run_isolated.py` grading. Full CLI parameters are preserved in each
run's process/request JSON. Offline validation uses
`python -m unittest discover -s tests -v`, PowerShell parser checks,
`python scripts/audit_public.py`, and `git diff --check`.

Dependencies are the pinned GGUF and separate CUDA runtime under the existing
data root; no driver, CUDA toolkit, new WSL installation, editor extension,
cloud service, boot task or hardware setting is installed or changed. Existing
WSL/bubblewrap, Python, Linux Node 24.22 and TypeScript 5.9.3 perform grading.
No UI changed, so no new browser/mobile test is claimed.

Latest local validation: **41 offline tests pass in 18.161 seconds**; all four
PowerShell files parse. Final public-content audit scans239files with0findings;
Git whitespace checks pass. Results commit **1f8fa59** passes
[Windows/Ubuntu CI](https://github.com/paras-lehana/local-coding-lab/actions/runs/40014077502),
as did earlier implementation commits321be33/a507173. Canonical closeout is
recorded in docs/prompts.md; publication targets the existing public main branch.
No model weights, private prompts, credentials or raw answers are staged.

## Owner request

See the unchanged owner-request.txt alongside this document.

## Higher-precision follow-up, 24 October

The owner subsequently reopened Flint with higher precision and additional
tuning research. The [v0.9 precision campaign](../2026-10-24-precision-and-gaps/2026-10-24-precision-and-coverage-v0.9.0.md)
records separately pinned Q4 XL, Q3 XL and distilled NVFP4 candidates, a reviewed
b11838 initial-prefetch opt-out, and native expert-cache controls. Q4 now passes
its full hash. The CPU44/GPU-KV router hits1200.031seconds with seven valid
reads but no final answer, after the original VRAM gate rejected. The separate
CPU48/1536MiB GPU-cache trial also misses1200seconds; partial text begins only
at1137seconds and remains unfinished. No higher-precision quality score exists
yet. This follow-up does not replace the IQ3_XXS outcomes above.

20:10IST: Q4 XL's full SHA256 is reverified and its exact25,054,688,704-byte
file retired to make room for the requested plain Qwen Q6. Both1200second
router outcomes, runtime, original profiles and raw evidence are retained.
No code/private quality score is claimed for this rejected configuration.
Q3 XL and the publisher's distinct distilled NVFP4 remain separately queued.
[Retirement receipt](../../../reports/2026-10-24-flint-q4xl-retirement.json).

21:07IST: pinnedQ3XL range download starts after exact tested QwenIQ4
retirement. It runs alongside the still-active QwenQ6 download, with no
inference engine; both require final full hashes. The intermediate precision
is a new test of usable quality between smallerIQ3XXS and the slowQ4XL,
not an assumed improvement. No liveQ3XL result yet.

Header review confirms theQ3XL label describes a mixed recipe dominated by
IQ3_S6.123GiB,IQ3XXS4.594GiB,IQ4XS4.395GiB andQ8_01.555GiB; it contains
noQ3_K tensor. Q4XL instead mostly stores Q5_K11.305GiB andIQ4XS8.769GiB.
The official NVFP4 artifact stores20.668GiB NVFP4 plus0.619GiB BF16 and small
F32 tensors, with its separate training recipe. These spans are not resident
RAM. The research review records community precision comparisons and their
limits, plus retained preview metadata; no external score enters our table.

27October compatibility review: b11838 source contains an AVX2 NVFP4 CPU dot
kernel and a CUDA integer-dot-product path for NVFP4, so the format name does
not establish a hard Blackwell-only requirement. This is source evidence,
not a local NVFP4 model-load or numerical-quality pass. The publisher's tested
hardware and48GB recommendation refer to its full-GPU recipe; our partial
offload would be a distinct trial. Keep the publisher's distilled artifact
separate from a generic four-bit conversion of BF16 and from its specialized
Blackwell performance results. [Publisher recipe](https://huggingface.co/RecursiveSI/flint-nvfp4-gguf),
[pinned CPU source](https://github.com/ggml-org/llama.cpp/blob/4231b23dc2c46661d01157aac5245bdcf03ce4b1/ggml/src/ggml-cpu/arch/x86/quants.c),
[pinned CUDA source](https://github.com/ggml-org/llama.cpp/blob/4231b23dc2c46661d01157aac5245bdcf03ce4b1/ggml/src/ggml-cuda/vecdotq.cuh).

A CPU49/cache2048/resident7 Q3XL calibration is frozen separately to reduce
the predicted GPU footprint and host residency. It still requires a measured
smoke and fresh admission; current Q3XL download is checkpointed, not complete.

24October23:14IST trace review: original native TS/SQL had all six required
sources before26failed optional/guessed paths (package.json, tests, README,
tsconfig, alternative source paths and backups). The parser/read tool delivered
the initial files correctly. This refines the diagnosis to failure to finish
after sufficient evidence and poor unavailable-file recovery, not absent initial
context. The new quant must first run the unchanged workflow. A later explicitly
labeled tool-feedback recovery diagnostic is planned if that failure repeats;
no repaired transcript, synthesized file or retroactive pass is permitted.

## 26 October: Q3XL ready for smaller-residency qualification

UD-Q3_K_XL now completes its bounded download and published whole-file SHA256
check:18,494,977,472bytes,
`91b8d85ab6ff7fb095d9a972f9afa6f3fa2b9acb642867a079f3e013ea3c350c`,
revision`20468edfc38ab43d6914cc88b08cbecb05d0fc62`. The last resume takes
1407.766seconds. No Q3XL inference/quality measurement exists yet.

The additional CPU49/cache1536/resident4/32K profile is frozen for current
apps-open headroom. Its estimated weights1.515GiB+expertcache1.5GiB+q8KV0.480GiB
exclude scratch/runtime costs. Resident cap4GiB and6.5GiB reserve require
10.5GiB available RAM,10GiB commit and5000MiB deviceVRAM at admission; runtime
floors remain unchanged. This deliberately permits file paging and qualifies
32K only. It does not demonstrate the preferred long-context configuration.
Native preserved reasoning remains; plain no-file greeting precedes public
file-driven collection. Extended diagnostics use their own cohort under the
owner's clarified policy; earlier1200second deadlines remain unchanged.

A separately frozen`flint-q3xl-cpu49-cache1536-resident6-extended32` option
raises the working-set maximum to6GiB and RAM admission to12.5GiB, preserving
the6.5GiB reserve and all inference/commit/VRAM settings. Choose it before the
first load if fresh headroom permits, otherwise retain the4GiB capacity fallback.
Gemma's two matched-output pairs motivate this choice; they do not establish
a Flint speedup or quality gain. Both Q3XL profiles remain unrun here.

At22:12IST a third, explicitly experimental64K option is prepared:
`flint-q3xl-cpu49-cache1024-resident5-extended64`. Doubling q8KV from32K to64K
adds an estimated490MiB; reducing the expert cache1536to1024MiB roughly offsets
that device allocation. Microbatch32to16 keeps the context-times-microbatch
attention workspace estimate similar. Actual buffers must be measured after
loading; these estimates do not establish either fit or quality.

This option caps resident host pages at5GiB with a4.5GiB startup reserve,
requiring9.5GiB free RAM,10GiB commit and5000MiB device memory before loading.
The smaller startup reserve is an explicit experiment, not a general default;
runtime floors remain2.5GiB RAM,1GiB commit,400MiB VRAM and84C. CPU49,
four context checkpoints, native preserved reasoning and publisher sampling
remain. The server ceiling is32768output tokens, while each frozen collector
request retains its own explicit limit. This better matches the owner's
instruction/history priority than the32K capacity fallback. It is not yet
loaded or scored, and neither nominal64K capacity nor extra reasoning room
demonstrates that the final answer uses the supplied files correctly.

At 22:59 IST a conditional 7 GiB resident option is also prepared, with all
64K/cache1024 inference arguments unchanged. It restores the original 6.5 GiB
startup reserve and requires 13.5 GiB free RAM, 10 GiB available commit and
5,000 MiB free VRAM. Choose this option before loading only if fresh gates
permit; otherwise retain the smaller prepared option. Both remain unrun.
This uses additional available RAM without changing a started comparison or
claiming that the earlier Gemma residency improvement transfers to Flint.

### Smaller-buffer qualification after the commit stop

Gemma's long-input run stops at its commit floor. After its owned engine exits,
the next-load checks reject the prepared Flint/K2 profiles. A newly started
Gradle build is verified finished and its sole daemon idle; normal Gradle
shutdown stops it, and the Kotlin daemon subsequently exits too. Editors,
browser and emulator stay open. Available commit rises to about 7.8 GiB, still
below the prepared profiles' 10 GiB requirement. No unchanged gate is bypassed.

The new `flint-q3xl-cpu49-cache512-resident4-extended32` reduces 64K/cache1024
to 32K/cache512 and batch128 to64, keeping microbatch16. Estimated KV/cache
savings alone are about 1002 MiB. The earlier measured Q4XL/cache1536/CPU48
profile peaked at 5.823 GiB private commit; this configuration also removes
another GPU expert block and uses smaller weights/workspace. These allocation
changes support a provisional 7.5 GiB commit admission for greeting-only
qualification, with measured usage required before file workloads. The
4 GiB resident cap plus original 6.5 GiB RAM reserve, 10.5 GiB physical gate,
5,000 MiB device gate and every runtime stop floor remain explicit.

At 23:16 IST it admits 12.131 GiB RAM, 8.237 GiB commit and 5,318 MiB VRAM,
then loads. An initial live sample is about 3.42 GiB private commit, 4 GiB
working set, 5.05 GiB available commit and 2,449 MiB free VRAM. This agrees
with a materially smaller allocation, but no greeting or quality result is
claimed yet. Native preserved reasoning and q8 KV are retained. The 32K
experiment is a capacity qualification, not the owner's eventual long-context
configuration or a higher-precision quality win.

The qualification then completes normally: load 21.0 seconds; plain greetings
48.375/31.141 seconds, both 168 generated tokens and byte-identical visible
answers. Generation rates are 3.52/5.50 tokens/s. Both requests process all
three input tokens, so the second is a warm-engine request, **not** an observed
prefix-cache hit. Minimum free RAM/commit/VRAM is 8.165 GiB / 4.846 GiB /
2,432 MiB; peak private commit 3.440 GiB, working set 4.000 GiB, GPU 52.03 C.
Normal requested stop and no new hardware event.
[Greeting and allocation receipt](../../../reports/2026-10-26-flint-q3xl-greeting.json).

Measured GPU buffers are 1551.39 MiB weights, 476 MiB global KV, 27.89 MiB
sliding-window KV, 508.53 MiB expert cache and 67.56 MiB compute. This measured
headroom supports a separate `flint-q3xl-cpu49-cache512-resident5-extended64`
follow-up: keep cache512/b64/u16, increase global KV by 476 MiB for 64K, and use
5 GiB resident host memory with the original 6.5 GiB reserve. Its admission is
11.5 GiB RAM, 8 GiB commit and 5,000 MiB VRAM; runtime floors are unchanged.
Collect greetings again before the frozen public workflows, then hold this
configuration fixed. No file/coding quality result is transferred from smoke.

The 64K follow-up is rejected before loading at 23:29 IST: available RAM
8.996 GiB and commit5.938 GiB fail its11.5/8GiB admission. The subsequent
original32K file attempt passes the controller snapshot but the launcher's
fresh check finds less than5000MiB VRAM. It stops before readiness; neither
attempt receives a quality score or indicates a hardware error.

A separate measured-admission32K profile keeps every inference argument and
runtime floor unchanged. The completed smoke's named GPU buffers total
2631.37MiB and the observed whole-device decline is2886MiB. A4500MiB launch
gate therefore retains1614MiB above that decline,1214MiB above the400MiB
stop floor. This calibration replaces the provisional5000MiB estimate only
in `flint-q3xl-cpu49-cache512-measured32`; original profiles/receipts remain.
RAM10.5GiB/commit7.5GiB admission and4GiB residency are unchanged. The
23:46IST launch loads in18.469seconds and its first plain greeting completes
in50.328seconds. Remaining greeting/public workflows are collecting; no
quality, private-audit or long-context result is claimed at this checkpoint.

During the27October continuation, the first router request reads all seven
fixture files and continues beyond1200seconds without visible answer text.
It remains within the21600second extended allowance; no provisional code
score is assigned to reasoning-channel drafts. Owned resident memory stays
near4GiB and private commit near3.53GiB while whole-system headroom varies.
The current operating-condition snapshot records four16GiB DIMMs configured
at3000MT/s. A GPU sample reports8121MiB whole-device use,42% utilization and
345MHz graphics clock; a later performance query reports555MHz, P2 and idle
clock reason active, with thermal/power slowdown reasons inactive. These are
snapshots, not evidence of stock tuning or a proven clock-related bottleneck.
No clocks/settings are changed. Windows per-process GPU counters are excluded
from resident-memory attribution because some exceed the entire card capacity.
The fixed inference profile continues unchanged; later tuning must be separate.

At00:25IST the process counters distinguish private residency from commit:
working set3.99996GiB, private working set0.01313GiB, private committed bytes
3.52916GiB. These are not additive physical-memory categories. The remaining
working set contains shared/mapped pages and cannot be attributed exclusively
to expert weights from this counter alone. The same sample reports156,960
page faults/s, which includes soft faults and does not establish SSD saturation.
This motivates a later resident-cap comparison without changing the active
run. No larger-cap Flint performance or quality benefit is claimed yet.
