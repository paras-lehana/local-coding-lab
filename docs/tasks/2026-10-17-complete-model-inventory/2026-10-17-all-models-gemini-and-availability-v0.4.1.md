# All model trials, Gemini research and current availability

Version 0.4.1 · 17 October 2026 · Windows 11 / RTX 3080 10 GB / Ryzen 7 5800X / 64 GB RAM.

## At a glance

| Owner request | Outcome |
|---|---|
| Every tried model, strengths, failures and untested reasons | Consolidated below: 14 model/quant artifacts actually attempted, including three historical artifacts absent from the recent campaign table. |
| Reread and summarize the shared Gemini report | All 833 lines of the archived research reread; recommendations separated from local evidence and corrected claims. |
| Explain why the installed Qwen was unavailable | No server was running after benchmark cleanup; the old non-mapped launcher needed more available commit than this apps-open system had. Mapped persistent API restored; current editor UI not rerun. |

## Business summary

**Keep Qwen3.6-35B-A3B UD-Q4_K_M as the working choice.** This is a 35B-total,
3B-active MoE model with native thinking. It is neither the original Qwen3-Next
80B IQ3 nor the retired dense Qwen3.8-27B. Its weights occupy 20.614 GiB on disk.
Gemma 4 26B-A4B QAT Q4_0 remains a smaller fallback. All other completed
candidates were retired with their reports preserved; no weights were deleted
for this reporting task.

The priority is reading and following `.github` / `.claude` instructions,
linked rules, current code and documentation through a long conversation.
The winner is therefore the best measured compromise for that workflow on
this PC, not the highest parameter count or a claim of universal superiority.
Qwen Q4 still loses local configuration keys and can share mutable nested
objects incorrectly. It also missed rules and made unsupported citations.
It needs reviewed changes and independent tests.

## 1. What was tried: full inventory

The private instruction audit is **36 points**, combining semantics, citation
honesty and executable code. Public Python and TypeScript use separate six-group
behavioral checks. They are not percentages of general intelligence. Different
families/settings did not all receive identical reasoning budgets; only the
explicit matched comparisons support narrower comparisons. An interrupted or
unfinished answer is **unscored**, not zero. “Retired” means the exact weights
were removed after evidence preservation, not that the model is unavailable
upstream.

### Original installation and dense Qwen phase

| Model / exact quant | Completed evidence and strengths | Problems / limitations | Decision |
|---|---|---|---|
| **Qwen3-Next-80B-A3B-Instruct IQ3_M**, 34.128 GiB | Eight completed post-VRAM-reset code answers: interval subtraction 94/105 in each of three profiles, TTL/LRU 34/34 in three, DAG 64/64 in two. Eighteen completed Python outputs across pre/post-reset batches parsed successfully. Decode 6.79–7.87 tok/s, median 7.08. | Empty/reversed interval edge cases failed. No completed real-instruction/file audit. Eight effort/thinking probes produced the same output hash and no reasoning; the Instruct model did not acquire thinking through an `ultra` label. Two system crashes interrupted the broader campaign; causality was not established. | Retired 12 October. The observed bug was semantic; “3-bit causes missing syntax” is not supported by these results. |
| **Qwen3.8-27B UD-Q6_K**, dense, 20.474 GiB | Short low/medium/xhigh tests completed; the corrected historical summary records 16/16 boundary and 5/5 source checks across the compared dense settings. Native reasoning controls were inspected. | A large composite was cancelled after about 228.86 minutes; a roughly 42K-token prefill alone took about 42.6 minutes. That composite has no quality score. | Retired. The measured dense setup was far too slow for interactive file work. |
| **Qwen3.8-27B Q8_0**, dense, 27.052 GiB | Short xhigh checks also passed after correcting a false rounding penalty. No measured higher-precision advantage over Q6 on those short checks. | A long code run was interrupted by a restart after about 92 minutes; a later 64K file run stopped at 348 MiB free VRAM. Short generation was around 1.1 tok/s. No completed broad instruction comparison. | Retired 15 October. More precision consumed more resources without establishing a better result. |

The original IQ3 artifact's recorded filename is
`Qwen_Qwen3-Next-80B-A3B-Instruct-IQ3_M.gguf`; it is **not**
Qwen3-Coder-Next. Its 32K f16 attention KV was 768 MiB, plus 75.38 MiB
recurrent state, not the 16 GiB claimed in the earlier pasted advice.
These old tests used different fixtures from the later campaign. The recovered
[historical digest](../../../reports/2026-10-17-historical-inventory.json)
records source hashes and selected numerical results; the
[earlier findings](../../../reports/2026-10-14-findings.md) preserve context.

### Current Qwen family: weight precision and placement

| Model / exact quant | Completed evidence and strengths | Problems / limitations | Decision |
|---|---|---|---|
| **Qwen3.6-35B-A3B UD-Q4_K_M**, 20.614 GiB | Matched mapped audit **31/36 in 11m40s**. Public Python **6/6 in all three repeats**, strict TS **5/6**. Both history sizes passed; the larger reached 51,580 input tokens in **12m04s**, with a **54s cached changed-file follow-up**. Separate CPU-KV testing recovered facts at 119,943 input tokens. Actual older-profile Copilot/Continue transport was exercised. | SQLite migration failed FK enforcement; TS missed plain-object validation. Private helper retained mutable aliases and dropped local-only keys in separate diagnostics. Some generated tests had wrong expectations or missing imports. Both editors missed a Python-specific rule; Copilot cited an unread report. | **Keep.** Best completed instruction result at useful measured latency. The new persistent mapped launcher requires its own API/UI evidence, not an inherited UI pass. |
| **Qwen3.6 UD-Q5_K_M**, 24.639 GiB | Public Python 6/6 in matched repeats and native trial; private source inventory honestly identified 14 files. Audit **28/36 in 8m57s**. | Only **2/6 private code groups**; nested `None` handling and mutable aliases failed. TS 4/6; SQL failed. Different answer lengths mean the shorter wall time is not proof that Q5 is intrinsically faster. | Retired; no demonstrated workflow-quality gain for about 4 GiB more weights. |
| **Qwen3.6 UD-Q6_K**, 29.657 GiB | Three Python **6/6**, TS **5/6**, both history lengths passed. Private **28/36 in 35m00s**. Large history reached 51,411 input tokens; cached update was about 49s. | SQL FK failure, mutable aliases and local-key loss remain. Full large-history task took **54m57s**. Generated tests falsely rejected empty dictionaries. About 9.04 GiB more weights than Q4. | Retired 17 October. Matched evidence favors Q4 here; higher precision did not fix the tested errors. |

Q4 placement was also varied. A 2 GiB GPU expert-cache configuration was faster
on one audit (about 6m43s), but scored **27/36** and failed strict TypeScript.
A 3 GiB cache left only about 661 MiB free VRAM and did not improve the long
history task. The old non-mapped instruction profile scored 31/36, but its
private commit requirement made it unsuitable for today's available memory.
These are settings of the same weights, not extra models.

Budget-zero and 512-token reasoning diagnostics scored 3/7 and 5/7 on a known
inline code regression; a 2048-budget result passed 7/7 **after context and
placement changed**. This is not a clean proof of a reasoning-budget curve.
Use native thinking, preserve its history when the client actually sends it,
and keep an output ceiling. Qwen3.6 has no verified native `xhigh`/`ultra`
effort selector. An accepted API field is not proof it changes the model.

### Gemma, GLM, Coder and Kimi alternatives

| Model / exact quant | Completed evidence and strengths | Problems / limitations | Decision |
|---|---|---|---|
| **Gemma 4 26B-A4B, Google QAT Q4_0**, 13.448 GiB | Three capped Python 6/6. Native 64K TS **5/6**, SQL **6/6**. About 52K-input history passed in **10m32s**. Fixed Google revision loaded successfully. | Capped and native private audits both **19/36**: weaker instruction retrieval and merge logic. Earlier capped TS did not compile and SQL failed. One history count was 318 instead of 320. | **Keep as low-memory fallback**, not instruction-quality winner. Native SQL success is useful, not blanket migration certification. |
| **Gemma 4 31B dense, Google QAT Q4_0**, 16.439 GiB | Public Python **6/6**, TS **5/6**. Private merge code **6/6**; overall private **26/36**. About 10K history passed. | Private audit **2h00m34s**; public Python about 65m45s, TS/SQL about 74m23s, history 33m49s. SQL FK failure, missed instructions and misleading read accounting. Dense decode about 1.17 tok/s. GPU-KV 8K follow-up stopped at 394 MiB free VRAM, unscored. | Retired 17 October. Waiting longer did not improve overall instruction quality. CPU placement raised short decode to about 1.56 tok/s but left 8K latency around 7.7 minutes. |
| **GLM-4.7-Flash UD-Q4_K_XL**, 16.317 GiB | Native **f16-cache** Python 6/6 and private **27/36 in about 15m42s**; all 15 source reads honestly accounted for. | q8/capped Python 1/6, 5/6, 2/6; TS compile failure; SQL 4/6 with critical data loss. Native f16 history facts correct but count 243 instead of 120. Private helper mutated/aliased inputs. | Retired. Best completed GLM audit, but weaker than Q4 Qwen and configuration-sensitive. Do not attribute capped q8 failures to the f16 profile. |
| **GLM-4.7-Flash Q5_K_M**, 19.939 GiB | It loaded with apps open, contradicting a blanket “guaranteed OOM” prediction. Native Python 6/6 twice. Completed private rerun **21/36 in 12m30s**. | Native third Python 0/6; capped 5/6, 0/6, 0/6. Native TS failed compilation; SQL 5/6 included total data loss. Claimed four unread files. Earlier restart-interrupted audit remains unscored. | Retired; inconsistent code and poor file honesty. |
| **GLM-4.7-Flash UD-Q6_K_XL**, 24.378 GiB | Completed native audit **24/36 in 14m30s**. Some public Python behavior passed. | Capped Python 5/6, 0/6, 6/6; native 5/6. TS compile failure; SQL 5/6 still lost data. History count 242 rather than 120. | Retired; greater precision did not establish improved reliability. |
| **Qwen3-Coder-30B-A3B-Instruct UD-Q4_K_XL**, 16.452 GiB | Coding-specialized, non-thinking MoE control; TS 5/6. | Python **2/6, 3/6, 1/6**, SQL failed. Self-tests missed defects; one file defined tests without invoking them. Private audit reached 20-minute deadline, **unscored**. No native thinking mode. | Retired. This result is for UD-Q4, not the untested Q6/Q8 versions. |
| **Kimi-Linear-48B-A3B-Instruct Q4_K_M**, 27.997 GiB | Matching f16 K/V loads; small cache of 252 MiB plus 42.81 MiB recurrent state. Completed Python **4/6** and **6/6**; history facts retrieved. | One malformed tool call produced no implementation, unscored. TS 4/6, SQL syntax failure, count 242 instead of 120. q8 value-cache dimensions unsupported; mixed q8/f16 rejected. Private 64K load gate required 27.5 GiB free, had 26.893, so **private audit not run**. | Retired. Public inference was tried; do not describe the entire model as untested. |
| **Qwen3-Coder-Next 80B Q4_K_M**, 45.196 GiB | After isolated mmap-prefetch fix, loaded with apps open through file-backed paging. Python **6/6** in 13m14s; TS **4/6**. Recovered history task passed all facts/count/update in **19m38s**. | Stock mmap load nearly exhausted RAM/commit and was stopped. SQL failed foreign keys/wrong uniqueness. One history attempt hit RAM floor. Actual-file audit repeated a wrong path ten times and exhausted **16 tool turns in 67m55s without a final answer**: unscored. No native thinking. | Retired 17 October. **Actually tested**, including public code, history and private tool behavior; not a successful workflow replacement. |

Evidence: [campaign](../../../reports/2026-10-15-campaign.md),
[expanded experiments](../2026-10-16-memory-and-candidate-expansion/2026-10-16-memory-context-and-expanded-model-tests-v0.4.0.md),
[matched precision](../../../reports/2026-10-17-qwen-precision.json),
[exact pinned artifacts](../../../catalog/models.json),
[retirement receipt](../../../reports/2026-10-17-retirement.json).

### Practical use and ranking

1. **Working model: Qwen3.6 Q4.** Use for scoped Python changes, explaining
   supplied code, draft refactors and explicitly requested source-backed answers.
   Demand the exact files/ranges read, ask it to flag missing information and
   validate changed behavior externally. Its strongest repeated public result
   is Python; its weakest important areas include source completeness, copying
   nested configurations, type validation and database migrations.
2. **Low-memory fallback: Gemma 26 QAT.** Good enough to test when Qwen's start
   gate refuses the current capacity; weaker on this owner's instruction audit.
3. **No promoted third model.** GLM Q4/f16 is the best completed GLM instruction
   result, but data safety and variability remain concerns. Qwen Q5/Q6 failed to
   demonstrate a precision upgrade. Gemma31 and Coder-Next were much slower
   without winning the target workflow.

A numerical 1-to-14 leaderboard would overstate comparability: the old models
had different fixtures, several runs are incomplete, and some tests changed
placement/budgets. Within the completed private audits, Q4's31 exceeds Q5/Q6's28,
GLM Q4/f16's27, Gemma31's26, GLM Q6's24, GLM Q5's21 and Gemma26's19. These are
individual local results, not confidence intervals or universal rankings.

## 2. What was not tried, and why

| Candidate or scenario | Actual status / reason | What cannot be concluded |
|---|---|---|
| Original Qwen3-Next-80B Instruct **Q4_K_M** | Initial larger option was not benchmarked; the installation proceeded with IQ3 under the memory-priority plan. | No direct Q4-vs-IQ3 syntax or reasoning comparison. Do not invent an observed Q4 OOM. |
| Qwen3-Coder-30B **Q6_K / Q8_0** | Suggested in the early discussion, but the later campaign selected UD-Q4 as its coding control. No higher-precision run exists. | UD-Q4's poor results do not prove these versions fail or that they would improve. This is a remaining candidate gap. |
| Qwen2.5-Coder-14B **Q6_K** | Emergency fallback was never selected; retained Qwen/Gemma alternatives were available. | No local quality rank. An approximately11GB file cannot be promised to fit entirely in a10GB GPU with all overhead. |
| Qwen3.5-27B dense | A later research hypothesis after correcting a vendor-score attribution; no exact artifact/profile selected or tested. | Retired Qwen3.8 measurements are not measurements of Qwen3.5. |
| Qwen3.5-122B-A10B; Qwen3-Next80B **Thinking**; GLM-4.5-Air | Listed in the cloud comparison plan; no completed local benchmark. | No locally demonstrated fit, quality or reasoning comparison. |
| Alternate ggml-org Gemma26 QAT; GLM standard Q4_K_M | Fallback artifact variants were not needed/selected after the specific pinned Google and Unsloth artifacts loaded. | Different publishers/quants are not interchangeable measured results. |
| Larger mainline Kimi/GLM/DeepSeek/Qwen/Llama suggestions | No verified local artifact/profile established for the apps-open memory envelope. The Gemini report names GLM5.3/5.3Flash, full GLM4.7, DeepSeekV4/V4.1Flash, Qwen3.5-397B, Qwen3.8-Flash-Next125B and KimiK3; earlier discussion also mentioned GLM4.6Air, DeepSeekV3.1 and Llama4. These names/capacity claims are source proposals, not a newly verified release catalog. | Not benchmarked; do not turn a source's capacity estimate into measured impossibility. Coder-Next's paging result already disproves that style of blanket claim. |
| All “apps closed, about50GiB free” recommendations | Not tested: owner instructed keeping applications open. | Results here do not establish performance in that different operating condition. |
| Kimi64K private audit; Gemma31 GPU-KV long follow-up | Specific stages rejected/stopped by measured memory gates; the models themselves did receive other tests. | No completed quality score for those stages. |
| OpenRouter comparison | Earlier account/IP-allowlist403 blocked evaluation; records show zero completed cloud evaluations and zero settled/reserved experiment cost. Owner subsequently set it aside. | No cloud ranking and no claim about the account's current balance. No key or cloud request used in this task. |
| q4 KV quality; persistent slot restore; MTP; dense CPU repacking; alternative engines | Proposed, not established in this campaign. CPU q8 KV, context growth, GPU expert cache and dense placement were actually tested separately. | No promised speed multiplier, permanent memory or accuracy equivalence. |

The cloud plan contained nine identifiers: Qwen3.8-27B, Qwen3.6-35B-A3B,
Qwen3.5-122B-A10B, GLM4.7Flash, Qwen3-Next80B Instruct/Thinking,
Qwen3-Coder30B, GLM4.5Air and Qwen3-Coder-Next. Their inclusion is not a result.

## 3. Gemini report: what it says, and our assessment

Source: [the owner's shared document](https://share.gemini.google/LadMuhd0ajY0),
[archived body reread in full](../../../research/raw/2026-10-14-gemini/report.txt),
[retrieval provenance](../../../research/raw/2026-10-14-gemini/README.md),
[detailed critical review](../../../research/reviews/2026-10-14-gemini.md).
This task reread the saved research body, not a newly fetched revision of the
shared page. Its numbered citation placeholders did not expose usable links.

### Its recommendation for this PC

- **Tune Qwen3.6 Q4 first**, then use Gemma26 QAT as a lower-memory fallback.
  Try GLM4.7Flash UD-Q4 conditionally at32K; keep Coder30 as a non-thinking edit
  control. Dense Gemma31 must pass a practical latency gate.
- If roughly50GiB RAM becomes free, consider QwenQ5/Q6 and longer context,
  GLM higher precision, KimiLinear48B and Coder-Next80B. That condition differs
  from keeping the current applications open.
- Separate weight precision, attention KV, recurrent state, saved prompt caches,
  compute buffers, physical RAM and Windows commit. Native context length is
  not the same as memory currently available to the client.
- Start around64K/q8 cache, four generation/eight prompt threads and512/128
  batch sizes. Explore expert placement, preserved thinking, prompt/slot reuse
  and smaller context before replacing a useful model.
- Test actual instruction routing, v2 precedence, stale/current files, honest
  missing-fact answers, nested configuration bugs and long-chat recovery.
  Use repeated and held-out questions; include all tool turns in deadlines.

It proposed a20-minute workflow gate and a90-second greeting plus three-file
gate, and strong repeat/held-out quality thresholds. The owner later explicitly
allowed longer dense/80B/Q6 experiments. The source's proposed40-point rubric,
our public rubric and the private36-point audit are distinct; none of our
models has demonstrated all of the source's proposed acceptance requirements.

### What the evidence changes

| Source claim/proposal | Checked result / decision |
|---|---|
| An8GiB default prompt cache caused the stops | The installed profile already used `--cache-ram 0`. This diagnosis did not explain those stops. Keep prompt cache and KV distinct. |
| CPU KV must be pinned CUDA-host memory | The inspected runtime used ordinary CPU buffers for this path. Measure the actual backend. |
| Q5 GLM guaranteed OOM, 80B impossible with apps open | Both loaded under tested profiles. 80B required mapped paging and an isolated prefetch fix; loading did not make it practical. |
| Gemma26 has26 sliding-window and4 global layers | The loaded model has25 sliding-window and5 global layers. |
| Kimi has36 layers/128 experts | Loaded metadata has27 layers/256 experts:20 KDA plus7 full-attention layers. |
| Qwen3.6 thinking75 vs non-thinking73.4 on a vendor coding score | The75 figure belonged to dense Qwen3.5-27B, not a controlled thinking toggle on Qwen3.6. Different model/scaffold results cannot prove that toggle's gain. |
| q8 to q4 saves340MiB at64K | Block overhead makes the tested architecture's calculated reduction320MiB. Tiny relative to weights; q4 accuracy was not tested. |
| All CPU experts is equivalent to a partial expert-layer count | `--cpu-moe` and `--n-cpu-moe 35` differ. Record actual tensor placement rather than use a universal28-layer rule. |
| Prompt cache1536MiB and temperature0.35/min-p0.02 should be defaults | These are proposals, not proven best settings. Retained native0.6 and cache-RAM0 avoid silently changing the reference or consuming extra headroom. |
| QAT/template repairs are necessarily required | The pinned fixed Google artifact loaded and worked; proposed history-template changes have not been demonstrated to improve live inference here. |

**My assessment:** the report offered a useful experimental direction, especially
its workload focus and memory distinctions. Its confident capacity predictions,
some architecture facts and parts of its diagnosis were unreliable. Local tests
support its first-choice family and fallback more strongly than its precise
commands or claimed explanations. Higher weight precision, larger models and
more thinking are experiments, not automatic fixes for coding correctness.

## 4. RAM, KV and context: the practical answer

We did test context growth: approximately2K through120K tokens. In this
llama.cpp setup the attention KV **buffer is reserved at context creation**;
occupied token positions grow inside it. Resident RAM can still change because
of demand paging, touched buffers, checkpoints and compute allocations.
“The chat gets longer, therefore the allocated KV buffer must grow linearly
from zero” does not describe these runs.

For Qwen3.6, q8 attention KV is **680MiB at64K**, or **1360MiB at128K**,
plus about62.81MiB recurrent state in the measured one-slot setup. Dense
Gemma31's64K CPU q8 KV was **3251.25MiB**. The model architecture matters;
generic “32K always costs16GB” or “128K always costs8GB” numbers are wrong.
CPU-KV placement uses `--no-kv-offload`; `--offload-kqv` is not a command to
keep KV in RAM. The working mapped Qwen profile keeps its small KV/state onGPU
and most expert weights in RAM/file-backed mappings to use scarce VRAM well.

The separate128K CPU-KV recall completed in12m13s, versus10m10s for default
GPU/CPU placement. Both recovered the supplied facts, but added unwanted
Markdown fences. A follow-up with history retained access; a request omitting
that history did not. **KV is a computation cache, not permanent knowledge of
your files or chats.** The client must send the history/content or use tools to
reread files. A restarted server loses its live cache. Merely mentioning
CLAUDE.md, enabling “preserve thinking,” or allocating128K does not automatically
load every linked instruction or prevent client-side pruning.

The working64K clients keep a48,000-token input budget and16,384 output budget.
The installed Continue2.0.0 adapter's pruning and timeout semantics were
inspected; its1200000ms socket timeout is not a whole multi-tool-task deadline.
Keep file receipts and explicitly refresh changed sources.

## 5. Why Qwen was unavailable; persistent restoration

The model file still existed. There was **no active llama-server** after the
comparison. Benchmark processes are deliberately stopped between candidates;
the final working endpoint was not restored because the old non-mapped profile
needed about24GiB available commit. A fresh unloaded snapshot today had only
about18GiB free physical RAM and19.5GiB available commit. The previous report
said it was stopped, but leaving the working client without an endpoint was an
operational gap.

There is no intended policy of unloading a working model whenever the assistant
finishes. The replacement launcher explicitly starts a detached manager and
server, which stay running after the launcher/session exits. They stop on manual
stop, reboot, server failure or measured RAM/VRAM/commit/temperature/hardware
error conditions. There is no boot autostart or automatic retry loop.

The verified configuration2.1 uses the same Q4 weights and editor alias with
`profiles/qwen36-mapped-editor64.json`:64K, q8 K/V, native thinking, preserved
reasoning, temperature0.6, four/eight threads,512/128 batches, all eligible GPU
layers with the first37 MoE expert layers onCPU, mapped loading and no repack.
It uses the isolated `b11562-noprefetch-v1` runtime, **not stock llama.cpp**;
its SHA-identified change disables eager Windows whole-file prefetch. The stock
runtime and frozen comparison profiles remain intact.

Start gates:16GiB freeRAM,10GiB available commit,6000MiB freeVRAM. The latter
is a reviewed reduction from the frozen control's6500MiB based on measured
GPU buffers of about4532MiB and about4823MiB device delta, leaving estimated
headroom above the unchanged400MiB stop floor. The resident working-set cap
is computed as availableRAM minus5GiB, at most48GiB. Less resident capacity can
increase paging and latency; the earlier11m40s audit is not a timing promise
for this launch. Runtime stops remain2.5GiB freeRAM,400MiB freeVRAM,1GiB
available commit,84C GPU or a newly detected WHEA error.

Owner shortcuts remain:

- `E:\llm\start-server.bat`: explicit start, verifies health and alias; refuses a
  conflicting server and does not launch a second copy.
- `E:\llm\server-status.bat`: live process/activity/memory and last stop receipt.
- `E:\llm\stop-server.bat`: stop only the configured model/runtime/port process.

Fresh verification and memory snapshot are recorded below.
Older15October editor passes are not relabeled as passes of this changed runtime.

## 6. Technical summary, validation and scope

Architecture: preserve private weights/settings outside Git; publish the pinned
portable profile and reviewed results. Reuse the guarded lab launcher for
hash verification, single-server enforcement and monitored process ownership.
No new dependency, model download, cloud spending, hardware setting or editor
credential change. Local settings/scripts were backed up before replacement.

Files read included project/parent AGENTS, README, methodology, tasks/prompts,
model catalog, historical and campaign reports, full833-line Gemini archive and
critical review, original12October JSON reports, deletion receipts, current
runtime config and launcher/status/stop scripts. Shared Windows/Codex routing,
platform and logging guidance was followed. The context-maintenance skill was
used for the project lifecycle lesson; shared adapters need no routing change.

Validation before inference: **27 offline tests passed in10.582s**; both public
PowerShell scripts and the three installed launch/status/stop scripts parsed.
The profile plan and stop dry-run passed. A preliminary149-file public audit
had zero findings. Final audit, links, API and publication results follow below.
No benchmark-generated code was executed during live inference.

Public changes: this report and unchanged owner request; historical digest;
mapped editor profile; README, CHANGELOG, VERSION; model/task/prompt indexes;
project AGENTS lifecycle guidance. Local-only changes: runtime-config.json,
start-server.ps1, stop-server.ps1, server-status.ps1, generated server state/logs
and parent AGENTS; backups and raw smoke evidence remain ignored onE:.

## 7. Pending, recommendations and owner decisions

- No decision needed to finish this report. Retain Q4 and Gemma26; do not infer
  an upgrade from parameter count or quantization labels.
- New mapped-runtime editor UI regression is separate from API validation.
  The old six UI probes retain their actual instruction/citation failures.
- Untested variants/settings are explicitly enumerated above. They have no
  scores; reopening them is new experimental work, not a missing measured row.
- Prefer held-out real-project edits, source receipts and external behavior
  tests over repeatedly optimizing this one known merge fixture. Especially
  check alias isolation, local-key retention, type boundaries and SQL rollback.
- Keep persistent availability and resource-stop reporting part of closeout.
  Do not stop an unrelated production process during benchmark cleanup.

## 8. Screenshots and appendix

No UI screenshots were generated for this reporting task. No new visual/editor
pass is claimed. Raw private instructions, answers, keys and desktop content are
not public. This document is the single forwardable output for the
[verbatim owner request](owner-request.txt); original research is preserved
without rewriting its claims. Historical crash reports do not establish a RAM
clock, GPU, model or quantization as the cause of the unexplained reboots.

## 9. Final verification record

At11:07IST17October the new launcher returned ready while the detached manager
and server remained alive. A second start returned the existing process without
loading a second model. The exact-runtime/model/port stop dry-run selected only
that process and left it running. `health` and `/v1/models` succeeded viaIPv4,
localhost andIPv6. All model bytes and the isolated runtime identity were
verified before load. No new hardware event caused a stop in this run.

The native greeting returned exactlyREADY in **13.125s**. A subsequent two-file
tool request finished in **69.484s**, reading both allowlisted sources and
returning all nine requested values correctly, including `null` for an absent
port. Every returned tool payload matched its recorded source hash. It emitted
Markdown fences despite “JSON only”: **transport and factual values pass;
formatting fails**. Decode across the three tool turns was16.37–19.08tok/s;
this short smoke is not a new long-context benchmark or whole-workflow speed
guarantee. Current editor UI was not manipulated or revalidated.

At11:11IST, process resident RAM was **13.306GiB**, private commit **6.123GiB**;
system freeRAM **5.123GiB**, available commit **13.459GiB**, freeVRAM **1532MiB**,
GPU43C. The11:10 Windows GPU-process snapshot showed about **4.70GiB dedicated
VRAM**, while total GPU usage included desktop apps. GPU model/KV/state/compute
buffers are3381.34/680/62.81/408MiB. CPU mapped weight address range19118.08MiB
is not all resident at once. The resolved resident cap is13.306GiB, below the
earlier comparison cap; extra paging is possible. Process counters are not
additive proof of exclusive physical allocations.

Receipt: [availability and smoke evidence](../../../reports/2026-10-17-availability.json).
Local raw evidence is under ignored`local-data/2026-10-17-inventory/`; manager
logs under`E:\llm\logs\mapped-production-20261017-110646802`. The working endpoint
is intentionally left running. This report does not promise survival of a
reboot, manual stop or later capacity decline.

Final publication checks and commit are logged in [tasks](../../tasks.md) and
[the canonical closeout](../../prompts.md#complete-model-inventory-and-availability).

Publication11:17IST: implementation commit`23f84b5` on public main;
[Windows and Ubuntu CI](https://github.com/paras-lehana/local-coding-lab/actions/runs/39007400281)
passed.153 public files audited with zero findings;174 relative Markdown file
targets resolved (external URLs/anchors not checked). The final prompt log adds
more report links and is checked again before its documentation commit. Last
recorded11:14 live status remains13.31GiB RSS/4.70GiB dedicatedVRAM, with4.55GiB
system freeRAM; app usage fluctuates. Exact prepared final response persisted.
