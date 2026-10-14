# What to try next

This is a gated test sequence, not a promised winner. All proposed profiles are
marked untested. The repository task performs no new model load or deletion.

| Step | Change / question | Evidence needed to continue |
|---|---|---|
| 0 | Check live free memory, GPU use and prior stop reason | Stable headroom above the profile preload gate; preserve apps and accepted clock settings |
| 1 | If it fits, Qwen reference then `--gpu-layers all --cpu-moe` only | Loader buffers, total/process memory, short prefill/decode, 3-file tool result; same sampling/context/batch/cache settings |
| 2 | Gemma 4 26B QAT at 32K | Exact SHA, tokenizer/load pass, native thinking actually active, JSON tool arguments survive three tool rounds, no memory stop |
| 3 | Public router-v1 tools + inline diagnostics | Source-correct answers, missing-fact honesty, behavioral validation in isolation, whole-prompt <=1200s |
| 4 | GLM UD-Q4_K_XL at 32K if headroom allows | Verify template, actual MLA/KV/compute buffers and q8 vs f16 behavior; check repeated/slashed output |
| 5 | Finalists on long-history and stale-file tasks | Add frozen multi-turn fixture before running; facts at beginning/middle/end, file edit and re-read, controlled truncation |
| 6 | Three repeats plus held-out language/task and actual VS Code | Consistent quality, no invented reads/tests, acceptable total latency and measured headroom |

**When memory is tight, start at step 2 instead of forcing step 1.** The proposed
Qwen placement profile requires 23 GiB free RAM because more experts move to
CPU. That threshold is provisional. The current 20.5 GiB reference gate cannot
prove the alternative fits. There is no point adding a 1.5 GiB host prompt cache
to a profile already stopped for memory pressure.

For Gemma, first use the fixed Google revision already pinned in the catalog.
If a tokenizer/template failure reproduces, retain the evidence and pin the
ggml-org alternative separately. Do not silently patch a template and present
the result as stock-model behavior. Try 64K only after 32K's allocations and
recall are measured, including desktop usage.

After a stable placement is chosen, compare Qwen's 512/2048/unrestricted
reasoning ceilings with the same profile, seed, prompt and deadline. Then
compare temperature 0.6 against the research's proposed 0.35, holding min-p
fixed initially. Current 7/7 code evidence is insufficient to set a global
2048 ceiling or claim unrestricted reasoning is worse.

All-RAM KV and a small 512 MiB GPU expert cache come later, one at a time,
with RAM/VRAM headroom. Record prefill as well as decode: a faster generator
can still finish a file-heavy request later. GPU expert caching retains the
CPU weight copies. Dense Gemma 31B needs a short latency gate before a full
audit. Qwen Q5 requires a larger memory envelope and a matched Q4 comparison.

## Promotion rules

No interrupted/truncated run receives a quality score. Require correct absence
handling and source accounting, verified mutable-object isolation, and actual
editor tool completion. Prefer sustained >=3 GiB free RAM and >=600 MiB free
VRAM during evaluation, beyond the emergency 2.5 GiB/400 MiB stop floors.
Do not erase a failed measurement or claim safety from one successful run.

A challenger replaces the reference only after repeatable improvement on the
same evaluation and an acceptable held-out result within the deadline. Preserve
the old report/settings before any explicitly selected weight deletion. If the
models tie within evaluation noise, prefer the configuration with more measured
headroom and more reliable file/tool behavior, not the largest parameter label.
