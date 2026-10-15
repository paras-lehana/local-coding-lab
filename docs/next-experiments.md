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

1. Public-suite grading and capped Gemma/GLM Q4 private grading are complete.
   Resume the interrupted GLM Q5 private audit as a new attempt after monitored
   recovery. Preserve its earlier partial output unscored. Qwen Coder's private
   attempt reached the deadline; its completed public results remain available.
2. Test feasible Qwen Q5 and GLM Q6 profiles with fresh memory and disk gates.
   Hold placement/context constant for precision claims, or explicitly label
   their differences. Reassess conditional capacity exclusions after unloading.
3. Complete the real frozen instruction-file audits and unrestricted finalist
   follow-ups. Gemma's 64K history/held-out tests are complete, but its capped
   private audit exposes invented reads and a different merge bug. Public
   fixtures alone cannot establish performance on the actual shared files.
4. Finish the outstanding Qwen placement, batch, 1536 MiB GPU expert-cache,
   CPU-KV and research-sampling
   experiments. The larger-batch attempt interrupted by Windows Update remains
   unscored. Dense Gemma's RAM-KV result does not substitute for Qwen's probe.
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
queued research bundle also changes min-p to 0.02; it cannot isolate either
sampling variable's effect. Current 7/7 code evidence is insufficient to set a global
2048 ceiling or claim unrestricted reasoning is worse.

All-RAM KV and a GPU expert cache come later, one at a time,
with RAM/VRAM headroom. Record prefill as well as decode: a faster generator
can still finish a file-heavy request later. GPU expert caching retains the
CPU weight copies. The queued cache probe uses 1536 MiB, replacing the initial
512 MiB suggestion. Dense Gemma 31B needs a short latency gate before a full
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
