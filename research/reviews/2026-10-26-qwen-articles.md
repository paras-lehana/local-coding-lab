# Seven Qwen articles: evidence, corrections and experiment decisions

26October2026; research in progress. Original pasted articles are archived with
SHA256 identities in ignored `local-data/2026-10-26-articles/`; they are not
republished. This review is original analysis. Publisher claims, our previous
measurements and new trials are different evidence classes.

## What matters for this PC

The objective remains correct coding grounded in `.github`, `.claude`, linked
instructions, source files, documentation and changing long chat history.
The RTX3080 has10GiB dedicated VRAM and Windows reports63.91GiB physical RAM.
Those are separate pools. At17:44IST,12.34GiB RAM,11.10GiB commit and5709MiB
device VRAM were available. Installed capacity is not available model capacity.
Keep units explicit too: model repositories often show decimalGB, while these
Windows measurements useGiB. The decisive question is each allocation and the
current free capacity, not a rounded74-versus75 headline.

Read-only storage inventory confirms E: is a463,316,447,232-byte volume on a
WD_BLACK SN7701TB NVMe SSD. This is suitable for investigating SSD-backed
lookup/weight reads, but no fresh storage benchmark was run during inference.
The physical disk's1TB capacity does not give this volume1TB of free space.
Actual available volume space, native packing overhead and measured read
behavior still determine the download/serving plan.

No llama/Strata engine remained loaded. Ollama was running but its `/api/ps`
returned no models. VS Code and Edge were the largest resident process groups,
about10.35/8.70GiB respectively; these working sets include shared pages and
must not be summed as exact exclusive usage. Windows' available-memory count
already includes reclaimable standby pages. Emptying standby would mostly
change its label, not add a second12GiB pool. No apps were closed or cache purged.
[Microsoft's memory definitions](https://learn.microsoft.com/en-us/windows-hardware/test/assessments/results-for-the-memory-footprint-assessment).

A second observation during Gemma's history run, at 22:43-22:44 IST, makes the
physical/commit distinction concrete. VS Code has about 11.50 GiB summed working
set and 18.45 GiB private commit; Edge 8.11/16.38 GiB; the QEMU emulator
1.47/6.81 GiB; the single Gemma engine 5.00/4.97 GiB. Working sets overlap shared
pages, and private commit can reside in RAM or the pagefile. System commit is
about 102.04 GiB against a 106.33 GiB limit while about 8.57 GiB physical RAM is
available. Thus available RAM alone does not authorize another allocation.
These snapshots do not establish a leak or attribute all remaining system
commit to a driver. No applications were stopped. The
[sanitized counters](../../reports/2026-10-26-memory-during-gemma.json) preserve
the different sampling times and omit process IDs and host paths.

The owner clarified latency: a plain greeting taking ten minutes fails the
practical check; useful instruction-heavy coding may take longer. Preserve
the old1200second scores, and label extended trials separately. Prefill cost,
reasoning length and generated-token rate differ: a slow greeting does not
mathematically imply days for every coding task, but it warrants investigation.

The article's75GB number is now verified against
[Unsloth's guide](https://unsloth.ai/docs/models/qwen3.8-next): it recommends
96GB for headroom, describes a75GB smallest quant and permits SSD-backed n-gram
offload. Its hardware table combines RAM/VRAM, but that does not override the
individual allocation requirements of a particular engine. Also, its roughly
80% top-1 figure is token agreement, not80% coding correctness. Our inference:
use smaller GSQ transformer storage and sparse SSD dictionary reads, then
measure actual free-memory floors; do not force a75GB resident allocation.

## Article-by-article assessment

| Article | What it argues | Assessment for our experiments |
|---|---|---|
|1. The Censorship Switch Strata Hid in Its Own Repo, Andrew Zhu,2Oct|A so-called speed projection removes a refusal direction; changed answers create misleading speed comparisons|Keep it off for the coding baseline. It changes the model's output distribution, not just execution speed. We have not observed refusal as the main cause of our coding failures.|
|2. Qwen3.8–27B with RTX3090, Jatin Prasad,15Aug|Dense27B can offer strong coding and long context on a24GB card, with thinking controls and MTP|Worth retaining as a quality candidate. Its fully-GPU throughput does not transfer to our partial-offload10GB setup. Separate quant, native effort and engine effects.|
|3. I Read Qwen's28-Page Report, Loengnavy|Flash-Next moves a large n-gram lookup table off accelerator, enabling RAM/SSD-oriented serving; cites75GB combined memory|The architecture is real and relevant. The75GB sizing claim is a deployment recommendation, not a result of the architecture paper or a guarantee with apps open. Reopen Flash-Next using measured placement, not installed-memory addition.|
|4. Qwen3.8–27B,177TokensPerSecond,OneRTX3090, Andrew Zhu,15Sep|Patched vLLM, smaller heads/drafter, KV formats and prefix reuse improve dense27B serving|The repository is now HyperQwen. Its current default headline differs from the article. Single-stream decode, concurrent throughput and prompt-copying rates must remain separate.24GB residency is the principal obstacle here.|
|5. Can Qwen3.8–27B Run in3GBVRAM?, Gavin Li,19Aug|AirLLM streams layers and demonstrates BF16 inference with3.33GB peakVRAM|Useful capacity experiment, not demonstrated instruction-heavy coding. Disk capacity, layer transfer on every generated token and growing cache still matter. It offers a possible high-precision diagnostic after disk budgeting.|
|6. Flash-Next:WhichQuantFrom16GBto128GB, Ankit Agrawal,9Oct|Compares GSQ-RCO/Unsloth quants, RAM tiers, Strata speed and failure modes|A valuable starting matrix. Its categorical no-Mac/one-model statements are now stale. GSQ-RCO Q2_0 is a new quant for this lab; prior Flash tests already used GSQ-RCO IQ3_XXS, not Unsloth.|
|7. A27BModelat92TokensaSecondona16GBGamingCard, Micheal Bee,10Sep|Embedded MTP, smaller batches and KV compression raise throughput on5070Ti|The current recipe uses a different modified checkpoint and custom sm120 kernels. Keep checkpoint changes separate from runtime optimizations; do not import a16GB recipe unchanged or claim it fits10GB.|

## Primary-source checks

### Flash-Next architecture versus the75GB claim

The official model card describes125B backbone parameters,6B active, plus51B
n-gram embeddings and4B MTP. Thus125B and roughly176B descriptions count
different components. Native context is262144; maximum configured context is
not recall accuracy. [Qwen model card](https://huggingface.co/Qwen/Qwen3.8-Flash-Next).

The28-page paper was downloaded from Qwen's repository at
`69885871a64393807d988b27b1b5e380e8f28526`; PDF SHA256
`04f263446d74a35cb7cea368574e0c561f3b05c133be2c777ac884404063655d`.
Its introduction and sections2.1.2/2.3 were inspected directly. Predictable
n-gram lookup allows host prefetch at layer2. Its7.6x/4.9x figures are
attention-module prefill/decode speedups at1Mcontext, not whole-agent speed.
The vocabulary ablations also show that better loss need not improve downstream
tasks. That supports measuring real file routing and code behavior here.
[Technical report](https://github.com/QwenLM/Qwen3.8-Flash-Next/blob/69885871a64393807d988b27b1b5e380e8f28526/tech_report.pdf).

Further inspection covers the retrieval evaluation on page8 and the base-model
comparison/conclusion on pages22-23. The paper reports strong RULER results,
but eight-needle MRCR falls from95.98 at128K to40.53 at512K and26.44 at1M
for QSA. That is direct evidence against interpreting a large context setting
as reliable recall of every instruction. Table11 favors Flash-Next over dense27B
on the reported base-model tasks; it does not compare our post-trained low-bit
artifacts, editor scaffolds or linked-file workflows. The training-stability
experiments also do not establish Windows hardware stability. This remains a
targeted reading of relevant sections, not a claim to have reviewed all28pages.

We must distinguish the n-gram weights, expert-weight cache, KV/recurrent state,
prompt-prefix reuse and the editor's retained transcript. The n-gram table is
learned model data, not a persistent store of the user's instruction files.
Putting KV in RAM does not make omitted files visible or prevent client pruning.

Two cautions from the supplied architecture article deserve explicit labels.
Its four-H200 SGLang figures (84to60GB weights,78% more KV room,0.07% throughput
change) are not verified here; the article itself says it could not locate
those figures in SGLang documentation. The current official cookbook supports
offload but does not by itself corroborate that experiment. Also, file-backed
cache does occupy physical memory while resident; reclaimability is different
from having zero memory cost. Unified-memory machines cannot count their shared
RAM once as system memory and again as additional VRAM.
[Official SGLang recipe](https://github.com/sgl-project/sglang/blob/main/docs/cookbook/autoregressive/Qwen/Qwen3.8-Flash-Next.mdx).

### Quant choice for the next Flash trial

GSQ-RCO Q2_0 has37.624GB transformer and28.800GB lookup shards,66.424GB total
(61.86GiB). The previous GSQ-RCO IQ3_XXS transformer shard was47.040GB.
Q2_0 therefore saves9.416GB of transformer storage, a material new test rather
than an unchanged retry. Its publisher LiveCodeBench result is81.14 versus
86.29 for IQ3_XXS and87.43 for BF16. This is a meaningful precision tradeoff,
not evidence that two-bit universally breaks syntax or that three-bit cannot
code. Sensitivity-aware tensor allocation matters alongside nominal bit width.
[Quantizer's model card](https://huggingface.co/ISTA-DASLab/Qwen3.8-Flash-Next-GSQ-RCO-GGUF).

Our priority is instruction accuracy. Q2_0 is the capacity/control experiment;
IQ3_XXS or IQ3_S remains the quality follow-up if a bounded memory recipe
completes. Shared n-gram shard identity permits later reuse, but the previous
copy was retired and must be fetched again. Do not download two independent
copies of the identical shard merely because their directory names differ.

### Strata has changed; platform distinctions matter

Source inspected at`4b9e05a2a806a3fe24f7b2560d98626c37dade35`.
Latest app release0.2.6 ships Qwen engine0.1.50, unchanged from app0.2.5;
this is newer than our0.1.45 experiment. Current documentation includes Mac
and other model families. Low-RAM mappings/bounded resident experts remain
relevant, but Linux zero-copy/file-tier prefetch improvements do not establish
a Windows gain. Dynamic KV growth has restrictions and is not interchangeable
with host-streamed KV. [Engine reference](https://github.com/Niko1221/Strata/blob/4b9e05a2a806a3fe24f7b2560d98626c37dade35/docs/DETAILS.md),
[release identity](https://github.com/Niko1221/Strata/releases/tag/v0.2.6).

Disable the separate parked-conversation cache during initial fit: its default
can use up to8GiB host RAM beyond the live context. Later prefix-reuse tests
need an explicit cache budget. Also record`answer_room`: by default the frontend
wraps up thinking before a finite output cap is exhausted, even when no explicit
reasoning budget is supplied. These controls affect memory and completion;
the engine flags alone do not describe the actual serving configuration.

Our previous10GB tests already demonstrated RAM-backed128K cache through51K
input, including1.55GiB host KV. They also demonstrated four coding deadlines
and an empty final response; successful separate recall replays do not erase
those failures. See the [measured Strata report](../../docs/tasks/2026-10-18-strata/2026-10-18-strata-on-10gb-v0.6.0.md).
Keep route-tail skipping disabled in accuracy controls. More GPU allocation
can reduce performance when Windows spills device allocations to shared RAM.

A specific next control targets our empty final: the frontend's opt-in
`reasoning_close_retry` closes an unfinished thinking segment and continues
once when the model otherwise stops without an answer or tool call. This
already existed before engine0.1.50; it is not a new-engine performance claim.
It is off by default and consumes the remaining output budget. Count both
segments in whole-request time and report off/on as different scaffolds.
Our old record has empty content, `finish_reason=stop` and unused output room,
which is consistent with the reported symptom; it does not prove the parser
state or establish this as our root cause. Test normal greetings, changed-file
tools, long history and literal thinking tags before adoption.
[Reported failure](https://github.com/Niko1221/Strata/issues/1053),
[pinned implementation](https://github.com/Niko1221/Strata/blob/4b9e05a2a806a3fe24f7b2560d98626c37dade35/serve/server.py).

The projection package explicitly confirms a behavioral intervention with a
small same-text processing cost. Its measured quality shift is an additional
reason to keep it outside our baseline. [Package description](https://github.com/Niko1221/Strata/blob/4b9e05a2a806a3fe24f7b2560d98626c37dade35/data/experimental-speed-projection/README.md).

### Dense27B acceleration and minimal-VRAM streaming

HyperQwen source`ce9615c4f2309be727407918a6c979bd67968069` targets a measured
24GB setup. Its newer results distinguish single-user, concurrent and
prompt-reproduction workloads. References to3080 measurements include two
20GB cards; they are not evidence for our single10GB card. The roadmap still
lists smaller checkpoints for12/16GB cards. [HyperQwen](https://github.com/syv-ai/HyperQwen/tree/ce9615c4f2309be727407918a6c979bd67968069).

The5070Ti recipe at`754e7adc6190b5a1861e521e1397e951140cf834` now uses a
12.120GB modified IQ3_S checkpoint, compressed KV and custom kernels tested
on sm120. Our3080 is sm86. This is a different model/runtime from the early
article. [Pinned recipe](https://github.com/feveromo/recipes-qwen3.8-27b-5070ti/tree/754e7adc6190b5a1861e521e1397e951140cf834).
The cited MTP issue27296 was closed as stale/not planned on24October, which
is not proof of a fix. Add alternating short/long requests and tool-call
integrity checks before promoting an MTP profile.
[Issue history](https://github.com/ggml-org/llama.cpp/issues/27296).

The article's ATX lead resolves to
[llamAmpere](https://github.com/JakeATX/llamAmpere/tree/5c9c97aa8cc1ebb8b7a8af68334c368f7b7e89ef).
Its current Linux12GB recipe uses a different Swift1.5 2.3bpw checkpoint,
compressed KV/recurrent state and MTP; the cited large-context run peaks at
12052MiB whole-device. This is closer to our capacity than24GB recipes but
still does not fit our10GB card as published, particularly with desktop VRAM
occupied. Partial offload/smaller context could be a distinct calibration.
Compare its modified weights separately; it is not a high-quant baseline.

AirLLM source`bc7ded5b7ddf798ef386735a44932c19a571f01d` supports the dense
hybrid architecture. Its implementation retains the vision tower and streams
decoder layers; its README warns that splitting checkpoints uses disk and has
an explicit original-deletion option. It now also documents adapter training,
so a blanket claim that it cannot fine-tune would be wrong. Neither support
nor a tiny generation demo establishes our long-file quality or throughput.
[AirLLM](https://github.com/lyogavin/airllm/tree/bc7ded5b7ddf798ef386735a44932c19a571f01d).

## Experiment order and what success means

The transferable lesson is to separate three kinds of change. Exact placement
and cache reuse aim to execute the same model with less transfer or recomputation.
Weight/KV quantization changes numerical precision. Expert pruning, route
skipping, refusal projection and forced reasoning closure change the computation
or response process more substantially. Report their quality results separately;
an attractive token rate does not identify which change produced it.

For instruction-heavy coding, the chain to verify is: the client includes the
entry instructions; the model follows their links through tools; successful
reads deliver the necessary ranges; the active transcript retains those facts;
the final code follows them. A larger KV allocation addresses only part of this
chain. Our changed-file and absent-fact questions matter because a large cache
can retain stale or incomplete information just as efficiently as useful input.

For this3080, prioritize usable expert residency and q8/int8 context before
optional drafting or more aggressive KV compression. Dynamic KV growth is
interesting only where the runtime supports the chosen RAM/SSD mode. The new
Strata requirement for all experts to fit RAM rules out assuming its dynamic
mode works with our bounded partial expert cache. A static host-KV allocation
can still serve increasing occupied context; measure both quantities.

1. Test the now-verified higher Flint quant and finish missing Gemma/K2
   qualification where a genuinely smaller allocation fits current headroom.
2. Separate plain greeting from the frozen file-driven cases. Keep completed
   answers, exact requests, timings and hardware telemetry. Extended native
   reasoning trials are separately labelled; no false1200second pass.
3. Stage Qwen engine0.1.50 separately. Try Flash-Next GSQ-RCO Q2_0 with bounded
   host expert residency and the n-gram shard on SSD, then test long context
   with int8 host KV. Preserve the original working Qwen3.6 Q4 file.
4. Compare no-draft versus MTP only after load/greeting/file tools work. Measure
   whole-task time and output correctness, not draft acceptance alone.
5. Revisit dense27B with a supported partial-offload recipe and native effort.
   HyperQwen's24GB recipe and AirLLM BF16 are research leads, not installed or
   locally validated improvements. Disk/host budgets must be explicit first.

The separate Windows engine0.1.50 archive is now hash-verified and extracted;
it has not loaded a model. Flint UD-Q3_K_XL is also fully hash-verified.
Gemma26's smaller4GiB resident calibration loads in20.56seconds and answers
plain native-thinking greetings in12.77 and8.20seconds. Its two completed coding
cases pass105/105 and34/34 frozen checks, but the separate NaN TTL diagnostic
fails. The calibration was intentionally stopped; its partial DAG is unscored.
A6GiB resident control recollects all twelve cases with unchanged inference
arguments and completes21:25IST. This is API evidence, not an editor test. Do not
promote any candidate from these articles alone. Every missing experiment must
retain its concrete capacity, compatibility or evidence reason in the model
report rather than silently disappear from the queue.

At20:06IST five answers from the6GiB control are complete. Intervals and TTL
match their4GiB outputs exactly and take about28-29% less time. CSV needs35m35s
and18227generated tokens to deliver code, while scheduling takes4m15s. CSV's
visible source has a likely newline-state defect awaiting isolated checks.
Thus allowing more time can recover a final answer without guaranteeing better
code. The64K Gemma context allocates812.81MiB of GPUq8KV at startup; occupied
tokens change without an equivalent new allocation for every token. Neither
the article's generic memory formula nor nominal bit width predicts all of
these outcomes. Final grading waited until the unchanged full suite stopped.

The completed isolated result is10/12 frozen task passes. CSV fails16chunk
variants of one quoted/newline case; TypeScript has an actual function-type
syntax error. Additional, separately reported checks expose NaN TTL acceptance
and worker scheduling after a synchronous failure; deep merge passes the
array-replacement edge. Median task11m51s, plain greetings10.9/6.7seconds,
and no new hardware event. This supports reporting completion, speed, syntax,
behavior and instruction grounding separately; it does not promote Gemma above
Qwen for the owner's linked-file workflow. Earlier public/private scores use
a different profile and cannot fill missing components here.
[Complete coding evidence](../../reports/2026-10-26-gemma-resident6-coding.json).
