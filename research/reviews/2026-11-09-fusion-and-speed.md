# Fusion and speed article review

9 November 2026. Companion to [articles.md](../../articles.md), rows A11/A13.
This is source review and experiment design, not a new model quality result.

## Sources actually recovered

The full fusion article by Nikhil Varma was recovered from the historical
21 October browser result in the private Claude session. Its extracted text
has 8,831 characters, SHA256
`84612fdecd596aa51cfbd622d6a440fe7a3cda91ac83fc2935ea84d0c0899644`.
The complete text and pasted code were read. Public
[article link](https://levelup.gitconnected.com/i-fused-3-tiny-local-models-to-beat-single-model-limits-without-weight-merging-b17bba9c7e45)
omits the access query. No third-party full text is republished here.
The capture identifies October2026; a relative publication age is insufficient
to assign an exact publication date.

The new speed article by Anubhav was read from the owner's complete attachment:
[Why Is My Local LLM So Slow?](https://medium.com/data-science-collective/why-is-my-local-llm-so-slow-half-of-it-you-can-fix-tonight-da7283a8adf6).
Its proposals are checked against the installed source and existing telemetry.

The [Flint publisher page](https://recursive.com/updates/introducing-recursive-flint)
was checked again9November. Its128K speed figure explicitly excludes prefill;
its agent evaluations allow up to five hours and average multiple attempts.
Those conditions explain why the headline cannot predict first-answer delay
or this single-seed file audit on a10GB partly offloaded desktop. They do not
invalidate the publisher's separately defined measurement.

## Fusion: what survives review

Selective token ensembling is a real research direction. The
[SAFE abstract](https://arxiv.org/abs/2510.15346) studies ensemble positions,
tokenization mismatch, consensus and probability sharpening; it reports gains
on its own benchmarks with fewer than one percent of tokens ensembled.
[UniTE's abstract](https://arxiv.org/abs/2410.03777) emphasizes compatible model
selection and the union of top-k predictions. These abstracts were read, not
the complete papers. Neither validates this article's exact three7B recipe
or our file-heavy coding workload.

The article combines Coder/Math/Instruct7B checkpoints with weights
0.55/0.25/0.20 and a lead-model entropy threshold0.65nats. It provides a code
example but no comparative task-results table. An entropy trigger does not
establish that the lead model is wrong or that the auxiliaries will correct it.

Its central normalization explanation is mathematically incorrect for the
implemented weighted product. For token j and model i:

```text
log_softmax(z_i)[j] = z_i[j] - log(sum_k exp(z_i[k]))
sum_i w_i log_softmax(z_i)[j] = sum_i w_i z_i[j] - C
```

C is independent of j. Taking the final softmax (including its common
temperature) or argmax therefore gives the same result as weighted raw logits,
apart from numerical effects. Log-softmax does not calibrate differing model
temperatures/scales in this construction. Calibration would require a separately
specified and validated intervention, not this algebraic normalization.

Other implementation limits:

- Equality of `get_vocab()` is a useful necessary check, not proof of matching
  normalization, merge rules, special-token handling or chat templates.
- Auxiliary models run in a Python loop without explicit concurrent CUDA-stream
  dispatch. Processing an unseen token block is batching, not proof of parallel
  execution across models. The first auxiliary call may process the entire prefix.
- Entropy `.item()` requires a host-visible scalar; its synchronization overhead
  needs measurement. Auxiliary KV catch-up still costs compute and memory.
- Three nominal7B4-bit bodies need roughly10.5GB before metadata, non-quantized
  tensors, compute buffers and three KV caches. This exceeds the measured free
  device capacity on our desktop. Automatic placement is not a fit guarantee.
- Skipping auxiliary calls on most tokens does not eliminate their weight/KV
  storage or eventual prefix processing. The supplied code has no robust
  admission, cancellation, context-budget or tool-protocol implementation.
- Blanket claims that weight merging destroys specialists, or that this recipe
  beats a large model on domain precision, are unsupported by its measurements.

## Fusion experiment decision

Do not install three7B checkpoints merely to reproduce an unvalidated headline.
The bounded first stage is tokenizer/template compatibility plus a tiny,
same-vocabulary implementation control: prove no-token-delta errors, identical
single-member behavior and correct EOS/cancellation. Only after that should a
fully pinned, resource-qualified ensemble compare each member separately,
weighted fusion and entropy-gated fusion on the same held-out tasks. Record
prefill, auxiliary catch-up, gating fraction, final-answer correctness, tool
behavior and peak aggregate memory. Member weaknesses and correlation matter
more than a model-count headline. No inference in this design has run yet.

## Speed: useful hypotheses versus this machine's evidence

Separating prompt processing from token generation is useful. It is incomplete
to measure only first visible text for a thinking model: hidden reasoning can
occupy most of that delay. Flint's new greeting control takes85-96seconds with
first visible text at68-79seconds, despite a three-token prompt. These requests
both report zero cached prompt tokens; the second is not a measured cache hit.

The existing historical audit found222fully reused and2partially reused Qwen
continuations out of224, with no complete re-prefill in that subset. Its
19.4second loss estimate is0.057% of prefill **plus decode** time. Across the
broader audit, four editor divergences account for578.3seconds, or8.3% of the
audited editor prefill. This is Claude's historical log analysis, not a freshly
recomputed benchmark or proof that current editor traffic has no cache issues.

Installed b12069 defaults are logical batch2048 / physical microbatch512.
Our constrained profiles deliberately use much smaller values. The server
checks KV shift support before enabling near-match cache reuse. This is not a
ban on every hybrid model: recurrent memory returns true in this source and
the hybrid implementation delegates to attention. Full-prefix hits,
checkpoint rollback and reusable changed chunks must be measured separately.

The initial plan, subsequently completed below, tests microbatch4/16/32/64 with unchanged
weights/placement/context, then a separately labelled expert-cache increase.
Use a fixed long prompt and cold/repeated/changed-middle variants; record actual
cache counts, processed tokens, memory and full completion. Increasing directly
to2048 without a fit measurement is unjustified. Full-GPU residency, MTP or
file-size/bandwidth arithmetic cannot substitute for those measurements.

The six new b12069 tiny-model stock/default/opt-in controls establish limited
loader compatibility. They do not yet establish a full-model performance gain.

### Cache observability and the microbatch boundary

Further source inspection covers both pinned b11838 and b12069
`src/llama-moe-cache.cpp`. Direct slot-map use stops above32tokens per
microbatch, or when selected expert demand exceeds its slots. Large batches
can copy already-cached experts without updating that cache. Consequently,
microbatch64 is also a cache-path boundary; a larger batch does not guarantee
more GPU cache benefit. Measure prefill and decode separately.

The actual Flint metadata makes the smaller-cache issue more specific:
`n_expert_used=6` and `n_expert=256`, with cached groups of36/86/61slots.
For a full16token microbatch, the source's demand bound is96slots, larger than
all three groups. That path is ineligible even below the32token boundary.
A newly prepared microbatch4 control needs24slots and is eligible in all
three groups; two uncached layers remain. Eligibility is not a hit-rate or
speed measurement. Larger batches may still copy already-cached experts.
The1536MiB control separately tests greater cache capacity at microbatch16.

The earlier capped private run requests256MiB but actually allocates243.08MiB of expert
cache; cached groups have1.6% slot coverage and two layers have none. Capacity
is not a hit rate. Its1071MiB global KV and27.89MiB sliding-window KV are
separate from this expert-weight cache.

Both inspected sources print expert hit/miss counters when the cache object
is destroyed. The lab's ordinary Windows terminate path may skip destructors.
For the seven original performance profiles, a uniform60second native idle timeout
allows model destruction **after** the three timed requests. The validated
controller requires both passive sleeping status and cache-stat log lines;
unexpected sleep between requests invalidates the comparison. Missing counters
are an explicit metrics gap, not an invented zero hit rate. Idle observation
time is outside request latency. All seven initial controls subsequently
observed these statistics and stopped normally; production's1800second setting
and the original private-audit profile are unchanged.

The exact three synthetic request bodies are now public in
[native-prefill-v1](../../benchmarks/fixtures/prefill-native-v1/README.md).
The private controller requires identical request values before launch
and records the fixture hash. This is a small native-completion control,
without a chat template, rather than a replacement for the source-reading audit.

The sequence also repeats its initial u16/resident1 control at the end.
The earlier private audit's generation rate changes while its profile stays fixed;
desktop load, source/token mix and cache state can all confound a one-pass
timing comparison. The repeated control helps expose drift, but does not turn
a single exploratory sequence into a general hardware-speed claim.

### First live changed-prefix observation,9November

The u16/resident1 cold request takes267.437s; its identical repeat takes9.641s
with1894cached/1fresh token. Changing only the middle marker then produces a
real full re-prefill. Native logs explicitly reject all three saved checkpoints
because their sliding-window ranges begin after the required rollback boundary.
This is observed behavior of this small native fixture, not a private-audit
failure or a general claim that prefix caching is broken.

In pinned b11838 `tools/server/server-context.cpp:4437-4471`, ordinary
mid-prompt checkpoints are skipped unless a batch starts a user-message span
or is near the prompt end. This native fixture has no chat-message spans.
Consequently, increasing checkpoint count or decreasing minimum spacing alone
does not create an earlier snapshot in this control. Source analysis prevents
treating the historical proposed16checkpoints/2048MiB cache combination as a
proven repair. A future matched short-context `--swa-full` pair or a separately
frozen multi-message fixture can investigate rollback; neither has run yet.
Full SWA at72K would add substantial KV storage, so it needs a fresh allocation
estimate and admission instead of being enabled in production.

A later real-workflow observation is now separate from that synthetic example:
the native private audit's turn06 restores a checkpoint and reuses 38,371 of
46,388 input tokens after a long reasoning/tool turn. This is partial replay;
the precise prompt/token divergence remains unconfirmed. Its threshold log
is not the common-prefix length. See the
[interim measurement](../../reports/2026-11-09-flint-native-rollback-observation.json).
This qualifies the earlier full-prefix observations in this run without
overwriting the completed capped audit's eight full-reuse continuations.

Prepared9November, not run: a matched2K-context pair at b64/u64,
cache1536/resident3, with `--swa-full` as the only within-pair difference.
The1895-token fixture plus32output tokens fits that context. Head geometry
predicts57.640625MiB of windowed KV versus104.125MiB of full storage, before
alignment/checkpoints. The unchanged conservative gates leave room for this
bounded experiment. Measure actual buffers, rollback logs, reused/fresh
tokens and timings; neither a partial cache hit nor a truncated32-token
answer establishes long-context semantic recall.

### Completed smaller-microbatch control

u4/resident1 completes cold514.454s, repeat8.859s and changed-middle524.047s,
versus267.437/9.641/259.765s for u16. Both stop normally with no new hardware
event. Both native destructor summaries report zero hits in the <=8bucket;
u4 reports908681misses and1188939.28MiB uploaded, versus29581misses and
38662.98MiB at u16. The u4 bucket includes much more prefill, so its counts
are not an isolated decode comparison. Uploaded bytes are this component's
reported expert-transfer volume, not SSD reads or total GPU bus traffic.

This rejects the simple idea that entering the direct expert-cache path must
improve latency. The source groups slots across compatible layers. The total
15770MiB host expert store with6of256experts selected per layer corresponds
to roughly369.6MiB of selected expert weights for one token, before other
buffers; the actual cache holds243.08MiB. That is a plausible thrashing
explanation, not a measured universal minimum or a cache hit-rate prediction.
The completed1536MiB control below tests a meaningfully larger cache. Preserve
separate prefill/decode statistics and verify any combined setting directly.

### Larger-cache result and combined follow-up

The1536MiB budget allocates1531.97MiB, with slot groups23/223/522/23/373.
The three larger groups can now enter the direct path at microbatch16. The
completed trial reports31.07% hits for <=8and4.86% for >8; large-batch uploads
are780314.55MiB. Cold/changed prefill becomes325.497/298.401s, slower than
baseline255.572/246.239s. Generation improves to3.469/3.396tok/s in those
two requests, and the identical-repeat wall time is6.765s. Cache capacity,
dispatch and phase costs must all be considered together.

Separately, u64/cache256/resident1 completes cold175.953s and changed195.281s;
resident3 at u16 gives245.000/241.390s. These single runs motivate directly
testing combined resident3/cache1536 with u64 and then b128/u128 after the
original runtime control and baseline repeat. Both combined profiles are
prepared, unarmed and unrun. Their joint changes are explicitly not a pure
one-variable ablation; do not add the measured individual gains together.

The b12069/u16/resident1 full-model control subsequently completes
263.984/9.984/259.203s, with normal stop and no new hardware event. Its
fresh-input timings closely match b11838's initial267.437/259.765s. The
newer build therefore supplies no material speed improvement in this test.
The original-build baseline repeat completes261.641/9.735/263.781s, normal
stop/no new hardware event. Cold/middle wall times differ by less than2.2%
from the initial baseline; the u64 gain is larger than that observed drift.
This does not establish a confidence interval from a single sequence.

All three corresponding32-token text hashes match the initial baseline for
the repeat, resident3-only and b12069 controls. Microbatch4/32/64 and
cache1536 differ. Changed dispatch can change greedy continuations; complete
quality tests remain necessary. No full-logit or arbitrary-output equivalence
is claimed. The combined64 control started06:04IST after fresh admission.

The combined64 run completes191.937/5.296/149.844s, followed by
combined128 at128.406/5.171/97.157s. Both stop normally with no new hardware
event. Combined128 cold/changed prefill takes120.423/88.580s, generation
3.916/3.638tok/s; its repeated-input generation rate is6.358tok/s. The
middle edit still has zero cached tokens, so its improvement is processing
speed, not restored rollback. These gains justify qualifying an uncapped
private72K audit on the same combined128 placement, but no new quality
result exists. The separately matched short2K rollback pair began06:19IST.

That pair completes normally with no new hardware event: windowed cold/repeat/
changed191.922/5.359/145.562s; full-SWA194.547/7.922/95.562s. Actual total KV
is57.640625 versus104.125MiB, an extra46.484375MiB. Full-SWA reuses962tokens
after the middle edit and processes933fresh, versus zero reused/1895fresh.
It retains earlier state; it does not widen the model's trained attention
window. Cold and repeat do not improve, and all three short output texts
differ. Thus this is measured rollback/capacity behavior, not a general
speed or correctness win. The native72K/u128 private audit started06:37IST
without full-SWA, passed two greetings in57.907/37.672s, and is collecting.

The full-SWA result cannot be scaled to72K by copying one flag. Using the
measured four KV heads,128dimensions,q8_0 blocks and35SWA layers, the72K
SWA arena would be2677.5MiB instead of27.890625MiB; global KV remains1071MiB.
That adds2649.609375MiB, exceeding the native audit's roughly2125MiB free
VRAM even before its400MiB reserve. This is an allocation estimate, not a
failed load. CPU KV or a smaller expert cache is a different candidate profile.
Ordinary append-only continuations already retain the whole prefix here, so
full storage specifically addresses earlier-edit rollback, not every delay.
The older prepared/unrun paragraphs above document the original hypotheses.

Passive disk telemetry during the later native private audit adds a separate
observation: E: reads142.2–159.9MiB/s at0.114–0.134ms mean read latency,
with instantaneous queue length0–1. The process's288,288faults/s and zero
ordinary IOReadBytes/s cannot substitute for this drive measurement. The
four samples are not model-exclusive or a saturation test. See the
[receipt](../../reports/2026-11-09-flint-paging-observation.json) and
[memory-counter interpretation](../../docs/memory-and-context.md).
A same-flags combined128 residency3→6GiB control is prepared, not run;
fresh RAM admission rises to12.5GiB while the6.5GiB startup reserve stays.

### Current upstream follow-up, 9 November

[Strata0.2.12](https://github.com/Niko1221/Strata/releases/tag/v0.2.12),
released7November, packages engine0.1.58. Its release notes report faster
prefill on a12GB card, but also workload-specific regressions. The12GB
file-tier fix is explicitly Linux-specific; it is not proof of a Windows3080
improvement. The notes also list tool-parser, copy-ordering and long-CUDA-prompt
fixes. Their tests used candidate builds and changed automatic draft choices;
they are not a same-settings result on our machine. This is an additional
source-review lead, not an installed update. Preserve0.1.50 qualification
as its own experiment; review relevant changes and exact artifacts before
any separately pinned newer-runtime trial.

The actual pull-request descriptions and diffs narrow those fixes further:

| Change | Source evidence | Relevance and limit here |
|---|---|---|
| MMQ row-table padding, [PR5108](https://github.com/Niko1221/Strata/pull/5108/files) | Allocates and initializes extra rows for an otherwise out-of-bounds stream-k fixup read; the author's long-prompt CUDA reproduction passed after padding | Inspect this path before a long-context newer-engine trial. The reproduction used a different multi-GPU setup; neither our old restart nor a Q2/64-token prefill fault is established by it |
| Ordered DMA completion, [PR5096](https://github.com/Niko1221/Strata/pull/5096/files) | Empty upload groups now queue completion behind pending copies instead of advancing a cumulative flag early; the author reports nonfinite-logit failures disappearing in an A-B-B-A control | A correctness change can matter more than a headline decode rate. Our pinned0.1.50 path and exact mechanism still need comparison; no local reproduction or measured speedup claimed |
| Adaptive expert bookkeeping, [PR4844](https://github.com/Niko1221/Strata/pull/4844) | Corrects the range recorded when a pipelined adaptive round completes later in a serial path; source and reported test use resident experts, two pipeline windows and async adaptation | Our pending qualification disables async adaptation and uses one GPU/mapped experts. Do not attribute an observed desktop RAM change to this specific expert-loss bug |

These are upstream evidence, not extra locally tested models or reasons to
overwrite old results. The qualification's small explicit cache,64-token
prefill and disabled adaptation remain recorded controls. Any0.1.58 follow-up
must pin its artifact/frontend, retain explicit draft settings, check supported
flags and compare completed answers as well as timing.
