# Task log — Local Coding Lab

Last updated: 2026-10-18 (Asia/Kolkata); Strata evaluation explicitly reopened.

## 2026-10-18 — Strata on 10 GB

| Task | Status | Evidence |
|---|---|---|
|Read article and verify current upstream|Done|Pinned v0.1.45; setup explicitly accepts 10 GB. Article compares different quantization/baselines.|
|Try Strata with guarded memory settings|Done with limits|Qwen32K and full Flash load on10GB; failed profiles retained. Production Qwen128K restored.|
|Compare coding/file/history performance|Done with limits|Same Q4 faster in Strata; Python/history pass, TS5/6, SQL fails. Flash four coding deadlines;51K history empty then diagnostic6/6 recoveries.|
|Assess 8/10 GB changes or fork|Done on10GB|No hardware gate removal needed. Public experimental fork has three separate opt-in/compatibility commits. CUDA tested; real8GB and HIP/SYCL untested.|
|Publish report and reproduction details|Final evidence ready|[Full report](tasks/2026-10-18-strata/2026-10-18-strata-on-10gb-v0.6.0.md); recommendation remains llamaQwen128K.|

Initial snapshot: 64 GB DDR4 / Ryzen 7 5800X / RTX 3080 10 GB, about25 GiB
RAM and6.8 GiB VRAM free with apps open. Installed driver617.42 supports the
isolated CUDA13 libraries. No driver, BIOS or application-closure changes.
The article's full text stays private; the public report will contain a review.

01:48 IST: all six same-weight workflow collections and isolated grading are
complete. Router wall time286.516s Strata /436.469s llama; history250.625/285.891s;
TS-SQL203.765/357.687s. Single samples with different placement/tool serialization,
not a general engine ratio. No current replacement recommendation. Both experiment
servers stopped; production will be restored after remaining guarded trials.
Offline suite38 tests passes. Range downloader integrity/recovery checks pass;
its allocation length is not download progress. A64-connection option remains
bounded to1MiB read buffers per connection; observed RSS140MiB, unlike Xet's
6.5GiB retained commit. Downloading remains outside comparative inference.

02:03 IST: restored production2.3 during the remaining download: health and
alias verified, short availability answer7.765s with an extra period.131072
context and1800second sleep unchanged. Public Qwen report published646dc2c;
fork documentationf17477d. No new editor typing or UI validation.

02:35 IST: native idle observation completes after1800.150seconds; sleeping
RSS0.579GiB. New API message wakes automatically and returns exactREADY in
25.062s. Apps/bounded download remain active. Later evidence closes the earlier
elapsed30minute test gap without claiming a controlled speed or editor result.

02:43 IST: normal launcher/controller now recognize existing Strata engines;
both live marker refusal checks and the normal already-loaded positive path
pass with production unchanged.38offline tests/four PS parses/public audit pass.

03:02 IST: first Flash-Next shard passes the pinned full SHA256; second shard
allocation/download remains in progress. Direct GGUF expert views support the
unbuffered file tier, avoiding an additional roughly40GiB expert copy. The
planned10GiB resident budget cannot use elastic KV growth; longer-context
trials must evaluate the separate KV streaming mode. No Flash inference yet.

03:36 IST: optional MTP metadata inventory resolves31tensors/5,214,301,696bytes
at its pinned Qwen revision; weights are not downloaded/enabled. Preparation
needs STRATA_GGUF_PY pointing to the existing pinned llama/GGML checkout.
Its Python module and Q2_0 support pass an import check; no extra install.
The conditional larger history question was also frozen before inference.

03:54 IST: both Flash shards passed full SHA256. Pack creation completes in
4.906s,1.43GiB dense arena, no additional precision conversions. The template
hash difference was Windows newline normalization, not changed model content.
Initial --spec0 is rejected by the native pack before model loading; --spec2
without MTP/suffix drafts is the required one-token path. The1200MiB reserve
trial stops at539MiB freeVRAM.3072MiB reserve loads; actual device free memory
is much lower than the engine's own free-VRAM print. Preserve both readings.
The quality profile turns default STRATA_ROUTE_TAIL_SKIP7 off (all routed
experts computed), retains10GiB pinned experts and selects automatic2304-token
prefill chunks. READY answers exactly in13.531s, decode7.0tok/s,0drafts. Router
collection now runs under its1200second deadline. Production is intentionally
stopped through its controller for this single-engine experiment.

04:17 IST: Flash router reaches1200.016seconds and is retained unscored. The
native log confirms disconnect cancellation; memory remains above the floors.
History collection begins on the unchanged profile. Conditional MTP and128K
KV-streaming follow-ups are frozen; the31-tensor draft download is not started
during inference. Windows open-file directory sizes can lag actual SSE bytes;
direct event reads confirm reasoning streams normally, correcting an initial
buffering suspicion. The model's slow complete-answer delivery remains real.

04:39 IST: no-draft Flash baseline completes with history6/6 in219.015seconds,
router and TS/SQL each deadline1200.016seconds/unscored. Cancellation confirmed;
owned server explicitly stopped before pinned MTP download begins. Peak engine
RSS14.300GiB, minimum RAM9.325GiB/commit7.116GiB/VRAM780MiB. No guard/WHEA
stop in that run.38offline tests pass15.283seconds; four PS parsers/diff check
pass. MTP and128K KV-streaming remain conditional, not measured results yet.

05:00 IST: all31MTP tensors verify (5.214GB,667.812seconds download including
a rejected incomplete-range retry). q2_0 packing348.453seconds and runtime
relayout3.828seconds complete; derived hashes are saved. MTP/spec4 with the
English/code subset loads at32K. READY13.125seconds,26generated tokens,
18/21drafts accepted, native6.0tok/s: not a speed claim. Main GPU expert cache
falls904→361slots and auto prefill2304→256tokens. Router comparison is running
as flash-mtp-router under the unchanged1200second limit. Production remains
stopped; restore it after experiments. A conditional14GiB RAM-budget variant
is frozen from measured headroom; not loaded. No actual8GB or editor test.

05:34 IST: MTP10GiB router also reaches1200.016seconds/unscored. Two capped
throughput probes per profile measure5.9/6.7tok/s at10GiB versus8.8/9.6 at14GiB,
with reduced file reads; desktop/cache states differ and these are not quality
scores.14GiB router runs with a declared16,384output cap, unchanged2048thinking
ceiling/1200second deadline. Initial RSS17.8GiB, freeRAM6.4/commit3.4GiB.
The conditional128K plan uses12GiB experts,32K resident GPU KV,3584MiB reserve
and prefill-head aliasing; it is not yet a measured result. Production remains
stopped only for sequential experiments. Report/source provenance updated.

05:44 IST:14GiB router also deadlines1200.016seconds; final-turn cancellation
7936tokens/1148seconds/7.0tok/s, unscored. Further MTP coding repeats deferred.
Owned server stopped.128K12GiB/MTP/head-alias loads but immediately crosses
theVRAMfloor at566MiB, guardstop14.844seconds before any quality request.
Frozen no-MTP10GiB128K fallback loads, reports1.55GiB pinned hostKV and32K
GPU window,799expert slots/1536prefill. READY14.313seconds exact; frozen larger
history case running. No fresh editor UI or actual8GB claim. Restore production
after this context check; no candidate promoted.

05:54 IST: larger history reaches51,534input tokens; actualKV streaming reads
fromRAM and phase0exactREADY640 pass. Phase1 rereads changed runtime but returns
only reasoning/empty final content at lastSSE468.078seconds; original status
empty/unscored retained. Two final-turn diagnostic replays frozen separately.
Unchanged replay returns6/6facts in49.296seconds with a warm51,529token prefix;
medium-effort replay is running and requires full prompt processing. No fresh
file reads in those replay requests; they reuse delivered tool history and do
not turn the original workflow into a pass. Production still awaits restoration.

06:02 IST: medium final-turn replay returns6/6facts in314.438seconds, including
253.966seconds full prefill; unchanged replay49.296seconds uses cached input.
No effort-speed ranking or retroactive whole-case pass. Strata owned job stopped;
38offline tests pass15.086seconds,4PSparsers pass, public audit clean. Production
Qwen restored, health/alias/actual128K CPUq8KV/1800idle verified; API READY. in
7.125seconds adds an unwanted period. Endpoint left available. No editor test,
clock/driver changes, cloud calls or automatic comparison queue. Final report
and public aggregates ready for publication; all limitations remain explicit.

## 2026-10-17 — Standalone tray controller

The owner requested compact notification-area meters, hover details, pin/drag,
configurable shortcuts/launchers and remote-workspace access. That work lives
in [LLM Tray](https://github.com/paras-lehana/llm-tray), public0.1.0. Actual
native UI/lifecycle checks and13offline tests pass; remote API requests pass
through two loopback SSH tunnels. Fresh remote editor chats remain untested
under the no-typing constraint. No cloud calls or model comparisons resumed.
This lab's `desktop/control.ps1` remains the guarded custom adapter; current
Qwen Q4/128K CPU KV and1800second sleep are unchanged. Owner shortcuts target
the new UI. Its task report and prompt log contain the full closeout.

## 2026-10-17 — Idle sleep, widget and shortcut

Owner redirected work from comparisons. Latest task is30minute native idle
unload, automatic wake, colored text resource widget and AutoHotkey toggle
with notifications. No editor typing, model download or placement change.

| Task | Status | Evidence |
|---|---|---|
|30minute idle/automatic wake|Done|Native15second path tested twice; production1800seconds verified.|
|VRAM/GPU/RAM widget and clicks|Done|Native meter, status dot/tray icon, click stop/start/wake and actual tray restoration.|
|AutoHotkey toggle/notifications|Done|Ctrl+Alt+L global stop/start; Windows delivery callbacks.|
|Validation|Done|35tests pass14.317s, sevenPSparsers, AHKvalidate, native screenshots and hidden reload.|
|Copilot latency|Unresolved|Owner's actual greeting took~7m42s; lifecycle feature does not fix prefill.|

19:35 onward: runtime help/local source confirmed native sleep and passive
props/health/models. Pinned AutoHotkey2.0.30 archive verified and installed on
E-drive. Initial idle-test collector stdout inheritance fixed; test continued
against the same15second server. Two wake responses5.359/5.000s;28.5s active
request survived15s idle threshold. VRAM drop3857MiB; final RAM16.907→0.638GiB.

19:48–19:56: widget sleep-wake click, global shortcut and separate click cycle
completed. First stop refused a valid venv-wrapper PID relationship; exact
live ancestry check fixed, then passed. Production2.3 started with1800seconds,
same131072context, model alias and inference settings. No broad process kill.

20:02–20:04: actual Windows tray overflow icon restores hidden widget after
explicit left-click callback fix. Hidden-window exit persistence bug fixed;
single-instance hidden reload passes. Screenshots actually viewed; palette
contrast8.11–11.40:1. Current resources and identity saved in private receipts.

See [one forwardable report](tasks/2026-10-17-idle-widget/2026-10-17-idle-widget-v0.5.0.md).
Raw evidence is ignored local-data/2026-10-17-desktop-control. No elapsed30minute
soak or newly typed editor wake test is claimed. Native guard stops/manual
stops do not automatically restart. Server and widget are left available.

20:12IST publication: implementation526fa28 pushed to public main; GitHubCI
39041761773 completed successfully. Final37offline tests passed14.593s,
171-file public audit has0findings and202relative Markdown targets resolve.
Only exact path/hash-reviewed widget crops are exempt from binary rejection;
new/modified images still fail. Canonical A-G closeout saved in prompts.md.

## 2026-10-17 evening — 128K context and tool-budget repair

Historical work, now closed partial: owner reports still broken and asks why only64K for many instruction
files. No editor typing remains in force. New1.142.0 logs again reject static
context despite applying native mcp:* exclusion. External editor tools can be
custom tools; updated Qwen-only scope to builtin:* with mcp:*/custom:* excluded.
Native SDK loopback fixture measures15,245 system +6,737 tool +67 conversation
tokens,17 native tools, and succeeds at both64K/128K. Fixture is not inference.

19:05 IST: idle64K server gracefully stopped via owned stop request. New
production2.2 profile qwen36-mapped-editor128-cpukv loaded, PID74684,
manager47660, run logs mapped-production-20261017-190514105.131072capacity,
q8CPU KV1360MiB/state62.81MiB,3381.34MiB GPU weights/439MiB GPU workspace.
Client budgets110000input/16384output/131072total. Native thinking unchanged.
Six DPAPI backups verified;27 offline tests pass10.444s before inference.

19:09 IST: installed Copilot engine native greeting returnsREADY. Captured
68,818-character system text and four allowlisted source-file test running in
isolated SDK session; no editor input. It read all four files successfully;
final answer not yet reviewed. Greater-than64K input/history test planned next.
Read-only UI saw an SSH project window; optional owner clarification about
which window fails is pending. Local endpoint remains one slot with guards.
See [new report](tasks/2026-10-17-context128-and-tool-budget/2026-10-17-context128-and-tool-budget-v0.4.2.md).

19:15 IST: actual installed-engine source test completed378.437s, four reads,
correct required facts, one wrong citation path; no SDK warning/error. Separate
70K API capacity/recall/history collection started with1200s per-prompt limit,
zero reasoning only for this synthetic diagnostic. Native production thinking
is unchanged. Collector exec session89923; output local-data/2026-10-17-context128/growth70k.
19:18: final client input reduced from110000 to98304 with16384output and16384
additional margin, based on measured SDK15241 vsQwen16139 tokens for the same
system text. No server restart; earlier raw requests retain their110000 limit.

## 2026-10-17 — Copilot context rejection and autonomy defaults

| # | Task | Status | Notes |
|---|---|---|---|
| 1 | Diagnose/fix no-response symptom | Mitigation applied; UI pending | Exact static-context rejection occurs before llama inference; Qwen-only MCP exclusion added. |
| 2 | Default Autopilot and Allow all | Configuration done; UI pending | New Copilot chat.defaultConfiguration and Local chat.permissions.default configured. |
| 3 | Continue without editor typing | Done | No prompt sent or existing chat cleared; owner response supersedes planned live typing. |

11:32 IST: server74136 still healthy/idle on task385;13.31GiB RSS/4.70GiB
dedicatedVRAM/freeRAM8.49GiB.11:30 AgentHost warning
compaction_static_context_blocked precedes the exact no-response error. Failed
session system body53,305characters/12,291Qwen tokens; tool count/budget unknown.
Separate unresolved ChromeMCP browser_url error retained without causal claim.
Running VSCode1.141.1/Copilot0.69.0 source inspected, not pending update bundles.

11:38 IST: encrypted settings/model backups verified; exactly three User setting
keys added. Model-specific mcp:* exclusion keeps builtin/custom coding tools and
instructions unchanged. Other values compare equal to decrypted backup. Existing
globalautoApprove was alreadytrue; newer session defaults were absent. Guarded
focus attempt failed before NewChat/send; owner declined typing, no further
editor input attempted. Existing UI labels are not fresh-default verification.

11:43 IST:27 offline tests pass10.168s after idle-slot check; fourPSparsers pass.
Health remainsok; no server restart/inference/model download/cloud evaluation.
Report and editor/regression guidance updated through context-maintenance skill;
shared adapters reviewed, unchanged. Actual fresh-chat verification remains
explicitly deferred. See the [task report](tasks/2026-10-17-copilot-context-defaults/2026-10-17-copilot-context-and-defaults-v0.4.1.md).

11:49 IST closeout: evidence commit581ba52 published to public main. Final
155-file content audit has0findings;181 relative file targets resolve; staged
diff whitespace check passes. The draft's personal home path was sanitized.
Canonical A-G response persisted in prompts.md. Fresh desktop chat remains
untested by owner instruction; production server is intentionally left running.
CI39009418382 was still running at the last check, so no new CI pass is claimed.

## 2026-10-17 — Complete inventory and Qwen availability

| # | Task | Status | Notes |
|---|---|---|---|
| 1 | All tried/untested models and pros/cons | Done |14 attempted artifacts; originalIQ3/denseQwen3.8 restored to inventory, scores and incomplete stages separated. |
| 2 | Reread and assess Gemini report | Done |All833 archived lines reread; recommended sequence/settings and factual corrections summarized. |
| 3 | Explain and restore existing Qwen | API done; current UI unverified |Old non-mapped commit requirement exceeded capacity. Configuration2.1 mapped endpoint restored and left running, same alias. |

The single [forwardable report](tasks/2026-10-17-complete-model-inventory/2026-10-17-all-models-gemini-and-availability-v0.4.1.md)
contains the full inventory, untested reasons, Gemini summary and operational
changes. Earlier stopped/unchanged statuses below are historical.

11:02IST recovery: no server; Q4 file present, about18GiB freeRAM/19.5GiB
availablecommit. Backed up local scripts/settings. Staged mapped editor profile
with existing alias, dual loopback, explicit isolated runtime and reviewed6000MiB
loadVRAM gate; runtime floors unchanged.27 offline tests pass10.582s, five
PowerShell scripts parse, preliminary149-file audit0findings; no inference during
tests. No editor credentials/settings, hardware, downloads or cloud calls changed.

11:07IST persistent start ready; second invocation returns samePID74136, guarded
manager79592. Full Q4 SHA and runtime identity verified. Stop dry-run matches
only configured process. Native greeting13.125s, two-file tool69.484s: all nine
values/source payloads correct, native reasoning present; JSON-only fences fail.
All response content and delivered source bytes reviewed. IPv4/localhost/IPv6
alias checks pass. No current UI pass claimed.11:11snapshotRSS13.306/private6.123,
freeRAM5.123/commit13.459GiB/freeVRAM1532MiB; earlier GPUprocess4.70GiB.
Lifecycle guidance updated through maintenance skill; Codex/Claude shared routing
reviewed, unchanged. No heavy grading or code execution during live inference.


11:17IST publication: implementation23f84b5 pushed to main; Windows/Ubuntu
CI39007400281 succeeds.153-file audit0findings,174relative file links and diffcheck
pass. Exact prepared A–G response saved in prompts.md before final. No current
editor UI claim. Last recorded11:14 process still running at13.31GiB RSS,
4.70GiB dedicatedVRAM,4.55GiB system freeRAM. Preserve the endpoint at closeout.

## 2026-10-16 — Memory and remaining-candidate expansion

| # | Task | Status | Notes |
|---|---|---|---|
| 1 | Measure RAM and growing KV context | Measured | 2K-120K occupancy, fixed KV reservations, CPU/GPU placement, history retention and omission tested. |
| 2 | Test Qwen3-Coder-Next 80B | Tested; audit failed | Public code/history reviewed; private audit reaches16 tool turns without a final in67m55s, so no private quality score. |
| 3 | Retest Gemma 31B dense | Reviewed; not promoted | Private26/36; Python6/6, TS5/6, SQLFKfailure. CPU-KV pair complete; GPU-KV short answer unchanged,8K stopped at394MiB freeVRAM and unscored. |
| 4 | Test Qwen3.6 Q6 | Done; retain Q4 | Q4 private31/36 in11m40s versus Q628/36 in35m. Both three Python6/6, TS5/6, SQL failure; histories pass. Separate diagnostics find local-key loss and nested aliases. |
| 5 | Independent research and report | Done | Research reread and corrected against primary sources, pinned code and measured results; all five points reconciled in the canonical report. |

03:53 IST final comparison: all Q4 public/private source reviews and isolated
grading complete. Frozen private20+5+6=31/36; Q628/36. Q4 standalone generated
tests74/75 fail missing imports; unchanged combined variants pass7/7. Three
concurrent grader fork failures retained, sequential unchanged-limit retries
complete. Both helpers fail two post-Q6 local-key diagnostics; post-both-answer
nested-alias tests fail2/2 for Q4 and1/2 for Q6, separate from frozen scores.
Q4 public peakRSS16.384/private6.213GiB,minRAM3.696/VRAM1909MiB; private
peakRSS15.954/private6.169GiB,minRAM4.221/VRAM1907MiB. No inference active.
Fresh unloaded18.93GiB physical/18.39GiB commit available; do not restart the
old non-mapped ~24GiB-commit launcher. Recommend measured mapped Q4 policy,
native thinking/64Kq8, with new editor validation separate. Existing editor
settings preserved. No WHEA since00:28 in the checked window; boot unchanged.
Used context-maintenance skill for project grading lessons; reviewed shared
Codex/Claude/Windows routing, no adapter change needed, frozen sources untouched.
Three nonleaders queued for exact verified-file retirement; Q4/Gemma26 retained.

03:30 IST matched Q4 public completes normally. TS/SQL251.062s reviewed;
plain-object validation missing, SQL FK failure predicted, false JS empty-array
truthiness explanation. Both histories pass:175.859s/10959maxinput and724.063s/
51580maxinput. Large49931new tokens627.185s; cached changed-file53.610s versus
Q6's48.515s with different generated length. Private PID61712/run032930 starts,
resident cap15.954GiB; no heavy grading during inference. All raw code preserved;
five Python packaging runs, TS/SQL, private grade and separate local-only-key
diagnostics await quiet review/execution. Production selection unchanged.

03:11 IST matched Q4 checkpoint: published74b76e7 passesCI38969216780.
Q4 controller5621, ownedPID71560, explicit isolatedruntime, resident cap16.384GiB.
GPUweights3381.34MiB/KV680/state62.81/compute408; readinessGPUcounter4.654GiB.
Three public Python answers complete302.063/313.484/248.922s; all visible content
and seven delivered sources per case reviewed. Code appears correct, but own
seed73 list test expects a removed key;74/75 omit imports. Preserve standalone
and labeled unchanged combined forms; isolated grading waits until all inference
ends. TypeScript/SQL active. A separate post-Q6 local-only-key diagnostic is
prepared before Q4 private answer, outside frozen scores. No new boot/WHEA since
Q6 launch in the inspected event window; no hardware-cause conclusion.

02:54 IST quiet validation:27 offline tests pass, both PowerShell scripts parse,
147-file public audit has0findings and git diff whitespace check passes. Frozen
Q4/Q6 profile hashes/task equality pass. Unloaded21.265GiB freeRAM/20.289GiB
availablecommit/6734MiB freeVRAM and5.285GiB E: disk free; no inference active.
Matched Q4 can proceed after this publication checkpoint.

02:53 IST Q6 review checkpoint: all six public cases plus private completed
with normal server stops. Five isolation preflights pass after inference ends.
Python implementations6/6 each; own tests6/6,6/7,6/7 (false empty-dict assertion).
StrictTS compiles5/6; SQLite FK execution failure. Private19semantic+4citation+
5code=28/36 in2099.672s; mutable alias fails, local-only keys also lost by source
inspection outside frozen checks.14sources/13successful ranges/2oversize errors,
no invented port or execution claim. Corrected shared-guide omissions/citations
are documented. Full tokenizer metadata matches Q4/Q6; only10.9MB headers read.
No production changes; fresh guards and frozen-input check precede matched Q4.

00:42 IST17October continuation: recovered current receipts and ownedPID56440;
Q6 core73 completed604.609s, two turns/seven complete source returns. All visible
content and source bytes reviewed; implementation/tests packaged unchanged for
quiet-period isolation. Correct v2 precedence, missing-fact abstention and read
inventory; bug diagnosis misattributes unknown-key omission and own tests omit
retained nested-list mutation. Second seed active; no executable score yet.
Read project/parent guidance, shared Windows guide/router/platform/logging,
Python/testing/discovery/git/documentation rules and grading methodology.
2d1579dCI38951495133 succeeds. No active settings changed or heavy checks run.

02:12 IST Q6 public suite completes normally:640-record history3296.891s,
READY640/all six facts/fresh revision2/retry0 pass; max input51411. Initial
phase3248.360s; cached changed-file phase48.515s. All source bytes and visible
answers reviewed. No read-error recovery exercised. PrivatePID63928 is active
under controller30694 with resolved17.243698GiB resident cap; all executable
grading and tokenizer-array checks wait until it stops. MatchedQ4 follows.

01:21 IST Q6 history checkpoint:120-record history completes628.735s, exact
READY120/all six facts/fresh runtime revision2 and retry0. Source review and
returned-byte comparison pass; max input11396tokens. No unavailable-ledger
attempt, so no error-recovery claim.640-record case remains active; no code
execution during inference. Gemma report now links reviewed placement outcomes.

00:59 IST Q6 public checkpoint: three native Python repeats completed in
604.609/453.922/588.953s. Seven source returns each; all visible text and
source bytes reviewed. Separate unchanged implementation/self-tests queued
for quiet isolation; only core74's project import is mapped to candidate.
Core74/75 contain false empty-dict expectations. Core75 improves retained
nested-list mutation coverage but misdiagnoses dictionary/scalar control flow.
TS/SQL active after ordered entry/router/linked-source reads. No code grade yet.
Saved header comparison confirms identical chat template, architecture fields
and tensor shapes; skipped tokenizer arrays are not claimed identical.

The current request supersedes the former 20-minute preference for these tests.
Applications stay open; resource guards remain. Full record:
[expanded experiments](tasks/2026-10-16-memory-and-candidate-expansion/2026-10-16-memory-context-and-expanded-model-tests-v0.4.0.md).

10:35 IST:64K CPU-KV sweep complete with1995/15928/31936/59955 actual input
tokens, all five-fact checks passing. Follow-up reused59951 tokens and correctly
applied revision2/retries0 in15.047s.128K CPU sweep started; measured KV1360MiB
and compute507MiB versus680/273 at64K. No new model download yet; pinned headers
and metadata inspected for the80B, dense andQ6 candidates.25 offline tests pass,
PowerShell parsing and public-content audit pass. Larger-model profiles use
explicit file mapping/resident caps, not a waived physical-memory floor.

11:08 IST checkpoint: context collection complete and reviewed. CPU64 fixed680MiB KV across2K-60K; CPU128 fixed1360MiB across2K-120K. At119943tokens CPU/GPU whole733.063/610.016s, decode2.69/4.15tok/s, RSS18.580/17.477GiB, dedicatedVRAM5.104/6.199GiB. Facts5/5 in both but plainJSON failed by code fences; follow-ups correct, omitted history UNKNOWN. Clean stops; CoderNext80 download started.26 offline tests pass10.886s; final candidate quality work pending.
11:27 IST checkpoint: 62607175 published; Windows+Ubuntu CI38856813259 succeeds. Mapped profiles now adapt to the observed19-23GiB unloaded headroom, require16GiB free and10GiB available commit (Gemma12), reserve5GiB and retain stop floors. Gemma prepared with mmap too.26 offline tests pass9.955s. Private whole-system paging/disk/GPU observer validated; first malformed-command attempt preserved, corrected observer active. CoderNext download progressing; no new model-quality score yet.
11:42 IST checkpoint: inspected exact Q4/Q6 tensor headers and published mixed-precision counts; Q6 is29.66GiB versus20.61GiB Q4, not a uniform bit-width change. Context profiles labeled measured recall only, with prospective25.5GiB commit load checks. Candidate MoE512/128 batches prepared from measured scratch reference; Gemma retains128/32.26 offline tests pass10.034s; two public PowerShell scripts parse;127-file audit and diff checks pass.090a7758 CI38858509322 succeeds.80B download continues; quality collection pending.

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

23:00 IST validation checkpoint:27 offline tests10.666s, updated-profile targeted check, twoPowerShell parses,142-file public audit0findings,13local report links and corrected whitespace check pass. Native dense scores and pending32K/Q6 experiments are documented before checkpoint publication.


23:37 IST dense placement checkpoint: two32K recall/history CPUKV arms completed with normal stops; all four requests byte-identical. CPUKV control/complete-layer 2K160.469/146.047s and8K457.610/462.234s. Default cache-offload follow-up2K146.109s; dedicatedVRAM5.906GiB. ActualGPUKV408+116.88MiB, weights4789.22/compute409.53MiB. Third8K stopped at394MiB freeVRAM below400floor during prefill; incomplete/unscored, no history follow-ups. Two shared requests byte-identical to second arm. No reboot; additionalVRAM consumer not attributed. Completed answers recover facts but add forbidden JSON fences; CPUKV changed/omitted history pass. These are budget0 recall diagnostics, not native coding scores. Desktop/resident-cap differences prevent isolated speed attribution. No grading/build/download overlapped. Q6 download and matchedQ4 quality follow; production selection unchanged.


23:52 IST pre-collection precision plan extension: Q6 transfer active, neither Q4/Q6 matched trial has started. Archived earlier five-task plan and added existing640-record context-large-v1 to both arms, alongside120-record history, threePython seeds and TS/SQL. Same profile hashes, requests controls, native thinking, six-hour deadline and frozen questions/checks. Previous Qwen input was about52K tokens; actual new usage must be measured. This extends long-file coverage before seeing either candidate answer.

00:08 IST17October pre-collection publication: six public precision tasks and
profile identities exported with exact local byte hashes plus portable canonical
JSON hashes. Public tasks exactly match the local frozen plan; profile checks
pass. This handles Git line-ending normalization without changing binary SHA
verification. The existing27 offline tests passed10.087s before these docs/data
edits; no runtime code changed.146-file audit has0findings and diffcheck passes.
Q6 download is active; neither matched arm has collected answers. Prior
d2927ae checkpoint's Windows/UbuntuCI38945253367 passed.

00:28 IST17October monitoring checkpoint: before precision inference, stopped
the ownedv3 observer normally and startedv4 with per-process WDDM GPU counters.
First sample85rows/2.437s; each collection is followed by30s sleep. Process
totals cannot be added as exclusiveVRAM; a desktop counter already exceeds the
contemporaneous device-used total. Microsoft sharing/counter-limit sources
reviewed, without diagnosing the Windows11 host or earlierVRAM stop. Lab output
note clarified; numerical counters/floors unchanged.27offline tests10.205s,
twoPowerShell parses,146-file audit0findings and diffcheck pass. Q6 transfer is
nearly complete; checksum/loads remain pending.966db75CI38948818005 succeeds.


00:31 IST17October Q6 start: full31843777504-byte pinned artifact/SHA verified after two resumed early transfers, E:5.30GiB free. Frozen six-task/profile checks pass; unloaded22.826GiB RAM/21.020GiB commit/6584MiB VRAM passes gate. Owned public PID56440 now runs native core-seed73; GPUweights4114.80/KV680/state62.81/compute566MiB. Actual resident cap17.777596GiB, ready dedicatedGPUcounter5.52484GiB. Smoke 3.609s returnsREADY. with extra period; transport only, not exact-format quality pass. Later private follows only successful collection/normal stop. No heavy auxiliary work during inference; mapped span is not RAM.

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
| Qwen3.6 Q4 | Both finalist suites and six editor probes reviewed; configuration2.0 running | Historical34 private31/36 selected; actual editor transport works; Python-routing/citation defects remain |
| Gemma 4 26B QAT | 32K/64K suites and both private audits reviewed | 52K-input recall passes; unrestricted SQL 6/6, TS 5/6; capped/unrestricted private scores both 19/36 |
| GLM-4.7-Flash UD-Q4 | q8 and f16 public follow-ups reviewed | f16 native code6/6; original own script runs zero tests, supplemental13/14; history count wrong; native f16 private27/36 |
| Qwen3-Coder 30B UD-Q4 | Five tasks graded | Core 2/6, 3/6, 1/6; private audit 20-minute deadline; exact weight retired with evidence |
| Gemma 4 31B QAT dense | Calibration rejected | GPU-KV resource stop; CPU-KV 0.95 tok/s and five-minute deadline; quality unscored |
| Qwen3.6 Q5 and optional Q6 | Q5 public/private complete and retired; Q6 capacity-rejected | Q5 matched core6/6 each but19.1% slower, native private28/36; Q6 fresh27.426<28.5GiB gate, no download/quality score |
| GLM Flash Q5 and optional UD-Q6 | Both complete and retired | Q5 native repeats6/6,6/6,0/6/private21/36; Q6 native private24/36; original evidence preserved |
| Kimi Linear 48B Q4 | f16 public reviewed;64K private gate rejected; exact weight retired | Two cache incompatibilities, one malformed tool call, code4/6 then6/6, TS4/6/SQL syntax failure; private has no score |
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

17:40 IST checkpoint: GLM Q5 native repeats6/6 and0/6, own7/7 and1/14; held-out strictTS compile fails and SQLite5/6 includes complete data loss. Recovery private audit750.391s,21/36 (16 semantic+3 citation+2 isolated code), ten sources delivered but four unread files claimed. Full weight SHA verified, exact21,408,850,272-byte file retired; all evidence remains. Qwen native private454.859s answer byte-identical to capped run, same read trace except generated IDs, same25/36. Verified launch ceilings2048/-1 and no request override; delivered reasoning172/26/37/57/92tokens on both. Prior identical-code isolated grade reused with explicit provenance, no new execution claimed. Adaptive cache queue active. Kimi transfer started after fresh unloaded26.42GiB/7112MiB snapshot; disk32.76GiB before transfer. Staged production stop shortcut now matches model+port8080+process creation, avoiding stale-PID targeting; CheckOnly excludes active8081. CIM/Process timestamp precision difference observed and handled; not installed. Checkpoint735745e passed both CI platforms.

17:58 IST checkpoint: no-cache reference212.750s/code6/6 and history133.969s passes;3072MiB cache118.422s/code6/6 and history135.391s passes. Both own-test suites6/7, with distinct false assertions;3072 standalone seven NameErrors preserved. Cache decode46.71tok/s, dedicatedVRAM6.26GiB, minfreeVRAM661MiB; history prefill slows and whole latency does not improve. Combined3072/batch512 rejected before load at7083<7100MiB, not OOM. New2GiB/batch512 candidate and historical34-expert replay prepared to choose actual-instruction quality before speed. Conditional native QwenQ5/GLMf16/GLMQ6 audits and subsequent two Qwen selection audits are serialized behind active GLMQ6 suite. GLMQ6 first core292.609s reviewed, code grading pending. Kimi download39% at17:53, not yet verified.20 offline tests pass9.556s; checks overlap GLMQ6 public collection and are disclosed. Public command construction for both new profiles passes; no production/editor changes.

18:20 IST: GLM Q6 public suite completed normally; capped Python5/6,0/6,6/6, unrestricted5/6. Own tests12/12,2/9,12/13,10/10; preserved failures separately. History six facts correct but count242 instead of120. Held-out source review finds TypeScript narrowing defects and SQL data loss; isolated grading queued. DedicatedVRAM5.71GiB, peakRSS20.74GiB, minfreeRAM5.20GiB/freeVRAM463MiB. QwenQ5 native private audit now running; subsequent GLMf16/Q6 and quality-first Qwen audits serialized. Kimi public suite queued after them. Continue2.0.0 installed-source inspection finds timeout units differ between SDK(milliseconds) and fetch agent(seconds); proposed model-entry correction1200000 awaits final editor validation. Production unchanged.

18:27 IST checkpoint: Kimi full30,061,058,720-byte pinned artifact/SHA verified at18:23; native non-thinking public suite frozen and serialized after existing audits. QwenQ5 native private collection remains active. Read-only UIAutomation confirms local VS Code window accessible alongside separate remote windows; no editor interaction or new UI inference yet. Continue timeout source evidence recorded with installed bundle hash; correction remains staged. Current report/model/next-step documents updated for GLMQ6 public outcomes.

18:27 IST validation:20 offline tests pass in9.167seconds; PowerShell scripts parse;103-file public-content audit has0 findings and diff check passes. Checks overlap QwenQ5 private inference and that timing caveat is recorded. Only reviewed documentation changed in this checkpoint; runtime/editor selection remains unchanged.

18:49 IST checkpoint: QwenQ5 native private537.250s,28/36 (20 semantic+6 citations+2 isolated code), honest14-source inventory and recovered read failure; nested dictionaries become None and mutable values alias. GLMQ4f16 native private942.000s,all15 sources/honest ranges,19 semantic+4 citations with isolated code pending; source code mutates/aliases inputs. GLMQ6 native private is active. Dedicated Local LLM VS Code window opened(handle462398); selected explicit local Qwen in Copilot and Continue Plan, no prompts sent. Added task-specific coding-use guide. Published6046eac CI38738677381 passes; later report updates remain local until next checkpoint.

19:16 IST checkpoint: GLMf16 native private27/36 (19+4+4); GLMQ6 native private24/36 (17+2+5), all saved and isolated graded. Qwen2GiB-cache private completed402.703s with honest14-source inventory; semantic19/citations4, code queued. Historical34-expert replay active; Kimi public suite waits serially. Restart cause remains unknown, owner did not observe event. No new editor prompt or production promotion.

19:30 IST checkpoint: historical Qwen placement replay31/36 (20+6+5),864.266s, all15 sources and accurate ranges;2GiB-cache27/36 (19+4+4),402.703s. Kimi q8V fails72/32 dimension constraint; mixed K/V fails architecture constraint; matching f16 loads with252MiB KV+42.81MiB recurrent state. Public suite active, first malformed-call failure preserved.20 offline tests pass9.192s; PS parse and110-file export audit/diff check pass. Offline tests overlap Kimi inference, disclosed. v0.3.8 adds separate compatibility profiles; production unchanged.

19:58 IST checkpoint: e2eb995/v0.3.8 published; Windows+UbuntuCI38748100354 passes. Kimi matching-f16 public suite completed normally: core4/6, malformed-call/no-code,6/6; own combined7/8 each and standalone8NameErrors; history facts pass/count242vs120 fails; TS/SQL source reviewed, isolated queued. Optional QwenQ6 fresh27.426GiB<28.5 gate rejected before retirement/download. Historical Qwen contender native cores73/74 completed473.265/469.328s, source reviewed and isolated queued;75/TS/52K follow. No hashing or sandbox grading during contender timing. Kimi64K private conditional after contender. Historical private answer exactly matches old31/36 answer, so repetition is reproducibility only. UI private helper staged/parsed, owned window screenshot inspected; no prompt sent. Conditional48K input/16K output budgets and candidate runtime staged only; production remains1.4/stopped.

20:34 IST checkpoint: historical Qwen final suite complete, normally stopped;
Python6/6,6/6,4/6, own7/7,7/8,7/7;TS5/6/SQLforeign-key failure. All six
history facts and READY640 pass at52,029inputtokens in448.062s. DedicatedVRAM
5.377GiB, peakRSS18.087GiB, minfreeRAM10.309GiB. Kimi held-out TS4/6 and
SQLite unsupported-CONSTRAINT failure graded in the quiet period. Its64K
private attempt rejected before loading at26.893<27.5GiB freeRAM. Cache2048
finalist three Python/TS answers source-reviewed and queued for quiet grading;
larger history active. Production/config changes still staged. Windows no
longer exposes an interactive input desktop/foreground; UI helper refused to
send. Owner asked to unlock when convenient; API/report work continues.

20:58 IST closeout: configuration2.0 installed and running. API greeting11.938s and actual two-file tool response34.297s pass, native reasoning present; curl alias correct. Live readiness16.99GiB RAM/5.38GiB dedicatedVRAM. Chosen34-expert placement reflects instruction priority31/36 versus cache27/36; repeated answer is byte-identical. No candidate passes every coding requirement. Four exact verified contenders retired93.330GiB, QwenQ4/Gemma26 retained. Continue SDK timeout1200000ms and48K/16K client budgets installed, other providers preserved with DPAPI backups.20 tests8.881s, PS parsing,113-file audit0findings and diffcheck pass. Desktop unavailable/error5; actual UI probes remain unsent. Project guidance updated through maintenance skill; shared adapters unchanged. No cloud calls, app closures or clock changes.


23:06 IST editor closeout: owner unlocked and provided an idle keyboard interval.
Six frozen actual UI prompts complete. Copilot submit-to-final events79.80/272.82/
76.43s; Continue observed upper bounds48.67/286.08/95.19s include six scoped read
approvals and polling. Both return fresh revision2/retries0 and earlier marker;
both miss Python-specific routing. Copilot297 words>250 and cites an unread
report; Continue249 words, GB/GiB slip and stale desktop note. Preserved eight
Copilot view calls (two size-limit responses, six source returns), six Continue
read calls, UI inventories and actual sessions privately. Native reasoning output
observed; exact prior-reasoning wire serialization not captured. No new model,
runtime/editor configuration, hardware or automatic-start changes. Working Qwen
remains running;22:58IST16.70GiB RAM/5.44GiB dedicatedVRAM,free6.39GiB/1126MiB.
20 offline tests pass8.909s;3 PowerShell scripts parse;114-file public audit has
0findings;diff check passes;94 local Markdown links resolve. Project/parent guidance updated via maintenance skill;
shared adapters reviewed and unchanged. No further automatic inference queued.

## Agent Deferred

-17October Copilot no-response: fresh-session Autopilot/Allow all, greeting and
  cited-file UI checks pending; owner explicitly requested no editor typing.
  Qwen-only MCP exclusion is a mitigation, not a demonstrated client fix.
-17October separate Chrome DevTools MCP browser_url substitution error not
  repaired; outside this scoped local-model context/defaults change.
-17October: current mapped-runtime Copilot/Continue UI regression not rerun;
  API/source-value verification is complete. Earlier UI quality failures remain.
-17October: Coder30Q6/Q8, originalNext80BQ4, Qwen2.5Coder14B and other proposed
  variants/settings remain untested as enumerated in the complete inventory;
  no automatic experimental queue created for this reporting request.
- Planned feasible core, held-out, precision/settings and private audits are
  complete with capacity/deadline exclusions explicit. No automatic queue remains.
- Clean-machine real runtime/model download is not part of offline validation.
- Long-history, stale-file and held-out language fixtures now run in v0.3.
  Larger-history coverage remains active; failed-tool recovery requires an
  observed attempted unavailable read and cannot be inferred from avoiding it.
- Python, strict TypeScript and SQLite grading is complete for the reported
  answers; implementation defects and model-written test errors remain separate.
- Copilot/Continue read-only UI probes are complete. Editing-tool workflows and
  an explicit source-manifest remediation remain untested.


Current dispositions:

| Item | Status | Next condition |
|---|---|---|
| Feasible precision/settings/private audits | Done with explicit exclusions | Frozen evidence retained; no automatic retry |
| Repeated/held-out/larger-history tasks | Done for both finalists | Keep defects visible; no universal quality claim |
| Actual Copilot/Continue UI | Six probes completed; quality partial | Read/history transport works; both miss Python-specific routing, Copilot cites an unread report |
| Optional QwenQ6/Kimi64K private | Historical capacity rejections remain unscored | QwenQ6 reopened in the16October mapped comparison; Kimi64K unchanged |
| Clean-machine installation/128K arbitrary sessions | Not tested | Separate future validation |
| Restart component cause | Unknown | New diagnostic evidence; no RAM-speed assumption |

## Agent Suggestions

-17October: use a new Copilot chat for changed session-construction settings;
  verify actual delivery and tool inventory before changing model context or
  placement. Keep local coding tools/instructions; enable extra external tools
  deliberately after measuring their static-context cost.
-17October: retain QwenQ4/Gemma26; prefer held-out real-project edits and explicit
  source receipts before further model churn. Validate aliases, local keys,
  type boundaries and SQL rollback independently.
-17October: preserve the healthy working endpoint after comparison closeout;
  report measured resource stops and restart explicitly when capacity permits.
- Start with a fresh memory snapshot; preserve the measured Qwen reference.
- Keep the research's multi-variable tuning bundle as separate experiments.
- Prefer Gemma QAT when current app usage makes Qwen's host allocation fragile.
- Collect repeated public results before claiming an accuracy leaderboard.


Current recommendations:

| Suggestion | Priority | Status |
|---|---|---|
| Supervised Python/file questions with independent mutation/type tests | High | Open |
| Review SQLite migrations on disposable copies | High | Open |
| Keep durable decisions in versioned notes and re-read changed files | High | Open |
| Preserve QwenQ4 and lower-memory Gemma fallback | High | Done |


03:55 IST17October closeout validation:27 tests pass10.134s;2PSparsers,148-file public audit0findings and diffcheck pass. Full baseline and three candidate SHA/size verification completed; exact80B/Gemma31/Q6 files retired91.291GiB, Q4/Gemma26 and all evidence retained. Owned observer stop marker set. No inference or new UI test active. All five research points complete; publish final results next.


Final publication: evidence116a67d pushed to main; CI38975676188 succeeds on Windows and Ubuntu.152 relative Markdown file links resolve (anchors/external URLs not validated by that check). Exact prepared A-G summary saved in prompts.md before the visible response. Owned observer34860 stopped normally. No server or inference queue active; all five requested research points complete. Optional mapped-profile editor regression remains explicit, not claimed done.
