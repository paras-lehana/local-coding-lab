# File inventory

## 10 November planning-only handoff

- `docs/tasks/2026-11-10-plan/2026-11-10-plan-v0.12.1.md`: Nov 10 2026 plan;36candidate/configuration groups,
  P0–P7, evaluation contracts, settings/context matrices, storage pins/rotation,
  single-runner multi-agent procedure, reproducible command cards and reporting.
- `docs/tasks/README.md`: index of the completed plan, execution not started.
- `docs/tasks.md`, `docs/prompts.md`: latest planning scope, original request,
  actual validation, independent-review corrections and deferred execution.
- No application/runtime/profile code or model artifacts changed by this task.


Initial repository contents and purpose, followed by subsequent change inventories.

## 10 November tuning continuation

36 public files in this change set. Private receipts, model answers, weights and
local collector/controller scripts remain outside Git. Prepared profiles are not
passed trials; measured profile snapshots are retained in the evidence JSON.

| File | Change |
|---|---|
| [AGENTS.md](../AGENTS.md) | New campaign authorization, exact incident and current stop/recovery boundary. |
| [CHANGELOG.md](../CHANGELOG.md) | Version0.12.0 measured tuning, split-shard support and interrupted follow-ups. |
| [README.md](../README.md) | Current measured status and report/incident navigation. |
| [VERSION](../VERSION) | Set0.12.0. |
| [articles.md](../articles.md) | Preserve fourteen supplied sources; add new release/residency/KV/effort evidence and limits. |
| [benchmarks/checks/merge_effort_v1.py](../benchmarks/checks/merge_effort_v1.py) | Five independent merge behavior groups including deep mutable isolation. |
| [benchmarks/fixtures/merge-effort-v1/README.md](../benchmarks/fixtures/merge-effort-v1/README.md) | Frozen task, sampling, controls and grading boundary. |
| [benchmarks/fixtures/merge-effort-v1/request.json](../benchmarks/fixtures/merge-effort-v1/request.json) | Predeclared merge prompt shared by effort/placement diagnostics. |
| [catalog/models.json](../catalog/models.json) | Pin Gemma12 QAT/Q6, Gemma31Q6 and Flash split shards/remote paths. |
| [docs/file-inventory.md](../docs/file-inventory.md) | This per-file change inventory. |
| [docs/memory-and-context.md](../docs/memory-and-context.md) | Measured Gemma CPU/GPU KV allocations, capacity versus occupancy. |
| [docs/model-comparison.md](../docs/model-comparison.md) | Current partial comparison and new hardware stop. |
| [docs/models.md](../docs/models.md) | Add measured Gemma12 record; current states and retained comparisons. |
| [docs/prompts.md](../docs/prompts.md) | Exact owner request, current evidence and canonical closeout. |
| [docs/tasks.md](../docs/tasks.md) | Dated campaign checkpoints and stop disposition. |
| [docs/tasks/2026-10-26-flash-next/2026-10-26-flash-next-v0.10.0.md](../docs/tasks/2026-10-26-flash-next/2026-10-26-flash-next-v0.10.0.md) | New native runtime controls and resident3 FECS stop addendum. |
| [docs/tasks/2026-11-03-groot/2026-11-03-groot-19b-a3b-apps-open-v1.0.md](../docs/tasks/2026-11-03-groot/2026-11-03-groot-19b-a3b-apps-open-v1.0.md) | Exact-file retirement receipt; preserve earlier unscored memory stops. |
| [docs/tasks/2026-11-10-gemma12/2026-11-10-gemma12-v0.12.0.md](../docs/tasks/2026-11-10-gemma12/2026-11-10-gemma12-v0.12.0.md) | Gemma12 identity,2/3/2 residency, native effort, CPU-KV, bugs and pending full suites. |
| [docs/tasks/2026-11-10-gemma12/owner-request.txt](../docs/tasks/2026-11-10-gemma12/owner-request.txt) | Exact campaign request retained with this task/model record. |
| [docs/tasks/2026-11-10-tuning/2026-11-10-tuning-v0.12.0.md](../docs/tasks/2026-11-10-tuning/2026-11-10-tuning-v0.12.0.md) | Campaign decisions, measured matrix, incident and every remaining trial/reason. |
| [docs/tasks/2026-11-10-tuning/owner-request.txt](../docs/tasks/2026-11-10-tuning/owner-request.txt) | Exact campaign request retained with this task/model record. |
| [docs/tasks/README.md](../docs/tasks/README.md) | Index the new campaign and Gemma12 report with actual status. |
| [experiments/strata/engine-0159-pins.json](../experiments/strata/engine-0159-pins.json) | Exact side-runtime asset and binary pins. |
| [lab.py](../lab.py) | Verify all automatic split shards; remote subdirectory pins and complete-set disk admission. |
| [profiles/flash-q2-llama-cpu48-q8-32k-res1.json](../profiles/flash-q2-llama-cpu48-q8-32k-res1.json) | Exact model/runtime/settings and admission floors; prepared-not-loaded. |
| [profiles/gemma4-12b-qat-layer32-cpukv-res3-32k.json](../profiles/gemma4-12b-qat-layer32-cpukv-res3-32k.json) | Exact model/runtime/settings and admission floors; diagnostic-only-not-promoted. |
| [profiles/gemma4-12b-qat-layer32-guarded32.json](../profiles/gemma4-12b-qat-layer32-guarded32.json) | Exact model/runtime/settings and admission floors; diagnostic-only-not-promoted. |
| [profiles/gemma4-12b-qat-layer32-res3-32k.json](../profiles/gemma4-12b-qat-layer32-res3-32k.json) | Exact model/runtime/settings and admission floors; diagnostic-only-not-promoted. |
| [profiles/gemma4-12b-qat-layer34-cpukv-res3-32k.json](../profiles/gemma4-12b-qat-layer34-cpukv-res3-32k.json) | Exact model/runtime/settings and admission floors; diagnostic-only-not-promoted. |
| [profiles/gemma4-12b-qat-layer36-cpukv-res3-32k.json](../profiles/gemma4-12b-qat-layer36-cpukv-res3-32k.json) | Exact model/runtime/settings and admission floors; prepared-not-loaded. |
| [reports/2026-11-10-flash-fecs-stop.json](../reports/2026-11-10-flash-fecs-stop.json) | Sanitized exact event/configuration/telemetry and evidence hashes. |
| [reports/2026-11-10-flash-fecs-stop.md](../reports/2026-11-10-flash-fecs-stop.md) | Incident timeline, attribution limits and unstarted queue controls. |
| [reports/2026-11-10-flash-tuning.json](../reports/2026-11-10-flash-tuning.json) | Three normal short controls; caps/counters/identities, no quality score. |
| [reports/2026-11-10-gemma12-tuning.json](../reports/2026-11-10-gemma12-tuning.json) | Five run receipts, profiles, timings, resource minima and four isolated grades. |
| [research/reviews/2026-11-10-release-and-tuning.md](../research/reviews/2026-11-10-release-and-tuning.md) | Primary-source availability and Windows/runtime applicability review. |
| [tests/test_model_shards.py](../tests/test_model_shards.py) | Five regressions for sibling integrity, paths, pins, disk and resume behavior. |


## 9 November research continuation

| Entry point | What it contains |
|---|---|
| [articles.md](../articles.md) | Every supplied article/report, its claims, corrections, local tests and next decision |
| [docs/models.md](models.md) | Every candidate's tested quants, strengths, bugs, missing results and standalone report |
| [Merged campaign](tasks/2026-11-09-merged-research/2026-11-09-merged-models-articles-and-experiments-v0.11.0.md) | Claude reconciliation, new configurations, measured outcomes, validation and pending work |
| [Historical configuration matrix](tasks/2026-11-03-master-summary/2026-11-03-all-models-and-combinations-v1.0.md) | Row-level runtime, quant, context, placement, sampler and outcome through3November; newer results are in the merged campaign |
| [Memory guide](memory-and-context.md) | Capacity versus occupied context and physical residency; CPU/GPU KV and measured allocation controls |
| [Fusion/speed review](../research/reviews/2026-11-09-fusion-and-speed.md) | Recovered fusion algorithm critique, microbatch/cache measurements and source-based limitations |
| [Fixed-prefix fixture](../benchmarks/fixtures/prefill-native-v1/README.md) | Exact public native-completion requests for cold/repeated/middle-edit controls |
| [Prefill receipt](../reports/2026-11-09-flint-prefill-controls.json) | Fifteen completed performance controls, hashes, allocation, cache reuse and memory telemetry; no correctness score |
| [Private-audit receipt](../reports/2026-11-09-flint-q3xl-private72k.json) | Reviewed capped Flint25/36 result and isolated behavior breakdown; private text excluded |
| [Profiles](../profiles) | Exact measured or explicitly unrun controls; check each profile's validation status and fresh capacity gates |

<!-- 2026-11-09-change-inventory:start -->

### Public file changes in this campaign

This includes reviewed inherited Claude work and the continuation. It is a working-tree inventory, not a claim that an unrun profile passed inference. Private collectors and raw outputs remain ignored.

| File | Change / purpose |
|---|---|
| `AGENTS.md` | Route resumed work to current evidence and article/model records; preserve installation and ownership boundaries. |
| `CHANGELOG.md` | Record the merged campaign, new controls, observed limits and validation. |
| `README.md` | Link the article ledger, complete model index and current campaign findings. |
| `VERSION` | Advance the documented campaign version to 0.11.0. |
| `articles.md` | Table of fourteen supplied sources: claims, corrections, local evidence and next decisions. |
| `benchmarks/fixtures/prefill-native-v1/README.md` | Frozen public native-completion fixture, provenance and exact cold/repeat/middle-edit requests; performance-only, no quality score. |
| `benchmarks/fixtures/prefill-native-v1/requests.json` | Frozen public native-completion fixture, provenance and exact cold/repeat/middle-edit requests; performance-only, no quality score. |
| `catalog/models.json` | Preserve exact new artifact pins and separate publisher filenames from local staging filenames; correct inspected reasoning metadata. |
| `catalog/runtime.json` | Catalog the isolated b12069 runtime with exact files and hashes. |
| `docs/file-inventory.md` | Navigation and this complete per-file campaign inventory. |
| `docs/memory-and-context.md` | Separate KV allocation, occupied context, residency, commit and device telemetry; add measured rollback and disk observations. |
| `docs/methodology.md` | Clarify first-event/content/tool timing, measurement limitations and distinct diagnostic cohorts. |
| `docs/model-comparison.md` | Reconcile newer coverage and link current measured findings without combining incompatible suites. |
| `docs/models.md` | Model-wise result, configuration, strengths, bugs, unrun reasons and reasoning-control tables. |
| `docs/prompts.md` | Owner request, chronological decisions, validation and canonical closeout. |
| `docs/tasks.md` | Timestamped recovery state, live identities, completed experiments and remaining work. |
| `docs/tasks/2026-10-18-strata/2026-10-18-strata-on-10gb-v0.6.0.md` | Standalone report/addendum: Strata on an RTX 3080 10 GB. Historical results remain distinct from new or unrun controls. |
| `docs/tasks/2026-10-20-bonsai2/2026-10-20-ternary-bonsai2-27b-pq2-ptq1-v0.10.0.md` | Standalone report/addendum: Ternary Bonsai 2 27B (PQ2_0 and PTQ1_0) on an RTX 3080 10 GB. Historical results remain distinct from new or unrun controls. |
| `docs/tasks/2026-10-23-flint/2026-10-23-recursive-flint-v0.8.0.md` | Standalone report/addendum: Recursive Flint on RTX 3080 10 GB. Historical results remain distinct from new or unrun controls. |
| `docs/tasks/2026-10-24-qwen-coverage/2026-10-24-qwen36-v0.9.0.md` | Standalone report/addendum: Qwen3.6 precision, memory and coding coverage. Historical results remain distinct from new or unrun controls. |
| `docs/tasks/2026-10-26-flash-next/2026-10-26-flash-next-v0.10.0.md` | Standalone report/addendum: Qwen3.8-Flash-Next: refreshed quant and engine investigation. Historical results remain distinct from new or unrun controls. |
| `docs/tasks/2026-10-26-qwen38-dense/2026-10-26-qwen38-dense-v0.10.0.md` | Standalone report/addendum: Qwen3.8-27B dense: precision and engine learning record. Historical results remain distinct from new or unrun controls. |
| `docs/tasks/2026-11-03-deep-research/2026-11-03-deep-research-v1.0.md` | Standalone report/addendum: Deep research: new models, Strata, Flash-Next, llama.cpp and token-level fusion (3 Nov 2026). Historical results remain distinct from new or unrun controls. |
| `docs/tasks/2026-11-03-groot/2026-11-03-groot-19b-a3b-apps-open-v1.0.md` | Standalone report/addendum: Groot-19B-A3B-261023 Q4_K_M with apps open on an RTX 3080 10 GB. Historical results remain distinct from new or unrun controls. |
| `docs/tasks/2026-11-03-groot/owner-request.txt` | Relevant owner request and continuing constraints, with credentials and private source text excluded. |
| `docs/tasks/2026-11-03-master-summary/2026-11-03-all-models-and-combinations-v1.0.md` | Standalone report/addendum: All models, combinations and tuning on an RTX 3080 10 GB (12 October to 3 November 2026). Historical results remain distinct from new or unrun controls. |
| `docs/tasks/2026-11-09-dory4b/2026-11-09-dory4b-v0.11.0.md` | Standalone report/addendum: Dory1.0-4B: prepared looped-model comparison. Historical results remain distinct from new or unrun controls. |
| `docs/tasks/2026-11-09-gemma4-31b/2026-11-09-gemma4-31b-v0.11.0.md` | Standalone report/addendum: Gemma 4 31B dense: historical model record. Historical results remain distinct from new or unrun controls. |
| `docs/tasks/2026-11-09-glm47-flash/2026-11-09-glm47-flash-v0.11.0.md` | Standalone report/addendum: GLM-4.7-Flash: historical model record. Historical results remain distinct from new or unrun controls. |
| `docs/tasks/2026-11-09-kimi-linear-48b/2026-11-09-kimi-linear-48b-v0.11.0.md` | Standalone report/addendum: Kimi-Linear-48B-A3B: historical model record. Historical results remain distinct from new or unrun controls. |
| `docs/tasks/2026-11-09-merged-research/2026-11-09-merged-models-articles-and-experiments-v0.11.0.md` | Standalone report/addendum: Merged model research, article ledger and resumed experiments. Historical results remain distinct from new or unrun controls. |
| `docs/tasks/2026-11-09-merged-research/owner-request.txt` | Relevant owner request and continuing constraints, with credentials and private source text excluded. |
| `docs/tasks/2026-11-09-nemotron35-bolt/2026-11-09-nemotron35-bolt-v0.11.0.md` | Standalone report/addendum: Nemotron 3.5 Bolt: historical model record. Historical results remain distinct from new or unrun controls. |
| `docs/tasks/2026-11-09-qwen3-coder-next80/2026-11-09-qwen3-coder-next80-v0.11.0.md` | Standalone report/addendum: Qwen3-Coder-Next 80B: historical model record. Historical results remain distinct from new or unrun controls. |
| `docs/tasks/2026-11-09-qwen3-coder30/2026-11-09-qwen3-coder30-v0.11.0.md` | Standalone report/addendum: Qwen3-Coder-30B-A3B: historical model record. Historical results remain distinct from new or unrun controls. |
| `docs/tasks/2026-11-09-qwen3-next80-instruct/2026-11-09-qwen3-next80-instruct-v0.11.0.md` | Standalone report/addendum: Qwen3-Next-80B-A3B-Instruct: historical model record. Historical results remain distinct from new or unrun controls. |
| `docs/tasks/2026-11-09-qwen35-9b/2026-11-09-qwen35-9b-v0.11.0.md` | Standalone report/addendum: Qwen3.5-9B: prepared small-model comparison. Historical results remain distinct from new or unrun controls. |
| `docs/tasks/README.md` | Index individual candidate and merged campaign reports. |
| `experiments/llama-mmap-prefetch/README.md` | Document the isolated b12069 build and completed tiny-model CPU/GPU controls. |
| `experiments/strata/check_guard.py` | Exercise identity-latch lifecycle with harmless processes. |
| `experiments/strata/guard.py` | Require the latched native process identity when requested; fail if it disappears or changes. |
| `experiments/strata/windows-token-defaults.md` | Explain the reproduced Windows token-default ACL failure, isolated correction, privacy controls and measurement limits. |
| `experiments/strata/windows-token-defaults.patch` | Narrow generic-access correction against the exact pinned upstream frontend; native engine unchanged. |
| `lab.py` | Enforce minimum stop floors, preserve upstream/local filenames and detect provider-qualified GPU, WHEA and unexpected-restart events before further loading. |
| `profiles/bonsai2-pq2-gpu52.json` | bonsai2-27b-pq2 configuration; status: proposed-not-measured. Exact flags, gates and evidence retained in this file. |
| `profiles/bonsai2-ptq1-gpu99.json` | bonsai2-27b-ptq1 configuration; status: proposed-not-measured. Exact flags, gates and evidence retained in this file. |
| `profiles/dory-4b-q5-gpu-mmap64.json` | dory-4b-q5 configuration; status: blocked-runtime: needs a Dory-enabled llama.cpp build (fork rev 98a74c97 / PR 30306); stock b12069 lacks the architecture. Exact flags, gates and evidence retained in this file. |
| `profiles/flint-q3xl-prefill-b12069-u16-resident1.json` | flint-q3xl configuration; status: measured-native-prefill-diagnostic-unscored. Exact flags, gates and evidence retained in this file. |
| `profiles/flint-q3xl-prefill-short2k-fullswa.json` | flint-q3xl configuration; status: measured-native-prefill-diagnostic-unscored. Exact flags, gates and evidence retained in this file. |
| `profiles/flint-q3xl-prefill-short2k-windowed.json` | flint-q3xl configuration; status: measured-native-prefill-diagnostic-unscored. Exact flags, gates and evidence retained in this file. |
| `profiles/flint-q3xl-prefill-u128-cache1536-resident3.json` | flint-q3xl configuration; status: measured-native-prefill-diagnostic-unscored. Exact flags, gates and evidence retained in this file. |
| `profiles/flint-q3xl-prefill-u128-cache1536-resident6.json` | flint-q3xl configuration; status: measured-native-prefill-diagnostic-unscored. Exact flags, gates and evidence retained in this file. |
| `profiles/flint-q3xl-prefill-u16-cache1536.json` | flint-q3xl configuration; status: measured-native-prefill-diagnostic-unscored. Exact flags, gates and evidence retained in this file. |
| `profiles/flint-q3xl-prefill-u16-resident1.json` | flint-q3xl configuration; status: measured-native-prefill-diagnostic-unscored. Exact flags, gates and evidence retained in this file. |
| `profiles/flint-q3xl-prefill-u16-resident3.json` | flint-q3xl configuration; status: measured-native-prefill-diagnostic-unscored. Exact flags, gates and evidence retained in this file. |
| `profiles/flint-q3xl-prefill-u32-resident1.json` | flint-q3xl configuration; status: measured-native-prefill-diagnostic-unscored. Exact flags, gates and evidence retained in this file. |
| `profiles/flint-q3xl-prefill-u4-resident1.json` | flint-q3xl configuration; status: measured-native-prefill-diagnostic-unscored. Exact flags, gates and evidence retained in this file. |
| `profiles/flint-q3xl-prefill-u64-cache1536-resident3.json` | flint-q3xl configuration; status: measured-native-prefill-diagnostic-unscored. Exact flags, gates and evidence retained in this file. |
| `profiles/flint-q3xl-prefill-u64-resident1.json` | flint-q3xl configuration; status: measured-native-prefill-diagnostic-unscored. Exact flags, gates and evidence retained in this file. |
| `profiles/flint-q3xl-private72k-budget1024.json` | flint-q3xl configuration; status: extended-private-completed-25-of-36-not-promoted. Exact flags, gates and evidence retained in this file. |
| `profiles/flint-q3xl-private72k-native-u128.json` | flint-q3xl configuration; status: measured-extended-private31-of36-not-promoted. Exact flags, gates and evidence retained in this file. |
| `profiles/flint-q3xl-quality72k-u128-budget1024.json` | flint-q3xl configuration; status: prepared-capped-quality-followup-not-run. Exact flags, gates and evidence retained in this file. |
| `profiles/groot-19b-q4-moe36-cache512-resident4-mmap64.json` | groot-19b-a3b-q4 configuration; status: proposed-not-measured. Exact flags, gates and evidence retained in this file. |
| `profiles/groot-19b-q4-moe36-mmap64.json` | groot-19b-a3b-q4 configuration; status: proposed-not-measured. Exact flags, gates and evidence retained in this file. |
| `profiles/groot-q4-resident4-guarded64.json` | groot-19b-a3b-q4 configuration; status: prepared-9nov-not-run. Exact flags, gates and evidence retained in this file. |
| `profiles/k2-mova-q4-fit48k.json` | k2-mova-36b-q4 configuration; status: proposed-not-measured. Exact flags, gates and evidence retained in this file. |
| `profiles/lfm25-qad-q4-cpu28.json` | lfm25-24b-qad-q4 configuration; status: proposed-not-measured. Exact flags, gates and evidence retained in this file. |
| `profiles/nemotron-bolt-fit64k.json` | nemotron-bolt-74b-24gb configuration; status: proposed-not-measured. Exact flags, gates and evidence retained in this file. |
| `profiles/qwen35-9b-q4-gpu-cpukv64.json` | qwen35-9b-q4 configuration; status: proposed-full-gpu-weights-cpu-kv-not-run. Exact flags, gates and evidence retained in this file. |
| `profiles/qwen35-9b-q4-gpu-mmap64.json` | qwen35-9b-q4 configuration; status: proposed-not-measured. Exact flags, gates and evidence retained in this file. |
| `profiles/qwen35-9b-q5-gpu-mmap64.json` | qwen35-9b-q5 configuration; status: proposed-not-measured. Exact flags, gates and evidence retained in this file. |
| `profiles/qwen36-iq3s-moe34-mmap64.json` | qwen36-iq3s configuration; status: proposed-not-measured. Exact flags, gates and evidence retained in this file. |
| `profiles/qwen36-iq4xs-core0-mmap64.json` | qwen36-iq4xs configuration; status: proposed-not-measured. Exact flags, gates and evidence retained in this file. |
| `profiles/qwen36-iq4xs-moe34-mmap64.json` | qwen36-iq4xs configuration; status: proposed-not-measured. Exact flags, gates and evidence retained in this file. |
| `profiles/qwen36-q4-core0-mmap64.json` | qwen36-q4 configuration; status: proposed-baseline-not-measured. Exact flags, gates and evidence retained in this file. |
| `reports/2026-11-03-b12069-noprefetch-build.json` | Sanitized evidence receipt for 2026 11 03 b12069 noprefetch build; exact measurements and scope retained. |
| `reports/2026-11-03-flash-next-q2-pack.json` | Sanitized evidence receipt for 2026 11 03 flash next q2 pack; exact measurements and scope retained. |
| `reports/2026-11-03-reprefill-audit.json` | Sanitized evidence receipt for 2026 11 03 reprefill audit; exact measurements and scope retained. |
| `reports/2026-11-09-b12069-prefetch-controls.json` | Sanitized evidence receipt for 2026 11 09 b12069 prefetch controls; exact measurements and scope retained. |
| `reports/2026-11-09-flash-paging-observation.json` | Sanitized evidence receipt for 2026 11 09 flash paging observation; exact measurements and scope retained. |
| `reports/2026-11-09-flash-q2-gpu-restart.md` | Standalone incident record: exact active model/parameters, dump and telemetry chronology, checker correction, unscored observations and unresolved cause. |
| `reports/2026-11-09-flash-q2-static-qualification.json` | Sanitized evidence receipt for 2026 11 09 flash q2 static qualification; exact measurements and scope retained. |
| `reports/2026-11-09-flash-q2-system-interruption.json` | Sanitized evidence receipt for 2026 11 09 flash q2 system interruption; exact measurements and scope retained. |
| `reports/2026-11-09-flint-native-private72k.json` | Sanitized evidence receipt for 2026 11 09 flint native private72k; exact measurements and scope retained. |
| `reports/2026-11-09-flint-native-rollback-observation.json` | Sanitized evidence receipt for 2026 11 09 flint native rollback observation; exact measurements and scope retained. |
| `reports/2026-11-09-flint-paging-observation.json` | Sanitized evidence receipt for 2026 11 09 flint paging observation; exact measurements and scope retained. |
| `reports/2026-11-09-flint-prefill-controls.json` | Sanitized evidence receipt for 2026 11 09 flint prefill controls; exact measurements and scope retained. |
| `reports/2026-11-09-flint-q3xl-private72k.json` | Sanitized evidence receipt for 2026 11 09 flint q3xl private72k; exact measurements and scope retained. |
| `reports/2026-11-09-installer-archive-retirement.json` | Sanitized evidence receipt for 2026 11 09 installer archive retirement; exact measurements and scope retained. |
| `research/reviews/2026-11-09-fusion-and-speed.md` | Critique token-fusion math, review article claims and connect performance measurements to pinned source mechanisms. |
| `tests/test_hardware_events.py` | Regression tests for real bugcheck event shapes without WHEA, normal-event exclusions, malformed inventories and query failure. |
| `tests/test_idle.py` | Use a compliant RAM floor in the existing idle lifecycle test. |
| `tests/test_lab.py` | Verify stop-floor refusal and upstream/local filename URL construction, including publisher subdirectories. |
| `tests/test_strata_guard.py` | Cover missing, exited and replacement native identities. |

<!-- 2026-11-09-change-inventory:end -->

The earlier tables below are historical inventories, not current candidate
status. Raw private instructions, answers, article pastes, binaries, models
and local controllers remain outside the public file list.

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
| `benchmarks/rubrics/router-v1.md` | Source-review criteria, excluded from model inputs |
| `catalog/models.json` | Pinned publisher identity, exact size and integrity metadata |
| `catalog/runtime.json` | Pinned publisher identity, exact size and integrity metadata |
| `docs/editors.md` | User/developer guide, decisions, task or session log |
| `docs/coding-use-cases.md` | Task-specific capabilities, observed code defects and limits of these small evaluations |
| `docs/memory-and-context.md` | User/developer guide, decisions, task or session log |
| `docs/methodology.md` | User/developer guide, decisions, task or session log |
| `docs/models.md` | User/developer guide, decisions, task or session log |
| `docs/next-experiments.md` | User/developer guide, decisions, task or session log |
| `docs/prompts.md` | User/developer guide, decisions, task or session log |
| `docs/repository-creation.md` | User/developer guide, decisions, task or session log |
| `docs/setup.md` | User/developer guide, decisions, task or session log |
| `docs/tasks.md` | User/developer guide, decisions, task or session log |
| `docs/tasks/README.md` | Index of forwardable task reports |
| `docs/tasks/2026-10-15-autonomous-model-campaign/owner-request.txt` | Relevant campaign requests and continuing constraints, excluding credentials |
| `docs/tasks/2026-10-15-autonomous-model-campaign/2026-10-15-model-comparison-and-editor-validation-v0.3.9.md` | One forwardable campaign report; measured selection, actual editor probes and quality limits |
| `profiles/qwen36-instructions-64k.json` | Selected working profile, native reasoning and explicit output/context budget |
| `reports/2026-10-15-finalist-results.json` | Reviewed repeated/held-out/long-history results for both finalist profiles |
| `reports/2026-10-15-selection.json` | Sanitized production selection, API and measured cache/memory evidence |
| `reports/2026-10-15-editor-results.json` | Six real editor probes, whole-prompt/server timing and source/history defects |
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
| `benchmarks/checks/router_v1.py` | Six Codex-authored independent contract groups, added after collection and excluded from model inputs |
| `reports/2026-10-15-qwen-precision-results.json` | Reviewed matched Q4/Q5 numeric results, exact model identities, timing/resource scope and grading caveats |
| `reports/2026-10-15-cache-results.json` | Five measured cache/batch/placement options, history/code checks, memory margins and unloaded rejection |
| `reports/2026-10-15-private-results.json` | Reviewed instruction-audit aggregates, exact artifacts/profiles and separate source/citation/code scores; excludes private text |
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
- `profiles/qwen36-cache2048-batch512-candidate.json`: untested daily-use
  candidate after the 3072 MiB probe left a narrow VRAM margin; requires exact
  profile code, history, actual-instruction and editor validation.
- `profiles/qwen36-historical34-64k-recheck.json`: fresh historical-placement
  proposal to compare instruction quality before selecting a faster profile.
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
- `profiles/kimi-linear-q8k-f16v-campaign.json`: separate compatibility retry
  after the original q8-value cache fails its dimension check; no result implied.
- `profiles/kimi-linear-f16-campaign.json`: matching f16 K/V retry after the
  architecture rejects differing cache types; preserve both prior load failures.

New raw run data, private instruction grading inputs and exact weight-deletion
records remain ignored. Reviewed findings are published in
`reports/2026-10-15-campaign.md`; capacity exclusions are in `research/reviews/`.
