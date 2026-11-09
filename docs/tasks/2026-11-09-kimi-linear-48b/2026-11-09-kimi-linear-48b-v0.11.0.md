# Kimi-Linear-48B-A3B: historical model record

Reconciled 9 November 2026 from Claude's configuration inventory and the linked
earlier reports. This is a documentation merge, not a new inference run.
Historical scores, deadlines, settings and interrupted cases are preserved.

| Assessment | Finding |
|---|---|
| Strengths observed / rationale | The f16-KV 32K profile completed public tasks, with a correct merge in one seed. This is a real load and inference result, not a wholly untested model. |
| Weaknesses / limits | Quantized KV combinations were rejected for the tested head dimension. Malformed tools, history counting and unsupported SQL occurred. The larger private profile failed its physical-memory admission. |
| Current decision | Retired. Private capacity rejection is not a private quality score. A new runtime must explicitly support the cache format before repeating the attempt. |

## Recorded configurations and outcomes

| ID | Date | Quant · engine · profile | Cohort | Status | Priv /36 | Public | Coding | Wall s | Notes | LB id | Source |
|---|---|---|---|---|---|---|---|---|---|---|---|
| KIM-1 | 10-15 | b11562 · 32K, 23 CPU-MoE blocks; q8 K/V rejected (head dim 72); q8 K + f16 V rejected; f16 K/V loaded | frozen | public old scale | – | old: core s73 4/6 (94.7 s), s74 malformed tool call (unscored), s75 6/6 (111.4 s); H count 242, fail; T 4/6 + S unsupported syntax (92.3 s) | – | 92-236 | 7.09 GiB VRAM | — (the LB row holds only the rejection) | CAMP (Kimi sections) |
| KIM-2 | 10-15 | 64K private | frozen | capacity-rejected (26.893 < 27.5 GiB) | – | – | – | – | – | h-kimi-linear-20261015 | CAMP |

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
| `kimi-linear-q4` | [bartowski/moonshotai_Kimi-Linear-48B-A3B-Instruct-GGUF](https://huggingface.co/bartowski/moonshotai_Kimi-Linear-48B-A3B-Instruct-GGUF/tree/228dbe476e5a02091624a19068f4c962caa8a1c5) / `228dbe476e5a02091624a19068f4c962caa8a1c5` | `moonshotai_Kimi-Linear-48B-A3B-Instruct-Q4_K_M.gguf` / 30061058720 | `a1a7d865370652221f937163f7e94c99e1f114861335ba4f8666606843f1620f` |

Runtime pins and launch profiles are in [the runtime catalog](../../../catalog/runtime.json) and [profiles](../../../profiles). Some older controls exist only in the cited raw receipts; no command is reconstructed from a partial label. License and missing template/hash fields must be checked at reproduction, not guessed from the model family.
