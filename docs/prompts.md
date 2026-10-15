# Prompt log — Local Coding Lab

Last updated: 2026-10-15. Public project history excludes earlier credentials,
private instruction contents and raw editor chats.

| # | Date | Time (IST) | Topic | Type | Status | Link |
|---|---|---|---|---|---|---|
| 1 | 2026-10-14 | 22:35 | Establish reusable research repository | Infrastructure | Done | [Entry](#repository-creation) |
| 2 | 2026-10-14 | 23:12 | Start research: controlled Qwen placement | Research | Done | [Entry](#research-placement-experiment) |
| 3 | 2026-10-15 | 00:47 | Autonomous full research campaign | Research | In progress | [Entry](#autonomous-research-campaign) |

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
