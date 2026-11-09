# Qwen3-Next-80B-A3B-Instruct: historical model record

Reconciled 9 November 2026 from Claude's configuration inventory and the linked
earlier reports. This is a documentation merge, not a new inference run.
Historical scores, deadlines, settings and interrupted cases are preserved.

| Assessment | Finding |
|---|---|
| Strengths observed / rationale | The original IQ3_M installation returned a reply/tool call; some synthetic DAG and TTL checks passed before interruptions. |
| Weaknesses / limits | 28 GPU layers caused shared-memory spill. Later 10-layer testing was interrupted by 0x124 / 0x3B crashes; interval and CSV defects were also observed. Those facts do not prove 3-bit weights caused the crashes or every coding bug. |
| Current decision | Retired historical installation. Preserve the original synthetic scale; it cannot be converted into the later private/public/coding scorecard. |

## Recorded configurations and outcomes

| ID | Date | Quant · engine · profile | Cohort | Status | Priv /36 | Public | Coding | Wall s | Notes | LB id | Source |
|---|---|---|---|---|---|---|---|---|---|---|---|
| QN80-1 | 10-12 | llama.cpp (12 Oct install) · 28 GPU layers, 32K f16 KV | install smoke | capacity-rejected (12.4 GiB shared-GPU spill) | – | – | valid reply and tool call | 25.6 | – | — | INSTALL L10-14 |
| QN80-2 | 10-12 | 10 GPU layers; greedy, recommended (0.7/0.8/20) and self-reviewed samplings | 12 Oct synthetic suite | interrupted (0x124 and 0x3B crashes) | – | – | diff-scale: intervals 94/105, ttl 34/34, dag 64/64; CSV 104/120 before the restart | 48.7-90.0 per task | – | — | BEN/2026-10-12/quality-results-rescored.json; BEN/2026-10-12/model-setup-report.html |

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

Recovered 9 November from the original installation log, lines 2, 9 and 41:

- Quantizer: `bartowski/Qwen_Qwen3-Next-80B-A3B-Instruct-GGUF`.
- Revision: `c07b9268d97d8ba09d0529980627f3bd70f5f90a`.
- File: `Qwen_Qwen3-Next-80B-A3B-Instruct-IQ3_M.gguf`.
- Size: 36,643,914,208 bytes, about 34.128 GiB.
- SHA256: `77eee87b804626f0e66992d6cc009097ad5b3beb0c6c904dc23111e375eaf2cd`.
- Catalog key: `qwen-next80-iq3m-historical`. Verification was recorded on
  12 October; no file was downloaded or hashed again in this recovery.

The [publisher card](https://huggingface.co/Qwen/Qwen3-Next-80B-A3B-Instruct)
identifies Apache-2.0, a non-thinking-only Instruct checkpoint, and 262,144
native context. The configured 32K trial was not its native context maximum.
The old claim that this model has only 32K native context is incorrect.

The publisher's [configuration](https://huggingface.co/Qwen/Qwen3-Next-80B-A3B-Instruct/blob/main/config.json)
also shows48layers, full attention every fourth layer,2KV heads and256head
width. Ideal full-attention f16 KV at32K is approximately0.75GiB:
2 K/V arrays ×12layers ×2heads ×256 ×32768 ×2bytes. Recurrent state,
checkpoints and runtime workspaces add memory; this is not a total process
measurement. It nevertheless contradicts the earlier blanket16GiB claim.
This geometry is model-specific and must not be copied to a dense model.

## 9 November source corrections and fuller measurements

The historical row QN80-1's shorthand "capacity-rejected" is imprecise:
the original 28-layer run **did answer**, then was rejected as an operational
configuration because it spilled about 12.4 GiB into shared GPU memory and
left under 0.5 GiB available RAM. It was not a pre-load admission rejection or
a CUDA OOM. The 10-layer follow-up improved the same short coding smoke from
5.894 to 7.214 generated tokens/s (25.609 to 20.218 seconds). This is one small
smoke, not a general speed or quality benchmark. Preserve the old row above
and this more precise interpretation together.

The [recovered numeric digest](../../../reports/2026-10-17-historical-inventory.json)
records 18 completed Python outputs that parsed across two batches. Eight
post-VRAM-reset answers generated 6.79–7.87 tokens/s, median 7.08. Semantic
interval and CSV defects occurred despite valid syntax; this directly refutes
the blanket claim that the quantization inevitably loses brackets. It does
not prove equivalence to higher precision. No complete instruction audit exists.

Original runtime: b11562, commit `b2f036c0f`, CUDA 12.4. Final recorded settings:
10 GPU layers, 32,768 context, 12 threads, flash attention, one slot,
batch 512 / microbatch 128, mmap/no-repack, cache-RAM 0, fit off,
temperature 0.7, top-p 0.8, top-k 20, min-p 0, repetition penalty 1.
These historical controls are not a recommended current launch without guards.

Runtime pins and launch profiles are in [the runtime catalog](../../../catalog/runtime.json) and [profiles](../../../profiles). Some older controls exist only in the cited raw receipts; no command is reconstructed from a partial label. License and missing template/hash fields must be checked at reproduction, not guessed from the model family.
