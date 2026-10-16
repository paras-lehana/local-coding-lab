# What to try next

This is a gated test sequence, not a promised winner. The first Qwen placement
pair is [complete](../reports/2026-10-14-placement.md): the alternative improved
generation speed but supplied one broken test. It is locally load-tested, not
promoted into production. The [autonomous campaign](../reports/2026-10-15-campaign.md)
has since completed Qwen repeats/held-out checks and Gemma's seven-task 32K
suite, rejected the dense Gemma latency profile, and collected GLM Q4/Q5 and
Qwen Coder suites.
Exact retired weight files were deleted only after evidence preservation.

## Completed campaign and remaining quality limits

**16 October expansion is active.** Context allocation/recall measurements are
complete through about120K input tokens. Coder-Next80B completed public coding
and history checks after a stock mmap startup failure and an isolated prefetch
opt-out. Its private audit reached the tool-turn limit without a final answer;
it is not promoted. Dense Gemma31 now has isolated public Python6/6, TS5/6,
SQL foreign-key failure, passing10K history and private26/36 in2h00m34s. The frozen
dense CPU-KV layer-placement pair is complete: short generation improves,8K
latency does not. A GPU-KV follow-up stops during8K prefill below400MiB freeVRAM;
its completed2K latency is unchanged. No unchanged retry is queued. The matched
QwenQ4/Q6 pair follows with explicit six-hour whole-prompt limits.
Previous capacity/calibration exclusions
are historical, not completed quality verdicts. See the
[current task report](tasks/2026-10-16-memory-and-candidate-expansion/2026-10-16-memory-context-and-expanded-model-tests-v0.4.0.md).

1. Native private audits are graded: Qwen Q5 scores28/36, GLM Q4/f16 scores27/36,
   GLM Q6 scores24/36. Q5 GLM's recovered21/36 and retirement remain separate
   from the interrupted unscored attempt. No general precision advantage was
   established. Preserve completed evidence before retiring nonleaders.
2. Kimi's matching-f16 public suite is collected after two preserved cache-type
   compatibility failures. It has one malformed tool call, inconsistent Python,
   an incorrect history count and flawed held-out code. Isolated TS behavior is
   4/6 and SQL fails syntax;64K private loading was rejected at26.893<27.5GiB
   freeRAM. Optional Qwen Q6 was rejected at
   a fresh27.426GiB RAM snapshot below its28.5GiB gate; no download/quality score.
3. Quality first: the2GiB-cache profile scores27/36 in402.703s; historical
   placement replay scores31/36 in864.266s. The latter answer is byte-identical
   to its earlier result, confirming reproducibility rather than independent
   accuracy evidence. Its native repeated Python results are6/6,6/6,4/6;
   held-out TS5/6 and SQL foreign-key failure;52K-input history passes in448s.
   Cache contender repeats all pass Python6/6, but strict TypeScript fails and
   SQL fails FK;52K history passes365s. The instruction-priority historical
   placement is installed as the provisional working choice. Speed alone
   does not select the winner.
4. Cache1536/3072, batch512 and CPU-KV probes are complete. All independent
   Python groups/history facts pass, but generated tests contain errors. The
   3GiB cache improves coding latency while leaving only661MiB freeVRAM; its
   batch512 combination was rejected before load. Both finalists' repeated,
   held-out and larger-history tasks are complete and reviewed.
5. Production API and six actual Copilot/Continue UI probes are complete. Both
   editors read fresh files and retain an earlier marker, but miss Python-specific
   instruction routing. Copilot also cites an unread report in its follow-up.
   Read the editor report before interpreting integration as quality approval.
   Next useful work is an explicit source/range manifest before implementation,
   followed by a representative project patch with independent tests. That
   remediation is suggested, not already benchmarked or silently queued.

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
gain and longer mean time; its native actual-instruction audit scores28/36 with a2/6 merge implementation.

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

No candidate cleared every strict quality condition. The installed Qwen profile
is a supervised working compromise, not a certified quality promotion. Retained
QwenQ4/Gemma26 weights and all original evidence allow future comparisons.
Reopen capacity-rejected tests only when available memory or a validated loading
approach materially changes; do not repeat an unchanged failing load or close
the owner's apps. A process working-set maximum did not constrain the stock
Windows whole-file prefetch peak in the16October80B attempt.
