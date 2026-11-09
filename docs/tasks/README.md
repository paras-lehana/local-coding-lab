# Task reports

Each task folder retains the owner's relevant request text and one forwardable
report. Raw benchmark answers, private sources and editor logs stay outside Git.
Detailed reusable experiment evidence remains in the repository's `reports/`.

| Date | Task | Status | Report |
|---|---|---|---|
|2026-11-09|Qwen3.5-9B Q4/Q5 preparation|No inference; E: relocation and qualification pending|[Model record](2026-11-09-qwen35-9b/2026-11-09-qwen35-9b-v0.11.0.md)|
|2026-11-09|Dory1.0-4B preparation|No inference; supported runtime and artifact verification pending|[Model record](2026-11-09-dory4b/2026-11-09-dory4b-v0.11.0.md)|
|2026-11-09|Merged Claude work, all models and article-driven experiments|Partial: native Flint31/36,15 performance controls; Flash GPU restart recorded unscored|[Merged report](2026-11-09-merged-research/2026-11-09-merged-models-articles-and-experiments-v0.11.0.md)|
|2026-11-03|All historical models and configuration combinations|Historical inventory; read9Novaddendum for current state|[Complete matrix](2026-11-03-master-summary/2026-11-03-all-models-and-combinations-v1.0.md)|
|2026-11-09|gemma4-31b historical standalone record|Documentation reconciliation; no new inference|[Model record](2026-11-09-gemma4-31b/2026-11-09-gemma4-31b-v0.11.0.md)|
|2026-11-09|glm47-flash historical standalone record|Documentation reconciliation; no new inference|[Model record](2026-11-09-glm47-flash/2026-11-09-glm47-flash-v0.11.0.md)|
|2026-11-09|kimi-linear-48b historical standalone record|Documentation reconciliation; no new inference|[Model record](2026-11-09-kimi-linear-48b/2026-11-09-kimi-linear-48b-v0.11.0.md)|
|2026-11-09|nemotron35-bolt historical standalone record|Documentation reconciliation; no new inference|[Model record](2026-11-09-nemotron35-bolt/2026-11-09-nemotron35-bolt-v0.11.0.md)|
|2026-11-09|qwen3-coder30 historical standalone record|Documentation reconciliation; no new inference|[Model record](2026-11-09-qwen3-coder30/2026-11-09-qwen3-coder30-v0.11.0.md)|
|2026-11-09|qwen3-coder-next80 historical standalone record|Documentation reconciliation; no new inference|[Model record](2026-11-09-qwen3-coder-next80/2026-11-09-qwen3-coder-next80-v0.11.0.md)|
|2026-11-09|qwen3-next80-instruct historical standalone record|Documentation reconciliation; no new inference|[Model record](2026-11-09-qwen3-next80-instruct/2026-11-09-qwen3-next80-instruct-v0.11.0.md)|
|2026-11-03|Groot-19B-A3B-261023 Q4_K_M apps-open trial|Capacity-limited apps-open; no quality score. Uncapped and 3.31 GiB-capped runs both RAM-guard stopped in the first router workflow (capped: 6.07/2.33 tok/s prefill/decode); reduced-residency profile prepared, no new inference|[Groot model record](2026-11-03-groot/2026-11-03-groot-19b-a3b-apps-open-v1.0.md)|
|2026-10-26|Flash-Next article-driven quant/engine review|Active; newQ2 pins, separate engine staging, no new quality score|[Flash-Next model record](2026-10-26-flash-next/2026-10-26-flash-next-v0.10.0.md)|
|2026-10-26|Dense Qwen3.8 article-driven learning|Research complete for supplied articles; new engine/model trials pending|[Dense27B model record](2026-10-26-qwen38-dense/2026-10-26-qwen38-dense-v0.10.0.md)|
|2026-10-24|Higher Flint precision, tuning research and missing coverage|Active; frozen old failures retained, capacity checks and new trials underway|[Precision and coverage](2026-10-24-precision-and-gaps/2026-10-24-precision-and-coverage-v0.9.0.md)|
|2026-10-24|Qwen3.6 precision and missing suites|NativeQ4 all12 attempted; IQ3/IQ4 components recorded; plainQ6 two router deadlines and retired; remaining controls active; 20-21 Oct Claude attempts added 3 Nov|[Qwen model record](2026-10-24-qwen-coverage/2026-10-24-qwen36-v0.9.0.md)|
|2026-10-24|Gemma26 QAT missing coverage|CPU26 public57/60/private23/36; separate26October CPU28/resident6 extended coding10/12, all answers complete; extra TTL/pool defects|[Gemma model record](2026-10-24-gemma26-coverage/2026-10-24-gemma26-v0.9.0.md)|
|2026-10-24|IFM K2 Horizon MoVA qualification|Installed; guarded load and quality checks pending|[K2 model record](2026-10-24-k2-mova/2026-10-24-k2-mova-v0.9.0.md)|
|2026-10-23/24|Recursive Flint and Claude campaign reconciliation|Complete with limits: private29/36, router39/40, coding11 completed passes/12, separate history8/8; keep Qwen; 3 Nov: Q3_K_XL run C graded in the extended cohort (router 38/40 at 1024 cap, 37/40 at 8192 cap; native 32K unscored)|[Flint evidence](2026-10-23-flint/2026-10-23-recursive-flint-v0.8.0.md)|
|2026-10-20|LFM2.5-24B-A2B QAD Q4_0 (Claude campaign, audited 3 Nov)|Retired. Public 48/60; private deadline loop with no repetition penalty; coding 6 completed passes of 12|[LFM2.5 model record](2026-10-20-lfm25/2026-10-20-lfm25-24b-a2b-qad-q4-v0.10.0.md)|
|2026-10-20|Ternary Bonsai 2 27B PQ2_0/PTQ1_0 (Claude campaign, audited 3 Nov)|Retired, unscored. PQ2 manual stop at 2.3-2.7 tok/s; PTQ1 router deadline|[Bonsai 2 model record](2026-10-20-bonsai2/2026-10-20-ternary-bonsai2-27b-pq2-ptq1-v0.10.0.md)|
|2026-10-19|azllm/TurboQuant article and10GB adaptation|Six probes measured; coding interrupted by restart; further inference withheld after hardware event|[Analysis and measurements](2026-10-19-azllm/2026-10-19-azllm-and-turboquant-v0.7.0.md)|
|2026-10-18|Strata on10GB and same-weight comparison|Complete with limits: faster32K Qwen, Flash coding deadlines/empty history; keep llama128K; 21 Oct Windows file-arena/expert-pack section added 3 Nov|[Strata measurements and limits](2026-10-18-strata/2026-10-18-strata-on-10gb-v0.6.0.md)|
| 2026-10-17 | Idle unloading, resource widget and AutoHotkey | Lifecycle/UI tests pass;30minute production timer; Copilot latency remains unresolved | [Measured desktop control report](2026-10-17-idle-widget/2026-10-17-idle-widget-v0.5.0.md) |
| 2026-10-17 | 128K context and remaining tool pressure | Engine source test completed; owner's greeting slow;70K canceled/unscored | [Context and tool-budget repair](2026-10-17-context128-and-tool-budget/2026-10-17-context128-and-tool-budget-v0.4.2.md) |
| 2026-10-17 | Copilot no-response and persistent autonomy defaults | Defaults configured; context mitigation applied; fresh UI test deferred by owner | [Context and default settings](2026-10-17-copilot-context-defaults/2026-10-17-copilot-context-and-defaults-v0.4.1.md) |
| 2026-10-17 | All models, Gemini reread and Qwen availability | Inventory complete; persistent API restored; current editor UI not rerun | [Complete inventory and assessment](2026-10-17-complete-model-inventory/2026-10-17-all-models-gemini-and-availability-v0.4.1.md) |
| 2026-10-16 | RAM, growing context and remaining candidates | All five research points complete; retain Q4, limitations recorded | [Expanded experiments](2026-10-16-memory-and-candidate-expansion/2026-10-16-memory-context-and-expanded-model-tests-v0.4.0.md) |
| 2026-10-15 | Autonomous model comparison and restart recovery | Campaign and editor probes reviewed; quality limits remain | [Campaign and practical recommendation](2026-10-15-autonomous-model-campaign/2026-10-15-model-comparison-and-editor-validation-v0.3.9.md) |
