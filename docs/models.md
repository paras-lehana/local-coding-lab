# Model shortlist and exact artifacts

Checked 15 October 2026. Sizes are GiB of **weights**, not total memory.
Download keys resolve to full pinned revisions and SHA256 in
[catalog/models.json](../catalog/models.json). The [live campaign report](../reports/2026-10-15-campaign.md)
separates completed measurements, downloads and conditional exclusions.

| Order / role | Download key | Weight GiB | Status and rationale |
|---|---|---:|---|
| Measured reference | `qwen36-q4` | 20.614 | Best completed local workflow reference; instruction/citation and aliasing errors remain |
| Smaller candidate | `gemma4-26b-qat` | 13.448 | Python and 52K-input history pass; unrestricted SQL 6/6 and TS 5/6; capped and native private audits both 19/36 |
| Distinct reasoning family | `glm47-udq4` | 16.317 | Capped private audit 21/36; f16 native Python 6/6 but history count fails; native f16 private 27/36 |
| Matched precision comparison | `glm47-q5` | 19.939 | Bounded Python 5/6, 0/6, 0/6; native 6/6, 6/6, 0/6; private retry 21/36; exact weight retired with reports retained |
| Dense conditional gate | `gemma4-31b-qat` | 16.439 | RAM-KV calibration 0.95 tok/s, deadline; weight file retired after preservation |
| Non-thinking coding control | `qwencoder30-udq4` | 16.452 | Python 2/6, 3/6, 1/6; private deadline, unscored; exact weight retired with reports retained |
| Conditional precision | `qwen36-q5` | 24.639 | Matched public Python repeats 6/6; native private 28/36, including only 2/6 code groups and accurate 14-source inventory; no repeatable precision advantage established |
| Optional precision | `qwen36-q6` | 29.657 | Header inspected after RAM briefly recovered to 28.76 GiB; conditional 32K profile requires 28.5 GiB / 7000 MiB fresh headroom and verified download |
| Conditional precision | `glm47-udq6` | 24.378 | Public capped Python 5/6, 0/6, 6/6; native 5/6; history count fails; native private 24/36 |
| Linear-attention alternative | `kimi-linear-q4` | 27.997 | Full pinned size/SHA verified; q8V and mixed K/V fail runtime checks; matching f16 loads, public suite running with one malformed tool call |
| Larger coding model | `qwencoder-next-q4` | 45.196 | Current apps-open resident-capacity exclusion, no quality score |

Model and artifact sources:

- [Qwen3.6 official model](https://huggingface.co/Qwen/Qwen3.6-35B-A3B),
  [pinned Q4 files](https://huggingface.co/unsloth/Qwen3.6-35B-A3B-GGUF/tree/a483e9e6cbd595906af30beda3187c2663a1118c).
- [Gemma 4 official model](https://huggingface.co/google/gemma-4-26B-A4B-it),
  [pinned Google QAT files](https://huggingface.co/google/gemma-4-26B-A4B-it-qat-q4_0-gguf/tree/d1c082be9cf3c8a514acf63b8761f4b41935842e).
- [GLM-4.7-Flash official model](https://huggingface.co/zai-org/GLM-4.7-Flash),
  [pinned quantized files](https://huggingface.co/unsloth/GLM-4.7-Flash-GGUF/tree/0d32489ecb9db6d2a4fc93bd27ef01519f95474d).
- [Qwen3-Coder 30B official model](https://huggingface.co/Qwen/Qwen3-Coder-30B-A3B-Instruct),
  [pinned coding-control files](https://huggingface.co/unsloth/Qwen3-Coder-30B-A3B-Instruct-GGUF/tree/b17cb02dd882d5b6ab62fc777ad2995f19668350).
- [Kimi Linear official model](https://huggingface.co/moonshotai/Kimi-Linear-48B-A3B-Instruct),
  [pinned Q4 files](https://huggingface.co/bartowski/moonshotai_Kimi-Linear-48B-A3B-Instruct-GGUF/tree/228dbe476e5a02091624a19068f4c962caa8a1c5).
- [Pinned Windows llama.cpp build](https://github.com/ggml-org/llama.cpp/releases/tag/b11562).

The Google Gemma revision above is the revision reported working after the
publisher's July malformed-GGUF fix. That improves provenance; it does not
replace a local tokenizer/load/tool test. A
[ggml-org QAT alternative](https://huggingface.co/ggml-org/gemma-4-26B-A4B-it-GGUF)
is a fallback to pin and verify if needed, not an automatic silent substitution.

Qwen3-Coder-30B-A3B is **MoE and non-thinking**, not dense. It is a useful possible
code-edit baseline, but has no native thinking mode to set to ultra/high.
Gemma 4 31B QAT failed its measured dense latency gate. Qwen Q5
can isolate weight precision more cleanly than changing families, but adds
roughly 4 GiB to the current Q4 artifact.

Kimi-Linear 48B and Qwen3-Coder-Next 80B require a larger free-memory envelope
than the recent apps-open snapshots. Mainline large Kimi, GLM, DeepSeek and
Llama releases must be evaluated by **total stored parameters/artifact size**;
a low active-parameter count does not make all weights fit. See the retained
research for wider candidates, but independently verify each exact artifact.

Do not compare vendor benchmark percentages as a local leaderboard: scaffolds,
precision, contexts and budgets differ. This table tracks **test roles and
progress**. The full local ranking remains unfinished.
