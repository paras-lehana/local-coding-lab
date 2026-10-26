# Higher precision and practical offload improvements

Reviewed 24 October 2026 for RTX 3080 10GB, Ryzen 7 5800X, 64GB system RAM,
Windows and an apps-open desktop. This is an engineering assessment; measured
outcomes live in the [precision campaign](../../docs/tasks/2026-10-24-precision-and-gaps/2026-10-24-precision-and-coverage-v0.9.0.md).

## Recommended order

Progress at22:00IST: the order below is the original plan, not a claim that
these controls remain untried. Native Qwen Q4 now attempts all twelve coding
questions: nine frozen passes, two failures and one output limit. Two passing
JavaScript answers also fail separate post-review checks. Higher Flint Q4
misses the router deadline in both tested placements. Qwen's fixed7GiB-resident
cache control loads but times out without code; plain Q6 has now passed full
file verification and short loading, with its public workflow still running.
The linked campaign is authoritative for subsequent outcomes.

During the Q6 file trial, three read-only Windows counter samples at
22:06:30-22:06:42IST show E: reads of67.6-135.3MiB/s and856-2245 system
hard-page read operations per second. The owned model process reports roughly
176K-216K page faults per second, which include soft faults. These separately
sampled counters are not additive or process-attributed disk measurements;
the owner's applications remain active. In particular, process IOReadBytes
reports zero despite system disk traffic, so that counter alone cannot rule
out memory-mapped reads. This supports investigating residency/I/O overhead;
it does not prove every disk read belongs to the model or measure a cold-cache
speedup. Raw sample receipt: the Q6 public trial's `io-observation.json`.

1. **Finish comparable quality coverage first.** Qwen Q4's retained instruction
   score does not include the newer twelve-task coding suite. Complete it and
   the smaller IQ3/IQ4 variants before calling any model the overall winner.
   Preserve identical questions, explicit sampling and the 1200-second limit.
2. **Try Flint Q4 with a memory plan.** The pinned Unsloth Q4 XL is23.33GiB,
   versus13.54GiB for the prior IQ3_XXS. More precision is a plausible quality
   control, but a model that pages heavily can lose the usable-task comparison.
   Use the reviewed initial-prefetch opt-out, measured placement and a bounded
   process working set. Q3 XL is a smaller fallback, not a4-bit equivalent.
3. **Test the already-merged GPU expert cache.** A matched IQ3 control can spend
   spare GPU memory without changing its CPU expert threshold. Flint needs a
   separate placement/cache tradeoff. Measure full task time, not just decode.
4. **Diagnose output limits separately.** Flint's earlier CSV task hit16K output
   without an answer. Its card recommends at least32K for hard tasks. A32K
   diagnostic retains the same20-minute wall limit and does not overwrite the
   frozen16K result. Preserve reasoning history through actual request payloads.
5. **Consider new engines only against a verified reference.** A fork needs
   architecture support, correctness checks, memory telemetry and the same
   complete workflows. A vendor's larger GPU result is insufficient.

## What each technique changes

| Technique | Possible benefit | Limit on this PC |
|---|---|---|
| Higher weight precision / better calibration | Lower distortion; calibration can protect code/tool-sensitive weights | Does not guarantee syntax, reasoning or instruction compliance; bigger weights increase paging |
| GPU KV instead of CPU KV | Faster attention and prompt processing in our earlier Flint controls | Competes with weights, expert cache and temporary GPU allocations |
| Quantized KV | Smaller attention cache at a chosen capacity | Architecture-specific size and possible quality loss; not permanent file/chat storage |
| GPU expert cache | Reuses CPU-held expert tensors in VRAM and reduces repeated transfers | CPU originals remain; cache hit rate and batch path matter |
| mmap without initial prefetch | Avoids eagerly pulling the whole mapped file into RAM | Later demand paging remains; it cannot create physical memory or bandwidth |
| Pinned host weights | Faster transfers for suitable non-mapped configurations | Cannot rely on eviction to disk when the same weights must remain pinned |
| Speculative decoding / MTP | May reduce decode latency with useful accepted drafts | Additional weights, cache and compute; acceptance is not end-to-end speedup |

### Precision is a recipe, not a guarantee

An increase from three to six bits is useful only if the resulting model
finishes and improves the tasks that matter. More accurate weights cannot
repair a client that omits instructions, a wrong tool path, a truncated answer,
or every learned coding mistake. Conversely, our smaller quants have delivered
syntactically valid code with behavioral bugs. The measured evidence rejects
the blanket explanation that every missing bracket or wrong answer is caused
by being below four bits.

[Google's Gemma QAT card](https://huggingface.co/google/gemma-4-26B-A4B-it-qat-q4_0-gguf)
describes training specifically for quantized deployment, rather than only
compressing a fixed full-precision checkpoint afterwards. That motivates
keeping the installed QAT fallback in the comparison; it does not establish
local superiority over a six-bit Qwen. Google's current recommended sampler is
temperature1/top-p.95/top-k64. It retains thoughts within tool-call turns but
excludes them from earlier completed user turns. Our frozen Gemma coverage
profile instead uses.6/top-k20 and preserved thinking; report those actual
controls, and keep any publisher-setting follow-up separate.

[IFM's K2 card](https://huggingface.co/IFM/K2-Horizon-MoVA-36B-A4B#best-practices)
recommends native high effort, temperature1 and top-p.95. Its published serving
recipe uses twoH200s and an explicit router-numerics setting. Neither those
benchmark scores nor that recipe validate our single3080 GGUF path. Its
MoVA value experts and much larger KV requirement also need their own memory
plan; Qwen's small hybrid-attention cache estimate does not transfer.

llama.cpp generally reserves a cache arena for configured context. Occupied
tokens increase inside that arena; resident host pages are another measurement.
For example, the new Qwen IQ3 audit reaches41,930 prompt-plus-generated tokens
while its64K GPU-q8 arena remains680MiB. Client truncation, source delivery and
history transport still determine what the model sees. A large cache does not
automatically read every `.github` or `.claude` file, and idle unloading frees it.

In the inspected b11838 CLI, `--no-kv-offload` places KV on the CPU;
`--kv-offload` enables device offload and is the default. The earlier suggested
`--offload-kqv` command is not advertised by this build and must not be described
as a RAM-cache flag. Always check the installed executable, then its allocation
logs. Fixed claims such as "32K always uses16GB" do not apply across architectures.

Likewise, [Qwen3-Coder-30B-A3B](https://huggingface.co/Qwen/Qwen3-Coder-30B-A3B-Instruct)
is an MoE model; its official card describes a non-thinking interface, not an
adjustable high-effort mode. Active parameter count is not a
conversion to an equivalent dense model's intelligence, and there is no
established universal rule that MoE Q6 equals dense Q4. The measured code and
grounding results are the useful comparison for this workstation.

## What upstream evidence actually supports

- [Merged PR29887](https://github.com/ggml-org/llama.cpp/pull/29887) introduces
  native GPU expert caching. Its published gains use larger GPUs and a specific
  decode benchmark. Both installed b11562 and b11838 expose the flag. Local
  historical Q4 cache results are faster but use different weight placement;
  their lower score is not proof that caching intrinsically reduces accuracy.
- [Merged PR30449](https://github.com/ggml-org/llama.cpp/pull/30449) splits large
  Windows pinned buffers for non-mapped expert loads. It addresses failed huge
  pinned allocations, not insufficient RAM for an apps-open desktop.
- [Open PR30594](https://github.com/ggml-org/llama.cpp/pull/30594) overlaps CPU
  misses with cached GPU computation. Results depend on the cache fraction;
  its own Flint example is slower than upstream. It is an experimental option,
  not the first change to deploy.
- [moe-cache](https://github.com/IbrahimSiddiqui007/moe-cache/tree/bb9315345eea6fbed5c7826a452c5864788ef758)
  explores bounded CPU expert memory backed by SSD. Its documented platform
  is Linux with matched shared GGML libraries. Stock is preferable when weights
  fit; approximate modes are a separate quality tradeoff. This is not a Windows
  flag that can be added to the existing executable.
- [llama-cpp-perf](https://github.com/mateusoro/llama-cpp-perf/tree/191121669732e6fbac9577528912b5df328a2553)
  explores pinning, streams and asynchronous work. Its reported hardware and
  architecture support differ, and whole-model pinning conflicts with paging.
- [Tere Labs' Flint calibration report](https://huggingface.co/terelabs/flint-GGUF)
  motivates code/tool calibration and mixed precision. Its small comparison
  does not establish a statistically significant4-versus5-bit winner. Local
  bugs must be rerun rather than predicted from a quantization label.
- [Flint's official card](https://huggingface.co/RecursiveSI/flint) recommends
  temperature1, top-p.95, top-k20, reasoning preservation and a large output
  budget. The distilled [NVFP4 release](https://huggingface.co/RecursiveSI/flint-nvfp4-gguf)
  changes the recipe as well as precision. Ampere compatibility and throughput
  need live checks; advertised Blackwell performance does not transfer to3080.
- [Qwen's official card](https://huggingface.co/Qwen/Qwen3.6-35B-A3B) gives
  precise-coding sampling controls; [Unsloth's guide](https://unsloth.ai/docs/models/qwen3.6)
  also discusses calibration and MTP. Our current file lacks the extra MTP
  tensors, so a flag alone cannot enable a valid draft model.

The old Flint hexadecimal-template fix is already included in b11838. Its
earlier file-driven task successfully read six sources before guessing paths;
that is not evidence of that old parser defect. Open issues about reasoning-
only tool XML and optional-argument permutations should be checked against the
actual tool schema, not used as blanket explanations for a failed agent.

The same caution applies to Qwen issue reports. The
[b9330 thinking-loop report](https://github.com/ggml-org/llama.cpp/issues/23684)
uses MTP, heterogeneous GPUs and CUDA13.x; our current single-GPU CUDA12.4
file has no MTP tensors. The
[cache-invalidation discussion](https://github.com/ggml-org/llama.cpp/issues/21831)
concerns reused multi-turn prefixes; our failing interval case is the first
request with no cached prompt. Neither establishes this local failure's cause.
Likewise, [issue30118](https://github.com/ggml-org/llama.cpp/issues/30118) uses a
custom template and missing tool-call opener, whereas our direct coding tasks
advertise no tools. These sources motivate targeted diagnostics, not a blind
template/kernel replacement. New instruction tests must still inspect actual
tool payloads and cached/new prompt counts after any runtime change.

## Other engines checked on24October

[ExLlamaV3](https://github.com/turboderp-org/exllamav3/tree/da68d57de61781e5b74ad68698ac4caf36408d7a)
is now at1.6.4 and documents experimental CPU MoE offload with AVX2 support,
including Windows paths. Its
[controls](https://github.com/turboderp-org/exllamav3/blob/da68d57de61781e5b74ad68698ac4caf36408d7a/doc/env_vars.md)
cover layer/expert splitting, streamed prefill and host-memory reserves. It is
a credible future engine comparison, not an AMX-only option. It requires EXL3
weights and a separate PyTorch/Triton environment; Windows host arenas consume
both RAM and commit. The documented stream-memory-operation path has a Windows
testing caveat. No local ExLlama result exists, and an
[open host-KV request](https://github.com/turboderp-org/exllamav3/issues/269)
does not establish implemented RAM-backed active attention.

[KTransformers' AVX2 tutorial](https://github.com/kvcache-ai/ktransformers/blob/main/doc/en/kt-kernel/AVX2-Tutorial.md)
does support older CPUs, but its current recipe calls for Linux and24GB-plus
VRAM with model-sized host memory. It does not validate our10GB Windows/apps-open
configuration. Do not dismiss every KTransformers path as AMX-only, or present
this recipe as an already compatible replacement.

[Strata's v0.2.4 release](https://github.com/Niko1221/Strata/releases/tag/v0.2.4)
is newer than the tested v0.1.45 fork. Its latest release body describes0.2.4.2
installer/DeepSeek changes and says Qwen engine packages remain0.1.48. The
current source at `7dd5cf18e68c639a8773e096c5c79f971ea2a9f5` still explicitly
allocates fp32 Qwen session caches; Flash-Next KV flags must not be inferred
to work on that separate path. The
[Qwen quantized-KV issue](https://github.com/Niko1221/Strata/issues/2693) was
closed in a tracker reset, not as a demonstrated fix or a technical rejection.
New engine timings and tool quality require new tests; historical1.2-1.75x
public-task gains do not certify the newer release. The advertised DeepSeek
route needs239GB-plus disk and much more free host memory than this desktop,
so its low-VRAM headline is not a current fit claim for this machine.

## Current assessment

A fresh Hugging Face metadata check on24October finds the current Unsloth
Qwen repository still at our pinned revision `a483e9e6cbd595906af30beda3187c2663a1118c`.
The IQ3_S, IQ4_XS and Q4_K_M published hashes match the catalog. The earlier
large Q6 experiment used **UD-Q6_K_XL**,31,843,777,504bytes, despite some
summary tables abbreviating it as Q6_K. The smaller UD-Q6_K artifact is
29,308,320,736bytes and is a different, untested file. The guide's statement
about an updated Q6 must not be treated as proof that this already-pinned
repository changed after our tests. Exact artifact names/hashes decide that.

The local K2 Horizon inspection adds a placement caveat: in b11838,
`--n-cpu-moe` matches only FFN expert tensors. It does not move the model's
3.955GiB attention-value experts. A naive sum of every `_exps.weight` tensor
underestimates VRAM for that flag. The queued IFM model is distinct from
Moonshot's Kimi K2. The prepared profile explicitly moves attention-value
experts to CPU and uses64K GPU q4 KV (estimated3.375GiB versus6.375GiB q8).
It also caps resident process memory; actual speed, allocation and quality
remain unmeasured. These settings should not be copied into Qwen or Flint
without inspecting their architectures.

New local Q4 Flint measurements do not support a recommendation yet. CPU44
without cache and CPU48 with1536MiB expert cache both hit the1200second router
deadline. The latter starts a partial visible answer near1137seconds but does
not finish. Different desktop headroom produces different resident caps, so
this is not an isolated estimate of cache speed. See the campaign receipts.

Qwen IQ3_S also exposes a different bottleneck: its first direct coding task
uses16K reasoning tokens without delivering code. The official Qwen card
recommends32K output and permits a0-to2 presence penalty against repetition,
with possible quality/language tradeoffs. The frozen precise-coding controls
remain.6 temperature and zero presence penalty. Larger output, a runtime
reasoning ceiling, native thinking-off, and a repetition penalty are separate
diagnostics; none should silently replace the original answer or be described
as a higher native effort level.

The most useful next step is a completed, grounded answer with executable
checks. Higher precision may help; it cannot compensate for missing source
delivery, tool loops, output truncation or severe paging. Keep the quality
scores and failure modes separate from memory fit and token throughput.

The new IQ3 control demonstrates why these distinctions matter: the4096
reasoning ceiling produces two completed frozen coding passes where native
reasoning exhausted16K tokens without code. Adding1536MiB expert cache then
raises first-case decode from15.025 to32.414tok/s, but changes the generated
algorithm and output length. Source review sees a missing touching-span merge.
This is a single-sample speed observation, not numerical-equivalence proof or
a reason to inherit the uncached correctness score. The full cached suite now
finishes all twelve questions, with six passing and six failing after source
review and isolated execution. Median whole-task time is133.86seconds;
decode ranges31.05–36.76tokens/sec. The uncached control passes its two
completed cases, but ten cases were not completed on that setting. These are
different coverage sets, not evidence that the cache itself halves accuracy.
Both TTL implementations also fail a separate post-review NaN diagnostic.
See [the coding receipt](../../reports/2026-10-24-qwen-iq3s-cached-coding.json).

Two further engine leads are research-only. The
[MaxDam prefetch fork](https://github.com/MaxDam/llama.cpp.35B.moe)
reports pinned expert transfers and prefetch improvements on a3060/12GB.
Pinning the whole CPU expert bank could defeat this desktop's paging reserve;
its hardware and source differ from our native cache measurement. The
[moe-pigeon Windows fork](https://github.com/1xayd/moe-pigeon)
advertises disk-backed experts and tiered Q2/Q4/Q8 context, with automatic
placement and changed repetition defaults. Its cache budgets are not process
RSS guarantees. Those defaults would confound a direct comparison and older
context atQ2 needs retrieval-quality checks. Neither fork is installed or
locally validated; they are not replacement commands for the current runtime.

Native effort controls also need model-specific inspection. The
[K2 Horizon card](https://huggingface.co/IFM/K2-Horizon-MoVA-36B-A4B)
actually recommends `reasoning_effort=high` in template kwargs,temperature1
and top-p.95. The
[Bolt card](https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Bolt-74B-A9B-24GB)
uses `enable_thinking=true`, with `medium_effort=true` for medium reasoning.
Its retained GGUF header confirms these keys and defaults historical-thinking
truncation totrue. The prepared coverage profile explicitly sets truncation
false and mediumfalse; this must remain part of the recorded conditions. Bolt's
eight attention blocks give a64K q8 attention-arena estimate of272MiB, plus
recurrent state and runtime buffers. K2's much larger estimate is architectural,
not a universal per-token memory law. Neither new profile is a live result yet.

## Which improvements deserve the next local test

| Technique | Evidence here | Next useful check |
|---|---|---|
| Native GPU expert cache |IQ3 decoding reaches31–37tok/s, but capped coding only6/12 |A separate native-reasoning/larger-output diagnostic may use the saved time for reasoning. Do not inherit capped scores or promise that more tokens correct mistakes |
| More weight precision |Earlier Q5/Q6XL do not beat Q4's private audit; new IQ4 bounded router finishes536s |Complete new IQ4 and Q4 coding before judging precision from a label |
| Bounded resident model pages |Uncapped IQ4 trips RAM floor; capped retry finishes the router with apps open |Measure longer input and task completion; disk-backed address space is not free physical memory |
| GPU q8 KV at64K |Qwen allocates680MiB for attention KV |Use CPU KV when its VRAM savings justify measured latency, rather than assuming a universal16GiB32K cache |
| Native output/reasoning controls |IQ3 uncapped16K can yield no code;4096 ceiling yields code but does not guarantee correctness |Keep the frozen16K cases, then try a separately recorded32K allowance under the same1200second wall limit |
| Alternative engines/prefetch forks |Primary-source compatibility and memory limitations reviewed; not locally installed |Finish the compatible model baselines first; pin any new engine, prove output/placement and rerun complete file workflows |

The native-cache32K idea is a hypothesis, not a result. At the observed cached
decode rates a longer output could fit the wall limit, but uncached IQ4/Q4
or heavily paged Flint may spend that allowance too slowly. Prefill, tool
round trips and final text must all fit; multiplying tokens by a peak decode
rate is not a completion measurement.

## Checks against misleading optimization claims

The author's later correction in [llama.cpp issue26025](https://github.com/ggml-org/llama.cpp/issues/26025)
withdraws a claimed version-fix verification: the new binary was never deployed,
and RAM pressure confounded the timing. This supports recording the actual
loaded runtime and desktop headroom; it is not evidence of our cache failing.

The separate [moe-cache plugin's decision record](https://github.com/IbrahimSiddiqui007/moe-cache/blob/main/docs/ENGINE_DECISION.md)
distinguishes simulated GPU-tier gains from built features and reports token
divergence between CPU/GPU arithmetic. Its one-token prototype defect is not
the native llama.cpp cache used here. Neither finding establishes a local
cache correctness bug. Our changed sampled answers require behavior tests and
repeat controls; token differences alone cannot prove corrupt expert mapping.

A [same-artifact Strata comparison](https://github.com/Niko1221/Strata/issues/3082)
reports useful gains on a32GB V100, but its256-token outputs, IQ1 model,
PCIe3x4 link and near-total GPU expert residency differ substantially from this
lab. The author's cache-size sweep also shows a sharp slowdown below its
working-set needs. It does not support a universal6x claim or predict this
3080's long-context tool workflow latency.

The installed Gemma26 GGUF header is also re-inspected before its queued run,
without loading tensor data. Its template supports `enable_thinking` and
`preserve_thinking`, defaulting both tofalse. The latter retains historical
thinking for messages with tool calls; it does not mean every old final
answer's reasoning survives. There is no native `reasoning_effort` or
`thinking_budget` selector in that template. These local source facts justify
the explicit booleans in the queued profile, not an invented ultra level.

A separate IQ4 presence-penalty control is frozen after its first native coding
request continues reasoning for nine minutes. The publisher explicitly permits
presence penalties0..2 to limit repetition, while warning of language mixing
and possible quality loss. Our .6 precise-coding baseline correctly uses0;
1.5 is an experimental change, not a correction to the publisher's recipe.
The installed sampler applies penalties over repeat_last_n64; this remains
unchanged in the one-variable control. It is not full-history repetition
suppression. The actual trial exhausts16384 reasoning tokens in1187.703seconds
without code. It does not restore completion. The larger resolved resident cap
also differs from the baseline, so the small throughput difference cannot be
attributed solely to sampling. Full-history penalties or other values remain
untested; the result is scoped to the recorded1.5/64-token window.

18:25IST follow-up frozen, not yet run: Q4 CPU40/cache2048/general32K.
This combines the publisher's general-thinking temperature1/presence1.5 recipe
with native reasoning,32K coding output and2GiB GPU expert cache. It is a joint
usability configuration, not an isolated quant/cache experiment. Header-only
estimates put CPU experts18.225GiB, embeddings0.503GiB and otherweights1.876GiB;
cache/KV/runtime allocations still need measurement. The native Q4 baseline
runs first. Its results do not transfer to this new configuration. All physical
RAM, commit, VRAM, hardware and1200second gates stay unchanged.

The distinct plain Q6 artifact is now catalog-pinned and header-inspected,
with full download/load pending. It has24.791GiB CPU expert spans atCPU40;
substantial paging is expected with apps open. Before calling it unusable,
a changed placement/cache profile may be tested, but decode-only gains do not
address the slow prefill observed in the historical larger XL artifact.

## Additional CPU-oriented engine: ik_llama.cpp

Reviewed primary documentation at commit
`804ee29c28a5e892df6e84941cb78628ed4c266c`; metadata/text hashes are retained
locally. No binary was built, installed or benchmarked. Its
[README](https://github.com/ikawrakow/ik_llama.cpp/blob/804ee29c28a5e892df6e84941cb78628ed4c266c/README.md)
lists Qwen3.5/3.6, Gemma4 and K2 Horizon support, CUDA and AVX2 CPU paths,
and improvements to CPU prompt processing. This is relevant to the measured
prefill bottleneck and deserves a later same-artifact engine comparison.

The author's [Qwen3.6 quantization discussion](https://github.com/ikawrakow/ik_llama.cpp/discussions/1663)
distinguishes IQ4_KS from trellis quants, warning that trellis CPU execution is
slower on plain AVX2. Its fast hybrid example uses a Ryzen3995WX and RTX3090
with an artificial8GiB limit, not a5800X/3080 with open desktop applications.
Its perplexity comparison is not a coding/instruction score, and the author
says the illustrated custom quant was not published. A commenter independently
reports bounded outputs consumed entirely by thinking; that corroborates a
failure pattern, not a validated fix or a result on this PC.

The [parameter reference](https://github.com/ikawrakow/ik_llama.cpp/blob/804ee29c28a5e892df6e84941cb78628ed4c266c/docs/parameters.md)
marks expert deferral/prefetch as Linux features. It also documents a separate
GGML_CUDA_NO_PINNED_WEIGHTS option for keeping CPU-overridden weights mapped,
and runtime repacking. These are distinct memory behaviors; none proves the
Windows initial-prefetch issue is solved. Before a trial, inspect actual source,
Windows build requirements, memory-copy behavior and supported flags; retain
the pinned baseline and avoid assuming AVX512 benchmark gains on this AVX2 CPU.
## Distinguish expert-cache implementations and link limits

The native cache's [multi-GPU follow-up](https://github.com/ggml-org/llama.cpp/pull/30112)
merged8October. Its author's two4090/EPYC example improves decoding while
reducing prompt throughput; it is not a claim that every stage gets faster.
This reinforces measuring full file workflows, not only generated tokens/sec.
The cache size is per GPU. Our single3080 configuration still needs its own
allocation, completion and correctness results.

The older [hybrid hit/miss RFC](https://github.com/ggml-org/llama.cpp/discussions/24528)
is a different implementation: it proposes GPU execution of cache hits while
CPU threads compute misses, with different flags and activation heuristics.
Its reported multi-GPU/EPYC gains and later user workarounds must not be pasted
into a native `--moe-cache-mib` profile as if they configure the same engine.
No extra fork is installed for this source review.

A saved instantaneous device sample during the Q4 native coding run at
19:50IST reports PCIe4.0x16, matching the reported maximum. It does not show
an obvious negotiated-link downgrade. GPU utilization18%, graphics405MHz and
power102W are individual samples during mixed CPU/GPU execution, not sustained
averages, proof of throttling or a reason to change clocks. Whole-device VRAM
used8268MiB includes desktop applications; it is not the model's dedicated
allocation. Compare the forthcoming cached profile using actual wall time.

## What these Qwen quantization names actually contain

Exact saved GGUF headers and the pinned runtime's `ggml_type` enum show mixed
tensor recipes. The following GiB values are stored tensor spans, including
alignment; they are neither resident RAM nor a prediction of correctness.

| Artifact label | Header-derived tensor storage |
|---|---|
| IQ3_S | IQ2_S 6.406GiB, IQ3_S 3.975GiB, Q6_K 1.851GiB, IQ4_XS 0.398GiB, F32 0.097GiB |
| IQ4_XS | IQ3_S 8.594GiB, IQ4_XS 4.914GiB, Q8_0 1.894GiB, Q6_K 1.004GiB, F32 0.097GiB |
| Q4_K_M | Q4_K 11.250GiB, Q5_K 6.359GiB, Q8_0 1.894GiB, Q6_K 1.004GiB, F32 0.097GiB |
| Q6_K | Q6_K 23.994GiB, Q8_0 3.194GiB, F32 0.097GiB |

Plain Q6 contains117 Q6_K tensors,255 Q8_0 tensors and361 F32 tensors.
Its full27.296GiB file is still pending download and integrity validation.
Q4 already keeps many non-expert tensors at higher precision. Therefore a
higher filename bit count changes a specific recipe, not every tensor equally;
a claim that Q6 guarantees correct syntax or instructions is unsupported.
The source headers, byte counts and enum hash are retained locally.

## Smaller resident calibration and prompt batches

At20:59IST the desktop has13.640GiB availableRAM,12.977GiB availablecommit
and6364MiB freeVRAM, with no inference engine. This is below the original
Q4/cache16GiB and plainQ6/cache18GiB admission requirements. Those profiles
remain unchanged. Two separately named resident7 calibration profiles use
a fixed7GiB resident maximum and a larger6.5GiB host reserve, with13.5GiB
admission and the unchanged2.5GiB RAM/400MiB VRAM/1GiB commit stop floors.
The lower admission threshold is explicit, justified by reduced permitted
residency rather than a claim that the original profiles now fit. It requires
a short smoke before longer work. Windows resident limits do not limit total
commit, GPU staging or the owner's other applications. Stronger paging may
make even short tasks impractical; record that as a measured outcome.

The native Q4 run's5.934GiB peak private allocation and13.861GiB resident
maximum motivate reducing resident pages. They do not predict the cached
profile's allocation or prove the7GiB trial safe. CPU40 placement leaves only
about0.115GiB more non-expert GPUweights in plainQ6 thanQ4, while mapped
CPU experts grow from18.225 to24.791GiB. Same cache capacity therefore stores
fewer higher-precision experts, and disk access may dominate both profiles.

Local b11562 `llama-moe-cache.cpp` explicitly selects its cache lookup only
for token batches at most32 and when the bank can hold the worst-case selected
experts. Large batches can copy existing cached experts but do not refill the
cache. A smaller physical prompt batch is consequently a distinct experiment
worth considering after the128-token baseline, not a guaranteed prefill gain:
it trades batched CPU throughput against GPU transfers, expert churn and paging.
No batch-size result or new profile quality score is claimed here.

Measured follow-up: the Q4 resident7 profile loads and answers its short
smoke in6.187seconds, but the native interval question reaches1200.016seconds
without code. Last intermediate decode6.69tok/s and a7GiB resident ceiling
are not the fast cached IQ3 configuration. Memory floors remain clear; minimum
freeRAM5.700GiB andVRAM504MiB. This calibrates a loadable smaller-memory
profile, not a usable coding solution. No disk-read attribution follows from
its page-fault counter, and changed placement/sampling/residency prevent a
claim that the expert cache itself reduces intelligence or always slows Q4.

### Source follow-up: ik_llama.cpp Windows memory handling

The pinned [loader caller](https://github.com/ikawrakow/ik_llama.cpp/blob/804ee29c28a5e892df6e84941cb78628ed4c266c/src/llama.cpp)
contains a Windows-specific bulk-prefetch exclusion when device buffers are
present. Thus this fork has a relevant source-level mitigation; the earlier
documentation-only review did not establish it. The same source still ignores
expert-deferral on Windows, so its Linux deferred-expert claims remain separate.
The [CUDA implementation](https://github.com/ikawrakow/ik_llama.cpp/blob/804ee29c28a5e892df6e84941cb78628ed4c266c/ggml/src/ggml-cuda.cu)
also exposes a Windows pinned-allocation cap with pageable fallback. That
limits one allocator, not total process RAM or commit. These findings make a
pinned, separately validated Windows build a better future experiment than
assuming it must reproduce stock llama.cpp's initial-prefetch behavior. They
do not establish local speed, full-model numerical compatibility or fit.
Five source files were downloaded and hashed under ignored research evidence;
selected memory paths were inspected, not the entire engine. No build/install
or inference was performed. A guessed llama-impl.cpp path returned404 and is
not source evidence.

## Community precision recipes: useful leads, not local scores

The creator of [minicx's Flint IQ3_S mix](https://huggingface.co/minicx/flint-IQ3_S-mix-GGUF)
reports a16.5GiB file that gives selected non-expert tensors more precision
while retaining3-bit experts. Their60-generation Python evaluation reports
parity with UnslothQ3XL in less space, but worse prose perplexity than the
smaller UnslothIQ3XXS. This is evidence that bit allocation and workload matter,
not independent proof of an instruction-following upgrade. Their context
numbers use two10GiB cards and a separate beellama KV implementation; they
cannot predict this single3080's capacity or be copied as upstream flags.
Their proposed further recipe is unbuilt, so it is not an available candidate.

[Tere Labs' Flint quantizations](https://huggingface.co/terelabs/flint-GGUF)
preserve attention, embeddings and shared/dense computations at higher
precision, compressing routed experts. Their reported tool benchmark has
wide uncertainty and does not establish a small Q5 advantage over Q4. They
also correctly distinguish similarity to BF16 from quality of a separately
trained quantized checkpoint. Their smallest-file claim is not general:
the already pinned UnslothIQ3XXS andQ3XL are smaller. These files remain
research leads, not newly measured candidates or additions to our scores.

The pinned Unsloth headers retain the name Flint Preview, a preview license
metadata field and262144 context, while the
[repository card](https://huggingface.co/unsloth/flint-GGUF/blob/main/README.md)
identifies RecursiveSI/flint andApache2.0. Preserve this metadata discrepancy;
it does not itself prove different weights. Tere Labs reports equal BF16
tensors in its sampled comparison, not a full local verification. Our report
therefore identifies exact artifacts instead of silently treating a filename
or the512K marketing claim as validated context.64K trials are within the
GGUF's declared limit. Old community template workarounds also predate our
b11838 parser fix; no template filter is removed on their advice.

Local Flint header analysis confirms why these names need care. Q3XL has
6.123GiB IQ3_S,4.594GiB IQ3_XXS,4.395GiB IQ4_XS and1.555GiB Q8_0 spans,
plus smaller types; no tensor in this recipe is Q3_K. Q4XL is dominated by
11.305GiB Q5_K and8.769GiB IQ4_XS, with1.945GiB Q8_0 and smaller types.
The official NVFP4 artifact has20.668GiB NVFP4 and0.619GiB BF16, plus F32
scalars. These are stored spans including alignment, not resident allocations.
The b11838 enum and exact header hashes are saved in the local
flint-weight-precision-named receipt. NVFP4 is also a differently trained
quantized checkpoint, so it is not just another point on a single-bit ladder.

## KV advice must match the runtime revision

An upstream [mixed-KV fallback report](https://github.com/ggml-org/llama.cpp/issues/28455)
describes older CUDA builds sending unsupported quantized attention to CPU.
This is a useful diagnostic lead, not evidence that our current latency has
that cause. Direct inspection of both pinned local b11562/b11838 `fattn.cu`
files finds their type filter already accepts q4_0,q4_1,q5_0,q5_1 andq8_0;
the reported old type-equality/ALL_QUANTS filter is absent there. The
[pinned b11838 source](https://github.com/ggml-org/llama.cpp/blob/4231b23dc2c46661d01157aac5245bdcf03ce4b1/ggml/src/ggml-cuda/fattn.cu)
still checks head dimensions, layout and other conditions. Accepted types
alone therefore do not prove every attention operation executes onGPU.
Current experiments keep matching q8/q8, or matching q4/q4 forK2, and verify
loader allocations. No kernel profile, build change or speed improvement is
claimed from this source review.

The [K2 author's integration explanation](https://github.com/ggml-org/llama.cpp/issues/29424)
confirms value experts mix into ordinary attention values; it does not multiply
the stored KV cache by the number of experts. Its extra value-projection
weights do need explicit placement. Local K2 metadata has48blocks,8KV heads
and128-dimensional keys/values. This explains why its64K cache budget differs
greatly from hybrid Qwen; reuse the architecture-specific estimate and then
measure the actual buffers. The Windows tokenizer also needs the integrated
splitter, another reason to pin the supported runtime rather than copy an
old generic command.

## Tool recovery is another independent lever

Re-reading the original Flint GPU-KV TS/SQL trace shows all six required files
were delivered successfully before its26unavailable-path requests. The latter
include package.json, README.md, tsconfig.json, guessed tests/source paths and
even backups. Some repeat. This is not evidence that the tool parser could not
read the supplied paths or that required files never reached the model. Its
recovery/exploration behavior still prevents a final response.

After the new quant's unchanged native workflow, a useful separate diagnostic
would make an unavailable-file response explicitly advise finishing from the
already delivered contract and reporting missing optional material. Keep the
read allowlist, source bytes, question, deadline and original failure unchanged;
identify the changed tool feedback and never transfer its score to the native
workflow. Returning invented file contents or handing it the private rubric is
not an acceptable repair. This is a predeclared unrun recovery experiment,
not a discovered template fix or proof that more weight precision is required.

## RAM expert management and pinned-memory prefill

The [moe-cache plugin](https://github.com/IbrahimSiddiqui007/moe-cache/blob/bb9315345eea6fbed5c7826a452c5864788ef758/README.md)
manages CPU expert residency and overlaps disk reads with computation. Its
author reports gains when weights exceed available RAM, but recommends stock
llama.cpp when they fit. Exact execution is separate from optional approximate
routing/hybrid modes. These are author measurements, not our results.
The documented supported platform is Linux x86-64 with matching shared ggml
backend APIs. Its Windows layer only has cross-compilation/Wine checks and
has not run with real Windows llama.cpp. It therefore is not a drop-in plugin
for our current runtime. A separately bounded WSL or native port experiment
needs ABI, memory, token-equivalence and whole-workflow checks first. No plugin
was installed or benchmarked. This is relevant to our restricted resident
profiles, but does not prove that every slow turn is disk-bound.

The [llama-cpp-perf fork](https://github.com/mateusoro/llama-cpp-perf/blob/191121669732e6fbac9577528912b5df328a2553/README.md)
reports improved prefill from page-locking mapped expert weights and overlapping
uploads on another CUDA stream. Its example uses an RTX3060 12GB and2048-token
physical batches, unlike our measured profiles. It also has a separate hybrid
expert-cache implementation. The reported token identity and speed gains are
publisher claims, not locally verified results. Pinning the full host expert
span conflicts with our need to leave applications open and restrict resident
RAM; do not enable these flags just to chase the headline. Selective pinning,
actual committed/resident memory and an identical-artifact comparison would
need investigation before a local trial. No fork build or inference occurred.

Both README revisions and SHA256 receipts are retained in ignored research
evidence. These are additional engine leads, not new model scores, and do not
replace the currently running Gemma or queued higher-precision Flint trials.

## Post-training for shorter useful reasoning

[ThinkingCap Gemma26](https://huggingface.co/bottlecapai/ThinkingCap-gemma-4-26B-A4B-it)
is a separate post-trained checkpoint, not a reasoning-effort flag or another
quantization of our current weights. Its publisher reports38.9% fewer thinking
tokens averaged across twelve benchmarks, with macro accuracy75.0% versus75.2%
for the base. The long-context results vary by task; equal average accuracy
does not mean every capability is preserved. Their setup uses GB300, vLLM,
DFlash and65K output ceilings, so these numbers predict neither our wall time
nor instruction-file accuracy. A16.6GB MXFP4_MOE GGUF is linked, but has not
been downloaded, pinned or locally tested here. This is a future candidate
specifically motivated by our reasoning-only limits. It does not replace the
remaining campaign's frozen model trials, and its advertised savings are not
credited to the original Gemma26 results.

## Gemma reasoning-control names need literal inspection

The loaded Gemma template reports `supports_preserve_reasoning=false`, yet
explicitly implements a different keyword, `preserve_thinking`. Its gate keeps
reasoning after the most recent user turn, and optionally older tool-call
reasoning when that keyword is true. It does not preserve every old final
answer's reasoning indefinitely. Thus the generic capability field alone is
not proof that this model ignores its actual control. The saved private request
contains `preserve_thinking=true` and carries the prior assistant's reasoning
field and tool call. The loaded template separately supports `enable_thinking`
but not effort levels. These observations come from the exact saved template
and request, not a new rendered-prompt or inference-equivalence test. They also
do not imply persistent memory after unloading or automatic file discovery.

## Recheck26October: generation gains do not erase file-processing time

[Hybrid-cache PR30594](https://github.com/ggml-org/llama.cpp/pull/30594) remains
open at head `9177f038969a1e272e6187d26d12223b62cb852e`. The author reports
roughly1.7x generation on an8GB laptop with88GB RAM, but unchanged prompt
processing. Its hybrid path handles single-token batches; speculative
verification does not benefit and can be slower. Numerical checks are useful
but do not establish this lab's code quality or bit-identical answers.
The API body/revision/hash are preserved locally. This branch is not installed.

Our Gemma private run spends381.5s on fresh prefill and416.4s on generation.
Even a hypothetical1.7x decode gain with unchanged prefill would reduce the
798.6s workflow to roughly626s, not470s. This arithmetic is an illustrative
bound, not a Gemma-compatible measured speedup. Prioritize measured prefill,
source-read correctness and retained-prefix reuse alongside decode throughput.

The rechecked [Strata0.2.4 release notes](https://github.com/Niko1221/Strata/releases/tag/v0.2.4)
describe later DeepSeek launch/install updates while explicitly leaving Qwen
engine packages unchanged. Do not assume the terminal version alone repairs
our earlier Qwen engine limitations. No new Strata runtime trial is claimed.
