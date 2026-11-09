# Qwen3-Coder-Next 80B: historical model record

Reconciled 9 November 2026 from Claude's configuration inventory and the linked
earlier reports. This is a documentation merge, not a new inference run.
Historical scores, deadlines, settings and interrupted cases are preserved.

| Assessment | Finding |
|---|---|
| Strengths observed / rationale | The mapped 64K follow-up did run this 80B candidate: frozen Python behavior passed and a separate recovery history completed. |
| Weaknesses / limits | Stock Windows mmap startup caused severe whole-file-prefetch pressure. The opt-out run still had TypeScript/SQL defects; private audit reached the tool-round limit after 4075 seconds and fifteen failed reads. |
| Current decision | Retired. It was not skipped. Keep the startup failure, modified-runtime success and separate history recovery distinct; no private/composite grade exists. |

## Recorded configurations and outcomes

| ID | Date | Quant · engine · profile | Cohort | Status | Priv /36 | Public | Coding | Wall s | Notes | LB id | Source |
|---|---|---|---|---|---|---|---|---|---|---|---|
| QCN-1 | 10-15 | stock b11562 | – | capacity-rejected (resident-weight arithmetic) | – | – | – | – | – | — | CAMP (capacity bound) |
| QCN-2 | 10-16 | stock mmap startup | – | capacity-rejected (0.115 GiB RAM, 0.125 GiB commit) | – | – | – | – | whole-file prefetch pressure; led to the prefetch opt-out (section 4.2) | — | RPT/2026-10-16-coder-next.json |
| QCN-3 | 10-16 | b11562-noprefetch, 64K; history recovery with 46 CPU blocks | frozen (21,600 s runner) | public old scale | – | old: Python 6/6 (793.8 s); T 4/6 + S FK (561.8 s); H attempt 1 RAM stop (383.4 s), recovery pass (1177.6 s) | – | 562-1178 | – | — | RPT/2026-10-16-coder-next.json; EXP section 2 |
| QCN-4 | 10-16 | private, temp 1.0 | frozen (21,600 s runner) | unscored (16-tool-round limit) | – | – | – | 4075.125 | 15 failed reads | h-codernext80-20261016 | RUNS/expansion-20261016-coder-next-recovery64/outcome.json |

Source keys and cohort definitions are in the
[master inventory](../2026-11-03-master-summary/2026-11-03-all-models-and-combinations-v1.0.md#how-to-read-this-document).
`RPT` means this repository's `reports/`; `CAMP` is
[the 15 October campaign](../../../reports/2026-10-15-campaign.md);
`PRIV` is [its private-results export](../../../reports/2026-10-15-private-results.json).
Old six-point router scales and extended/historical allowances do not become
new /60 results. Resource stops are unscored. Historical low stop floors are
evidence of what happened, not settings authorized for a new launch.

## Lessons for other machines

Capacity must include model tensors, cache, workspace and the desktop; on this
Windows host GPU allocations also consumed system commit. A larger GPU may
change throughput without fixing unread citations or code defects. Reproduce
the exact artifact, runtime, prompt, sampler and cohort before comparing scores.
See [all models](../../models.md), [article ledger](../../../articles.md) and
[reporting policy](../../model-reporting.md).

## Artifact identity

| Catalog key | Publisher / immutable revision | File / bytes | SHA256 |
|---|---|---|---|
| `qwencoder-next-q4` | [unsloth/Qwen3-Coder-Next-GGUF](https://huggingface.co/unsloth/Qwen3-Coder-Next-GGUF/tree/ce09c67b53bc8739eef83fe67b2f5d293c270632) / `ce09c67b53bc8739eef83fe67b2f5d293c270632` | `Qwen3-Coder-Next-Q4_K_M.gguf` / 48528320544 | `9e6032d2f3b50a60f17ce8bf5a1d85c71af9b53b89c7978020ae7c660f29b090` |

Runtime pins and launch profiles are in [the runtime catalog](../../../catalog/runtime.json) and [profiles](../../../profiles). Some older controls exist only in the cited raw receipts; no command is reconstructed from a partial label. License and missing template/hash fields must be checked at reproduction, not guessed from the model family.
