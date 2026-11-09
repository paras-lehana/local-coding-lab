# Article ledger: claims, evidence and experiments

**Post-restart finding, 9 November:** article-driven Flash Q2 growth reached
0.23 / 0.33 / 0.52 GiB allocated GPU KV, but the 33K request was interrupted by
a confirmed GPU timeout-recovery crash. There is no qualified growth/trim or
coding result. [Configuration, evidence and limits](reports/2026-11-09-flash-q2-gpu-restart.md).

Updated 9 November 2026. This is the maintained index of the owner's supplied
research, not a collection of benchmark endorsements. Full third-party pastes
stay private. Links below lead to attributed reviews, primary sources and our
measurements. A published throughput number is never a local quality score.

Our target is correct coding grounded in `.github`, `.claude`, linked rules,
source files, documentation and changing chat history on a Windows RTX 3080
10 GB / Ryzen 7 5800X / 64 GB desktop **with applications open**. A plain `hi`
must finish within 600 seconds. Accurate file-heavy work may take longer;
extended results remain separate from the frozen 1200-second comparison.

## Supplied articles and reports

| ID / source | What it says | Our assessment / corrections | What we actually tried or found | Improvement / next decision |
|---|---|---|---|---|
| A01. [Gemini research](https://share.gemini.google/LadMuhd0ajY0), received 14 Oct; [preserved review](research/reviews/2026-10-14-gemini.md) | Retain Qwen as reference; try Gemma26QAT and GLM, q8 KV, attention/expert placement and prompt-cache changes | Its claimed8GiB prompt-cache problem contradicts the launcher's existing cache-ram0. Suggested speed figures were estimates, Gemma/Kimi block counts needed correction, and preserved thinking does not guarantee recall. GLM Q5 later loaded, contradicting a guaranteed-shutdown claim | The [complete matrix](docs/tasks/2026-11-03-master-summary/2026-11-03-all-models-and-combinations-v1.0.md) records the proposed families. Q4 private31 versus matched Q6XL28; Qwen CPU/GPU cache probes recovered facts near120K input but failed bare-JSON formatting. No universal winner | Keep compatible profiles separate; finish the exact reference profile's coding component. Test cache/placement changes separately, not the report's bundled speed promise |
| A02. “Is Strata Really 6x Faster Than llama.cpp? I Checked the Numbers”, Loengnavy, 4 Oct; [review](research/reviews/2026-10-18-strata-claims.md) | Investigate large Strata speed claims and their comparison conditions | Supplied paste ends mid-sentence. No hard 12 GB minimum in the pinned engine. Faster execution does not establish equivalent outputs or agent success | Same Qwen 32K workflows completed faster in single Strata runs, but SQL failed where the llama control passed. Flash-Next fit 10 GB with controls but had deadlines / an empty history answer | Test current Windows VRAM accounting and expert-pack loading; preserve exact engine identity and reject silent native restarts |
| A03. “An Inference Engine Nobody Has Heard Of, Runs Qwen 3.8–27B at 207tok/s on One RTX3090Ti, Full262k Context”, Andrew Zhu; received 19 Oct; [provenance](research/raw/2026-10-19-azllm/README.md) | azllm / TurboQuant and drafts provide high dense-model speed and large context | The all-GPU body alone requires about 11.35 GiB here. The 24 GB-card headline cannot be reproduced by calling a different partial-offload engine the same experiment | Six separate llama.cpp-tq3 probes achieved 1.49–2.09 tok/s; linked-file coding was interrupted by restart and remains unscored | Revisit only as a labelled dense capacity/quality experiment, with hardware checks and complete output; no 207 tok/s local claim |
| A04. “The Censorship Switch Strata Hid in Its Own Repo”, Andrew Zhu, 2 Oct; [seven-article review](research/reviews/2026-10-26-qwen-articles.md) | A projection marketed around speed changes refusal behavior and can bias comparisons | Output-distribution changes belong in a different experiment. Refusal has not been demonstrated as our main coding failure | Baseline plans explicitly disable projection and route-tail skipping; no projection quality trial | Keep off for correctness comparisons; do not credit changed answers as a pure engine speedup |
| A05. “Qwen3.8–27B with NVIDIA RTX 3090: Best Time To Be Alive”, Jatin Prasad, 15 Aug; [dense report](docs/tasks/2026-10-26-qwen38-dense/2026-10-26-qwen38-dense-v0.10.0.md) | Dense 27B offers strong coding with thinking controls and MTP on 24 GB | Plausible quality candidate; full-GPU performance does not transfer to 10 GB. Native effort is xhigh / medium / low, not an arbitrary ultra string | Historical Q6 and TQ3 are slow/incomplete; a Q4 candidate is metadata-pinned, not downloaded or scored. The later catalog Q6 is the same already-tested artifact, not a new revision | Q4 before repeating Q6, explicit native effort, plain greeting first; qualify accuracy before a larger-quant download |
| A06. “I Read Qwen’s 28-Page Report So You Don’t Have To: Why RAM Now Matters More”, Loengnavy; [review](research/reviews/2026-10-26-qwen-articles.md#flash-next-architecture-versus-the75gb-claim) | Flash-Next host/SSD n-gram lookups make large models feasible; cites roughly 75 GB combined capacity | PLE is model storage, not chat KV. The deployment guide recommends 96 GB headroom. Our nominal 74 GB does not mean 74 GB is available. Paper module speedups are not whole-agent speedups | Earlier IQ3_XXS fit with SSD/host placement; 128K/int8 cache allocated 1.55 GiB host KV, but the long workflow returned an empty final. New Q2 shards are verified and packed; static32K greetings now31.813/9.437s after an isolated frontend ACL correction | Static32K completed; dynamic GPU KV grew, but33K prefill ended in0x116. Preserve incomplete recall and shrink coverage. A `/slots` token counter alone cannot prove allocated cache growth |
| A07. “Qwen3.8–27B, 177 Tokens Per Second, One RTX 3090”, Andrew Zhu, 15 Sep; [review](research/reviews/2026-10-26-qwen-articles.md) | Patched vLLM / HyperQwen, drafting, KV formats and prefix reuse raise throughput | Current repository and article recipe differ. Single-user decode, concurrent throughput and cached-prefix rates are different measurements; 24 GB residency is material | Source and capacity review only; HyperQwen not run on this 3080 | Retain as a reference for compatible hardware; do not sacrifice target precision or silently substitute a modified checkpoint |
| A08. “Can the New King of Open Source — Qwen3.8–27B — Really Run in 3GB of VRAM?”, Gavin Li, 19 Aug; [review](research/reviews/2026-10-26-qwen-articles.md) | AirLLM streams BF16 layers with about 3.33 GB peak VRAM | Demonstrates a capacity technique, not instruction-heavy correctness or acceptable whole-task latency. Disk, transfers, cache and Windows support still need checking | Not installed/tested here; source/capacity assessment only. BF16 plus split storage is well beyond current free E: space | Consider only after disk budgeting and a bounded greeting; keep high-precision streaming separate from efficient resident inference |
| A09. “Qwen3.8-Flash-Next: Which Quant to Run From 16GB to 128GB in 2026”, Ankit Agrawal, 9 Oct; [Flash report](docs/tasks/2026-10-26-flash-next/2026-10-26-flash-next-v0.10.0.md) | GSQ-RCO / Unsloth quant tiers, Strata placement and memory-size recommendations | Prior lab Flash was already GSQ-RCO IQ3_XXS. Q2 is a capacity control, not a precision upgrade. Categorical platform/model restrictions were stale at review | Q2 transformer 37.624 GB plus common PLE shard 28.800 GB; full hashes verified 3 Nov, native-view pack built in 9.327 s. New Q2 static32K greetings complete; native64K growth interrupted at33K by0x116; 8K/17K answers preserved unscored, no coding score | Static qualification passed with1294MiB minimum free deviceVRAM; growth allocated0.23/0.33/0.52GiB before0x116; quarantine the profile, retain observations without a score |
| A10. “A 27B Model at 92 Tokens a Second on a 16 GB Gaming Card”, Micheal Bee, 10 Sep; [review](research/reviews/2026-10-26-qwen-articles.md) | Embedded MTP, batches and KV compression accelerate a 5070 Ti | Recipe uses a modified IQ3_S checkpoint and custom sm120 kernels; RTX 3080 is sm86. About 12.12 GB weights cannot be assumed to fit 10 GB | Repository / artifact review, no local reproduction | Only test after compatible kernels and capacity are established; record changed weights separately from inference flags |
| A11. [Three-model token fusion](https://levelup.gitconnected.com/i-fused-3-tiny-local-models-to-beat-single-model-limits-without-weight-merging-b17bba9c7e45), Nikhil Varma; shared 21 Oct; [detailed review](research/reviews/2026-11-09-fusion-and-speed.md) | Three Qwen2.5 7B specialists use entropy-gated weighted log probabilities; claims normalization fixes mismatched logit scales | Full historical article recovered and read9Nov. In this weighted product, log-softmax subtracts a vocabulary-constant term: final softmax/argmax is identical to weighted raw logits, so it does **not** fix cross-model scale. No task-result table supports the recipe | Analytical code review only, no ensemble inference. Three4-bit7B bodies need about10.5GB before overhead and three KV caches; actual free VRAM was about6.3GiB. The auxiliary loop has no explicit parallel dispatch | First verify tokenizer/template compatibility and a bounded tiny control; compare each member and fusion on fixed tasks, with catch-up time and aggregate memory. Do not download three7B models on the strength of the headline |
| A12. [Introducing Flint](https://recursive.com/updates/introducing-recursive-flint), Recursive, 18 Oct; [model report](docs/tasks/2026-10-23-flint/2026-10-23-recursive-flint-v0.8.0.md) | 40B total / 2.5B active model, strong coding, optimized local execution, large context | Vendor speed uses different hardware and stack; its agentic evaluation permits five hours. `rec` is an engine, Flint a model. Distilled NVFP4 differs from generic GGUF quantization | IQ3_XXS: private29/36, router39/40, eleven completed coding passes, CSV incomplete. Q3XL router caps1024/8192:38/40 vs37/40, 38 vs91minutes. Q3XL72K/cap1024 private25/36 in2h53m; tuned native31/36 in1h46m,6/6merge groups, all15sources. Instruction omissions remain; multiple controls changed | No higher-quant promotion. Measure useful placement/cache controls before remaining code cases; a cap is not a trained effort mode |
| A13. [Why Is My Local LLM So Slow? Half of It You Can Fix Tonight](https://medium.com/data-science-collective/why-is-my-local-llm-so-slow-half-of-it-you-can-fix-tonight-da7283a8adf6), Anubhav, 21 Sep; supplied9Nov | Separate prefill/decode; inspect placement/cache; increase microbatch; try speculation where beneficial | Useful measurements, overbroad prescriptions. Partial offload is intentional. Larger microbatches can exceed headroom or bypass a cache path. First visible text also waits for reasoning; bandwidth arithmetic is not a diagnosis | Fifteen Flint performance runs complete safely. Combined microbatch128/cache1536/resident3 cuts cold wall267.437→128.406s; microbatch4 slows it to514.454s. Larger cache alone improves decode but slows microbatch16 prefill; newer runtime gives no material gain. The matched2K full-SWA control reuses962tokens after a middle edit versus zero for windowed, costing46.484MiB more KV. [Measurements](reports/2026-11-09-flint-prefill-controls.json) | Native72K private audit completes31/36 in6386.703s after greetings57.907/37.672s. Residency3/6/3complete; cached repeats improve, cold gain remains inconclusive. Short output hashes differ; no numerical-equivalence claim. Full-SWA changes cache retention, not the trained attention window; short-context reuse does not qualify72K full-SWA capacity |
| A14. Earlier owner-pasted AI advice about weight quantization, RAM KV and CPU offload (conversation source, no article URL supplied) | Claims sub4-bit causes syntax errors, Q6 guarantees correct code, Coder30B is dense, and `--offload-kqv` puts KV in RAM | These are incorrect or unsupported absolutes. Coder30B-A3B is MoE; no quant guarantees correct code. In the inspected llama.cpp controls, `--no-kv-offload` selects CPU KV; enabling KQV offload is not a RAM-placement command. Native context is model-specific, not a fixed file count | CPUq8 KV and GPUq8 variants were actually measured; Q4/Q6 and IQ3 variants all had distinct reasoning/code failures. IQ3 also passed substantial checks. RAM/cache allocation and retained facts were tested separately | Use exact model metadata, effective command and delivered source bytes; inspect memory buffers and recall instead of inferring failure from a quant label or a fixed twenty-file rule |

## What the evidence changes for our setup

Additional primary-source corrections to A14, checked9November:

- Original Qwen3-Next80B Instruct declares262144positions, not a32K native
  limit. Its48layers use full attention every fourth layer, with2KV heads of
  width256. Ideal f16 full-attention KV at32K is therefore about0.75GiB
  (two K/V arrays ×12layers ×2heads ×256width ×32768tokens ×2bytes).
  This is architecture arithmetic, not a total-memory measurement: recurrent
  state, checkpoints, batches and runtime overhead remain additional. It
  disproves applying a blanket16GiB KV estimate to this checkpoint.
  [Official configuration](https://huggingface.co/Qwen/Qwen3-Next-80B-A3B-Instruct/blob/main/config.json).
- GLM-4.5-Air is106B total/12B active according to its publisher. Ideal4-bit
  weights alone are roughly53GB before overhead, so the pasted28GB Q4 plan
  is not a valid size budget. It is a different candidate from the tested
  GLM-4.7-Flash; this is not a new inference or permanent fit exclusion.
  [Official model card](https://huggingface.co/zai-org/GLM-4.5-Air).
- In the pinned llama.cpp default layer assignment, GPU placement starts at
  the later layers/output end, not the first28layers described in the pasted
  advice. Tensor/expert overrides then change placement further; ordinary
  partial offload is not automatically layer streaming every token.
  [Pinned loader source](https://github.com/ggml-org/llama.cpp/blob/e6192de0a62b73f566f825ecb531f7e4fe699eae/src/llama-model.cpp#L1602).

**9November08:25IST follow-up:** the tuned native Flint audit completes31/36
in6,386.703s versus the earlier capped25/36 in10,380.106s. Its delivered merge
passes6/6isolated groups; first visible answer arrives after5,995.230s.
All15sources are supplied, yet instruction-chain/adapter omissions remain.
This tests A12/A13's practical relevance but changes several settings together;
it does not prove a pure reasoning or quantization effect. See the
[new measurement](reports/2026-11-09-flint-native-private72k.json).
The table's earlier collecting checkpoints are superseded by this result.
The3/6/3GiB residency comparison now completes: cached repeats improve at6GiB, while cold/changed gains remain smaller than baseline drift.

The earlier AI advice also assigns fixed intelligence levels to active
parameter counts and quant labels. Our results do not support such rules.
MoE versus dense, weight precision, KV format, placement and trained reasoning
controls are separate variables. Neither Q6 nor a large context setting
guarantees syntax, correct logic, valid citations or reliable middle-of-file
recall. GPU layer count also cannot be interpreted without tensor/expert
placement: the measured all-layer-attention profiles keep routed experts on
CPU and an explicit GPU expert cache.

The owner's other9November attachment is Claude's4November handoff, not a
benchmark article. Its claims and merge decisions are tabulated in the
[merged report](docs/tasks/2026-11-09-merged-research/2026-11-09-merged-models-articles-and-experiments-v0.11.0.md#what-was-read-and-reconciled):
completed downloads/packing and code preparation are retained, while unrun
queues, low historical memory floors and unverified performance claims remain
distinct from measured results. New tests below supersede its stopped status.

**9November measured follow-up to A12/A13:** Flint Q3XL72K/cap1024 completes
the private audit in2h53m and scores25/36; all15sources were delivered but its
merge logic still overwrites null and aliases mutable values. Eight of eight
continuations reuse the full available prefix. Prefill takes102.34minutes and
generation70.60minutes: whole-history re-prefill does not explain this run's
delay. This is a single-seed extended result, not a quantization or cap ablation.
See the [measurement](reports/2026-11-09-flint-q3xl-private72k.json).
Fifteen fixed-prefix controls have now completed, including a baseline repeat,
two combined profiles and a matched2K full/windowed-SWA pair. The best combined
profile halves short cold-input time; full-SWA retains useful earlier state for
a middle edit at an allocation cost. Outputs also differ, and no quality gain
follows from timing alone. The native72K audit subsequently completed31/36 with unchanged
frozen questions/sources, no engine reasoning ceiling and separately measured
reasoning/content/tool-event timing. It is not a reasoning-only ablation: cache,
microbatch and resident settings also differ from the completed capped audit.

A separate15second passive sample during that native audit observes
142.19–159.88MiB/s E: reads and0.114–0.134ms average read latency. It is
whole-drive telemetry, not model-exclusive I/O or proof of SSD saturation.
Process page faults also include soft faults. See the
[raw-counter summary](reports/2026-11-09-flint-paging-observation.json) and
[memory interpretation](docs/memory-and-context.md). A resident6GiB A-B-A
follow-up completed:6GiB improves cached repeats, but cold gains are smaller than baseline drift.

9November additional reading of the preserved Qwen technical report (§2.3,
§4–5 and long-context/MTP evaluation): its headline model comparison is for
**base checkpoints**, not our quantized tool agent. Larger n-gram tables lower
training loss without consistently raising downstream scores. Their placement
in layer2 enables host lookup prefetch to overlap layer1 computation; this
does not establish the cost of our SSD-backed PLE route. Long-context tests
also remain imperfect: the reported eight-needle MRCR score at512K is40.53.
Thus native long context is a capability budget, not guaranteed retention.
The report's MTP acceptance result is not a whole-workflow speedup. These
points reinforce testing actual file reads, retained facts and total time.
[Pinned paper](https://github.com/QwenLM/Qwen3.8-Flash-Next/blob/69885871a64393807d988b27b1b5e380e8f28526/tech_report.pdf).
The previously extracted local text was used after the browser could open the
GitHub wrapper but could not parse the raw PDF response; this is selected
section review, not a claim to have read every training derivation/reference.

9 November recovery also confirms the original Next80 Instruct's exact IQ3_M
artifact and 18 syntactically valid completed Python outputs. Its interval/CSV
bugs were semantic. The [publisher](https://huggingface.co/Qwen/Qwen3-Next-80B-A3B-Instruct)
specifies non-thinking Instruct and 262,144 native context; the old advice
confused our configured 32K with the model's native capacity. See the
[historical model record](docs/tasks/2026-11-09-qwen3-next80-instruct/2026-11-09-qwen3-next80-instruct-v0.11.0.md).

| Question | Conclusion supported so far | What remains unproven |
|---|---|---|
| Is an old model still occupying all the RAM? | 9 Nov recovery found no llama/Strata engine and Ollama's loaded inventory was empty. Available RAM was 7.856 GiB, later 9.644 GiB without closing apps | This does not identify every consumer or prove a leak. Standby is already included in available RAM; summing working sets double-counts shared pages |
| Does higher quantization fix coding? | No automatic guarantee. Qwen Q4's matched private score was 31/36, Q6 XL 28/36; different native Q4 coding still exposed interval/CSV/JS defects | A single seed does not prove Q4 intrinsically smarter. Quant, placement, sampler, precision recipe and incomplete outputs must remain distinguishable |
| Can RAM KV preserve every file forever? | CPU KV and q8 reduce VRAM demand. Context capacity, actual occupied tokens and allocated/resident memory are separate. Sleep discards KV; clients must resend history | Larger context does not guarantee retrieval or instruction adherence. Source delivery and changed-file invalidation need direct tests |
| Should we fill every spare MB of VRAM? | Some additional offload/cache can help, but prefill scratch, KV, drafts, desktop use and WDDM commit need headroom | Reported free VRAM from an allocator can differ from physical device availability. Do not size solely from CUDA's Windows free-memory number |
| Is more reasoning always better? | Flint's two capped router answers passed the same six behavior groups; 8192 took 2.4x longer with no demonstrated score gain | Private audit / broader coding may behave differently; no universal optimum or trained ultra-effort label established |
| Are speculative tokens or MTP free speed? | Prior local draft/MTP tests did not establish a broad gain; they consume memory and may reduce the expert cache | A modern same-weight runtime may improve results. Measure accepted tokens **and** net wall time, with output equivalence controls |

## Primary-source anchors and limitations

### Which memory grows?

| Mechanism | What changes as work grows | What it does not establish |
|---|---|---|
| Weight mmap / resident cap | Windows faults weight pages into RAM and can evict them; a low cap can increase repeated page traffic | Weights are not conversation memory; process fault counts include soft faults |
| Ordinary llama.cpp KV arena | Capacity is commonly allocated at load; occupied cells increase as prompt/output tokens accumulate. CPU residency can change separately | A stable allocation does not mean context stopped growing; a large allocation does not prove recall |
| q8 / q4 KV | Cache cells use fewer bytes, with block metadata and architecture-specific overhead | No universal "32K equals16GB" or "128K equals8GB" formula; no guaranteed accuracy equivalence |
| `--cache-ram` and checkpoints | Additional prompt-cache/state reuse may retain reusable computation across requests | This is separate from a model's primary KV placement and cannot recover files the client omitted |
| Strata `--kv-grow` in the reviewed native code | GPU KV backing grows in steps and can evict GPU expert-cache slots | It is not the same mechanism as pinned-host-KV streaming; stable total VRAM can hide the trade |
| Idle model unloading | Weights and in-memory KV are released; a later request reloads the model | The client must resend needed history/files; the model does not retain permanent chat memory |

Our current Flint72K profile allocates 1,071 MiB global-attention GPU KV plus
27.89 MiB sliding-window KV at load. That is a model-specific observation, not an estimate for Qwen,
GLM or Dory. The subsequent Flash growth test recorded allocation events and two completed
fact answers, then crashed during33K prefill; its qualification is incomplete.

For this exact Flint allocation, the logged4KV heads and128-dimensional K/V
heads let us reconcile the buffers directly. q8_0 uses34bytes per32values,
including its scale. Full-context storage is
`73728 × 14 × 2 × 4 × 128 × (34/32) = 1071 MiB`; the sliding-window arena is
`768 × 35 × 2 × 4 × 128 × (34/32) = 27.890625 MiB`.
Together they are about1.073GiB, before other runtime buffers.768is the
allocated sliding-window cell count, not the full model context. These are
the actual recorded shapes, not a generic RAM estimate. Moving that KV to CPU
would change placement, not its configured token capacity or guarantee recall.

Further corrections to A14's earlier pasted advice:

- The [GLM-4.5-Air card](https://huggingface.co/zai-org/GLM-4.5-Air) describes
  106 billion total parameters and 12 billion active. Even the simple nominal
  four-bit calculation is about 53 GB before overhead, so the quoted 28 GB Q4
  recommendation is not a credible artifact-size estimate. GLM-4.7-Flash is a
  different model, which we actually tested.
- Fixed claims such as "MoE needs Q6 to equal dense Q4" or "80B-A3B is as
  smart as a 30B model" are not established by parameter counts. Our local
  precision trials are task-specific counterexamples to a universal ranking.
- Layer offload normally places selected weights and their computation on
  CPU/GPU. It is not automatically a streaming scheduler that copies every
  layer into VRAM for every token. Tensor overrides also require actual tensor
  names; a guessed router regex does not prove the intended placement.
- Context size is a token budget shared by instructions, files, tools, history
  and output. KV quantization reduces storage per cache cell; it does not force
  an editor to send omitted files, guarantee recall, or preserve state through
  model unloading. Long-context correctness still needs direct tests.

9 November source clarification: Strata0.1.50 `--kv-grow` grows **GPU** K/V
backing in steps while trading GPU expert-cache slots. Its eligibility check
requires `kv_resident <= 0`, so it is distinct from the older pinned-host-KV
streaming experiment. Neither that flag nor stable total VRAM establishes
dynamic RAM-KV allocation. The planned comparison must inspect native mapped
cells, cache slots, fresh allocations and recall, not only Task Manager.
CUDA VMM support was queried successfully3Nov; that capability query loaded
no model and is not proof that Strata activated growth.

Further source review9Nov adds two checks for that future experiment. The
elastic controller must actually start with more than128eligible cache slots
after the prefill loan; passing the initial VMM capability check is insufficient.
At its expert-cache floor, growth can allocate fresh GPU memory. It therefore
does not guarantee flat VRAM use. A shorter request also need not immediately
return every allocation: trimming has a two-step hysteresis and accounts for
parked conversations. Require the native start/grow/trim logs alongside memory
and recall measurements; do not infer behavior from the flag alone.

The b12069 cache-shift check is a capability restriction, not proof that every
hybrid model fails it: this source's recurrent memory returns true and hybrid
memory delegates to attention. A useful cache-reuse experiment must still
measure changed-prefix behavior and preserved output; ordinary full-prefix
hits do not demonstrate that a new reuse setting helps.

Early9November checkpoint, superseded by the completed result above: Flint's first three
completed continuations report cached counts3,082/14,114/21,833, exactly equal
to the preceding reported KV length in each case. They process10,653/7,472/2,859
new tokens. Thus the observed wait in these turns is new-file prefill and
generation, not a full-prefix cache miss. This timing reconciliation neither
certifies recall nor predicts editor traffic. The later completed answer scores25/36.

Later in that audit, all15source documents were reached and the original three
read errors were recovered. Turn06 then exhausted the1024reasoning-block cap
and redundantly reread one delivered line. Keep this separate from the earlier
router result: a useful ceiling on one task is not established as optimal for
another. This b11838 sampler can re-arm on a new reasoning start tag, so the
ceiling is not an aggregate thinking budget for the full tool workflow.


- [Pinned llama.cpp server documentation](https://github.com/ggml-org/llama.cpp/blob/e6192de0a62b73f566f825ecb531f7e4fe699eae/tools/server/README.md): physical microbatch and logical batch differ; cache reuse depends on KV-shift support. Local source additionally checks `llama_memory_can_shift()` before enabling reuse.
- [Qwen technical report](https://github.com/QwenLM/Qwen3.8-Flash-Next/blob/69885871a64393807d988b27b1b5e380e8f28526/tech_report.pdf): the prior review read the introduction and relevant architecture/long-context sections, not every page. Native context and module speedups do not measure our agent workflow.
- [Windows memory accounting](https://learn.microsoft.com/en-us/windows-hardware/test/assessments/results-for-the-memory-footprint-assessment) and [our WDDM observations](docs/memory-and-context.md#vram-allocations-also-consume-windows-commit): physical availability and commit are independent launch gates.
- [Claude's re-prefill audit](reports/2026-11-03-reprefill-audit.json) is a historical log analysis: 805 timed turns, 762 matched to server tasks; no new model run. Four editor divergences cost an estimated 578 seconds. This does not rule out a fresh editor transport/context failure.
- [New runtime control](reports/2026-11-09-b12069-prefetch-controls.json): stock, modified-default and opt-in produce identical tiny-model greedy output on CPU and GPU. This is limited compatibility evidence, not full-model equivalence or a throughput improvement.

All recommendations remain hypotheses until their individual rows gain an
actual receipt. New articles append rows; corrections are dated, and old
measurements remain available. No model is promoted by adding a research link.


### Historical 9 November pre-serving checkpoint

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


### Flash qualification and active KV diagnostic

### Final 9 November disposition

Static Q2 greetings completed after the isolated frontend ACL correction;
dynamic64K GPU KV then grew0.23/0.33/0.52GiB before a0x116 system crash
during33K prefill. Its first two five-fact answers are observations, not a
qualified recall/coding score. The shrink request and128K private audit did
not run. See the [incident](reports/2026-11-09-flash-q2-gpu-restart.md).
All15Flint performance controls completed earlier; native private31/36 is
retained. Current pending work and publication checks are in the merged report.
Detailed chronological checkpoints remain in docs/tasks.md and Git history.
