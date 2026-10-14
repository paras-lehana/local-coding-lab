# YYYY-MM-DD — model / experiment

Status: proposed / completed / interrupted / reviewed.

## Question and controls

What changed? What was held fixed? Name fixture/rubric versions, source hashes,
model repository/revision/SHA, runtime commit, template, context, placement,
sampling, reasoning controls, output budget, cache state and whole-prompt limit.

## Machine and delivery

OS/CPU/GPU/RAM, free memory before load, apps-open condition, clock settings,
driver, actual source/tool delivery, editor version if tested. No personal paths
or private source snapshots. Distinguish estimated from measured allocations.

## Results

Record completion status; time to first event and first final text; prefill and
decode; wall time; host working set/commit; dedicated process and total GPU use;
KV/state/compute buffers; temperatures; stop events. Include repeat count.

## Quality and evidence

Separate syntax, isolated behavioral results, citations, absent facts, tool
round trips, history/stale-file checks and UI observations. Provide sanitized
answers or reproducible public inputs. Interrupted work stays unscored.

## Decision and limitations

Recommend retain / retest / reject this profile / promote. Explain why and what
would change the decision. List checks not run. Link provenance and next tasks.
