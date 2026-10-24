# Higher precision and practical offload improvements

Reviewed 24 October 2026 for RTX 3080 10GB, Ryzen 7 5800X, 64GB system RAM,
Windows and an apps-open desktop. This is an engineering assessment; measured
outcomes live in the [precision campaign](../../docs/tasks/2026-10-24-precision-and-gaps/2026-10-24-precision-and-coverage-v0.9.0.md).

## Recommended order

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
