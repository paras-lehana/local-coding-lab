# Local model comparison and editor validation

**Status: model selection and API verified; fresh editor UI blocked.** This is
the forwardable campaign record for tooling version0.3.9 and local runtime
configuration2.0. Windows currently exposes no interactive desktop; no fresh
Copilot/Continue UI success is claimed.
The [detailed measurements](../../../reports/2026-10-15-campaign.md) preserve
each attempt; this document brings the request, conclusions and remaining work
together without publishing private sources or answers.

## 1. At a glance

| Requirement | Status | Evidence / remaining work |
|---|---|---|
| Read and verify supplied research | Done | Full archived research, separate corrections, pinned publisher artifacts |
| Recover after the unexpected restart | Done for evidence/recovery | Unclean shutdown confirmed; component cause unknown; interrupted answer unscored |
| Compare feasible families and quantizations | Done with explicit capacity dispositions | Qwen, Gemma, GLM, Coder and Kimi public suites reviewed; optional Qwen Q6 and Kimi64K private rejected before load, not scored |
| Test actual instructions and file references | Done for completed audits | Frozen private six-question audit, recorded read ranges and separate code checks; capped/deadline/capacity attempts distinguished |
| Test cache, placement and thinking settings | Done for planned feasible probes | CPU-KV,1536/2048/3072MiB expert cache, batch, sampling, precision and native/bounded reasoning; checkpoint-count A/B not measured |
| Select a usable model within20 minutes | Provisional working choice installed | QwenQ4 historical34 placement; strongest private case,52K history passes; coding defects remain |
| Verify Copilot and Continue | Partial; UI blocked | Local settings corrected/backed up; production API and tool calls pass; unavailable desktop prevents fresh actual editor test |
| Share reproducible tooling and findings | Done and maintained | Public repository, pinned downloads, guarded launcher, fixtures, reports and Windows/Ubuntu CI |

## 2. Business summary

The experiments now distinguish useful code from plausible answers and passing
self-tests. Higher weight precision has not removed coding defects. Source
following, correct code, long-document recall and completion time are measured
separately. Qwen3.6 UD-Q4 with34CPU expert blocks is the selected working
configuration for this owner's instruction priority. Gemma26QAT is retained
as a lower-memory fallback. Neither is certified for unattended coding.

The latest unexpected restart cannot be diagnosed from the available event
record. Recovery tests completed and subsequent inference has continued with
resource/error stops. This is not a claim that the underlying restart cause is
fixed.

## 3. Request-by-request findings

- **Research and candidate coverage:** the supplied Gemini report was read and
  archived. Publisher metadata corrects architecture and fit assumptions.
  Giant artifacts receive explicit capacity dispositions, not invented scores.
- **Coding correctness:** independent Python, strict TypeScript and SQLite
  checks expose missing validation, shared mutable objects, broken self-tests
  and data loss. Original answers are preserved before any review.
- **Instructions and files:** candidates start from the actual entry document
  and must explicitly read allowlisted frozen sources. Invented reads, wrong
  host assumptions, missing facts and citation support are checked separately.
- **Long context:** history tasks test earlier facts and changed-file reads.
  Gemma and both Qwen finalists succeed at roughly52K input tokens; that is not permanent
  memory or proof of every many-turn coding workflow.
- **Thinking and cache:** native controls differ by model. A nonbinding token
  ceiling can be removed without changing the answer. RAM KV can free VRAM but
  can slow the workload; GPU expert caching retains the host weight copies.
- **Editor usability:** a real local endpoint, correct model selection and
  actual completed tool turns are required. Prepared configuration is not a
  successful editor test. An installed Continue timeout-unit mismatch is
  corrected in the local entry to1200000milliseconds. Input/output client
  budgets are48000/16384. Actual editor flows remain unverified while locked.

### Comparison and my recommendation

| Candidate / profile | Completed private audit | Other decisive evidence | Recommendation |
|---|---:|---|---|
| Qwen3.6 Q4, historical34 placement |31/36; repeated answer byte-identical | Public Python6/6,6/6,4/6;TS5/6;SQL FK failure;52K history passes448s | Working choice for instruction priority; review code independently |
| Same Q4,2GiB expert cache |27/36 | Public Python6/6 all three; strict TS fails; SQL FK failure;52K history passes365s; roughly41decode tok/s | Faster alternate, weaker measured instruction/held-out result |
| Qwen3.6 Q5 |28/36, including2/6 code | Matched public Python no improvement overQ4, mean19% longer and greater RAM use | No demonstrated reason to keep the larger artifact |
| GLM-4.7-Flash Q4/f16 |27/36 | Native public Python6/6, but history count wrong; private mutations/aliases | Tested alternative, no complete workflow advantage |
| GLM Flash Q6 /Q5 |24/36 /21/36 | Inconsistent Python, strict TS errors and SQL data loss | Not selected; higher precision did not fix behavior |
| Gemma4 26B official QAT |19/36 capped and native | Repeated public Python passes; one SQL6/6/TS5/6;52K history passes; lower memory | Retained fallback; weaker actual-instruction following |
| Kimi Linear Q4/f16 |64K private load gate rejected; no score | Public4/6, malformed tool call,6/6;TS4/6;SQL syntax failure; count wrong | Not selected; native non-thinking and narrow memory margin |
| Qwen Coder30 Q4 |Private deadline; unscored | Public Python2/6,3/6,1/6; non-thinking | Not selected |
| Dense Gemma31 /historical Qwen3.8 |No new comparable completed audit | Dense calibration0.95tok/s; previous Qwen3.8 long prefill exceeded20minutes | Reject tested latency profiles |
| Qwen3.6 Q6 /CoderNext80B /research giants |Capacity dispositions, no quality scores | Current apps-open memory insufficient for proposed profiles/artifacts | Do not rank unrun models as better or worse |

This is a workflow recommendation from a small, Codex-reviewed task set.
It is not a universal model leaderboard. I favor the31/36 instruction result
and compiling TypeScript over cache speed because that matches the owner's
priority. The repeated31/36 answer demonstrates reproducibility only. The
chosen profile still aliases mutable objects on one public seed and fails
the SQL migration; no candidate clears every quality requirement.

### Installed settings and measured memory

The chosen Qwen model uses30GPU layers, first34expert blocks on CPU,64K q8 K/V,
512/128 batches,4generation/8prompt threads, non-mmap loading, temperature0.6,
top-p0.95/top-k20/min-p0/repeat1 and32context checkpoints. Native thinking is
on with no separate runtime reasoning ceiling. The16384 output allowance
still limits generated tokens; there is no verified ultra/xhigh switch.

At production readiness: **16.99GiB processRAM,5.38GiB dedicatedVRAM**, with
**11.03GiB freeRAM**. The finalist suite peaks at18.09GiB processRAM.
Actual64K attention KV is680MiB:136CPU/544GPU. Recurrent state is62.81MiB:
18.84CPU/43.97GPU. Model buffers4383.13MiB GPU/16715.52MiB host; compute
273MiB GPU/22.36MiB host. These components are already included in process
measurements; shared GPU memory overlaps RAM and is not extra capacity.

The production greeting returns READY in11.938s. A subsequent actual
read_file round trip answers both configuration snapshots correctly in34.297s,
including native thinking, an absent service port represented as null, and exact probe state.
Health, model alias through curl, idempotent start and stop-target identity
checks pass. This is API evidence, not editor UI evidence.

Four completed nonselected artifacts were fully re-hashed and their exact
files retired, reclaiming93.330GiB: GLMQ4/Q6, QwenQ5 and KimiQ4. Earlier
retirements and all reports remain. QwenQ4 was fully verified before retirement
and loading; Gemma26 remains installed. No directories or unrelated models
were removed. Editor backups containing configuration are encrypted locally
with Windows DPAPI; unrelated providers remain unchanged.

## 4. Technical approach

Windows11 / Ryzen7 5800X / RTX3080 10GB /64GB RAM, with applications open.
The pinned llama.cpp build serves one slot on loopback. Test and production
ports are separate, but only one inference server runs at a time. Every whole
benchmark prompt has a1200-second deadline covering prefill, reasoning and tools.
Full artifact size/SHA checks precede loading. Resource and hardware-event
checks remain enabled; there is no boot-time restart loop.

Portable code and synthetic fixtures live in Git. Private source snapshots,
answers, settings backups and raw logs remain local. Generated code executes
only after source review, in Linux/bubblewrap isolation; there is no Windows
execution fallback. Semantic assessments are by Codex and have not received
independent human review.

## 5. Validation and evidence

- Prior published checkpoint: `e2eb995`, main; Windows and Ubuntu CI passed.
- Final local checks:20 offline tests pass in8.881seconds, public PowerShell
  parsing,113-file public-content audit and diff check pass. A PowerShell5
  stderr-wrapper interruption preceded the full rerun; that partial log remains.
- [Matched Qwen precision data](../../../reports/2026-10-15-qwen-precision-results.json).
- [Cache and placement data](../../../reports/2026-10-15-cache-results.json).
- [Reviewed private-audit aggregates](../../../reports/2026-10-15-private-results.json).
- [Both finalist suites](../../../reports/2026-10-15-finalist-results.json),
  [installed selection/API receipt](../../../reports/2026-10-15-selection.json).
- [Methodology and limitations](../../methodology.md),
  [isolated grading](../../grading.md), [coding use cases](../../coding-use-cases.md).

These benchmark results are the baseline for final profile and editor checks.
No current editor pass or128K-context pass is claimed.

## 6. Owner decisions already established

Autonomous downloads, tests, reports and exact-file retirement are authorized.
Applications remain open. RAM2800 remains an accepted test condition. Quality
comes before speed, within the20-minute whole-prompt limit. No further
confirmation is needed to continue the frozen candidate matrix. Hardware/driver
changes and automatic boot startup are outside this campaign.

## 7. Pending work

The remaining required usability check is actual Copilot and Continue greeting,
file-reading and changed-file/history completion. Windows exposes no interactive
desktop; the UI helper refused to send, and the owner was asked to unlock when
convenient. The frozen prompts and owned test window remain prepared. No
permission to bypass the lock is inferred. Optional QwenQ6 and Kimi64K private
remain capacity-rejected, with a final26.794GiB unloaded snapshot below both
gates. Clean-machine installation, arbitrary128K sessions and a checkpoint-count
A/B were not tested. The restart's component cause remains unknown.

## 8. Practical recommendations so far

Use independent tests and source-supported answers. Small Python helper success
does not establish safe database migration or repository-wide autonomy. Keep
durable project decisions in versioned notes and retrieve relevant files;
neither larger KV nor opening a file tab proves the model received it.
The final recommendation must include actual free-memory margins and client
context budgets, not only the model's native context window.

## 9. Screenshots and UI proof

UIAutomation verified the separate workspace and explicit local model selection
before the desktop became unavailable. No new editor prompt was sent. Actual
greeting, source-reading and changed-file/history tests remain pending. Private
UI evidence is kept locally rather than publishing personal file contents.

## Appendix A. Important corrections

Three-bit weights do not automatically cause syntax failures, and Q6/Q8 do not
guarantee correct code. Qwen Coder30A3B is MoE and non-thinking. In this runtime,
host KV is requested with `--no-kv-offload`. Cache size depends on architecture;
the generic16GB-per32K-token claim is not applicable to the measured Qwen
hybrid model. A zero bugcheck value does not identify a power fault or prove
overclocking.

## Appendix B. Test-run interpretation

Keep the public six-group code checks, public40-point rubric and private36-point
audit distinct. Interrupted/truncated finals are unscored. Report self-test
failures separately from implementation defects. Profiles, tokenization and
tool paths differ; apps-open timings are observed workflow measurements. The
campaign report discloses downloads, hashing, offline checks and editor startup
that overlap particular runs.

## Appendix C. Request

The relevant original requests and continuing constraints are preserved in
[owner-request.txt](owner-request.txt). Earlier credentials and unrelated chats
are excluded from this public record.
