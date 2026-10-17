# Desktop control design

Job: make it obvious whether the local model is using resources and let the
owner release that memory or resume work with one deliberate action.

The concept is a small companion power meter: a smiling colored tray face,
one status/control at the left, and three aligned readouts. It sits above the
taskbar, can be dragged by its heading and hides without stopping the model.
This is a native desktop UI; website templates, mobile viewports and web
deployment do not apply. No browser runtime or external visual asset is used.

| Token | Value | Use |
|---|---|---|
| Background | #16202D | Quiet dark surface |
| Text | #AABACB | Labels and shortcut |
| Green | #86E3A7 | Loaded / usage below70% |
| Amber | #FFD07D | Sleeping/loading / usage70–89% |
| Red | #FF9A9E | Stopped / usage90%+ |
| Typeface | Segoe UI9/12/13pt | Windows-native readable metrics |
| Geometry | 540×92 logical pixels, rounded corners | Compact taskbar-edge strip |

Every state combines a word, color and dot. Values include units and
used/total, so color is not the only signal. Ctrl+Alt+L is a keyboard equivalent
to clicking. The tray menu exposes explicit Stop and Hide/Show actions.
Actions run outside the UI process; status sampling is bounded. No animation
or attention-grabbing idle notification is used. Notifications respect Windows
settings. Unavailable telemetry does not become a fabricated0%.

Validation: actual desktop screenshots inspected for loaded, loading and off;
Windows global shortcut, click and tray actions exercised. Palette ratios and
exact results are in the [task report](tasks/2026-10-17-idle-widget/2026-10-17-idle-widget-v0.5.0.md).
The interface is intentionally desktop-only; it is not an Explorer taskbar
extension. The compact window can still obscure underlying content, so hide
and drag remain available. Current measurement targets the primary NVIDIA GPU.
