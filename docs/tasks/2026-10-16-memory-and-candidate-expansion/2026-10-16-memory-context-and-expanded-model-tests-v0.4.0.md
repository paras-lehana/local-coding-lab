# Memory, growing context and the remaining candidates

Status: in progress, 16 October 2026 (Asia/Kolkata). This report extends the
15 October campaign; it does not change its historical results.

| Owner point | Status | Evidence and next step |
|---|---|---|
| RAM use and KV growth | Measured | 2K–120K occupancy, 64K/128K reservations, CPU/GPU placement, retained and omitted history. |
| Qwen3-Coder-Next 80B | Downloading | Pinned Q4 artifact; file-backed mapping and monitored offload follow verification. |
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
the process used about18.02GiB RAM.

At128K configured capacity, the all-CPU KV profile completed119,943 input tokens
in733.063seconds (12m13s):709.020seconds input processing,169.17 input tokens/s,
and2.69 generated tokens/s. All five facts were correct, but the answer included
a Markdown code fence despite the plain-JSON instruction. Recall passes;
strict formatting fails. The changed-revision follow-up completed in26.563s
with correct facts and the same formatting mistake. Removing the supplied
history produced `UNKNOWN` in1.094s, as requested. A cache is not independent,
permanent knowledge of a conversation the client omitted.

Resident process RAM stayed around18.45–18.59GiB during the long input. Free
physical memory remained above4GiB, while available Windows commit approached
1.28GiB. These are separate constraints: sufficient free physical RAM does not
imply sufficient commit allowance. The existing pagefile was not changed.

The GPU-offloaded128K counterpart completed too. Only cache/state placement
changes relative to CPU128; both use the same weights and layer placement.
Its GPU compute buffer is507MiB too. The default offload follows layer placement,
so this comparison is all-CPU KV versus mixed CPU/GPU KV. The latter allocates
272MiB KV onCPU and1088MiB onGPU; recurrent state splits18.84/43.97MiB.

| At119,943 input tokens | All KV/state on CPU | Default mixed placement |
|---|---:|---:|
| Whole request | 733.063s | 610.016s |
| Input processing | 709.020s /169.17tok/s | 594.367s /201.80tok/s |
| Generation | 2.69tok/s | 4.15tok/s |
| Resident process RAM after answer | 18.580GiB | 17.477GiB |
| Dedicated process VRAM | 5.104GiB | 6.199GiB |
| Correct source facts | 5/5 | 5/5 |
| Plain JSON instruction | Failed: code fence | Failed: code fence |
| Updated-file/history follow-up | 26.563s, correct facts | 17.141s, correct facts |
| History omitted | UNKNOWN | UNKNOWN |

The GPU follow-up reused119,939 input tokens and processed121 new ones. This
shows the benefit of a retained prefix, not permanent file memory. The updated
file was supplied inline in these probes; real tool discovery is assessed
separately. Recall requests used temperature0 and reasoning budget0 to isolate
memory behavior; these are not native-thinking coding scores. All three context
servers stopped cleanly. Raw measurements are summarized in
[the public result](../../../reports/2026-10-16-context-growth.json).

My recommendation from this pair is to keep GPU cache placement when headroom
allows, and use CPU KV to recover VRAM when necessary.128K is an optional long
input profile, not automatically a better everyday default. At120K the GPU
run left only775MiB device VRAM free and about1.76GiB available commit, despite
6.44GiB physical RAM available.64K remains the conservative working profile
pending the remaining candidate and editor comparisons.

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

Before candidate inference, unloaded desktop RAM varied around 19–23 GiB.
The mapped candidate profiles therefore accept at least 16 GiB free, derive
their resident bound from current free RAM minus 5 GiB, and retain the 2.5 GiB
physical / 1 GiB commit stop floors. Dense Gemma also uses mapped CPU weights
to reduce anonymous weight commit; this differs from its old latency-only
calibration. Exact caps and buffer placement will be recorded per load.

Raw local evidence: `local-data/2026-10-16-expansion/`. Public aggregate results
will be added after reviewing complete answers. Existing working profiles and
baseline weights are retained. No new model is promoted merely for loading.

## Independent interpretation of the supplied research

The report is a useful hypothesis list, not a verified experiment log. Today's
measurements support its small Qwen cache estimate, but contradict the earlier
chat advice that128K always requires tens of GiB of KV. Cache shape depends on
the architecture; dense versus MoE alone does not determine it. Native context
capacity also does not guarantee retrieval accuracy, instruction compliance,
or that an editor actually sends every referenced file.

The claim that Q4 cannot cause the remaining coding errors is unproven. So is
the opposite claim that a Q6 upgrade guarantees correct syntax or fixes all
bugs. Q6 and a matched Q4 control are scheduled with the same runtime, tasks,
sampling and placement policy. Different physical residency and desktop load
will still limit timing comparisons. These mixed quantization artifacts do
not represent a uniform four- versus six-bit change to every tensor.

Header inspection makes that concrete. The current Q4 artifact stores its
120 routed-expert tensors as 80 Q4_K, 37 Q5_K and 3 Q6_K tensors. The Q6 artifact
uses 78 Q6_K and 42 Q8_0 expert tensors. Most other quantized tensors are already
Q8_0 in the Q4 file; its output tensor changes from Q6_K to Q8_0 in Q6. Tensor
counts are not parameter counts, and this is not a quality score. The files are
20.61 versus 29.66 GiB, about 44% more storage for Q6. See the
[header evidence](../../../reports/2026-10-16-quantization-headers.json).

Coder-Next80B has an explicit trial despite exceeding currently available
resident RAM. File-backed mapping can trade repeated storage reads for a lower
resident working set; it does not make all80B weights resident or increase
available RAM. A launch rejection will be recorded separately from quality.
The pinned Coder-Next Instruct checkpoint is non-thinking: an effort flag
cannot turn it into a trained thinking model. Dense Gemma31, by contrast,
will receive native thinking and a longer collection deadline; the earlier
five-minute calibration is not a completed quality evaluation.

The report's blanket GLM-Q5 failure prediction and incorrect Gemma/Kimi layer
counts were already corrected by the15October campaign. Its claim that an
8GiB default prompt cache caused our stops also does not apply to the actual
launcher, which already used `--cache-ram 0`. Preserve those distinctions when
comparing the research with measurements.

## Source provenance

- [Supplied Gemini report](../../../research/raw/2026-10-14-gemini/report.txt)
- [Prior claim audit](../../../research/reviews/2026-10-14-gemini.md)
- [Prior campaign](../../../reports/2026-10-15-campaign.md)
- [Qwen Coder-Next publisher](https://huggingface.co/Qwen/Qwen3-Coder-Next)
- [Qwen3.6 publisher](https://huggingface.co/Qwen/Qwen3.6-35B-A3B)
- [Gemma dense publisher](https://huggingface.co/google/gemma-4-31B-it)

## Owner request

The unmodified request is retained in `owner-request.txt` beside this report.
