# Current model comparison

Updated 26 October 2026. Components and completion gates matter more than a
single leaderboard number. Claude's newer campaign was private; this table
brings its reviewed summary into the public lab. Results are agent-assessed,
not independently human-reviewed. It is not a controlled universal ranking.

26October clarification: the table retains its frozen1200second cohort.
The owner now permits separately labelled longer accurate coding diagnostics;
a plain greeting taking600seconds remains a practical failure. New
[Flash-Next](tasks/2026-10-26-flash-next/2026-10-26-flash-next-v0.10.0.md) and
[dense27B](tasks/2026-10-26-qwen38-dense/2026-10-26-qwen38-dense-v0.10.0.md)
article reviews reopen concrete engine/quant work, without new scores yet.
Gemma's new CPU28/resident4/64K calibration passes plain native-thinking API
greetings in12.77/8.20seconds and two completed coding cases. A separate NaN TTL
diagnostic fails. Its6GiB residency control completes all12answers with10frozen
task passes, median710.843seconds. CSV and TypeScript fail; extra TTL/pool checks
also fail. The additional array-replacement merge check passes.
Neither profile inherits earlier public/private scores or proves editor use.
[Qualification evidence](../reports/2026-10-26-article-qualification.json).

| Candidate | Private /36 | Public /60 | Coding /12 | Practical result |
|---|---:|---:|---:|---|
| Qwen3.6 35B-A3B UD-Q4_K_M, mapped64 | 31 | 52 | Not collected | Retained leader on available components; private 699.7 s; SQL failure and aliasing diagnostics remain |
| Qwen3.6 Q4 CPU37/native64K,24October |Unrun |Unrun |9 frozen task passes;2 failures;1 output limit |All12 attempted across original+JSresume. Original RAM stop preserved. Interval/CSV failures; separate checks expose JS scheduling/replacement bugs despite frozen passes. No historical scores transferred |
| Qwen3.6 Q4 CPU40/cache2GiB/resident7/general32K |Unrun |Unrun |Interval1200.016s deadline; TTL unrun |Separate smaller-memory calibration loads, but no visible code by deadline. RAM/VRAM/hardware guards clear; last intermediate decode6.69tok/s. No quality score |
| Qwen3.6 Q4, historical2GiB expert cache |27 |Separate historical cases |Not collected |Private402.703s; strict TypeScript and SQL defects; different placement/non-mapped profile, not evidence that expert caching intrinsically lowers intelligence |
| Qwen3.6 Q5 | 28 | Separate historical cases | Not comparable | Lower private score; retired |
| Qwen3.6 UD-Q6_K_XL | 28 | Historical completed cases | Not comparable | Private 2099.7 s, exceeds current gate; retired. Plain UD-Q6_K below is a different artifact |
| Qwen3.6 plain UD-Q6_K, CPU40/cache2GiB/resident7 |Unrun after gate failure |Router1200.016s deadline |Unrun after gate failure |Seven successful reads; first visible answer1080.828s, incomplete at deadline. Resource/hardware checks clear; no correctness grade. Exact artifact retired after the follow-up below |
| Qwen3.6 plain UD-Q6_K, CPU40/cache2GiB/resident10 |Unrun after gate failure |Router1200.031s deadline |Unrun after gate failure |Seven successful reads; first visible824.609s and6989partial characters. Earlier visible output is not completion or a pure residency speed comparison. Original18GiB profile capacity-rejected; exact file retired22:46IST |
| GLM-4.7-Flash UD-Q4_K_XL, f16 KV | 27 | Separate historical cases | Not comparable | Private 942 s, below Qwen on this audit; retired |
| Gemma 4 26B-A4B QAT Q4_0 | 19 | Separate historical cases | Not comparable | Retained lower-memory fallback; private 400 s |
| Gemma 4 26B-A4B QAT, CPU28/resident8,24October |Unrun on new profile |Router38/40; TS5/6; SQL0/6; history incomplete |Unrun on new profile |Router1031.860s,TS/SQL1142.469s. Python groups6/6 andself-tests8/8 pass; TS prototype validation and SQLite FK error remain. History4096-token reasoning-only limit789.282s; no full total |
| Gemma 4 26B-A4B QAT, CPU26/resident8 |23 |57 |Unrun; current capacity rejection |Private798.6s: semantics15/citations2/code6. Public uses topK64; private explicitly20. Conflicting fact ownership, unread citations and missed closeout remain despite correct merge. Public skips linked TS/SQL rule; prototype-validation/self-test defects. No full composite or promotion |
| Gemma 4 26B-A4B QAT, CPU28/resident4, extended64K |Unrun |Unrun |Two completed frozen passes; partial suite |Intervals105/105 in1105.766s; TTL34/34 in964.140s. Separate NaN TTL fails. Intentional stop interrupts DAG; nine later cases unrun. No hardware event |
| Gemma 4 26B-A4B QAT, CPU28/resident6, extended64K |Unrun |Unrun |10/12 frozen passes; all12 complete |CSV104/120, TS syntax/compile failure; separate NaN TTL and synchronous worker-failure defects. Merge extra passes. Median710.843s; CSV2135.172s. Greetings10.891/6.656s; no hardware event or transferred workflow scores |
| Gemma 4 31B dense QAT Q4_0 | 26 | Historical completed cases | Not comparable | Private 7234 s; fails current latency gate; retired |
| Qwen3-Coder-Next 80B Q4 | Unscored | Separate historical cases | Not comparable | Private tool-loop limit after 4075 s; retired |
| Qwen3-Coder-30B UD-Q4_K_XL | Deadline | Separate historical cases | Not comparable | Public cases complete, private 1200 s deadline |
| Kimi-Linear 48B Q4 | Capacity rejection | Separate historical cases | Not comparable | Not evidence of poor answer quality; retired |
| Qwen3.8 27B dense Q6 / TQ3 | Unscored | Interrupted | Not collected | Roughly 1.4-2.1 decode tok/s; long requests/restart, not promoted |
| Qwen3.8-Flash-Next 125B, Strata IQ3_XXS | Not completed | Coding deadlines; empty history final | Not collected | Separate replays recover facts; not a retroactive workflow pass; retired |
| Qwen3.8-Flash-Next GSQ-RCO Q2_0, Strata0.1.50 |Not run |Not run |Not run |New engine staged and verified; Q2 shards not yet downloaded. Requires61.86GiB plus packing/headroom; current volume has about34.4GiB free. Complete current candidates before exact-file retirement. Smaller quant is a capacity control, not an assumed quality upgrade |
| Bonsai 2 27B PQ2_0 | Not run | Stopped | Not run | Partial CPU placement only 2.3 tok/s; retired |
| Bonsai 2 27B PTQ1_0 | Not run | Deadline | Not run | Full GPU, router exceeds 1200 s after one tool turn; retired |
| LFM2.5 24B-A2B QAD Q4_0 | Deadline | 48 | 6 completed passes of 12 | Private reasoning loop; coding includes deadline/truncation, so 6/12 is task completion, not twelve completed correctness grades; retired 23 October |
| Qwen3.6 UD-IQ4_XS | Not run | Router 39/40 only | Not run | TS/SQL interrupted by RAM guard; not a complete public score |
| Qwen3.6 UD-IQ4_XS,CPU35 bounded64K,24October |29 |55 |First task1200s deadline; eleven unrun |Private725.4s,code6/6 plus extra4/4. Instruction omissions/path contradiction/control-flow misexplanation remain. Native interval problem delivers no code; public SQL/TS bugs and prior RAM stop preserved |
| Qwen3.6 UD-IQ3_S,38 CPU expert blocks |29 |52 |Two reasoning-only16K output limits; later cases interrupted/unrun |24October: private638.6s, all public workflows complete; alias, TS validation and SQL migration bugs; exact smoke punctuation fails. Separate capped controls appear below |
| Qwen3.6 UD-IQ3_S,4096 reasoning ceiling |Not collected on this variant |Not collected on this variant |Two completed passes; deliberately stopped before full suite |Intervals105/105 and TTL34/34; native scores above cannot be transferred. Redundant interval work and extra NaN TTL finding remain |
| Qwen3.6 UD-IQ3_S,4096 ceiling plus1536MiB GPU expert cache |Not collected on this variant |Not collected on this variant |6/12; all twelve complete |Median134s,31–37tok/s. Interval,CSV,money,strictTS,worker-pool and deep-merge defects. Worker-pool lexical false alarm corrected by hash-scoped unchanged-source recheck; six task passes unchanged. Extra NaN TTL fails |
| K2 Horizon MoVA 36B-A4B Q4 | Not run | Not run | Not run | Downloaded, queued; no demonstrated apps-open fit. [Qualification report](tasks/2026-10-24-k2-mova/2026-10-24-k2-mova-v0.9.0.md) |
| Nemotron 3.5 Bolt 74B-A9B 24GB | Not run | Not run | Not run |Verified file rotated off disk24October for Flint Q4; quality still queued |
| Recursive Flint UD-IQ3_XXS, uncapped reasoning | Not run after gate failure | Router deadline | Not run after gate failure | 1200.031 s, seven reads, zero final text; clean shutdown, unscored |
| Recursive Flint UD-IQ3_XXS, CPU KV, 2048 cap | Not run after gate failure | Router deadline | Not run after gate failure | 1200.016 s; visible planning after cap, no finished answer |
| Recursive Flint UD-IQ3_XXS, GPU KV | 29 | Router 39/40; TS/SQL tool limit; history output limit | **11 completed passes of 12** | All 374 frozen checks on eleven complete answers pass; CSV produces no code before output limit. Private 692.5 s; separate NaN TTL bug; no full public total or promotion |
| Recursive Flint UD-Q4_K_XL, CPU44/GPU KV |Not run after gate failure |Router1200.031s deadline |Not run after gate failure |Seven valid reads, no final answer; resource/hardware guards clear |
| Recursive Flint UD-Q4_K_XL, CPU48/cache1536 |Not run after gate failure |Router1200.031s deadline |Not run after gate failure |Seven valid reads, partial visible answer starts1137s but remains unfinished; memory guards clear |
| Recursive Flint UD-Q3_K_XL, CPU49/cache1536/resident4/32K |Not run |Not run |Not run |Full download/hash verified26October. Smaller allocation profile and extended collection prepared; queued after the current Gemma run. Plain greeting must complete first;32K qualification is not long-context validation |

## What changed in Claude's work

The active [precision and coverage campaign](tasks/2026-10-24-precision-and-gaps/2026-10-24-precision-and-coverage-v0.9.0.md)
reopens the unfinished candidates. IQ3_S's earlier capacity/VRAM failures remain
valid historical trials; its new38-CPU-expert profile completes public/private
collection with conservative guards. Higher Flint Q4 is verified; its uncached
CPU44 profile and CPU48/1536MiB expert-cache variant both miss the router
deadline. No higher-Flint-precision quality score exists yet. IQ3 capped/cached
coding completes6/12 passes; its native settings remain a separate experiment.
IQ4's bounded-memory workflows score55/60 and private audit29/36 after source
review and isolated checks. Its native direct-coding interval task then reaches
1200seconds with no delivered code; eleven later tasks are unrun. A separate
presence1.5 control also exhausts16K reasoning tokens without code; later
cases are interrupted/unrun. Native thinking is retained in both controls. Missing
compatible components still prevent a composite.

At21:07IST the exact tested IQ4_XS file is hash-verified and retired; its scores
remain above. Qwen plainQ6 subsequently finishes download/full SHA and loads
at21:58; its public workflow then reaches the deadline without a complete answer. FlintQ3XL remains partial and is
paused during inference. Reduced-residency Q4/Q6 profiles preserve the original
larger profiles: the7GiB Q4 coding calibration hits its deadline without code,
while the7GiB Q6 smoke succeeds. The earlier13.213GiB capacity rejection remains
historical; Q6's fresh launch has16.98GiB available RAM. All runtime stop floors
remain unchanged.

At22:46IST the exact plainQ6 file and its completed download checkpoint are
retired after a fresh full SHA check. The second10GiB-resident router attempt
also misses1200seconds. Neither attempt has a correctness score; remaining
suites are explicitly unrun after the principal workflow fails qualification.
Gemma26's separate smaller-residency public trial starts22:48IST. Full details
and limitations are in its [report](tasks/2026-10-24-gemma26-coverage/2026-10-24-gemma26-v0.9.0.md).

The separate CPU26/publisher-sampling trial finishes25October00:24IST with
all public workflows complete:57/60 after source review and isolated checks.
The Python implementation passes6/6 groups; one of its own seven tests has
an incorrect assertion after explicitly mutating an input. Its SQL migration
now passes6/6, while TypeScript still accepts nonplain objects. The model
honestly lists five TS/SQL file reads but omits a required linked v2 rule.
History passes the original4K-output two-turn case; its prose read inventory
is correct even though the old grader only extracts bullets. Both original
grader outputs and documented assembly/semantic corrections are preserved.
Minimum freeRAM3.916GiB, commit1.253GiB, VRAM1320MiB; no hardware event.
Fresh13.115GiB RAM subsequently rejects the next Gemma/Qwen/K2/Bolt/NVFP4
profiles. These remain capacity dispositions, not quality scores. The paused
FlintQ3XL download resumes only with inference stopped.

The subsequent Gemma private audit completes25October00:46IST in798.6seconds;
source review and isolated grading finish26October:23/36 (15/24 semantic,
2/6 citations,6/6 code). Seven documents delivered; one oversized logging read
fails and is not recovered. The final inventory omits one actual source, and
the answer includes unsupported citations, wrong machine-fact ownership and
local-validation/closeout advice. The final explicitly corrected Python fence
passes all six checks unchanged. This is a weaker result than historical Qwen
Q4's31/36 on this audit, but not a matched-sampler causal model ranking.
Record: [private evidence](../reports/2026-10-25-gemma26-cpu26-private.json).

On26October08:07IST, no engine is running and only2.169GiB RAM is available
(7.747GiB commit/5347MiB VRAM). All six queued profiles reject before loading;
even the bounded download is deferred below its desktop reserve. No new boot
or hardware event is observed since the last run. This is changed application
pressure, not a new failed model test; apps stay open and production is not
silently restarted below its admission checks.

- Added the twelve-task executable suite and a consistent 50/30/20 scorecard;
  regraded the public baseline as 52/60 and LFM as 48/60.
- Returned to a strict 1200-second gate. Earlier two-hour or six-hour runs
  remain useful diagnostics but cannot rank as usable everyday completions.
- Demonstrated paging/thrashing with apps occupying about 56 GiB: a roughly
  20 GiB model slowed to 0.3-2 tok/s. Commit capacity did not establish RAM fit.
- Used CPU affinity excluding logical CPUs 0/1 after core-0 machine-check
  records. This is a precaution, not proof of the faulty component or a cure.
- Added candidate/runtime pins and exact-file retirement receipts. These
  unpublished changes are preserved; report coverage is still incomplete.

## Our assessment

Qwen Q4 remains the retained quality reference, not a guarantee of fit under
today's application load. More quantization bits have not consistently improved
these tasks. Fast generation did not rescue Bonsai's incomplete workflow; LFM's
good public router score did not predict private instruction reliability. Test
the actual file-reading and code contracts, not a greeting or tokens/second alone.

Claude's displayed 86.3 for Qwen combines only private and public components
after renormalization. No complete three-suite leader exists. Keep component
scores visible and collect comparable missing components before declaring a
new composite winner. Current driver 621.01 differs from the earlier 617.42;
timing comparisons across those conditions are observational.

On this desktop,10GiB GPU memory is not all available to inference: applications
already occupy roughly3GiB. Flint's short probe uses5.097GiB dedicated GPU memory
and10.377GiB peak process RAM, leaving about1.4GiB device VRAM at its lowest
sample. Filling the remaining VRAM is not itself an optimization target; the
profile must retain scratch/headroom under real prompts. Its13.537GiB mixed
GGUF is a constrained experiment, not the publisher's distilled NVFP4 artifact.
No conclusion about higher Flint quantizations follows from this one profile.

Flint's GPU-KV profile is more promising than its CPU-KV variants: the router
finishes in 523 seconds and its private audit in 693 seconds. The latter scores
29/36 versus Qwen Q4's 31/36. Its deep merge passes the frozen checks and all four
extra nested-alias/local-only-key diagnostics. The lost audit points concern
instruction omissions, incomplete platform guidance and unsupported citations.
However, the public TypeScript/SQLite tool loop and history output limit prevent
a complete public score. Good code on the finished merge tasks is not sufficient
evidence for replacing the owner's instruction-heavy coding assistant.

The twelve direct coding prompts show a different strength: Flint completes
and passes eleven, including both SQLite queries, strict TypeScript, exact-money
changes across two files, and JavaScript concurrency/deep cloning. CSV uses its
16,384-token allowance without delivering code. Median completed-task time is
225.6 seconds; the worker pool takes 688.1 seconds. All 374 frozen behavior and
compiler checks on the eleven complete answers pass, but a separate positive-TTL
diagnostic exposes acceptance of NaN and non-expiring entries. This is not
bug-free certification. It is 11 completed passes versus LFM's 6 on the same
questions, under different recorded sampling/runtime/desktop conditions; Qwen
still lacks this component, so there is no matched all-model coding ranking.

Flint's direct SQL and TypeScript success does not erase the file-driven
TS/SQL tool-loop failure. The distinction is important for this owner's work:
being given a precise function contract is easier to use reliably than having
to discover files, recover from missing paths and maintain project instructions.

A separate fresh-server history diagnostic raises the output allowance to
8,192 tokens and passes 8/8 in 328.016 seconds. It does not replace the original
4K-output failure or establish tool-error recovery/maximum context. Flint's
tested weights were retired after a fresh full hash, while its installer,
runtime and evidence remain. Qwen Q4 stays selected for the owner's workflow.

## Reports and provenance

- [Qwen3.6 model record and active coverage](tasks/2026-10-24-qwen-coverage/2026-10-24-qwen36-v0.9.0.md)
- [Higher precision and offload research](../research/reviews/2026-10-24-precision-and-offload.md)
- [Flint standalone record](tasks/2026-10-23-flint/2026-10-23-recursive-flint-v0.8.0.md)
- [All-model inventory through 17 October](tasks/2026-10-17-complete-model-inventory/2026-10-17-all-models-gemini-and-availability-v0.4.1.md)
- [Matched Q4/Q6 and expanded candidates](tasks/2026-10-16-memory-and-candidate-expansion/2026-10-16-memory-context-and-expanded-model-tests-v0.4.0.md)
- [Strata](tasks/2026-10-18-strata/2026-10-18-strata-on-10gb-v0.6.0.md)
- [TurboQuant](tasks/2026-10-19-azllm/2026-10-19-azllm-and-turboquant-v0.7.0.md)

Private source records reviewed: the 20 October local-LLM campaign v1.0,
local-llm skill evaluation/runtime/hardware/leaderboard references, 21 October
IQ3_S attempt/stop receipts and Claude's current catalog/profile changes.
Private instructions and raw answers are intentionally not copied here.
