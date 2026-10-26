# Reproducible evaluation

## Scope

The owner wants correct code grounded in `.github`, `.claude`, project files and
documentation; honest handling of absent facts; and usable long chat history.
The frozen comparison cohort uses **1200 seconds for one whole prompt**,
including input processing, reasoning, tool turns and final text. Apps stay open.
On26October the owner explicitly permits longer accurate instruction-heavy
coding, while rejecting a plain greeting that takes ten minutes. New extended
diagnostics keep their own stated allowance and are not inserted into the old
deadline cohort. A greeting has no tool schemas or instruction files: measure
it separately from an editor greeting that may send a large hidden prefix.
Record load time, cold/warm request time, prefill, reasoning, final text and
completion. A high decode rate or a fast cached answer does not prove a cold
instruction-heavy workflow is fast or correct.

**Historical 16 October expansion:** the owner temporarily relaxed that latency
preference, and explicit collector deadlines could be up to21600seconds. The
20 October scorecard restored1200seconds;26October adds extended diagnostics.
Longer historical runs retain their recorded allowance but cannot rank in the
1200second cohort.
Do not retroactively pass earlier timeouts. Resource stops and a completed
answer before grading remain required.

`router-v1` is a new public synthetic project with deliberate merge bugs. It
resembles that instruction-routing workflow without publishing personal files.
Its 40-point rubric is separate from the old private 36-point audit and the
seven-check code diagnostic. The first [placement pair](../reports/2026-10-14-placement.md)
has provisional Codex-assessed scores and isolated code checks; it is not a leaderboard.

## Freeze inputs before asking the model

```powershell
python benchmark.py --model qwen36-lab --mode tools --prepare-only
```

This saves questions, allowed source files and SHA256 hashes under ignored
`local-data/`. It makes no network request. For actual collection, choose a new
output directory and omit `--prepare-only`:

```powershell
python benchmark.py --model qwen36-lab --mode tools --deadline 1200 --reasoning-budget 2048
python benchmark.py --model qwen36-lab --mode inline --deadline 1200 --reasoning-budget 2048
```

Use only budgets supported by the actual runtime/template. A field accepted by
HTTP is not proof of enforcement. The supplied reasoning ceiling applies per
request/tool turn; the wall deadline covers the entire multi-turn run.

The tools mode advertises exact fixture paths and offers only `read_file`.
It serves immutable allowlisted text, not arbitrary local paths. The inline
mode supplies all source contents directly. Do not infer retrieval success from
inline answers or compare totals without reporting delivery differences.

## Evidence and grading

Each run saves its manifest, source snapshot, prompt, outgoing requests, streamed
events, separate reasoning/final text, tool responses, available timings/usage,
and completion status. Preserve runtime logs and memory telemetry beside them.
The parent kills its network worker at the deadline, even for a silent stream.
Check the server's logs after disconnect: client cancellation alone does not
guarantee every server backend has stopped inference.

The harness **does not execute generated code** and **does not invent a score**.
Review the [rubric](../benchmarks/rubrics/router-v1.md). Behavioral code points
require testing in a disposable restricted environment with no secrets, network
or privileged mounts. Source review and syntax checks must be labeled separately.
Do not run unreviewed model answers directly on your normal workstation.
An optional [Linux/bubblewrap grader](grading.md) now supports reviewed Python
answers. Its independent checks were added after the first answers were seen;
keep that distinction from frozen questions and held-out evaluation explicit.

Report syntax, semantics, file citations, missing facts and tool reliability
separately. Check claims against successful returned source bytes, not just
requested reads. Interrupted, empty and truncated answers are unscored; retain
their partial evidence instead of counting them as quantization syntax failures.

In this campaign, Codex reviews source grounding and authors the independent
contract checks. These assessments have not received independent human review.
They are distinct from model-written self-tests and from the collector, which
assigns no score. Earlier "human" labels were corrected on 15 October; original
raw artifacts remain unchanged. Preserve this attribution when sharing results.

The legacy per-turn field `first_final_seconds` measures the first visible
`content` fragment, which can be a plan before a tool call. It is not necessarily
the first text of the eventual answer or whole-task completion. Identify the
actual final tool-free turn separately, and use total wall time for the owner's
20-minute requirement. Likewise, review visible content across tool turns when
locating delivered code; an implementation can precede the final message.

In `benchmark.py` and `scenarios.py`, `first_event_seconds` and
`first_final_seconds` use the start of the **whole workflow** as their time
origin. Later turns therefore contain cumulative offsets, not that turn's
individual time to first token. Use the saved event timestamps and request
boundaries, or the server's per-request input/generation timings, when reporting
turn latency. The separate plain-greeting and direct-coding workers start a new
timer for each request; do not mix these two interpretations in one table.

## Fair comparisons

1. Freeze model SHA, runtime commit, template, profile, question and rubric.
2. Keep context, placement, sampling, budget and source delivery fixed when
   isolating one variable. Record desktop memory changes and cache state.
3. Separate time to first event, first final text, prefill speed, generation
   speed and whole-prompt duration. A greeting can have a large editor prefill.
4. Repeat finalist runs three times and add a held-out task before promotion.
5. Run real editor tool rounds after API checks. Record each editor/version.
6. Evaluate long history, stale-file recovery, beginning/middle/end retrieval and
   context truncation separately. The v0.3 history scenarios implement retained
   ledger facts and changed-file reads. A tool-failure recovery claim additionally
   requires observing an attempted unavailable-ledger read and its handling.

Repeated seeds in one server are not identical cold starts. Record each turn's
cached and newly processed tokens: native outputs and retained checkpoints can
change prefix reuse even when the task order is fixed. A fresh server also does
not clear Windows' file cache. Hashing/downloading a model can warm that cache;
do not silently flush the owner's system cache to manufacture a cold result.
The Q4/Q6 comparison keeps task order and policy fixed, but desktop load, file
cache state and resolved resident caps remain practical timing limitations.

Inspect saved serialized requests before describing effective controls. On
16October, the separate legacy private audit sent `top_k=20`,
`preserve_thinking=true` and `max_tokens=24576`. These override Gemma's server
publisher profile (`top_k=64`, preservationfalse) and differ from the public
coding requests'16384-token limit. Coder-Next's private request also overrides
its server top_k40. These are valid recorded configurations, but they are not
publisher-sampling private measurements. Do not silently change a started run
to make it match a planned label. Record the discrepancy, retain the original
requests, and freeze any new variant separately. The matched QwenQ4/Q6 private
pair agrees with its server top_k20/preservationtrue settings.

If a resource intervention is needed during collection, preserve the original
launch and requests and save a separate timed before/after receipt. Report the
affected run as an interrupted or changed-resource experiment as appropriate;
do not claim its timing is an unchanged-profile comparison. On16October the
Gemma private audit continued after a smaller owned-process resident cap freed
about1.95GiB of system headroom. Its sampling/context/weights stayed unchanged,
and the original cap and monitor history remain available.

Commit reviewed aggregate results using [the report template](../reports/TEMPLATE.md).
Keep raw answers local by default. Share only a deliberate sanitized export.
