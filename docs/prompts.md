# Prompt log — Local Coding Lab

Current phase,26October: higher Flint precision, tuning research and incomplete
Qwen/other-model coverage explicitly reopened by the owner. See the new task
report. IQ3_S has native public52/60 and private29/36; two native coding
questions exhaust output without code. A separate4096-reasoning-ceiling control
passes its two completed coding cases. The cached capped suite completes12
answers with6passes; bounded IQ4 finishes public55/private29 but its coding
controls fail completion, and its exact file is retired. Native Q4 attempts
all12 questions with9 frozen passes,2 failures and1 output limit, plus two
extra JavaScript defects. A separate resident7/cache/general32K interval
times out without code. Higher Qwen plainQ6 is verified and its resident7
public router reaches1200seconds with seven reads and an incomplete answer;
a larger-residency follow-up also deadlines; exact Q6 is retired with evidence.
Gemma CPU26 public57/60 and private23/36 are reviewed; coding remains unrun.
All next-load profiles reject26October's2.169GiB availableRAM. FlintQ3XL
remains paused at68/276 checkpointed ranges; no inference is active.
Verified FlintQ4 misses both router deadlines and is retired.
Production is stopped during the active campaign; no new promotion.

Previous phase,24October: Recursive Flint evaluation and Claude reconciliation
are complete with explicit limitations. Standalone/comparison reports record
private29/36, router39/40, coding11 completed passes/12 and separate history8/8.
No full composite or promotion. Tested Flint weights are retired, Qwen Q4 is
restored unchanged, and the canonical closeout is recorded in the entry below.

Historical phase,19October: azllm/TurboQuant evidence is reviewed on
experiment/azllm-20261019. Six calibrated CPU/GPU profiles finish; the router
reads seven files but is interrupted by an unexpected restart before any final
answer. A corrected processor-cache event is logged during startup. Remaining
inference is withheld under the parent hardware-stop rule. No completed coding
score, model replacement or active production endpoint is claimed. Read the
19October report and recovery receipt before another load.

Previous phase,18October: Strata evaluation is complete with explicit limits.
Same-weight Qwen32K is faster but has code defects; full Flash fits10GB, while
four coding trials deadline. Its51K RAM-KV workflow returns an empty final;
two separate final-turn replays recover6/6facts, not a retroactive workflow pass.
Existing Qwen Q4/128K CPUq8KV/1800idle is restored and API-verified. Apps stay
open; clocks/drivers and editor settings are unchanged. No editor typing or
automatic experimental queue. Evidence466d2f1 is published on main and the
experiment branch; matching closeout is recorded below.

Last updated: 2026-10-26. Public project history excludes earlier credentials,
private instruction contents and raw editor chats.

| # | Date | Time (IST) | Topic | Type | Status | Link |
|---|---|---|---|---|---|---|
|19|2026-10-26|08:04|Resume comparison and grade saved Gemma audit|Research / Experiment|Partial; reports published, inference capacity constrained|[Entry](#resume-26-october)|
|18|2026-10-24|13:23 first trial|Higher precision, tuning research and unfinished candidates|Research / Experiment|Active|[Report](tasks/2026-10-24-precision-and-gaps/2026-10-24-precision-and-coverage-v0.9.0.md)|
|17|2026-10-23/24|21:55 start|Claude review and Recursive Flint|Research / Experiment|Done with measured limitations|[Entry](#recursive-flint-and-claude-review)|
|16|2026-10-19|22:14|Continue after the interrupted experiment|Recovery / Report|Evidence preserved; further inference withheld|[Entry](#azllm-and-turboquant-on-10-gb)|
|15|2026-10-19|18:40|azllm article and TurboQuant on10GB|Research / Experiment|Six probes complete; coding coverage partial|[Entry](#azllm-and-turboquant-on-10-gb)|
|14|2026-10-18|00:00|Strata on 10 GB|Research / Experiment|Published; Qwen restored; limitations explicit|[Entry](#strata-on-10-gb)|
|13|2026-10-17|21:05|Standalone tray and SSH access|Feature / Config|Published; remote editor UI untested|[Entry](#standalone-tray-and-ssh-access)|
|12|2026-10-17|20:12|Native idle sleep and desktop controls|Feature / Config|Published/tested; Copilot latency unresolved|[Entry](#idle-sleep-and-desktop-controls)|
|11|2026-10-17|19:35|128K and remaining tool pressure|Config / Bug Fix|Partial; superseded by desktop task|[Entry](#context128-and-remaining-tool-pressure)|
| 10 | 2026-10-17 | 11:49 | Copilot context failure and defaults | Bug Fix / Config | Mitigation applied; fresh UI deferred | [Entry](#copilot-context-rejection-and-persistent-defaults) |
| 9 | 2026-10-17 | 11:17 | All models, Gemini and availability | Research / Config | Report complete; persistent API restored; current UI separate | [Entry](#complete-model-inventory-and-availability) |
| 8 | 2026-10-17 | 03:57 | Complete expanded comparison | Research | Done | [Closeout](#expanded-comparison-closeout) |
| 7 | 2026-10-16 | 10:23 | KV growth and remaining candidates | Research | Five points completed; Q4 retained | [Entry](#memory-and-remaining-candidate-expansion) |
| 1 | 2026-10-14 | 22:35 | Establish reusable research repository | Infrastructure | Done | [Entry](#repository-creation) |
| 2 | 2026-10-14 | 23:12 | Start research: controlled Qwen placement | Research | Done | [Entry](#research-placement-experiment) |
| 3 | 2026-10-15 | 00:47 | Autonomous full research campaign | Research | In progress | [Entry](#autonomous-research-campaign) |
| 4 | 2026-10-15 | 15:17 | Recover after unexpected shutdown | Infrastructure / Research | Evidence reviewed; cause unknown | [Entry](#unexpected-shutdown-recovery) |
| 5 | 2026-10-15 | 20:58 | Working selection, comparison and editor gate | Research / Config | API done; UI blocked | [Entry](#working-selection-and-editor-gate) |
| 6 | 2026-10-15 | 23:06 | Actual editor validation after unlock | Research / Config | Six probes complete; quality defects retained | [Entry](#actual-editor-validation-after-unlock) |

## azllm and TurboQuant on 10 GB

Owner asks to try the attached24GB article on this PC, add the article/research
and measurements to the public repo, compare approaches/current reports, and
summarize the completed Strata work. Exact relevant request is in the task
folder's owner-input.txt; full article with private UI/account material stays
ignored. Read project/parent instructions, shared Codex/platform/router/host
and relevant v2 discovery, logging, Git, Python, coding and testing instructions.
Recovered complete Strata and model-inventory reports, methodology and grading.
No editor input, hardware changes, cloud calls or production stop issued.
Continuation request at22:14IST: "continue". Recovered the actual stopped
process state and preserved the interrupted run. Decoded the startup WHEA
record against installed SDK layouts; no claim that it proves restart cause
or RAM-speed blame. Further inference is withheld; no retry or production
start occurs after the new hardware evidence. Evidence commit `1faf278` records
the measured results; the matching prepared owner-facing closeout follows.

**A. Outcome**

**Done:** Published the [TurboQuant/azllm report](https://github.com/paras-lehana/local-coding-lab/blob/main/docs/tasks/2026-10-19-azllm/2026-10-19-azllm-and-turboquant-v0.7.0.md), measurements, reproducible settings and Strata comparison.

**Partial:** Six short tests completed. The instruction/code benchmark read seven files, then the PC restarted after **14m22s without a final answer**. It has no coding score.

**Not done:** Remaining coding/history and larger-context tests. **Keep Qwen3.6-35B-A3B Q4 selected; its server is currently off.**

**B. Results and analysis**

The article combines weight compression, compressed KV history, draft-token verification and prefix reuse. These address different costs; none automatically reads your instruction files.

Native azllm's selected dense model needs **11.35 GiB for its main layers alone**, exceeding this 10 GiB GPU. I built the separate compatible **llama.cpp-tq3** runtime to split those weights between CPU and GPU.

| Tested configuration | Short response | Generation |
|---|---:|---:|
| 28 GPU layers, no draft | 27.30s | 1.94 tokens/s |
| 24 layers + MTP | 30.09s | 1.79 tokens/s |
| 24 layers + DFlash2 | 26.59s | 2.09 tokens/s |

These were tiny, mostly 49-token answers, **not coding benchmarks**. DFlash2 was barely quicker than the simpler 28-layer profile and left less VRAM available.

At 28 layers, peak process RAM was **14.24 GiB**, total device VRAM **8.71 GiB**, and the **32K CPU q8 KV allocation was 1.06 GiB**. KV capacity is allocated ahead of use in this profile; occupied tokens grow within it. Restarting clears that working context.

**Strata:** My experimental fork handles optional MTP metadata and reduces redundant Windows memory residency. The same Qwen completed three workflows **1.14–1.76× faster** than the llama control. Python and history checks passed, but Strata's SQL migration failed and both engines retained TypeScript bugs. Strata Qwen at 128K remains unvalidated. Larger Flash-Next fitted, but four coding attempts exceeded 20 minutes; its original long-history workflow returned no final answer.

Validation: **38 offline tests passed**, four PowerShell scripts parsed, and the public audit checked **200 files with zero findings**. [GitHub checks passed on Windows and Ubuntu](https://github.com/paras-lehana/local-coding-lab/actions/runs/39290022175). No fresh editor test or completed new-code grading is claimed. The report lists every changed file, source read, dependency, build command and exclusion. Evidence commit [1faf278](https://github.com/paras-lehana/local-coding-lab/commit/1faf278) is published to `main` and `experiment/azllm-20261019`.

**C. Request status**

| # | Pointer Task | Original Pointer Text | Status | What Was Done |
|---|---|---|---|---|
| 2 | Publish research | “add it to our repo and report” | DONE | Report, source review, settings and measurements published. |
| 4 | Compare approaches | “summarize me about the difference” | DONE | Compression, caching, drafting and engine differences explained. |
| 5 | Explain Strata | “what did you do for strata” | DONE | Fork changes, measured gains and failures included. |
| 1 | Try and optimize | “try… optimize for our server” | PARTIALLY DONE | Compatible CPU/GPU route and six profiles tested. |
| 3 | Measure | “measure etc” | PARTIALLY DONE | Short-probe resources/timings complete; coding interrupted. |
| 6 | Resume work | “continue” | PARTIALLY DONE | Recovered evidence and finished reporting; further inference withheld. |

**D. Additional findings**

Windows logged a **corrected processor-cache hardware event** during startup. This does not establish the restart's cause or blame RAM at 2800. [The host instructions](/E:/llm/AGENTS.md) explicitly say to “stop on a new hardware error,” so I have not launched another inference run.

Only two verified, redundant Strata draft-source tensors were removed to recover **4.69 GiB**; packed artifacts, main models and earlier evidence remain.

**E. Pending**

| Item | Status | Reason |
|---|---|---|
| Complete router, history and TS/SQL tests | Deferred | New hardware event |
| Lower-reasoning diagnostic and 131K capacity test | Not run | Same stop condition |
| Restart production model | Deferred | Hardware stability needs review |

**F. My recommendation**

Keep the existing Qwen configuration. TurboQuant improves fit, but these measurements do not justify switching for coding. Strata is the more promising speed experiment, subject to its SQL and long-context limitations. Investigate the restart evidence before sustained testing, then resume the frozen cases without discarding the interrupted attempt.

**G. Copyable summary**

```text
Local Coding Lab — TurboQuant and Strata comparison updated, 19 October 2026

What's done
- The new article was reviewed against its implementation and adapted for the available graphics card.
- Six short tests completed. The dense model fitted by sharing work between the processor and graphics card, but generated only about two tokens per second.
- Drafting added memory use for little improvement over the simpler configuration.
- The research, measured settings and limitations are documented in the public repository.
- Earlier Strata tests completed three workflows faster, but retained coding defects. Its larger model repeatedly exceeded the twenty-minute coding limit.

Limits
- The longer instruction-and-code test was interrupted by another computer restart before delivering an answer.
- A new hardware error was recorded. Further model testing is withheld, and the selected model remains configured but stopped.
- There is no completed new coding score or evidence supporting a replacement.

Suggested next steps
- Keep the existing Qwen selection.
- Review the recurring hardware instability before sustained testing.
- Resume the remaining instruction, code and context checks using the preserved questions and evidence.
```

## Strata on 10 GB

Project: local-coding-lab. Branch: experiment/strata-20261018. Mode: Default.

Original request: try Strata, incorporate it in the comparison report, inspect
the believed12GB requirement and consider a fork if8/10GB becomes practical.
Use the supplied article as research input. Source: Niko1221/Strata.

Read: project/parent instructions, shared Codex/platform/topic/logging guides,
Python/Git/coding rules; Strata AGENTS, AI_SETUP, QWEN36 and relevant build,
loader, memory and server source. The complete supplied article is private.

Decisions so far: pin v0.1.45 and verify its Windows archive; no12GB hard gate
exists. Test the exact existing Qwen3.6 Q4 first. Its original release load
failed before allocation because optional non-MTP metadata was required.
Develop a small loader compatibility patch with geometry/layout regressions.
Qwen3.6 uses GPU KV and a full host expert arena, unlike Flash-Next's separate
memory paths. Download only pinned Flash-Next IQ3_XXS shards, with hashes, to
evaluate the memory-budget path. The broad setup command was blocked by
automatic review; the accepted alternative only downloads explicit artifacts
and does not perform setup's cross-install discovery or file relocation.

Validation and closeout: six Qwen workflow collections and isolated grading now
complete; Flash-Next remains in download. A forced memory-floor check has
verified owned-job cleanup while leaving an unrelated child alive.
Stock Qwen3.6 failure is preserved and is not a quality or VRAM-fit score.

01:37 IST checkpoint: experimental fork published at
https://github.com/paras-lehana/Strata/tree/experiment/qwen36-no-mtp . CUDA source
commit6ef632f; documentation21d48b3. No upstream PR or HIP/SYCL validation.
The no-download trim/no-trim32K control establishes a residency benefit. Initial
graph-enabled API profile hits the VRAM guard;64-token/no-graph profile completes
router286.516s, history250.625s and TS/SQL203.765s. Isolated Python6/6 and model
tests7/7 pass; public router review40/40 (one run, separate40-point rubric),
history6/6 facts; TS5/6 with nonplain-input failure; SQL fails during migration
on foreign keys. These are not editor UI or128K Strata quality results.
Same-weight llama32K comparison is active on8081: router completes436.469s;
history is running, TS/SQL remains next. Production8080 is still stopped for
the experiments and must be restored. Flash-Next has no verified shard yet:
the bounded range downloader is paused during timings. A preallocated working
file's length is not downloaded bytes. Owned Xet buffers were released and its
four incomplete files removed with an exact-path receipt. All apps remain open.
The context-maintenance skill was applied to the project regression guidance;
both Windows entry adapters were reviewed and left unchanged.

02:03 IST checkpoint: all same-weight comparisons and isolated grading complete;
llama history285.891s, TS/SQL357.687s; SQL passes6/6 while Strata's migration
fails. Published lab646dc2c on experiment branch and main; fork documentation
f17477d.38offline tests, four PowerShell parsers and183-file public audit pass;
11 upstream mock effort API tests also pass. Flash template header confirms
native xhigh/medium/low, high maps to xhigh, reasoning preservation defaults
true. Header-only inspection is not the full artifact hash gate. Range transfer
continues,64connections/~140MiB RSS. Production2.3 restored at02:03 with128K
CPUq8KV and1800second sleep; health/model alias pass, actual short answer is
READY. (extra period, not exact requested text),7.765s. This is availability
during download, not a performance or editor UI benchmark.

02:35 IST: real production idle cycle verified from native logs:1800.149981s
from idle to sleep, RSS0.57885GiB asleep. A new message wakes automatically and
answers exactREADY in25.062s. Full-duration timer gap from17October is now
closed; existing settings unchanged and no editor typing. This extra check
uses otherwise idle download time. See reports/2026-10-18-real-idle-cycle.json.

02:43 IST: found normal launcher/controller inventory ignored Strata names.
Added both native engine names. Harmless live marker programs prove Start
refuses each while preserving both marker and production; normal Start with
markers removed still recognizes the loaded baseline. No broad process kill,
new inference load, UI edit or atomic cross-launcher lease is claimed. The38
offline tests, four PowerShell parses and184-file public audit pass afterward.

03:02 IST: first Flash shard fully SHA256-verified; second still downloading.
Reviewed direct-GGUF unbuffered expert reads and the incompatibility between
elastic KV growth and a bounded resident expert budget. No Flash fit or quality
claim follows from these source checks. README status now matches VERSION0.6.0.

05:34 IST: MTP block and derived runtime verify.10GiB MTP router times out;
the accepted draft fraction alone did not improve throughput. Two fixed capped
probes at14GiB expert RAM reach8.8/9.6tok/s versus5.9/6.7 at10GiB, with reduced
file reads. These are unscored throughput probes with different cache/app states.
The14GiB complete router follow-up is running.128K/32K-resident KV with12GiB
experts and prefill-head aliasing remains a frozen conditional test, not evidence.

06:02 IST: full Strata comparison complete with explicit exclusions. Main
report records8Flash server trials/6workflow collections plus distinct RAM
probes/final-turn effort diagnostics, and the earlier same-weight Qwen pair.
38offline tests pass15.086seconds/4PSparses pass; production restored and
actually replies7.125seconds with extra period. Actual128K CPUq8KV and1800idle
verified. Context-maintenance source is projectAGENTS; both shared adapters
already route here and require no edits. No new editor UI, BIOS/driver/cloud
work. Final publication and matching visibleA–G record follow below.

### Final Strata closeout — prepared visible response

**A. Outcome**

**Strata runs on your 10GB card, but I recommend keeping llama.cpp as your daily setup.** The report and experimental fork are public, and your normal Qwen endpoint is restored. Actual 8GB hardware remains untested.

[Full report](https://github.com/paras-lehana/local-coding-lab/blob/main/docs/tasks/2026-10-18-strata/2026-10-18-strata-on-10gb-v0.6.0.md) · [Experimental fork](https://github.com/paras-lehana/Strata/tree/experiment/qwen36-no-mtp)

**B. Measured results**

| Setup | What happened |
|---|---|
| Qwen3.6-35B-A3B Q4 through Strata, 32K | Three tasks finished 1.14–1.76× faster than the llama control. Python 6/6; TypeScript 5/6; SQL migration failed. This is not a general 6× speedup. |
| Same Qwen through llama.cpp | Python 6/6, TypeScript 5/6, SQL 6/6. Its existing 128K configuration remains selected. |
| Full Qwen3.8-Flash-Next IQ3_XXS | Fits 10GB. Four coding attempts across three profiles hit 20 minutes. Increasing expert RAM improved short-probe speed, but did not produce a completed coding answer. |

Flash's **RAM-backed KV worked**: 1.55GiB host cache, 32K GPU-resident capacity, and real RAM reads beyond 32K. The 51.5K history task returned an empty final answer; unchanged/medium final-turn replays recovered 6/6 facts. Those recoveries are separate from the failed original workflow.

Validation: 38 offline tests, 4 PowerShell parses and 188-file public audit passed. The report lists actual files, sources, commands and exclusions. Evidence commit `466d2f1` is published on `main` and `experiment/strata-20261018`; fork code is `6ef632f`.

**C. Your requests**

| # | Task | Your pointer | Status | Outcome |
|---|---|---|---|---|
|1|Try Strata|“lets also try strata”|DONE|Two model paths tested|
|2|Update report|“incorporate in report”|DONE|Results and failures published|
|4|Experimental fork|“maybe make a fork”|DONE|Qwen compatibility/memory changes published|
|5|Compare results|“compare it to our current model reports”|DONE|Same-weight control and historical limits included|
|6|Review article|“Refer the report i attached”|DONE|Reviewed its claims; no hard 12GB gate found ([upstream guide](https://github.com/Niko1221/Strata/blob/v0.1.45/docs/INSTALL.md))|
|3|Smaller VRAM|“run it on 8 or 10GB”|PARTIALLY DONE|10GB measured; 8GB hardware unavailable|

**D. Additional work**

Verified the real 30-minute idle unload and automatic wake. Updated the launcher to refuse concurrent Strata engines. Your restored Qwen API answered in 7.1 seconds; 128K CPU q8 KV and 1,800-second idle settings were verified.

**E. Limits**

| Unverified | Reason |
|---|---|
|Actual 8GB, HIP/SYCL|Only this 10GB CUDA machine tested|
|Full 128K Strata accuracy, broad quality ranking|Smaller measured inputs and single samples|
|Fresh Copilot/Continue UI|Your no-editor-typing constraint remains|

**F. My take**

Keep **Qwen Q4 + llama.cpp + 128K CPU KV**. Strata is a useful experimental alternative for shorter tasks. Further work should target long-context memory support and reliable final-answer delivery before promotion.

**G. Copyable summary**

```text
Local Coding Lab — Strata evaluation completed, 18 October 2026

What's done
- Strata was tested successfully on this computer's 10GB graphics card. The tested release does not impose the assumed 12GB minimum.
- The existing Qwen model completed three smaller-conversation tasks faster through Strata, but coding errors remained, including a failed database migration.
- The larger Flash-Next model loaded successfully. Its tested coding answers did not finish within the 20-minute limit.
- Long-history testing used system memory as well as graphics memory. One response was empty; repeating the final request recovered all six facts. That recovery does not erase the original failure.
- A detailed report and experimental public fork were published. The existing working model was restored with its 30-minute idle unloading policy.

Suggested next steps
- Keep the existing setup for daily work.
- Treat Strata as experimental until longer conversations and answer delivery are more reliable.
- Validate actual 8GB hardware separately before advertising support based on this computer's results.
```

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


## Complete model inventory and availability

### Original request

> give me the report for all models tried and if any not tried with reason, pro con everything, refer your report, if that is not in report, refer your context and put that in report first.
>
> then reread the gemini report, summarize it what does it say, recommened etc for me
>
> also why cant i run the existing qwen model, do you always unload it after session?

### Recovered context and validation

Project local-coding-lab; branch main; all assets underE:/llm. Read project/parent
guidance, shared Windows/Codex/router/platform/logging sources, historical and
campaign reports and all833 archived Gemini lines. Do not equate incomplete
tests, accepted effort labels or old UI passes with completed current evidence.
No cloud requests or key access, downloads/deletions or hardware changes.
Used agent-context-maintenance for project lifecycle rules; shared Codex/Claude
adapters reviewed and unchanged.27 tests10.582s before load, fivePSparsers,
153-file audit0findings,174 relative file links resolved, diffcheck passed.
Implementation23f84b50640e8831bd966d1c3d7a78c6c92a6c02 published; CI39007400281
successful. Source bytes and all response content reviewed; source-value pass
and JSON-fence defect preserved. API/runtime changed, not editor credentials.
Actual current UI not rerun. No heavy grading while server runs.

### Canonical closeout

**A. Business summary — done**

I updated and published the [complete model report](https://github.com/paras-lehana/local-coding-lab/blob/main/docs/tasks/2026-10-17-complete-model-inventory/2026-10-17-all-models-gemini-and-availability-v0.4.1.md). It includes **14 tested model/quant combinations**, missing historical results, untested candidates, pros/cons and the Gemini assessment.

**My recommendation remains Qwen3.6-35B-A3B UD-Q4_K_M**, with Gemma 26 QAT as the smaller fallback. Higher precision and larger models did not demonstrate a better overall result for your instruction-heavy coding workflow.

| Model tried | Strengths | Problems / my take |
|---|---|---|
| Original **Qwen3-Next 80B IQ3_M** | TTL/LRU and DAG tests passed; about 7 tok/s; all 18 completed Python outputs parsed | Interval edge-case bugs; file audit incomplete after crashes; no native thinking. The results do **not** support “3-bit always breaks syntax.” |
| Dense **Qwen3.8-27B Q6** | Short code/source checks passed | Large audit cancelled after 229 minutes. Too slow in the tested setup. |
| Dense **Qwen3.8-27B Q8** | Corrected short checks passed | Long tests interrupted by restart or lowVRAM; no demonstrated advantage over Q6. |
| **Qwen3.6 Q4 — retained** | Private instruction audit **31/36 in 11m40s**; Python 6/6 three times; roughly 52K history passed | Missing instructions/citations, nested aliases, lost local keys and SQL bugs remain. Best measured compromise. |
| **Qwen3.6 Q5** | Python repeats passed; honest file inventory | Private 28/36, weak private merge code, TS/SQL failures. No established upgrade. |
| **Qwen3.6 Q6** | Python 6/6 three times; long history passed | Private 28/36 in 35 minutes; large history 55 minutes; same important logic defects. Adds 9 GiB without demonstrated benefit. |
| **Gemma 4 26B-A4B QAT — retained** | Smaller; Python passed; native SQL 6/6 and TS 5/6; long history passed | Private 19/36; weaker instruction retrieval and some count errors. Useful fallback. |
| **Gemma 4 31B dense QAT** | Python 6/6; private merge helper 6/6 | Overall private 26/36 in **two hours**; SQL and instruction/read-accounting failures. Waiting longer did not make it the winner. |
| **GLM-4.7-Flash UD-Q4** | Native f16-cache audit 27/36; honest source inventory | Other settings inconsistent; aliasing/count errors and SQL data-loss failures. Not promoted. |
| **GLM-4.7-Flash Q5** | Some Python runs 6/6; successfully loaded | Other runs 0/6; private 21/36; unread-file claims and unsafe SQL. |
| **GLM-4.7-Flash UD-Q6** | Completed private 24/36 | Inconsistent Python, TS compilation and SQL failures. More precision did not establish reliability. |
| **Qwen3-Coder 30B UD-Q4** | TS 5/6; coding-specialized control | Python 2/6,3/6,1/6; private timed out; no native thinking. Q6/Q8 remain untested. |
| **Kimi-Linear 48B Q4** | f16-cache loading worked; one Python 6/6; retrieved history facts | Cache compatibility issues, malformed tool call, SQL/count errors; 64K private audit rejected by memory gate. |
| **Qwen3-Coder-Next 80B Q4** | Actually loaded and tested; Python 6/6; recovered history passed | Private audit looped over wrong paths and produced **no final answer in68 minutes**. Huge memory/paging cost; not promoted. |

The private scores are out of 36. These are separate local test results—not a universal leaderboard. Interrupted answers are unscored, and older models used different questions.

**Not tried:** original Next 80B Q4 was bypassed under the initial memory plan; Coder 30 Q6/Q8 were proposed but the campaign selected UD-Q4; Qwen2.5-Coder 14B was never needed as the emergency fallback. Dense Qwen3.5-27B and several larger Qwen/GLM/Kimi/DeepSeek/Llama proposals never received verified local trial profiles. The report lists each group and its reason. OpenRouter produced **no completed comparisons** because the earlier account/IP restriction blocked it; no cloud ranking exists.

**What Gemini recommends:** I reread all 833 lines of the archived document you shared.

- Tune **Qwen3.6 Q4 first**; keep **Gemma 26 QAT** as the lower-memory alternative.
- Try GLM-4.7-Flash conditionally; treat Coder 30 as a non-thinking coding control and dense Gemma31 as a latency experiment.
- With applications closed and roughly 50 GiB free, explore higher quants, KimiLinear and Coder-Next 80B. Your apps-open tests are a different condition.
- Separate weight precision, KV/cache memory and offloading. Test real instruction routing, current files, missing information and long conversations—not just syntax or tokens/sec.

**My assessment:** useful direction, unreliable in several specifics. Its predicted GLM-Q5/80B impossibility was disproved by loading tests, although 80B remained impractical. Some architecture counts and a vendor-score attribution were wrong. It blamed an 8 GiB prompt cache when your configuration already disabled that cache. Its proposed flags and precision upgrades were hypotheses, not proven fixes.

**Why Qwen was unavailable:** the file was still installed, but the server had been stopped between experiments and not restored. The old launcher needed about 24 GiB available committed memory; Windows had around 19.5 GiB. Leaving you without the working endpoint was an operational gap.

**It is running again**, using the tested mapped approach. A greeting took 13 seconds; a two-file tool task took 69 seconds and returned all requested values correctly. It still added unwanted Markdown fences. This verifies the API, not a fresh Copilot/Continue UI test.

I am **leaving it running after this session**. It can stop on reboot, manual stop, failure or measured resource pressure. There is no automatic boot startup. Use [start-server.bat](/E:/llm/start-server.bat) to start it and [server-status.bat](/E:/llm/server-status.bat) to check it.

**B. Technical summary — done, with UI validation separate**

Current Qwen: **64K context, q8 K/V, native thinking, temperature 0.6**, most expert weights on CPU, mapped loading through the explicitly identified modified runtime. Snapshot: **13.3 GiB resident RAM, 6.1 GiB private commit and 4.7 GiB dedicated VRAM**. These counters measure different things and should not be added together.

Its attention KV reserves **680 MiB**, plus about 63 MiB recurrent state. Token occupancy grows inside that allocation. It is **not permanent file/chat memory**: the editor must supply history or reread sources, and restarting loses the live cache. Qwen3.6 has no verified native `ultra`/`xhigh` selector.

Changes: the report/owner-request pair, two evidence JSON files, mapped profile, README, CHANGELOG, VERSION, model/task/prompt indexes and project guidance. Local runtime configuration, start/status/stop scripts and parent guidance were updated with backups; generated logs remain private. The report contains the file inventory. No dependency, download, hardware or editor-credential changes.

Validation: 27 offline tests, five PowerShell parsing checks, public-content audit and relative-file links passed. Live health/model identity, IPv4/IPv6, actual file-tool responses and repeated-start behavior passed. Published on `main`, implementation commit `23f84b5`; [Windows/Ubuntu CI passed](https://github.com/paras-lehana/local-coding-lab/actions/runs/39007400281). Final documentation is also saved and published. No new editor UI pass is claimed.

**C. Your requests**

| # | Pointer task | Original pointer text | Status | What was done |
|---|---|---|---|---|
| 1 | Complete model report | “all models tried and if any not tried with reason, pro con everything” | DONE | Consolidated 14 attempted artifacts and explicit gaps before this reply. |
| 2 | Gemini assessment | “reread the gemini report, summarize it” | DONE | Full archived body reread; recommendations and corrections recorded. |
| 3 | Qwen availability | “why cant i run the existing qwen model…always unload” | DONE | Explained stopped server, restored persistent API and retained stop protections. |

**D. Additional findings**

Neither greater precision nor a passing syntax check guarantees correct code. Your most relevant remaining failures are incomplete instruction loading, unsupported file claims, nested configuration bugs and unsafe SQL. I also corrected the lifecycle guidance so benchmark cleanup does not leave the selected endpoint unnecessarily unavailable.

**E. Pending / deferred**

| Item | Status | Reason |
|---|---|---|
| Fresh Copilot/Continue UI checks | Not rerun | New launcher is API-verified; previous UI results belong to the older profile. |
| Untried variants and settings | Explicitly untested | Listed individually in the report; no scores invented or new automatic test queue started. |

**F. My suggestions**

Keep Qwen Q4 and the Gemma fallback. Next, prioritize held-out edits from your actual projects with explicit file-read receipts and independent tests—especially local-key preservation, nested mutation and database rollback—before another model swap.

**G. Copyable summary**

```text
Local Coding Lab — full comparison and working model restored, version 0.4.1, 17 October 2026.

What's done
- Consolidated 14 tested model variants, their strengths, failures and incomplete experiments. Untested alternatives have explicit reasons.
- Reread the supplied Gemini research and separated useful recommendations from claims contradicted by measurements.
- Retained Qwen3.6 Q4 as the best measured choice for this computer and Gemma 26 as the smaller fallback. Higher precision and larger models did not demonstrate a better overall workflow.
- Restored the local service and left it running. Basic conversation and reading two files completed successfully, although exact response formatting still failed. Fresh checks through both editors remain outstanding.

Suggested next steps
- Use the selected model with human review and independent tests.
- Prioritize real project edits, accurate file references and preservation of existing settings before changing models again.
- Check database changes carefully; several candidates produced unsafe migrations.
```


## Copilot context rejection and persistent defaults

Project: local-coding-lab. Branch: main. Type: Bug Fix / Config.
Date: 2026-10-17, 11:49 IST. Status: mitigation applied; fresh UI test deferred.

### Original request and subsequent constraint

> Not working, also why do i have to always choose allow all permission and autopilot, this should be default

The screenshots show the no-response query error with the local Qwen selected,
and the new mode/permission picker. No new screenshot was generated.

> Continue without typing in the editor for now

### Context, evidence and validation

The [single report](tasks/2026-10-17-copilot-context-defaults/2026-10-17-copilot-context-and-defaults-v0.4.1.md)
records the exact error, settings, source inspection, encrypted backups,
file inventory and remaining UI check. Static context was rejected before
inference. Only three User-setting keys were added; every existing value was
preserved. No editor prompt was sent. Tests: 27 offline passes, four PowerShell
parsers, JSON and encrypted-backup comparison. Publication checks are recorded
in the task log. No server restart, new inference, model download/deletion,
cloud evaluation, dependency change or hardware adjustment occurred.

Context-maintenance skill applied to project regression guidance. Shared
Codex/Claude adapters were reviewed and left unchanged because routing already
covers the lesson. Raw source transcripts and backups remain private.

### Canonical closeout

**A. Outcome — partly verified**

I continued without typing in the editor. **Qwen is running; Copilot rejected your message before sending it to Qwen.** Its system instructions and tool definitions exceeded its usable context budget.

I saved **Autopilot + Allow all as new-chat defaults**. The older enablement switches did not set defaults for this newer Copilot interface.

**B. Changes and checks**

- Added a Qwen-specific exclusion for external MCP tools to reduce context overhead. Built-in coding tools and your instructions remain available.
- Preserved all existing settings; encrypted backups verified. No model restart or dependency changes.
- **27 offline tests, four PowerShell parsing checks, settings comparison and public-content checks passed.** These do not prove a successful Copilot chat.
- Updated the project/parent guidance, README, editor guide, task/report indexes and prompt log. [Full report and file inventory](https://github.com/paras-lehana/local-coding-lab/blob/main/docs/tasks/2026-10-17-copilot-context-defaults/2026-10-17-copilot-context-and-defaults-v0.4.1.md). Published on `main`; evidence commit `581ba52`.

**C. Your requests**

| # | Pointer Task | Original Pointer Text | Status | What Was Done |
|---|---|---|---|---|
| 3 | No editor typing | “Continue without typing in the editor for now” | DONE | No prompt sent or chat cleared. |
| 1 | Restore chat | “Not working” | PARTIALLY DONE | Cause identified; context mitigation applied; fresh chat untested. |
| 2 | Persistent defaults | “allow all permission and autopilot, this should be default” | PARTIALLY DONE | Both configured; new-session UI confirmation pending. |

**D. Additional finding**

Chrome DevTools MCP also has an unresolved browser-address setting. I left it unchanged; it is not established as the cause of this failure.

**E. Pending**

| Item | Status | Reason |
|---|---|---|
| Fresh-chat response and default selections | Deferred | Honoring your no-typing instruction. |
| Chrome MCP configuration | Unresolved | Separate issue; repair not attempted. |

**F. My recommendation**

When you next use Copilot, **start a new chat** with the local Qwen model. Existing chats can retain old settings. Try “Hi”, then a cited file read. Keep the reduced tool set until those succeed; add external tools back selectively after measuring their context cost.

**G. Forwardable summary**

```text
Local Coding Lab — Copilot configuration updated; final interactive check pending.

What's done
- Identified why the local chat failed: the editor rejected the accumulated instructions and tool descriptions before contacting the model.
- Configured new conversations to start with Autopilot and Allow all selected.
- Reduced the external tools offered to the local model while preserving built-in coding tools and existing instructions.
- Verified that the model remains running, preserved the previous settings, and recorded the findings.
- Respected the request to continue without typing in the editor.

Suggested next steps
- Start a fresh conversation and confirm the default selections, a greeting response, and a correct file reference.
- Restore additional external tools gradually after the basic conversation works.
- Treat the repair as awaiting interactive verification, rather than confirmed working.
```

## Context128 and remaining tool pressure

17October2026,19:35IST. Configuration/bug fix, partially complete, then owner
redirected the task. This entry recovers the preceding interrupted session.

Original request: "not working. also why do i see 64K context. dont we need a
lot of cotnmext as our main issue was multiplle instruction file etc."
The owner also required continuing without typing in the editor.

The actual128K CPU-KV profile loaded with98304input/16384output and16384margin.
Native engine greeting and four-file test completed; all required facts were
correct but one citation was wrong. Native budgeting fixture used17tools and
reached its mock endpoint at both64K/128K; that is not inference. SDK/Qwen
tokenizer discrepancy motivated the margin. The70K experiment was deliberately
interrupted to release the sole slot for the owner's real greeting. That
greeting had28659prompt tokens,372.689seconds prefill and~7m42s final response
latency including queue time. It is a response, not a satisfactory speed fix.
The user clarified the same local window was in use; prior optional window
clarification is resolved. No assistant editor typing was performed.

Full implementation, evidence, sources and limits:
[128K report](tasks/2026-10-17-context128-and-tool-budget/2026-10-17-context128-and-tool-budget-v0.4.2.md).
No additional long-context score was assigned, and comparison work is stopped.

## Idle sleep and desktop controls

17October2026,20:10IST. Feature/configuration; project local-coding-lab, main.

Original request excerpts, verbatim:
> LEAVE THAT, i am trying it in the same window as yours. Now i wrote hi, saw 131K context but the response is stil not there after 2 minutes. Man do you even test thigns before changing. I see 7GB used VRAM, we could still use 3 GB, i dont think it is of use anyways.
>
> So what we can do is first have this idle configurationof 30 mins (i hope that it loads automatically when i start new message. do test). Also we build a cute good widget for task bar that shows current VRAM, GPU and RAM usage in text (coloured as per %) and also a icon like green or red which shows if the model is on or off. Cliocking the widget we can toggle also.
>
> Also use autohotkey to make a keybinding (easy to remember for local llm) which does this also shows a toast notification.
>
> Do test

The pasted research offered native sleep, Ollama, a game watcher and pystray.
Those were starting proposals; the explicit request above selected native
idle sleep, desktop resource control and AutoHotkey. No game watcher installed.

Pre-flight context: project instructions and task logs recovered on main;
existing owner model/settings retained; no editor input; guarded process
ownership, native Windows UI, E-drive installation and public-secret audit.
UI design/context-maintenance skill sources were read, and applicable shared
sources are listed in the task report. Native desktop QA applies instead of
browser/mobile validation. Existing authorization covers install/test/publish.

The [complete measured report](tasks/2026-10-17-idle-widget/2026-10-17-idle-widget-v0.5.0.md)
records the implementation, full file inventory, tests and corrected failures.
Native sleep/wake and desktop checks are complete. Canonical published response:

**A. Installed and running**

Press **Ctrl+Alt+L** or click the widget to toggle the model. It shows VRAM, GPU utilization and RAM, with colored readings and model status.

- **30-minute idle sleep is enabled.** The next message reloads a sleeping model. A manual **Stop** requires toggling it back on.
- After reboot, open [Local LLM Widget.lnk](<E:/llm/Local LLM Widget.lnk>).
- **Copilot latency remains unresolved:** your greeting eventually answered after about **7m42s**, including queue time.

**B. What I actually tested**

Two accelerated sleep/wake cycles answered short API prompts in **5.36s and 5.00s**, releasing about **3.77 GiB VRAM** during sleep. A longer generation survived the idle timer. Clicks, the global shortcut, tray reopening and notification callbacks passed. **37 tests**, PowerShell parsing and AutoHotkey validation passed.

The [full report](https://github.com/paras-lehana/local-coding-lab/blob/main/docs/tasks/2026-10-17-idle-widget/2026-10-17-idle-widget-v0.5.0.md) includes settings, screenshots, every changed file and defects caught during testing. Published on `main`, implementation commit [526fa28](https://github.com/paras-lehana/local-coding-lab/commit/526fa2859e848afb62e2eeb4628a3fefeb9bd8a3).

**C. Your requests**

| # | Pointer Task | Original Pointer Text | Status | What Was Done |
|---|---|---|---|---|
| 1 | Idle sleep | “30 mins… loads automatically” | DONE | Native sleep and automatic wake tested. |
| 2 | Resource widget | “VRAM, GPU and RAM… toggle” | DONE | Floating taskbar-edge widget and tray icon. |
| 3 | Shortcut | “autohotkey… toast notification” | DONE | Ctrl+Alt+L with Windows notifications. |
| 4 | Test behavior | “Do test” | DONE | Live lifecycle/UI checks and failure tests. |
| 5 | Slow response | “not there after 2 minutes” | PARTIALLY DONE | Measured and explained; speed not fixed. |

**D. Important findings**

The roughly 7GB VRAM reading includes other apps; it is not all model usage. I preserved the model’s reasoning and placement settings.

Sleep also clears **KV cache**. Copilot retains its saved chat, but must resend history, which the model processes again. [llama.cpp documentation](https://github.com/ggml-org/llama.cpp/blob/master/tools/server/README.md#sleeping-on-idle)

**E. Remaining limits**

| Item | Status |
|---|---|
| Faster actual Copilot responses | Unresolved |
| Full 30-minute elapsed soak | Not run; 15-second cycles tested, deployed 1,800 seconds verified |
| Fresh editor wake test | No editor typing; automatic wake verified through real API messages |

**F. My recommendation**

Use **Stop before gaming** to prevent background messages from waking the model. The next performance experiment should measure your actual instruction-heavy prompt and additional GPU expert placement; simply filling VRAM is not evidence of improvement.

**G. Copyable summary**

```text
Local Coding Lab — desktop controls and idle unloading installed (version 0.5.0, 17 October 2026)

What's done
- The model automatically unloads after thirty idle minutes and reloads when another message arrives.
- A compact desktop widget displays graphics memory, GPU activity and system memory, with clear model status.
- Clicking the widget or pressing Ctrl+Alt+L toggles the model and sends a Windows notification.
- Automatic wake, memory release, active requests, mouse controls, keyboard controls and tray reopening were tested. Problems found during testing were corrected.
- Model reasoning settings remain unchanged.

Limits
- The short wake tests succeeded, but they do not establish fast responses for large coding conversations.
- The earlier Copilot greeting took several minutes. That performance issue remains unresolved.
- Unloading clears the model's working context, so saved conversation history must be processed again.

Suggested next steps
- Stop the model before gaming when automatic wake is undesirable.
- Investigate the real coding prompt and GPU placement before claiming a performance improvement.
```


## Standalone tray and SSH access

Owner asked for a tray-first icon, hover/pinned draggable panel, configurable
metrics/hotkey/backends, remote-workspace access and a separate public repo.
Canonical original pointers, A-G closeout and measured report belong to
[LLM Tray](https://github.com/paras-lehana/llm-tray), the new target project.
This lab received documentation links only; its guarded custom control backend
and Qwen Q4/128K CPU KV/1800-second idle configuration remain unchanged.
Two remote API checks answer; fresh remote editor tests remain separate under
the owner's no-typing instruction. Public artifact excludes private host data.
No model downloads/deletions, cloud calls or social posts were performed.

## Recursive Flint and Claude review

23 October 2026; project local-coding-lab; branch experiment/flint-20261023.

### Original prompt

> awesome, there were some new changes and analysis done by Claude. Read them out, update your learnings, summarize also to me in the last.
>
> then get started with this: https://recursive.com/updates/introducing-recursive-flint
>
> It was just released, we test it on the same (latest) metrics after installing and make report (add it to current report and also make a seperate report about it, infact update claude project file, we do this for all as we might later need to publish blogs about each model tried and its comparison).

### Pre-flight context and progress

- Preserve Claude's existing changes (initial branch experiment/azllm-20261019).
- Read latest private local-llm skill/campaign and actual receipts before comparing.
- Keep installations under the owner's LLM data root; one engine at a time;
  apps stay open; no editor typing, driver/clock changes or broad process kills.
- Apply agent-context-maintenance to project guidance; standalone plus aggregate
  reports now required for each candidate.

22:14 IST checkpoint: separate runtime b11838 installed/hash verified; model
download nearly complete. Tests40pass17.222s, PSparserchecks pass, public audit
223files0findings at earlier checkpoint. Frozen comparison plan saved privately.
Reviewed Claude's actual LFM public-score/coding grades and candidate receipts;
incomplete cases and partial composite coverage remain explicit. Public
instructions do not expose private fixture text. Generated code is not executed
automatically: collection preserves raw requests/streams for review first.

Canonical A-G closeout appears below after the measured-result checkpoints.

23 October resume: owner said "continue". Re-read project guidance, methodology,
task report and mandatory shared logging protocol. Smoke succeeded; public
attempt a stopped after148seconds with no completed answer, no stop receipt
and no surviving controller/server. Windows boot remains00:14; no new relevant
hardware/restart/application-crash event found. Cause unknown, not a model score.
Saved separate recovery receipt; original manifest remains untouched. Attempt b
uses the same frozen profile/questions in a new directory and a hidden detached
controller, with the same resource gates and1200second prompt deadlines.

Follow-up: native attempt b deadlines at1200.031seconds with seven successful
reads and zero final content. Capped2048 variant transitions to API content near
three minutes, but review finds continued planning/revisions. Corrected the
early interpretation: channel transition is not a finished usable answer. No
quality or latency pass is awarded. Preparing a separate GPU-KV placement test
with two more expert blocks on CPU to preserve GPU headroom; not yet measured.

24 October final-measurement checkpoint: GPU-KV native router39/40, private29/36,
coding11 completed passes/12 with374/374 frozen checks on the complete answers.
CSV produces no final code by the output limit. A separate NaN TTL diagnostic
fails, outside the frozen score. Larger-output history8/8 in328.016seconds
is recorded separately from the original4K failure. No full public score or
composite/promotion. Exact Flint weights rehashed and retired; Qwen restored
unchanged at128K/1800seconds idle. API responds READY. in15.641seconds; the
period fails the exact-literal check. No new hardware event or editor typing.
Final offline41tests pass18.161seconds;4PowerShell files parse. Public audit,
publication and canonical A-G closeout follow.

### Canonical closeout — 24 October 2026

**A. Outcome**

Completed the Claude review and Flint evaluation. **Keep Qwen Q4 as the default for your instruction-heavy workflow.**

- **Claude's results:** Qwen Q4 remains the reference; Q5/Q6 did not improve its instruction score. LFM completed 6/12 coding tasks successfully; Bonsai failed to finish its workflow. Qwen's earlier 86.3 was a partial score, not a complete ranking.
- **Flint:** strong direct coding, but weaker instruction adherence and file-tool reliability. It does not replace Qwen based on this trial.

[Flint report](https://github.com/paras-lehana/local-coding-lab/blob/main/docs/tasks/2026-10-23-flint/2026-10-23-recursive-flint-v0.8.0.md) · [All-model comparison](https://github.com/paras-lehana/local-coding-lab/blob/main/docs/model-comparison.md)

**B. Measurements and implementation**

- Tested **Flint UD-IQ3_XXS**, llama.cpp b11838, native reasoning, 64K context and GPU q8 KV. No native `xhigh` setting exists in this template.
- **Private instructions: 29/36**, versus Qwen's 31/36. **Public router: 39/40.** These are single-run, agent-assessed scores.
- **Coding: 11 completed passes/12; all 374 checks on completed answers pass.** CSV exhausted its output budget without code. A separate test found that the cache accepts an invalid NaN TTL.
- **History diagnostic: 8/8 in 5m28s** with a larger output budget. The original history failure and file-driven TS/SQL tool-loop failure remain recorded; no full composite is claimed.
- About **10.2 GiB process RAM**, **5.47 GiB dedicated VRAM**, including **0.96 GiB GPU KV**; roughly **21–23 tokens/s**. CPU-KV variants both exceeded the router deadline.
- **Qwen is running again:** 128K context, existing 30-minute idle sleep. API reply took 15.6 seconds; its extra period failed the exact-format request. No fresh editor test is claimed.

Validation: 41 offline tests, four PowerShell parses and Windows/Ubuntu CI passed. Results commit: `1f8fa59`; published in the public repository's main branch. The report lists changed files, commands, sources read and limitations. Private evidence remains outside Git.

**C. Request status**

| # | Pointer Task | Original Pointer Text | Status | What Was Done |
|---|---|---|---|---|
| 1 | Review Claude | “Read them out” | DONE | Reconciled newer results and stop receipts |
| 2 | Update learnings | “update your learnings” | DONE | Updated campaign, skills and leaderboard |
| 3 | Summarize findings | “summarize also to me” | DONE | Summary above and full reports linked |
| 4 | Test Flint | “same (latest) metrics” | DONE | All three suites attempted and reviewed |
| 5 | Update comparison | “add it to current report” | DONE | Component scores and limitations added |
| 6 | Separate report | “make a seperate report” | DONE | Standalone evidence report published |
| 7 | Maintain guidance | “update claude project file” | DONE | Reporting required for future models |

**D. Additional work**

Fixed incomplete-stream evidence handling and misleading partial-score wording. Retired the verified LFM and Flint downloads after preserving evidence; retained Qwen/Gemma and reproducible installers.

**E. Untested items**

| Item | Status | Reason |
|---|---|---|
| Higher Flint quantization / larger context | Not tested | This trial covers the selected low-memory 64K configuration |
| Complete Qwen coding baseline | Missing | Historical reference lacks the twelve-task component |
| Repeated finalist / editor checks | Deferred | Flint failed promotion gates; your no-editor-typing constraint remains |

**F. My recommendation**

Fill Qwen's missing coding baseline first. If revisiting Flint, test higher precision and file-tool recovery as separate experiments. Its direct coding results are promising; they do not establish reliable unattended work across your instruction files.

**G. Forwardable summary**

```text
Local Coding Lab — Flint evaluation and comparison reports completed (version 0.8.0, 24 October 2026)

What's done
- Reviewed Claude's newer results and corrected comparisons that mixed incomplete and complete evaluations.
- Tested Flint across instructions, file-based workflows and twelve coding tasks. Eleven coding answers passed every standard check; one task produced no finished code.
- A separate history exercise passed with a larger answer allowance. The original unsuccessful attempt remains recorded.
- Found instruction omissions, unreliable file-tool behavior and an additional cache edge-case bug. Flint is promising, but these results do not justify replacing Qwen for this workflow.
- Published standalone and comparison reports, and made evidence reporting part of future model evaluations.
- Preserved the evidence, removed the tested Flint download and restored the existing Qwen service with its normal idle behavior.

Suggested next steps
- Keep Qwen as the default for instruction-heavy work.
- Complete its missing coding comparison before declaring an overall winner.
- Revisit Flint's precision and file-handling behavior through separate controlled trials, with independent checks on generated code.
```

## Higher precision and incomplete candidate coverage

Owner request,24October2026, verbatim:

> yes we should try higher quantization and we should deep research on how people are even makign it better.
>
> For qwen or any other model incompete stuff, please dcomplet.e

Active execution record: [precision and coverage](tasks/2026-10-24-precision-and-gaps/2026-10-24-precision-and-coverage-v0.9.0.md).
The previous phase's completed closeout remains historical. This new request
is still in progress; its final A–G summary will be recorded after the new
measurements, reports, checks and production-restoration outcome are known.

17:38IST progress checkpoint: IQ3 native public52/private29, separate capped
expert-cache coding6/12; bounded IQ4 public55/private29, coding now collecting.
Higher Flint Q4's two router deadlines remain unscored. Research and exact
artifact-label corrections are recorded. Public audit275files/zero findings,
four PowerShell parses and whitespace check pass; latest offline suite42passes
19.108s. No promotion or completed-campaign claim; remaining candidates and
production restoration are still active work.

20:40IST progress checkpoint: native Q4 completes all12 question attempts
across original/resumed runs:11 delivered answers,9 frozen task passes,2
failures,1 output limit. Two passing JavaScript answers also fail separately
recorded post-review diagnostics. Original RAM interruption remains preserved.
IQ4 native/presence controls fail completion. Flint Q4 exact-file retirement
after full hash frees space for the distinct plain Q6 download, now active.
42 offline tests pass in18.925s; four existing PowerShell files parse; public
audit283files/zero findings and whitespace check pass. An initial parse command
named a nonexistent install.ps1; corrected enumeration checks install-widget.ps1.
This is an in-progress checkpoint, with cached Qwen, higher Q6, other candidates
and production restoration still pending. No completed-campaign claim.

21:41IST progress checkpoint: smaller-resident Q4 calibration loads/smokes,
then its native32K-output interval request times out1200.016s without code.
TTL unrun after collector abort; no quality score. Memory/hardware guards
clear. ExactIQ4 retirement after fresh SHA funds higherFlintQ3XL. Q6 download
is active; Flint's ranges are paused to prioritize Q6 completion.42offline
tests pass19.199s (19.594s command wall),4PowerShell parses,audit289/0.
An initial PowerShell stderr pipeline exits1 despite42/OK; preserved original
and direct subprocess exit0 establish the test outcome. Primary-source review
adds ik Windows memory paths and community mixed-precision limitations. Work
continues on higher quants/remaining candidates; final A–G remains pending.

22:23IST progress checkpoint: plainQ6 full file is verified; resident7 public
router misses1200seconds after seven successful reads and an incomplete final.
Minimum freeRAM9.263GiB/commit6.313GiB/VRAM594MiB, no hardware event. The
fresh original18GiB profile rejects17.40GiB availableRAM; a distinct fixed10GiB
resident follow-up now collects with unchanged6.5GiB reserve and stop floors.
Its smoke completes6.672s. Gemma/K2 smaller-resident plans remain unrun.
Q6 paging observations and exact artifact/settings/result receipts are saved.

The ambiguous period in the READY smoke is now explicitly excluded from
quality conclusions; original requests, literal checks and scores remain.
Agent-context-maintenance reviewed project/shared routing; authoritative
docs/grading.md and projectAGENTS updated, Claude/shared adapters unchanged.
42offline tests pass18.544s, fourPSparses, audit294/0 and whitespace check pass.
Previous CI40110363216 Windows has a20s mocked subprocess timeout, Ubuntu
passes; automatic approval review rejects an unchanged failed-job rerun.
No CI success claimed for that checkpoint. Campaign and production restoration
remain active work; no final A–G or model promotion yet.

22:56IST progress: plainQ6 resident10 also misses1200seconds after seven
successful source reads; first visible824.609seconds, incomplete atcancel.
No quality grade. Original18GiB profile capacity-rejected at actual snapshots.
Fresh completeSHA and exact retirement22:46 preserve all evidence/Q4/Gemma.
Gemma26 resident8 public trial begins22:48; smoke2.141seconds, collecting.
CI40113657913 for1664022 passes Windows/Ubuntu; earlier Windows timeout stays
recorded. No inference overlaps downloads/grading; campaign still active.

23:19IST: Gemma26 first public workflow completes1031.860s. Six source reads
and all visible turns reviewed; code not executed while inference continues.
TS/SQL collecting with six valid reads, history pending. Saved model-specific
report and a separately frozen GPU24/publisher-sampling follow-up if needed;
its future private/coding requests would override topK64 with20 unless explicitly
changed, so no publisher64 claim is inherited. Added K2 report/placement plan.
Research checked current CUDA source against historical mixed-KV warnings and
re-read Flint's actual failed-tool trace. No model promotion or final closeout.

23:42IST: Gemma26 CPU28/resident8 public router38/40; TS5/6 plus SQLiteFK
abort0/6. History initial-phase4096-token reasoning-only limit789.282s is
unscored, so no complete public total. All code reviewed before WSL isolation,
after engine exit. Normal stop, no new hardware event. MinRAM6.394GiB,
commit4.837GiB/VRAM2143MiB;42offline tests pass,4PSparses,audit301/0.
CPU24/publisher load gate rejects6313MiB freeVRAM, no request. A separately
frozenCPU26 plan reducesGPUallocation by0.798GiB and keeps stop floors; it is
not yet tested. Campaign continues; original Q4 production remains preserved.

23:44IST: CPU26/publisher Gemma public collection launched, controller63408,
fresh16.104GiB RAM/11.275GiB commit/6263MiB VRAM. Smaller two-block GPU move
and public1/.95/64 sampler are explicit joint changes; original38/40 router,
5/12 TS/SQL and incomplete history remain.42offline checks pass18.770s,
fourPowerShell parses and public audit302/0. No new score or campaign closeout.

23:48IST: checkpoint2589946 pushed and CI40119849141 passes both platforms.
CPU26 smoke3.875s; measured GPUweights3137.64MiB,816.75MiB more thanCPU28,
same KV/compute buffers. Public router collecting; no quality/timing conclusion.

25October00:09IST: CPU26/publisher Gemma router completes889.985s; first
visible732.375s, six required reads. Source review records likely-correct
implementation but faulty generated isolation assertions; executable grade
awaits shutdown. TS/SQL collecting, history unrun. Research distinguishes
Linux RAM expert management, memory-costly host pinning and shorter-reasoning
post-training from a higher-bit quantization. No newly installed engine or
tested ThinkingCap model is claimed. Campaign and production restoration
remain active work; no completed-campaign summary yet.

25October00:32IST checkpoint: Gemma CPU26 public57/60, all workflows complete,
with missed linked instructions, TS object-validation and generated-test bugs
preserved. Source-reviewed isolated checks and semantic inventory correction
are hash-linked; original grader artifacts remain. Follow-up load gates reject
13.115GiB RAM, so higherFlint download resumes with no engine.42offline tests,
fourPSparses, audit304files/zero findings and whitespace check pass. New reports
do not promote Gemma or fill missing private/coding values. Remaining candidate
work and eventual production restoration continue autonomously.

25October00:33IST: public checkpoint8961410 is pushed and CI40123433820 passes.
Recovered15.559GiB RAM permits the missing Gemma private audit; controller82276,
native thinking, actualtopK20. Flint download pauses at68/276 ranges before
inference. No new private score, promotion or completed-campaign claim.


## Resume 26 October

Original prompt: ?continue? ? continues higher quantization, deep optimization
research and unfinished Qwen/other-model tests; no cancellation or new scope.

Preflight: project local-coding-lab; branch experiment/flint-precision-20261024;
apps remain open, one engine,1200second whole-prompt deadlines and no editor
input. Current dated resume follows a completed25October private collection.

08:04?08:10IST: source-reviewed Gemma audit23/36 (15semantic,2citation,6code),
798.6seconds. Final corrected code fence selected unchanged and all six frozen
checks pass in existing WSL isolation after engine exit. Raw private sources
remain outside Git. Public57/60 and private23 use topK64 versus20 respectively;
no direct-coding/composite result or promotion. Actual next-load RAM falls from
3.722 to2.169 then1.379GiB; all six queued profiles reject and download is
withheld. No new hardware event/boot. Apps and production settings untouched.
Research rechecks open hybrid-cache PR30594 head9177f03 and its unchanged
prefill/multi-token limitation; newer Strata terminal notes do not update Qwen
engine packages. Remaining collection/production restoration stay pending.

26October08:16IST: Gemma private23/36 export/review complete;42offline tests pass21.516s (22.110s command),4PowerShell parses pass. Public audit305/0 before capacity receipt, git whitespace check pass. Production admission also rejects1.916GiB freeRAM (needs18),8.423GiB commit (needs12),5385MiB VRAM (needs6000). No launch/remote-SSE test; settings/baseline preserved. No new hardware event. Current capacity report lists each unrun queue item; no campaign completion.


### 26 October capacity-constrained checkpoint

**A. Business summary.** Completed Gemma's saved instruction audit: **23/36**, alongside its earlier **57/60 public score**. Its merge code passes, but instruction handling and citations remain unreliable. Higher-precision Qwen Q6 exceeded 20 minutes in both tested profiles. Neither earns promotion.

Further inference is capacity constrained: about **2.3 GiB RAM is free**, while queued profiles need13.5–18GiB. Your apps remain open. Production Qwen is offline because its load checks also fail; its weights and settings are preserved. No background inference/retry is running.

**B. Technical summary.** Reports are published in [Local Coding Lab](https://github.com/paras-lehana/local-coding-lab/tree/experiment/flint-precision-20261024), report commit `e959c3b`, branch `experiment/flint-precision-20261024`.

- `docs/model-comparison.md`: updated Gemma score and current capacity limits.
- Gemma's standalone report: source review, selected corrected code fence, timing and memory evidence.
- Precision/coverage campaign report: remaining trials and their current dispositions.
- `docs/tasks/README.md`, `docs/tasks.md`, `docs/prompts.md`: index, progress and closeout.
- `research/reviews/2026-10-24-precision-and-offload.md`: optimization review and prefill/decode distinction.
- `reports/2026-10-25-gemma26-cpu26-private.json`: sanitized private score/settings/hashes.
- `reports/2026-10-26-resume-capacity.json`: load rejections and unrun checks.

Validation: Gemma code 6/6 in isolation; 42 offline tests, 4 PowerShell parses, 306-file public audit with zero findings, whitespace check and Windows/Ubuntu CI pass. Read project/shared guides, logging/router/host sources, local-LLM skill, frozen audit sources/rubric and actual answer/read trace. No new inference, editor test, dependency, runtime change or deletion this resume.

**C. Requested work status.**

| Request | Status | Result |
|---|---|---|
| “deep research on how people are even making it better” |DONE for current review |Published source-backed analysis; experimental gains kept separate from local measurements |
| “try higher quantization” |PARTIALLY DONE |Qwen Q6 and Flint Q4 attempts recorded; remaining Flint variants await capacity/download |
| “qwen or any other model incomplete stuff…complete” |PARTIALLY DONE |Gemma private audit finished; remaining collection blocked by current RAM availability |

**D. Additional findings.** Gemma spends about 6m22s processing input during its 13m18s private audit. Generation speed alone is an incomplete measure for your many-file workload. No new hardware error or reboot was found since the preceding trial.

**E. Pending work.**

| Work | Reason still pending |
|---|---|
| Gemma 12 coding tasks; Qwen remaining setting trial; K2 qualification |Current load checks reject available memory |
| Flint Q3XL/NVFP4 and Bolt |Capacity constrained; downloads incomplete or not started |
| Production Qwen and remote streaming verification |Requires 18 GiB free RAM, 12 GiB available commit and 6000 MiB free VRAM |

**F. Recommendation.** Keep Qwen selected. Complete Gemma's coding coverage, then K2 and the remaining Flint precision trials when load checks permit. Judge upgrades by correct completed tasks and actual file use; increasing quantization alone has not demonstrated a better everyday setup here.

**G. Manager copy block.**

```text
Local Coding Lab — comparison checkpoint published, 26 October 2026

What's done
- Completed the saved Gemma instruction audit. It scored 23 out of 36, alongside its earlier 57 out of 60 public workflow score.
- Its merge implementation passed all six checks, but it missed important instructions and supplied unsupported citations. It has not replaced the selected Qwen model.
- Recorded both higher-precision Qwen attempts that exceeded the twenty-minute limit. Incomplete answers remain unscored.
- Updated the comparison, individual model report and optimization research. Repository checks passed on Windows and Linux.

Current limitation
- Only about 2.3 GiB of system memory is available with applications open. The remaining candidates cannot currently load within the established limits. The selected model is also offline; its files and configuration remain intact.

Suggested next steps
- Finish Gemma's coding tests, then K2 and the remaining Flint variants once sufficient memory is available.
- Prefer evidence from completed coding tasks, reliable file references and whole-task response time over precision labels or generation-speed headlines.
```
