# Current model comparison

**9 November restart update:** Flash-Next Q2 / Strata 0.1.50's 64K
GPU-KV growth trial ended in a confirmed 0x116 NVIDIA timeout-recovery crash
at 10:10:57 IST. Its 8K/17K fact answers and allocation growth are observations;
the interrupted 33K case and unrun shrink/private audit have no score. The exact
configuration is quarantined, no engine is running, and production remains off.
See the [incident and configuration](../reports/2026-11-09-flash-q2-gpu-restart.md).
This records workload association, not a proven parameter-level cause.

**9 November08:25IST:** tuned native Flint Q3XL72K finishes **31/36** in
6,386.703s, with6/6isolated merge groups, versus the earlier capped25/36 in
10,380.106s. Both are extended, different multi-setting profiles; no causal
reasoning-only claim. Required-reading/adapter/installer omissions remain.
All15sources read, normal stop/no new hardware event.
[Evidence](../reports/2026-11-09-flint-native-private72k.json).
This private result alone does not promote Flint or fill missing public/coding
components. Historical Qwen's31/36 remains in its own1200second cohort.

**9 November status correction:** [all model records](models.md) and the
[merged review](tasks/2026-11-09-merged-research/2026-11-09-merged-models-articles-and-experiments-v0.11.0.md)
are the current navigation. Flash Q2 shards were fully verified and packed on
3 November; the older “not yet downloaded” row below is historical. The new
engine completed static greetings; the later dynamic64K trial ended in0x116, unscored. b12069 now passes six tiny-model controls, not a
full-model comparison. Flint72K/cap1024 now completes the extended private
audit in10,380.106s with25/36 (18semantic/3citation/4behavior), all15sources
read and all8continuations fully reused. Null handling and mutable aliasing
fail isolated checks. [Receipt](../reports/2026-11-09-flint-q3xl-private72k.json).
No earlier router score transfers. Production remains capacity-gated and off.
Groot's two stops establish those two profiles' failure under their measured
headroom, not that every future apps-open profile requires closing apps.
The native Flint RAM stop does not by itself attribute growth to desktop apps.


Updated 3 November 2026. Components and completion gates matter more than a
single leaderboard number. Claude's newer campaign was private; this table
brings its reviewed summary into the public lab. Results are agent-assessed,
not independently human-reviewed. It is not a controlled universal ranking.

3 November: Flint Q3_K_XL run C is graded (see the dated note just above the
table), and Claude's 20-21 October runs now have standalone records
([audit addendum](#audit-of-claudes-20-21-october-runs-3-november)). Capacity
note: on this WDDM host, GPU buffers are charged to Windows commit at about
their own size; see
[VRAM allocations also consume Windows commit](memory-and-context.md#vram-allocations-also-consume-windows-commit).
Commit-floor stops and capacity rejections are host-capacity events, not
model-quality results. No score changes.

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

Gemma's separate 128K/640-record history run is resource-stopped at 23:05 IST:
available commit falls below 1 GiB during input processing, with no new hardware
event. It reaches 28,464 cached tokens but no history answer, so it has no recall
score. [Interruption record](../reports/2026-10-26-gemma128-history-resource-stop.json).
Flint Q3 XL's smaller 32K/cache512/resident4 profile completes greetings in
48.375/31.141 seconds with peak private commit 3.440 GiB. A measured-memory
64K follow-up rejects current RAM/commit before loading. A separate measured
32K admission profile loads18.469seconds, completes greetings50.328/38.000s
and the router exhausts16384output tokens after4095.422seconds with no visible
answer despite all7source reads. TS/SQL also ends at5039.500seconds with a
16384-token final-turn output limit, zero visible text in all six turns,
six required files read and eight unavailable extra reads. Both are unscored;
history completes8/8 in3380.750seconds, extended-only and120records, with no
new hardware error. The owned engine is stopped; no complete public total.
[Collection and history review](../reports/2026-10-27-flint-q3xl-file-workflows.json).
[Router receipt](../reports/2026-10-27-flint-q3xl-router-limit.json),
[TS/SQL receipt](../reports/2026-10-27-flint-q3xl-ts-limit.json).
The separate resident1/40K/output32K control passes greetings75/67seconds and
completes the1024-capped router in2268.531seconds. Source review finds an
incorrect empty-dictionary self-test and a claimed read-order mismatch;
isolated execution is pending while8192/native controls continue. No completed
quality score is implied. [Capped-case evidence](../reports/2026-10-27-flint-router-budget1024.json).
The admission
[rejections](../reports/2026-10-26-flint-admission-rejections.json) are retained.
Gemma and Qwen IQ3 weights are exact-file retired at 23:25 IST after full hashes,
recovering 26.19 GiB. All evidence remains; selected Qwen Q4 and Flint/K2 weights
are preserved. [Retirement receipt](../reports/2026-10-26-reviewed-weight-retirement.json).

3 November: run C grading is complete. In the extended cohort, the 1024-capped
router scores 38/40 (26 non-code + 12 behavior; 2268.531 s) and the 8192-capped
router 37/40 (25 + 12; 5438.078 s). Both pass all six frozen behavior groups in
WSL bubblewrap, and each answer's own tests contain one wrong assertion (6/7).
The one-point gap lies within reviewer judgment, so the 8192 cap adds 2.4 times
the time for no measured gain. Native 32K-output reasoning is unscored: the RAM
guard stopped the server at 6136.2 s after outside desktop memory growth, with
no visible text and no hardware event. These are extended-diagnostic router
scores only, not frozen-cohort or full-public results; Flint stays unpromoted.
[Run C grades](../reports/2026-11-03-flint-runC-grades.json).

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
| Gemma 4 26B-A4B QAT Q4_0 | 19 | Separate historical cases | Not comparable | Historical lower-memory fallback; private 400 s. Exact weights retired26October after the expanded tests below |
| Gemma 4 26B-A4B QAT, CPU28/resident8,24October |Unrun on new profile |Router38/40; TS5/6; SQL0/6; history incomplete |Unrun on new profile |Router1031.860s,TS/SQL1142.469s. Python groups6/6 andself-tests8/8 pass; TS prototype validation and SQLite FK error remain. History4096-token reasoning-only limit789.282s; no full total |
| Gemma 4 26B-A4B QAT, CPU26/resident8 |23 |57 |Unrun; current capacity rejection |Private798.6s: semantics15/citations2/code6. Public uses topK64; private explicitly20. Conflicting fact ownership, unread citations and missed closeout remain despite correct merge. Public skips linked TS/SQL rule; prototype-validation/self-test defects. No full composite or promotion |
| Gemma 4 26B-A4B QAT, CPU28/resident4, extended64K |Unrun |Unrun |Two completed frozen passes; partial suite |Intervals105/105 in1105.766s; TTL34/34 in964.140s. Separate NaN TTL fails. Intentional stop interrupts DAG; nine later cases unrun. No hardware event |
| Gemma 4 26B-A4B QAT, CPU28/resident6, extended64K |Unrun |Unrun |10/12 frozen passes; all12 complete |CSV104/120, TS syntax/compile failure; separate NaN TTL and synchronous worker-failure defects. Merge extra passes. Median710.843s; CSV2135.172s. Greetings10.891/6.656s; no hardware event or transferred workflow scores |
| Gemma 4 26B-A4B QAT, CPU30/cache448/resident5, extended128K |Unrun |Large history interrupted, unscored |Unrun on this profile |Commit guard after 3637.469 s; 56% of long input processed, no phase answer. Plain greetings24.406/11.172 s. No new hardware event; changed desktop commit is recorded |
| Gemma 4 31B dense QAT Q4_0 | 26 | Historical completed cases | Not comparable | Private 7234 s; fails current latency gate; retired |
| Qwen3-Coder-Next 80B Q4 | Unscored | Separate historical cases | Not comparable | Private tool-loop limit after 4075 s; retired |
| Qwen3-Coder-30B UD-Q4_K_XL | Deadline | Separate historical cases | Not comparable | Public cases complete, private 1200 s deadline |
| Kimi-Linear 48B Q4 | Capacity rejection | Separate historical cases | Not comparable | Not evidence of poor answer quality; retired |
| Qwen3.8 27B dense Q6 / TQ3 | Unscored | Interrupted | Not collected | Roughly 1.4-2.1 decode tok/s; long requests/restart, not promoted |
| Qwen3.8-Flash-Next 125B, Strata IQ3_XXS | Not completed | Coding deadlines; empty history final | Not collected | Separate replays recover facts; not a retroactive workflow pass; retired |
| Qwen3.8-Flash-Next GSQ-RCO Q2_0, Strata0.1.50 |Not run |Not run |Not run |New engine staged and verified, source frontend pinned; Q2 shards not yet downloaded. Requires61.86GiB plus packing/headroom; volume has about60.58GiB free after reviewed retirement. Complete current candidates before more exact-file retirement. Smaller quant is a capacity control, not an assumed quality upgrade |
| Bonsai 2 27B PQ2_0 | Not run | Stopped | Not run | Partial CPU placement only 2.3 tok/s; retired |
| Bonsai 2 27B PTQ1_0 | Not run | Deadline | Not run | Full GPU, router exceeds 1200 s after one tool turn; retired |
| LFM2.5 24B-A2B QAD Q4_0 | Deadline | 48 | 6 completed passes of 12 | Private reasoning loop; coding includes deadline/truncation, so 6/12 is task completion, not twelve completed correctness grades; retired 23 October |
| Qwen3.6 UD-IQ4_XS | Not run | Router 39/40 only | Not run | TS/SQL interrupted by RAM guard; not a complete public score |
| Qwen3.6 UD-IQ4_XS, CPU34 placement, 21 October | Not run | Not run | Not run | Loaded in 5.72 s; about 1.25 GiB of weights moved from CPU to GPU. Commit floor stop at 23.7 s during the first smoke; no answer. Placement evidence only |
| Qwen3.6 UD-IQ3_S, CPU34, 21 October | Not run | Router interrupted | Not run | Load test decoded at 12.01 tok/s with 1.9 GiB VRAM free. Run a was capacity-rejected. Run b read all 7 files, produced reasoning only, and stopped at 382.7 s on an nvidia-smi read failure (fail-closed; lowest VRAM 1,152 MiB). Unscored |
| Qwen3.6 Q4 core-0 baseline, 20 October | Not run | RAM floor stop | Not run | Owner-approved 5 GiB gates. Working set 19.07 GiB, decode 0.3-0.6 chunks/s, RAM floor at 193.0 s. Paging evidence, not a quality result |
| Strata Qwen Q4, file-backed expert arena (fork c451fbe8), 21 October | Not run | Not run | Not run | 18.23 GiB arena with no commit charge, but engine memory reached 15.98 GiB and the RAM floor (0.364 GiB) tripped at 35.6 s before readiness. Expert pack (b5211998) built, never loaded. [Strata section](tasks/2026-10-18-strata/2026-10-18-strata-on-10gb-v0.6.0.md#windows-expert-arena-experiments-21-october-audited-3-november-2026) |
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
| Recursive Flint UD-Q3_K_XL, CPU49/cache512/resident4/32K |Not run |Not run |Not run |Load21s; plain greetings48.375/31.141s, both complete. Peak private3.440GiB; no hardware/resource stop.64K follow-up prepared;32K greetings are not file-quality or long-context validation |
| Recursive Flint UD-Q3_K_XL, measured32K file-workflow B |Not run |Router/TS output limits; history8/8 extended-only |Not run |History3380.750s,120records; router4095.422s and TS/SQL5039.500s exhaust16384 output tokens with zero visible answer. Required sources delivered;8extra unavailable TS/SQL reads. No full public score; greetings50.328/38.000s. Clean stop/no hardware event. Settings differ from IQ3XXS |
| Recursive Flint UD-Q3_K_XL, resident1/40K/output32K run C (extended cohort) | Not run | Router 38/40 with 1024 cap, 37/40 with 8192 cap (extended-only); native 32K unscored; no TS/SQL/history in C | Not run | 1024 cap 2268.531 s, 8192 cap 5438.078 s; both pass 6/6 frozen behavior groups, one wrong self-test each (6/7). Native RAM-guard stop at 6136.2 s, 11,221 reasoning tokens, no visible text, no hardware event. Not the 1200 s cohort; no full public total |
| Groot-19B-A3B-261023 Q4_K_M (bartowski), apps open, 3 November | Not run | Router interrupted twice (RAM guard); TS/SQL and history not run | Not run | Capacity-limited apps-open; no quality score. Uncapped CPU36 run: smoke READY., RAM guard (0.5 GiB floor) 5.1 s into router prefill at 0.42 GiB available. 3.31 GiB working-set cap plus 512 MiB expert cache (diagnostic): prefill 6.07 tok/s, decode 2.33 tok/s, two correct first reads, then the 2.0 GiB RAM guard at 227.6 s. About 8 GiB of CPU experts do not fit the about 6 GiB apps-open budget; needs an apps-closed window. [Model record](tasks/2026-11-03-groot/2026-11-03-groot-19b-a3b-apps-open-v1.0.md) |

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

### Audit of Claude's 20-21 October runs (3 November)

Every 20-21 October candidate now has a standalone record:
- LFM2.5 and Bonsai 2 have new task folders:
  [LFM2.5 record](tasks/2026-10-20-lfm25/2026-10-20-lfm25-24b-a2b-qad-q4-v0.10.0.md)
  and [Bonsai 2 record](tasks/2026-10-20-bonsai2/2026-10-20-ternary-bonsai2-27b-pq2-ptq1-v0.10.0.md).
- The Qwen attempts are appended to the
  [Qwen record](tasks/2026-10-24-qwen-coverage/2026-10-24-qwen36-v0.9.0.md#2021-october-claude-campaign-runs-audited-3-november-2026).
- The Strata Windows arena work is appended to the
  [Strata report](tasks/2026-10-18-strata/2026-10-18-strata-on-10gb-v0.6.0.md#windows-expert-arena-experiments-21-october-audited-3-november-2026).

The table rows for Bonsai 2 PQ2_0/PTQ1_0, LFM2.5 and Qwen3.6 UD-IQ4_XS keep
their 23 October wording. The new 20-21 October rows (IQ4_XS CPU34 placement,
IQ3_S CPU34, Q4 core-0 baseline and the Strata file arena) sit below the IQ4_XS
row. No score changed. The saved evidence corrects five earlier statements:
1. LFM's private loop ran with request overrides top_k 20, min_p 0 and repeat
   penalty 1.0, not the publisher sampling stated in the private review. Each
   of the three LFM suites used a different sampler.
2. LFM coding was graded automatically in WSL bubblewrap before any source
   review. On review, js_pool's 0/1 comes from a promise that never settles
   and sql_report's 0/20 from one wrong column.
3. LFM's intervals deadline happened while the desktop was paging: about
   4-5 tok/s, against about 23 tok/s on later tasks.
4. The 21 October IQ3_S run b stopped on a telemetry read failure, not on VRAM
   below 400 MiB.
5. Strata's file-backed arena trades commit charge for physical residency. The
   read-only pack is unmeasured.

Bonsai 2 details from the new record: PQ2_0 cannot load on mainline b11669
(ggml type 142). On the Prism fork (b10787, 52/65 GPU layers) it decoded at
2.3-2.7 tok/s and was stopped by hand at about 82 s. PTQ1_0 ran fully on the
GPU with CPU KV at xhigh effort and delivered all 7 router reads in turn 0 at
13.1 tok/s; its visible answer starts at 998 s and is unfinished at 1200.016 s.
Both are unscored and were retired on 21 October. Medium effort and the
stock-llama.cpp Q2_0 file added upstream on 30 October are untested.

Derivations with source hashes are in the ignored
`local-data/2026-11-03-campaign-audit/`.

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
  and its [run C grades](../reports/2026-11-03-flint-runC-grades.json) (3 November)
- [Groot-19B-A3B Q4_K_M apps-open record](tasks/2026-11-03-groot/2026-11-03-groot-19b-a3b-apps-open-v1.0.md) (3 November; capacity-limited, no quality score)
- [LFM2.5 24B-A2B QAD Q4_0 record](tasks/2026-10-20-lfm25/2026-10-20-lfm25-24b-a2b-qad-q4-v0.10.0.md) (Claude campaign, audited 3 November)
- [Ternary Bonsai 2 27B record](tasks/2026-10-20-bonsai2/2026-10-20-ternary-bonsai2-27b-pq2-ptq1-v0.10.0.md) (Claude campaign, audited 3 November)
- [All-model inventory through 17 October](tasks/2026-10-17-complete-model-inventory/2026-10-17-all-models-gemini-and-availability-v0.4.1.md)
- [Matched Q4/Q6 and expanded candidates](tasks/2026-10-16-memory-and-candidate-expansion/2026-10-16-memory-context-and-expanded-model-tests-v0.4.0.md)
- [Strata](tasks/2026-10-18-strata/2026-10-18-strata-on-10gb-v0.6.0.md)
- [TurboQuant](tasks/2026-10-19-azllm/2026-10-19-azllm-and-turboquant-v0.7.0.md)

Private source records reviewed: the 20 October local-LLM campaign v1.0,
local-llm skill evaluation/runtime/hardware/leaderboard references, 21 October
IQ3_S attempt/stop receipts and Claude's current catalog/profile changes.
Private instructions and raw answers are intentionally not copied here.
