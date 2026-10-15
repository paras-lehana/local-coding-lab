# Local model comparison and editor validation

**Status: in progress.** This is the forwardable campaign record for tooling
version 0.3.8. Final settings and real editor results remain to be established.
The [detailed measurements](../../../reports/2026-10-15-campaign.md) preserve
each attempt; this document brings the request, conclusions and remaining work
together without publishing private sources or answers.

## 1. At a glance

| Requirement | Status | Evidence / remaining work |
|---|---|---|
| Read and verify supplied research | Done | Full archived research, separate corrections, pinned publisher artifacts |
| Recover after the unexpected restart | Done for evidence/recovery | Unclean shutdown confirmed; component cause unknown; interrupted answer unscored |
| Compare feasible families and quantizations | In progress | Qwen, Gemma, GLM and Coder suites; Kimi verified and queued; optional Qwen Q6 needs fresh capacity |
| Test actual instructions and file references | In progress | Frozen private six-question audit, recorded read ranges and separate code checks |
| Test cache, placement and thinking settings | Partial | Completed CPU-KV, GPU expert cache, batch, sampling, precision and budget comparisons; selection audits pending |
| Select a usable model within20 minutes | Pending | Prefer correctness and source grounding; do not select solely on decode speed |
| Verify Copilot and Continue | Prepared | Separate workspace, explicit local model and read-only modes; no fresh UI inference pass yet |
| Share reproducible tooling and findings | Done and maintained | Public repository, pinned downloads, guarded launcher, fixtures, reports and Windows/Ubuntu CI |

## 2. Business summary

The experiments now distinguish useful code from plausible answers and passing
self-tests. Higher weight precision has not removed coding defects. Source
following, correct code, long-document recall and completion time are measured
separately. Qwen Q4 remains the retained reference; a final replacement has not
been selected. A lower-memory Gemma alternative is retained too.

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
  A Gemma64K case succeeds at roughly52K input tokens; that is not permanent
  memory or proof of every many-turn coding workflow.
- **Thinking and cache:** native controls differ by model. A nonbinding token
  ceiling can be removed without changing the answer. RAM KV can free VRAM but
  can slow the workload; GPU expert caching retains the host weight copies.
- **Editor usability:** a real local endpoint, correct model selection and
  actual completed tool turns are required. Prepared configuration is not a
  successful editor test. An installed Continue timeout-unit mismatch is
  documented; its correction remains staged until final selection.

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

- Latest published checkpoint: `6046eac`, main; Windows and Ubuntu CI passed.
- Local checkpoint checks:20 offline tests, PowerShell parsing, public-content
  audit and diff check passed. Later documentation is awaiting its next check.
- [Matched Qwen precision data](../../../reports/2026-10-15-qwen-precision-results.json).
- [Cache and placement data](../../../reports/2026-10-15-cache-results.json).
- [Reviewed private-audit aggregates](../../../reports/2026-10-15-private-results.json).
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

Finish Kimi's feasible suite after two recorded cache-compatibility errors.
The historical Qwen placement replay scores31/36 in864.266seconds; the faster
2GiB-cache profile scores27/36 in402.703seconds. GLM Q6 native scores24/36,
GLM Q4/f16 scores27/36, and Qwen Q5 scores28/36. These are case-specific
Codex assessments plus isolated code checks, not universal model rankings.
Reassess optional Qwen Q6 from fresh unloaded capacity.
Grade remaining answers, validate the exact finalist on repeated/held-out/large
history tasks, then run actual Copilot and Continue greeting/file/history flows.
Install only the measured chosen profile, reconcile final disposition tables,
and preserve evidence before retiring completed nonleading weights.

## 8. Practical recommendations so far

Use independent tests and source-supported answers. Small Python helper success
does not establish safe database migration or repository-wide autonomy. Keep
durable project decisions in versioned notes and retrieve relevant files;
neither larger KV nor opening a file tab proves the model received it.
The final recommendation must include actual free-memory margins and client
context budgets, not only the model's native context window.

## 9. Screenshots and UI proof

No new editor inference screenshot is evidence of success yet. UIAutomation
has verified the separate test workspace and explicit local model selection.
Actual greeting, source-reading and changed-file/history tests remain pending.
Private UI evidence will stay local if it contains personal file contents.

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
