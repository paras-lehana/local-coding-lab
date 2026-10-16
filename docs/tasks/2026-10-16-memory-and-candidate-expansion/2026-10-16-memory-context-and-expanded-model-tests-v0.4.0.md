# Memory, growing context and the remaining candidates

Status: in progress, 16 October 2026 (Asia/Kolkata). This report extends the
15 October campaign; it does not change its historical results.

| Owner point | Status | Evidence and next step |
|---|---|---|
| RAM use and KV growth | In progress | Measure unloaded/loaded RAM, configured buffers and increasing token occupancy separately. |
| Qwen3-Coder-Next 80B | Queued | Attempt the pinned Q4 artifact with file-backed mapping and monitored offload. |
| Gemma 4 31B dense | Queued | Repeat beyond the previous latency gate; collect complete answers before judging quality. |
| Qwen3.6 Q6 | Queued | Attempt mapping/placement appropriate to current headroom, then matched quality checks. |
| Independent research and reasoning | In progress | Re-read supplied research and verify runtime behavior and publisher facts. |

## Decisions and constraints

The owner now accepts longer experiments. The former 1200-second practical
criterion remains historical and the default for ordinary runs; this campaign
may explicitly allow up to six hours per complete prompt. This is a collection
ceiling, not a claim that six-hour turns are desirable. Applications remain
open. One inference process runs at a time. Resource and hardware-event monitors
remain active. No driver, clock, BIOS or pagefile settings change.

The initial snapshot has 63.91 GiB physical RAM, about 21.15 GiB available and
42.76 GiB occupied, with no llama-server running. Device VRAM is 3266 MiB used,
6788 MiB free. These are time-specific observations, not model allocations.
E: is a WD_BLACK SN770 NVMe drive. Windows already has a 21 GiB pagefile;
file-backed model mapping and anonymous committed memory must be distinguished.

## Experimental reasoning

KV token occupancy need not equal dynamically allocated bytes. A server can
reserve capacity at load, then fill it as context grows. Recurrent state,
checkpoints, scratch buffers and mapped weights also affect process memory.
Measure these separately rather than infer context retention from RAM growth.

File-backed mapping is worth trying for the 80B and Q6 artifacts when resident
weights exceed available RAM. A slow page-faulting run is not the same as a
resident model, and a load failure is not a quality score. Dense Gemma requires
completed code and instruction checks under the expanded time allowance.

## Validation and raw evidence

### First measured context sweep

The unchanged Qwen Q4 weight placement with all KV/state on CPU allocated
680 MiB q8 attention KV for 65,536 cells and 62.81 MiB recurrent state at load.
The initial larger-context load allocates 1360 MiB for 131,072 cells while the
recurrent allocation remains 62.81 MiB. It also increases GPU compute buffers
from 273 to 507 MiB: KV is not the only context-dependent allocation.

| Actual input tokens | Whole prompt seconds | Process RAM GiB after answer | Dedicated VRAM GiB | Exact five-fact JSON |
|---:|---:|---:|---:|---|
| 1,995 | 15.312 | 17.881 | 4.875 | Pass |
| 15,928 | 88.500 | 17.884 | 4.875 | Pass |
| 31,936 | 178.531 | 17.889 | 4.875 | Pass |
| 59,955 | 345.984 | 17.893 | 4.875 | Pass |

The follow-up retained all three source markers and applied runtime revision2
and retryLimit0 in 15.047 seconds. The server reused 59,951 input tokens and
processed only116 new tokens. That demonstrates reuse of delivered chat history,
not permanent memory of files that the client never supplied. After this follow-up
the process used about18.02GiB RAM. The 128K run is still being collected.

The much smaller change in resident RAM within a fixed context follows from
preallocation. Increasing the configured capacity changes the reservation;
filling that capacity changes occupied cells. The observed fixed buffer is
consistent with the [pinned runtime allocation code](https://github.com/ggml-org/llama.cpp/blob/b2f036c0f138414dedc987446f1d9d802f920275/src/llama-kv-cache.cpp).
Do not infer model weights, reserved capacity and token occupancy from a single
Task Manager number. WDDM shared memory overlaps RAM and is not added again.

Windows exposes physical and commit totals; process working sets overlap shared
pages and cannot simply be summed for an exact whole-system breakdown. Hyper-V
memory enumeration was denied by the current token, so no precise VM allocation
is claimed. No permissions, VM settings or apps were changed.

### Tooling validation checkpoint

25 offline tests passed in11.147seconds, including whole-request cancellation,
explicit longer-deadline propagation, commit-headroom rejection and a read-back
test of a resident-memory bound on an owned disposable child. Three PowerShell
scripts parsed successfully; public-content audit reported0 findings in125 files.
These development checks overlapped inference, so timings describe desktop use.

The resident-memory bound uses the Windows
[working-set API](https://learn.microsoft.com/en-us/windows/win32/api/memoryapi/nf-memoryapi-setprocessworkingsetsizeex)
only on the server process owned by the launcher. It does not cap total commit,
reserve extra RAM, modify other apps, or change the pagefile. This is an
experimental paging profile, not a speed or stability guarantee.

Raw local evidence: `local-data/2026-10-16-expansion/`. Public aggregate results
will be added after reviewing complete answers. Existing working profiles and
baseline weights are retained. No new model is promoted merely for loading.

## Source provenance

- [Supplied Gemini report](../../../research/raw/2026-10-14-gemini/report.txt)
- [Prior claim audit](../../../research/reviews/2026-10-14-gemini.md)
- [Prior campaign](../../../reports/2026-10-15-campaign.md)
- [Qwen Coder-Next publisher](https://huggingface.co/Qwen/Qwen3-Coder-Next)
- [Qwen3.6 publisher](https://huggingface.co/Qwen/Qwen3.6-35B-A3B)
- [Gemma dense publisher](https://huggingface.co/google/gemma-4-31B-it)

## Owner request

The unmodified request is retained in `owner-request.txt` beside this report.
