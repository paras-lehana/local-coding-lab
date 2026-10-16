# Prompt log — Local Coding Lab

Current phase, 17 October: all five expanded research points are complete.
Matched Q4 private31/36 in11m40s versus Q628/36 in35m; both public Python6/6
three times, TS5/6, SQL failure and passing histories. Post-review checks find
local-key loss and nested aliases beyond the frozen score. Retain Q4 and
recommend its mapped apps-open policy; production/editor configuration is
unchanged and inference is stopped. Evidence116a67d is published; Windows/Ubuntu CI38975676188 passes. Final closeout follows below.

Last updated: 2026-10-17. Public project history excludes earlier credentials,
private instruction contents and raw editor chats.

| # | Date | Time (IST) | Topic | Type | Status | Link |
|---|---|---|---|---|---|---|
| 8 | 2026-10-17 | 03:57 | Complete expanded comparison | Research | Done | [Closeout](#expanded-comparison-closeout) |
| 7 | 2026-10-16 | 10:23 | KV growth and remaining candidates | Research | Five points completed; Q4 retained | [Entry](#memory-and-remaining-candidate-expansion) |
| 1 | 2026-10-14 | 22:35 | Establish reusable research repository | Infrastructure | Done | [Entry](#repository-creation) |
| 2 | 2026-10-14 | 23:12 | Start research: controlled Qwen placement | Research | Done | [Entry](#research-placement-experiment) |
| 3 | 2026-10-15 | 00:47 | Autonomous full research campaign | Research | In progress | [Entry](#autonomous-research-campaign) |
| 4 | 2026-10-15 | 15:17 | Recover after unexpected shutdown | Infrastructure / Research | Evidence reviewed; cause unknown | [Entry](#unexpected-shutdown-recovery) |
| 5 | 2026-10-15 | 20:58 | Working selection, comparison and editor gate | Research / Config | API done; UI blocked | [Entry](#working-selection-and-editor-gate) |
| 6 | 2026-10-15 | 23:06 | Actual editor validation after unlock | Research / Config | Six probes complete; quality defects retained | [Entry](#actual-editor-validation-after-unlock) |

## Repository creation

Project: local-coding-lab. Branch: main. Mode: Default.

### Original request

> lets make a repo for this where you have reports, other docs, model links,
> installation script etc very user-friendly managed so that others can also try
> and test things via our repo.
>
> this also a research doc, shift this to the repo is some bare research folder
> and then plan what to try next
>
> https://share.gemini.google/LadMuhd0ajY0 see if you can read this doc.

Publication choice: Public GitHub repository, selected by the owner.

### Recovered context and pre-flight

- New portable repo on the dedicated installation drive (existing parent lab
  contains private logs, secrets and large artifacts and must not be published).
- Public synthetic fixture instead of personal source contents (owner's main
  evaluation requirement is instruction/file grounding and correct code).
- Whole-prompt limit 1200 seconds and apps remain open (current parent rules).
- Preserve measured/proposed distinctions (recent trials included two memory
  stops; current Qwen reference is not a demonstrated universal winner).
- Use project-owned guidance plus small Claude/Copilot adapters (shared
  context-maintenance workflow); no global adapter changes needed.

### Implementation and validation

See [repository-creation.md](repository-creation.md),
[file inventory](file-inventory.md), and [tasks.md](tasks.md). No dependencies
were added. Offline tests and publication audit passed. Public main was verified after push; both implementation CI jobs passed.

### Canonical closeout

**A. Business summary — Done**

Published [Local Coding Lab](https://github.com/paras-lehana/local-coding-lab): setup instructions, model downloads, benchmarks, reports and a next-test plan. I successfully read and archived the Gemini document, with a separate critical review.

**B. Technical summary — Done**

The repo includes hash-verified downloads, guarded launch profiles, a file-reading benchmark with a 20-minute deadline, and synthetic project files others can safely use. **13 tests passed locally and in Windows/Ubuntu CI.** Implementation commit: `eda5eb5`, branch `main`; no new dependencies.

Start with the [setup guide](https://github.com/paras-lehana/local-coding-lab/blob/main/docs/setup.md). The [file inventory](https://github.com/paras-lehana/local-coding-lab/blob/main/docs/file-inventory.md) and [validation record](https://github.com/paras-lehana/local-coding-lab/blob/main/docs/repository-creation.md) document the changes and checks. No new model inference or editor UI testing occurred during this task.

**C. Request status**

| # | Pointer Task | Original Pointer Text | Status | What Was Done |
|---|---|---|---|---|
| 1 | Shareable repository | “reports, other docs, model links, installation script” | DONE | Public repository with setup and evaluation tooling |
| 2 | Archive research | “shift this to the repo…research folder” | DONE | Source text, provenance and separate review |
| 3 | Next experiments | “plan what to try next” | DONE | Controlled, memory-aware test sequence |
| 4 | Read Gemini | “see if you can read this doc” | DONE | Retrieved through anonymous browser rendering |

**D. Additional findings**

The research incorrectly attributes memory stops to a default prompt cache: your launcher already sets `--cache-ram 0`. Its proposed 1536 MiB cache would increase that allowance. Its predicted speed gains remain unmeasured. Details are in the [research review](https://github.com/paras-lehana/local-coding-lab/blob/main/research/reviews/2026-10-14-gemini.md).

**E. Pending work**

| Item | Status | Reason |
|---|---|---|
| New model comparisons, long-history tests and editor validation | Planned | Repository preparation is complete; these require live experiments |

**F. My recommendation**

Keep Qwen as the measured reference. Test GPU placement separately when memory permits; **Gemma 4 26B QAT is my next smaller candidate**, followed by GLM-4.7-Flash UD-Q4 at 32K. Neither is a proven upgrade yet. Your existing installation, models and private evidence remain intact.

**G. Copyable summary**

```text
Local Coding Lab — public research repository published (v0.1, 14 October 2026)

What's done
- Created a shared home for installation guidance, model choices, benchmark questions and measured reports.
- Preserved the supplied research and added a separate review explaining which claims are supported, uncertain or contradicted by local evidence.
- Added reusable tests focused on instruction following, file references, missing information and coding mistakes.
- Automated tooling checks passed on Windows and Linux. Private credentials and instruction files were excluded from publication.
- Existing models and the original installation remain intact. No new model performance result is claimed from this packaging work.

Suggested next steps
- Retain Qwen as the measured reference and test one setting change at a time.
- Evaluate the smaller Gemma candidate, then GLM if memory allows.
- Require repeatable code correctness, reliable file handling and completion within twenty minutes before choosing a replacement.
```

## Research placement experiment

Project: local-coding-lab. Branch: main. Mode: Default.

### Original request

> lets start the experiment as per the research (i hope you can read or have read, otherwise stop): https://share.gemini.google/LadMuhd0ajY0

### Recovered constraints and pre-flight

- Research contents already archived and read; verified the archived SHA and
  reread the experiment/tuning sections before loading (source provenance in
  research/raw/2026-10-14-gemini/source.json).
- Follow project/parent AGENTS and maintained shared Codex, topic, platform,
  logging, Python and Git guidance (project local-coding-lab, existing owner
  repository main branch; personal instruction paths excluded from publication).
- Preserve apps and accepted clock settings (GPU/CPU reported stock, RAM 2800;
  no new evidence establishing RAM speed as the cause of old restarts).
- Freeze placement-only comparison, retain thinking/preservation, 64K/q8 and
  cache-ram 0; explicit 2048 per-request budget and 1200-second total deadline.
- Use isolated localhost:8081 and stop only owned children. No editor changes,
  new weight downloads/deletions or API spend (current original server stopped).
- Add process/dedicated GPU measurements and save raw evidence locally; execute
  reviewed generated code only inside the separate restricted Linux environment.

### Evidence and validation

See [placement report](../reports/2026-10-14-placement.md),
[numeric evidence](../reports/2026-10-14-placement-results.json),
[file inventory](file-inventory.md) and [tasks](tasks.md).

The reference and treatment completed in 576.453 and 204.891 seconds. Both
implementations passed six independent contract groups. Model-authored tests
passed 7/7 and 6/7; the treatment's alias test contradicts its preceding append.
Manual rubric scores are 39/40 and 38/40 on one small public fixture, not a
cross-model ranking. The known-broken fixture failed all behavior groups.

16 offline tests and both PowerShell parsers passed. The public-content audit
found no flagged material. Sandbox preflight was fixed after rejecting the
isolation tool's PWD variable; no code ran in those rejected attempts. No new
WHEA or reboot was observed. Both inference servers are stopped.

Applied agent-context-maintenance to the reusable grading guidance: updated
the project source, reviewed shared Codex/Claude routing, and left adapters
unchanged because their existing pointers already cover it. No new Python or
system package was installed; grading uses existing WSL/Python/bubblewrap.

### Canonical closeout

**A. Result — done**

I read the Gemini research and completed the first controlled experiment. [Full report](https://github.com/paras-lehana/local-coding-lab/blob/main/reports/2026-10-14-placement.md).

| Measurement | Qwen reference | Alternative placement |
|---|---:|---:|
| Whole prompt | 9m36s | **3m25s** |
| Generation speed | 13.3 tok/s | **23.7 tok/s** |
| Peak process RAM | 17.18 GiB | 19.76 GiB |
| Dedicated VRAM snapshot | 5.88 GiB | 3.30 GiB |
| Model-written tests passing | 7/7 | 6/7 |

Both corrected functions passed all six independent contract checks. Provisional scores: **39/40 versus 38/40** on this small fixture—not a general model ranking.

**B. Technical summary — done**

Tested **Qwen3.6-35B-A3B UD-Q4_K_M**, holding 64K context, q8 KV and sampling constant. Thinking stayed enabled with a **2048-token ceiling per request** for this comparison; that is not native “ultra high.”

Added memory measurements, controlled stopping and isolated code grading. **16 local tests and Windows/Ubuntu CI passed.** No new packages were installed. Implementation: `c3e9d26`, branch `main`. [Complete file/change inventory](https://github.com/paras-lehana/local-coding-lab/blob/main/docs/file-inventory.md).

**C. Request status**

| # | Pointer Task | Original Pointer Text | Status | What Was Done |
|---|---|---|---|---|
| 1 | Start experiment | “lets start the experiment as per the research” | DONE | Completed and published the placement comparison |
| 2 | Read research first | “otherwise stop” | DONE | Read archived contents and verified provenance before testing |

**D. Findings**

The faster answer generated a contradictory test: it appended a value, then asserted that value was absent. Its implementation passed the independent checks.

Lower VRAM use was compatible with faster generation here. **Moving KV into RAM was not tested.** No new reboot or WHEA event was observed; both experiment servers are stopped.

**E. Remaining experiments**

| Item | Status | Reason |
|---|---|---|
| Repeats, unrestricted thinking, long-history and editor tests | Planned | One small run cannot establish reliability |
| Gemma and GLM comparison | Planned | No new weights downloaded yet |

**F. My recommendation**

Keep Qwen installed and repeat the promising placement before changing your everyday setup. Next distinct candidate: **Gemma 4 26B-A4B official QAT Q4_0, initially 32K/q8**. Its 13.45 GiB weights offer a useful memory-fit experiment while your apps stay open; its coding quality remains unproven.

**G. Copyable summary**

```text
Local Coding Lab — first research experiment completed and published (v0.2, 14 October 2026)

What's done
- Read the supplied research and tested two configurations of the current Qwen model using identical questions and reasoning limits.
- The alternative finished in approximately three minutes twenty-five seconds, compared with nine minutes thirty-six seconds for the reference.
- Both proposed code fixes passed independent checks. The faster answer nevertheless included one broken test, so it is not yet an established quality winner.
- Recorded memory use, file-reading behavior and limitations. Automated tooling checks passed on Windows and Linux.
- Existing model files and editor settings were preserved. Both experiment servers are stopped.

Suggested next steps
- Repeat the promising configuration and test longer conversations and real editor use before adopting it.
- Compare unrestricted reasoning within the twenty-minute limit.
- Evaluate the smaller Gemma candidate next, followed by GLM if memory permits. Select a replacement through repeatable correctness and reliable file handling.
```

## Autonomous research campaign

### Original request

> man, you need to work autonomously, you have full rights to download model, make report, test vigrously, delete,  test next model. Please i dont have time to just keep telling you continue, please make sure to fulfil testing for all models in the report.

### Active authorization and constraints

Continue through the complete research candidate matrix without another user
prompt. Downloads, testing, reporting and exact-file model cleanup are explicitly
authorized. Updated project guidance through agent-context-maintenance so the
older blanket no-deletion rule does not block the owner's current instruction.
No shared adapter change is needed; existing links already lead here.

Apps remain open, each whole prompt is capped at 1200 seconds, and the resource
and WHEA stop conditions remain active. A failed fit/runtime check must not be
presented as a completed quality score. Retain the current verified Qwen baseline
while gathering comparison evidence and preserve reports before cleanup.

See [campaign plan](../reports/2026-10-15-campaign-plan.md), [task log](tasks.md),
and ignored local-data/2026-10-15-campaign for resumable live evidence.

### Work in progress

Rechecked pinned artifact metadata, began Gemma 26B, GLM Q4 and Gemma dense
31B downloads, and started Qwen seed 74/75 and unrestricted-thinking trials.
Added frozen long-file/stale-file and held-out TypeScript/SQLite scenarios before
collecting their answers. New catalog entries cover every runnable family and
conditional precision variant in the research. No final ranking yet.

Checkpoint: three Qwen core repeats, history and held-out tasks collected; all
Python implementations pass independent checks, while held-out TypeScript and
SQLite expose real bugs. Unrestricted held-out rerun and extended history are
running. Gemma/GLM downloads continue. Nineteen offline tests, PowerShell parsing
and public-content audit pass; campaign remains in progress.

- 01:23 IST: Ubuntu CI passed; Windows CI exposed an overly tight one-second
  test deadline that expired during process startup. Increased startup margin
  while keeping the combined phases over the deadline; targeted checks pass.

### Recovery after the planned Windows Update restart

> please continue, dont know why the computer restarted.

Recovered completed Qwen answers/grades and unfinished downloads. Event 1074
identifies planned Windows Update restarts at 01:29:38 and 01:33:59 IST; no new
WHEA/bugcheck/display crash or dump was found in the surrounding window.
The unfinished batch512 attempt remains unscored. Current free RAM is lower,
so the campaign continues with measured placement changes and unchanged guards.
Gemma dense is verified; GPU-KV reached the guard, and RAM-KV passed smoke with
a five-minute calibration underway. Full candidate coverage remains active.

Recovery checkpoint: dense RAM-KV reached the five-minute deadline at 0.95
generation tok/s with no complete answer; its verified weights were recorded
and deleted, preserving evidence and the Qwen baseline. Gemma 26B's first core
answer completed in 349.313 seconds and passed 6/6 isolated Python groups and
8/8 generated tests with the documented shared-module assumption. Its current
suite continues. GLM Q4 downloads; Qwen Coder and GLM Q5 are queued. Published
portable task plans, a larger frozen ledger and primary-source size exclusions.
No final ranking, production promotion or new editor pass is claimed.

Continued recovery checkpoint: four Gemma core answers are now reviewed; all
pass the six independent Python groups. The unrestricted answer took 588.391
seconds without an observed behavior improvement. Its shorter history case
passes six factual/current-file checks in 247.109 seconds. GLM Q4 finished
full artifact verification and is queued after Gemma's remaining tasks/unload.
The original six private-audit code cases were moved into the existing isolated
grader without changing their assertions: reference 6/6, shallow-copy negative
control 5/6. This prepares the real-instruction comparison; it is not yet a new
candidate result. Nineteen offline tests, PowerShell parsing and the public
audit passed again for the checkpoint. Candidate ranking remains in progress.

Next checkpoint: the full Gemma 32K suite completed and was reviewed. All five
core implementations pass six independent Python groups; the held-out code has
a strict TypeScript compilation error and a failed SQLite migration. A linked
rules file was skipped. GLM Q4 has loaded, preserved an actual prior tool thought,
and completed its first core in 226.844 seconds; isolation assertions break
legitimate merges (1/6 independent groups, 2/14 generated tests). Retired Qwen3.8
Q8 weights were hash-verified and deleted after evidence preservation. Added
conditional Qwen Q5 / GLM Q6 profiles and a smaller-host-RAM Qwen 64K proposal.
Current capacity exclusions carry no quality score and explicitly omit disk-
paged experiments. One owned inference process remains active; no production
editor promotion or completed overall ranking is claimed.

Further checkpoint: GLM's bounded core repeats score 1/6, 5/6 and 2/6 independent
Python groups. Its unrestricted second turn emitted 16,384 reasoning tokens
without a final answer; total 988.563 seconds, preserved unscored. Its short
history case passes six checks in 259.859 seconds. These distinguish source
retrieval from applying the retrieved contract. Qwen Coder's artifact is fully
verified and its first-load proposal uses 39 CPU expert blocks with an explicit
RAM/VRAM estimate. Prepared host-private guarded orchestration for the frozen
15-file personal audit, with a 2048 per-turn runtime reasoning ceiling and the
unchanged 1200-second whole-prompt limit; no private result yet. Reviewed current
editor instruction-discovery documentation and bundled implementation without
claiming automatic file injection or a new UI pass.

Grading checkpoint: GLM's held-out answer loses all SQL data and adds cascading
deletion; TypeScript fails strict compilation. Fixed a grader defect involving
leading comments on BEGIN and dependent fixture rows. Preserved the initial
result and reran all four unchanged migrations plus both controls in isolation.
GLM's SQL groups correct from 2/6 to 4/6, with both critical failures retained;
other model outcomes are unchanged. Positive 6/6, negative 2/6. The report also
discloses grading/download overlap as a timing limitation; finalist timing
confirmation must avoid simultaneous grading or artifact hashing.

Checkpoint validation for v0.3.4: 20 offline unittests pass, all PowerShell
scripts parse, the publication audit reports zero findings across 92 files,
and git diff whitespace checks pass. No private corpus/output is staged.

Continued checkpoint: Qwen Coder completed its five-task suite. Three core
answers take 78-82 seconds but skip linked rules/contract, retain validation or
aliasing bugs, and one claims tests ran. The short history facts pass but the
read inventory is omitted. Code has been reviewed and prepared for isolated
grading in the next interval without timed inference. Its 32K q8 cache is
1632 MiB; readiness dedicated VRAM 5.80 GiB, peak sampled RAM 13.28 GiB.
GLM Q5 then loaded with matched placement, using 5.57 GiB dedicated VRAM and
about 3 GiB more host model buffers than Q4. Quality collection continues.

Prepared portable matched-Q4, GLM-f16 and research-sampling profiles; private
64K personal audits are queued. All 15 frozen real instruction sources total
27,488 Qwen Coder tokens before wrappers/history/output. Rechecked Kimi's
official config against the GGUF: 27 blocks/256 experts, correcting the research.
Improved unloaded headroom means its earlier arithmetic exclusion no longer
suffices; a conditional profile now requires a fresh 26 GiB / 6800 MiB snapshot
and enough disk. No Kimi load or score is claimed. No editor promotion yet.

v0.3.5 checkpoint validation: 20 offline tests pass; PowerShell parsing and
whitespace checks pass; public-content audit covers all 96 tracked/unignored
files with zero findings. The frozen prompts and model answers are unchanged.

09:18 IST checkpoint: GLM Q5 finished all seven tasks and unloaded normally.
All visible responses were reviewed, including TypeScript delivered before a
later tool call. Prepared eleven unchanged answers for isolated grading during
the next interval without inference. The unrestricted Python answer needs
verification/repeats; bounded answers and SQL retain defects. Its bounded-core
logs show budget activation without exhaustion, so no truncation-causality claim
is made. Updated grading/timing methodology to distinguish visible intermediate
content from the final message. Gemma's 64K follow-up is running. Qwen Q5 is
verified; GLM Q6 awaits disk space after its pre-download gate refused. Four
remaining Qwen settings probes are queued behind the precision comparisons.

09:39 IST checkpoint: Gemma's three-task 64K follow-up is complete with normal
shutdown. The 640-record history case passes six facts/count/fresh-read checks
at 52,231 input tokens; the 320-record count is wrong despite six correct final
facts. Twelve previously reviewed code answers were graded between model loads.
Gemma unrestricted SQL is 6/6 and strict TypeScript 5/6. GLM Q5 bounded Python
scores 5/6, 0/6, 0/6; unrestricted 6/6. Qwen Coder scores 2/6, 3/6, 1/6; its
last standalone test script invokes no tests, so supplemental unchanged tests
with a harness entrypoint are queued. No implementation was repaired for scores.

Corrected the current parent installation guide's retired Qwen Q8 note and
added the campaign pointer, with a private backup. Read the maintenance skill,
Windows Claude/Codex entry points and shared router; existing adapters need no
change. Unrelated dirty files in the shared repo were preserved. Froze actual
editor greeting/source/history prompts and observed 1044 accessible VS Code
controls, without opening another window or claiming UI inference. Rechecked
Continue's installed reasoning serializer and corrected the public example to
the explicit-localhost Deepseek adapter. The private Gemma audit is running.

### 10:00 IST continuing checkpoint

Gemma and GLM Q4 completed the separate actual-instruction audit. Private source
bytes stay local; the public report records retrieval failures, contradictory
code claims, measured memory and timings. Reviewed unchanged code is queued for
isolated grading between loads. Added an optional private-wrapper budget flag
(default 2048 unchanged) and queued unrestricted Gemma/Qwen follow-ups. Qwen
Coder supplemental test invocation is 6/7; the original script ran no tests.

### 10:19 IST continuing checkpoint

Private code grading completed between loads: Gemma 2/6, GLM Q4 4/6; combined
manual-source/code totals 19/36 and 21/36. Coder timed out without a final answer,
unscored, despite sufficient context capacity. Preserved evidence and retired
only its hash-verified exact weight; GLM Q6 download now runs. GLM Q5 retry
passed the original gates after a preflight rejection. Staged launcher reads
profile-specific settings and checks existing endpoint health; production
remains unchanged. Published checkpoint 2268c0f passed both CI platforms.


## Unexpected shutdown recovery

Original request: "you please continue, the pc was restarted itself, see if you can find an y reason from the image (and continue your work)". The image points to a local crash report for the 14:58 boot.

15:17 IST checkpoint: re-read project/parent instructions, shared Codex entry, router, platform and logging rules; recovered reports and on-disk trial state. Earlier completed results survive. GLM Q5 private retry was interrupted and is now explicitly unscored; none of its queued successors started. The external crash report and event XML are preserved privately. Zero bugcheck, no new WHEA/NVIDIA error/minidump and last heartbeat at10:24 do not identify a specific failing component. The external report's CPU-overclock and hardware-reset assertions are unsupported by those fields. Current load recovery uses a short Gemma check; no BIOS, driver, application or editor changes. Added commit telemetry without weakening existing stops. Full campaign remains active; no final model ranking or UI pass is claimed.

15:25 IST checkpoint: owner was not watching and cannot distinguish freeze/power loss/restart. Short Gemma recovery greeting completed in1.11s; deliberately500-token calibration stopped on output length in38.625s, unscored, normal owned shutdown. Peak process RAM11.06GiB; minimum free RAM15.14GiB, available commit24.05GiB, free VRAM1952MiB, core maximum50C. Unrestricted private audit now active. Eleven named recovery actions are frozen in ignored local data and run sequentially, with new hardware-event checks and fresh memory gates; no startup task. GLM Q6 download resumed. Offline validation:20 tests pass in9.186s, both PowerShell scripts parse,96-file audit has0 findings, diff check passes. Source definitions clarify that GlobalMemoryStatusEx commit values may include calling-process limits.

16:02 IST checkpoint: Gemma unrestricted private audit400.234s,19/36 after isolated2/6 code; Qwen new capped private audit458.703s,25/36 (18 semantic+4 citation+3 code),13 sources delivered but one failed read falsely claimed. Public batch512 and1536MiB GPU cache code6/6, generated tests6/7 with wrong empty-dict expectation; CPU-KV code6/6 and own tests7/7. All three120-record history checks recover six facts and fresh revision/zero retry, without attempting the unavailable ledger read. GPU expert cache generation39.18tok/s versus CPU-KV13.13; different profiles/tool paths prevent a universal speed claim. CPU-KV buffers680+62.81MiB, dedicatedVRAM2.43GiB/peakRSS21.04GiB. Download stopped short at8,319,246,931bytes and is continuing from that offset with bounded retries/full verification. Prepared adaptive3GiB cache and combined-batch profiles, plus conditional Qwen Q6 after28.76GiB unloaded RAM recovery and actual header inspection. No editor promotion or hardware diagnosis.

16:25 IST checkpoint: published c2cd01c, CI passed. Research sampling three core implementations6/6, own tests6/7 each; TS/SQL manually reviewed and queued for isolation. Matched Q4 control running. GLM Q6 complete artifact size/SHA verified after bounded continuation; disk12.8GiB, no new download until completed candidate retirement. Native finalist/code/history/editor validation plan frozen; no production promotion.

16:35 IST: corrected legacy human-review/human-authored labels to Codex source assessments and independent contract checks. Semantic scores are not independently human-reviewed. Collector note and grader docstring change only attribution, not prompts, assertions or raw artifacts. Q4 matched control finished186.016/210.984/239.656seconds; first two independent implementations6/6, third awaiting between-load grading. Q5 loaded and first answer244.187seconds reviewed. No new editor pass.

16:38 IST validation:20 offline tests pass in9.288seconds, PowerShell scripts parse,99-file publication audit has0 findings, diff check passes. v0.3.7 corrects attribution only in collector/checker code; no benchmark prompt, behavioral assertion or original raw-result changes. Dedicated server remains the single Q5 test on8081.

17:15 IST checkpoint: matched Qwen Q4/Q5 core implementations all6/6; Q5 average252.797s versus212.219s,19.1% longer, without a demonstrated code advantage. Q5 whole-suite peakRAM21.35GiB and dedicatedVRAM5.99GiB; held-out strictTS4/6 and SQL FK migration failure. Numeric matched settings/input/artifact/checker hashes published separately. GLM Q4 f16 allocation1692MiB K/zero separate V, native173.219s/code6/6; original generated script invokes no tests, supplemental entrypoint13/14. Capped f16 code5/6 with alias bug. History six facts correct but READY243 instead of120; explicitly failed count. Conditional64K native QwenQ5/GLMf16/GLMQ6 private profiles prepared, no load claimed. GLMQ5 native74/75 and TS/SQL reviewed, waiting for between-load isolated grading; private retry currently running. No new cloud calls, editor promotion, app closure or hardware changes.

17:40 IST checkpoint: GLM Q5 native repeats6/6 and0/6, own7/7 and1/14; held-out strictTS compile fails and SQLite5/6 includes complete data loss. Recovery private audit750.391s,21/36 (16 semantic+3 citation+2 isolated code), ten sources delivered but four unread files claimed. Full weight SHA verified, exact21,408,850,272-byte file retired; all evidence remains. Qwen native private454.859s answer byte-identical to capped run, same read trace except generated IDs, same25/36. Verified launch ceilings2048/-1 and no request override; delivered reasoning172/26/37/57/92tokens on both. Prior identical-code isolated grade reused with explicit provenance, no new execution claimed. Adaptive cache queue active. Kimi transfer started after fresh unloaded26.42GiB/7112MiB snapshot; disk32.76GiB before transfer. Staged production stop shortcut now matches model+port8080+process creation, avoiding stale-PID targeting; CheckOnly excludes active8081. CIM/Process timestamp precision difference observed and handled; not installed. Checkpoint735745e passed both CI platforms.

17:58 IST checkpoint: no-cache reference212.750s/code6/6 and history133.969s passes;3072MiB cache118.422s/code6/6 and history135.391s passes. Both own-test suites6/7, with distinct false assertions;3072 standalone seven NameErrors preserved. Cache decode46.71tok/s, dedicatedVRAM6.26GiB, minfreeVRAM661MiB; history prefill slows and whole latency does not improve. Combined3072/batch512 rejected before load at7083<7100MiB, not OOM. New2GiB/batch512 candidate and historical34-expert replay prepared to choose actual-instruction quality before speed. Conditional native QwenQ5/GLMf16/GLMQ6 audits and subsequent two Qwen selection audits are serialized behind active GLMQ6 suite. GLMQ6 first core292.609s reviewed, code grading pending. Kimi download39% at17:53, not yet verified.20 offline tests pass9.556s; checks overlap GLMQ6 public collection and are disclosed. Public command construction for both new profiles passes; no production/editor changes.

18:20 IST: GLM Q6 public suite completed normally; capped Python5/6,0/6,6/6, unrestricted5/6. Own tests12/12,2/9,12/13,10/10; preserved failures separately. History six facts correct but count242 instead of120. Held-out source review finds TypeScript narrowing defects and SQL data loss; isolated grading queued. DedicatedVRAM5.71GiB, peakRSS20.74GiB, minfreeRAM5.20GiB/freeVRAM463MiB. QwenQ5 native private audit now running; subsequent GLMf16/Q6 and quality-first Qwen audits serialized. Kimi public suite queued after them. Continue2.0.0 installed-source inspection finds timeout units differ between SDK(milliseconds) and fetch agent(seconds); proposed model-entry correction1200000 awaits final editor validation. Production unchanged.

18:27 IST checkpoint: Kimi full30,061,058,720-byte pinned artifact/SHA verified at18:23; native non-thinking public suite frozen and serialized after existing audits. QwenQ5 native private collection remains active. Read-only UIAutomation confirms local VS Code window accessible alongside separate remote windows; no editor interaction or new UI inference yet. Continue timeout source evidence recorded with installed bundle hash; correction remains staged. Current report/model/next-step documents updated for GLMQ6 public outcomes.

18:27 IST validation:20 offline tests pass in9.167seconds; PowerShell scripts parse;103-file public-content audit has0 findings and diff check passes. Checks overlap QwenQ5 private inference and that timing caveat is recorded. Only reviewed documentation changed in this checkpoint; runtime/editor selection remains unchanged.

18:49 IST checkpoint: QwenQ5 native private537.250s,28/36 (20 semantic+6 citations+2 isolated code), honest14-source inventory and recovered read failure; nested dictionaries become None and mutable values alias. GLMQ4f16 native private942.000s,all15 sources/honest ranges,19 semantic+4 citations with isolated code pending; source code mutates/aliases inputs. GLMQ6 native private is active. Dedicated Local LLM VS Code window opened(handle462398); selected explicit local Qwen in Copilot and Continue Plan, no prompts sent. Added task-specific coding-use guide. Published6046eac CI38738677381 passes; later report updates remain local until next checkpoint.

19:16 IST checkpoint: GLMf16 native private27/36 (19+4+4); GLMQ6 native private24/36 (17+2+5), all saved and isolated graded. Qwen2GiB-cache private completed402.703s with honest14-source inventory; semantic19/citations4, code queued. Historical34-expert replay active; Kimi public suite waits serially. Restart cause remains unknown, owner did not observe event. No new editor prompt or production promotion.

19:30 IST checkpoint: historical Qwen placement replay31/36 (20+6+5),864.266s, all15 sources and accurate ranges;2GiB-cache27/36 (19+4+4),402.703s. Kimi q8V fails72/32 dimension constraint; mixed K/V fails architecture constraint; matching f16 loads with252MiB KV+42.81MiB recurrent state. Public suite active, first malformed-call failure preserved.20 offline tests pass9.192s; PS parse and110-file export audit/diff check pass. Offline tests overlap Kimi inference, disclosed. v0.3.8 adds separate compatibility profiles; production unchanged.

19:58 IST checkpoint: e2eb995/v0.3.8 published; Windows+UbuntuCI38748100354 passes. Kimi matching-f16 public suite completed normally: core4/6, malformed-call/no-code,6/6; own combined7/8 each and standalone8NameErrors; history facts pass/count242vs120 fails; TS/SQL source reviewed, isolated queued. Optional QwenQ6 fresh27.426GiB<28.5 gate rejected before retirement/download. Historical Qwen contender native cores73/74 completed473.265/469.328s, source reviewed and isolated queued;75/TS/52K follow. No hashing or sandbox grading during contender timing. Kimi64K private conditional after contender. Historical private answer exactly matches old31/36 answer, so repetition is reproducibility only. UI private helper staged/parsed, owned window screenshot inspected; no prompt sent. Conditional48K input/16K output budgets and candidate runtime staged only; production remains1.4/stopped.

## Working selection and editor gate

Project: local-coding-lab. Branch: main. Mode: Default.

### Continuing request

> please continue, dont know why the computer restarted.
> I wasn't watching / don't know

The owner's earlier autonomous comparison/report authority remains active; see the preserved owner-request file. Applications remain open, RAM2800 accepted, whole prompts1200s, no new cloud calls.

### Sources and validation actually used

Read project/parent AGENTS, README, methodology, grading and task records; maintained shared Codex guide, Windows adapters, router, host facts, platform rules, Python/documentation and logging rules; agent-context-maintenance skill. Reviewed frozen benchmark sources as data, complete visible answers and isolated test records. Updated project-owned guidance; shared adapters reviewed and unchanged because routing remains valid. No private source bodies or credentials exported.

Production API/native reasoning/two-file round trip passed.20 offline tests passed8.881s; public scripts parsed,113-file audit0findings, diff check passed. Initial PowerShell5 stderr-wrapper interruption preserved; complete Python subprocess rerun passed. Windows input desktop access still denied/error5 at20:54, foreground0; no fresh UI prompt sent.

### Prepared user-visible closeout

**A. Result**

The comparisons are saved and **Qwen3.6-35B-A3B UD-Q4_K_M is running at localhost:8080**. I chose the instruction-focused profile: **31/36** on your instruction audit versus **27/36** for the faster expert-cache profile. It also passed the roughly 52K-token history test. Coding bugs remain; the repeated 31/36 answer was identical to its earlier result.

The restart’s cause is still **unknown**. The logs establish an unclean shutdown without a recorded bugcheck; they do not establish that RAM speed caused it.

[Full comparison, settings and recommendation](https://github.com/paras-lehana/local-coding-lab/blob/main/docs/tasks/2026-10-15-autonomous-model-campaign/2026-10-15-model-comparison-and-editor-validation-v0.3.9.md)

**B. Installed setup and checks**

- **Memory:** about 17 GiB process RAM and 5.38 GiB dedicated VRAM at readiness; 18.09 GiB peak RAM in the finalist suite.
- **Context:** 64K, with 680 MiB attention KV split between GPU 544 MiB and RAM 136 MiB. This is temporary context, not permanent file memory.
- **Thinking:** native thinking enabled; no separate reasoning ceiling or invented “ultra” setting. Output allowance: 16,384 tokens.
- **Live API:** READY in 12 seconds; correct two-file tool response in 34 seconds. Twenty offline tests, PowerShell parsing and publication checks passed.

**C. Request status**

| Request | Status |
|---|---|
| Compare models, settings and actual instructions | Completed for feasible tests; capacity/deadline exclusions documented |
| Publish reports and reusable setup | Published in the repository |
| Select and load a model | Done; API verified |
| Identify restart cause | Evidence reviewed; cause unresolved |
| Verify actual Copilot and Continue chats | Blocked by unavailable Windows desktop |

**D. Other changes**

Corrected Continue’s timeout units and installed 48K-input/16K-output client budgets. Encrypted configuration backups preserve other providers. Retired four verified nonselected weights, reclaiming **93.33 GiB**; Qwen Q4 and the lower-memory Gemma 26 fallback remain.

**E. Remaining work**

| Item | What is needed |
|---|---|
| Fresh Copilot/Continue greeting, file reads and history checks | An unlocked interactive desktop; no fresh UI prompt was sent |
| Optional larger models | More available RAM; no scores invented for rejected profiles |

**F. My recommendation**

Use this setup for supervised Python work and file-grounded questions. Run independent tests, especially for mutation and validation bugs. Review SQL migrations carefully. Keep durable decisions in project notes and re-read changed files.

**G. Manager copy**

```text
Local Coding Lab — comparisons published and preferred model installed, version 0.3.9.

What's done
- Compared the feasible candidates using coding problems, real instruction documents, file references and long conversation history.
- Selected a model that best matches the owner's emphasis on following instructions. The local service is running and answered both a greeting and a file-reading check.
- Preserved the experiment evidence, retained a smaller fallback and removed completed alternatives to recover disk space.
- Reviewed the restart evidence. The cause remains unknown; the available logs do not identify a failed component.

Suggested next steps
- Unlock the workstation to finish the actual editor checks. Those checks have not been claimed as successful.
- Use independent tests and human review before accepting generated code, especially database changes.
- Keep important project decisions in maintained documents so future conversations can retrieve them reliably.
```

## Actual editor validation after unlock

Project: local-coding-lab. Branch: main. Mode: Default. Configuration2.0 unchanged.

### Original prompt and steering

> I’ve unlocked the PC
>
> Yes, I’ll leave it untouched

The second reply established an idle keyboard interval after unexpected drafts
appeared. Those drafts were preserved; no ambiguous test request was submitted.

### Instructions actually used

Read the parent/project AGENTS, README, task logs, methodology, editor guide and
current forwardable report. Recovered the frozen probes and prior comparison
evidence. Read the maintained Codex guide, shared Claude router, Windows adapters,
host facts, platform/logging/coding guidance and matching v2 Python/Git rules.
Applied the previously announced agent-context-maintenance skill to project
guidance. Both shared adapters already route correctly and remain unchanged;
the model's failure to follow the router is recorded rather than concealed by
rewriting the benchmark. Actual editor versions and read-only modes were checked.

Pre-flight: dedicated local workspace/read-only tools;1200-second whole-prompt
limit and existing guards; raw evidence private; publish reviewed results on main.

### Exact visible closeout

**A. Business summary**

Both Copilot and Continue completed the local greeting, file-reading and changed-file/history tests. **Each of the six prompts finished within five minutes.**

The quality limitations matter: **both missed the Python-specific instruction file**, and Copilot cited an unread report. The integration works; instruction-following still needs supervision. [Updated comparison and editor report](https://github.com/paras-lehana/local-coding-lab/blob/main/docs/tasks/2026-10-15-autonomous-model-campaign/2026-10-15-model-comparison-and-editor-validation-v0.3.9.md).

**B. Technical summary**

The running model remains **Qwen3.6-35B-A3B UD-Q4_K_M**, native thinking enabled, 64K context and q8 K/V cache. At 22:58 IST it used **16.7 GiB RAM / 5.44 GiB dedicated VRAM**. KV allocation is **680 MiB**, split between RAM and VRAM; it does not provide permanent memory.

Copilot’s greeting required 71.5 seconds of server work versus Continue’s 29.6 seconds, mainly because Copilot supplied more input. Continue also paused for individual file-read approvals. Full elapsed timings and caveats are in the report.

Published the reviewed evidence. **20 offline tests, PowerShell parsing and the 114-file publication audit passed.**

**C. Your request status**

| # | Pointer task | Your words | Status | Result |
|---|---|---|---|---|
| 1 | Resume editor checks | “I’ve unlocked the PC” | DONE | Tested both actual editors against the local server |
| 2 | Finish without keyboard interference | “Yes, I’ll leave it untouched” | DONE | Preserved drafts and completed the six probes; keyboard use is finished |

**D. Additional findings**

Copilot marked two oversized-file reads successful even though they returned a size-limit message. It later read only the first 150 lines. A green tool indicator alone does not establish full file coverage.

**E. Remaining limits**

| # | Item | Status | Reason |
|---|---|---|---|
| 1 | Reliable unattended coding | Not demonstrated | Instruction and code defects remain |
| 2 | Restart’s cause | Unknown | Logs do not identify a component |
| 3 | 128K / clean-machine installation | Not tested | Outside the completed validation |

**F. My recommendation**

Keep this Qwen profile for supervised coding. The tested larger quantizations did not establish a better overall workflow. Before a patch, require an explicit list of instruction files and ranges read, then independently check syntax, types and behavior. That retrieval checklist is a recommendation, not a proven fix for today’s failures.

**G. Manager copy block**

```text
Local Coding Lab — editor validation completed, 15 October 2026

What's done
- The local coding assistant now completes the tested conversations through both supported editors.
- All six prompts finished within five minutes, including the observed waiting time for file approvals.
- Both editors reread a changed file correctly and retained a detail from the earlier conversation.
- The comparison report now includes response times, memory usage and the mistakes found during testing.
- Personal source files and raw conversations remain private.

Suggested next steps
- Keep the selected model for supervised work rather than assuming a larger download will solve the remaining mistakes.
- Require the assistant to identify the instructions it actually read before changing code.
- Check generated work independently, especially database changes and shared data structures.
- Keep the earlier computer restart listed as unresolved; these successful tests do not identify its cause.
```


## Memory and remaining-candidate expansion

Owner requests RAM/KV growth measurement, actual Coder-Next 80B and Qwen Q6 attempts, a longer dense Gemma31 trial, and independent reasoning beyond the supplied report. Full wording is preserved in [the task folder](tasks/2026-10-16-memory-and-candidate-expansion/owner-request.txt). Applications stay open; the former 20-minute latency preference is relaxed for explicit experimental runs. Resource stops and frozen evidence remain required. Work is in progress; final A-G outcomes will follow measured results.

11:08 IST checkpoint: context collection complete and reviewed. CPU64 fixed680MiB KV across2K-60K; CPU128 fixed1360MiB across2K-120K. At119943tokens CPU/GPU whole733.063/610.016s, decode2.69/4.15tok/s, RSS18.580/17.477GiB, dedicatedVRAM5.104/6.199GiB. Facts5/5 in both but plainJSON failed by code fences; follow-ups correct, omitted history UNKNOWN. Clean stops; CoderNext80 download started.26 offline tests pass10.886s; final candidate quality work pending.

12:47 IST checkpoint:80B full SHA verified after three bounded resumptions; first stock mmap load stopped at0.115GiB freeRAM/0.125GiB availablecommit, processRSS0.329GiB. No new WHEA in inspected interval. Six-line opt-in same-commit core patch built in isolatedruntime; stock backends unchanged. Tiny CPU/GPU greedy controls identical, verbose confirms prefetch switch. Guarded QwenQ4 smoke1.25s completes (READY. formatting differs); normalstop.27 offline tests10.027s pass.80B modified-runtime retry started; no candidate quality score or production change.

13:17 IST checkpoint: CoderNext80 public core793.828s, seven truthful source reads, isolated implementation6/6; nine own unittest methods8/9 after explicit invocation (original direct script ran none). TS/SQL561.812s, six truthful reads, strictTS compiles4/6, SQL FK failure plus incorrect global uniqueness. Context collection remains active, private audit pending. Grading and offline checks overlapped context prefill after desktop RAM headroom increased; timing caveat saved. Runtime controls exported; dense prepared with one531MiB-class checkpoint at unchanged64K; Q4/Q6 share isolatedruntime.27 offline tests and135-file public audit pass; c3dfb635 CI38866468848 passes both platforms. No production/editor or hardware changes.

13:18 IST context maintenance: used agent-context-maintenance skill. Updated project AGENTS with runtime-identity, prefetch-failure and live-expansion recovery rules; private parent guide points to the canonical report. Reviewed both global Codex/Claude adapters and shared router; their existing project links suffice, so shared sources/adapters remain unchanged. Pre-existing unrelated shared-repo edits were preserved. Frozen benchmark sources untouched.

13:24 IST correction/recovery:13:15:17 physical guard stopped80B at2.269GiB freeRAM during history383.359s; interrupted context unscored, private audit never started. ModelRSS/private stayed17.638/7.531GiB; outside-process growth not attributed, WSL grading is a possible contributor. Previous stale-log progress update corrected. No new WHEA/reboot. Changed recovery caps residentRAM at min14GiB/free-minus7, ncpu46, GPUKV, ubatch256; same stop floors. Fresh19.21GiB RAM/6573MiB VRAM passes preflight. New observer adds process-family memory; no grading/builds/downloads during retry. Completed Python/TS/SQL evidence retained.

13:48 IST checkpoint:80B recovery history completes1177.594s, max10102inputtokens, READY120 and6/6 facts correct, fresh revision2/retry0 read and honest inventory. One misspelled .clude path recovered; no unavailable-ledger retry. Public cap12.331GiB/readinessVRAM5.343GiB; GPU KV816MiB/state75.38MiB/compute885MiB. Normal stop. Fresh private audit now running on same recovery flags with14GiB actual resident maximum; about7GiB RAM free. No auxiliary grading/build/download during recovery or private inference. Full27-test code checks already passed10.775s and0af041392 CI38870392053 passes both platforms; new changes are reviewed evidence only.


14:05 IST planning checkpoint: checked live80B private process and fresh monitor;14GiB resident cap, about9GiB freeRAM, no stop receipt. Latest published6f4cc870 CI38872721288 passes both platforms. Reconciled stale model/memory guide statuses and moved16October task logs into their session. Prepared a separate Gemma31 publisher-temperature1.0 native-thinking profile after primary-source review; earlier0.6 preparation remains unrun. Froze matched Q4/Q6 three Python seeds plus TS/SQL/history and private audits. No heavy validation/build/download during inference; new profile checks await the quiet interval.


15:00 IST checkpoint:80B private audit ended at16-tool-turn limit in4075.125s, no final or code to grade.11distinct sources/10successful tool ranges/15rejections; repeated wrong Codex path. Public Python6/6, TS4/6, SQLFKfailure and six-fact history remain valid. Private peakRSS14.000GiB/minfreeRAM6.466/minfreeVRAM517MiB/maxGPU48C; no resource stop. Whole-system sampled reads254.5MiB/s and GPUutil18.4% describe paging, not isolated hardware throughput. Gemma31 download started; revised unrun publisher profile places first12attention blocks onCPU (909.836MiB spans),64KCPUq8KV,8threads,onecheckpoint,temp1.0. Offline exact-template markers support preserving current-tool thoughts while dropping older-user-turn thoughts; actualAPI check prepared. Full27tests pass10.166s; updated-profile manifest check passes, twoPSscripts parse,32flags advertised, runtime hash matches,138-file public audit0findings/diffcheckpass. No generated private code executed because none was delivered. Production remains unchanged/stopped.


15:28 IST checkpoint: Gemma31 full SHA verified after one download attempt. Publisher64 profile loaded on isolated runtime; CPU q8KV2720+531.25MiB, GPUweights4745.60/compute797.63MiB, readiness dedicatedVRAM5.648GiB. Early RSS17.202GiB/private9.795GiB, freeRAM6.687GiB. Exact READY smoke8.5s, five output tokens at1.20tok/s; not a quality score. ActualAPI template markers pass all three settings with string tool arguments. Public native-thinking collection running, private follows only normal completion. Updated critical review: CPU KV is ordinary CPU allocation in this pinned runtime, distinct from CUDA_Host buffers. 627889cb CI38881024701 succeeds. No heavy grading/build/test/download during inference; new evidence/docs await quiet-interval validation.


16:14 IST checkpoint: Gemma native public core remains active after about50minutes; seven source reads succeeded, reasoning completed and final text is streaming. Current processRSS17.202GiB/private10.022GiB/freeRAM5.384GiB; no stop receipt. Prepared a separate complete-layer15 placement diagnostic at an estimated4789.20MiB GPU weights, comparable to measured4745.60MiB current weights. Frozen2K/8K occupancy/history pair and owned-server helper are unrun; helper AST parses and targeted manifest/profile unittest passes. Defer both probes until native suite and quiet review finish, before Q6. Independent MTP review found14October upstream zero-free-memory fix newer than pinned runtime; no draft model downloaded or run. No heavy grading/build/download during inference.


16:36 IST checkpoint: Gemma Python/instruction answer completed3944.578s across3turns/7successful sources; final text begins2364.75s, last-turn prefill17.55/gen1.19tok/s. Source review confirms v2/loading/facts/inventory but wrong scalar-update exception and omitted test import. Preserved original six-method tests plus separately labeled combined-code variant, without repairs. No isolated execution yet; TypeScript/SQLite remains active. Production unchanged and no heavy auxiliary work during inference.


16:57 IST research checkpoint: rechecked and pinned Qwen/GLM publisher cards. Qwen table assigns SWE-bench73.4 to3.6 and75.0 to3.5-27B, not a3.6 thinking/non-thinking pair; GLM tau2 figure is not explicitly telecom-only. Updated critical review with source/scaffold caveats. Dense memory guide now separates fixed3251.25MiB activeKV from observed one-checkpoint growth3.322to425.013MiB. Gemma TS/SQL still running; no generated code executed or heavy validation during inference.


17:47 IST checkpoint: Gemma TS/SQL completed4463.031s across7turns/6successful reads; maximum input1226tokens, first final text3315.094s, final generation1.27tok/s. All visible turns and sources reviewed; missing plain-object validation and ineffective foreign_keys switch inside BEGIN identified. Original blocks packaged for quiet isolated grading, no execution yet. Python delivery milestones now recorded (first code48m58s, full implementation54m11s). Native history is running; private audit follows normal public completion. Same-generation RSS later fell17.2to14.2GiB while privatecommit stayed10.026GiB, cause unassigned. Added conditional repacking and dense Qwen27B research; no new candidate queue or runtime changes.


18:12 IST checkpoint: Gemma history first phase correctly returns READY120. Follow-up still active; server explicitly resets cached tokens to0 because the existing SWA checkpoint cannot restore the changed prefix. Four actual template/tokenizer pairs (no inference) show default preserve_thinking=false retains137 identical leading tokens versus10021 with true, at341 additional follow-up tokens. Counts exclude BOS; true remains untested for runtime speed/quality. Saved exact synthetic renders privately and aggregate public evidence. Native settings unchanged; no heavy auxiliary work during inference.


18:21 IST checkpoint: Gemma public history completes2029.031s across6turns, maximum10133inputtokens. READY120 and6/6 facts correct; fresh revision2/retry0, null absent port, truthful follow-up read. All6source returns match frozen bytes (5distinct files); no unavailable-ledger attempt. Follow-up first prefill9779tokens/513.073s/cache0; after file read10056cached/77new. Public normalstop;2079samples peakRSS17.202GiB/private10.034, minfreeRAM4.265/commit9.305/VRAM678MiB, maxGPU57C. Private audit now running PID64840. Generated code remains unexecuted until quiet interval.


18:33 IST metadata checkpoint: clarified QwenQ4 experimental-profile prose so the stock mmap failure is correctly attributed to Coder-Next80B. Q4 modified-runtime smoke passed earlier; matched quality remains unrun. All arguments, gates, runtime identity and tasks are unchanged. Archived the earlier frozen plan and refreshed only the description/hash (e26c20a24bd690ce53294b7dbcc91131070d2e40aba6ea5a53ea9f588643687c) before pair collection. Private Gemma audit remains active; no live inference settings changed.


18:49 IST checkpoint: private Gemma first tool turn completes1451.625s (1731generatedtokens); seven complete ranges succeed, including correct Codex guide/README. Together with the supplied entry, eight source texts exactly match the current maintained copies already reviewed; no read errors so far. Next request is17363tokens and reuses3547. Audit remains running/unscored. Added all-turn public timing breakdowns and318observer samples: mean disk4.19MiB/s (median0), server6.57CPUcore-equivalents, deviceGPU30.6%; shared-desktop scope, no causal kernel claim. No heavy work during inference.


19:10 IST effective-request audit: inspected actual private requests, which inherit legacy audit top_k20, preserve_thinkingtrue, max_tokens24576, seed73, temperature1/top_p0.95. These override Gemma publisher-profile top_k64/preservefalse/public coding max16384. Native thinking is still active. Coder-Next private likewise used top_k20 rather than server40. Reports now state actual controls; no frozen inputs or active settings changed. This is not a publisher-sampling private claim. Matched Q4/Q6 server/request top_k20 and preservation agree.


19:28 IST context-maintenance checkpoint: applied the maintained skill for the effective-request lesson. Project AGENTS now points to methodology for client overrides versus server defaults. Re-read Windows Codex/Claude adapters, shared guide/router and project adapters; existing links already route to project guidance, so adapters/shared sources are unchanged. Preserved the two unrelated dirty files in the shared repository. Frozen benchmark sources and active requests remain unchanged; validation/push await the quiet interval.


19:39 IST resource intervention: system freeRAM fell below4GiB while modelRSS/private stayed flat. Verified exact owned Gemma process, parent, executable/model/port and creation time, then used the existing read-back-checked working-set API to reduce only its cap19.218208 to17.202354GiB (the completed public-suite cap). Immediate freeRAM3.812 to5.764GiB; commit11.690GiB unchanged; native generation continues around1.12tok/s. Original profile, requests and initial-limit receipt are preserved, with a separate intervention receipt. Stop floors, cache capacity, model/placement/sampling and apps unchanged. Public result now labels the private timing intervention; no fixed-cap speed claim. Guidance clarifies original-request preservation and explicit intervention labeling.


20:00 IST checkpoint: public code remains unexecuted while the native private Gemma final streams. Added19:51:50 apps-open snapshot: 63.91GiB usable/5.62GiB available, serverRSS17.20GiB, Edge/Code/WebView summedworking sets7.97/7.26/1.59GiB and existingpagefileusage3.92GiB. These overlapping counters are not an additive RAM partition. Updated next-experiment status and moved late checkpoints into this session without deleting history. Diff whitespace check passed; full validation and generated-code isolation await the quiet interval. No active request or model settings changed.


22:58 IST continuation (owner: "continue"): verified native Gemma private completed20:19:33 with normal stop and unchanged boot. All returned sources and visible turns reviewed. Private26/36=16semantic+4citation+6code, 7234.171s; no mutable-alias bug, but missing guidance and inaccurate read inventory. Public isolated Python6/6, combined self-tests6/6, original standalone6NameErrors; TSstrictcompilepass5/6; SQLFKfailure. Four isolation preflights pass; no host execution.27offline tests pass10.666s, twoPSscripts parse. Original64K dense diagnostic rejected before load at6284<6400MiB freeVRAM. Preserved plan; froze both32K arms for unchanged2K/8K probes with6000MiB loadgate and unchanged stopfloors. Rewrote canonical report around verified outcomes; prior chronological text retained privately. Q6/matchedQ4 unstarted. No promotion, app closures or hardware changes.


23:37 IST dense placement checkpoint: two32K recall/history CPUKV arms completed with normal stops; all four requests byte-identical. CPUKV control/complete-layer 2K160.469/146.047s and8K457.610/462.234s. Default cache-offload follow-up2K146.109s; dedicatedVRAM5.906GiB. ActualGPUKV408+116.88MiB, weights4789.22/compute409.53MiB. Third8K stopped at394MiB freeVRAM below400floor during prefill; incomplete/unscored, no history follow-ups. Two shared requests byte-identical to second arm. No reboot; additionalVRAM consumer not attributed. Completed answers recover facts but add forbidden JSON fences; CPUKV changed/omitted history pass. These are budget0 recall diagnostics, not native coding scores. Desktop/resident-cap differences prevent isolated speed attribution. No grading/build/download overlapped. Q6 download and matchedQ4 quality follow; production selection unchanged.


23:52 IST pre-collection precision plan extension: Q6 transfer active, neither Q4/Q6 matched trial has started. Archived earlier five-task plan and added existing640-record context-large-v1 to both arms, alongside120-record history, threePython seeds and TS/SQL. Same profile hashes, requests controls, native thinking, six-hour deadline and frozen questions/checks. Previous Qwen input was about52K tokens; actual new usage must be measured. This extends long-file coverage before seeing either candidate answer.


00:31 IST17October Q6 start: full31843777504-byte pinned artifact/SHA verified after two resumed early transfers, E:5.30GiB free. Frozen six-task/profile checks pass; unloaded22.826GiB RAM/21.020GiB commit/6584MiB VRAM passes gate. Owned public PID56440 now runs native core-seed73; GPUweights4114.80/KV680/state62.81/compute566MiB. Actual resident cap17.777596GiB, ready dedicatedGPUcounter5.52484GiB. Smoke 3.609s returnsREADY. with extra period; transport only, not exact-format quality pass. Later private follows only successful collection/normal stop. No heavy auxiliary work during inference; mapped span is not RAM.

00:42 IST17October continuation (owner: "continue"): recovered current receipts
and ownedPID56440. Q6 core73 completed604.609s, two turns/seven complete source
returns. All visible content and source bytes reviewed; implementation/tests
packaged unchanged for quiet-period isolation. Correct v2 precedence,
missing-fact abstention and read inventory; bug diagnosis misattributes unknown
key omission and own tests omit retained nested-list mutation. Second seed
active; no executable score yet. Read project/parent guidance, shared Windows
guide/router/platform/logging, Python/testing/discovery/git/documentation rules
and grading methodology.2d1579dCI38951495133 succeeds. No active settings changed
or heavy checks run; final A–G remains pending the complete requested matrix.

00:47 IST research re-read: read the archived Gemini source across its full
sections and rechecked the Qwen publisher card. Additional pinned-code
correction: q4_0 uses18bytes/32values versusq8_0's34, so64K Qwen attention
payload is360versus680MiB, saving320MiB, not340. Confirmed local block-layout
file unchanged atb2f036c; two web fetches of that file timed out. This is a
calculation, not a q4 load/quality claim. Updated memory guide/critical review;
frozen q8 comparison unchanged. Diff check passes; quiet-period checks pending.

00:59 IST Q6 public checkpoint: three native Python repeats completed in
604.609/453.922/588.953s. Seven source returns each; all visible text and
source bytes reviewed. Separate unchanged implementation/self-tests queued
for quiet isolation; only core74's project import is mapped to candidate.
Core74/75 contain false empty-dict expectations. Core75 improves retained
nested-list mutation coverage but misdiagnoses dictionary/scalar control flow.
TS/SQL active after ordered entry/router/linked-source reads. No code grade yet.
Saved header comparison confirms identical chat template, architecture fields
and tensor shapes; skipped tokenizer arrays are not claimed identical.

01:12 IST source review and context maintenance: Q6 TS/SQL completed454.750s,
four turns/six full correct-path source reads. Reviewed all visible text; code
preserved for isolation. Plain-object validation is absent; SQL drops a referenced
table with foreign_keys ON. Final inventory has a typescript-ssql filename typo,
and the proposed uniqueness test conflicts with the pre-migration schema.
The120-record history input is active. Applied the context-maintenance skill to
the cache-state timing lesson in project methodology/comparison guide. Reviewed
Windows Codex/Claude/Continue/Copilot and project adapters; existing pointers
already cover methodology, so adapters/shared policy sources remain unchanged.
Shared repository's two unrelated dirty files are preserved. No active model,
request, sampler or resource-limit changes; no executable grades claimed.

01:21 IST continuation: checked receipts and livePID56440 before reporting the
large-history run active. The120-record case completed628.735s across six turns,
with all six facts, READY120, an actual changed-file reread and revision2/retry0
correct. Reviewed visible answers, marker lines and all returned source bytes;
no unavailable-ledger read occurred, so no error-recovery claim. Maximum input
was11396tokens. The640-record case is processing its larger input. Source review
and light documentation only; isolated grading/offline checks wait for inference
to stop. Corrected the Gemma result's stale placement-pending status and linked
the already-reviewed completed pair/interrupted GPU-KV follow-up. Recovered
project/parent/shared guides and current logs; final closeout remains pending.

02:12 IST Q6 public completion: all six cases collected; server stopped normally.
The640-record case completes3296.891s, READY640/all six facts/fresh runtime
revision2 and retry0 pass, max input51411. All visible turns/source returns
reviewed and returned bytes verified. Initial phase ends3248.360s; changed-file
phase adds48.515s, reusing51105 then51358 tokens. No unavailable-ledger attempt;
no error-recovery claim. The matching target facts across the two history
lengths are intentional controls, not independent knowledge questions.
Private audit now runs underPID63928/server-20261017-021105; controller30694
owns it. Fresh private preflight22.187GiB RAM/20.850GiB commit/6715MiB VRAM;
actual resolved resident cap17.243698GiB, no mid-run intervention. Code remains
queued for quiet isolation. Prepared ignored summary/tokenizer-comparison helpers;
both parse but have not run. The tokenizer check is deferred until inference
stops and reads only10.9MB metadata per verified artifact. Progress helper's
optional brief mode was exercised. No publication/checks or model retirement yet.


02:53 IST17October Q6 review checkpoint: all six public and private cases completed; five isolated grading preflights pass after inference stops. Python6/6 three times, own tests6/6,6/7,6/7; strictTS5/6, SQLiteFKfailure. Private28/36=19semantic+4citation+5code in2099.672s. Mutable alias confirmed; source review also finds local-only-key loss outside frozen check coverage.14actualsources/13ranges/2oversizeerrors; no port fabrication or execution claim. Full tokenizer metadata matches across Q4/Q6. Public report2026-10-17-qwen-precision.json added; matchedQ4 remains, production unchanged.


## Expanded comparison closeout

User prompt: "continue"; complete the five memory/model/research pointers preserved in the canonical task report.

**A. Business summary**

All five research points are complete. **My choice remains Qwen3.6-35B-A3B UD-Q4_K_M.** The alternatives did not demonstrate a better overall result for your instruction-heavy coding workflow.

| Model | Actual-instruction audit | Time | My take |
|---|---:|---:|---|
| **Qwen3.6 Q4** | **31/36** | **11m40s** | Keep it; strongest practical result in this comparison |
| Qwen3.6 Q6 | 28/36 | 35m | More memory, no demonstrated quality gain |
| Gemma 4 31B dense QAT | 26/36 | 2h00m34s | Correct private merge helper, weaker instruction coverage |
| Qwen3-Coder-Next 80B Q4 | Unscored | 67m55s | Repeated unavailable paths; reached the tool limit without a final answer |

These are small local tests, not universal rankings. [Full report and evidence](https://github.com/paras-lehana/local-coding-lab/blob/main/docs/tasks/2026-10-16-memory-and-candidate-expansion/2026-10-16-memory-context-and-expanded-model-tests-v0.4.0.md).

**B. Technical summary**

- **RAM/KV:** usable RAM is 63.91 GiB; applications/Windows occupied about 42.76 GiB at the initial snapshot. Qwen reserves **680 MiB q8 KV at 64K**, or **1,360 MiB at 128K**, at load. Occupied tokens grow inside that reservation; checkpoints can grow separately. Cache does **not** permanently remember omitted files or chat history.
- **Measured mapped Q4:** peak resident RAM **16.38 GiB**, peak private commit **6.21 GiB**, readiness GPU counter **4.65 GiB**; minimum device VRAM headroom **1.9 GiB**. These counters overlap and must not be added as independent allocations.
- **Recommended settings:** 64K context, q8 K/V, native thinking with no separate reasoning ceiling, 37 CPU expert blocks, other eligible tensors on GPU, and the explicitly verified mmap runtime. This is not an “ultra/xhigh” effort setting.
- Both Q4/Q6 passed all three public Python implementation runs, scored TypeScript **5/6**, and failed the SQLite migration. Q4’s roughly 52K-input history case passed in **12m04s**, versus Q6’s **54m57s**. Desktop load and cache differences limit speed conclusions.

Updated comparison/retirement evidence, memory/model/grading guides, research corrections and project logs. Published on `main`, evidence commit `116a67d`; **27 tests**, PowerShell parsing, public-content audit and Windows/Ubuntu CI passed.

**C. Your pointers**

| # | Pointer task | Original pointer text | Status | What was done |
|---|---|---|---|---|
| 1 | RAM and KV | “kv in ram shuld grow” | DONE | Tested 2K–120K input, CPU/GPU cache, retained and omitted history |
| 2 | Coder-Next 80B | “still should be tested” | DONE | Coding, history and actual-instruction audit; failure preserved |
| 3 | Dense Gemma 31B | “i can wait even longer” | DONE | Extended quality runs plus placement/cache experiments |
| 4 | Q6 comparison | “try the Q6” | DONE | Matched Q4/Q6 prompts, source review and isolated grading |
| 5 | Independent analysis | “dont read it blindly” | DONE | Corrected research claims using source inspection and measurements |

**D. Additional findings**

Extra checks exposed local-key loss and nested aliasing in **both Qwen private helpers**, including defects missed by the frozen score. Higher precision did not eliminate bugs.

Deleted the three verified non-leading weight files, freeing **91.29 GiB**. Q4, Gemma 26B and all reports/raw evidence remain.

**E. Pending and deferred**

| Item | Status / reason |
|---|---|
| Mapped Q4 in Copilot/Continue | Benchmark recommendation; new editor validation remains separate. Existing settings are unchanged. |
| Running server | Stopped. The old launcher needs roughly 24 GiB commit; the latest available allowance was 18.4 GiB. A guarded mapped-start command is documented. |
| Restart cause | Unresolved; these results do not identify a faulty component. |

**F. My recommendation**

Keep Q4 with **64K/q8/native thinking**. For your workflow, prioritize verified file reads, a source inventory, durable project notes and independent code tests. The evidence supports improving those controls before buying more precision or choosing a larger model.

**G. Manager copy block**

```text
What's done: Completed the requested model and memory comparisons. The existing Qwen model remains the best practical choice in these tests. Larger alternatives did not improve the overall result. Reports are published and unused model files removed.

Suggested next steps: Validate the recommended memory-saving setup in the editors, then test a real project change with explicit source tracking and independent checks. Continue reviewing generated code; every candidate has limitations.
```
