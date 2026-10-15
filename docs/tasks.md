# Task log — Local Coding Lab

Last updated: 2026-10-15 (Asia/Kolkata).

## 2026-10-15 — Autonomous research campaign

Owner explicitly authorized downloads, rigorous testing, reports and selected
model deletion. Continue across candidates without asking for another prompt.
Apps remain open; keep the 1200-second prompt limit and resource/error guards.
Use resumable on-disk state and preserve failed attempts rather than restarting
them blindly after interruption.

- 15:17 IST recovery: new boot at 14:58:04 follows an unexpected shutdown;
  last heartbeat 10:24:01 during GLM Q5 private audit. No new dump/WHEA/GPU
  error or planned-restart event identifies the cause. Marked that audit
  interrupted/unscored; all successors were unstarted. GLM Q6 download was
  incomplete (directory size alone did not establish retained bytes).
  Preserved external report, heartbeat and raw event XML privately.
  Added commit telemetry and started a short monitored Gemma recovery check.
- Recovered 10:19 checkpoint: private totals Gemma 19/36, GLM Q4 21/36;
  Coder private audit hit 1200 seconds without a final answer. Its completed
  public grades and exact-file retirement evidence remain intact. No editor
  promotion, new cloud calls, clock changes or application closures occurred.

| Candidate | Status | Required disposition |
|---|---|---|
| Qwen3.6 Q4 | Core/history/held-out and initial flag probes collected | Private capped 25/36; batch/cache/CPU-KV code and recall pass; lower-temperature TS/SQL fail; matched Q4 control complete, larger-cache probes pending |
| Gemma 4 26B QAT | 32K/64K suites and both private audits reviewed | 52K-input recall passes; unrestricted SQL 6/6, TS 5/6; capped/unrestricted private scores both 19/36 |
| GLM-4.7-Flash UD-Q4 | q8 and f16 public follow-ups reviewed | f16 native code6/6; original own script runs zero tests, supplemental13/14; history count wrong; conditional f16 private audit pending |
| Qwen3-Coder 30B UD-Q4 | Five tasks graded | Core 2/6, 3/6, 1/6; private audit 20-minute deadline; exact weight retired with evidence |
| Gemma 4 31B QAT dense | Calibration rejected | GPU-KV resource stop; CPU-KV 0.95 tok/s and five-minute deadline; quality unscored |
| Qwen3.6 Q5 and optional Q6 | Q5 public suite complete; Q6 conditional | Q5 matched core6/6 each but19.1% slower, held-out TS4/6/SQL failure; native private pending. Q6 requires fresh28.5GiB/7000MiB gates and full verified artifact |
| GLM Flash Q5 and optional UD-Q6 | Q5 suite graded; Q6 download verified | Q5 bounded core 5/6, 0/6, 0/6; unrestricted 6/6; follow-ups/private retry and Q6 inference queued |
| Kimi Linear 48B Q4 | Conditional profile | Runtime/header reviewed; fresh 26 GiB RAM and disk gates required, no score |
| Qwen Coder Next 80B Q4 | Current capacity rejected | 45+ GiB weights exceed apps-open resident allowance, no quality score |
| Research's explicitly excluded giant models | Capacity review complete | Publisher metadata pinned; four-bit payload arithmetic excludes them from the current apps-open matrix, no local score |

Initial free memory: 25.62 GiB RAM / 7114 MiB VRAM; 85.0 GiB free disk.
Original Qwen Q4 and retired Qwen Q8 archive still present. No server running.
Pinned publisher metadata rechecked before new downloads. No user applications
closed and no clock/driver changes.

- 01:05 IST: three additional Qwen core runs completed in 240.187, 237.640 and
  325.204 seconds. Independent Python checks passed 6/6 on every implementation.
- 01:15 IST: history task passed the six factual/current-file checks in 134.172
  seconds. Held-out TypeScript/SQLite completed but produced a nonplain-object
  validation bug and a broken migration. Unrestricted-thinking retry started.
- 01:17 IST: frozen extended ledger has 21,461 Qwen tokens before chat overhead.
  Added isolated TS/SQLite grading; positive and negative controls behaved as
  expected. No generated code executed on Windows. Live campaign evidence is
  maintained in [the campaign report](../reports/2026-10-15-campaign.md).
- 06:45 IST recovery: Windows Update initiated planned restarts at 01:29:38
  and 01:33:59; no new hardware-crash evidence in that window. Preserved the
  interrupted Qwen larger-batch attempt as unscored, resumed partial downloads.
- 06:53 IST: dense Gemma GPU-KV reached the VRAM guard; RAM-KV loaded and
  passed smoke. Current unloaded RAM fluctuates around 15–19 GiB. No user
  applications closed, update-policy changes, hardware tuning or cloud calls.
- 06:58 IST: dense CPU-KV calibration cancelled at 300.016 seconds with 259
  generated tokens, 0.95 tok/s. Peak sampled RAM 14.57 GiB; no resource stop in
  this attempt. Gemma 26B trial queued behind its verified download; GLM and
  Qwen Coder downloads queued sequentially. Published 067f6dd passes both CI OSes.
- 07:04 IST: Gemma 26B verified, loaded and passed smoke; actual routed file
  calls are being collected. Preserved and deleted the rejected dense model's
  exact verified weight file, retaining the Qwen baseline. Added portable task
  plans and froze a 43,228-token Gemma ledger for the later 64K profile.

- Continued checkpoint: Gemma's three bounded core repeats and unrestricted
  core all pass 6/6 independent Python groups. Generated-test packaging and
  coverage limitations retained. The 120-record history case passes all six
  factual/current-file checks; no failed-ledger recovery was exercised. GLM Q4
  verified and queued behind this single owned Gemma server.
- Gemma's seven-task 32K suite is now collected and reviewed, with normal owned
  shutdown. Its TypeScript fails strict compilation and SQLite fails migration;
  the temperature-1.0 core passes Python checks but introduces a wrong exception
  claim. GLM Q4 loaded successfully; first core is 1/6 independent Python groups
  and 2/14 generated tests. Qwen Coder, matched GLM Q5 and conditional precision
  downloads remain queued. Larger-history/private audits and editor checks are
  still required. Recorded apps-open resident-capacity exclusions separately.
- Verified and deleted only the retired Qwen3.8 Q8 weight archive, reclaiming
  27.052 GiB. Raw historical evidence and the Qwen3.6 baseline remain intact.
- GLM's three bounded core repeats pass 1/6, 5/6 and 2/6 independent Python
  groups. Its unrestricted repeat exhausted 16,384 output tokens without a final
  answer in 988.563 seconds, unscored. The short history case passes six checks
  in 259.859 seconds. Qwen Coder is verified; the first-load proposal moves two
  more expert blocks to RAM to accommodate current desktop VRAM use. The frozen
  actual-instruction audit is queued after Gemma's larger-history follow-up.
- Corrected commented-transaction detection and isolated SQL constraint checks
  from preservation failures. Reran all four completed migrations and both
  controls in the sandbox, preserving originals. GLM's corrected SQL count is
  4/6 with destructive data loss and altered deletion behavior still failing.
  Twenty offline tests, PowerShell parsing and the 92-file public audit pass.
- Qwen Coder completed five tasks with normal shutdown and 5.80 GiB dedicated
  VRAM. Core responses skip linked rules/contract and retain code bugs; one
  falsely claims test execution. Reviewed code is queued for grading between
  timed model runs. GLM Q5 is verified/loaded at 5.57 GiB dedicated VRAM with
  matched 32K placement. Private audits, matched Qwen precision and GLM f16
  cache tests are queued. Kimi's earlier capacity exclusion is reconsidered
  against improved unloaded memory; a fresh gate and disk space remain required.
- 09:18 IST checkpoint: GLM Q5's seven tasks are collected/reviewed, with normal
  shutdown, 16.32 GiB peak sampled RAM and 5.57 GiB readiness dedicated VRAM.
  Its unrestricted Python answer is promising but awaits grading/repeats; bounded
  variants and held-out SQL still contain defects. Gemma's 64K follow-up is
  running. Eleven reviewed answers are queued for grading before the private
  audits. Qwen Q5 is verified; GLM Q6 stopped at its disk gate. Batch512,
  GPU expert-cache, CPU-KV and research-sampling probes are queued sequentially.
- 09:39 IST: Gemma 64K completed both larger-history cases and unrestricted
  held-out work. The 640-record case passes all six final facts and correct
  count at 52,231 maximum input tokens in 631.563 seconds; the 320 case
  miscounts 318 despite correct final facts. Twelve reviewed answers were
  graded in isolation between loads. Gemma's unrestricted SQL passes 6/6 and
  TS 5/6; GLM Q5 unrestricted Python passes 6/6 but bounded repeats vary badly.
  Qwen Coder own-test coverage misses independent failures. Its seed75 test
  file defines tests without invoking them; supplemental runner-only execution
  is queued. Private Gemma audit started; production editor selection unchanged.

## 2026-10-14 — Begin research experiments

| Task | Status | Notes |
|---|---|---|
| Confirm research was read | Done | Archived report hash verified; recommendation, tuning and benchmark sections reread |
| Establish controlled Qwen reference | Done | 576.453 seconds; 39/40 provisional; both code blocks parsed; 6/6 independent groups and 7/7 generated tests pass |
| Test all non-expert GPU placement | Done | 204.891 seconds; 38/40 provisional; 6/6 independent groups pass, one of seven generated tests fails |
| Inspect answers and publish findings | Done | Public report, numeric aggregates and isolated grading; no production promotion |

Preflight at 23:12 IST: about 22.9 GiB free RAM, 7349 MiB free VRAM, unchanged
12 October boot; no running llama-server. Apps remain open. No weight deletion,
clock/driver changes or production-editor changes are part of this experiment.
Research cache correction retained: current cache-ram is already zero. Thinking
and preservation stay enabled. A runtime budget is a ceiling, not native xhigh.

Evidence: [placement report](../reports/2026-10-14-placement.md),
[frozen plan](../reports/2026-10-14-placement-plan.md),
[numeric results](../reports/2026-10-14-placement-results.json).

- 23:14–23:32 IST: owned reference and alternative servers ran sequentially;
  both passed smoke/health/identity and completed router-v1 within 20 minutes.
- 23:32–23:35 IST: both unloaded; existing WSL/bubblewrap used for grading.
  Initial environment preflight rejected PWD and executed no candidate; fixed
  the explicit allowlist and verified namespace boundaries before execution.
- 23:35 IST: unchanged 12 October boot and no new WHEA event confirmed.
- 23:40 IST: 16 offline tests, both PowerShell parsers and publication audit
  passed. Known-broken fixture fails all six behavior groups as a negative control.
- 23:44 IST: implementation c3e9d26 published on main; both Windows and Ubuntu
  CI jobs passed. Canonical closeout recorded in prompts.md before responding.
- Raw source/answer/telemetry remains ignored. No weight downloads/deletions,
  editor changes, new system packages or cloud API calls. New grading uses the
  already installed Ubuntu, Python and bubblewrap; no new Python dependencies.

## 2026-10-14 — Establish the public research repository

| Task | Status | Notes |
|---|---|---|
| Create a reusable repository | Done locally | Portable instruction entry points, README, setup, profiles, benchmark harness, contribution/security/license docs |
| Organize reports and model links | Done | Sanitized historical digest, numeric subset, source hashes and four pinned artifacts |
| Read and preserve Gemini research | Done | Anonymous browser rendered the full report; extracted/redacted text, provenance and separate critical review |
| Plan next experiments | Done | Placement-only Qwen test if memory permits, Gemma QAT, conditional GLM UD-Q4, then repeat/held-out/editor checks |
| Offline validation | Done | 13 tests, PowerShell parsing and dry run, frozen-prompt preparation, publisher hash/size/revision checks, public-content audit |
| Publish on GitHub | Done | Public paras-lehana/local-coding-lab, main; initial implementation eda5eb5 pushed and verified; Windows and Ubuntu CI passed |

No model was downloaded, loaded or deleted. No editor, driver or clock settings
were changed. Original private reports and installation remain outside Git.

## Agent Deferred

- Repeated core and held-out comparisons now exist for Qwen/Gemma/GLM. Finish
  pending precision/settings/private-audit results before choosing a finalist.
- Clean-machine real runtime/model download is not part of offline validation.
- Long-history, stale-file and held-out language fixtures now run in v0.3.
  Larger-history coverage remains active; failed-tool recovery requires an
  observed attempted unavailable read and cannot be inferred from avoiding it.
- Isolated Python contract grading now passed for both completed answers. The
  benchmark collector still cannot execute code; broader language tests remain.
- Continue UI and candidate editor tool transport require observed tests.

## Agent Suggestions

- Start with a fresh memory snapshot; preserve the measured Qwen reference.
- Keep the research's multi-variable tuning bundle as separate experiments.
- Prefer Gemma QAT when current app usage makes Qwen's host allocation fragile.
- Collect repeated public results before claiming an accuracy leaderboard.

## Work log

- Recovered earlier model, memory-stop, reasoning-budget and instruction-grounding evidence.
- Retrieved the shared Gemini research through anonymous rendering; preserved
  58,446 characters of research text with 22 personal-path/name replacements.
- Verified four pinned model artifacts against publisher metadata and both CUDA
  runtime release digests. Cross-checked the publisher's fixed Gemma revision.
- Built and exercised the offline tooling. Fixed a Windows path-format assertion
  in the test and removed personal path keys from extracted-source metadata.
- Publication result and exact validation record: see prompts.md and
  repository-creation.md.
- 22:35-22:42 IST: completed content review, normalized extracted text, committed
  and pushed the public repository; verified both CI jobs passed on eda5eb5.

- 01:23 IST: Ubuntu CI passed; Windows CI exposed an overly tight one-second
  test deadline that expired during process startup. Increased startup margin
  while keeping the combined phases over the deadline; targeted checks pass.

- 15:25 IST: recovery smoke1.11s; short calibration deliberately output-limited/unscored, normal stop. Gemma unrestricted private audit active; frozen eleven-action sequential queue resumes Qwen flags/precision and GLM follow-ups. GLM Q6 download resumed.20 offline tests, PS parsing and96-file publication audit passed. No diagnosis established by owner observation.

- 16:02 IST: recovered Qwen private25/36 and Gemma unrestricted19/36 graded. Batch512/cache1536/CPU-KV probes collected and code graded; all history facts pass. Sampling bundle is running. Prepared but not run3GiB cache, batch combination and conditional Qwen Q6. GLM Q6 transfer ended short; continuing from8.319GB with mandatory full hash.

16:25 IST checkpoint: published c2cd01c, CI passed. Research sampling three core implementations6/6, own tests6/7 each; TS/SQL manually reviewed and queued for isolation. Matched Q4 control running. GLM Q6 complete artifact size/SHA verified after bounded continuation; disk12.8GiB, no new download until completed candidate retirement. Native finalist/code/history/editor validation plan frozen; no production promotion.

16:35 IST: corrected legacy human-review/human-authored labels to Codex source assessments and independent contract checks. Semantic scores are not independently human-reviewed. Collector note and grader docstring change only attribution, not prompts, assertions or raw artifacts. Q4 matched control finished186.016/210.984/239.656seconds; first two independent implementations6/6, third awaiting between-load grading. Q5 loaded and first answer244.187seconds reviewed. No new editor pass.

16:38 IST validation:20 offline tests pass in9.288seconds, PowerShell scripts parse,99-file publication audit has0 findings, diff check passes. v0.3.7 corrects attribution only in collector/checker code; no benchmark prompt, behavioral assertion or original raw-result changes. Dedicated server remains the single Q5 test on8081.

17:15 IST checkpoint: matched Qwen Q4/Q5 core implementations all6/6; Q5 average252.797s versus212.219s,19.1% longer, without a demonstrated code advantage. Q5 whole-suite peakRAM21.35GiB and dedicatedVRAM5.99GiB; held-out strictTS4/6 and SQL FK migration failure. Numeric matched settings/input/artifact/checker hashes published separately. GLM Q4 f16 allocation1692MiB K/zero separate V, native173.219s/code6/6; original generated script invokes no tests, supplemental entrypoint13/14. Capped f16 code5/6 with alias bug. History six facts correct but READY243 instead of120; explicitly failed count. Conditional64K native QwenQ5/GLMf16/GLMQ6 private profiles prepared, no load claimed. GLMQ5 native74/75 and TS/SQL reviewed, waiting for between-load isolated grading; private retry currently running. No new cloud calls, editor promotion, app closure or hardware changes.
