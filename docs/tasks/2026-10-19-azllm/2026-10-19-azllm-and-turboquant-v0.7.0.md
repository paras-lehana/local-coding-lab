# azllm, TurboQuant and Strata on 10 GB

19 October 2026. Six calibration trials complete; sustained evaluation stopped
after an unexpected restart and a newly logged corrected hardware error.
Production recommendation remains Qwen 3.6-35B-A3B UD-Q4_K_M in llama.cpp.
It remains configured, but the server is currently off after the restart.

| Request | Status | Outcome |
|---|---|---|
|Try and optimize the article for 10 GB|Partially done|Same target runs in the compatible fork; six placements/draft probes finish. Native azllm is excluded by resident weight capacity; coding is interrupted.|
|Add research and measurements to the repo|Done; final publication recorded below|Pinned artifacts, build/download recipe, critical review and sanitized measurements.|
|Compare with existing results|Done with limits|New short-probe timings, explicit lack of a new coding score, and prior same-Qwen/Flash Strata outcomes.|
|Explain Strata work and findings|Done|Compatibility/memory fork, measured 32K gains, code defects, Flash deadlines and RAM-KV limits preserved.|

## Starting evidence

The supplied Andrew Zhu article describes azllm, a tqllm fork, running dense
Qwen 3.8-27B with custom weight formats, low-bit KV, DFlash2 speculation and
prefix reuse on 24 GB/32 GB GPUs. Pinned source adds host embeddings, output-head
and KV-tail placement, but does not provide general dense layer CPU offload.
Dense body matrices use the GPU uploader. The smallest published TQ_XS file
is 11.85 GB; the selected TQ3_4S-v2 file is 14,495,191,008 bytes. A smaller context
does not shrink these weights. Native Windows serving also uses POSIX APIs;
its mapped-GGUF implementation explicitly requires Linux/WSL or macOS.

The same TQ3_4S weights have a separate CPU/GPU-capable llama.cpp-tq3 path.
That is the practical measured fallback, not an azllm reproduction. The fork
also supports separately tested native MTP and DFlash2 with a different draft.
See the [frozen plan](../../../experiments/azllm/README.md).

Initial Windows snapshot: 22.7 GiB free physical RAM, about 33.2 GiB available
commit, 7315 MiB free VRAM, 14.0 GiB free disk. No inference server is running
after the 18 October 22:04 reboot. No stop was issued by this experiment.
Apps, clocks, editor settings and remote tunnel configuration remain unchanged.

## Previous Strata result

The [completed Strata report](../2026-10-18-strata/2026-10-18-strata-on-10gb-v0.6.0.md)
is the authority. Same-Qwen 32K workflows complete 1.14-1.76x faster in single
practical runs, but SQL migration fails, both engines retain TypeScript defects,
and Strata's Qwen 128K path was not validated. Flash-Next fits 10 GB; four coding
trials time out. 128K/int8 with 32K GPU-resident KV really uses 1.55 GiB pinned RAM
and processes 51K input, but the original history workflow ends with empty final
content. Two diagnostic replays recover 6/6 facts; they do not pass that workflow.

## Measured calibration: what actually fits and runs

The isolated Windows sm86 build succeeds with MSVC's explicit C11-atomics
compiler flag. No upstream source edits or production runtime replacements
were needed. Target and Q4 DFlash2 files pass their full SHA256 checks. Exact
revisions, file sizes, hashes and draft vocabulary/notice are in the
[artifact manifest](../../../experiments/azllm/artifacts.json); binary hashes
and compiler identity are in the [build receipt](../../../reports/2026-10-19-tq3-build.json).

Six sequential guarded profiles load and answer the same 63-input-token,
no-thinking, greedy inline-facts probe. These are single availability/timing
samples, **not coding scores or autonomous file-reading tests**. Windows file
cache is not flushed; apps stay open. Native generation timing excludes
prefill; whole response time includes it. Device VRAM includes other apps.

| Target GPU layers / method | Context | Whole response seconds | Native generation tok/s | Peak server RAM GiB | Peak device VRAM MiB | Minimum free VRAM MiB |
|---|---:|---:|---:|---:|---:|---:|
|16 / no draft|16,384|35.781|1.494|13.689|6,823|3,417|
|24 / no draft|32,768|30.437|1.757|14.236|8,383|1,857|
|28 / no draft|32,768|27.296|1.939|14.238|8,916|1,324|
|30 / no draft|32,768|30.093|1.923|14.239|9,293|947|
|24 / native MTP, max 2|32,768|30.094|1.790|14.931|8,550|1,690|
|24 / Q4 DFlash2, max 7|32,768|26.594|2.093|16.661|9,423|817|

All six reproduce the supplied values. The 30-layer answer adds Markdown
fences despite the JSON-only request: 54 output tokens versus 49 in the other
five. Therefore its longer wall time is partly output length, not just speed.
Different placement produces different text even with greedy sampling; these
tests do not establish general token equivalence or a quantization-only effect.

MTP accepts 30/36 draft tokens (83.3%), yet saves only 0.343 seconds against the
same 24-layer baseline. DFlash2 accepts 42/42(100%); it saves 3.843 seconds against
24 layers, but only 0.702 seconds against the simpler 28-layer profile. A tiny
sample cannot establish a repeatable 2.6% practical speed advantage. The draft
also reduces headroom and adds RAM. No speculative profile is promoted.
The fork disables backend sampling when a reasoning budget is present; this
effective fallback is preserved in native logs. The probe disables thinking
and the native log confirms a zero-token reasoning budget.

**Decision before quality collection:**28 layers/no draft, 32K context, 8 threads,
batch 256/microbatch 128, flash attention, CPU q8 K/V, one slot. 30 layers add memory
pressure without a measured token-rate gain. Native MTP is not useful in this
probe; DFlash2's small gain does not justify its reduced room for real prompts.
The 20-layer DFlash fallback is not triggered because 24 layers load and answer.
No broad speculative coding sweep follows this weak practical benefit.

The model itself reserves 5,713 MiB on GPU and 7,897 MiB in a CPU mapped buffer
at 28 layers. The 32K attention KV buffer is 1,088 MiB on CPU; recurrent state adds
149.6 MiB, plus temporary buffers and recurrent checkpoints. 16K KV is 544 MiB.
These are measured architecture-specific allocations, not a universal
"32K requires16GB" formula. Allocated capacity, live tokens, process RSS and
system free RAM are distinct. RSS can include mapped pages also used during
weight upload; adding file size, RSS and GPU bytes double-counts memory.

A one-second spot sample during router generation records771.9% process CPU
usage in psutil's one-core units (about 7.7cores on this 8-core/16-thread CPU).
The simultaneous whole-device reading is 88% GPU utilization, 8,771 MiB used,
49.51 W and 40 C. This is not a per-process GPU reading or a sustained average;
it confirms substantial CPU activity and does not prove a specific kernel
bottleneck. Filling the last VRAM megabyte is not itself a performance target.
At19:44, system free RAM rises from about 10.6 to 15.9 GiB and freeVRAM from
about 1,280 to 1,423 MiB without an agent intervention or profile change. Desktop
load/cache residency vary during these practical trials. Resource peaks are
observed one-second samples, not an assertion that no shorter peak occurred.

## Main workflow result: interrupted, not a deadline or quality score

Planned controls: fresh owned server per case, frozen public fixtures, seed 73,
temperature 0.6/top_p0.95/top_k20, xhigh template instruction, 2048 reasoning tokens
per turn, 8192 output tokens per turn, 1200 seconds for the entire workflow.
The embedded froggeric-v22 template maps high/xhigh to a natural-language
instruction, not a proven separate trained effort mode. A512reasoning-budget
router retry is predeclared only if the original router reaches the deadline;
it must remain a separately labeled diagnostic.

The frozen tests require linked instruction reads and source use, Python
repair/tests, a changed file plus beginning/middle/end historical facts, and
TypeScript/SQLite behavior. They do not ask the model to merely claim that it
knows the owner's files. Original private instructions are not uploaded or
published. Completed code requires isolated behavioral grading; partial
streams and timeouts remain unscored. See the machine-readable
[measurements](../../../reports/2026-10-19-tq3-measurements.json).

Only the router collection starts. It successfully reads all seven fixture
files, including both instruction versions, and reaches a 1,982-token prompt.
The next response remains entirely in its reasoning channel: zero visible
final-content characters. The last persisted streamed event is 862.125 seconds
into the workflow (14m22s); the native log reaches 1,173 generated tokens in
that turn at 1.77 tok/s. No final implementation is delivered. This is an
**interrupted run**, not a 20-minute timeout, syntax failure, or completed score.
Two completed tool turns preserve 799 cached prefix tokens on the second turn;
that proves some slot-prefix reuse, not the article's large warm-prefix speedup.

Observed router peaks: 14.571 GiB process RSS and 9,018 MiB whole-device VRAM;
minimum free RAM 10.487 GiB, available commit 24.618 GiB and free VRAM 1,222 MiB.
Maximum sampled GPU temperature 45 C; CPU temperature was not measured. The
last valid sample before the gap shows 15.817 GiB free RAM, 30.521 GiB available
commit, 1,422 MiB free VRAM and 41 C GPU. These do not indicate an observed memory
floor breach. One partial telemetry line is preserved and excluded from parsing.

Windows next boots at 19:46:39 IST. Kernel-Power 41 records an unclean restart,
BugcheckCode 0, no detected long power-button press and no sleep transition.
There is no new minidump. Event 6008's stale 19:25 shutdown estimate conflicts
with inference telemetry still written at 19:46:21; it is not treated as the
precise failure time. No natural collector result or stop receipt survived.
Recovery metadata is a separate record; original streams are not rewritten.

At 19:46:56 IST, WHEA logs a corrected hardware event. Decoding its 1,919-byte
CPER using the installed Windows SDK 26100 packed layouts identifies valid
processor fields: cache error, data write, level 1, processor/APIC 0, MCA bank 0,
status `0x9820100000120145`, corrected severity. The memory section has
ValidBits 0: it does **not** identify a DIMM or prove RAM 2800 is responsible.
This event is logged during startup; neither it nor Event 41 establishes the
restart's root cause or proves the model/runtime caused it. See the sanitized
[restart receipt](../../../reports/2026-10-19-interrupted-run.json).
Microsoft describes corrected severity as corrected by hardware or firmware;
its [severity definition](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/ntddk/ne-ntddk-_whea_error_severity)
and [processor section definition](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/ntddk/ns-ntddk-_whea_processor_generic_error_section)
explain the field meanings, not this machine's root cause.

The owner says "continue" after the gap. Initial live verification corrects the
stale running status. At first a reduced-thread/reasoning rerun is considered;
the newly decoded hardware record changes that decision. Existing parent
guidance explicitly requires stopping on a new hardware error. No further
inference is launched, no clock/driver/BIOS change is made, and no unrelated
apps are closed. The history, TS/SQL, 512-budget router retry and 131K capacity
probe remain **not run**, not failures or successes. No isolated generated-code
grader runs because there is no completed new coding answer to grade.

## Recommendation

Keep the existing Qwen 3.6 MoE Q4 as the selected configuration; do not replace
it with this dense TQ target on the current evidence. The smaller file is a
capacity improvement, while measured short responses remain about 1.5-2.1 tok/s.
Draft acceptance is impressive but its practical gain here is small. No new
completed coding-quality result justifies promotion, and the full-GPU article
setup has not been reproduced. The selected server remains off after the
restart/new hardware event; this is not normal 30-minute idle sleep or an
assistant routinely unloading a healthy endpoint at the end of a session.

Resolve the recurrent restart/hardware evidence before resuming sustained
comparisons. A separate hardware investigation should correlate firmware,
power and CPU/cache events and collect CPU temperatures; this record does
not justify declaring a particular part defective or blaming RAM frequency.
Then resume the frozen pending cases in new directories, retaining the
interrupted attempt and identifying any changed thread/reasoning profile.

## How the approaches differ

| Approach | What it changes | What our evidence supports |
|---|---|---|
|Existing Qwen 3.6-35B-A3B Q4 / llama.cpp|MoE experts mostly in RAM, GPU attention, CPU q8 KV, 128K capacity|Selected working setup; long editor prompts still slow and code defects remain.|
|Same Qwen / Strata|Different expert scheduling, prefill and GPU KV|Three32K workflows faster in single practical runs; SQL regression and no 128K Qwen validation.|
|Flash-Next / Strata|Much larger model with SSD/RAM/GPU expert tiers, optionalMTP and real hostKV|Fits10GB, but four coding attempts exceed20minutes; original51K history answer is empty.|
|Article's azllm|Dense target resident on GPU, custom weights/KV, DFlash2 verification and prefix reuse|Author's24/32 GB measurements; selected target body alone exceeds our10GB GPU.|
|Our llama.cpp-tq3 fallback|Same dense TQ3_4S target split across CPU/GPU; CPU q8 KV|Six short probes complete at 1.49-2.09 tok/s; router interrupted, with no completed coding score.|

This is the previously evaluated dense Qwen 3.8-27B family in a smaller custom
format and another runtime/template. Its13.50 GiB target is smaller than the
old20.47 GiB Q6 and 27.05 GiB Q8 artifacts. That is meaningful capacity progress;
it is not proof that the model became smarter or that a like-for-like speedup
was measured. Older runs also used different placement, buffers and reasoning.
The [complete model inventory](../2026-10-17-complete-model-inventory/2026-10-17-all-models-gemini-and-availability-v0.4.1.md)
preserves those earlier Q6/Q8 results and their limitations.

TQ3_4S stores32weights in 16 bytes including scales: 4.0bpw for those blocks,
about 4.24bpw for the mixed file. It is not simply the old IQ3_M format. Weight
compression, KV compression, speculation and prefix caching solve different
problems. Prefix reuse can avoid recomputing unchanged history; it cannot
discover unread files, preserve changed file bytes automatically, or retain
KV across process shutdown/sleep. Clients must send the required material.

## Strata: completed findings, not promises

We pinned upstreamv0.1.45, found no hard12GB minimum, and published a
[Windows10GB experimental fork](https://github.com/paras-lehana/Strata/tree/experiment/qwen36-no-mtp).
The compatibility patch makes optional MTP metadata optional; a separate
Windows path trims redundant copied GGUF source pages. Conservative64-token
prefill chunks with CUDA graphs disabled allow the same Qwen Q4 to complete
the public32K cases. Initial higher-memory serving attempts remain failures.

| Same-weight public case | Strata seconds | Existing llama control seconds | Quality |
|---|---:|---:|---|
|Instruction router / Python|286.516|436.469|Both40/40 source audit and 6/6 Python groups; Codex-assessed, finite checks.|
|Changed-file/history|250.625|285.891|Both6/6 facts and actual reread; roughly 11K input.|
|TypeScript / SQLite|203.765|357.687|BothTS5/6. Strata migration fails; llama SQL6/6.|

The 1.14-1.76x whole-workflow ratios are practical single-run comparisons,
not proof of a universal6x engine improvement. KV, placement, output length
and tool serialization differ. Strata's migration tries to disable foreign
keys after beginning a transaction; SQLite ignores that change and dropping
the referenced table fails. Both engines miss plain-object validation in
TypeScript; Strata also accepts arrays as job objects.

Strata Qwen peaks near 20.09 GiB RSS/9,344 MiB device VRAM versus llama's
17.90 GiB/7,783 MiB. Strata's fp32GPU KV path was validated at 32K, not128K.

For full Flash-Next IQ3_XXS, both 75.84 GB shards were verified. Native packing,
larger GPU reserve and bounded10/14 GiB host expert caches make it load on 10 GB.
Accuracy runs explicitly disable approximate route-tail expert skipping.
Four coding runs deadline: no-draft router andTS/SQL, plus10/14 GiB MTP router.
The smaller history case completes6/6 facts in 219.015 seconds. MTP sacrifices
GPU expert/prefill room; greater acceptance does not make the coding jobs
finish. Larger host cache improves capped throughput but is not a quality win.

The 128K/int8 configuration with 32K GPU-resident KV allocates1.55 GiB pinned
hostKV and processes 51,534 input tokens. Its original workflow rereads the
changed file but returns empty final content, so it remains unscored. Two
separate final-turn replays recover 6/6 facts; the warm replay takes 49.296 seconds,
while the medium/full-prefill replay takes 314.438 seconds. Different cache and
effort conditions prevent a fair direct ratio and do not repair the original
failed workflow. Real8GB hardware, full128K recall and new editor UI tests
were not performed.

## Sources and claim boundaries

The supplied Andrew Zhu article was read in full as pasted. Its exact canonical
URL/publication date was not recoverable; full copyrighted text and account UI
stay private. [Attributed claim inventory](../../../research/raw/2026-10-19-azllm/README.md)
and [critical review](../../../research/reviews/2026-10-19-azllm.md) preserve the
lead without republishing the article. Primary implementation sources:
[azllm](https://github.com/xhinker/azllm),
[tqllm](https://github.com/turbo-tan/tqllm),
[compatible llama.cpp fork](https://github.com/turbo-tan/llama.cpp-tq3),
[target weights](https://huggingface.co/YTan2000/Qwen3.8-27B-TQ3_4S), and
[DFlash2 weights](https://huggingface.co/z-lab/Qwen3.8-27B-DFlash2-GGUF).

The headline207tok/s and main table use different target variants. The article's
largest shown input is roughly 146K, not a262K accuracy benchmark. Its synthetic
throughput/filler and warm-prefix results are not linked-instruction coding
scores. Native azllm inference was excluded before load, not attempted and
observed to OOM. We did not port its dense engine or claim a native Windows
azllm server. No such engineering is hidden behind the fallback label.

## Exclusions and limits

| Item | Disposition and reason |
|---|---|
|Native azllm inference|Excluded before load: selected main dense blocks exceed dedicated VRAM, and the inspected engine lacks general dense CPU-layer placement. No observed azllm OOM is claimed.|
|TQ_XS/S/M/L and article TQ3 drafter|Different custom formats/quality; no compatible general CPU layer backend for these was established. The tested target and Q4 DFlash2 draft are identified separately.|
|DFlash2 20-layer target fallback|Not triggered: 24 target layers loaded and completed its probe. No claim that all possible draft placements were exhausted.|
|MTP/DFlash coding repeats|Not selected after short calibration: little practical gain versus 28-layer no-draft and less memory room. Short answer agreement is not a general equivalence proof.|
|History, TS/SQL and 512-budget retry|Not run after the unexpected restart/new hardware event. The original router never reached its natural deadline, so the original conditional retry trigger is not satisfied.|
|131K capacity and 131K/262K accuracy|The capacity probe was prepared but not launched after the hardware event. No new long-context fit or recall claim.|
|Stock llama.cpp loading this TQ3 type|Not used; the isolated compatible fork is essential. Existing production binaries are unchanged.|
|Full upstream numerical equivalence suite|Not run locally. Windows build/readiness and finite workflow tests are not a general kernel-parity certification.|
|Hardware8GB/24 GB and Linux azllm performance|Not measured on this PC; no extrapolated headline validation or buying recommendation.|
|Fresh editor integration and production restart|Not run after the new hardware event. Existing profile/client settings remain selected; endpoint is off. No editor typing.|
|Repeated/held-out promotion suite|No candidate promotion is established by single public-fixture runs.|

## Technical record and reproducibility

Public repository: [local-coding-lab](https://github.com/paras-lehana/local-coding-lab).
Working branch: `experiment/azllm-20261019`; public report destination: `main`.
Preparation checkpoint `4a1966c` is published. The final evidence commit and
matching owner-facing closeout are recorded in [the prompt log](../../prompts.md#azllm-and-turboquant-on-10-gb).
No paid service, new editor typing, clock/driver changes or upstream submission
was made. Production model, runtime, client settings and SSH routes are not
changed by these experiment profiles. Production restoration is withheld after
the new hardware event; a saved selected-model label is not a running endpoint.

| Public files | Purpose |
|---|---|
|`README.md`, `VERSION`, `CHANGELOG.md`|v0.7.0 research entry and release status.|
|`docs/tasks.md`, `docs/tasks/README.md`, `docs/prompts.md`|Progress, forwardable report index and matching owner-request/closeout record.|
|This report and `owner-input.txt`|One forwardable output and the relevant original request.|
|`experiments/azllm/README.md`|Build, scope, tested placement and guarded reproduction requirements.|
|`experiments/azllm/artifacts.json`|Pinned target/draft/source/vocabulary identities and hashes.|
|`experiments/azllm/download.py`|Explicit target/draft selection using the existing bounded range transport.|
|`experiments/azllm/settings.json`|Frozen controls, conditional trials and pre-quality selection rationale.|
|`research/raw/2026-10-19-azllm/README.md`|Attributed article claim inventory; full paste stays private.|
|`research/reviews/2026-10-19-azllm.md`|Independent source/capacity review and calibration-based interpretation.|
|`reports/2026-10-19-azllm-preflight.json`|Capacity/header and narrowly scoped artifact-retirement receipt.|
|`reports/2026-10-19-tq3-build.json`|Exact binary/compiler/source identity.|
|`reports/2026-10-19-tq3-measurements.json`|Sanitized calibration and recovered interrupted-run results with resource peaks.|
|`reports/2026-10-19-interrupted-run.json`|Sanitized reboot/CPER interpretation and last valid telemetry; raw event data stays private.|

All installations, downloads and private evidence remain below the existing
LLM directory. To make room, only two exact, redundant raw Strata MTP source
tensors were hash-checked and retired (4.6875 GiB total). Packed draft/runtime,
main Strata model, prior evidence and the selected production model remain.
The original full-file hashes and deletion receipt are retained. No directory
tree or unrelated process was removed. The initial machine had no inference
engine after reboot; this task did not stop an active production conversation.

Read sources: parent/project AGENTS and current task logs; shared Codex,
platform, topic router, host facts and applicable v2 discovery/logging/Git/
Python/testing/coding guidance; complete supplied article; prior full Strata,
complete-model, memory and methodology/grading reports; pinned azllm dense
loader/fitter/hostKV/mapping/server source and compatible fork build/arguments/
speculation code; model metadata, template and publisher artifact manifests.
Neither links nor model-generated claims were treated as automatic file reads.

## Validation record

Baseline offline suite: 38 tests pass in 16.434 seconds. Four PowerShell parser
checks, public-content audit (197 files, zero findings at that checkpoint),
relative-document links and `git diff --check` pass before live collection.
After recovery, all 38 offline tests pass again in 15.892 seconds. All four
tracked PowerShell scripts parse with zero errors. The public-content audit
checks 200 files with zero findings; `git diff --check` and downloader `--help`
pass. The relative Markdown check resolves 239 links (external URLs, anchors
and two historical host-absolute links are outside that check). Publication
details are recorded in the prompt/task logs. No new generated-code grader was
run: the interrupted workflow delivered no complete implementation to grade.
[GitHub CI39290022175](https://github.com/paras-lehana/local-coding-lab/actions/runs/39290022175)
passes on both Windows and Ubuntu at published revision `38d0e1b`. Later CI
receipt/summary changes are documentation only. Both remote branches were
verified at that revision, with a clean working tree and no inference listener.

The offline suite command is `python -m unittest discover -s tests -v`;
publication audit is `python scripts/audit_public.py`. PowerShell validation
uses `System.Management.Automation.Language.Parser.ParseFile` on all tracked
`.ps1` files. These checks do not launch the model or certify the hardware.
Commands used include the isolated CMake/Ninja CUDA build, full-hash bounded
download helper, engine `--version`/`--list-devices`, owned-job `guard.py`,
streamed availability probes, `benchmark.py` and `scenarios.py`. Real generated
code is never run on the Windows host. Private transcripts and runtime logs
remain available for local audit; public outputs are reviewed aggregates.

## Screenshots and UI scope

No user interface was changed in this experiment. Browser/mobile screenshots
are not applicable, and no fresh Copilot/Continue UI pass is claimed. Existing
editor latency and remote-client regressions remain distinct from API/model
availability and the synthetic read-only fixture.

## Original request

The relevant request is preserved verbatim in the adjacent `owner-input.txt`.
The attachment is the supplied Andrew Zhu article identified above; its full
text, private account UI and raw model responses are intentionally not copied
into this public forwardable document.
