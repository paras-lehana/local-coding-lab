# Reproducible evaluation

## Scope

The owner wants correct code grounded in `.github`, `.claude`, project files and
documentation; honest handling of absent facts; and usable long chat history.
The current limit is **1200 seconds for one whole prompt**, including input
processing, reasoning, tool turns and final text. Apps stay open. Quality is
more important than raw tokens/sec, but multi-hour prompts are disqualified.

`router-v1` is a new public synthetic project with deliberate merge bugs. It
resembles that instruction-routing workflow without publishing personal files.
Its 40-point rubric is separate from the old private 36-point audit and the
seven-check code diagnostic. No model has yet been scored on router-v1.

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
or privileged mounts. Human review and syntax checks must be labeled separately.
Do not run unreviewed model answers directly on your normal workstation.

Report syntax, semantics, file citations, missing facts and tool reliability
separately. Check claims against successful returned source bytes, not just
requested reads. Interrupted, empty and truncated answers are unscored; retain
their partial evidence instead of counting them as quantization syntax failures.

## Fair comparisons

1. Freeze model SHA, runtime commit, template, profile, question and rubric.
2. Keep context, placement, sampling, budget and source delivery fixed when
   isolating one variable. Record desktop memory changes and cache state.
3. Separate time to first event, first final text, prefill speed, generation
   speed and whole-prompt duration. A greeting can have a large editor prefill.
4. Repeat finalist runs three times and add a held-out task before promotion.
5. Run real editor tool rounds after API checks. Record each editor/version.
6. Evaluate long history, stale-file recovery, beginning/middle/end retrieval and
   context truncation separately. These are planned, not implemented in v0.1.

Commit reviewed aggregate results using [the report template](../reports/TEMPLATE.md).
Keep raw answers local by default. Share only a deliberate sanitized export.
