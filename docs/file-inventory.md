# File inventory

Initial repository contents and purpose, followed by subsequent change inventories.

| File | Purpose |
|---|---|
| `.gitattributes` | Consistent text line endings |
| `.github/copilot-instructions.md` | Small agent adapter linking authoritative project rules |
| `.github/workflows/offline-checks.yml` | Windows and Ubuntu offline validation workflow |
| `.gitignore` | Exclude local state, credentials, weights and binaries |
| `AGENTS.md` | Portable authoritative project instructions |
| `CHANGELOG.md` | Release change history |
| `CLAUDE.md` | Claude import adapter |
| `CONTRIBUTING.md` | Contributor evidence and validation standards |
| `LICENSE` | MIT terms for original materials; external material excluded |
| `README.md` | Start page, navigation and quick start |
| `SECURITY.md` | Data/execution boundary and disclosure guidance |
| `benchmark.py` | Frozen-input streaming and allowlisted tool harness with parent deadline |
| `benchmarks/fixtures/router-v1/.claude/CLAUDE.md` | Synthetic public project input with instruction hierarchy and deliberate bugs |
| `benchmarks/fixtures/router-v1/.github/instructions/python-v1.md` | Synthetic public project input with instruction hierarchy and deliberate bugs |
| `benchmarks/fixtures/router-v1/.github/instructions/v2/python.md` | Synthetic public project input with instruction hierarchy and deliberate bugs |
| `benchmarks/fixtures/router-v1/AGENTS.md` | Synthetic public project input with instruction hierarchy and deliberate bugs |
| `benchmarks/fixtures/router-v1/docs/config-contract.md` | Synthetic public project input with instruction hierarchy and deliberate bugs |
| `benchmarks/fixtures/router-v1/docs/host.md` | Synthetic public project input with instruction hierarchy and deliberate bugs |
| `benchmarks/fixtures/router-v1/src/config_loader.py` | Synthetic public project input with instruction hierarchy and deliberate bugs |
| `benchmarks/questions/router-v1.txt` | Frozen multi-part source-grounded coding prompt |
| `benchmarks/rubrics/router-v1.md` | Human scoring criteria, excluded from model inputs |
| `catalog/models.json` | Pinned publisher identity, exact size and integrity metadata |
| `catalog/runtime.json` | Pinned publisher identity, exact size and integrity metadata |
| `docs/editors.md` | User/developer guide, decisions, task or session log |
| `docs/memory-and-context.md` | User/developer guide, decisions, task or session log |
| `docs/methodology.md` | User/developer guide, decisions, task or session log |
| `docs/models.md` | User/developer guide, decisions, task or session log |
| `docs/next-experiments.md` | User/developer guide, decisions, task or session log |
| `docs/prompts.md` | User/developer guide, decisions, task or session log |
| `docs/repository-creation.md` | User/developer guide, decisions, task or session log |
| `docs/setup.md` | User/developer guide, decisions, task or session log |
| `docs/tasks.md` | User/developer guide, decisions, task or session log |
| `lab.py` | Pinned downloader, safe extraction, telemetry and guarded process launcher |
| `profiles/gemma4-smoke-proposed.json` | Explicit measured-reference or proposed launch configuration |
| `profiles/qwen36-all-attention-proposed.json` | Explicit measured-reference or proposed launch configuration |
| `profiles/qwen36-reference.json` | Explicit measured-reference or proposed launch configuration |
| `reports/2026-10-14-findings.md` | Reviewed historical evidence or reusable report template |
| `reports/TEMPLATE.md` | Reviewed historical evidence or reusable report template |
| `reports/historical-results.json` | Reviewed historical evidence or reusable report template |
| `research/raw/2026-10-14-gemini/README.md` | Supplied external AI research/provenance with personal details redacted |
| `research/raw/2026-10-14-gemini/report.txt` | Supplied external AI research/provenance with personal details redacted |
| `research/raw/2026-10-14-gemini/source.json` | Supplied external AI research/provenance with personal details redacted |
| `research/reviews/2026-10-14-gemini.md` | Separate verification and decision record |
| `scripts/audit_public.py` | Bootstrap or public-content audit |
| `scripts/setup.ps1` | Bootstrap or public-content audit |
| `tests/test_lab.py` | Offline failure-boundary and integration tests |
| `docs/file-inventory.md` | This per-file change inventory |

## 14 October: research experiment v0.2

| Changed file | Change |
|---|---|
| `lab.py` | Process RAM sampling, owned PID record and explicit stop-file handling |
| `scripts/capture-gpu.ps1` | Dedicated GPU-memory snapshot for an explicit owned PID |
| `scripts/run_isolated.py` | Optional Linux/bubblewrap grading, namespace preflight and resource limits; no host fallback |
| `benchmarks/checks/router_v1.py` | Six human-authored contract groups, added after collection and excluded from model inputs |
| `tests/test_lab.py` | Owned-stop-file regression test |
| `tests/test_isolation.py` | Unsupported-host and failed-preflight execution boundary tests |
| `.github/workflows/offline-checks.yml` | Parse every PowerShell script |
| `profiles/qwen36-reference.json` | Record completed public-fixture pilot, preserve runtime settings |
| `profiles/qwen36-all-attention-proposed.json` | Mark one load-tested pilot, explicitly distinguish production promotion |
| `reports/2026-10-14-placement-plan.md` | Plan frozen before collection |
| `reports/2026-10-14-placement-results.json` | Reviewed measured aggregates, source/output hashes, timings and scores |
| `reports/2026-10-14-placement.md` | Full findings, code/test defects, memory analysis, limitations and next candidates |
| `docs/grading.md` | Restricted execution setup, boundaries and honest scoring procedure |
| `docs/setup.md` | Owned stop request and dedicated GPU measurement usage |
| `docs/methodology.md` | Link first public results and separate post-collection grading |
| `docs/next-experiments.md` | Mark first placement pair complete; retain promotion gates |
| `AGENTS.md` | Route code grading to the restricted runner and separate implementation/test defects |
| `README.md` | v0.2 status, measured pair and updated navigation |
| `CHANGELOG.md` | Record v0.2 changes and limits |
| `SECURITY.md` | Explain the optional grader's distinct execution boundary |
| `docs/tasks.md` | Timestamped experiment, validation and pending-work record |
| `docs/prompts.md` | Original request, recovered constraints and canonical A–G closeout |
| `docs/file-inventory.md` | This per-file update inventory |

Shared context maintenance: project guidance updated once; existing Codex,
Claude and Copilot adapters already point here and remain unchanged. The global
Codex guide and shared router were checked. No private guidance was copied into
the public fixture.

Actual validation: 16 offline unittest checks on Windows; both PowerShell files
parsed; publication audit; live smoke/health/model checks and two completed
tool benchmarks; isolated syntax/behavior/generated-test checks and a failing
known-bug control. Detailed per-run evidence and gaps are in the placement report.

Instructions read for this task: project and parent AGENTS, maintained Codex
guide, shared topic router, platform/logging/Python/Git rules, host facts and
agent-context-maintenance skill. Also read the project methodology, plan,
research archive/review, relevant source code/profiles and rubric. Private
home paths are omitted from this public inventory.

## Campaign additions

The live campaign and frozen scope are indexed from README. `trial.py` owns
one guarded server and a sequential task plan; `scenarios.py` supplies the
history and TypeScript/SQLite cases. `benchmarks/plans/` contains reusable task
lists. `scripts/grade_ts_sql.py` runs reviewed code in the same restricted Linux
environment. Individual `profiles/*campaign.json` files are explicit experiments,
not recommendations merely because their files exist.

- `profiles/qwen36-balanced-64k-campaign.json`: proposed GPU attention plus
  five GPU expert blocks, intended to reduce host RAM at 64K context.
- `profiles/qwen36-q5-balanced-campaign.json`: conditional Q5 precision proposal
  at 32K; it requires a fresh capacity check and a matched Q4 control.
- `profiles/qwen36-q6-balanced-campaign.json`: conditional Q6 precision proposal
  after later RAM recovery; actual header spans, fresh28.5GiB/7000MiB gates,
  same35-CPU-expert placement as Q4/Q5; no measured Q6 fit yet.
- `profiles/qwen36-gpu-expert-cache3072.json`: adaptive cache-size-only proposal
  following the measured1536MiB probe; no new result implied.
- `profiles/qwen36-cache3072-batch512.json`: proposed cache/batch combination,
  explicitly separate from single-variable measurements.
- `profiles/glm47-q6-balanced-campaign.json`: conditional 32K Q6 proposal using
  measured Q4 cache/compute costs and more CPU expert blocks; not yet loaded.
- `profiles/qwen36-q4-precision-control.json`: proposed 32K matched Q4 control
  for the Q5 placement/sampling/context settings.
- `profiles/glm47-q4-f16-campaign.json`: proposed cache-precision-only follow-up
  to the measured 32K q8 GLM profile.
- `profiles/qwen36-research-sampling.json`: proposed temperature/min-p bundle;
  explicitly a two-variable change, requiring matching request temperature.
- `profiles/kimi-linear-balanced-campaign.json`: conditional 32K placement after
  headroom recovery; four checkpoints, fresh memory/disk gates, no measured fit.

New raw run data, private instruction grading inputs and exact weight-deletion
records remain ignored. Reviewed findings are published in
`reports/2026-10-15-campaign.md`; capacity exclusions are in `research/reviews/`.
