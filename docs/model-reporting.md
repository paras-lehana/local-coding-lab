# Evidence records for every model

Owner requirement, 23 October 2026: every model tested must have a standalone
report as well as an entry in the current comparison. These are the source
material for later model-specific and comparative blog posts.

## Where to write

- Keep one forwardable report in the model's task folder, alongside the owner's
  original request. Follow the existing docs/tasks convention; link it from
  docs/tasks/README.md and docs/model-comparison.md.
- A new quantization, engine or setting is a separately identified experiment
  inside that model report. Never overwrite the older run or silently replace
  its result. Link historical reports instead of rewriting their evidence.
- Keep raw answers, private source snapshots, editor logs, and machine-specific
  launch receipts under ignored local-data/ or the external data root. Publish
  only reviewed, sanitized measurements. No credentials or private instructions.
- Update the current campaign report and task/prompt logs in the same session.

## Required report contents

1. Why this candidate, what it changes, and what would justify keeping it.
2. Exact upstream repository/revision, quantizer, file bytes/SHA256, license,
   runtime commit/build/hash, model template and effective request controls.
3. Hardware and free RAM/commit/VRAM before loading, desktop load, context,
   KV format/placement, CPU/GPU weight placement, batching and concurrency.
4. Frozen fixture/rubric/script hashes and delivery mode; seeds, deadlines,
   output/reasoning budgets, changed conditions and cache state.
5. Separate results for instructions, citations/actual file reads, absent facts,
   executable code correctness, syntax, tool calls, history and changed files.
6. Load time, input/prefill time, first visible text, reasoning versus final
   output, decode rate, complete workflow time, peak RAM/VRAM and stop reason.
7. Every failed, interrupted, capacity-rejected or unrun configuration, with
   the actual reason. An unfinished answer has no correctness score.
8. Pros, cons, appropriate coding tasks, observed bugs, comparison limits,
   recommendation and what remains untested. API results are not editor proof.
9. Exact reproducible commands and public/private evidence locations, cleanup
   decisions, and the final production availability check.

## Latest scorecard, without overstating coverage

The 20 October v2 scorecard is private instruction audit /36 (weight 0.5),
public router/history/strict TypeScript/SQLite /60 (0.3), and 12 coding tasks
(0.2). Reuse the frozen questions and graders. Show each component and coverage.
Report the full composite only when all components are complete and compatible.
Historical partial composites are explicitly partial; do not compare their
renormalized percentages with a complete score as if coverage were identical.

The whole-prompt deadline is 1200 seconds including prefill, reasoning and all
tool turns. Preserve incomplete cases separately from graded failures. A useful
completion fraction may count unfinished tasks as not completed, but must not
be called a semantic correctness score or a quantization syntax defect.

Review generated code before running it in the existing isolated grader. A
collector must not automatically execute outputs before that review. Retain
grader infrastructure errors separately. For a near-finalist, collect additional
seeds 74 and 75 and a held-out task before promotion. If the baseline lacks a
component, state the gap or collect a matched baseline; never fill it in.

## Blog readiness

Write the report first. Blog claims must link to measured runs and explain
hardware, workload, precision and settings. Keep publisher claims separate from
local observations. Neither a warm cached turn nor a vendor's five-hour agent
evaluation establishes this lab's cold 20-minute workflow performance. A passing
finite test suite does not guarantee bug-free code or unlimited retained memory.
