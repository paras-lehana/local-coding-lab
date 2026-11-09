# Nemotron 3.5 Bolt: historical model record

Reconciled 9 November 2026 from Claude's configuration inventory and the linked
earlier reports. This is a documentation merge, not a new inference run.
Historical scores, deadlines, settings and interrupted cases are preserved.

| Assessment | Finding |
|---|---|
| Strengths observed / rationale | Quantization-aware low-bit weights are a plausible capacity/quality lead; artifact identity and a compatible-runtime plan were preserved. |
| Weaknesses / limits | No local model load or answer exists. The verified file was deleted for disk space, not for poor model quality. The prepared 18 GiB RAM gate exceeds current recovery headroom. |
| Current decision | Not tested. Re-download requires disk and fresh RAM/commit/VRAM admission; do not assign a leaderboard score or call this a failed model. |

## Recorded configurations and outcomes

| ID | Date | Quant · engine · profile | Cohort | Status | Priv /36 | Public | Coding | Wall s | Notes | LB id | Source |
|---|---|---|---|---|---|---|---|---|---|---|---|
| NEM-1 | 10-24 | QAD low-bit (22,018,326,528 B) · b11669 planned · bolt-cpu88-coverage64 (18 GiB gate) | frozen | not run; file deleted 24 Oct 13:51 for disk space (not a quality decision) | – | – | – | – | – | nemotron-bolt-74b-not-run | RPT/2026-10-24-bolt-disk-rotation.json |

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
| `nemotron-bolt-74b-24gb` | [nvidia/NVIDIA-Nemotron-3.5-Bolt-74B-A9B-24GB-GGUF](https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Bolt-74B-A9B-24GB-GGUF/tree/e0fecb69cb3e5e4c5e8a056fa2aec98c78e91246) / `e0fecb69cb3e5e4c5e8a056fa2aec98c78e91246` | `NVIDIA-Nemotron-3.5-Bolt-74B-A9B-24GB.gguf` / 22018326528 | `91d63363e782c8a3d5f4be42816eba8e0d42dd2530bd07a7d0d2dc440599af75` |

Runtime pins and launch profiles are in [the runtime catalog](../../../catalog/runtime.json) and [profiles](../../../profiles). Some older controls exist only in the cited raw receipts; no command is reconstructed from a partial label. License and missing template/hash fields must be checked at reproduction, not guessed from the model family.
