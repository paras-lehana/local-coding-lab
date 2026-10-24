# Verify code in isolation

The collector never executes model output. Review an answer first, then place
its implementation in `candidate.py` and its proposed tests in `model_tests.py`
inside a new ignored local-data grading directory. Preserve the original code;
do not repair it before recording the initial result. Copy
`benchmarks/checks/router_v1.py` into that directory as `behavior_checks.py`.
Only those three regular files are exposed to the optional grading runner.

On Linux, or an existing WSL Ubuntu installation with `bubblewrap` and Python:

```bash
python3 scripts/run_isolated.py \
  --directory local-data/my-run/grading \
  --output local-data/my-run/grading-result.json
```

From Windows, use the corresponding Linux paths, for example:

```powershell
wsl -d Ubuntu --exec python3 /mnt/e/llm/local-coding-lab/scripts/run_isolated.py --directory /mnt/e/llm/local-coding-lab/local-data/my-run/grading --output /mnt/e/llm/local-coding-lab/local-data/my-run/grading-result.json
```

The runner does not install WSL or packages and has **no Windows-host fallback**.
It refuses an existing output. Its preflight checks namespace separation,
absence of host home/mount directories, the three-file input inventory and the
cleared environment. A failed preflight saves evidence and executes no test
file. The process namespace is isolated; the host network namespace is not
shared. Only the system runtime and selected source files are bound read-only.
The candidate cannot see the rest of your checkout, Windows drives or home.

Each process has a 20-second wall limit, 10-second CPU limit, 512 MiB address
space, capped descriptors/processes and 1 MiB per captured output file. Review
the saved return codes and unittest output; a generated test can fail while
the separately checked implementation passes. Do not call such a failure a
model syntax error. The runner returns nonzero on either failed grading pass.

Run grading invocations sequentially on the shared WSL host. On 17 October,
concurrent invocations passed their namespace probes but three later processes
failed with `bwrap: fork: Resource temporarily unavailable`. Preserve those
outputs as infrastructure failures, then retry unchanged inputs and limits in
new result files. Record the selected result and both hashes; never count a
process-creation failure as an incorrect model answer or relax isolation.

A passing finite suite is not proof of a correct implementation. The frozen
private merge checks missed local-only keys and nested mutable values inside
shallow copies. Additional checks exposed both after source review. Preserve
the frozen scores and label these as post-review diagnostics, including when
they were prepared; do not retrospectively call them held out.

Inspect **all visible assistant turns** in `turns.json`, not just `answer.txt`.
The latter contains the final tool-free message. A model may provide an
implementation before another tool call and finish with the migration/tests.
Record the selected turn and code-fence index; do not grade such visible code
as missing. Reasoning-only drafts are not delivered implementations. In the
GLM Q5 held-out case, the TypeScript implementation appears in visible turn 4,
before a final schema read, while the last message contains SQL and examples.

This is a restricted environment for reviewed simple Python answers, not a
guarantee against actively hostile native code or a kernel exploit. Use a
disposable VM for that threat model. Do not mount credentials or run unknown
answers on the normal workstation to work around unavailable isolation.

The six contract groups correspond to the existing 12 behavior points. The
checks were added after the first answers were collected; they are not held out.
Score instruction discovery, grounding, absent facts, test quality and actual
reads separately using the rubric. Do not award behavior points for syntax alone.

## TypeScript and SQLite

`scripts/grade_ts_sql.py` additionally accepts reviewed `candidate.ts`,
`migration.sql`, the frozen `schema.sql`, and the two independent
`benchmarks/checks/ts_sql_v1.*` checks. Supply an already verified Linux Node
binary and TypeScript `lib` directory explicitly. There is no package installation
or Windows execution fallback in the grader. It compiles with strict TypeScript
settings and executes the emitted JavaScript only inside the namespace.

Node uses a 128 MiB JavaScript heap limit and an 8 GiB **virtual address** ceiling
for V8 reservations; this is not an 8 GiB physical-memory allocation. Compilation
plus JS checks have a 60-second wall limit and 30-second CPU limit. SQLite retains
the Python runner's 20-second / 512 MiB limits. Preserve initial errors before any
repair. A failed migration is not six independently observed assertion failures.

The SQLite checker strips leading comments from trace statements before checking
transaction boundaries. Its uniqueness/reference checks insert their own rows,
so loss of original data does not also masquerade as a missing constraint.
This correction was made during the 15 October campaign: original results are
retained, unchanged candidates were rerun, and the report identifies affected
scores. The positive control includes leading line/block comments.

## Screening false positives

On24October the legacy JavaScript coding grader rejected a local scheduler
function named `process()` through a lexical capability filter. Source review
confirmed that it did not access Node's global process object. Preserve such
a screening result as review-required, not an observed malicious action or a
behavior-test failure. The separately recorded recheck used the exact unchanged
response hash, identical frozen behavior checks and the existing VM/OS resource
isolation; only that one name check was bypassed for that reviewed artifact.
Actual execution then exposed duplicate scheduling (10/11 checks), so the task
still failed. Keep both grader hashes/results and the reason for selection.
Never disable capability screening generally or edit model code to obtain a
better score. See the24October Qwen model report for the measured example.

## Preserve passing scores alongside newly exposed bugs

The24October native Qwen Q4 JavaScript answers pass the frozen worker-pool
11/11 and merge8/8 checks, then fail source-motivated isolated diagnostics.
A synchronous second initial worker can throw while an earlier worker is
pending; later completion wrongly starts new work. Replacing an array with
an object can wrongly merge old numeric-index fields. These cases are absent
from the frozen suite. Keep the original passes and separately identify the
new test preparation time, exact unchanged response/grader hashes, isolation
and results. They are post-review diagnostics, not held-out tests or a
retroactive scoring change. Add such cases only in a separately versioned
future benchmark applied consistently to candidates. See the24October Qwen
model report for evidence.

## Smoke wording is not a quality benchmark

The existing smoke asks `Reply with exactly READY.` while old report checks
expect the literal `READY` without a period. Because the prompt itself ends
with that period, `READY.` is ambiguous evidence of a formatting mistake.
Preserve the actual request, answer and historical literal-check result, but
do not count this punctuation alone as an instruction-following defect or a
reason to reject a model. The current smoke only gates nonempty transport.
Use an explicitly quoted target in a separately versioned future format test;
do not rewrite a request after seeing its response.
