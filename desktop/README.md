# Local LLM desktop control

**Maintained tray-first UI:** [LLM Tray](https://github.com/paras-lehana/llm-tray).
The owner moved to that standalone project on17October. Its hover panel has
pin/drag and configurable metrics, shortcuts and backend profiles. It uses this
directory's `control.ps1` as a trusted custom adapter, preserving existing
resource/process safeguards. Both owner launch shortcuts now open LLM Tray.

The following instructions document the original0.5.0 floating widget, retained
as historical implementation/evidence. Installing it again selects that older
UI; new users should follow the standalone project's README.

A small Windows taskbar-edge widget and notification-area icon for an existing
guarded Local Coding Lab installation. It is a floating native window above the
taskbar, not a modification of Windows Explorer's taskbar.

## Everyday use

- Open `Local LLM Widget.lnk` in your installation directory.
- **Ctrl+Alt+L** toggles the model and sends a Windows notification.
- Click the status or resource values to toggle. Drag the heading to move it.
- Green **Ready** means the configured model is loaded, not that a reply is fast.
- Amber **Sleeping** means the listener is available and a new message reloads
  the model. Clicking it or using the shortcut also wakes it.
- Red **Stopped** means the endpoint is off. Toggle again before chatting.
- Right-click for an explicit Stop, Show/Hide, guide, or Exit widget action.
  Exiting the widget leaves the server's current state unchanged.
- The small dash hides the widget; its tray icon brings it back. No boot startup
  entry is installed. Notifications obey Windows Do Not Disturb settings.

The VRAM and RAM figures are **whole-computer used/total GiB**. GPU is device0's
utilization percentage, not VRAM usage. Text is green below70%, amber70–89%,
red90% and above. Other applications are included. Missing telemetry is labeled
Unavailable. Native NVML and Windows memory APIs are sampled every3seconds;
there is no repeated Python or PowerShell resource-monitor subprocess.

## Installation

Requires Windows, the existing configured `runtime-config.json`, guarded
`start-server.ps1` and state/stop receipts under the installation root. This is
an optional controller, not a replacement model installer. It targets the
single-model localhost8080 setup used by this lab.

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\desktop\install-widget.ps1 -Root E:\llm
```

The installer downloads portable AutoHotkey2.0.30 from the official release,
checks its published SHA256 and checks an existing executable against that
archive. It leaves other AutoHotkey installations alone. The generated shortcut
refers to this checkout; keep the checkout in place. Icons/settings/logs are
under `<root>/widget/`; binaries and archive stay outside Git.

## Native idle unloading

The owner installation starts with `--idle-seconds 1800` in the guarded lab
launcher. For a new installation, append that option to its `lab.py run ...`
command and restart through the existing guarded launcher. It maps to native
`--sleep-idle-seconds 1800`; the inference settings are preserved. Check the
actual process arguments. The widget itself does not enable sleep on an older
launcher and must not be mistaken for an idle manager.

The listener stays alive while weights **and KV/state** are unloaded. The next
inference task reloads them. Saved editor chats are unaffected, but the client
must resend the history; sleep does not preserve an in-memory conversation.
Reprocessing a large instruction/tool prompt can take minutes again.

Only `/props` is polled by this widget. Native `/health`, `/props`, `/models`,
and `/metrics` are documented as passive. `/slots` and `/tokenize` are tasks;
do not poll those during sleep. A manual Wake uses `/tokenize` intentionally,
without generating a message or changing editor chat.

The existing supervisor still stops on resource/WHEA thresholds. Native wake
does not rerun the launcher's initial capacity preflight; it is monitored by
the existing running-process guard. A manual full Stop prevents a background
editor request from reloading during gaming. A stopped/crashed/guard-stopped
server does not automatically restart. There is no broad process kill or game
detector. A manual Stop can cancel an active answer.

## Verification and limitations

See the [measured task report](../docs/tasks/2026-10-17-idle-widget/2026-10-17-idle-widget-v0.5.0.md).
The initial tests used15seconds. A later [real30minute cycle](../reports/2026-10-18-real-idle-cycle.json)
observes native sleep after1800.150seconds and an automatic API wake answering
READY in25.062seconds, with the ordinary apps and a bounded download active.
Sleeping process RSS is0.579GiB. Model reload speed with a tiny API prompt is
not Copilot end-to-end latency. Native Windows visual/click/shortcut checks
replace browser/mobile checks for this desktop-only surface.

Public implementation: `LocalLLM.ahk` renders the UI and registers the shortcut;
`control.ps1` validates exact model/port/PID/manager ancestry and requests stop
via the supervisor's owned stop file. Actions are serialized with a mutex and
run outside the UI thread. `install-widget.ps1` installs the pinned dependency
and creates icons/shortcut. Runtime data stays in the installation root.

Sources: [llama.cpp native sleep](https://github.com/ggml-org/llama.cpp/blob/master/tools/server/README.md#sleeping-on-idle),
[AutoHotkey release](https://github.com/AutoHotkey/AutoHotkey/releases/tag/v2.0.30),
[AutoHotkey notification documentation](https://github.com/AutoHotkey/AutoHotkeyDocs/blob/v2/docs/lib/TrayTip.htm).
