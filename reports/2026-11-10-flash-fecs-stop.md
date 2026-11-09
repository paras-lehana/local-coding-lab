# Flash Q2 / Strata0.1.59: NVIDIA event stops residency control

10 November 2026,02:27:29IST. **Hardware/display-event stopped, unscored. No
new PC reboot observed.** The queue stopped after its first control; no later
profile was launched. Raw events and original partial receipts are preserved.

## What happened

Windows System record70392, providernvlddmkm, event13, levelError contains:
`Graphics FECS Exception: Logging error 0x2`.
Its XML execution PID4 names the system logger, not the originating application.
The event occurs during the plain greeting, before the larger cold-prefix
request. The greeting finishes27.344s, but that does not qualify this run.
The guard observes the error and stops its owned process tree at02:27:46.
The next request loses its connection after5.219s without an answer. The
qualification postflight raises the same event; the sequential queue exits1.
It does not continue to resident6/resident8 or the remaining controls.

The original partial collector receipt remains unchanged. The guard's result,
error traceback and event XML establish why this is incomplete; it is not a
quantization syntax defect or a completed performance comparison.

## Exact condition and memory

| Item | Value |
|---|---|
| Model | Pinned Qwen3.8-Flash-Next GSQ-RCO Q2_0, both shards |
| Runtime | Strata0.1.59 CUDA13/sm86; native SHA12a21cddb83e3af14c36478590676e5749b0075dedd3568e8630848f20ad819f |
| Frontend | Isolated4b9e05a2 plus recorded token-default ACL correction |
| Driver/GPU |621.01, RTX3080 10GiB |
| Changed control | Native resident working-set limit1to3GiB; admission5.5to7.5GiB, same4.5GiB reserve |
| KV/placement | Static32K int8 GPU KV,512expert cache slots, mapped CPU experts, direct PLE |
| Scheduling | Prefill64,6workers on logical2/4/6/8/10/12, host14,FFFCaffinity |
| Accuracy controls | xhigh (high alias), seed73, temperature1; drafting/projection/routing biases/tail skip off |
| Pre-event sample02:27:27.991 | RAM8.628GiB free, commit22.545GiB free, VRAM1300MiB free, GPU47.31C |
| Run minima | RAM6.922GiB, commit21.012GiB, VRAM594MiB free; no configured memory floor breached |
| Maximum measured GPU core temperature |48.41C; memory-junction temperature not collected here |
| Last active sample02:27:45.140 | RAM8.364GiB, commit22.185GiB, VRAM993MiB free, GPU46.94C |

This does not establish RAM/VRAM exhaustion or a thermal-limit stop. Nor does
it identify the root cause: the same FECS text exists on12October11:46:19,
before this runtime/configuration. An Armoury Crate application-hang report
at02:26:58 is adjacent evidence, not proof that it caused the GPU event.
Do not equate a Windows provider event number with a Linux Xid taxonomy or
transfer a Blackwell/Linux issue's diagnosis to this Ampere/Windows host.

Boot remains9November10:11:56. No new bugcheck, WHEA, display-reset or unclean
restart record was found in the reviewed interval. The protected LiveKernelReports
directory denied this session access; no new dump inspection is claimed.
The prior9November0x116 incident remains separate and unresolved.

## Disposition and reproduction boundary

No clocks, drivers, BIOS, TDR registry settings or owner apps changed. No
automatic retry, later queue step or timestamp reset. GPU testing remains
unqualified; a new run needs an evidence-based incident decision rather than
silently ignoring this event. Production remains off; the stored Qwen reference
is preserved. This guard stop cannot be claimed to have prevented a reboot.

The report's [sanitized receipt](2026-11-10-flash-fecs-stop.json) includes
configuration, counters and evidence hashes. Private originals:
`local-data/2026-11-10-tuning/flash-q2-0159-resident3-a/`,
`nvidia-event-022729/`, `flash-controls-01.json`, `hardware-hold.json`.
The qualified prior controls remain in
[the Flash timing export](2026-11-10-flash-tuning.json); this failed control is
not inserted into their successful-run table.
