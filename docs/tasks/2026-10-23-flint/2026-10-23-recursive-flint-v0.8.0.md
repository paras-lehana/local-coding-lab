# Recursive Flint on RTX 3080 10 GB

23 October 2026. Work in progress. Installation and smoke completed; quality
evaluation continues. No replacement or quality ranking is claimed yet.

## Requested work and status

| Requirement | Status | Evidence |
|---|---|---|
| Review Claude's new campaign | Done | Private 20 October campaign, local-llm skill, 21 October records; aggregate comparison |
| Install and evaluate Flint on latest metrics | In progress | Pinned Unsloth GGUF and llama.cpp b11838 |
| Update comparison and make standalone report | In progress | This report; aggregate to follow |
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
  Its loaded-model state still needs checking before launch.
- Boot: 23 October 00:14 local. Current clock/tuning state and incident check
  remain preflight work, not assumed from historical notes.

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
on spans. Inference/quality results remain pending.

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
Private instruction audit and standalone coding collection are next; production
Qwen has not been changed or promoted away.

## Owner request

See the unchanged owner-request.txt alongside this document.
