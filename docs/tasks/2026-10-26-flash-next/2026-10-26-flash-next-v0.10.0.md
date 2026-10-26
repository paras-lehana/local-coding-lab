# Qwen3.8-Flash-Next: refreshed quant and engine investigation

26October2026. Active research/installation; no new quality score yet.
This is the model-specific continuation of the
[18October Strata measurements](../2026-10-18-strata/2026-10-18-strata-on-10gb-v0.6.0.md).
The [seven-article review](../../../research/reviews/2026-10-26-qwen-articles.md)
holds article summaries, source revisions and distinctions relevant to other PCs.

## Why reopen it

The owner prioritizes precision, reasoning, linked instructions and long context,
and now permits extended coding diagnostics. Earlier20minute failures do not
prove the model cannot finish with a larger allowance. They remain failures in
their original cohort. A newer separately installed engine and a smaller
GSQ-RCO Q2_0 quant are explicit new variables. They need their own evidence.

## Historical result and limits

The previous artifact was **ISTA-DASLab GSQ-RCO IQ3_XXS**, two shards totalling
75,839,998,528bytes, not Unsloth's similarly named quant. Strata0.1.45 with
10/14GiB expert pools fit the10GB GPU but four coding attempts hit1200seconds.
Measured capped decode improved from5.9-6.7 to8.8-9.6tok/s with the larger pool;
that was not a completed-code result or a clean causal timing comparison.
128K int8KV with32K GPU cells allocated1.55GiB host KV; the51K-input workflow
returned an empty final. Two separate final-turn replays recovered6/6facts.
Full shards were retired20October; pins and transcripts remain.

## New artifact identities

Repository`ISTA-DASLab/Qwen3.8-Flash-Next-GSQ-RCO-GGUF`, revision
`ed59f92082b1e93c0e96d60a8b11aab089b52f09`:

| Q2_0 shard | Bytes | SHA256 |
|---|---:|---|
|Qwen3.8-Flash-Next-GSQ-RCO-Q2_0-00001-of-00002.gguf|37623740192|69820c02ec7d0b45ef2ebb19d6620299db749fe2aded7f39f93c6b88b199b720|
|Qwen3.8-Flash-Next-GSQ-RCO-Q2_0-00002-of-00002.gguf|28800138432|316b46f3a2dbd68c900f43136ab9449f9dcc3725dfd8c794847c204bc161e113|

Both are under`Q2_0/`. The second is byte-identical to the old dictionary shard;
it is no longer on disk. Full files/hashes are required before a live load.
Q2 saves9.416GB of transformer storage versus oldIQ3XXS. Publisher coding
benchmarks favor IQ3XXS, so Q2 is a capacity/control candidate, not a declared
quality upgrade. IQ3_S is the later higher-precision option if resources allow.

Staged separate runtime: Strata Qwen engine0.1.50 from app release0.2.6,
Windows x86_64 CUDA13 archive581,368,579bytes, SHA256
`a9643e2f5dd5c62e734d2980484c320d41da0160fc4932bf638b7f34e38e74f5`.
Archive verified and safely extracted into a new directory; engine executable
SHA256`5745022e7c8f743cfee83544da7d3672cd86103c854f23600e2c69ddd6593bef`.
No new engine load or quality measurement yet. The old checkout/build is
preserved. App0.2.6's DeepSeek changes
do not imply a new Qwen engine versus app0.2.5.

## Profile and evaluation plan

- Start with a bounded expert-RAM pool sized from fresh physical and commit
  headroom, n-gram table on SSD, int8KV, one slot, and explicit device reserve.
- Disable the engine's additional parked-conversation cache for initial fit
  (`--conversation-cache-mib 0`). Its default can use up to8GiB more host memory;
  it is distinct from the live KV cache. Later prefix-reuse experiments get
  their own explicit budget. The container memory-limit flag governs parking,
  not a universal cap on model allocations or Windows commit.
- No route-tail skipping or refusal projection in the accuracy baseline.
- Plain greeting/no files first, cold and warm;600second practical ceiling.
- Freeze native effort/output limits and compare public instruction routing,
  strict TS/SQLite, changed-file/history and private source-citation audit.
- Record frontend controls as well as engine flags: high is the model's
  default effort, and `answer_room` normally reserves a quarter of a finite
  output cap by closing thinking early. Keep this behavior explicit; budget0
  does not mean an unconstrained answer when answer_room remains enabled.
- Long diagnostics may exceed1200seconds; report exact duration and do not
  import those scores into the old leaderboard.
- Only then compare MTP and64K/128K KV placement, recording allocated capacity,
  occupied tokens, resident pages, I/O and delivered final answers separately.
- Compare the existing frontend opt-in`reasoning_close_retry` off/on for
  empty-final recovery. It appends a thinking-close marker and permits one
  continuation within the remaining output limit; this changes scaffolding,
  not model precision. It predates0.1.50 and is disabled by default. The old
  empty-final trace is compatible with the reported symptom, but the root
  cause remains unproven. Include normal answers and literal tags as controls.
  [Issue1053](https://github.com/Niko1221/Strata/issues/1053) and
  [pinned source](https://github.com/Niko1221/Strata/blob/4b9e05a2a806a3fe24f7b2560d98626c37dade35/serve/server.py).

## Pros, cons and current disposition

Pros: sparse compute, predictable dictionary offload, native long context and
an engine with explicit RAM/SSD controls. Prior fit and host-KV use are measured.
Cons: expert paging competes for scarce RAM and disk bandwidth; strong publisher
scores have not translated into completed local coding workflows. Lower quants
can reduce task accuracy. Greater context does not fix missing file retrieval.
Current recommendation: **retest, not promote**. Existing Qwen3.6 Q4 remains the
preserved baseline. New Q2 weights/load/quality are unrun at this checkpoint;
available disk is below the full two-shard download plus headroom, so finish
and record current candidates before exact-file retirement creates room.
