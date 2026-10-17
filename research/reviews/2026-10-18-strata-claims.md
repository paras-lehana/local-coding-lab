# Reviewing the supplied Strata article

Input: the owner's pasted “Is Strata Really 6x Faster Than llama.cpp? I Checked
the Numbers” article, attributed to Loengnavy, dated4October2026. The supplied
copy ends mid-sentence. Its SHA256 is
`29f8502a1bbb75516e1aad69eecc4bf1e91446a299a6fc2edbe4927596b25a72`.
The complete text remains private. This is an independent review, not a
republication or an endorsement of the article's benchmark numbers.

## Useful starting ideas

- Strata targets a particular mixture-of-experts workload. Keeping frequently
  used experts on the GPU while computing misses on the CPU can help a model
  that does not fit completely in VRAM. It is not a universal dense-model engine.
- Flash-Next's lookup embeddings and sparse attention make model-file size a
  poor estimate of the amount that must be copied into RAM at startup.
- Multi-token prediction can improve accepted output throughput when its
  proposals are useful. Measure accepted tokens and complete answers, not
  speculative proposals or a cherry-picked peak.
- CPU memory bandwidth, currently available RAM, GPU cache space and SSD
  traffic matter on this DDR4 workstation. Total installed64GB is not the
  same as64GB available to inference while everyday apps remain open.

## Corrections and limits

1. **12GB is not an enforced minimum in the pinned release.** The current
   [installation guide](https://github.com/Niko1221/Strata/blob/v0.1.45/docs/INSTALL.md)
   explicitly permits8GB with a speed caveat. Removing a VRAM check is not a
   necessary first step for this10GB card.
2. **The headline6x is not an engine-controlled comparison.** The supplied
   article itself contrasts different quantizations and an older baseline.
   Even its suggested lower ratio is not a measurement on our PC. Use identical
   weights, input, output limits and reasoning controls, and report load/prefill,
   first visible answer, decode, total completion and correctness separately.
3. **The engine paths differ.** Our existing Qwen3.6 is not Flash-Next. The
   pinned Qwen3.6 source keeps its attention KV in GPU fp32 and copies the full
   routed-expert arena into host memory. Flash-Next's RAM-budget/file-tier and
   KV-streaming controls cannot simply be transplanted into that path; ignored
   flags do not establish support. See the
   [Qwen3.6 implementation guide](https://github.com/Niko1221/Strata/blob/v0.1.45/docs/QWEN36.md).
4. **Selected sparse positions are not necessarily the last48 tokens.** A
   sparse-attention selection count does not mean all earlier KV can be
   discarded. Recurrent state, allocated attention buffers and tokens actually
   retained must be measured separately. Neither a large setting nor RAM KV
   guarantees that an editor sends every instruction or the model follows it.
5. **Quantization labels do not certify code quality.** The article's coding
   scores are external claims, not our fixture results. “Coder IQ1_M” also
   denotes a pruned variant in Strata's catalog; it must not be ranked as if it
   were merely the same full model compressed to one bit. More weight precision
   cannot guarantee valid syntax, correct merge semantics or honest citations.
6. **Do not generalize hardware tuning advice.** This experiment changes no
   BIOS, memory clocks, GPU clocks or driver settings. Past unexpected restarts
   have not established a single hardware cause. No benchmark justifies
   silently changing those settings.

## Testable implications for this PC

Start with the unchanged installed Qwen3.6 Q4 artifact and MTP disabled. The
stock v0.1.45 loader rejected its absent optional MTP count before allocating
model memory; this is a compatibility failure, not evidence that10GB cannot
run Strata. A small source patch and geometry tests address that specific case.

Then evaluate the full Flash-Next IQ3_XXS separately, with an explicit host
resident budget and SSD-backed remainder. It is a different model from the
earlier dense Qwen3.8 candidate in the inventory. Its75.84GB download does not
fit available host RAM as a full expert arena; the bounded path is essential
while apps stay open. A failed fit, interrupted answer or incomplete download
must remain unscored. Do not replace the current Qwen until completed coding,
source-reference and conversation-history evidence supports the change.

Local measurements will be linked from the Strata experiment report. A reduced
budget on a10GB card can explore constraints but cannot certify actual8GB
hardware. No public upstream contribution is claimed by this review.
