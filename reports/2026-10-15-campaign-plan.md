# Autonomous campaign: frozen scope and test policy

Owner request, 15 October 2026: autonomously download, test rigorously, report,
delete completed candidates as appropriate, and test every model in the research.
This supersedes the former blanket prohibition on deleting old model weights.
It does not cancel the apps-open condition, 20-minute prompt limit or resource
and hardware-error stop conditions. No repeated "continue" request is needed.

## Coverage

| Candidate / artifact | Required work |
|---|---|
| Qwen3.6 UD-Q4_K_M | Existing placement pair plus seeds 74/75, unrestricted thinking, long-file/stale-file and held-out language checks |
| Gemma 4 26B-A4B official QAT Q4_0 | Verified download, native template/tools, 32K profile and full feasible suite |
| GLM-4.7-Flash UD-Q4_K_XL | Verified download, MLA allocation/q8 behavior, 32K profile and full feasible suite |
| Qwen3-Coder 30B-A3B UD-Q4_K_XL | Non-thinking control, 32K profile and full feasible suite |
| Gemma 4 31B official QAT Q4_0 | Dense five-minute calibration; code suite if latency permits |
| Qwen3.6 UD-Q5_K_M | Capacity-aware precision trial; preserve placement for matched comparison when possible |
| Qwen3.6 UD-Q6_K_XL | Optional research precision variant: evaluate capacity, test if a guarded profile fits |
| GLM-4.7-Flash Q5_K_M | Capacity-aware precision trial; do not assume a non-UD prohibition without publisher evidence |
| GLM-4.7-Flash UD-Q6_K_XL | Optional research precision variant: evaluate capacity, test if a guarded profile fits |
| Kimi Linear 48B-A3B Q4_K_M | Pinned runtime includes kimi-linear; assess fit and real template/tool behavior |
| Qwen3-Coder Next 80B Q4_K_M | Document current capacity, attempt only if sufficient physical RAM/VRAM exists |
| Retired Qwen3.8 Q6/Q8 | Preserve existing measured timeout evidence; no claim of a fresh run |
| Research's excluded giant models | Account for exclusions separately; no invented performance scores or unnecessary enormous downloads |

Exact artifacts/revisions/bytes/hashes belong in catalog/models.json. Metadata
was rechecked against publisher APIs on 15 October. Existence in the catalog
means a candidate was identified, not that it loaded or passed a task.

## Collection and scoring

One inference process at a time. Downloading may overlap inference; this is an
apps-open practical campaign, not a quiet microbenchmark. Record that background
I/O and current memory can affect timings. Use existing b11562 unless an observed
compatibility failure justifies a separately pinned runtime experiment.

1. Load and verify health/alias. Save metadata, template capabilities and buffers.
2. Run a bounded smoke and inspect native reasoning/tool transport. Do not
   invent xhigh or copy model-family template kwargs blindly.
3. Collect router-v1 tools at seeds 73, 74 and 75 where the initial attempt is
   viable. Use temperature 0.6 and a 2048 per-request reasoning ceiling for the
   controlled first comparison. Also test native unrestricted thinking for
   thinking-capable candidates, subject to the same wall deadline and recorded
   total output cap. Non-thinking candidates are labeled, not penalized for an
   unsupported thinking control.
4. Collect context-v1: discover instructions through AGENTS and its router, read
   a long ledger with beginning/middle/end facts, then re-read a changed runtime
   file. The earlier ledger becomes temporarily unavailable on turn two. Check
   earlier facts, new zero-valued config, actual fresh read and absent-fact honesty.
5. Collect ts-sql-v1, frozen before any candidate answer: typed normalization,
   zero/false/default behavior, mutable isolation and a data-preserving SQLite
   migration with tenant-scoped uniqueness and surviving foreign keys.
6. Review returned code before isolated grading. Preserve model tests and
   implementation failures separately. Do not score incomplete/truncated output.

New case hashes: context-v1
8f1f7b1abf0393780b0d6f3e54136027647b79ab000bc5615c0c329c152cdbed;
ts-sql-v1 af8630ea22910674d17ebc43b6731e45b9ebacf19c2514f736b33fc7f0ec330e.
These scenarios have their own checks; do not merge their scores into the older
36-point private rubric or silently change router-v1's 40-point rubric.

The whole scenario deadline includes all phases and tool requests and is capped
at 1200 seconds. Core output caps and reasoning ceilings are explicit in each
manifest. A timeout rejects the tested configuration, not every possible profile
of the same model. Permit a documented smaller-context/batch/placement retry
when the first failure supplies evidence for that change; do not restart loops.

## Stops, retention and continuation

Keep free RAM >=2.5 GiB, free dedicated VRAM >=400 MiB and GPU core <84 C.
Record more conservative promotion margins (3 GiB/600 MiB). A new WHEA event
stops sustained inference for investigation. A routine capacity rejection moves
the campaign to another feasible candidate; it is not a quality score.

Keep the current verified Qwen Q4 baseline and any leading challenger. Before
deleting another completed model, preserve its hash, profile, results and exact
path in the local retention log. Delete only that file after checking it is
inside the intended model directory and is not loaded. Never delete directory
trees, private reports, editor settings or secrets. Keep all installation data
on E:. Do not close user applications or enable boot-time startup.

Each trial saves state before loading and after every task. An existing trial
directory is preserved; use a new attempt name after reviewing an interruption.
Finish every candidate with measured results or an explicit, evidenced blocking
condition. Continue the campaign autonomously rather than stopping at a plan.
