# Prompt log — Local Coding Lab

Last updated: 2026-10-15. Public project history excludes earlier credentials,
private instruction contents and raw editor chats.

| # | Date | Time (IST) | Topic | Type | Status | Link |
|---|---|---|---|---|---|---|
| 1 | 2026-10-14 | 22:35 | Establish reusable research repository | Infrastructure | Done | [Entry](#repository-creation) |
| 2 | 2026-10-14 | 23:12 | Start research: controlled Qwen placement | Research | Done | [Entry](#research-placement-experiment) |
| 3 | 2026-10-15 | 00:47 | Autonomous full research campaign | Research | In progress | [Entry](#autonomous-research-campaign) |
| 4 | 2026-10-15 | 15:17 | Recover after unexpected shutdown | Infrastructure / Research | In progress | [Entry](#unexpected-shutdown-recovery) |

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
