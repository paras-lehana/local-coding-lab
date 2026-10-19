# Supplied azllm article: provenance and claims

Received19 October 2026 as pasted text. Author: Andrew Zhu (xhinker). Title:
“An Inference Engine Nobody Has Heard Of, Runs Qwen 3.8–27B at 207tok/s on One
RTX3090Ti, Full262k Context”. The paste says “4days ago”; an exact publication
timestamp and canonical article URL were not provided. Do not infer a date.

The full paste contains third-party prose and account/UI material. It is
retained privately; this public record contains an attributed claim inventory,
not a republication. External claims below remain unverified on this host.

Primary implementation links:
- [azllm](https://github.com/xhinker/azllm), the article author's serving fork.
- [tqllm](https://github.com/turbo-tan/tqllm), underlying inference engine.
- [llama.cpp-tq3](https://github.com/turbo-tan/llama.cpp-tq3), separate compatible engine.
- [TQ3_4S artifact](https://huggingface.co/YTan2000/Qwen3.8-27B-TQ3_4S).
- [Other TQ artifacts and drafter](https://huggingface.co/YTan2000/Qwen3.8-27B-TQ).

## Claims to evaluate

| Claim | What a local reproduction must establish |
|---|---|
|207decode tok/s on 3090Ti; 333on5090|Same model/format, draft mode, sampling, input/output lengths and timing definitions; never predict3080 speed from this.|
|262144configured context|Actual occupied tokens, successful retrieval and memory, not just a launch flag.|
|14.5 GB TQ3_4S weights plus0.79 GB drafter|Exact revisions/hashes, resident buffers and additional scratch/head allocations.|
|Low-bit KV provides long context|Quantization changes cache representation, not weight capacity or client file delivery.|
|Speculation matches target greedy output|Compare generated token IDs with/without drafts under the same arithmetic; not BF16 quality equivalence.|
|Large warm-prefix speedup|Repeat the exact prefix, then change a middle file and verify invalidation/reread.|
|Tool-schema replies stream normally|Measure actual content deltas and complete tool arguments/results in the client protocol.|

See the [critical review](../../reviews/2026-10-19-azllm.md) and
[local experiment](../../../experiments/azllm/README.md).
