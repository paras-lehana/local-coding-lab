# Models: results, configurations and individual records

**9 November restart update:** Flash-Next Q2 / Strata 0.1.50's 64K
GPU-KV growth trial ended in a confirmed 0x116 NVIDIA timeout-recovery crash
at 10:10:57 IST. Its 8K/17K fact answers and allocation growth are observations;
the interrupted 33K case and unrun shrink/private audit have no score. The exact
configuration is quarantined, no engine is running, and production remains off.
See the [incident and configuration](../reports/2026-11-09-flash-q2-gpu-restart.md).
This records workload association, not a proven parameter-level cause.

Updated 9 November 2026. This table is a navigation and decision summary, not
a universal ranking. Exact pins are in [the catalog](../catalog/models.json),
commands in [profiles](../profiles), and every historical combination has a row
in [the configuration inventory](tasks/2026-11-03-master-summary/2026-11-03-all-models-and-combinations-v1.0.md).
The newer [merged review](tasks/2026-11-09-merged-research/2026-11-09-merged-models-articles-and-experiments-v0.11.0.md)
supersedes stale installation/queue status, without overwriting old measurements.

Private means the 36-point instruction/file audit. Public means the 60-point
workflow suite only where explicitly shown. No candidate has a complete,
compatible three-suite score. Separate profiles' best scores must not be combined.

9Nov latest: Flint Q3XL72K/cache256/resident1/cap1024 completes the private
audit in10,380.106s with25/36 (18/3/4). All15sources delivered; null handling,
mutable aliasing and rule/citation errors remain. It does not replace Qwen.
The [new receipt](../reports/2026-11-09-flint-q3xl-private72k.json) is extended,
not part of the1200second ranking. Fifteen performance-only controls now
complete safely; combined u128/cache1536/resident3 improves short prefill.
A native72K audit completes31/36 (19/6/6) on that tuned profile in6,386.703s;
all six isolated merge groups pass. Several controls differ, so this is not
a reasoning-only ablation. [Native receipt](../reports/2026-11-09-flint-native-private72k.json).
The separate full-SWA2K control improves middle-edit cache reuse but
changes outputs; it has not been enabled for the72K quality audit.

| Model / individual record | Quants and principal configurations actually tried | Strengths / measured results | Weaknesses / current take |
|---|---|---|---|
| [Qwen3-Next 80B Instruct](tasks/2026-11-09-qwen3-next80-instruct/2026-11-09-qwen3-next80-instruct-v0.11.0.md) | IQ3_M, llama.cpp, 28 then 10 GPU layers, 32K f16 KV | Original reply/tool smoke; some synthetic checks passed | Shared-GPU spill at 28 layers; hardware interruptions and interval/CSV defects. Retired; old scale |
| [Qwen3.6 35B-A3B](tasks/2026-10-24-qwen-coverage/2026-10-24-qwen36-v0.9.0.md) | Q4/Q5/Q6 XL/plain Q6/IQ3_S/IQ4_XS; mapped64 GPU q8 reference, separate production128K CPU q8; several CPU-expert/cache/cap variants | Reference Q4 private31/36, public52/60. Still the retained reference on instruction evidence | Exact reference coding missing. Different native Q4: 9 task passes, 2 failures, 1 output limit; JS edge defects. No higher-quant improvement established |
| [Qwen3-Coder 30B-A3B](tasks/2026-11-09-qwen3-coder30/2026-11-09-qwen3-coder30-v0.11.0.md) | UD-Q4_K_XL, b11562, public32K/CPU39/q8; private64K; non-thinking | Public workflows complete | Merge/history/SQL failures, private deadline. MoE, not dense; retired |
| [Qwen3-Coder-Next 80B](tasks/2026-11-09-qwen3-coder-next80/2026-11-09-qwen3-coder-next80-v0.11.0.md) | Q4_K_M, stock mmap failure then b11562 prefetch-opt-out64K | Python6/6; separate recovered history pass | Private tool limit, 15 failed reads, TS/SQL errors. Tested and retired, not skipped |
| [Qwen3.8 dense27B](tasks/2026-10-26-qwen38-dense/2026-10-26-qwen38-dense-v0.10.0.md) | Historical Q6 and Q8 partial offload; TQ3_4S via separate fork, draft controls | Legacy short boundary fix 16/16 and source question 5/5 at all three Q6 efforts; Q8 also passes. Six TQ probes measured 1.49–2.09 tok/s | Long coding incomplete/restart; short checks are a different scale. Q4/IQ4 unrun; proposed Q6 is the same historically tested artifact with new placement still pending. Higher effort did not improve already-perfect short scores |
| [Qwen3.8 Flash-Next](tasks/2026-10-26-flash-next/2026-10-26-flash-next-v0.10.0.md) | GSQ-RCO IQ3_XXS / Strata0.1.45, no-draft/MTP,32K and128K/int8 host KV; new Q2 on0.1.50/512cache/static32K with isolated frontend ACL fix | New Q2 greetings31.813/9.437s; RSS4GiB, dedicatedGPU5.243GiB. Earlier128K/32K-resident allocated1.55GiB hostKV; separate replays recovered6facts | Historical coding deadlines/empty history final remain. New Q2 has no quality score;64K native growth ended in0x116 during33K prefill; no score or shrink result. Lower precision and changed engine are distinct variables |
| [GLM-4.7-Flash](tasks/2026-11-09-glm47-flash/2026-11-09-glm47-flash-v0.11.0.md) | Q4 XL/Q5/Q6 XL; q8 versus f16 MLA KV; native/capped reasoning; 32K public/64K private | Q4/f16 private27/36 in942s, all15sources read | Higher quant not consistently better. Unread citations, TS and SQL data-loss defects; retired |
| [Gemma4 26B-A4B](tasks/2026-10-24-gemma26-coverage/2026-10-24-gemma26-v0.9.0.md) | QAT Q4_0; CPU28/26, resident4/6/8, GPUq8; separate128K history | Later public57/60; private23/36 on different sampler. Extended resident6 coding10/12, all12complete | Instruction ownership/citations weaker than reference; CSV/TS/TTL/worker defects.128K commit stop. Retired; scores not one composite |
| [Gemma4 dense31B](tasks/2026-11-09-gemma4-31b/2026-11-09-gemma4-31b-v0.11.0.md) | QAT Q4_0, mapped64K CPUq8, FFN/layer/GPU-KV placement controls | Private26/36; correct frozen Python behavior; history completion on smaller input | Private7234s; TS and SQL errors; some GPU placements stopped. Longer wait did not establish superiority; retired |
| [Kimi-Linear48B](tasks/2026-11-09-kimi-linear-48b/2026-11-09-kimi-linear-48b-v0.11.0.md) | Q4_K_M, b11562/CPU23/32K f16; q8 combinations unsupported; private64K rejected | Real public inference; one seed Python6/6 | Malformed tool/history/SQL problems; private memory gate. Do not describe the whole model as never run; retired |
| [Recursive Flint](tasks/2026-10-23-flint/2026-10-23-recursive-flint-v0.8.0.md) | IQ3_XXS/Q4_K_XL/Q3_K_XL; b11838, CPU/GPU KV, expert cache and resident caps;32/40/72K | IQ3 private29, router39; eleven completed coding passes. Q3XL history8/8; cap1024 router38/40 | CSV incomplete and TTL edge bug; higher quants have output/deadline/resource limits. Cap8192 took2.4x longer without demonstrated gain. Tuned native Q3XL private31/36 in6386.703s,6/6merge groups; new TS/SQL/coding still unrun |
| [LFM2.5 24B-A2B](tasks/2026-10-20-lfm25/2026-10-20-lfm25-24b-a2b-qad-q4-v0.10.0.md) | QAD Q4_0, b11669/CPU28/64Kq8, b512/u128; sampler differs by suite | Public48/60; six completed coding passes | Private reasoning loop and incomplete code cases; retired. QAD did not guarantee instruction reliability |
| [Bonsai2 dense27B](tasks/2026-10-20-bonsai2/2026-10-20-ternary-bonsai2-27b-pq2-ptq1-v0.10.0.md) | PQ2_0 partialGPU and PTQ1_0 fullGPU, Prism runtime | Very small ternary weights permit capacity exploration | PQ2 about2.3tok/s; PTQ1 router deadline despite fullGPU. No quality score; retired |
| [Groot19B-A3B](tasks/2026-11-03-groot/2026-11-03-groot-19b-a3b-apps-open-v1.0.md) | Q4_K_M, CPU36/64Kq8; uncapped then cache512/resident3.31/b128/u32 | Plain smoke4.813s; reduced total weights make it worth qualifying | Both router attempts RAM-stopped; no model-quality result. Installed; reduced-residency4GiB profile prepared but unrun; no assumption that every apps-open state fails |
| [K2 Horizon MoVA36B-A4B](tasks/2026-10-24-k2-mova/2026-10-24-k2-mova-v0.9.0.md) | Q4_K_M downloaded; CPU FFN and value-expert overrides prepared, not run | Potential sparse-attention candidate; identity pinned | Never loaded. Parked on C: by prior work; needs restored E: storage/full hash and admission. Not Moonshot Kimi K2 |
| [Nemotron3.5 Bolt74B-A9B](tasks/2026-11-09-nemotron35-bolt/2026-11-09-nemotron35-bolt-v0.11.0.md) | QAD low-bit22.018GB downloaded/verified; b11669/CPU88/64K plan | Candidate rationale only | Never loaded; file rotated for disk. No quality conclusion |

## Prepared or research-only candidates

| Candidate | Status / exact distinction | Why not counted as tested |
|---|---|---|
| [Qwen3.5-9B Q5/Q4](tasks/2026-11-09-qwen35-9b/2026-11-09-qwen35-9b-v0.11.0.md) | Claude staged both in a C: directory exposed by a junction; catalog pins exist. Partial-FFN/GPU-KV proposals plus a new Q4 GPU-layer/CPU-q8-KV64 alternative | No inference; new installs must stay E:. Full copy identity/admission before use; the new6500MiB VRAM gate is an estimate, not measured fit |
| [Dory1.0-4B Q5](tasks/2026-11-09-dory4b/2026-11-09-dory4b-v0.11.0.md) | C:-staged; looped architecture and boolean/efficient controls documented | Local full hash and compatible publisher runtime still required; ordinary b12069 support not established |
| Qwen3.5-0.8B Q8 draft | Installed811.84MB artifact; draft profiles proposed | No current full target/draft comparison or quality gain claim |
| Flint distilled NVFP4 | Pinned22.86GB artifact | Not downloaded; differs from generic Q4 and needs separate hardware/runtime validation |
| Ornith / Logics-SWE / ToolSpace | Claude's [3 Nov research leads](tasks/2026-11-03-deep-research/2026-11-03-deep-research-v1.0.md) | No local trials; vendor/community claims are not our results |
| Token-level fusion | Same-tokenizer, bounded-memory design proposal | No implementation or benchmark; cannot inherit members' scores |
| Earlier OpenRouter nine-model plan | Nine hosted identifiers, 144 planned evaluations | Historical HTTP403 IP-allowlist rejection; zero completed evaluations and zero recorded experiment spend. Owner set it aside; no new key use or cloud spending in this review |
| Large GLM/DeepSeek/Kimi/Llama alternatives | Historical scan and size/support exclusions in the master inventory | Not tested; model families are not permanently rejected by a dated capacity check |

## Thinking controls actually supported

A reasoning-token ceiling limits generation; it is not a trained effort level.
Template keywords, runtime controls and demonstrated answer quality are separate.

| Family / artifact | Native or inspected control | What was measured / limitation |
|---|---|---|
| Qwen3.6 / Groot | Boolean thinking and preserved thinking history; no native xhigh | Qwen settings were tested; Groot never finished its scored workflow |
| Dense Qwen3.8 / Flash-Next | low, medium, xhigh in the reviewed templates | Dense short effort probes exist; full coding comparison incomplete. Flash frontend `high` may alias xhigh; do not invent a distinct level |
| Bonsai2 PQ2 / PTQ1 | low, medium, xhigh, default xhigh; **high rejected** | Both archived server templates rechecked9Nov; SHA c3cf9e34… . Previous catalog medium/high/xhigh wording corrected. Only xhigh was run |
| Flint | Native reasoning plus engine token ceiling; no validated low/high scale | Router caps1024/8192 produced38/40 and37/40 in separate extended runs. Q3XL private cap1024 gives25/36 in2h53m; tuned native gives31/36 in1h46m with several controls changed. The cap can rearm per reasoning block, not a whole-workflow ceiling |
| LFM2.5 | Native thinking without an effort scale | Private reasoning loop reached deadline despite strong public components |
| Original Next80 Instruct / Coder30 / Coder-Next80 | Non-thinking checkpoints | An ultra/xhigh UI label cannot add a native reasoning mode |
| Qwen3.5-9B / Dory4B | Prepared boolean/template controls; Dory also has efficient prompt mode and loop count | No inference yet. Loops change runtime computation; they are not just a larger token budget. Exact marker/runtime checks precede claims |

The private benchmark intentionally serves frozen13October source snapshots,
not today's live instruction repository. That preserves a fair comparison.
Passing it would not certify every newer rule or real editor file delivery;
a separately versioned live-project follow-up is needed before promotion.

## Engine findings are separate from model quality

Strata's same-Qwen 32K comparison was faster but introduced a SQL failure.
The newer expert pack and NVML budget change still need a guarded model trial.
azllm's all-GPU headline was not reproduced by its separately tested CPU/GPU
route. New b12069 stock/default/opt-in tiny-model CPU/GPU controls pass all six
cases; this does not promote it over production b11562 or prove a speed gain.

The retained production setting is Qwen Q4,128K CPUq8 KV,1800-second idle sleep.
At 9 Nov recovery it is **off**: its18GiB RAM admission exceeds available RAM.
An endpoint configuration is not a running model. No fresh editor test is
claimed, and the owner's instruction against editor typing remains in force.

## Preserved 17 October shortlist

The original measured rows and artifact links are retained below as a dated
record. Installation and production statements there are historical; use the
9 November index above for current state.

<details>
<summary>Expand the earlier shortlist and measurements</summary>

# Model shortlist and exact artifacts

The [complete inventory](tasks/2026-10-17-complete-model-inventory/2026-10-17-all-models-gemini-and-availability-v0.4.1.md)
now covers14 attempted artifacts, all untested proposals/reasons, pros/cons and
the Gemini recommendation versus measured evidence. This table lists the11
portable campaign artifacts; the three historical entries below are separate.

Checked 17 October 2026. Sizes are GiB of **weights**, not total memory.
Download keys resolve to full pinned revisions and SHA256 in
[catalog/models.json](../catalog/models.json). The [live campaign report](../reports/2026-10-15-campaign.md)
separates completed measurements, downloads and conditional exclusions.

| Order / role | Download key | Weight GiB | Status and rationale |
|---|---|---:|---|
| Measured reference | `qwen36-q4` | 20.614 | Best completed local workflow reference; instruction/citation and aliasing errors remain |
| Smaller candidate | `gemma4-26b-qat` | 13.448 | Python and 52K-input history pass; unrestricted SQL 6/6 and TS 5/6; capped and native private audits both 19/36 |
| Distinct reasoning family | `glm47-udq4` | 16.317 | Capped private audit 21/36; f16 native Python 6/6 but history count fails; native f16 private 27/36 |
| Matched precision comparison | `glm47-q5` | 19.939 | Bounded Python 5/6, 0/6, 0/6; native 6/6, 6/6, 0/6; private retry 21/36; exact weight retired with reports retained |
| Dense extended trial | `gemma4-31b-qat` | 16.439 | Native public Python6/6, TS5/6, SQLite FK failure; private26/36 in2h00m34s; correct private merge but weaker instruction coverage; not promoted |
| Non-thinking coding control | `qwencoder30-udq4` | 16.452 | Python 2/6, 3/6, 1/6; private deadline, unscored; exact weight retired with reports retained |
| Conditional precision | `qwen36-q5` | 24.639 | Matched public Python repeats 6/6; native private 28/36, including only 2/6 code groups and accurate 14-source inventory; no repeatable precision advantage established |
| Matched precision trial | `qwen36-q6` | 29.657 | Reviewed Python6/6 three times; TS5/6, SQL FK failure; private28/36 in35m including mutable alias bug. Both history lengths pass, larger case54m57s with49s cached follow-up. Matched Q4 scores31/36 in11m40s and large history12m04s; retain Q4. |
| Conditional precision | `glm47-udq6` | 24.378 | Public capped Python 5/6, 0/6, 6/6; native 5/6; history count fails; native private 24/36 |
| Linear-attention alternative | `kimi-linear-q4` | 27.997 | Matching f16 public core4/6, malformed call/no code,6/6; TS4/6, SQL syntax failure;64K private gate rejected; exact weight retired with reports |
| Larger coding model | `qwencoder-next-q4` | 45.196 | Verified and loaded using an isolated prefetch opt-out: Python 6/6, TS 4/6, SQL foreign-key failure; recovered history passes all six facts; actual-instruction audit hits16-turn limit without a final answer in67m55s |

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
Gemma 4 31B QAT has now completed longer native-thinking tests: public Python6/6,
TS5/6, SQLite foreign-key failure and private26/36 in2h00m34s. Its private merge
helper passes6/6, but instruction coverage and read accounting remain weaker
than the working Qwen reference. Dense placement diagnostics remain separate
from that quality assessment. Qwen Q5
can isolate weight precision more cleanly than changing families, but adds
roughly 4 GiB to the current Q4 artifact.

Kimi-Linear's previous 64K private load was rejected by its resident-memory gate.
Coder-Next 80B now runs with file-backed paging, but input processing is slow
and one history attempt hit the physical-memory stop before a revised profile
completed it. Its stock Windows mmap load also failed before inference; the
successful runs use an explicitly identified modified runtime, not the stock
binary. See the [expanded evidence](tasks/2026-10-16-memory-and-candidate-expansion/2026-10-16-memory-context-and-expanded-model-tests-v0.4.0.md).
Mainline large Kimi, GLM, DeepSeek and
Llama releases must be evaluated by **total stored parameters/artifact size**;
a low active-parameter count does not make all weights fit. See the retained
research for wider candidates, but independently verify each exact artifact.

Do not compare vendor benchmark percentages as a local leaderboard: scaffolds,
precision, contexts and budgets differ. This table tracks **test roles and
progress**. For this owner's instruction priority, QwenQ4's34-expert profile is
the provisional working choice:31/36 private, successful52K history, but code
defects remain. The faster2GiB-cache version scores27/36 private and fails
held-out strict TypeScript. Gemma26QAT is retained as a lower-memory fallback.
GLMQ4/Q6 and QwenQ5 weights were retired after complete reviews, full SHA
verification and evidence preservation. The selected Qwen profile completed six
actual Copilot/Continue probes on 15 October; both editors missed Python-specific
instruction routing, and Copilot cited an unread report. No expanded candidate
has passed new editor validation or been promoted. None is certified for
unattended coding. See the campaign's selection rationale.


17October retention: Coder-Next80B, dense Gemma31 and QwenQ6 exact weights were retired after completed reviews and fresh full SHA verification. QwenQ4/Gemma26 remain. [Retirement receipt](../reports/2026-10-17-retirement.json).

Historical artifacts absent from the portable download catalog:

| Model | Evidence | Status |
|---|---|---|
| Qwen3-Next80B Instruct IQ3_M,34.128GiB | Eight post-reset answers: intervals94/105, TTL/LRU34/34, DAG64/64;18 completed outputs parsed across two batches. No completed file audit; effort fields did not activate reasoning. | Retired12October; distinct from Coder-Next80B. |
| Dense Qwen3.8-27B UD-Q6_K,20.474GiB | Short boundary/source checks passed; large audit cancelled after228.86min, unscored. | Retired; no practical long-file result. |
| Dense Qwen3.8-27B Q8_0,27.052GiB | Corrected short checks passed; long runs interrupted by reboot or lowVRAM. | Retired15October; no established Q8 advantage. |

See the [recovered numeric digest](../reports/2026-10-17-historical-inventory.json).
Do not merge their old fixture scores into the current36-point audit.
Current production configuration2.1 uses the37-CPU-expert mapped64K Q4 profile;
the old34-expert/non-mapped choice above is historical. New API verification is
recorded in the [availability receipt](../reports/2026-10-17-availability.json);
new editor UI validation remains separate.

</details>


### Historical 9 November pre-serving checkpoint (superseded above)

9November recovery checkpoint: all fifteen Flint performance controls now finish normally.
The resident3/6/3GiB comparison gives cold wall123.016/117.203/113.735s,
cached-repeat5.297/3.500/5.391s and changed-input90.719/84.312/83.907s.
Extra residency helps cached repeat, but cold/changed improvement is smaller
than baseline drift; retain3GiB for matched quality follow-ups. No quality
score follows from these short32-token controls. Native private31/36 remains.
Flash Q2's11artifacts pass fresh full hashes. Direct guarded native loading
reaches READY32768 and exits normally on stdin EOF in9.390s; no questions.
Two serving attempts stop fail-closed before requests with WinError5 at
OpenProcess in the working-set guard. All descendants are cleaned up, no
new hardware event. A source lead is frontend adopt_user_defaults using file
access bits in the process token default ACL; harmless reproduction pending.
Guard now preserves traceback/error.json without changing floors or cleanup.
52offline tests and6harmless lifecycle checks pass. Four Flash growth inputs
8178/17356/33788/8178tokens match the real pinned frontend encoder offline;
no growth inference. Production remains off; no model retired or promotion.
