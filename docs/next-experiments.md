# What to try next

This is a gated test sequence, not a promised winner. The first Qwen placement
pair is [complete](../reports/2026-10-14-placement.md): the alternative improved
generation speed but supplied one broken test. It is locally load-tested, not
promoted into production. The [autonomous campaign](../reports/2026-10-15-campaign.md)
has since completed Qwen repeats/held-out checks and Gemma's seven-task 32K
suite, rejected the dense Gemma latency profile, and collected GLM Q4/Q5 and
Qwen Coder suites.
Exact retired weight files were deleted only after evidence preservation.

## Current remaining work

1. Complete the active GLM Q6 public suite and the queued native private audits
   for Qwen Q5, GLM Q4 f16 and GLM Q6, subject to fresh memory gates. GLM Q5's
   recovered audit scored21/36; its weight is retired with all answers retained.
   Its earlier interrupted attempt remains unscored.
2. Finish and verify Kimi's download, then test its actual fit and tools. The
   download began after an unloaded26.42GiB/7112MiB snapshot; that does not
   replace the fresh load check. Reassess optional Qwen Q6's28.5GiB RAM gate
   after unloading; do not invent a quality score for a capacity rejection.
3. Quality first: compare the proposed2GiB cache/batch512 Qwen profile with a
   fresh replay of the historical34-CPU-expert placement that scored31/36.
   The newer35-expert capped/native audits emit the same25/36 answer; removing
   a ceiling does not force more reasoning. Speed alone cannot select a winner.
4. Cache1536/3072, batch512 and CPU-KV probes are complete. All independent
   Python groups/history facts pass, but generated tests contain errors. The
   3GiB cache improves coding latency while leaving only661MiB freeVRAM; its
   batch512 combination was rejected before load. Run repeated core, held-out
   code and larger-history tasks on the exact selected profile.
5. Verify actual Copilot and Continue file/history flows before promotion and
   publish a ranking limited to the measured tasks and current apps-open memory.

## Original sequence and experiment controls

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
compare temperature 0.6 against the research's proposed 0.35. The currently
completed research bundle also changes min-p to 0.02; it cannot isolate either
sampling variable's effect. Current 7/7 code evidence is insufficient to set a global
2048 ceiling or claim unrestricted reasoning is worse.

All-RAM KV and a GPU expert cache come later, one at a time,
with RAM/VRAM headroom. Record prefill as well as decode: a faster generator
can still finish a file-heavy request later. GPU expert caching retains the
CPU weight copies. The first cache probe used1536MiB, replacing the initial
512MiB suggestion; its measured successor used3072MiB. Dense Gemma31 missed
the calibration latency gate. Qwen Q5's matched public core showed no behavior
gain and longer mean time; its actual-instruction audit remains pending.

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
