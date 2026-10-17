# Idle unloading, desktop widget and shortcut — v0.5.0

17 October2026. Owner workstation: Windows11, RTX3080/10GB, Ryzen5800X,
64GB RAM, everyday applications left open. Native desktop feature; no website.

## Outcome

The model now unloads after30minutes idle and automatically reloads for the
next inference task. A compact taskbar-edge widget displays whole-computer
VRAM/RAM used versus total and GPU utilization. Click it or press **Ctrl+Alt+L**
to toggle, with native Windows notifications. Green means loaded, amber means
sleeping/loading, red means stopped. Sleep preserves the listener; a manual
Stop turns it off until explicitly started again.

The previous Copilot issue is **not fixed by this feature**. Its actual greeting
eventually answered after about7m42s. Increasing context capacity did not make
its large instruction/tool prompt quick. No further model comparison was run.

| # | Pointer Task | Original Pointer Text | Status | What Was Done |
|---|---|---|---|---|
|1|Idle unloading|"idle configurationof 30 mins ... loads automatically ... do test"|DONE|Native1800second setting deployed; accelerated idle/wake and busy-request tests passed.|
|2|Resource widget|"VRAM, GPU and RAM usage in text (coloured as per %) ... Cliocking ... toggle"|DONE|Native floating taskbar-edge strip plus smiling colored tray icon; real resource readings and click cycles checked.|
|3|Shortcut and notification|"use autohotkey ... easy to remember ... toast notification"|DONE|Pinned portable AutoHotkey; Ctrl+Alt+L actual global shortcut stopped/started the model; Windows notification callbacks recorded.|
|4|Testing|"Do test"|DONE|Native sleep, wake, busy request, UI, shortcut, tray, ownership/error paths, parsers and offline suite checked.|
|5|Slow Copilot greeting|"response is stil not there after 2 minutes"|PARTIALLY DONE|Real response and timing recovered; latency remains poor. Owner redirected work from comparison to lifecycle controls.|

## What the latency evidence actually says

The owner's later chat used the local Qwen endpoint and supplied28659 input
tokens, despite visible text being just a greeting. It waited behind our70K
probe until that probe was canceled. Server input processing then took372.689s
at76.90tokens/s. The first generation took3.248s for35tokens. The editor's final
greeting arrived about7m42s after send; its task-complete tool finished later.
The completed conversation proves transport worked for that instance; it is
not a satisfactory interactive latency result.

The70K probe processed16384 tokens before intentional cancellation, remained
unscored, and was not silently labeled a memory failure. The separate installed
Copilot-engine source test completed in378.437s with four successful reads and
correct required facts, but one wrong citation path. Full context and tool
scope caveats are retained in the [preceding report](../2026-10-17-context128-and-tool-budget/2026-10-17-context128-and-tool-budget-v0.4.2.md).

About7GB total VRAM did not mean the model used all7GB: an earlier process
sample measured about4GiB dedicated model-process usage. Loader buffers were
3381.34MiB GPU weights and439MiB GPU workspace, with other allocations beyond
those two buffers. Desktop applications account for additional device usage.
Moving more expert weights to VRAM may help performance, but available VRAM
alone neither eliminates the28659-token prefill nor proves a new placement
fits. This task did not change expert placement to fill the remaining space.

## Installed behavior and limits

Production configuration2.3 retains Qwen3.6-35B-A3B UD-Q4_K_M and the isolated
b11562 prefetch-opt-out runtime. Context remains131072, CPU q8 attention KV,
37CPU expert blocks,4generation/8prompt threads,512/128batches. Native thinking
is still enabled with no invented ultra-effort setting. No weights were
downloaded/deleted and no GPU/CPU/RAM tuning or apps were changed.

The new guarded-launch option `--idle-seconds 1800` maps to native
`--sleep-idle-seconds 1800`. The existing capacity and running resource/WHEA
guards remain. Native wake does not rerun the initial capacity preflight; a
subsequent resource guard stop still requires an explicit restart. There is
no boot startup, game detector, retry loop, Ollama wrapper or broad taskkill.

Sleep unloads **weights AND KV/recurrent state**. A saved editor chat remains
on disk, but its client must resend history and referenced source content.
The next request rebuilds the cache, so a large cold Copilot prompt can again
take minutes. Unloading is a memory-management choice, not durable model memory.

Only `/props` is polled by the widget; the tested `/health` and `/v1/models`
checks also stayed passive. The local status script now skips `/slots` when
sleeping because that endpoint would wake the model. Manual Wake intentionally
uses `/tokenize` without generating chat content. Manual Stop can cancel an
active answer; it prevents automatic wake until Start is requested.

The widget is a540×92logical-pixel, draggable native Windows window above the
taskbar, **not a built-in Explorer taskbar band**. The dash hides it; the tray
icon restores it. Closing the widget leaves the server state unchanged. Open
`Local LLM Widget.lnk` in the installation root after a reboot. See the
[control guide](../../../desktop/README.md) for installation and everyday use.

## Measured lifecycle tests

All timings below are wall times from actual calls. The15second accelerated
timer exercises the same code path as1800seconds; **an elapsed30minute soak was
not performed on17October**. A later [18October real cycle](../../../reports/2026-10-18-real-idle-cycle.json)
observes native sleep after1800.150seconds, sleeping RSS0.579GiB, and automatic
wake with an exact READY response in25.062seconds. Apps and a bounded download
remain active, so this is not a controlled wake-speed comparison.
Diagnostic short prompts in the original17October tests disabled thinking per request only;
the production native-thinking setting was not changed.

| Check | Result |
|---|---|
|Loaded → idle sleep while status polling continues|PASS, roughly16seconds observed with2second polling cadence.|
|Memory release, first sleep|Device VRAM used7479→3622MiB:3857MiB/3.77GiB released. Model process resident RAM9.676→0.609GiB.|
|Longer-generation memory release|Resident RAM16.907→0.638GiB after final sleep. Remaining process/CUDA bookkeeping is not zero.|
|First new chat after sleep|PASS, exactWAKE_OK,5.359seconds including reload and response.|
|Second complete sleep/wake cycle|PASS, exactSECOND_WAKE_OK,5.000seconds.|
|Request longer than15second idle timer|PASS, still active at20seconds; completed120-number response in28.5seconds; only slept afterward.|
|Passive checks while asleep|PASS, health/props/models polling did not wake the model or prevent the tested sleep.|
|Click Sleeping → Ready|PASS, actual widget control event; no editor input.|
|GlobalCtrl+Alt+L loaded → stopped → loaded|PASS, owned process exited, new production process started with1800seconds.|
|Click loaded → stopped → loaded|PASS, separate mouse/control cycle, about5seconds to stop and24seconds to guarded startup.|
|Hide → actual Windows tray icon click → Show|PASS, native tray overflow icon clicked using measured UI bounds.|
|Reload while widget hidden|PASS after fixing hidden-window position persistence; one widget instance remains.|
|Native notifications|Windows NIN_BALLOONSHOW callbacks observed for actions and completion. Delivery still obeys Windows notification/DND settings.|
|Offline suite|35 tests passed in14.317seconds; includes conflicting timeout, foreign server, stale receipt, busy controller, failed start and already-off behavior.|
|Final suite/public audit|37 tests passed in14.593seconds after adding exact-image-review checks;171public files audited with0findings.|
|Syntax/static validation|Seven PowerShell parsers passed; AutoHotkey `/validate` passed; guarded launcher CheckOnly shows1800seconds.|
|Live identity|Configured alias and131072context verified via API; actual launch receipt contains1800seconds.|

At19:56:58IST the restored model's resident RAM was7.038GiB immediately after
loading; free system RAM22.329GiB, free VRAM2791MiB, GPU41C. Resident mapped
weights grow as pages are used; that startup figure is not a maximum or a
long-prompt memory measurement. A later widget read7.3/10GiB VRAM and42/64GiB
RAM, reflecting all applications. Its own sampled working set was about41MiB.

The widget uses NVML GPU0 and GlobalMemoryStatusEx directly every3seconds,
without spawning a periodic resource-query shell. GPU utilization can change
between its sample and nvidia-smi; values are rounded. Missing data is shown as
Unavailable. Palette text/background contrast ratios: muted8.29:1,
green10.60:1, amber11.40:1, red8.11:1. Native screenshots were actually opened
and inspected. Browser/mobile testing is inapplicable to this desktop surface.

![Loaded widget](../../../reports/assets/desktop-v0.5.0-ready.png)
![Action in progress](../../../reports/assets/desktop-v0.5.0-working.png)
![Stopped widget](../../../reports/assets/desktop-v0.5.0-stopped.png)

## Defects caught and corrected during testing

- First stop attempt refused the legitimate venv manager because the wrapper
  and real Python process have different PIDs. The corrected check verifies
  live ancestry, exact runtime/model/port, receipt and stop path. It does not
  relax into a process-name kill. The actual shortcut cycle then passed.
- Brief HTTP unavailability during native wake initially flashed Stopped.
  Status now retains Loading when the recorded process is alive, and a newer
  pending action wins over a status request that it interrupted.
- Hiding the widget exposed a real cleanup bug: visible-window lookup failed
  during reload. GUI-specific hidden-window positioning now handles this,
  and persistence errors cannot prevent exit.
- Tray restoration is explicitly wired to the native left-click callback.
  It was verified through the actual Windows overflow icon, not assumed from
  menu construction. Earlier failed test attempts are retained privately.
- The first idle test collector waited on inherited output handles after the
  detached launcher exited. Redirecting the collector's launcher output to a
  file fixed the test harness. No model failure was attributed to that hang.
- The first mouse-cycle harness raced widget startup; adding a bounded window
  wait fixed that test. These are harness corrections, separate from features.

## Files, dependency and provenance

| Files | Change |
|---|---|
|`lab.py`, `tests/test_idle.py`|Optional native idle setting and launch-boundary tests.|
|`desktop/LocalLLM.ahk`|Widget, native resource sampling, tray, shortcut and notifications.|
|`desktop/control.ps1`|Serialized, receipt-verified Start/Stop/Wake controls.|
|`desktop/install-widget.ps1`|Pinned portable AutoHotkey, generated native icons and explicit-launch shortcut.|
|`desktop/README.md`, `docs/DESIGN.md`|User guide, architecture, UI tokens, limitations and QA.|
|`tests/test_desktop.py`|Controller refusal, idempotence and failure-path tests.|
|`scripts/audit_public.py`, `tests/test_public_images.py`|Permit only three reviewed widget screenshot paths with pinned hashes; changed or unknown binaries still fail.|
|`profiles/qwen36-mapped-editor128-cpukv.json`|Prior128K profile and accurate updated measured status; no new quality score.|
|`docs/tasks/2026-10-17-context128-and-tool-budget/owner-request.txt` and its report|Recover prior incomplete work, actual greeting and canceled70K outcome.|
|This report and `owner-request.txt`|Current request, measured tests, defects and limits.|
|`reports/assets/desktop-v0.5.0-{ready,working,stopped}.png`|Reviewed, cropped widget-only screenshots.|
|`AGENTS.md`, `README.md`, `CHANGELOG.md`, `VERSION`|Regression rules, discovery, release notes and version0.5.0.|
|`docs/tasks.md`, `docs/tasks/README.md`, `docs/prompts.md`|Current task status, report index and canonical closeout.|
|Host-only `start-server.ps1`, `server-status.ps1`, `runtime-config.json`|1800second launch, passive sleeping status and lifecycle2.3; host files remain outside Git.|

AutoHotkey2.0.30 official archive SHA256:
`1e0ece7ecb2d5646e55758150472677996a57f9db5c83d2996d8b47b9e2f31a4`.
The archive was checked before extraction; an existing executable was compared
with the verified archive on installer rerun. No Python dependency was added.
Installation is under the owner's existing E-drive model root. No credential
or raw private instruction text is in the public changes.

Instructions actually read: project AGENTS/README/tasks/methodology; shared
Codex guide and setup README; platform/logging protocol and Claude router;
Windows host facts; matching Python/testing/coding/discovery rules; UI design
skill and tool-dashboard reference; context-maintenance skill. Project lessons
were updated; shared Codex/Claude adapters were reviewed and left unchanged.

Private receipts: ignored `local-data/2026-10-17-desktop-control/` contains
idle-live.json, final-checks.json, launch/test logs, click/shortcut/tray records,
screenshots and dependency verification. Installed widget action/state logs
live outside Git under the installation root. Old128K test evidence remains in
its original ignored folder. No cloud model or paid API was used.

Primary sources read and checked against this installed runtime:
[llama.cpp sleeping-on-idle documentation](https://github.com/ggml-org/llama.cpp/blob/master/tools/server/README.md#sleeping-on-idle),
[official AutoHotkey release](https://github.com/AutoHotkey/AutoHotkey/releases/tag/v2.0.30),
[official TrayTip documentation source](https://github.com/AutoHotkey/AutoHotkeyDocs/blob/v2/docs/lib/TrayTip.htm).
The installed b11562 help and local server source confirmed supported flags,
cached sleeping props and passive endpoint behavior before implementation.

## Pending items and recommendation

| Item | Status | Reason |
|---|---|---|
|Actual Copilot prompt-processing latency|Unresolved|A large instruction/tool prefill still takes minutes. This lifecycle task does not claim a speed fix.|
|Elapsed30minute idle soak|Verified18October|Native1800.150second idle and automatic25.062second API wake; later evidence linked above.|
|Fresh Copilot/Continue UI auto-wake chat|Not typed|Owner's no-editor-input restriction retained. API wake was tested with real messages.|
|New expert-placement or model comparison|Stopped/deferred|Owner explicitly redirected work; no new placement is silently promoted.|

Use explicit Stop before gaming if background clients must not reload the
model. Keep30minute idle sleep for automatic resource release between coding
sessions. A future performance task should measure the actual editor request,
reduce unnecessary injected tool schemas where possible, and compare a
carefully bounded increase in GPU expert placement against the same prompt.
That experiment should preserve necessary file access and report cold versus
cached timings separately. It is not started by this report.

The relevant original owner request is retained in `owner-request.txt` beside
this document. Its pasted research examples were treated as hypotheses, not
proof that flags, memory estimates or broad process-kill code were suitable.

Publication: implementation commit526fa28 on public main. Its
[GitHub CI run](https://github.com/paras-lehana/local-coding-lab/actions/runs/39041761773)
completed successfully. Final public audit:171files,0findings;202relative
Markdown targets resolve. Screenshots have exact reviewed-path/hash exceptions;
this is not permission to publish arbitrary binary files or private screenshots.
