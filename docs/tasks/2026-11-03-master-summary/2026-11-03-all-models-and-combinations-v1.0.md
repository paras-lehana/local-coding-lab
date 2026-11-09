# All models, combinations and tuning on an RTX 3080 10 GB (12 October to 3 November 2026)

**9 November reconciliation:** this is the preserved historical configuration
inventory. Use [the current merged report](../2026-11-09-merged-research/2026-11-09-merged-models-articles-and-experiments-v0.11.0.md)
and [individual model index](../../models.md) for newer state. Q2 download and
packing completed3Nov; six b12069 tiny-model controls now pass. The private
Flint72K/cap1024 trial is new, not a completion of an old interrupted prompt.
Groot's “apps closed” suggestion is not owner authorization to close apps.
Qwen's lack of full re-prefill refers to the224 audited continuation turns;
0.057% is estimated lost time divided by prefill plus decode. Larger context
and a saved ready flag do not establish actual recall or a live endpoint.

Additional source correction: QN80-1's "capacity-rejected" means operationally
rejected after a completed smoke with excessive shared-memory spill, not a
pre-load rejection/OOM. Original IQ3_M identity and both 28/10-layer smoke
timings are recovered in the [model record](../2026-11-09-qwen3-next80-instruct/2026-11-09-qwen3-next80-instruct-v0.11.0.md).
The older rows below remain preserved.

Two additional wording limits apply throughout this historical record.
"Every CUDA allocation" overstates the WDDM observation: sampled allocation
phases showed roughly matching device-memory and system-commit changes;
this is not a universal allocation identity. Likewise, an apps-open failure
describes the measured profile and available resources at that time, not a
permanent exclusion of a model. The9November work uses fresh admission and
explicitly different bounded profiles; it does not relax the stop floors or
retroactively award those earlier runs a pass.


3 November 2026, compiled 21:00-21:30 IST by Claude from saved lab evidence. This
is a read-only consolidation: no engine was started or stopped for it and no
score was changed. It rests on a reconciliation of 144 rows (as of 20:51 IST) in
which both sources were opened for every conflict (section 2.2). Two rows were
added and three updated in place after 20:51 (section 2.1, intro).

**Status: no candidate has complete, compatible private, public and coding scores,
so there is no full-composite leader.** On the components that exist, Qwen3.6-35B-A3B
UD-Q4_K_M in the mapped64 profile remains the reference: 31/36 private and 52/60
public, with the coding suite never collected on that profile. It does not fit
while the owner's applications are open, and the production endpoint built on the
same weights has been off since 24 October 13:23.

## How to read this document

**Scales** (lab [model-reporting.md](../../model-reporting.md) and the private
local-llm evaluation reference):
- Private /36: frozen instruction-chain audit (24 meaning + 6 citation + 6 isolated
  code). Weight 0.5.
- Public /60: router 40 + history 8 + strict TypeScript 6 + SQLite 6. Weight 0.3.
- Coding /12: twelve frozen executable tasks, graded in WSL bubblewrap. Weight 0.2.
- A composite exists only when all three suites are complete and compatible. The
  leaderboard's "partial composite" renormalises the components a run has, so it
  is not comparable with a full composite.

**Labels**
- "old" (15-17 Oct public format): router-v1 groups out of 6 per seed, TS /6,
  SQLite /6, history pass/fail. "old40" (18 Oct): router /40, history facts /6, TS
  and SQLite /6. Neither converts to /60; only Q36-22 was regraded to /60.
- "part": a graded sub-score; it never fills a /60.
- "compl N/12": a coding completion count (unfinished tasks count as not
  completed); never a score and never in a composite.
- "diff-scale": a non-campaign rubric.
- R/H/T/S: router, history, TypeScript, SQLite.
- "LB rank" and composites come from the private skill leaderboard
  (0.5 private + 0.3 public + 0.2 coding, partial values renormalised).

**Cohorts**
- frozen-1200: every scored prompt finishes within 1200 s, including prefill,
  reasoning and all tool turns. The only rankable cohort. Runs from 16 October that
  used a 21,600 s runner stay here as over-deadline.
- extended: the owner's 26 October policy for longer accurate coding; its own
  allowance; never ranked. A plain greeting still has a 600 s ceiling.
- diagnostic: capped, cached or otherwise changed controls; never ranked.

Publisher claims are labelled as such. Everything else is a local measurement
unless it is marked as an estimate or inference. Times are IST; the year is 2026.

**Path abbreviations used in source columns**

| Abbreviation | Location | Where |
|---|---|---|
| RPT | `reports/` | this repository |
| LT | `docs/tasks/` | this repository |
| LD | `local-data/` | ignored raw evidence, not published |
| CAMP | `reports/2026-10-15-campaign.md` | this repository |
| PRIV | `reports/2026-10-15-private-results.json` | this repository |
| STR | `LT/2026-10-18-strata/2026-10-18-strata-on-10gb-v0.6.0.md` | this repository |
| EXP | `LT/2026-10-16-memory-and-candidate-expansion/2026-10-16-memory-context-and-expanded-model-tests-v0.4.0.md` | this repository |
| QWR | `LT/2026-10-24-qwen-coverage/2026-10-24-qwen36-v0.9.0.md` | this repository |
| FLR | `LT/2026-10-23-flint/2026-10-23-recursive-flint-v0.8.0.md` | this repository |
| GMR | `LT/2026-10-24-gemma26-coverage/2026-10-24-gemma26-v0.9.0.md` | this repository |
| DR | `LT/2026-11-03-deep-research/2026-11-03-deep-research-v1.0.md` | this repository |
| RPA | `RPT/2026-11-03-reprefill-audit.json` | this repository |
| BEN | `E:/llm/benchmarks/` | private parent installation |
| RUNS | `BEN/2026-10-13-instructions/runs/` | private |
| DT | `E:/llm/docs/tasks/` | private parent task logs |
| RB | `DT/2026-11-03-campaign-recovery/2026-11-03-recovery-brief-v1.0.md` | private |
| SKL | `E:/llm/.claude/skills/local-llm/` | private skill and scorecard |
| LB | `SKL/reference/leaderboard.json` and `leaderboard.md` (64 runs at 20:51:35) | private |
| INSTALL | `E:/llm/install-log.txt` | private |
| MIG | `E:/llm/migrations/` | private |
| QUEUE | `LD/2026-11-03-queue/queue-README.md` | ignored |

## Live state at 21:15 IST, 3 November

- **No engine is loaded.** Nothing listens on port 8080 or 8081 (netstat at 21:07)
  and no llama-server or Strata process runs; Ollama is idle. The two Groot trials
  ended at 20:33:46 and 20:39:37, so the "timed Groot benchmark" in this task's
  brief had already finished.
- **Production is off** since 24 October 13:23; `server-settings.json` still says
  "ready", which is stale (RB section 4).
- **Flash-Next GSQ-RCO Q2_0 is downloaded and packed, never loaded.** Shard 1 was
  SHA256-verified at 20:14:39 and shard 2 at 21:07:07. The native pack was built at
  21:10 in 9.3 s: 1,495,796,923 bytes, 0 conversions, and a packed chat template
  identical to the 18 October IQ3 pack. ([pack receipt](../../../reports/2026-11-03-flash-next-q2-pack.json))
- **llama.cpp b12069:** the release archives are downloaded, and a side build with
  the lab's prefetch opt-out linked `llama.dll` at 21:10 (`C:/llm-staging/build`).
  No load, identity or speed test has run.
- **Strata fork:** `build-gpu/strata-q36.exe` was rebuilt at 21:00 for the 3 November
  free-VRAM commits (section 4.4).
- **Another workflow step is downloading small models** for an apps-open arm:
  Dory-4B Q5_K_M (43% at about 21:08, after two HTTP 404 failures at 20:48), then
  Qwen3.5-9B Q5 and Q4. Nothing has loaded.
- **The re-prefill log audit finished at 21:08** ([RPA](../../../reports/2026-11-03-reprefill-audit.json); section 6.3).
- **Memory:** 11.3-13.7 GiB RAM and 10.9-11.9 GiB commit available between 21:08
  and 21:10 (b12069 build memory log); 10.7 GiB minimum during the pack step.
  Earlier today it was as low as 2.2 GiB RAM (18:50). VRAM free was about 6.8 GiB
  at 21:08 (QUEUE).
- **Disk:** E: has 6.9 GB free after the pack (6,888,914,944 bytes); C: has 58 GB.
- **Leaderboard:** 64 runs: 8 ranked, 28 frozen but not ranked, 8 extended, 7
  diagnostic, 13 not loaded.

## 1. Executive summary

### 1.1 Best result per cohort

| Cohort | Best measured result | Why it leads | What it lacks |
|---|---|---|---|
| frozen-1200 (rankable; 8 scored runs) | **Qwen3.6-35B-A3B UD-Q4_K_M, mapped64** (Q36-22): private 31/36 (20/5/6), public 52/60 (R39 H8 T5 S0); partial composite 86.3, rank 1 | Highest private score (tied with Q36-05 and its byte-identical replay Q36-17) and the only scored run with a /60. Every task finished within 724.1 s | Coding suite never collected. SQLite 0/6 (foreign-key failure) and TS 5/6. One seed. Production uses a different, unscored profile |
| extended (never ranked) | Gemma 4 26B-A4B QAT, CPU28/resident6 (G26-9): coding 10/12, median 710.8 s, suite 9,076 s | The only complete suite score in this cohort | No public or private run on that profile; weights retired 26 Oct |
| diagnostic (never ranked) | Qwen3.6 UD-IQ3_S with a 4096-token reasoning cap and a 1536 MiB expert cache (Q36-44): coding 6/12, all 12 finished, median 133.9 s | The only complete diagnostic suite | A capped variant; weights retired |
| Strongest unscored components | Gemma CPU26 57/60 + 23/36 (G26-7; top-k differs between suites). IQ4_XS 55/60 + 29/36 (Q36-47). IQ3_S 52/60 + 29/36 (Q36-42). Flint IQ3_XXS 29/36 + R 39/40 + 11 completed passes of 12 (FLT-04) | – | Each misses a suite or a completion gate; none combines into a composite |

**Recommendation.** Keep Qwen3.6-35B-A3B UD-Q4_K_M as the reference and production
model. The most useful next measurement is its missing coding suite on the mapped64
profile (section 7). No other candidate has shown a measured reason to replace it.

### 1.2 What fits with the applications open

The budget moved a lot within one evening:

| Time (3 Nov) | Available RAM | Commit available | VRAM free | Source |
|---|---|---|---|---|
| 18:50 | 2.2 GiB | about 4.1 GiB | 5,839 MiB | RB section 4 |
| 20:40, owner working | 6.0-6.5 GiB | 8.5-11.7 GiB | about 6 GiB | SKL/reference/runtime.md |
| 20:59-21:08 | 8.8-13.6 GiB | 10.9-11.9 GiB | about 6.8 GiB | QUEUE |
| 21:08-21:10 | 11.3-13.7 GiB | 10.9-11.9 GiB | not logged | b12069 build memory log |

| Profile | Gates (RAM GiB / commit GiB / VRAM MiB) | At about 6 GiB (20:40) | At 13.6 GiB (21:08) |
|---|---|---|---|
| Production Qwen Q4, 128K CPU KV | 18 / 12 / 6,000 | no | no |
| Qwen Q4 mapped64 (the leader) | 16 / 10 / 6,000-6,500 | no | no |
| Qwen Q4 + 0.8B draft (proposed) | 17 / 10 / 6,500 | no | no |
| Groot Q4, apps-closed estimate | at least 14 / 8 / 5,500 | no (measured failure) | just short |
| Flint Q3_K_XL private72K | 7.5-10.5 / 8.5 / 5,500-6,000 | no | yes (queue dry run) |
| Strata expert pack on Qwen Q4 | 10 / 10 / 6,400 | no | yes (queue dry run) |
| Flash-Next Q2_0 mmap32 (provisional) | 12 / 14 / 7,000 | no | no |

Sources: `profiles/*.json`, the Groot record, QUEUE and the Q2 pack receipt.

- **Rule of thumb** (SKL/reference/runtime.md): with apps open, a model's
  CPU-resident part must fit within about available RAM minus the stop floor minus
  1 GiB. At 6 GiB available that leaves about 2.5-3 GiB.
- **GPU placement does not escape the limit.** Every CUDA allocation is also
  charged to Windows commit at about its own size (section 5.3).
- **Nothing installed today completes the frozen suites at the 6 GiB end.** Groot Q4
  failed both ways: about 8 GiB of its experts sit on the CPU (GRT-1, GRT-2).
- **Earlier apps-open completions used files that are now retired.** IQ3_S CPU38 and
  IQ4_XS with a 13.356 GiB cap both finished public and private collection on
  24 October; both files have since been retired.

### 1.3 What the evidence shows

1. **The profile moves scores as much as the quant does.** With the same Q4 file,
   seed 73 and temperature 0.6, the private audit scored 25, 27, 31 and 31 on
   different placements and batches. A reproduced profile gave a byte-identical
   answer (Q36-15, Q36-16, Q36-05/17, Q36-22). So a single-run gap of 3 points is
   not evidence of a precision effect (section 3.3).
2. **More bits did not help consistently.**
   - On the matched CPU35 profile, Q5 scored 28 against Q4's 25 (Q36-18, Q36-15).
   - On the matched mapped CPU37 profile, Q6_K_XL scored 28 against Q4's 31, took
     2,099.7 s and was over the deadline (Q36-23).
   - IQ4_XS and IQ3_S each scored 29/36.
3. **Temperature 0.6 beat 1.0** on the same configuration: 31 against 26 (Q36-05,
   Q36-04).
4. **Keep non-expert layers and the KV cache on the GPU.**
   - All non-expert layers on the GPU with experts on the CPU ran the router in
     204.9 s, against 576.5 s with 30 GPU layers (Q36-07).
   - CPU KV was about 1.9 times slower than GPU KV: 407.9 against 212.8 s (Q36-12).
   - Flint finished its router only with GPU KV (FLT-04 against FLT-02 and FLT-03).
5. **A GPU expert cache raised decode speed** from 22.78 to 39.18 to 46.71 tok/s at
   0, 1536 and 3072 MiB on the all-experts-CPU profile (Q36-12). It costs VRAM and
   commit, and its hit rate has never been measured. Its only private run scored
   27/36, on a different placement (Q36-16).
6. **Working-set caps let big files load with apps open, but mostly turn the RAM
   shortfall into paging:** Groot 2.33 tok/s (GRT-2), Flint Q3_K_XL about 2.1 tok/s
   (FLT-16, FLT-17), Qwen Q4 resident7 6.69 tok/s (Q36-50).
7. **Reasoning caps change completion, not proven quality.**
   - Flint with a 1024 cap scored router 38/40 in 2,268.5 s; with an 8192 cap,
     37/40 in 5,438.1 s (extended).
   - IQ3_S with a 4096 cap finished all 12 coding tasks but passed 6 (Q36-44).
8. **Strata ran the same Q4 weights 1.14-1.76 times faster** on three 32K workflows,
   one sample each. It failed the SQLite migration and needed about 25 GiB of free
   RAM (Q36-31 against Q36-32).
9. **Re-prefill is not what makes Qwen3.6 slow** in the lab workflows: 19.4 s lost
   across 224 continuation turns. Editor traffic lost 578 s in four events (section
   6.3).
10. **Two Windows memory facts shape every profile.**
    - CUDA allocations charge commit about 1:1: median 1.038 over 67 loads (ENG-1).
    - `cudaMemGetInfo` ignores other processes' VRAM (ENG-2). Engines that size
      buffers from it can overcommit the desktop's GPU.
11. **Hardware or power events interrupted runs** on 12, 15 and 19 October (QN80-2,
    Q38-2, GLM-4 attempt 2, Q38-12). None has occurred since the 23 October 00:14
    boot (QUEUE check at 20:42).

### 1.4 Coverage

- **Section 2 has 146 rows:** 135 model rows across 16 families, 5 engine or host
  diagnostics and 6 routes not run.
- **14 families were loaded at least once.** K2 Horizon MoVA and Nemotron Bolt never
  loaded.
- **26 distinct weight files loaded at least once.** Four more were downloaded but
  never loaded: K2 Q4_K_M, Nemotron Bolt (since deleted), Flash-Next Q2_0 and the
  Qwen3.5-0.8B draft. Flint NVFP4 and two dense Qwen3.8-27B quants are pinned as
  metadata only. These counts come from section 2.
- **Engines:** seven llama.cpp variants and two Strata builds ran; Strata engine
  0.1.50 and llama.cpp b12069 are staged but have never loaded a model.

## 2. Every model tried

Model families A-Z, then date; non-model rows last. "LB id" is the leaderboard run
id; "—" means the row has no leaderboard entry (76 of the 144 reconciled rows; three
more, QFN-3, QFN-5 and QFN-6, appear only in another row's notes). Rows QFN-9, Q36-57
and NR-5 were updated after 20:51 with the live state; ENG-4 and ENG-5 are new.
FLT-04's sources are corrected to the actual file names.

### 2.1 Master table

#### Bonsai 2 27B, ternary

| ID | Date | Quant · engine · profile | Cohort | Status | Priv /36 | Public | Coding | Wall s | Notes | LB id | Source |
|---|---|---|---|---|---|---|---|---|---|---|---|
| BON-1 | 10-20 | PQ2_0 (7,206,168,928 B) · llama b11669 mainline · gpu-layers 52 | frozen | not run: load failure (ggml type 142) | – | – | – | 13 (trial span) | no inference | — | LD/2026-10-20-campaign/bonsai2-pq2-gpu52-20261020-record.json; LT/2026-10-20-bonsai2/2026-10-20-ternary-bonsai2-27b-pq2-ptq1-v0.10.0.md L10 |
| BON-2 | 10-20 | PQ2_0 · Prism b10787 · 52/65 offloaded (12 of 64 blocks on CPU), CPU q8 KV 64K, b512/u128, 4/8 threads, core 0 excluded, xhigh, temp 1.0 | frozen | interrupted (manual stop) | – | none | – | 82.391 | decode 2.3-2.7 tok/s | bonsai2-pq2-prism-20261020 (LB wall 120; K3) | LD/2026-10-20-campaign/bonsai2-pq2-prism-20261020-public/core-seed73/result.json; server.log |
| BON-3 | 10-20 23:40 to 10-21 00:00 | PTQ1_0 (5,946,648,928 B) · Prism b10787 · -ngl 99 (65/65), CPU q8 KV 64K, b512/u64, xhigh | frozen | over-deadline (router; 6,622-character partial answer) | – | none | – | 1200.016 | decode 13.1, prefill 340 tok/s | bonsai2-ptq1-prism-20261021 | LD/2026-10-20-campaign/bonsai2-ptq1-prism-20261020-record.json; -public/core-seed73/result.json |

#### Gemma 4 26B-A4B QAT Q4_0 (14,439,363,584 B)

| ID | Date | Quant · engine · profile | Cohort | Status | Priv /36 | Public | Coding | Wall s | Notes | LB id | Source |
|---|---|---|---|---|---|---|---|---|---|---|---|
| G26-1 | 10-15 | b11562 · 32K, first 24 expert blocks on CPU, q8 KV; seeds 73/74/75 with a 2048 cap, plus unrestricted and temp 1.0 runs | frozen | public old scale | – | old: core 6/6 ×3; unrestricted 6/6 (588.4 s); t1.0 6/6 (510.7 s); H-120 pass (247.1 s); TS compile fail + S FK fail (347.1 s) | – | 247-588 | 15.2-16.4 tok/s | — | CAMP (Gemma 26B QAT) |
| G26-2 | 10-15 | 64K, n-cpu-moe 24, b128/u32, top-k 20, reasoning cap 2048 | frozen | scored | 19 (14/3/2) | – | – | 398.906 | capped twin of G26-3 | — | PRIV gemma26-private-2048 |
| G26-3 | 10-15 | same, native (budget -1) | frozen | scored; LB rank 8 (52.8) | 19 (14/3/2) | – | – | 400.234 | 16.34 tok/s | h-gemma26-qat-20261015 | PRIV gemma26-private-unrestricted |
| G26-4 | 10-15 | 64K public, unrestricted, KV 813 MiB | frozen | public old scale | – | old: H-320 count 318, fail (467.0 s); H-640 pass (631.6 s); T 5/6 + S 6/6 (455.7 s) | – | 455-632 | the only SQLite 6/6 of 15-17 Oct | — | CAMP |
| G26-5 | 10-24 | b11562-noprefetch · CPU24 | frozen | capacity-rejected (VRAM 6313 < 6400 MiB) | – | – | – | – | – | gemma26-cpu24-rejected-20261024 | LB; GMR |
| G26-6 | 10-24 | CPU28, resident8, 64K GPU q8, b128/u32, temp 0.6, top-k 20 | frozen | unscored (history incomplete) | – | parts: R 38/40 (1031.9 s), T 5/6, S 0/6 FK (1142.469 s) | – | 1142.469 | history hit a 4096-token reasoning-only limit | gemma26-resident8-public-20261024 | RPT/2026-10-24-gemma26-resident8-public.json, -grades.json |
| G26-7 | 10-25 | CPU26, resident8, temp 1.0; public top-k 64, private top-k 20 | frozen | unscored (coding unrun) | 23 (15/2/6) | 57/60 (R38 H8 T5 S6) | unrun | 798.6 | samplers differ between suites | gemma26-cpu26-publisher-public-20261025 | RPT/2026-10-25-gemma26-cpu26-public.json, -private.json, -grades.json |
| G26-8 | 10-26 | CPU28, resident4, extended64 | extended | interrupted (deliberate) | – | – | compl 2/12 (intervals 105/105, TTL 34/34) | 1105.766 | separate NaN-TTL diagnostic fails | gemma26-cpu28-resident4-extended64-20261026 | RPT/2026-10-26-gemma-resident4-calibration.json |
| G26-9 | 10-26 | CPU28, resident6, extended64, predict 32768 | extended | scored (never ranked) | – | – | **10/12** (452/470 checks) | 710.843 median; suite 9076.1 | 29% faster than resident4 with identical tokens | gemma26-cpu28-resident6-extended64-20261026 | RPT/2026-10-26-gemma-resident6-coding.json; RPT/2026-10-26-gemma-residency-pair.json |
| G26-10 | 10-26 | 128K plans: first plan (12.5 GiB / 5700 MiB gates), cpu30-resident4 (10.5 GiB), cpu30-cache448-resident2p5 (5450 MiB) | extended | capacity-rejected ×3 | – | – | – | – | free 9.543 GiB / 5383 MiB; 9.326 GiB; 5415 MiB | — | RPT/2026-10-26-gemma128-calibrations.json |
| G26-11 | 10-26 | 128K cpu30-resident2p5 b128/u32; cpu30-cache448-resident2p5 b64/u16 | extended | interrupted ×2 (calibration) | – | – | – | – | prefill 7.15 tok/s uncached against 5.03 with a 448 MiB cache | — | same; RPT/2026-10-26-gemma128-cache-calibration.json |
| G26-12 | 10-26 | run G: cpu30, cache448, resident5, 128K, b64/u16, 640-record history | extended | interrupted (commit floor; 0.928 GiB) | – | none (56% of the input processed) | – | 3637.469 | prefill 8.17 tok/s | gemma26-cpu30-cache448-resident5-128k-history-20261026 | RPT/2026-10-26-gemma128-history-resource-stop.json |

#### Gemma 4 31B dense QAT Q4_0 (17,651,001,568 B)

| ID | Date | Quant · engine · profile | Cohort | Status | Priv /36 | Public | Coding | Wall s | Notes | LB id | Source |
|---|---|---|---|---|---|---|---|---|---|---|---|
| G31-1 | 10-15 | b11562 · 16K, FFNs on CPU: (a) GPU KV, (b) CPU KV | diagnostic (300 s) | (a) resource stop at 223 MiB VRAM; (b) deadline at 259 tokens | – | – | – | 300.016 | 0.95 tok/s | — | CAMP (Gemma dense placement probes) |
| G31-2 | 10-16 | b11562-noprefetch · mapped, 64K CPU q8 KV (3251 MiB), 8/8 threads, b128/u32, temp 1.0 | frozen (21,600 s runner; K6) | over-deadline | 26 (16/4/6) | old: Python 6/6 (3944.6 s); T 5/6 + S FK (4463.0 s); ~10K H pass (2029.0 s) | – | 7234.171 | 1.17 tok/s | h-gemma31-dense-20261016 | RPT/2026-10-16-gemma31.json; RUNS/expansion-20261016-gemma31-publisher64/outcome.json |
| G31-3 | 10-16 | 32K placements: (a) FFN on CPU, (b) last 14 blocks on GPU, (c) b + GPU KV | diagnostic | (a)(b) done; (c) VRAM-floor stop (394 MiB) | – | 2K-token: 160.5 / 146.0 / 146.1 s; 8K-token: 457.6 / 462.2 s | – | ≤ 462 | faster decode did not shorten the workflow | — | RPT/2026-10-16-dense-placement.json |

#### GLM-4.7-Flash

| ID | Date | Quant · engine · profile | Cohort | Status | Priv /36 | Public | Coding | Wall s | Notes | LB id | Source |
|---|---|---|---|---|---|---|---|---|---|---|---|
| GLM-1 | 10-15 | UD-Q4_K_XL (16.317 GiB) · b11562 · 32K q8 MLA KV, cap 2048, temp 0.6; plus unrestricted and temp 0.7 runs | frozen | public old scale | – | old: core 1/6, 5/6, 2/6; unrestricted used 16,384 reasoning tokens with no answer (988.6 s); t0.7 5/6 (334.641 s); H-120 pass; TS compile fail; S 4/6 after a grader fix (total data loss) | – | – | temp 0.7 comes from the plan file (K18) | — | CAMP; LD/2026-10-15-campaign/glm-thinking-tasks.json |
| GLM-2 | 10-15 | UD-Q4_K_XL, q8 KV · private 64K, n-cpu-moe 41, b128/u32, cap 2048 | frozen | scored | 21 (15/2/4) | – | – | 530.203 | 16.32 tok/s | — | PRIV glm47-q4-private-2048 |
| GLM-3 | 10-15 | UD-Q4_K_XL, f16 KV · public 32K CPU40; private 64K, n-cpu-moe 44, native | frozen | scored; LB rank 5 (75.0) | 27 (19/4/4) | old: capped core 5/6, native 6/6; H-120 READY count 243, fail | – | 942.0 | all 15 sources read | h-glm47-q4f16-20261015 | PRIV glm47-q4-f16-private-unrestricted; CAMP |
| GLM-4 | 10-15 | Q5_K_M (19.939 GiB) · private 64K, n-cpu-moe 42, cap 2048 | frozen | scored on attempt 3 (attempt 1 capacity-rejected at 21.72 < 22 GiB; attempt 2 lost to the unclean shutdown) | 21 (16/3/2) | old: capped core 5/6, 0/6, 0/6; t0.7 5/6 (338.719 s); unrestricted 6/6, 6/6, 0/6; TS 4/6 + S FK; native TS fail + S 5/6 (data loss) | – | 750.391 | claims 4 unread files | — (only "Q5 21" in the h-glm47-q4f16 notes) | PRIV glm47-q5-private-2048-3; CAMP L440-447 |
| GLM-5 | 10-15 | UD-Q6_K_XL (26,175,238,496 B) · private 64K, n-cpu-moe 44, native | frozen | scored; LB rank 7 (66.7) | 24 (17/2/5) | old: core 5/6, 0/6, 6/6; unrestricted 5/6; TS compile fail; S 5/6 (loses jobs and events) | – | 870.297 | public minimum VRAM 463 MiB | h-glm47-q6-20261015 | PRIV glm47-q6-private-unrestricted |

#### Groot-19B-A3B-261023 Q4_K_M (12,484,339,584 B, sha c941e12a, rev 0025df0d)

| ID | Date | Quant · engine · profile | Cohort | Status | Priv /36 | Public | Coding | Wall s | Notes | LB id | Source |
|---|---|---|---|---|---|---|---|---|---|---|---|
| GRT-1 | 11-03 20:33 | b11562-noprefetch · moe36-mmap64: gpu-layers all, n-cpu-moe 36, 64K q8, b512/u128, core 0 excluded, temp 0.6, floor 0.5 GiB, no cap | frozen | interrupted (RAM floor; minimum 0.419 GiB) | – | none | – | 5.125 | smoke READY. in 4.813 s; working set 7.82 GiB and rising | groot-q4-20261103 | LD/2026-11-03-campaign/groot-q4-20261103-record.json, -public/; LT/2026-11-03-groot/2026-11-03-groot-19b-a3b-apps-open-v1.0.md |
| GRT-2 | 11-03 20:35-20:39:37 | + 512 MiB GPU expert cache, 3.31 GiB working-set cap, b128/u32, floor 2.0 GiB | diagnostic (LB; K10) | interrupted (RAM floor; 1.946 GiB) | – | none (2 of 7 sources read) | – | 227.641 | prefill 6.07, decode 2.33 tok/s; about 27.1M page faults | groot-q4-resident4-20261103 | LD/2026-11-03-campaign/groot-q4-resident4-20261103-record.json, -public/ |

#### K2 Horizon MoVA 36B-A4B (IFM)

| ID | Date | Quant · engine · profile | Cohort | Status | Priv /36 | Public | Coding | Wall s | Notes | LB id | Source |
|---|---|---|---|---|---|---|---|---|---|---|---|
| K2-1 | 10-24 to 10-26; parked 11-03 19:03 | Q4_K_M (22,368,011,616 B) · b11838-noprefetch planned · cpu48-vcpu-kvq4-64k (18 GiB), resident8 (14.5), resident4-ext32 (10.5), resident6-ext32 (12.5) | frozen (planned) | capacity-rejected; never loaded | – | – | – | – | now in `C:/llm-staging/parked`; any load needs a fresh full SHA256 after the move back | k2-mova-q4-never-loaded | LT/2026-10-24-k2-mova/2026-10-24-k2-mova-v0.9.0.md; RPT/2026-10-26-resume-capacity.json; DT/2026-11-03-campaign-recovery/k2-parked-on-c.json |

#### Kimi-Linear-48B-A3B Q4_K_M (30,061,058,720 B)

| ID | Date | Quant · engine · profile | Cohort | Status | Priv /36 | Public | Coding | Wall s | Notes | LB id | Source |
|---|---|---|---|---|---|---|---|---|---|---|---|
| KIM-1 | 10-15 | b11562 · 32K, 23 CPU-MoE blocks; q8 K/V rejected (head dim 72); q8 K + f16 V rejected; f16 K/V loaded | frozen | public old scale | – | old: core s73 4/6 (94.7 s), s74 malformed tool call (unscored), s75 6/6 (111.4 s); H count 242, fail; T 4/6 + S unsupported syntax (92.3 s) | – | 92-236 | 7.09 GiB VRAM | — (the LB row holds only the rejection) | CAMP (Kimi sections) |
| KIM-2 | 10-15 | 64K private | frozen | capacity-rejected (26.893 < 27.5 GiB) | – | – | – | – | – | h-kimi-linear-20261015 | CAMP |

#### LFM2.5-24B-A2B QAD Q4_0 (13,578,190,880 B)

| ID | Date | Quant · engine · profile | Cohort | Status | Priv /36 | Public | Coding | Wall s | Notes | LB id | Source |
|---|---|---|---|---|---|---|---|---|---|---|---|
| LFM-1 | 10-20 | b11669 · n-cpu-moe 28, 64K q8 GPU, b512/u128, core 0 excluded, temp 0.1, a different sampler per suite | frozen | over-deadline (private reasoning loop) | deadline | 48/60 (R37 in 627.125 s, H7 in 439.157 s, T4 + S0 in 538.218 s) | compl 6/12 | 1200.016 | – | lfm25-qad-q4-20261020 (no parts stored) | LT/2026-10-20-lfm25/2026-10-20-lfm25-24b-a2b-qad-q4-v0.10.0.md L10-L132 |

#### Nemotron 3.5 Bolt 74B-A9B

| ID | Date | Quant · engine · profile | Cohort | Status | Priv /36 | Public | Coding | Wall s | Notes | LB id | Source |
|---|---|---|---|---|---|---|---|---|---|---|---|
| NEM-1 | 10-24 | QAD low-bit (22,018,326,528 B) · b11669 planned · bolt-cpu88-coverage64 (18 GiB gate) | frozen | not run; file deleted 24 Oct 13:51 for disk space (not a quality decision) | – | – | – | – | – | nemotron-bolt-74b-not-run | RPT/2026-10-24-bolt-disk-rotation.json |

#### Qwen3-Coder-30B-A3B UD-Q4_K_XL (16.452 GiB)

| ID | Date | Quant · engine · profile | Cohort | Status | Priv /36 | Public | Coding | Wall s | Notes | LB id | Source |
|---|---|---|---|---|---|---|---|---|---|---|---|
| QC30-1 | 10-15 | b11562 · 32K CPU39, q8 KV, non-thinking; private 64K | frozen | over-deadline (private) | deadline | old: core 2/6, 3/6, 1/6; H omits READY; T 5/6 + S FK (96.9 s) | – | 1200.016 | – | h-qwencoder30-20261015 ("public complete", no parts) | CAMP |

#### Qwen3-Coder-Next 80B-A3B Q4_K_M (45.196 GiB)

| ID | Date | Quant · engine · profile | Cohort | Status | Priv /36 | Public | Coding | Wall s | Notes | LB id | Source |
|---|---|---|---|---|---|---|---|---|---|---|---|
| QCN-1 | 10-15 | stock b11562 | – | capacity-rejected (resident-weight arithmetic) | – | – | – | – | – | — | CAMP (capacity bound) |
| QCN-2 | 10-16 | stock mmap startup | – | capacity-rejected (0.115 GiB RAM, 0.125 GiB commit) | – | – | – | – | whole-file prefetch pressure; led to the prefetch opt-out (section 4.2) | — | RPT/2026-10-16-coder-next.json |
| QCN-3 | 10-16 | b11562-noprefetch, 64K; history recovery with 46 CPU blocks | frozen (21,600 s runner) | public old scale | – | old: Python 6/6 (793.8 s); T 4/6 + S FK (561.8 s); H attempt 1 RAM stop (383.4 s), recovery pass (1177.6 s) | – | 562-1178 | – | — | RPT/2026-10-16-coder-next.json; EXP section 2 |
| QCN-4 | 10-16 | private, temp 1.0 | frozen (21,600 s runner) | unscored (16-tool-round limit) | – | – | – | 4075.125 | 15 failed reads | h-codernext80-20261016 | RUNS/expansion-20261016-coder-next-recovery64/outcome.json |

#### Qwen3-Next-80B-A3B-Instruct IQ3_M (36,643,914,208 B)

| ID | Date | Quant · engine · profile | Cohort | Status | Priv /36 | Public | Coding | Wall s | Notes | LB id | Source |
|---|---|---|---|---|---|---|---|---|---|---|---|
| QN80-1 | 10-12 | llama.cpp (12 Oct install) · 28 GPU layers, 32K f16 KV | install smoke | capacity-rejected (12.4 GiB shared-GPU spill) | – | – | valid reply and tool call | 25.6 | – | — | INSTALL L10-14 |
| QN80-2 | 10-12 | 10 GPU layers; greedy, recommended (0.7/0.8/20) and self-reviewed samplings | 12 Oct synthetic suite | interrupted (0x124 and 0x3B crashes) | – | – | diff-scale: intervals 94/105, ttl 34/34, dag 64/64; CSV 104/120 before the restart | 48.7-90.0 per task | – | — | BEN/2026-10-12/quality-results-rescored.json; BEN/2026-10-12/model-setup-report.html |

#### Qwen3.6-35B-A3B

Quant is UD-Q4_K_M (22,134,528,992 B) unless stated. Other files: IQ4_XS
17,730,509,792 B; IQ3_S 13,676,723,168 B; Q5 24.639 GiB; Q6_K_XL 31,843,777,504 B;
plain Q6_K 29,308,320,736 B.

| ID | Date | Quant · engine · profile | Cohort | Status | Priv /36 | Public | Coding | Wall s | Notes | LB id | Source |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Q36-01 | 10-13 | b11562 · 30 GPU layers, n-cpu-moe 32, 64K q8, b128/u32, mmap, temp 1.0 | frozen | unscored (harness rename error) | – | – | – | – | – | — | RUNS/qwen36-q4-thinking/outcome.json |
| Q36-02 | 10-13 | same | frozen | over-deadline | – | – | – | 1200.0 | prefill 36.42 tok/s | — | RUNS/qwen36-q4-thinking-r2/outcome.json |
| Q36-03 | 10-13 | short tests: thinking on, t1.0, cap 2048 / thinking off / on, t0.6, cap 8192 | diff-scale | done (the on-2048 boundary test hit its cap) | – | – | diff-scale: boundary unscored / 15/16 / 16/16; source 5/5 ×3 | 152.75 / 3.69 / 210.81 | placement not recorded | — | BEN/2026-10-13-instructions/short-tests/review.json |
| Q36-04 | 10-13 | config-1.3 flags: 30 GPU, n-cpu-moe 34, b512/u128, 4/8 threads, non-mmap, temp 1.0 | frozen | scored; LB rank 6 (72.2) | 26 (19/4/3) | – | – | 830.9 | prefill 233.48 tok/s | h-qwen36-q4-t10-20261013 | RUNS/qwen36-q4-tuned/review.json |
| Q36-05 | 10-13 | config 1.3, temp 0.6 | frozen | scored; LB rank 2 (86.1) | 31 (21/5/5; regraded 20/6/5 on 15 Oct, K1) | – | – | 863.89 | became config 1.3 | h-qwen36-q4-t06-20261013 | RUNS/qwen36-q4-coding-t06/review.json, runtime-profile.json |
| Q36-06 | 10-14 | config 1.4: n-cpu-moe 33, b256/u64 | editor | Copilot greeting 82.35 s, 3-file reply 59 s; Continue inconclusive; CPU32 variant capacity-rejected (VRAM) | not re-audited | – | – | – | – | — | DT/2026-10-14-copilot-recovery/2026-10-14-copilot-gpu-recovery-v1.4.md |
| Q36-07 | 10-14 | placement pair at 64K, cap 2048: 30 GPU + 33 CPU-expert blocks against gpu-layers all + --cpu-moe | frozen (old40) | done | – | old40: R 39/40 against 38/40 | – | 576.453 against 204.891 | 13.34 against 23.67 tok/s | — | RPT/2026-10-14-placement-results.json |
| Q36-08 | 10-14 | runtime flags at 64K CPU33: reasoning budget 0 / 512 / 2048 | diagnostic | 0 and 512 done; 2048 RAM-guard stop | – | – | diff-scale 3/7, 5/7, unscored | 136.22 / 161.95 / 103.47 | budgets verified by re-tokenizing | — | DT/2026-10-14-runtime-flags/2026-10-14-runtime-flags.md |
| Q36-09 | 10-14 | 32K CPU32: budget 2048 / unrestricted; --no-kv-offload and moe-cache 512 arms prepared | diagnostic | 2048 done; unrestricted RAM stop at 9.77 s; the two arms never loaded | – | – | diff-scale 7/7 | 264.95 | production restore refused (16.7 < 20.5 GiB) | — | same; BEN/2026-10-14-flags/restore-attempt.json |
| Q36-10 | 10-15 01:29 | early b512/u128 trial | frozen | interrupted (planned Windows Update) | – | – | – | – | – | — | CAMP (Restart recovery) |
| Q36-11 | 10-15 | all non-expert layers on GPU, routed experts in RAM | frozen (old) | done | – | old: core 6/6 ×3 (240.2 / 237.6 / 325.2 s); context pass; T 5/6 + S FK + bad RENAME | – | 134-325 | about 22 tok/s | — | CAMP |
| Q36-12 | 10-15 | 64K, all experts on CPU, cap 2048: (a) no cache, (b) cache 1536, (c) cache 3072, (d) b512/u128, (e) --no-kv-offload, (f) 3072 + b512/u128 | frozen (old) | (a)-(e) done, each core 6/6 + history pass; (f) capacity-rejected (7083 < 7100 MiB) | – | router s: 212.75 / 136.92 / 118.42 / 248.09 / 407.92 | – | – | decode tok/s 22.78 / 39.18 / 46.71 / 23.57 / 13.13 | — | RPT/2026-10-15-cache-results.json |
| Q36-13 | 10-15 | sampling: temp 0.35 + min-p 0.02 | frozen (old) | done | – | old: core 6/6 ×3; TS compile fail + S FK | – | 217-314 | no gain over 0.6 | — | CAMP (Research sampling) |
| Q36-14 | 10-15 | Q4 against Q5, matched 32K CPU35 b128/u32 cap 2048 | frozen (old) | done | – | old: Q4 6/6 ×3; Q5 6/6 ×3 | – | Q4 186-240; Q5 240-274 | Q5 19.1% slower | — | RPT/2026-10-15-qwen-precision-results.json |
| Q36-15 | 10-15 | 64K CPU35 b128/u32: cap 2048 / native | frozen | scored ×2 (identical answers) | 25 (18/4/3) ×2 | not on this profile | – | 458.703 / 454.859 | the cap never bound | — | PRIV qwen36-q4-private-2048, -unrestricted |
| Q36-16 | 10-15 | cache2048 finalist: all layers GPU, --cpu-moe, 2048 MiB cache, non-mmap | frozen | scored; LB rank 4 (75.0) | 27 (19/4/4) | old: Python 6/6 ×3; TS compile fail; S FK; 52K H pass | – | 402.703 | about 41 tok/s | h-qwen36-q4-cache2048-20261015 | PRIV; RPT/2026-10-15-finalist-results.json |
| Q36-17 | 10-15 | historical34 finalist (config-1.3 flags); became config 2.0 | frozen | private replay + public old scale | 31 (20/6/5; answer byte-identical to Q36-05) | old: Python 6/6, 6/6, 4/6; T 5/6 + S FK; 52K H pass (448.062 s) | – | 864.266 | – | shares h-qwen36-q4-t06-20261013 | PRIV qwen36-historical34-private-recheck; RPT/2026-10-15-finalist-results.json |
| Q36-18 | 10-15 | UD-Q5_K_M · 64K CPU35 b128/u32, native | frozen | scored; LB rank 3 (77.8) | 28 (20/6/2) | old: core 6/6; H-120 pass; T 4/6 + S FK | – | 537.25 | – | h-qwen36-q5-20261015 | PRIV qwen36-q5-private-unrestricted |
| Q36-19 | 10-15 | UD-Q6_K_XL · 32K CPU35 (gate 28.5 GiB) | frozen | capacity-rejected (27.426 GiB) | – | – | – | – | – | — | CAMP (Optional Qwen Q6) |
| Q36-20 | 10-15 | production config 2.0 (historical34, port 8080) | production | API READY 11.938 s, 2-file reply 34.297 s; 6 UI probes done, with defects | inherits 31 | – | – | – | – | — | RPT/2026-10-15-selection.json; RPT/2026-10-15-editor-results.json |
| Q36-21 | 10-16 | context recall at temp 0, budget 0: CPU KV 64K / 128K; mixed KV 128K | diagnostic | done | – | recall 2K-60K pass; at 120K the facts are correct but the JSON is fenced | – | 733.06 CPU / 610.02 mixed (120K) | KV 680 MiB at 64K, 1360 MiB at 128K | — | RPT/2026-10-16-context-growth.json |
| Q36-22 | 10-16/17 | mapped64 (profile qwen36-q4-noprefetch64-control): b11562-noprefetch, mmap, all layers GPU, n-cpu-moe 37, 64K q8 GPU KV, b512/u128, temp 0.6 | frozen (every task ≤ 724.1 s) | scored; **LB rank 1 (86.3)** | **31 (20/5/6)** | **52/60** (R39 H8 T5 S0; regraded 20 Oct) | not collected | 699.656 | reference profile | h-qwen36-q4-mapped64-20261016 | RPT/2026-10-17-qwen-precision.json; EXP section 4 |
| Q36-23 | 10-16/17 | UD-Q6_K_XL · matched mapped CPU37 | frozen (21,600 s runner; over-deadline) | over-deadline | 28 (19/4/5) | old: Python 6/6 ×3; T 5/6 + S FK; H-120 pass; H-640 pass (3296.9 s) | – | 2099.672 | about 3× slower than Q4 | h-qwen36-q6-20261016 | RPT/2026-10-17-qwen-precision.json |
| Q36-24 | 10-17 | production config 2.1 (mapped-editor64, CPU37) | production | READY 13.125 s; 2-file reply 69.484 s (9/9 values, JSON fences) | – | – | – | – | – | — | RPT/2026-10-17-availability.json |
| Q36-25 | 10-17 | configs 2.2 (19:05) then 2.3 (19:50): 131072 context, --no-kv-offload q8, CPU37, 1800 s idle sleep | production + diagnostic | READY receipts; 4-file test 378.437 s; 70K probe interrupted | – | – | – | – | – | — | INSTALL L116-126; LT/2026-10-17-context128-and-tool-budget/2026-10-17-context128-and-tool-budget-v0.4.2.md |
| Q36-26 | 10-18 06:01 | production 2.3 restored | API | READY. in 7.125 s | – | – | – | – | – | — | RPT/2026-10-18-production-restored.json |
| Q36-27 | 10-18 | Strata v0.1.45 stock, 8K | diagnostic | compatibility failure (exit 1 at 3.156 s) | – | – | – | – | missing nextn_predict_layers metadata | — | RPT/2026-10-18-strata-qwen.json; STR L308 |
| Q36-28 | 10-18 | Strata fork 3e0b27d4, pinned 8K: (a) packed Q8, (b) no extra Q8 copy, (c) b + 19.5 GiB cap | diagnostic | capacity-rejected ×3 (RAM floor at 13.281 / 8.922 / 14.109 s) | – | – | – | – | – | — | RPT/2026-10-18-strata-qwen.json; STR L310-312 |
| Q36-29 | 10-18 | Strata pageable b0513bee; TRIM_GGUF 6ef632f7 A/B at 32K | diagnostic | smoke done (64.390 s); 32K pageable RAM floor; trim-off RAM floor at 12.36 s; trim-on done (54.25 s) | – | – | – | – | tg64 about 21 tok/s | — | same; STR L313, L365-378 |
| Q36-30 | 10-18 | Strata server, pinned 32K, graphs on | frozen | interrupted (VRAM guard < 600 MiB) | – | partial router only | – | 204.984 | – | — | same; STR L380-382 |
| Q36-31 | 10-18 | Strata 6ef632f7: 32K fp32 GPU KV, 64-token chunks, --no-graph, 0.25 GiB GPU experts | frozen (old40) | done (not /60) | – | old40: R 40/40 (286.516 s); H 6/6 facts (250.625 s); T 5/6 + S migration fail (203.765 s) | – | 204-287 | peak working set 20.09 GiB; minimum free 2.62 GiB | — | same; STR L164-220 |
| Q36-32 | 10-18 | llama b11562-noprefetch 32K control: CPU q8 KV, CPU37, b512/u128 | frozen (old40) | done | – | old40: R 40/40 (436.469 s); H 6/6 (285.891 s); T 5/6 + **S 6/6** (357.687 s) | – | 286-436 | minimum free 6.28 GiB | — | same; profiles/qwen36-strata-control32.json |
| Q36-33 | 10-20 | core-0 baseline: CPU37, 64K GPU q8, mask 0x5554, 5 GiB gates | frozen | interrupted (RAM floor 0.454 GiB) | – | none | – | 176.156 (server clock 192.98; K2) | working set 19.07 GiB | q4-baseline-core0-20261020 | LD/2026-10-20-campaign/q4-baseline-core0-20261020-public/core-seed73/result.json; server memory.jsonl |
| Q36-34 | 10-21 06:27 | UD-IQ4_XS · CPU37, 64K GPU q8, no cap | frozen | interrupted (RAM floor during TS/SQL) | – | part R 39/40 (701.75 s); TS/SQL stopped at 385.984 s | – | 701.75 | preflight 12.25 GiB free (K13) | qwen36-iq4xs-20261020 | LD/2026-10-21-campaign/qwen36-iq4xs-20261020-public/{core-seed73,ts-sql-v1}/result.json |
| Q36-35 | 10-21 | UD-IQ4_XS · CPU34 placement (a)/(b) | diagnostic | (a) capacity-rejected; (b) interrupted (commit floor at 23.7 s) | – | – | – | – | +4.378 GiB commit for +4.22 GiB VRAM | — | QWR; LD/2026-10-21-placement/server/runs/server-20261021-113320/stop.json |
| Q36-36 | 10-21 | UD-IQ3_S · CPU34 placement (a)/(b) | diagnostic | (a) capacity-rejected (VRAM); (b) load test, requested stop | – | – | – | load 4.12 | decode 12.01 tok/s | — | LD/2026-10-21-placement/server/runs/server-20261021-120020/ |
| Q36-37 | 10-21 12:07:41 | Strata file arena c451fbe8, 32K | diagnostic | interrupted (RAM floor before readiness) | – | – | – | 35.734 (telemetry 35.60) | engine RSS 15.98 GiB | qwen36-q4-strata-filearena-20261021 | LD/2026-10-21-strata-arena/run-q4-fileArena-5/result.json |
| Q36-38 | 10-21 20:43:30 | UD-IQ3_S · run A, moe34-mmap64 | frozen | capacity-rejected (7.83 < 8 GiB) | – | – | – | – | – | qwen36-iq3s-20261021 | LB addendum |
| Q36-39 | 10-21 20:44 | UD-IQ3_S · run B | frozen | interrupted (fail-closed nvidia-smi read under RAM pressure) | – | none | – | 369.39 (server 382.67; K4) | lowest VRAM seen 1,152 MiB | qwen36-iq3s-20261021b | LD/2026-10-21-campaign/qwen36-iq3s-20261021b-public/core-seed73/stream-01.jsonl; server/runs/server-20261021-204425/ |
| Q36-40 | built 10-21 20:47 | Strata expert pack b5211998 | diagnostic | not run (queue gates unmet until 21:08 on 3 Nov) | – | – | – | – | now queue item 2 | — | STR L669-684; LD/2026-11-03-queue/queue.json |
| Q36-41 | 10-24 | production 2.3 restore | API | READY. in 15.641 s; production off since 24 Oct 13:23 | – | – | – | – | – | — | RPT/2026-10-24-production-restored.json |
| Q36-42 | 10-24 | UD-IQ3_S · coverage64 CPU38, native | frozen | unscored (coding gate failed) | 29 (20/4/5) | 52/60 (R39 T5 S0 H8) | native: intervals and TTL hit the 16K output limit; DAG interrupted | 638.6 | 15.66 tok/s | qwen-iq3s-coverage-a | RPT/2026-10-24-qwen-iq3s-coverage.json, -native-coding.json |
| Q36-43 | 10-24 | UD-IQ3_S · 4096 cap, no cache | diagnostic | interrupted (deliberate) | – | – | compl 2/12 | – | – | qwen-iq3s-budget4096-control-a | RPT/2026-10-24-qwen-iq3s-budget-control.json |
| Q36-44 | 10-24 | UD-IQ3_S · 4096 cap + 1536 MiB cache | diagnostic | coding scored | – | – | **6/12** (all 12 finished) | 133.86 median | 31-37 tok/s | qwen-iq3s-budget4096-cache1536-coding-a | RPT/2026-10-24-qwen-iq3s-cached-coding.json |
| Q36-45 | 10-24 | UD-IQ3_S · uncapped + 1536 MiB cache | diagnostic | not run | – | – | – | – | – | qwen-iq3s-uncapped-cache1536-not-run | LB |
| Q36-46 | 10-24 | UD-IQ4_XS · CPU35, no cap | frozen | interrupted (RAM guard) | – | none | – | 190.25 | – | qwen-iq4xs-cpu35-nocap-ramstop-20261024 | RPT/2026-10-24-qwen-iq4xs-ram-stop.json |
| Q36-47 | 10-24 | UD-IQ4_XS · CPU35, 13.356 GiB cap | frozen | unscored (coding: intervals deadline) | 29 (19/4/6) | **55/60** (R39 T5 S3 H8) | intervals deadline; 11 unrun | 725.4 | – | qwen-iq4xs-cpu35-paging-a | RPT/2026-10-24-qwen-iq4xs-public.json, -private.json, -native-coding.json |
| Q36-48 | 10-24 | UD-IQ4_XS · presence penalty 1.5 | diagnostic | unscored | – | – | intervals spent 16,384 tokens on reasoning | 1187.703 | – | qwen-iq4xs-presence15-control-a | RPT/2026-10-24-qwen-iq4xs-presence-control.json |
| Q36-49 | 10-24 | native coverage64, CPU37 | frozen | interrupted (RAM stop, then JS resume) | – | – | compl 9/12 | 557.828 median | – | qwen-q4-native-coverage-a | RPT/2026-10-24-qwen-q4-native-coding.json, -native-js-resume.json |
| Q36-50 | 10-24 | CPU40, cache 2048, resident7, general32K | frozen | over-deadline (intervals) | – | – | none | 1200.016 | 6.69 tok/s | qwen-q4-resident7-general32k-20261024 | RPT/2026-10-24-qwen-q4-resident7-coding.json |
| Q36-51 | 10-24 | UD-Q6_K plain · 18 GiB gate | frozen | capacity-rejected | – | – | – | – | – | qwen-q6plain-18gib-rejected-20261024 | RPT/2026-10-24-qwen-q6plain-install.json |
| Q36-52 | 10-24 | UD-Q6_K plain · resident7 | frozen | over-deadline (router; first visible text at 1080.8 s) | – | none | – | 1200.016 | – | qwen-q6plain-resident7-20261024 | RPT/2026-10-24-qwen-q6plain-resident7-public.json |
| Q36-53 | 10-24 | UD-Q6_K plain · resident10 | frozen | over-deadline (router; first visible text at 824.6 s) | – | none | – | 1200.031 | – | qwen-q6plain-resident10-20261024 | RPT/2026-10-24-qwen-q6plain-resident10-public.json |
| Q36-54 | 10-26 08:10 | CPU40, cache 2048, general32K (16 GiB gate) | frozen | capacity-rejected (2.169 GiB free) | – | – | – | – | – | qwen-q4-cpu40-cache2048-general32k-rejected-20261026 | RPT/2026-10-26-resume-capacity.json |
| Q36-55 | 11-03 | + Qwen3.5-0.8B Q8_0 draft (811,843,840 B), draft-simple n-max 8 | diagnostic (planned) | not run | – | – | – | – | the draft moved after its hash check (K9); profile has no --cpu-mask and no runtime_variant pin | — | profiles/qwen36-q4-spec-draft08b-mmap64.json; LD/2026-11-03-queue/qwen35-draft-download.log |
| Q36-56 | 11-03 | ngram-simple self-drafting | diagnostic (planned) | not run | – | – | – | – | profile has no --cpu-mask and no runtime_variant pin | — | profiles/qwen36-q4-spec-ngram-mmap64.json |
| Q36-57 | 11-03 | MTP self-speculation (needs an MTP GGUF); b12069 side-build arms | research | not run | – | – | – | – | b12069 side build linked 21:10; untested | — | DR L204, L237-273; `C:/llm-staging/build/b12069-build.log` |

#### Qwen3.8-27B dense

| ID | Date | Quant · engine · profile | Cohort | Status | Priv /36 | Public | Coding | Wall s | Notes | LB id | Source |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Q38-1 | 10-12 | Q8_0 (29,047,086,048 B) · 16K, 8 layers, xhigh | smoke | passed | – | – | – | – | 1.072 tok/s | — | INSTALL L60 |
| Q38-2 | 10-12 | Q8_0 · 64K, 12 layers, xhigh, cap 8192 | coding rerun | interrupted (19:03 restart) | – | – | intervals at xhigh: 0 final characters | 5552.3 | – | — | BEN/2026-10-12-qwen38/progress.json |
| Q38-3 | 10-12 | Q8_0 · 16K, 14 layers | short tests | capacity-rejected (RAM guard ×2) | – | – | – | 755.4 | – | — | BEN/2026-10-12-qwen38-q8-small/monitor-stop.json |
| Q38-4 | 10-12 | UD-Q6_K (21,983,677,344 B) · 16K, 18 layers | short tests | interrupted on purpose (placement change) | – | – | – | 123.3 | – | — | BEN/2026-10-12-qwen38-q6/18-layer-*.json |
| Q38-5 | 10-12 | UD-Q6_K · 16K, 16 layers; effort low / medium / xhigh | diff-scale | done | – | – | diff-scale: boundary 16/16 and source 5/5 at all three efforts | boundary 277.4 / 373.0 / 625.9 | 1.44-1.56 tok/s | — | BEN/2026-10-13-instructions/historical-short-results.json |
| Q38-6 | 10-12/13 | UD-Q6_K · 64K, 5 real files attached | probe | unscored (output cap) | – | – | – | 7548.5 | – | — | BEN/2026-10-12-qwen38-q6-64k/progress.json |
| Q38-7 | 10-12/13 | Q8_0 · 64K, non-mmap, xhigh | diff-scale | 2 tests done, then a VRAM-guard stop | – | – | diff-scale: boundary 16/16 (808.4 s); source 5/5 (after a grader fix from 4/5) | – | – | — | BEN/2026-10-12-qwen38-q8-nommap/; MIG/2026-10-13-editor-setup/grader-correction.json |
| Q38-8 | 10-13 | UD-Q6_K · config 1.1 editor | editor | API pass (71.84 s); no completed UI reply | – | – | – | – | a 39,111-token input took 2,358.44 s | — | MIG/2026-10-13-editor-setup/ |
| Q38-9 | 10-13 | UD-Q6_K · /36 audit, 64K, 14 layers, xhigh | frozen | over-deadline (cancelled, no answer) | unscored | – | – | 13731.7 | about 0.65 tok/s at long context | h-qwen38-27b-q6-20261013 (LB 13734 s, "1.4 tok/s"; K7) | RUNS/qwen38-q6-xhigh/outcome.json, benchmark-start.json |
| Q38-10 | 10-19 | TQ3_4S-v2 (14,495,191,008 B) · llama.cpp-tq3, -ngl 16/24/28/30 | diagnostic | done | – | – | – | – | 1.494 / 1.757 / 1.939 / 1.923 tok/s | — | LT/2026-10-19-azllm/2026-10-19-azllm-and-turboquant-v0.7.0.md L64; RPT/2026-10-19-tq3-measurements.json |
| Q38-11 | 10-19 | TQ3 · 24 layers: native MTP max 2; DFlash2 draft max 7 | diagnostic | done (not promoted) | – | – | – | – | 1.790 tok/s (83.3% accepted); 2.093 tok/s | — | same report L67-68 |
| Q38-12 | 10-19 | TQ3 · 28 layers, 32K CPU q8 KV, 8 threads | frozen | interrupted (PC reset, core-0 machine check) | none | – | – | 862.125 | 1.77 tok/s | h-qwen38-tq3-20261019 | RPT/2026-10-19-tq3-measurements.json |
| Q38-13 | 10-26/27 | UD-Q4_K_M / UD-Q6_K / UD-IQ4_XS (14,252,845,984 B) | plan | not run (metadata only) | – | – | – | – | – | — | LT/2026-10-26-qwen38-dense/2026-10-26-qwen38-dense-v0.10.0.md L37-106 |

#### Qwen3.8-Flash-Next 125B (6B active)

| ID | Date | Quant · engine · profile | Cohort | Status | Priv /36 | Public | Coding | Wall s | Notes | LB id | Source |
|---|---|---|---|---|---|---|---|---|---|---|---|
| QFN-1 | 10-18 | GSQ-RCO IQ3_XXS (47,039,860,096 + 28,800,138,432 B) · Strata v0.1.45: spec 0; spec 2 + 1200 MiB reserve; 3072 MiB reserve | diagnostic | two early stops (3.843 s; 7.14 s), then READY in 13.531 s | – | – | – | – | 7.0 tok/s | — | RPT/2026-10-18-strata-flash.json; STR L150-160 |
| QFN-2 | 10-18 | no draft: 32K int8 KV, 10 GiB expert pool, xhigh with a 2048 cap | frozen | over-deadline (router and TS/SQL) | – | history 6/6 facts + READY count 120 (219.015 s) only | – | 1200.016 | 5.1-5.9 tok/s | h-flashnext-strata-20261018 | RPT/2026-10-18-strata-flash.json (cases) |
| QFN-3 | 10-18 | + MTP spec 4: 10 GiB pool / 14 GiB pool | frozen | over-deadline (router 1200.031 / 1200.016 s) | – | none | – | 1200 | 248/326 drafts accepted, 6.2 tok/s; 14 GiB pool 8.8-9.6 tok/s on capped probes | folded into the h-flashnext-strata notes | RPT/2026-10-18-strata-flash.json; RPT/2026-10-18-strata-ram-probes.json |
| QFN-4 | 10-18 | 128K head-alias, 12 GiB pool | diagnostic | capacity-rejected (VRAM 566 MiB at 14.844 s) | – | – | – | – | – | — | RPT/2026-10-18-strata-flash.json |
| QFN-5 | 10-18 | 128K RAM-backed KV (32K resident) | frozen | unscored (empty final answer) | – | phase 0 READY count 640, exact | – | 468.078 (last event) | prefill 201.0 tok/s | folded | RPT/2026-10-18-strata-flash.json (flash-large-history) |
| QFN-6 | 10-18 | final-turn replays: xhigh / medium | diagnostic | done | – | 6/6 facts each | – | 49.296 / 314.438 | – | folded | RPT/2026-10-18-strata-history-replays.json |
| QFN-7 | 10-18 | 16 GiB pool | – | not run (commit estimate) | – | – | – | – | – | — | STR L44-45 |
| QFN-8 | 10-27 | GSQ-RCO Q2_0 · Strata 0.1.50 + frontend v0.2.6; 4 plans | planned | not run (launchable: false) | – | – | – | – | – | flashnext-gsq-q2-strata0150-not-run | LD/2026-10-26-articles/strata-q2-*.planned.json |
| QFN-9 | 11-03 18:57 to 21:10 | Q2_0 download (rev ed59f920) and native pack | – | downloaded and packed, never loaded: shard 1 SHA256 verified 20:14:39, shard 2 21:07:07; pack built 21:10 in 9.3 s (1,495,796,923 B; 0 conversions) | – | – | – | – | mmap32 qualification still blocked (section 7) | same LB row (its "not-downloaded" addendum is now stale; K8) | `E:/llm/Strata-data/models/flash-next/verified-download.json`; RPT/2026-11-03-flash-next-q2-pack.json |

#### Recursive Flint 40B-A2.5B

| ID | Date | Quant · engine · profile | Cohort | Status | Priv /36 | Public | Coding | Wall s | Notes | LB id | Source |
|---|---|---|---|---|---|---|---|---|---|---|---|
| FLT-01 | 10-23 | UD-IQ3_XXS (14,535,427,520 B) · b11838 · CPU KV 64K, n-cpu-moe 36 | frozen | unscored (smoke only) | – | – | – | 0.937 | READY | flint-iq3xxs-cpukv-smoke-20261023 | RPT/2026-10-23-flint-smoke.json |
| FLT-02 | 10-23 | same, native reasoning | frozen | over-deadline (router, no answer) | – | none | – | 1200.031 | 50,287 reasoning characters, 0 final | flint-iq3xxs-cpukv-native-20261023 | RPT/2026-10-23-flint-native.json |
| FLT-03 | 10-23 | + 2048 reasoning cap | diagnostic | over-deadline | – | none | – | 1200.016 | planning moved into visible content | flint-iq3xxs-cpukv-cap2048-20261023 | RPT/2026-10-23-flint-cap2048.json |
| FLT-04 | 10-23 | GPU q8 KV 64K, n-cpu-moe 38, native | frozen | unscored (TS/SQL tool-turn limit; history output limit) | 29 (19/4/6) | part R 39/40 (523 s) | compl 11/12 | 692.5 | coding median 225.6 s | flint-iq3xxs-gpukv64-20261023 | RPT/2026-10-23-flint-gpukv-public.json; RPT/2026-10-23-flint-private.json; RPT/2026-10-23-flint-coding.json |
| FLT-05 | 10-23 | GPU KV + 2048 cap | diagnostic | not run (prepared) | – | – | – | – | – | — | FLR L687 |
| FLT-06 | 10-24 | history with 8192 output tokens | diagnostic | done | – | part H 8/8 | – | 328.016 | 22.1 tok/s | flint-iq3xxs-history8192-20261024 | RPT/2026-10-24-flint-history8192.json |
| FLT-07 | 10-24 | b11838 stock against the prefetch opt-out, greedy equality | engine check | passed | – | – | – | – | – | — | RPT/2026-10-24-b11838-prefetch-control.json |
| FLT-08 | 10-24 | UD-Q4_K_XL (25,054,688,704 B) · CPU42 | frozen | capacity-rejected (VRAM gate) | – | – | – | – | – | flint-q4xl-cpu42-rejected-20261024 | LB |
| FLT-09 | 10-24 | UD-Q4_K_XL · CPU44 paging | frozen | over-deadline (router) | – | none | – | 1200.031 | seven reads, no final answer | flint-q4xl-cpu44-paging-a | RPT/2026-10-24-flint-q4xl-cpu44.json |
| FLT-10 | 10-24 | UD-Q4_K_XL · CPU48 + 1536 MiB cache | frozen | over-deadline (router; partial text from 1137 s) | – | none | – | 1200.031 | – | flint-q4xl-cpu48-cache1536-paging-a | RPT/2026-10-24-flint-q4xl-cache1536.json |
| FLT-11 | 10-26 08:10 | UD-Q3_K_XL (18,494,977,472 B) · cpu49-cache2048-resident7 | extended | capacity-rejected (2.169 GiB free) | – | – | – | – | – | — | RPT/2026-10-26-resume-capacity.json |
| FLT-12 | 10-26 | Q3_K_XL · profile A: CPU49, 32K, cache 512, 4 GiB cap | extended | unscored (greeting qualification) | – | – | – | 48.375 cold | greetings 48.375 / 31.141 s | flint-q3xl-a-greeting-20261026 | RPT/2026-10-26-flint-q3xl-greeting.json |
| FLT-13 | 10-26 23:29 / 23:39 | Q3_K_XL · file64-a / file32-a | extended | capacity-rejected ×2 | – | – | – | – | RAM 8.996 < 11.5 GiB; VRAM below 5000 MiB at postflight | flint-q3xl-file64-a-rejected-20261026; flint-q3xl-file32-a-rejected-20261026 | RPT/2026-10-26-flint-admission-rejections.json |
| FLT-14 | 10-26 | official NVFP4 (22.86 GB) | frozen | not run (not downloaded) | – | – | – | – | – | flint-nvfp4-not-run | LB |
| FLT-15 | 10-27 | Q3_K_XL · profile B, measured32 | extended | unscored (router and TS/SQL hit the 16K output limit) | – | part H 8/8 (3380.75 s) | – | 5039.5 | 4.3 / 3.5 tok/s | flint-q3xl-b-measured32-20261027 | RPT/2026-10-27-flint-q3xl-file-workflows.json, -router-limit.json, -ts-limit.json |
| FLT-16 | 10-27 | Q3_K_XL · profile C: 40K, 1 GiB cap, 32K output, reasoning budget 1024 | extended | unscored as /60 (graded 3 Nov) | – | part R 38/40 | – | 2268.531 | 2.13 tok/s | flint-q3xl-c-budget1024-20261027 | RPT/2026-11-03-flint-runC-grades.json |
| FLT-17 | 10-27 | profile C, budget 8192 | extended | unscored as /60 | – | part R 37/40 | – | 5438.078 | 2.116 tok/s | flint-q3xl-c-budget8192-20261027 | RPT/2026-11-03-flint-runC-grades.json |
| FLT-18 | 10-27 | profile C, native reasoning | extended | interrupted (RAM guard) | – | none | – | 6136.203 | 0 visible text | flint-q3xl-c-native32k-20261027 | RPT/2026-11-03-flint-runC-grades.json; stop.json |
| FLT-19 | 10-26/27 | private72K ×2, cache1024-resident5/7, resident6-measured32 | extended | not run (prepared; private72K is queue item 1 since 3 Nov) | – | – | – | – | the private audit needs about 72K of context | — | RB section 5; RPT/2026-10-27-private-context-sizing.json; QUEUE |

#### Engine and host diagnostics (no model loaded)

| ID | Date | What | Result | LB | Source |
|---|---|---|---|---|---|
| ENG-1 | 11-03 19:04 | WDDM commit probe: hold 1 GiB with cudaMalloc (vram_hog) | +1210 MiB VRAM gave +1.379 GiB commit, released on free. Median commit/VRAM ratio 1.038 across 67 saved loads | n/a | LD/2026-10-21-strata-8gb/wddm-commit-causal-probe-20261103.json; LD/2026-11-03-wddm-commit/analysis.json |
| ENG-2 | 11-03 19:05-19:26 | cudaMemGetInfo against NVML; Strata fork 28ce3b52 `--vram-report` | cudaMemGetInfo reports 9097 MiB free with or without another process holding 2048 MiB; NVML 6003 then 3765; upstream DXGI rule 8142 | n/a | LD/2026-10-21-strata-8gb/wddm-cudamemgetinfo-probe-20261103.json; strata-q36-vram-report-validation-20261103*.log |
| ENG-3 | 11-03 19:43 | Strata rebase-trial/v0210 cbfbb0c1 (does not include 28ce3b52) | build passes; 276 sampling checks and all model_family checks pass; no model load | n/a | `E:/llm/Strata-data/build-rebase-trial.log`, `-unit-tests.log` |
| ENG-4 | 11-03, report 21:08 | Read-only re-prefill audit: 120 server logs, 189 conversations, 561 continuation turns | 1 forced full re-prefill (Gemma 4 31B, 9,778 tokens, 512.7 s). Qwen3.6: 222 of 224 turns reused the whole KV; 19.4 s lost in 2 partial turns. Editor logs: 578.3 s in 4 same-prefix divergences (8.3% of editor prefill) | n/a | RPA |
| ENG-5 | 11-03 21:00-21:01 | Strata fork 1beb824e: `STRATA_WDDM_BUDGET` parsing, checked with `--vram-report` | unset 6599 MiB (NVML rule); =0 9097; =dxgi 8142; =NVML now 6594 (was silently 9097) | n/a | commit 1beb824e message in `E:/llm/Strata`; LD/2026-10-21-strata-8gb/strata-q36-vram-report-review-20261103-fixed.log |

#### Routes not run, combinations and other candidates

| ID | Date | Item | Status | Source |
|---|---|---|---|---|
| NR-1 | 10-12 | OpenRouter: 9 hosted models, 144 planned evaluations | not run (HTTP 403 IP allowlist; $0 spent) | BEN/2026-10-12-openrouter/access-status.json |
| NR-2 | 10-14 | Shortlist research (Flash-Next at 103.69 GiB did not fit E:) | research only | DT/2026-10-14-next-model-research/2026-10-14-next-model-research.md |
| NR-3 | 10-26/27 | HyperQwen (24 GB target), a 5070 Ti recipe (12.12 GB weights), AirLLM BF16, llamAmpere (12 GB) | not run | RPT/2026-10-26-article-qualification.json |
| NR-4 | 11-03 | Qwen3.6 + Qwen3.5-4B token fusion; a Groot-to-35B cascade | not run (research; the cascade is not recommended) | DR sections 1.5 and 2 (rank 11) |
| NR-5 | 11-03 20:48 onward | Apps-open small-model arm fetched by another workflow step: Dory-4B Q5_K_M, then Qwen3.5-9B Q5 and Q4 | not run. Dory failed twice with HTTP 404 at 20:48; a later attempt was at 43% at about 21:08; nothing loaded | `C:/llm-staging/logs/appsopen-fetch-20261103.log` |
| NR-6 | all | Never measured: `--fit` (every launch used `--fit off`), a thread sweep, a core-0 pinning A/B, ik_llama.cpp, KTransformers, Bonsai medium effort | not run | LD/2026-11-03-campaign/groot-q4-20261103-public/launcher.log; LT/2026-10-20-lfm25/2026-10-20-lfm25-24b-a2b-qad-q4-v0.10.0.md L83; SKL/reference/hardware.md |

### 2.2 Reconciliation notes

Each conflict was resolved after opening both sources.

| # | Topic | Resolution |
|---|---|---|
| K1 | Qwen Q4 t0.6 private split | 21/5/5 (13 Oct) and 20/6/5 (15 Oct) are two gradings of one byte-identical answer (sha256 ede16ba2…). The total 31 holds; the split depends on the grading pass |
| K2 | Q4 core-0 baseline wall | 176.156 s is the workflow clock; 192.98 s is the server clock. Both are correct |
| K3 | Bonsai PQ2 Prism wall and layers | Wall is 82.391 s (result.json); LB's 120 matches no receipt. "52/65" counts the output layer: 52 of 64 blocks on the GPU |
| K4 | IQ3_S run B wall | 369.39 s (stream) against 382.67 s (server memory log); different clocks |
| K5 | Strata file-arena wall | 35.734 s (result.json) against 35.60 s (telemetry); different clocks |
| K6 | Cohort of Gemma31 7234 s, Q6_K_XL 2099.7 s, Coder-Next 4075 s | Frozen, over-deadline: the 16 Oct runner allowed 21,600 s, but the extended cohort means the 26 Oct policy only. Q4 mapped64 qualifies for frozen because every task took ≤ 724.1 s |
| K7 | Qwen3.8 Q6 audit wall and speed | 13,731.7 s (start to outcome). LB's 1.4 tok/s is the short-context rate; the audit decoded at about 0.65 |
| K8 | Flash-Next Q2_0 download | The 19:35 "51%" was shard 1. Both shards are now verified (20:14:39 and 21:07:07) and packed (21:10); the LB addendum is stale |
| K9 | 0.8B draft location | Hash-checked on C:, then moved to `E:/llm/models` (19:10). No post-move hash was found; the integrity gate needs one before a load |
| K10 | Groot resident4 cohort | LB's "diagnostic" kept (expert cache, cap and batch changes). Several cache-bearing profiles sit in frozen-1200, so an explicit cohort rule is needed |
| K11 | Config label of the 13 Oct 31/36 run | Config 1.3 (30 layers, n-cpu-moe 34, b512/u128). Config 1.4 was never audited |
| K12 | KV type of Strata Qwen3.6 | fp32 on the GPU; int8 belongs to the Flash-Next plan |
| K13 | IQ4_XS 21 Oct preflight | 12.25-12.35 GiB free; LB rounds up to 13. The TS/SQL stop was at 385.984 s |
| K14 | LB rounding of wall times | Rounding only: Q5 537.25, GLM Q6 870.297, cache2048 402.703, Gemma 400.234 |
| K15 | 16.99 GiB / 5.38 GiB snapshots | Two separate snapshots (13 Oct and 15 Oct) of the same placement; both correct |
| K16 | Leaderboard run count | 64, not 62: the two Groot rows were added at 20:51:35 |
| K17 | "Timed Groot benchmark running on 8081" | Nothing was running: the records finished at 20:33:46 and 20:39:37 and no port 8080/8081 listener exists |
| K18 | GLM temperature-only core run | 0.7 comes from the campaign plan file, not a per-run receipt |
| K19 | Date/id mismatches | Naming only: PTQ1 spans midnight; the IQ4_XS id carries the queue date |

## 3. Combinations and tuning dimensions

### 3.1 Which combinations ran

| Family | Quants run | Engines | Context and KV | Other axes varied | Best graded result (cohort) | Rows |
|---|---|---|---|---|---|---|
| Qwen3.6-35B-A3B | UD-Q4_K_M, UD-Q5_K_M, UD-Q6_K_XL, plain UD-Q6_K, UD-IQ4_XS, UD-IQ3_S | b11562, b11562-noprefetch, Strata v0.1.45 fork | 8K-128K; q8 GPU, q8 CPU, mixed; Strata fp32 GPU | 30 GPU layers or all; n-cpu-moe 32-40 or --cpu-moe; expert cache 1536-3072 MiB; caps 7-13.356 GiB; batches 128/32 to 512/128; reasoning budget 0-4096 or native; temperature 0.35-1.0; presence 1.5; mmap or non-mmap; core-0 mask | 31/36 + 52/60 (Q4 mapped64, frozen) | Q36-01 to Q36-57 |
| Recursive Flint 40B-A2.5B | UD-IQ3_XXS, UD-Q4_K_XL, UD-Q3_K_XL | b11838, b11838-noprefetch | 32K, 40K, 64K; CPU or GPU q8 KV | n-cpu-moe 36-49; cache 256-1536 MiB; caps 1-4 GiB; budget 1024, 2048, 8192 or native; output 4096-32768 | 29/36 + R 39/40 + compl 11/12 (IQ3_XXS GPU KV, unscored); R 38/40 (Q3_K_XL C1024, extended part) | FLT-01 to FLT-19 |
| Gemma 4 26B-A4B | QAT Q4_0 | b11562, b11562-noprefetch | 32K, 64K, 128K; q8 GPU | n-cpu-moe 24-30; cache 448; caps 2.5-8 GiB; batches 64/16 to 128/32; temperature 0.6 or 1.0; top-k 20 or 64; cap 2048 or native | 19/36 ranked; 23/36 + 57/60 unscored; coding 10/12 extended | G26-1 to G26-12 |
| Gemma 4 31B dense | QAT Q4_0 | b11562, b11562-noprefetch | 16K-64K; GPU or CPU KV | FFN on CPU or last 14 blocks on GPU; 8/8 threads | 26/36 at 7234 s (over-deadline) | G31-1 to G31-3 |
| GLM-4.7-Flash | UD-Q4_K_XL, Q5_K_M, UD-Q6_K_XL | b11562 | 32K, 64K; q8 MLA or f16 | n-cpu-moe 40-44; cap 2048 or native; temperature 0.6 or 0.7 | 27/36 (Q4 f16 KV, rank 5) | GLM-1 to GLM-5 |
| Qwen3.8-27B dense | Q8_0, UD-Q6_K, TQ3_4S-v2 | b11562, llama.cpp-tq3 | 16K-64K | 8-30 GPU layers; effort low, medium, xhigh; MTP and DFlash2 drafts; mmap or non-mmap | short tests only (diff-scale) | Q38-1 to Q38-13 |
| Qwen3.8-Flash-Next | GSQ-RCO IQ3_XXS; Q2_0 packed, never loaded | Strata v0.1.45; 0.1.50 staged | 32K, 128K; int8 and RAM-backed KV | expert pool 10, 12 or 14 GiB; MTP spec 4; VRAM reserve 1200 or 3072 MiB; effort xhigh or medium | history 6/6 facts at 32K (part) | QFN-1 to QFN-9 |
| Qwen3-Coder-Next 80B-A3B | Q4_K_M | b11562 stock, b11562-noprefetch | 64K | 46 CPU blocks (recovery); temperature 1.0 | old-scale Python 6/6 | QCN-1 to QCN-4 |
| Qwen3-Coder-30B-A3B | UD-Q4_K_XL | b11562 | 32K, 64K; q8 | CPU39; non-thinking | old scale only | QC30-1 |
| Qwen3-Next-80B-A3B | IQ3_M | llama.cpp (12 Oct install) | 32K f16 | 28 or 10 GPU layers; three samplings | synthetic suite (diff-scale) | QN80-1, QN80-2 |
| Kimi-Linear-48B-A3B | Q4_K_M | b11562 | 32K f16 (q8 rejected); 64K rejected | 23 CPU-MoE blocks | old-scale core 6/6 (seed 75) | KIM-1, KIM-2 |
| LFM2.5-24B-A2B | QAD Q4_0 | b11669 | 64K q8 GPU | CPU28; temperature 0.1; a sampler per suite | 48/60 (private over-deadline) | LFM-1 |
| Ternary Bonsai 2 27B | PQ2_0, PTQ1_0 | b11669 (refused), Prism b10787 | 64K CPU q8 | 52 or 99 GPU layers; xhigh | none | BON-1 to BON-3 |
| Groot-19B-A3B | Q4_K_M | b11562-noprefetch | 64K q8 GPU | uncapped, or 3.31 GiB cap + 512 MiB cache; batches 512/128 or 128/32; floors 0.5 or 2.0 GiB | none | GRT-1, GRT-2 |
| K2 Horizon MoVA 36B-A4B | Q4_K_M | b11838-noprefetch planned | – | five profiles prepared | never loaded | K2-1 |
| Nemotron 3.5 Bolt 74B-A9B | QAD low-bit | b11669 planned | – | one profile | never loaded | NEM-1 |

**Multi-model combinations.**
- **Measured:** none on Qwen3.6. Draft and MTP speculation was measured only on the
  dense Qwen3.8 TQ3 file (Q38-11) and on Flash-Next under Strata (QFN-3).
- **Prepared, never run:** Qwen3.6 with the 0.8B draft (Q36-55) and ngram
  self-drafting (Q36-56).
- **Research only:** Qwen3.6 MTP (Q36-57), token fusion with Qwen3.5-4B, and a
  Groot-to-35B cascade (NR-4).

### 3.2 Tuning dimensions

| Dimension | Tried (rows) | Measured effect | Best setting so far | Not tried |
|---|---|---|---|---|
| Quantization, Qwen3.6 | Q4_K_M, Q5_K_M, Q6_K_XL, plain Q6_K, IQ4_XS, IQ3_S | Private: Q4 25-31 depending on profile. Q5 28 against Q4's 25 on the same CPU35 profile. Q6_K_XL 28 against Q4's 31 on the same mapped CPU37 profile, about 3× slower and over the deadline. IQ4_XS 29, IQ3_S 29. Public /60: Q4 52, IQ4_XS 55, IQ3_S 52. Q5 was 19.1% slower than Q4 on a matched 32K profile (Q36-14) | UD-Q4_K_M | Q8_0; MTP-bearing GGUFs; seeds 74/75 for any quant |
| Quantization, other families | GLM Q4/Q5/Q6; Flint IQ3_XXS/Q3_K_XL/Q4_K_XL; Bonsai PQ2/PTQ1; Qwen3.8 Q8/Q6/TQ3 | GLM: Q4 f16 27, Q6 24, Q5 21, Q4 q8 21, with KV type and the reasoning cap confounded. Flint Q4_K_XL never finished a router within 1200 s; Q3_K_XL ran only in the extended cohort | – | Flint NVFP4 and Q2_K_XL |
| Engine | llama.cpp builds; Strata v0.1.45 fork; TQ3 fork; Prism fork | Strata 1.14-1.76× faster wall on three 32K workflows, one sample each, with a SQLite failure and about 25 GiB of free RAM needed (Q36-31, Q36-32). TQ3 dense 27B ran at 1.5-1.9 tok/s | llama.cpp b11562-noprefetch | b12069 (built, untested); loads on Strata 0.1.50 or 0.2.10; ik_llama.cpp; KTransformers |
| Load mode | mmap + prefetch opt-out; stock mmap; non-mmap; Strata pinned, pageable, file arena | Stock mmap of the 80B exhausted RAM and commit before inference (QCN-2). The non-mapped Q4 launcher held about 24 GiB of commit, against 5.4-6.5 GiB mapped. The Strata file arena drained RAM in 35.7 s (Q36-37) | mmap + prefetch opt-out | Strata expert pack (Q36-40) |
| MoE weight placement | gpu-layers 30 + n-cpu-moe 32-34; gpu-layers all + n-cpu-moe 35-40 or --cpu-moe | All non-expert layers on the GPU with experts on the CPU: router 204.9 s against 576.5 s with 30 GPU layers; 23.67 against 13.34 tok/s; old40 38 against 39 (Q36-07). Moving 1.25 GiB of experts to the GPU cost the same in commit and tripped the commit floor (Q36-35) | gpu-layers all + n-cpu-moe 37 with 64K GPU KV | `--fit`; tensor overrides beyond n-cpu-moe |
| Dense placement | Gemma 31B FFN on CPU, last 14 blocks on GPU, + GPU KV; Qwen3.8 8-30 layers | Faster decode did not shorten the workflow (G31-3). Qwen3.8 TQ3 ran at 1.494-1.939 tok/s from 16 to 30 layers (Q38-10) | none qualifies under 1200 s | – |
| KV placement | GPU q8, CPU q8 (--no-kv-offload), mixed | CPU KV about 1.9× slower on the router: 407.92 against 212.75 s (Q36-12). Flint finished only with GPU KV (FLT-04 against FLT-02/03). At 120K: mixed 610.02 s against CPU 733.06 s (Q36-21) | GPU q8 at 64K; CPU q8 at 128K in production to save VRAM | – |
| KV type | q8_0, f16, Strata fp32 and int8 | Kimi rejects q8 K/V (head dim 72). GLM f16 27 against q8 21, confounded. Qwen3.6 KV is 680 MiB at 64K and 1360 MiB at 128K | q8_0; f16 where q8 is unsupported | q4 KV (K2 plan only) |
| Context | 8K to 131072 | Qwen recall passes 2K-60K; at 120K the facts are correct but the JSON is fenced (Q36-21). The private audit reached 41,305 input tokens on Flint, so a 32K or 40K profile cannot qualify it. Gemma 128K history stopped on the commit floor (G26-12) | 64K for benchmarks; 128K CPU KV in production (no quality score) | 128K serving on Strata; Flint's vendor 512K claim |
| Batch and micro-batch | 512/128, 256/64, 128/32, 64/16; Strata 64-token chunks | b512/u128 against b256/u64: router 248.09 against 212.75 s, so no gain (Q36-12). Smaller batches were used to bound paging profiles | 512/128 on mapped64 | a sweep on mapped64 |
| Threads and affinity | 4 generation / 8 batch with core 0 excluded (mask 0x5554) since 20 Oct; 8/8 for dense | A precaution after core-0 machine checks, not an A/B result | 4/8 with core 0 excluded | a thread sweep; pinned against unpinned |
| GPU expert cache | 448, 512, 1536, 2048, 3072 MiB | On the all-experts-CPU 64K profile: decode 22.78, 39.18, 46.71 tok/s and router 212.75, 136.92, 118.42 s at 0, 1536, 3072 MiB (Q36-12). Cache2048 private 27/36 in 402.7 s on a different placement (Q36-16). Gemma 128K prefill fell from 7.15 to 5.03 tok/s with 448 MiB (G26-11). The hit rate was never measured | 1536-3072 MiB when VRAM and commit allow | a cache on mapped64 with hit-rate logging |
| Working-set cap (residentN) | 1, 3.31, 4, 5, 6, 7, 8, 10 and 13.356 GiB | Lets larger files load with apps open, mostly by paging: Gemma resident6 29% faster than resident4 with identical tokens (G26-9); Groot 2.33 tok/s (GRT-2); Q4 resident7 6.69 tok/s (Q36-50); plain Q6 resident7 and resident10 router deadlines | as large as RAM allows; not a fit fix | – |
| Reasoning budget | 0, 512, 1024, 2048, 4096, 8192, native | Qwen short fixture: 0 gave 3/7, 512 gave 5/7, 2048 gave 7/7 (diff-scale; Q36-08, Q36-09). On the audit the 2048 cap never bound (Q36-15). Flint's 2048 cap still missed the deadline (FLT-03). Flint 1024: R 38/40 in 2268.5 s; 8192: R 37/40 in 5438.1 s (extended). IQ3_S 4096: all 12 coding tasks finished, 6 passed (Q36-44) | native for Qwen Q4; 1024 for Flint Q3_K_XL (extended) | budget effects on the leader's coding suite |
| Thinking and effort | thinking on or off (Qwen3.6); low, medium, xhigh (Qwen3.8, Flash-Next) | Qwen thinking off: 15/16 in 3.69 s; on: 16/16 in 210.81 s (diff-scale, Q36-03). Qwen3.8: 16/16 + 5/5 at every effort, 277-626 s (Q38-5). Flash-Next replays: 6/6 at xhigh and medium (QFN-6) | thinking on, with reasoning history preserved | Bonsai medium effort |
| Output allowance | 4096, 8192, 16384, 24576, 32768 | Flint history fails at 4096 and passes 8/8 at 8192 (FLT-06). Several native runs spent all 16,384 tokens on reasoning (Q36-42, Q36-48, FLT-15) | 16384 standard; at least 8192 for history | – |
| Sampling | temperature 0.1, 0.35 + min-p 0.02, 0.6, 0.7, 1.0; top-k 20 or 64; presence 1.5 | Qwen 0.6 against 1.0: 31 against 26 on the same config (Q36-05, Q36-04). 0.35 + min-p: no gain on old public (Q36-13). Presence 1.5: no completion (Q36-48). LFM looped at 0.1 (LFM-1) | 0.6 / top-p 0.95 / top-k 20 for the Qwen family | seeds 74/75 |
| Speculative decoding | Qwen3.8 TQ3 MTP max 2 and DFlash2 max 7; Flash-Next MTP spec 4 | Dense TQ3 at 24 layers: 1.757 tok/s, 1.790 with MTP, 2.093 with DFlash2 (Q38-10, Q38-11). Flash-Next: 248/326 drafts accepted but 6.2 tok/s and still over the deadline; MTP shrank the GPU expert cache from 904 to 361 slots (QFN-3; STR) | not adopted | Qwen3.6 0.8B draft, ngram and MTP; Groot's built-in MTP layer |
| Prompt cache and checkpoints | `--cache-ram 0`; `--ctx-checkpoints 4` in Qwen profiles | Lab workflows: Qwen3.6 lost 19.4 s to re-prefills across 224 continuation turns. Editor traffic lost 578.3 s in four same-prefix divergences (ENG-4) | unchanged for benchmarks | editor profile with `--ctx-checkpoints 16` and `--cache-ram 2048` (audit estimates only) |
| Admission gates and stop floors | RAM floors 0.5, 2.0 and 2.5 GiB; 1 GiB commit; 400 MiB VRAM; per-profile gates | With a 0.5 GiB floor the desktop reached 0.42 GiB available (GRT-1). The runtime reference (21:00) says `lab.py` now refuses floors below 2.5 GiB | 2.5 GiB RAM / 1 GiB commit / 400 MiB VRAM / 84 C | – |

### 3.3 Scores move with the profile, not only the weights

The same Qwen3.6 UD-Q4_K_M file, at seed 73 and temperature 0.6, gave these
private-audit totals:

| Profile | Private /36 | Row |
|---|---|---|
| 64K, CPU35, b128/u32, cap 2048 or native (identical answers) | 25 | Q36-15 |
| all layers GPU, --cpu-moe, 2048 MiB cache, non-mmap | 27 | Q36-16 |
| config 1.3: 30 GPU layers, CPU34, b512/u128, non-mmap | 31 (replayed byte-identically) | Q36-05, Q36-17 |
| mapped64: all layers GPU, CPU37, b512/u128, mmap | 31 | Q36-22 |

- Replaying a profile reproduced the answer byte for byte. Changing placement or
  batching changed the answer and moved the total by up to 6 points.
- One run per profile is one sample. A 3-point gap between quants on different
  profiles (Q5 28 against Q4 31) cannot be read as a precision effect.
- A fair precision or engine comparison keeps everything else matched, as Q36-14,
  Q36-15/18 and Q36-22/23 did, and needs seeds 74 and 75 before a decision. None of
  the near-finalists has those seeds yet.

## 4. Engines

### 4.1 llama.cpp builds

| Build | Identity | Used for | State on 3 Nov |
|---|---|---|---|
| b11562 stock | release b11562, commit b2f036c0f, Windows CUDA 12.4 archive (sha e06a4659…) | 13-15 Oct Qwen3.6, Qwen3.8, GLM, Gemma, Kimi and Coder runs; production configs up to 2.0 | installed as the reference |
| b11562-noprefetch-v1 | b11562 + the lab loader patch; llama.dll sha 7bf9b3b0… | production 2.1-2.3; most experiments from 16 Oct (58 of 67 audited mmap loads), including Q36-22 and Groot | installed; the production runtime |
| b11669 (v0.7.0) | commit 620d2225; archive sha c2da1f73… | LFM2.5 (LFM-1); refused Bonsai PQ2_0 (BON-1); planned for Nemotron Bolt | installed. It lies in the CUDA corruption range b11632-b11995 for speculative decoding that mixes draft types, fixed in b11996 (DR section 1.4): avoid it for that use |
| b11838 | commit 4231b23dc, CUDA 12.4; native Flint support | Flint IQ3_XXS (FLT-01 to FLT-07) | installed |
| b11838-noprefetch-v1 | b11838 + loader-b11838.patch; llama.dll sha 10331e86… | Flint Q4_K_XL and Q3_K_XL (FLT-08 to FLT-18); planned for K2 | installed |
| Prism b10787 | PrismML fork 73bfe6cc with ternary PQ2_0/PTQ1_0 kernels | Bonsai 2 (BON-2, BON-3) | removed 3 Nov 19:12; release archive kept |
| llama.cpp-tq3 | TurboQuant fork, local build ([build receipt](../../../reports/2026-10-19-tq3-build.json)) | Qwen3.8-27B TQ3 (Q38-10 to Q38-12) | removed 3 Nov 19:12; rebuildable |
| b12069 | release of 3 Nov; prefetch-opt-out side build in `C:/llm-staging/build`, llama.dll linked 21:10 | nothing yet | untested: no load, identity or speed check |

Source: `catalog/runtime.json`, SKL/reference/runtime.md, the
[WDDM section](../../memory-and-context.md#vram-allocations-also-consume-windows-commit)
for the 67-load count, and RB section 1.

### 4.2 Our llama.cpp change: initial mmap prefetch opt-out

The only lab change to llama.cpp is a loader patch of about six lines
([experiment notes](../../../experiments/llama-mmap-prefetch/README.md)).
- **What it does:** with the process environment variable
  `LLAMA_LAB_NO_MMAP_PREFETCH=1`, it skips the initial Windows `PrefetchVirtualMemory`
  of a mapped GGUF. Demand paging and weight values are unchanged, and it does not
  make a model fit.
- **Why:** the stock mmap load of the 45.20 GiB Coder-Next exhausted physical memory
  and commit before inference (QCN-2).
- **Validation:** CPU and GPU greedy output on stories260K matches stock (b11562).
  Greedy equality between b11838 stock and the opt-out passed (FLT-07). Neither is
  full equivalence.
- **Guard:** `lab.py` refuses an unrequested variant or a mismatched DLL hash and
  records the switch in each launch receipt.
- **b12069:** the same patch was applied for the side build on 3 November
  (`C:/llm-staging/build/loader-b12069.applied.diff`).

### 4.3 Strata versions

| Version | Identity | Used for | State on 3 Nov |
|---|---|---|---|
| Upstream v0.1.45 | 477ac13c (16 Oct); Windows release archive | Flash-Next IQ3_XXS (QFN-1 to QFN-7); stock refused our Qwen3.6 GGUF (Q36-27) | base of the lab fork |
| Lab fork, `strata-q36` target | v0.1.45 + the commits in 4.4; `E:/llm/Strata-data/build-gpu/strata-q36.exe` | Qwen3.6 Q4 (Q36-28 to Q36-31, Q36-37) | rebuilt 3 Nov at 21:00 (55,913,984 B); the 21 Oct expert-pack build was 55,899,136 B. QUEUE pins the rebuilt binary's sha |
| Engine 0.1.50 (CUDA 13) + frontend v0.2.6 | app release v0.2.6, native build 1aff6d14117b; strata.exe sha 5745022e…; frontend clone 4b9e05a2 (engine CMake 0.1.51), 15-package venv | Flash-Next Q2_0 plans (QFN-8); the Q2 pack was built with this frontend's `iq_pack.py` (QFN-9) | staged 26 Oct, help-verified 27 Oct, never loaded a model; ships no `strata-q36.exe` |
| Upstream v0.2.10 (engine 0.1.56) | ffa80d73, 2 Nov | rebase trial only (ENG-3) | not staged. Its 8 GB start fixes and Windows arena trim are in the generic Flash/DeepSeek path, not in q36 |

Strata is a separate MoE engine with its own CLI, Python frontend and pack format.
Its build tree contains ggml targets; its lineage is otherwise unverified (RB
section 6).

### 4.4 Strata fork changes

All changes are opt-in and Windows-specific unless stated.

| Commit (v0.1.45 base) | Rebased on v0.2.10 | Date | Change | Measured |
|---|---|---|---|---|
| 3e0b27d4 | 5ba0a520 | 18 Oct | Accept Qwen3.6 GGUFs without the optional MTP metadata (`nextn_predict_layers`) | lets our non-MTP GGUF load (Q36-28 to Q36-31) |
| b0513bee | 631f50bb | 18 Oct | `STRATA_Q36_PAGEABLE_EXPERTS`: unpinned expert arena | pageable, but still charged to commit (Q36-29) |
| 6ef632f7 | 7b1ce158 | 18 Oct | `STRATA_Q36_TRIM_GGUF`: trim copied GGUF views | trim-on reached readiness at 32K (54.25 s); trim-off hit the RAM floor (Q36-29). It enabled the 32K comparison (Q36-31) |
| c451fbe8 | acc3d2eb | 21 Oct | `STRATA_Q36_FILE_ARENA`: file-backed expert arena, no commit charge | every expert is still touched at load: RAM fell from 12.92 to 0.36 GiB and the guard stopped it at 35.7 s (Q36-37) |
| b5211998 | cbfbb0c1 | 21 Oct | `STRATA_Q36_EXPERT_PACK`: write a packed expert file once, then map it read-only; requires `--mtp 0` | never run (Q36-40; queue item 2) |
| 28ce3b52 | – | 3 Nov 19:27 | Windows free VRAM = min(cudaMemGetInfo, NVML), with the DXGI rule as fallback; `STRATA_WDDM_BUDGET` switch; `--vram-report` | ENG-2: 6003 MiB instead of 9097; 3765 with a 2048 MiB holder |
| 1beb824e | – | 3 Nov 21:01 | Read `STRATA_WDDM_BUDGET` words in any case and log unknown values | ENG-5: "=NVML" now gives 6594 MiB instead of silently 9097 |

**Branches.** These were judged from local refs only.
- `experiment/qwen36-no-mtp`: the three 18 Oct code commits plus two documentation
  commits. Published to the lab fork remote.
- `experiment/win-arena-mmap`: adds c451fbe8 and b5211998. Local only.
- `experiment/win-vram-budget`: adds the two 3 Nov commits. Local only; the current
  HEAD.
- `rebase-trial/v0210`: the five code commits rebased onto v0.2.10. Builds and its
  tests pass (ENG-3). Local only.

Pushing or sharing any local branch is an owner decision (RB D1).

### 4.5 Engine comparisons that were measured

**Strata against llama.cpp, same Qwen Q4 weights, 32K, one sample each** (Q36-31
against Q36-32, old40 scale):

| Workflow | Strata | llama.cpp | Ratio |
|---|---|---|---|
| Router | 286.516 s, 40/40 | 436.469 s, 40/40 | 1.52× |
| History | 250.625 s, 6/6 facts | 285.891 s, 6/6 | 1.14× |
| TS/SQL | 203.765 s, T 5/6, SQLite migration fails | 357.687 s, T 5/6, S 6/6 | 1.76× |

Strata copied every expert into a host arena. Its peak working set was 20.09 GiB,
with 2.62 GiB free at minimum; llama.cpp kept at least 6.28 GiB free. That is why
Strata needs an apps-closed window until the expert pack is proven.

**Other measurements**
- **Flash-Next on Strata v0.1.45** fits the 10 GB card. But four coding attempts
  across three profiles reached 1200 s, at 5.1-9.6 tok/s. The 128K RAM-backed history
  returned an empty final answer, and separate replays recovered 6/6 facts (QFN-2 to
  QFN-6).
- **TurboQuant** dense TQ3 ran at 1.494-1.939 tok/s; its coding run ended in a PC
  reset (Q38-10 to Q38-12).

## 5. Memory model of this PC

### 5.1 Hardware

- **GPU:** RTX 3080 10 GB. Driver 617.42 through 21 October, 621.01 from 23 October,
  so timing comparisons across the two are observational.
- **CPU:** Ryzen 7 5800X with PBO. Core 0 has been excluded from inference threads
  since 20 October, after core-0 machine checks on 12 and 19 October. The exclusion is
  a precaution, not a diagnosis.
- **RAM:** 4×16 GB DDR4 of mixed modules at 3000 MT/s; 63.91 GiB is usable.
- **Storage:** models on E: (WD SN770); a system-managed page file on C:.
- Source: SKL/reference/hardware.md.

### 5.2 Three separate budgets

Every load must pass RAM, commit and VRAM gates independently.
- **Admission gates** are set per profile (section 1.2).
- **Runtime stop floors** are 2.5 GiB available RAM, 1 GiB available commit, 400 MiB
  free VRAM and 84 C on the GPU. They protect the owner's applications, not the
  model. A capacity rejection or floor stop is a host disposition, not a quality
  result.

### 5.3 WDDM: VRAM also costs commit

Under WDDM, a CUDA allocation raises system commit by about its own size, while the
process working set barely moves.
- **Saved loads:** across 67 mmap loads on four llama.cpp builds and 13 GGUF files,
  process commit divided by VRAM growth has a median of 1.038 (IQR 1.029-1.072; 59
  of 67 within 0.95-1.15).
- **Direct probe:** holding 1 GiB raised commit by 1.379 GiB for 1210 MiB of device
  use, and freeing it released the charge (ENG-1).
- **Relocation control:** moving 1.1 GiB of KV between RAM and VRAM left commit
  unchanged (16 Oct, 128K).
- Sources: [memory-and-context.md](../../memory-and-context.md#vram-allocations-also-consume-windows-commit);
  LD/2026-11-03-wddm-commit/analysis.json.

| Bytes | Commit | Resident RAM |
|---|---|---|
| CUDA0 buffers: weights, KV, recurrent state, compute | about their size | about 0 |
| mmap'd CPU weights (`CPU_Mapped`) | 0 | touched pages only; discardable |
| Read-write file-backed arena (Strata `FILE_ARENA`) | 0 | dirty pages until written back |
| Pinned host buffers (`CUDA_Host`; Strata's default arena) | their size | their size, page-locked |
| Pageable private memory (CPU KV, malloc arena) | their size | touched pages |
| llama.cpp CUDA runtime outside the logged buffers | 1.2-1.5 GiB | not separated |

Consequences:
- **GPU placement is paid twice.** Moving expert blocks to the GPU saves RAM but
  costs the same commit (Q36-35: +4.38 GiB commit for +4.22 GiB of VRAM).
- **The old non-mapped Q4 launcher held about 24 GiB of commit**; mapped Q4 and IQ4
  profiles hold 5.4-6.5 GiB, mostly charged for VRAM.
- **Server commit after a load** is about the sum of CUDA0 buffers plus non-mapped
  host buffers plus about 1.3 GiB. A sound commit gate is that sum plus the 1 GiB
  floor plus a desktop margin.
- **Both commit-floor stops that were examined came from other processes growing
  after the load:** 5.1 GiB in 17 s on 21 October, and 5.3 GiB in an hour on
  26 October.

### 5.4 cudaMemGetInfo over-reports free VRAM

Under WDDM, `cudaMemGetInfo` returns the process's own DXGI budget minus its own use.
It ignores the desktop and other processes (ENG-2):
- A fresh process saw 9097 MiB free of 10239 while nvidia-smi showed 6050 MiB free.
- With another process holding 2048 MiB, it still saw 9097 MiB. NVML fell to 3765
  MiB, and upstream Strata's DXGI rule gave 8142 MiB.

Consequences:
- **Engines that size buffers from cudaMemGetInfo can oversubscribe the desktop's
  GPU.** Examples are Strata q36 `place_experts` (free minus 768 MiB), the upstream
  0.1.50 automatic expert cache and llama.cpp `--fit`. WDDM then demotes memory to
  shared system RAM.
- **An external VRAM holder does not simulate an 8 GB card** for such engines.
- **The fork now uses NVML** (28ce3b52, 1beb824e). The upstream 0.1.50 engine staged
  for Flash-Next Q2_0 does not, which is one reason its qualification is still
  blocked.
- **Per-process GPU memory counters are not reliable here.** On 27 October they
  exceeded the device's whole capacity; use device-wide telemetry and engine buffer
  logs instead.

### 5.5 The commit limit moves, and the apps-open budget is small

The page file is system-managed, so the commit limit grows late and in steps:
- **Commit limit:** 84.91 GiB (15 Oct), 89.91 (21 Oct), 91.91 (24 Oct), 106.33
  (26-27 Oct), 109.32 (3 Nov 18:55), 110.33 (19:16), 115.36 GiB (21:08).
- **Plan from fresh available commit,** never from a peak or an old limit. A higher
  limit is not more RAM, and its growth consumes C: disk.
- **Apps-open RAM** ranged from 2.2 to 13.7 GiB available on 3 November alone
  (section 1.2). The owner's applications typically hold 45-56 GB.
- **A 20 GB model paged under that load:** on 20 October, Qwen Q4 with a 19.07 GiB
  working set slowed to 0.3-2 tok/s before the RAM floor stopped it (Q36-33).
- **Working-set caps** turn an overrun into soft-fault churn. Groot logged about 27.1
  million page faults at 2.33 tok/s (GRT-2). A cap bounds neither commit nor the
  standby file cache.

### 5.6 Model-specific memory facts

| Item | Measured value | Source |
|---|---|---|
| Qwen3.6 q8 KV | 680 MiB at 64K, 1360 MiB at 128K, plus 62.81 MiB recurrent state | Q36-21; Groot record |
| Flint q8 GPU KV | 979.89 MiB at 64K; 503.89 MiB at 32K | FLR; memory-and-context.md |
| Groot Q4 host experts | 8,205 MiB inside a 10,054 MiB `CPU_Mapped` buffer at CPU36 | Groot record |
| Strata Qwen Q4 expert arena | 18.23 GiB | Q36-37 |
| Flash-Next Q2_0 pack | 1.38 GiB dense arena; 31.6 GiB of mapped experts | Q2 pack receipt |
| Gemma 31B private run | 10.02 GiB private commit, of which about 5.41 GiB was CUDA0 buffers and 3.18 GiB CPU KV | memory-and-context.md |

### 5.7 Not established

- A cudaMalloc/cudaFree probe instrumented with VirtualQuery. The simple 19:04
  hold-and-release probe (ENG-1) is not that test.
- Commit accounting for desktop D3D and browser GPU allocations.
- The TCC driver model.
- What triggered the persistent page-file growth of 25-26 October.

## 6. Failures and why

### 6.1 Failure classes

| Class | Rows | Main cause |
|---|---|---|
| Missed 1200 s with no finished answer | Q36-02, Q36-50, Q36-52, Q36-53, Q36-47 (coding), Q38-9, QC30-1 (private), BON-3, FLT-02, FLT-03, FLT-09, FLT-10, QFN-2, QFN-3, LFM-1 (private) | Slow decode from CPU-resident or paged experts, and long reasoning before any visible text. Flint wrote 50,287 reasoning characters and no final (FLT-02) |
| Finished, but over the deadline | G31-2 (26/36 in 7234 s), Q36-23 (28/36 in 2099.7 s), QCN-4 (4075 s, unscored) | Dense or 6-bit weights on this card; measured but not rankable |
| RAM-floor stops | Q36-08 (2048), Q36-09, Q36-28, Q36-29, Q36-33, Q36-34, Q36-37, Q36-46, QCN-3 (history attempt 1), GRT-1, GRT-2, FLT-18 | The model and the desktop shared too little RAM; a working-set cap does not prevent it |
| Commit-floor stops | G26-12, Q36-35 (b) | GPU buffers charge commit; in both examined cases other processes then grew |
| VRAM floor or unreadable telemetry | G31-1 (a), G31-3 (c), Q36-30, Q38-7, Q36-39 | Q36-39 was a fail-closed nvidia-smi read under RAM pressure; VRAM never fell below 1,152 MiB |
| Capacity rejections before loading | QN80-1, Q38-3, KIM-2, QCN-1, QCN-2, Q36-12 (f), Q36-19, Q36-35 (a), Q36-36 (a), Q36-38, Q36-51, Q36-54, G26-5, G26-10 ×3, GLM-4 attempt 1, QFN-1, QFN-4, FLT-08, FLT-11, FLT-13 ×2, K2-1 | Admission gates; a host disposition, not a quality result |
| Output, tool-round and reasoning limits | Q36-42 (two 16K reasoning-only coding answers), Q36-48, FLT-04 (TS/SQL tool turns, 4096-output history, CSV at 16K), FLT-15 (16K limits, 8 unavailable reads), G26-6 (4096-token reasoning-only history), GLM-1 (16,384 reasoning tokens, no answer), QCN-4 (16 tool rounds, 15 failed reads), QFN-5 (empty final) | Over-deliberation fills the allowance before a visible answer; tool loops on unavailable paths |
| Reasoning loop | LFM-1 (private) | Repetition at temperature 0.1 with repeat penalty 1.0 |
| Hardware and OS events | QN80-2 (0x124/0x3B), Q38-2 (12 Oct 19:03 restart), Q36-10 (planned Windows Update), GLM-4 attempt 2 (15 Oct unclean shutdown), Q38-12 (19 Oct reset, core-0 machine check) | Core 0 is marginal under CPU-heavy load (12 and 19 Oct records). The 15 Oct cause is not established. Nothing since the 23 Oct boot |
| Engine or format compatibility | BON-1 (ggml type 142 on mainline), Q36-27 (missing MTP metadata on Strata), KIM-1 (q8 K/V rejected) | Fixed by a fork (Prism, the Strata patch) or another KV type |
| Harness or operator | Q36-01 (rename error), BON-2 (manual stop), G26-8 and Q36-43 (deliberate), Q38-4 (placement change), G26-11 (calibration) | – |

### 6.2 Why workflows miss 1200 s: decode rates

| Profile | Decode tok/s | Row |
|---|---|---|
| Qwen3.6 Q4, all experts on CPU + 3072 MiB cache | 46.71 | Q36-12 (c) |
| Qwen3.6 Q4 cache2048 finalist | about 41 | Q36-16 |
| Qwen3.6 IQ3_S + 1536 MiB cache, 4096 cap | 31-37 | Q36-44 |
| Qwen3.6 Q4, all experts on CPU, no cache | 22.78 | Q36-12 (a) |
| Flint IQ3_XXS, GPU KV (history 8192) | 22.1 | FLT-06 |
| Qwen3.6 IQ3_S CPU38, native | 15.66 | Q36-42 |
| Qwen3.6 Q4, 30 GPU layers + 33 CPU-expert blocks | 13.34 | Q36-07 |
| Bonsai PTQ1, full GPU | 13.1 | BON-3 |
| Flash-Next on Strata | 5.1-9.6 | QFN-2, QFN-3 |
| Qwen3.6 Q4 resident7, 32K | 6.69 | Q36-50 |
| Flint Q3_K_XL, bounded residency | 2.1-4.3 | FLT-15 to FLT-17 |
| Groot Q4 with a 3.31 GiB cap | 2.33 | GRT-2 |
| Bonsai PQ2 with 12 CPU layers | 2.3-2.7 | BON-2 |
| Qwen3.8-27B dense | about 0.65 at long context to 2.1 | Q38-9, Q38-10, Q38-11 |
| Gemma 4 31B dense | 0.95-1.17 | G31-1, G31-2 |
| Qwen3.6 Q4 under thrash | 0.3-2 | Q36-33 |

At 2.33 tok/s, 1200 s allows about 2,800 output tokens for a whole workflow before
any prefill (Groot record, an estimate). Profiles below about 10 tok/s have not
finished a frozen tool workflow here.

### 6.3 Re-prefill is not the cause for Qwen3.6

The read-only audit covered 120 server logs and 561 continuation turns (ENG-4;
[RPA](../../../reports/2026-11-03-reprefill-audit.json)).
- **Forced full re-processing on a continuation turn happened once:** Gemma 4 31B,
  9,778 tokens and 512.7 s. Its template dropped the earlier reasoning, and it ran
  with a single checkpoint.
- **Qwen3.6 never re-prefilled.** 222 of 224 continuation turns reused the whole
  previous KV, and the two partial turns lost 19.4 s in total. The 700-860 s
  private-audit times are new tool-result prefill plus decode.
- **Editor traffic is where re-prefills cost time:** four same-prefix divergences
  re-processed 56,155 tokens in 578.3 s, 8.3% of audited editor prefill.
- **The audit's proposals are estimates, not measurements:** `--ctx-checkpoints 16`
  for the editor profile (about 62.8 MiB RAM per checkpoint) and `--cache-ram 2048`.

### 6.4 Completed but wrong: recurring quality defects

These are measured answer defects, not reliability failures:
- **SQLite foreign-key migration.**
  - Failed: Q36-22, Q36-42 and G26-6 (all 0/6), and the old-scale runs Q36-11,
    Q36-13, Q36-16, Q36-17, Q36-18, Q36-23, QCN-3, QC30-1, G26-1 and GLM-4.
  - Passed fully only in G26-4 (old), G26-7 (6/6) and the llama.cpp control Q36-32
    (old40). IQ4_XS scored 3/6 (Q36-47).
- **Strict TypeScript validation.** 5/6 is typical. There were compile failures in
  G26-1, GLM-1, GLM-5, Q36-13 and Q36-16.
- **Private-audit instruction fidelity.** Omissions, unsupported citations and wrong
  fact ownership (G26-7, FLT-04, Q36-47).
- **Post-review diagnostics outside the frozen scores:**
  - NaN TTL accepted (Flint, Gemma, IQ3_S).
  - JavaScript scheduling and array-to-object replacement bugs (Q36-49).
  - A mutable-default alias (Q36-42).

## 7. What remains untested, and the recommended next experiments

### 7.1 Untested

- **Coverage gaps**
  - Any complete three-suite composite. The leader's coding suite was never
    collected on mapped64.
  - Seeds 74 and 75, and a held-out task, for any near-finalist.
  - Any quality score for the production 128K CPU-KV profile.
  - Editor UI checks for any new candidate since 15 October.
- **Speed and runtime**
  - Speculative decoding on Qwen3.6 or Groot (draft, ngram, MTP).
  - llama.cpp b12069.
  - The knobs never measured: `--fit`, a thread sweep, a core-0 pinning A/B, and
    the expert-cache hit rate.
  - ik_llama.cpp and KTransformers.
- **Strata:** the expert pack (b5211998); any load on engine 0.1.50 or upstream
  0.2.10; 128K serving.
- **Candidates never loaded or retired early:** K2 MoVA, Nemotron Bolt, Flint NVFP4,
  dense Qwen3.8-27B Q4/IQ4_XS on a current build, Flash-Next Q2_0 (now packed),
  Ornith-1.5, Logics-SWE, ToolSpace, and the apps-open small models (Dory-4B,
  Qwen3.5-9B).
- **Memory facts:** see 5.7.

### 7.2 Ranked next experiments

The ranking is Claude's recommendation from the evidence above. Speed experiments
are diagnostics: their answers must stay identical, and they never add a quality
score.

| Rank | Experiment | Why | Needs now | Cohort and rule | Source |
|---|---|---|---|---|---|
| 1 | Coding /12 on the leader (Qwen3.6 Q4, `qwen36-q4-noprefetch64-control`) | The leader lacks its third suite, so no complete composite exists anywhere. A prerequisite for any promotion | Profile gates of 16 GiB RAM / 10 GiB commit / 6,000-6,500 MiB VRAM fail at 13.6 GiB, so an apps-closed window | frozen; hard-deadline collector, source review, then WSL grading | SKL/reference/candidates.md; RB B6 |
| 2 | b12069 side build against b11562 on the same weights | Small expected gains plus fixes (mixed-draft corruption fix, partial whitespace fix). The build exists | Same window and gates as rank 1 | Temperature-0 token identity first, then one private and one public run for wall time | DR rank 3; Q36-57 |
| 3 | Speculative decoding on the leader: ngram-simple, then the 0.8B draft | Faster decode buys headroom under 1200 s without changing outputs. Ngram needs no weights; the draft is downloaded | Both profiles are proposed but unmeasured. Confirm the launcher adds the core-0 mask and the prefetch-opt-out runtime; re-hash the moved draft; gates 16-17 / 10 / 6,500 | diagnostic; token identity at temperature 0, then wall time; scores must not change | DR ranks 5-6; Q36-55, Q36-56 |
| 4 | Groot-19B-A3B Q4, apps-closed full suites | The only installed new same-architecture derivative; the publisher claims shorter output | At least 14 GiB RAM, 8 GiB commit and 5,500 MiB VRAM; floor at least 2.0 GiB, lab default 2.5 | frozen; keep only if private ≥ 29/36 with no strict TS or SQLite regression | Groot record |
| 5 | Flint Q3_K_XL private audit at 72K, no context shift | Completes Flint's extended evidence (router 38/40 at a 1024 cap) | Gates 7.5-10.5 / 8.5 / 5,500-6,000; passed in the 21:08 dry run | extended only; never ranked | QUEUE item 1; FLT-19 |
| 6 | Strata expert pack on Qwen Q4 | Tests whether Strata's speed can come without its 25 GiB RAM copy | Gates 10 / 10 / 6,400 (passed at 21:08); at least 21 GiB free on C: for the first pack write | diagnostic; output equality against the pageable path; record pack write time, RSS and commit per phase | QUEUE item 2; Q36-40 |
| 7 | Editor-profile re-prefill change: `--ctx-checkpoints 16`, optionally `--cache-ram 2048` | The audit estimates up to 578 s saved across four editor events | A production restore window; about 1 GiB more host RAM for 16 checkpoints | editor latency diagnostic; no quality change expected | ENG-4 |
| 8 | Flash-Next Q2_0 mmap32 qualification | Downloaded and packed; a capacity and control candidate, not a quality upgrade | Template rendering check; a reviewed fix for 0.1.50's cudaMemGetInfo cache sizing; provisional gates 12 / 14 / 7,000 fail with apps open | extended unless a prompt finishes in 1200 s | QFN-9; QUEUE item 5 |
| 9 | Ornith-1.5-35B-A3B Q4_K_M | Largest vendor coding claim among drop-in Qwen3.6 derivatives (vendor numbers only) | 21.86 GB download, but E: has 6.9 GB free; apps-closed window | frozen A/B against Q4 with only the weights and template changed | DR rank 4 |
| 10 | K2 MoVA resident4/6 | Downloaded, never loaded | About 22.4 GB on E: to move it back, a fresh full SHA256, then 10.5-12.5 GiB RAM | per profile (extended32 profiles are extended) | K2-1 |
| 11 | Dense Qwen3.8-27B Q4 on a current build | The tested dense profiles ran at 1.4-2.1 tok/s | 16.46 GB download | extended only | Q38-13 |
| 12 | Apps-open small models (Dory-4B, Qwen3.5-9B) | A fit test only: their vendor numbers sit below Qwen3.6 | Downloads in progress | frozen | DR section 1.1; NR-5 |
| 13 | Offline fusion probe with Qwen3.5-4B | Published results show no reliable code gain from fusion | 2.74 GB download | offline only; probably no-go | DR rank 11; NR-4 |

**Cheap checks to add inside the rank 1-3 window:**
- a thread sweep (4/8 against 6/12, core 0 still excluded);
- `--fit on` against off;
- `GGML_OP_OFFLOAD_MIN_BATCH=64`;
- `--moe-cache-mib` 1536 on mapped64, with a clean shutdown so the hit-rate counters
  print;
- seeds 74 and 75 for the leader's private audit.

A core-0 pinning A/B needs the owner's approval because of the machine-check
history, and it must stop on any new WHEA event.

**Operational, not an experiment.** Restore the production endpoint when its
18 / 12 / 6,000 gates pass; that needs the owner's confirmation (QUEUE item 6).

### 7.3 Owner decisions that unblock the most

1. **An apps-closed window** (close Edge, the emulator, the VM and Gradle, or
   reboot). Ranks 1-4 and the production restore all need it.
2. **Disk on E:** only 6.9 GB is free. Ornith, an MTP GGUF and moving K2 back each
   need 15-23 GB. Choose a reviewed file to retire or move, such as the Flash-Next
   Q2_0 shards after their qualification or Flint Q3_K_XL after rank 5.
3. **Whether to share the Strata fork commits**, and whether to adopt upstream Strata
   v0.2.10.

## 8. Source index

### 8.1 In this repository

- **Comparison and rules:** [model-comparison.md](../../model-comparison.md),
  [model-reporting.md](../../model-reporting.md),
  [memory-and-context.md](../../memory-and-context.md),
  [grading.md](../../grading.md), [methodology.md](../../methodology.md).
- **Per-model records:**
  - [Qwen3.6](../2026-10-24-qwen-coverage/2026-10-24-qwen36-v0.9.0.md)
  - [Recursive Flint](../2026-10-23-flint/2026-10-23-recursive-flint-v0.8.0.md)
  - [Gemma 4 26B](../2026-10-24-gemma26-coverage/2026-10-24-gemma26-v0.9.0.md)
  - [K2 MoVA](../2026-10-24-k2-mova/2026-10-24-k2-mova-v0.9.0.md)
  - [Flash-Next](../2026-10-26-flash-next/2026-10-26-flash-next-v0.10.0.md)
  - [Qwen3.8 dense](../2026-10-26-qwen38-dense/2026-10-26-qwen38-dense-v0.10.0.md)
  - [LFM2.5](../2026-10-20-lfm25/2026-10-20-lfm25-24b-a2b-qad-q4-v0.10.0.md)
  - [Bonsai 2](../2026-10-20-bonsai2/2026-10-20-ternary-bonsai2-27b-pq2-ptq1-v0.10.0.md)
  - [Groot](../2026-11-03-groot/2026-11-03-groot-19b-a3b-apps-open-v1.0.md)
- **Campaign and engine records:**
  - [15 Oct campaign](../2026-10-15-autonomous-model-campaign/2026-10-15-model-comparison-and-editor-validation-v0.3.9.md)
  - [16 Oct expansion](../2026-10-16-memory-and-candidate-expansion/2026-10-16-memory-context-and-expanded-model-tests-v0.4.0.md)
  - [17 Oct inventory](../2026-10-17-complete-model-inventory/2026-10-17-all-models-gemini-and-availability-v0.4.1.md)
  - [128K and tool budget](../2026-10-17-context128-and-tool-budget/2026-10-17-context128-and-tool-budget-v0.4.2.md)
  - [Strata](../2026-10-18-strata/2026-10-18-strata-on-10gb-v0.6.0.md)
  - [TurboQuant](../2026-10-19-azllm/2026-10-19-azllm-and-turboquant-v0.7.0.md)
  - [precision and coverage](../2026-10-24-precision-and-gaps/2026-10-24-precision-and-coverage-v0.9.0.md)
  - [3 Nov deep research](../2026-11-03-deep-research/2026-11-03-deep-research-v1.0.md)
- **Reports cited most:**
  - [15 Oct campaign](../../../reports/2026-10-15-campaign.md)
  - [private results](../../../reports/2026-10-15-private-results.json)
  - [cache results](../../../reports/2026-10-15-cache-results.json)
  - [placement results](../../../reports/2026-10-14-placement-results.json)
  - [Qwen precision](../../../reports/2026-10-17-qwen-precision.json)
  - [Strata Qwen](../../../reports/2026-10-18-strata-qwen.json)
  - [Strata Flash](../../../reports/2026-10-18-strata-flash.json)
  - [Flint run C grades](../../../reports/2026-11-03-flint-runC-grades.json)
  - [re-prefill audit](../../../reports/2026-11-03-reprefill-audit.json)
  - [Q2 pack receipt](../../../reports/2026-11-03-flash-next-q2-pack.json)
  - [resume capacity](../../../reports/2026-10-26-resume-capacity.json)
- **Engine changes:** [prefetch opt-out](../../../experiments/llama-mmap-prefetch/README.md);
  `catalog/runtime.json`; `catalog/models.json`; `profiles/`.

### 8.2 Private sources outside Git

- **Scorecard:** LB (64 runs), SKL/reference/evaluation.md, runtime.md,
  hardware.md and candidates.md.
- **Recovery brief and parent logs:** RB; DT; INSTALL; MIG.
- **Raw benchmark folders:** BEN and RUNS.
- **Ignored lab evidence:**
  - `LD/2026-11-03-wddm-commit/`
  - `LD/2026-10-21-strata-8gb/`
  - `LD/2026-11-03-campaign/`
  - `LD/2026-11-03-queue/`
  - `LD/2026-11-03-campaign-audit/`
- **Engine trees and staging:** the Strata repositories `E:/llm/Strata` and
  `E:/llm/Strata-20261026`; the Flash-Next receipt
  `E:/llm/Strata-data/models/flash-next/verified-download.json`; and
  `C:/llm-staging/build`, `logs` and `parked`.

### 8.3 Leaderboard gaps and corrections to make

- **76 reconciled rows have no leaderboard entry.** Four graded frozen private audits
  could be added: Q36-15 (25/36 ×2), GLM-2 (21/36), GLM-4 (21/36) and G26-2 (19/36).
- **Existing rows lack parts:**
  - `lfm25-qad-q4-20261020` should carry R37 H7 T4 S0.
  - `h-kimi-linear-20261015` lacks the public run (KIM-1).
  - `h-qwencoder30-20261015` stores no values.
  - The `h-gemma31-dense`, `h-qwen36-q6`, `h-codernext80`, `h-glm47-*` and
    `h-qwen36-q4-cache2048` rows lack old-scale public parts.
  - `h-qwen36-q4-t06` has no record of Q36-17's public results.
- **Value corrections:** K3 (Bonsai PQ2 wall 82.391 s), K7 (the Qwen3.8 Q6 audit
  decoded at about 0.65 tok/s), K8 (Q2_0 downloaded and packed) and K13 (IQ4_XS
  preflight 12.25-12.35 GiB).
- **A cohort rule for cache-bearing profiles** (K10).

## Appendix A. Owner request (verbatim, 3 November)

> do whats next. i need full summary of current models tried since startingf, their
> combnination, extra tuning tha tyou want to try (try that) and then get back. do
> whatever it needs to, do in different subagents, i already told you.
>
> and kep traccking
