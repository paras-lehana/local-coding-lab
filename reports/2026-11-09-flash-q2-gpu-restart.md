# GPU restart during Flash-Next Q2 context growth

9 November 2026. **System-interrupted, unscored; unchanged retry quarantined.**

The owner reported another PC restart and asked that its consequences be tied
to the model and parameters. Windows dump time is 10:10:57.212 IST; next boot
is 10:11:56. This report separates the workload association from root cause.

## Active model and exact settings

| Item | Recorded value |
|---|---|
| Model | Qwen3.8-Flash-Next GSQ-RCO Q2_0, both pinned shards plus native-view pack |
| Engine | Strata 0.1.50, SHA256 5745022e7c8f743cfee83544da7d3672cd86103c854f23600e2c69ddd6593bef |
| Frontend | 4b9e05a2a806a3fe24f7b2560d98626c37dade35 plus isolated token-default ACL correction |
| Driver / GPU | 621.01 / RTX 3080 10 GiB |
| KV | int8 GPU VMM; maximum 65,536, initial 16,384, step 8,192 cells; hold disabled |
| Expert placement | 512 GPU cache slots, floor 128; mapped CPU experts, direct SSD PLE |
| CPU / residency | 6 workers on logical 2/4/6/8/10/12, host 14, affinity FFFC; 4 GiB native RSS cap |
| Input / output | prefill 64; xhigh; temperature 1, seed 73, output ceiling 4,096 |
| Other controls | MTP, suffix draft, projection and route-tail skipping off; sm86 native defaults retained |
| Interrupted work | 33,788-token fact prompt; last progress 16,832 processed tokens, 1,400 seconds |

Full artifact/plan/log hashes and measurements are in the
[sanitized incident receipt](2026-11-09-flash-q2-system-interruption.json).
Raw answers, events, minidump and existing debugger analysis remain private.
The 5.18 GB full dump was not duplicated onto the nearly full experiment drive.

## What completed and what did not

| Request | Wall time | Input processing / generation | Outcome |
|---|---:|---|---|
| 8,178 tokens | 723.859 s | 651.817 / 71.957 s; 271 generated tokens | Visible JSON contains all five supplied facts; observation only |
| 17,356 tokens | 1,480.453 s | 1,431.525 / 48.863 s; 180 generated tokens | Visible JSON contains all five supplied facts; observation only |
| 33,788 tokens | Interrupted | No final answer | GPU crash during prefill |
| Final 8,178-token shrink | Not run | None | Cannot claim trimming or post-growth recovery |

Native allocation increased from 16,384 cells / 0.23 GiB to 24,576 / 0.33 GiB,
then 40,960 / 0.52 GiB, leaving 292 of 512 expert-cache slots. Allocation
growth is observed; long-context qualification is incomplete. These independent
prompts each include their facts and do not test omitted chat-history retention.
Earlier static-32K greetings completed normally in 31.813/9.437 seconds; those
separate results remain valid observations, not evidence of long-run stability.

## Crash evidence and interpretation

The minidump reports **0x116 VIDEO_TDR_FAILURE**, bucket
`0x116_IMAGE_nvlddmkm.sys`, offset `nvlddmkm+0x198be40`, process `System`.
The stack is the Windows display timeout recovery path. Microsoft defines
0x116 as failed display-driver recovery after a timeout; its third argument
is the last failed operation's status, not a physical-memory measurement.
[Primary reference](https://learn.microsoft.com/en-us/windows-hardware/drivers/debugger/bug-check-0x116---video-tdr-failure).

Last guard sample, 10:10:43.544 IST: **10.172 GiB available RAM, 17.070 GiB
available commit, 1,580 MiB available VRAM, GPU 54.22 C, native RSS 4.000 GiB**.
CrashMonitor first reports GPU-is-lost at 10:10:48; last heartbeat is 10:10:56.
Earlier sensor rows show about 107 W GPU power, 74 C memory junction and
65.5 C CPU. Post-loss sensor fields become stale and are not fresh temperatures.
No WHEA record was logged in the crashed interval.

These observations do not establish ordinary RAM/VRAM exhaustion or overheating.
They also cannot exclude a driver, kernel workload, power or hardware issue.
NVML's GPU-is-lost text does not independently prove a physical PCIe disconnect.
CrashMonitor's nominal CPU-clock heuristic does not prove a new overclock.
Event 6008's shutdown text says 09:40:09, contradicted by subsequent live samples;
the dump and heartbeat provide the useful chronology.

The 8 November dump has the same 0x116 recovery signature and module offset,
before this trial. That supports a recurring GPU failure path, but neither
proves identical underlying causes nor clears the current workload. Do not
label Q2 compression, xhigh reasoning or elastic KV the proven cause.

## Checker correction and next decision

The old lab checker queried only WHEA. A post-restart regression probe wrongly
accepted this interval. It now checks provider-qualified bugcheck, unexpected
restart, display-recovery and NVIDIA error records as well, and rejects malformed
or unavailable event inventories. The real interval is now rejected for
WER 1001/1019, Kernel-Power 41 and EventLog 6008. This fixes detection; it cannot
prevent a kernel crash or prove hardware stability.

The exact GPU profile is quarantined and the prepared 128K private audit was
never armed. No model is promoted or automatically restarted. Continue offline
report reconciliation and collector validation. A future changed-condition
GPU trial needs a recorded incident review, new baseline and short bounded
qualification; do not simply reset the event timestamp or rerun the old queue.
No BIOS, clocks, driver or Windows TDR changes were made.
