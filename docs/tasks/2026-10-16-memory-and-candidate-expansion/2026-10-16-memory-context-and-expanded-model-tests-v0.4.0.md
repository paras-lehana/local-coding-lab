# Memory, context and expanded local-model tests — v0.4.0

**Status: in progress, updated 17 October 2026, Asia/Kolkata.** The growing-context
measurements, Coder-Next attempt and dense Gemma native quality review are
complete. Dense CPU-KV placement diagnostics are complete; the GPU-KV follow-up
was stopped for low VRAM. The matched Qwen Q6/Q4 comparison remains. No
replacement has been selected.

| Owner point | Status | Result / next action |
|---|---|---|
| Explain 64 GB use and test growing KV | Measured | Actual input from 2K to 120K, CPU/GPU cache placement, reused history and omitted history tested. Main KV reserves capacity at load. |
| Test Qwen3-Coder-Next 80B | Tested; not promoted | Python 6/6, TS 4/6, SQL fails. History passes. Private audit repeats wrong paths and reaches its tool-turn limit without a final answer. |
| Retest Gemma 4 31B dense | Reviewed; not promoted | Public/private Python helpers pass 6/6; TS 5/6, SQL fails. Private instruction audit 26/36 in 2h00m34s. Placement diagnostics do not establish a faster file-heavy workflow. |
| Test shortlisted Qwen3.6 Q6 | Downloading | Pinned mixed-precision artifact and matched Q4 control prepared; verification and collection remain. |
| Independently assess the research | Ongoing | Publisher-score attribution, cache sizing, template reuse and Windows loading claims checked against sources and measurements. |

## Business summary and current recommendation

More RAM for context is useful, but it does not make an agent read referenced
files, follow their instructions or retain unlimited history. Our current Qwen
architecture needs much less KV memory than the earlier chat advice assumed.
At 128K capacity it reserves about 1.33 GiB of q8 attention KV, not 32–64 GiB.

The two larger candidates now have actual evidence. Coder-Next can run through
file-backed paging, but failed the real-instruction workflow. Dense Gemma
produced a correct private merge helper after a long wait, yet its overall
instruction answer was weaker than the historical Qwen reference. Neither is
promoted. Q6 still deserves the requested matched test before a final choice.

All scores here are small local cases, not universal model rankings. Instruction
and citation assessments are by Codex, without independent human review;
executable behavior was checked separately in Linux/bubblewrap isolation.

## 1. RAM, VRAM and growing context

The PC has 63.91 GiB usable physical RAM, an RTX 3080 10 GB and a Ryzen 7 5800X.
The initial unloaded snapshot had 21.15 GiB available RAM, 42.76 GiB occupied,
and 6,788 MiB device VRAM free. Apps remain open. The existing Windows pagefile
is 21 GiB allocated; this campaign did not change it.

With the same Qwen Q4 weight placement, CPU q8 KV reserves **680 MiB at 64K**
and **1,360 MiB at 128K**. Recurrent state stays 62.81 MiB. GPU workspace also
changes, from 273 to 507 MiB. Occupied tokens, allocated buffers and resident
physical pages are different counters.

| Actual input tokens, CPU KV | Whole prompt | Process resident RAM | Dedicated process VRAM | Recall / formatting |
|---:|---:|---:|---:|---|
| 1,995 | 15.31s | 17.881 GiB | 4.875 GiB | Five facts and plain JSON pass |
| 15,928 | 88.50s | 17.884 GiB | 4.875 GiB | Pass |
| 31,936 | 178.53s | 17.889 GiB | 4.875 GiB | Pass |
| 59,955 | 345.98s | 17.893 GiB | 4.875 GiB | Pass |

The 60K follow-up reused 59,951 tokens and processed 116 new ones. It retained
the markers and applied the supplied revision 2 / retryLimit 0 in 15.05s.

| At 119,943 input tokens | All KV/state on CPU | Default mixed CPU/GPU placement |
|---|---:|---:|
| Whole request | 733.06s | 610.02s |
| Uncached input processing | 169.17 tokens/s | 201.80 tokens/s |
| Generation | 2.69 tokens/s | 4.15 tokens/s |
| Resident process RAM after answer | 18.580 GiB | 17.477 GiB |
| Dedicated process VRAM | 5.104 GiB | 6.199 GiB |
| Private committed bytes | 24.150 GiB | 24.146 GiB |
| Five source facts | Correct | Correct |
| Required plain JSON | Failed: added code fence | Failed: added code fence |
| Changed-revision follow-up | Correct, 26.56s | Correct, 17.14s |
| History deliberately omitted | UNKNOWN | UNKNOWN |

The mixed placement has 272 MiB KV on CPU and 1,088 MiB on GPU; recurrent state
splits 18.84/43.97 MiB. The predicted 1.105 GiB CPU allocation difference agrees
with the observed 1.103 GiB resident difference. Private commit is not another
physical-memory allocation to add to RAM and VRAM. Shared GPU memory also
overlaps system RAM.

These were temperature-zero, reasoning-budget-zero **inline recall probes**.
They establish supplied-fact recall and cache reuse, not autonomous discovery
of 120K tokens of repository files. All servers stopped normally. Near the long
GPU run's end, only 775 MiB device VRAM and about 1.76 GiB commit allowance
remained despite 6.44 GiB physical RAM available. Keep 64K as the working default;
128K is a measured optional input profile, not unlimited chat memory.

At 19:51:50 during dense Gemma, Windows had 5.62 GiB RAM available and the server
occupied 17.20 GiB resident RAM. Edge, VS Code and WebView summed working sets
were about 7.97, 7.26 and 1.59 GiB; existing pagefile usage was 3.92 GiB. These
process totals can double-count shared pages and are not an exact partition of
the roughly 58.29 GiB unavailable physical RAM. Windows, other apps and caches
also consume memory. Hyper-V allocation enumeration was unavailable, so no
precise VM allocation is claimed.

Dense Gemma's active CPU KV is **3,251.25 MiB at 64K**, including 2,720 MiB global
and 531.25 MiB sliding-window KV. Its separate single checkpoint grew from
3.322 to 425.013 MiB as occupancy increased, then was replaced at the configured
limit. Thus some context-related allocations do grow even when active KV is
reserved up front. `--cache-ram 0` does not disable these checkpoints.

**Take:** use GPU KV when it fits; CPU KV recovers VRAM when needed. In this
runtime `--no-kv-offload` selects CPU cache. CPU KV is ordinary CPU allocation,
not automatically CUDA pinned memory. Files must actually be delivered or
retrieved, changed files re-read, and durable decisions stored in project notes.
[Context results](../../../reports/2026-10-16-context-growth.json),
[memory guide](../../memory-and-context.md).

## 2. Qwen3-Coder-Next 80B

Artifact: `Qwen3-Coder-Next-Q4_K_M.gguf`, 45.196 GiB, pinned Unsloth revision
`ce09c67b53bc8739eef83fe67b2f5d293c270632`. Full size and SHA256 verified.
This checkpoint is non-thinking; an effort label cannot add a trained thinking
mode. Full identity, flags and results are in the [80B record](../../../reports/2026-10-16-coder-next.json).

The first stock Windows mmap startup exhausted headroom before inference:
0.115 GiB free physical RAM and 0.125 GiB available commit, while process
residency was only 0.329 GiB. The monitor stopped the owned process and memory
recovered. There was no new WHEA event in that interval. This load failure does
not diagnose the owner's earlier restarts.

Inspection identified whole-file `PrefetchVirtualMemory` as a plausible source
of pressure outside the process working set. An isolated same-commit opt-in
disabled initial mmap prefetch. Only `llama.dll` was rebuilt; CPU/CUDA backends
remain byte-identical. Tiny CPU/GPU greedy controls match across stock and
modified modes; this is not complete numerical-equivalence proof. A separate
Qwen smoke passed before the 80B retry. The stock runtime remains intact.
[Patch, identity and reproduction](../../../experiments/llama-mmap-prefetch/README.md).

| Completed case | Result | Whole time |
|---|---|---:|
| Public Python / file instructions | Implementation 6/6; nine generated tests 8/9 after explicit unittest invocation | 13m14s |
| TypeScript / SQLite | TS compiles, 4/6; SQL foreign-key failure and wrong uniqueness declaration | 9m22s |
| Recovered history | READY120 and six facts correct, updated file re-read; one mistyped path recovered | 19m38s |
| Actual-instruction audit | 16-tool-turn limit; no final answer or code, unscored | 67m55s |

The original history attempt stopped at 2.269 GiB available RAM and remains
unscored. Outside-process growth was not attributed; overlapping WSL grading
was a possible contributor. Later inference excludes grading/build/download
work. The recovery uses 46 CPU expert blocks, GPU cache, larger microbatch and
a smaller resident cap; it is a multi-variable recovery, not an isolated speed
comparison. Its history load has 816 MiB GPU KV, 75.38 MiB recurrent state,
885 MiB GPU workspace and 5.343 GiB dedicated process VRAM.

The private audit repeatedly requested wrong Codex paths despite the inventory.
It received 11 distinct sources, with 10 successful tool ranges and 15 rejected
reads, reaching only 25,063 input tokens. It did **not** exhaust 64K context.
Weighted uncached prefill was 6.27 tokens/s and tool generation 5.80 tokens/s.
Whole-system reads averaged 254.5 MiB/s; these shared-desktop samples describe
paging, not isolated disk throughput. Peak resident RAM was 14 GiB; minimum
free RAM 6.47 GiB, device VRAM 517 MiB. It stopped normally.

The private client used top-k 20 rather than the server's 40. This is a recorded
configuration, not exhaustive rejection of every sampler or agent scaffold.
**Take:** the tested setup is not a better instruction-heavy coding assistant;
extra cache capacity alone cannot correct repeated wrong-path requests.

## 3. Gemma 4 31B dense

Artifact: Google's official QAT `gemma-4-31B_q4_0-it.gguf`, 16.439 GiB, revision
`59dde24573e7e61570dba08b18a2e1fe246955ed`; full SHA256 verified. It uses the
explicit isolated prefetch variant, mapped CPU weights and native thinking.

The completed public profile has 64K CPU q8 KV, all dense FFNs plus the first
12 attention blocks on CPU, remaining attention/output GPU-eligible, 8/8
threads, 128/32 batches and one checkpoint. Loader GPU weights/workspace are
4,745.60/797.63 MiB. Readiness dedicated VRAM is 5.648 GiB. The CPU-mapped
16,818.14 MiB address span contains holes for GPU tensors; it is not resident
CPU weight memory. Public peak residency was 17.202 GiB, with at least
4.265 GiB free RAM, 678 MiB free VRAM and maximum GPU core temperature 57 C.

| Case | Reviewed outcome | Whole time |
|---|---|---:|
| Public Python / instructions | Correct implementation 6/6; separate tests omit an import, combined unchanged blocks pass 6/6 | 65m45s |
| TypeScript / SQLite | Strict TS compiles, 5/6; SQL fails foreign-key enforcement | 74m23s |
| 10K history and changed file | READY120 and six facts correct; fresh revision 2/retry 0; honest follow-up inventory | 33m49s |
| Actual-instruction audit | 16/24 semantic + 4/6 citation + 6/6 code = **26/36** | 2h00m34s |

The public Python diagnosis incorrectly calls the scalar-update exception
`AttributeError` rather than `TypeError`. TypeScript omits plain-object
validation. SQLite tries to disable foreign keys inside an already-open
transaction, then drops a referenced table; isolated execution confirms the
failure. A failed migration is not six independently failed assertions.

The private merge helper correctly deep-copies both local and missing base
values. Its explanation nevertheless omits required nested/shared guidance,
relevant adapter-review conditions and exact per-repository log locations.
Its inventory omits a delivered router and describes a registry request that
never happened. It does not invent the absent port. All nine delivered source
texts were checked against frozen bytes; no tool read failed. No private source
or answer is published in the public aggregate.

One additional style mismatch is outside the frozen behavior score: the answer
names type hints and docstrings as requirements, but its own helper omits them.
That is instruction/style noncompliance, not a Python syntax failure; no new
post-hoc scoring criterion is added.

Public sampling is temperature 1, top-p .95, top-k 64 and
`preserve_thinking=false`, with 16,384 output tokens. The legacy private client
actually overrides top-k to 20, preservation to true and output allowance to
24,576. Both use native thinking, without a separate practical reasoning cap.
Metadata does not advertise native reasoning-effort levels. The private run's
resident cap was reduced from 19.218 to 17.202 GiB after headroom fell below
4 GiB; a separate before/after receipt preserves that intervention. Commit
remained unchanged, and generation continued without restarting. This is not
a fixed-cap timing comparison. Private minimum free RAM was 3.609 GiB and free
VRAM 910 MiB; it stopped normally with no new hardware-event stop.

### What caused the long waits, and the placement diagnostics

Python spent about 104s processing input and 3,841s generating; TS/SQL spent
84s and 4,378s. Their small inputs were not filling 64K. Private weighted
prefill/generation rates were 18.92/1.17 tokens/s. Whole-system private disk reads
averaged only 2.41 MiB/s, unlike the 80B paging-heavy run. This motivates testing
how dense weights use the available GPU, not adding cache capacity blindly.

At 22:54, current free VRAM was 6,284 MiB, below the original 64K diagnostic's
6,400 MiB loading gate. No diagnostic load began. The original plan is preserved;
both new arms use 32K context for the same frozen 2K/8K recall/history probes,
temperature zero and reasoning budget zero. A 6,000 MiB loading gate accompanies
the smaller workspace; all runtime stop floors remain unchanged.

Both CPU-KV arms completed and stopped normally:

| Same request | FFNs on CPU, selected attention on GPU | Last 14 complete blocks + output on GPU |
|---|---:|---:|
| 2,060-token input, whole request | 160.469s | 146.047s |
| Short-answer generation | 1.183 tokens/s | 1.564 tokens/s |
| 8,115-token input, whole request | 457.610s | 462.234s |
| Changed-value follow-up | 66.672s | 61.110s |
| History deliberately omitted | UNKNOWN, 7.625s | UNKNOWN, 7.266s |

All supplied facts and changed values are correct; both add a Markdown fence
despite the required plain JSON format. Each follow-up reuses 8,115 tokens and
processes 117 new ones. The complete-layer loader records 4,789.22 MiB GPU
weights and 409.53 MiB workspace, versus 4,745.60 / 403.63 MiB for the control.
Both reserve 1,360 + 531.25 MiB CPU KV. CPU KV makes this a weight-placement
description, not proof that every operation executes on GPU. Desktop load and
adaptive resident caps differ, so this is not a controlled hardware speed claim.

The generation improvement did not improve the file-heavy request. A separately
frozen third arm removes `--no-kv-offload` at the same 32K capacity and complete-
layer placement. Its fresh 6,714 MiB free VRAM passes the 6,650 MiB loading gate.
The loader measures 408 + 116.88 MiB GPU KV, matching the estimate from three
global and eleven sliding-window blocks. Its short request completes in
146.109s, essentially unchanged from 146.047s with CPU KV. It uses 5.906 GiB
dedicated VRAM. During the 8K prefill, free device VRAM falls to 394 MiB and
the monitor stops the server at the unchanged 400 MiB floor. The last progress
entry is 6,536 of 8,115 input tokens; this interrupted answer is unscored and
the third arm's history follow-ups were not run. The additional VRAM consumer
is not attributed by the collected counters; no reboot occurred.

All four requests are byte-identical across the completed pair; both submitted
requests match in the GPU-cache follow-up. This changes cache placement and
associated scheduling, not weight precision. There is no demonstrated
file-heavy latency improvement, and the third arm has less desktop margin.
These recall probes are not native coding scores or a basis for promotion.
[Placement measurements](../../../reports/2026-10-16-dense-placement.json).

### Template and history reuse

Actual API rendering confirms that Gemma's default preserves current tool-turn
reasoning and source facts but drops older-user-turn thoughts. In the public
history follow-up, the server invalidated its checkpoint and reprocessed 9,779
tokens in 513s with zero reuse. The subsequent fresh-file turn reused 10,056
tokens and processed only 77 new ones.

Rendering/tokenizing the same saved requests with preservation false/true gives
137 versus 10,021 identical leading tokens, for 341 extra follow-up tokens with
true. Counts exclude one BOS. This is a concrete cache-reuse hypothesis,
**not a measured speed or quality A/B**. More checkpoints cannot restore an
early prefix changed by templating; clients must resend the reasoning fields
for retention to work. Both settings retain source facts.

**Take:** dense Gemma provides a correct private helper but has not demonstrated
a better overall workflow. Longer thinking is not a guarantee of correct
instructions, citations or migrations. [Dense results](../../../reports/2026-10-16-gemma31.json),
[template evidence](../../../reports/2026-10-16-gemma-template.json).

## 4. Matched Qwen3.6 Q6/Q4 — prepared, not yet measured

The requested Q6 artifact is `Qwen3.6-35B-A3B-UD-Q6_K_XL.gguf`, 29.657 GiB,
pinned revision `a483e9e6cbd595906af30beda3187c2663a1118c`. Current Q4 is
20.614 GiB. Q6 adds about 44% weight storage; it is not a uniform six-bit model.

Among the 120 routed-expert tensors, Q4 uses 80 Q4_K, 37 Q5_K and 3 Q6_K;
Q6 uses 78 Q6_K and 42 Q8_0. Most other quantized tensors are already Q8_0 in
Q4. Counts are not parameter-weighted precision or quality scores.
[Header evidence](../../../reports/2026-10-16-quantization-headers.json).

The frozen pair uses the same isolated runtime, native thinking, temperature
.6, top-k 20, preservation true, context and expert-placement policy. It includes
Python seeds 73/74/75, TypeScript/SQLite, both 120- and 640-record changed-file
history cases, and the same private instruction audit. The existing 640-record
case was added to both arms before either collected answers; the earlier plan
is archived. It previously produced about 52K Qwen input tokens, but new actual
usage must be measured. No profile, question or check was changed.
[Public task plan and identities](../../../reports/2026-10-16-qwen-precision-plan.json).
Desktop usage and adaptive resident caps remain
timing confounders. Fresh memory/VRAM/disk checks precede each load. Keep the
verified Q4 baseline; do not infer Q6 superiority before answers are graded.

## 5. Critical interpretation of the research

The Gemini document is a hypothesis source, not a measurement log. Its original
text remains unchanged. The [critical review](../../../research/reviews/2026-10-14-gemini.md)
records primary sources and disagreements:

- The Qwen publisher table assigns SWE-bench 73.4 to Qwen3.6 and 75.0 to dense
  Qwen3.5-27B, not to non-thinking/thinking modes of Qwen3.6. The publisher uses
  a different agent scaffold and 200K context; those figures are not our local
  quantized scores. The quoted IFBench/telecom figures remain unverified there.
- GLM's 79.5 tau2 result is not explicitly labelled telecom-only. Its Q5 did
  load with apps open despite the report's blanket capacity prediction.
- Dense/MoE labels alone do not determine KV size or instruction reliability.
  Qwen Coder 30B is MoE. An active-parameter count is not stored weight size.
- Neither “Q4 cannot cause errors” nor “Q6 fixes syntax” follows from the
  evidence. Precision effects require matched cases; interruption is unscored.
- Initial Windows prefetch can cause pressure outside a process working set.
  Demand paging enables the 80B trial but does not make 45 GiB of weights
  resident in 14 GiB or make storage as fast as RAM.
- CPU expert weights execute through the CPU backend in these profiles; they
  are not automatically all streamed to GPU every token. `--gpu-layers all`
  plus CPU overrides does not mean all weights reside on GPU.
- Conditional follow-ups include dense Qwen3.5-27B, CPU weight repacking and
  Gemma MTP. None is selected or tested here. Repacking can add committed CPU
  allocations; MTP requires measured acceptance and total latency, not an
  assumed 2x gain. A newer zero-free-VRAM runtime fix does not diagnose these
  dense delays or earlier restarts. Finish the requested matrix first.

## Technical summary, validation and reproducibility

All installations/artifacts stay under `E:/llm/`. Tests use one owned server on
loopback 8081. Production selection/editor settings are unchanged and the
production server is stopped during experiments. No cloud calls, app closures,
automatic boot starts, BIOS/clock/driver changes or pagefile changes were made.
GPU stock and RAM 2800 remain the owner's accepted test condition; the old
restart cause is unresolved.

Ordinary prompts retain a 1,200s default. The owner explicitly permits these
slower trials, which use a 21,600s whole-prompt ceiling including tool turns.
Stop floors remain 2.5 GiB free physical RAM, 1 GiB available commit, 400 MiB
free VRAM and 84 C GPU core, plus new Windows WHEA events. A resident cap is
not a total-commit limit or a stability guarantee.

The isolated runtime is `b11562-noprefetch-v1` at stock commit
`b2f036c0f138414dedc987446f1d9d802f920275`, CUDA 12.4; its rebuilt DLL SHA256 is
`7bf9b3b0549e64c06e2b55bf47235f056838eba7f5b70de62bc48457996d2009`.
Stock binaries remain preserved. [Controls](../../../reports/2026-10-16-runtime-controls.json).

Latest quiet-interval tooling check: 27 offline tests pass in 10.087s; both
public PowerShell scripts parse. All four new Gemma isolated executions pass
the namespace preflight, including the deliberately preserved standalone-test
failure. Code runs only with selected read-only files, no host homes/drives or
network, and time/memory limits. The updated profile check passes; the public
audit reports zero findings in 146 files,
and the whitespace check passes. No new editor UI validation is claimed.

Maintainer sources actually read include project/parent guides, the maintained
Windows/shared Codex and Claude entry points, platform/logging/Python/testing
guidance, host facts, lab methodology/grading docs, the archived research,
pinned runtime/template code and the returned benchmark source ranges.
Benchmark source copies remain frozen; shared adapters needed no routing edit.
Chronological details and validations remain in [tasks](../../tasks.md) and
[prompt history](../../prompts.md). Private raw evidence is under
`local-data/2026-10-16-expansion/`; reports publish reviewed aggregates only.

## Pending work and recommendations

| Item | Next step |
|---|---|
| Dense placement diagnostics | Reviewed: CPU-KV pair complete; GPU-KV short probe complete, 8K interrupted for VRAM and unscored. No unchanged retry. |
| Q6 / matched Q4 | Verify download, collect repeated coding/history/private cases, review and isolate code. |
| Final working setup | Choose from completed quality evidence, validate fresh capacity and any changed editor integration before promotion. |
| Final report/publication | Reconcile this report and public summaries, run checks/audit, publish and report remaining limits. |

Keep independent tests for mutation/type edges and database migrations. Require
an actual source inventory before trusting instruction-heavy answers. Maintain
project decisions in versioned notes and re-read changed files. GPU utilization
alone is not the objective: completed, correctly grounded work is.

## Source provenance

- [Archived Gemini report](../../../research/raw/2026-10-14-gemini/report.txt)
- [Original shared report](https://share.gemini.google/LadMuhd0ajY0)
- [Previous full campaign](../../../reports/2026-10-15-campaign.md)
- [Qwen Coder-Next publisher](https://huggingface.co/Qwen/Qwen3-Coder-Next)
- [Qwen3.6 publisher](https://huggingface.co/Qwen/Qwen3.6-35B-A3B)
- [Gemma dense publisher](https://huggingface.co/google/gemma-4-31B-it)

## Owner request, verbatim

> thats good, but i have points stil need to be solved.
>
> - the kv in ram shuld grow as the context grows right? we should have tested that. How are we utiizing our 64GB RAM currently?
> - Qwen3-coder-next-80B still should be tested, nothing should be left
> - same for gemmma 4 31B dense ( i can wait even longer if things are better)
> - we should try the Q6 of current shiortlisted one.
> - Reread the report and you dont read it blindly, its for you to think what else can be done based on its reasoning, have your research and reaosing too, you have full system access and you can just try things, get stats, and try experiements, its only for you to fill you with good starting and knowledge, but you are free to test things more based on what you learnt from the system experiement and from the theory report gave you.
>
> Complete all these points one by one.
