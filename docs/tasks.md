# Task log — Local Coding Lab

Last updated: 2026-10-15 (Asia/Kolkata).

## 2026-10-15 — Autonomous research campaign

Owner explicitly authorized downloads, rigorous testing, reports and selected
model deletion. Continue across candidates without asking for another prompt.
Apps remain open; keep the 1200-second prompt limit and resource/error guards.
Use resumable on-disk state and preserve failed attempts rather than restarting
them blindly after interruption.

| Candidate | Status | Required disposition |
|---|---|---|
| Qwen3.6 Q4 | Core/history/held-out collected | Python passes; TS/SQL bugs persist with unrestricted thinking; larger batch interrupted by planned update |
| Gemma 4 26B QAT | Verified; suite running | Balanced 32K profile, 4.97 GiB dedicated VRAM; file tools working |
| GLM-4.7-Flash UD-Q4 | Downloading | Load/MLA/q8 behavior, coding, memory, history |
| Qwen3-Coder 30B UD-Q4 | Pending | Non-thinking comparison, coding and history |
| Gemma 4 31B QAT dense | Calibration rejected | GPU-KV resource stop; CPU-KV 0.95 tok/s and five-minute deadline; quality unscored |
| Qwen3.6 Q5 and optional Q6 | Pending | Verified capacity check and matched precision test where feasible |
| GLM Flash Q5 and optional UD-Q6 | Q5 download queued | Matched Q4/Q5 placement prepared; Q6 capacity review remains |
| Kimi Linear 48B Q4 | Pending | Runtime support and capacity, then feasible tasks |
| Qwen Coder Next 80B Q4 | Pending capacity review | 45+ GiB weights versus apps-open RAM/VRAM; no invented score |
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

- First Qwen placement pair is complete; repeated/held-out and reasoning-budget
  comparisons remain required before promotion. Gemma and GLM remain untested.
- Clean-machine real runtime/model download is not part of offline validation.
- Long-history, stale-file, transient-tool-error and held-out language fixtures
  remain future work; v0.1 offers frozen inline and allowlisted-read modes.
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
