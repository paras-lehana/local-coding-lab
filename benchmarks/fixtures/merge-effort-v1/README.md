# Small reasoning-effort diagnostic

The prompt and five behavioral groups were frozen on10November2026 before
collecting this diagnostic. They adapt the existing router merge checks to a
single short question. This deliberately does not test instruction discovery,
file retrieval, whole-project edits, invalid root rejection or long history.

Use the same question, seed73, output8192 and1800second whole-request deadline.
Record native effort/template enforcement and sampling for each model; an
unsupported effort label must not be treated as a working setting. This is a
diagnostic cohort, separate from the frozen1200second leaderboard.

Only completed answers are eligible. Review the delivered Python block before
running it in the existing isolated grader. Keep the original answer unchanged,
split implementation from proposed assertions only for reporting, and record
source hashes. Syntax, five independent behavioral groups, the model's three
requested assertions and unsupported execution claims are separate findings.
Do not turn a passed finite suite into a claim of bug-free code.

Checks: [merge_effort_v1.py](../../checks/merge_effort_v1.py).
