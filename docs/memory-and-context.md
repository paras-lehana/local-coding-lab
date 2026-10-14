# RAM, VRAM, quantization and context

| Concept | Changes | Does not guarantee |
|---|---|---|
| Weight quantization | Stored parameter precision and footprint | Correct syntax or reasoning at Q6/Q8; automatic failure at 3-bit |
| KV/state precision | Representation of cached attention/recurrent state | Perfect recall of every file |
| Layer/expert placement | Which device stores and computes model components | A universal safe number of GPU layers |
| Context length | Maximum token workspace exposed to a request/slot | Permanent history or automatic instruction-file loading |
| Prompt/slot cache | Reuse of eligible computation/state | A durable searchable repository memory |
| GPU expert cache | Copies of CPU-resident experts cached in VRAM | Removal of the original CPU weights |

The actual Qwen3.6 32K diagnostic allocated **340 MiB attention KV** plus
**62.81 MiB recurrent state**. KV split was 68 MiB CPU / 272 MiB GPU. A simple
doubling gives 680 MiB attention KV at 64K; state does not necessarily scale
the same way. A generic claim that every model needs 16 GB KV at 32K is wrong.
Architecture, layers, heads, dimensions, precision, slots and backend all matter.

In the pinned runtime, `--no-kv-offload` requests host-side KV. GPU offload flags
do not mean "put KV in RAM." Moving this relatively small cache to RAM could
recover some VRAM but uses more host memory and may slow attention. It cannot
solve dense CPU matrix multiplication or a host-RAM shortage. These placement
experiments were prepared previously but **not measured** after memory stops.

`--gpu-layers all --cpu-moe` is a useful **proposal**: offload eligible non-expert
computation while keeping routed experts on CPU. It may increase host memory
because experts previously on GPU move back to RAM. Shared experts, embeddings,
output tensors and compute buffers must be checked from actual loader logs.
Do not label all layers equally sized or reuse a 28-layer limit across families.
See [pinned flag definitions](https://github.com/ggml-org/llama.cpp/blob/b2f036c0f138414dedc987446f1d9d802f920275/common/arg.cpp).

Context remains useful only when the client actually sends the relevant files,
instructions and history. A CLAUDE import, a Copilot instruction rule and an
ordinary Markdown link have different loading behavior. The benchmark records
exact source delivery and successful reads. Opening a file tab is not proof its
contents reached the model. Editing a file requires a fresh read to avoid stale
answers; our initial frozen fixture does not yet test that change-between-turns
scenario. Long-term project knowledge belongs in versioned notes plus retrieval.

Native Qwen thinking on/off differs from llama.cpp's `reasoning_budget_tokens`.
The latter was locally verified as a ceiling of 0/512/2048 tokens; it is not a
trained "xhigh" level. A longer budget can improve a case and still miss files.
Always count prefill, thinking, tool rounds and final text toward the deadline.
