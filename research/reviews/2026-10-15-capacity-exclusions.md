# Capacity exclusions from the research matrix

Checked against publisher model cards and Hugging Face metadata on 15 October 2026.
These are capacity dispositions, not local benchmark scores. No weights were
downloaded for these models. The recent unloaded host snapshots had roughly
15 to 23 GiB free RAM and 6.7 to 7.3 GiB free VRAM, before inference overhead
and guards. Later snapshots improved to about 26 GiB free RAM; this does not
change the exclusions for the giant models in this table.

The final column is arithmetic: stored parameter/tensor-element count times 0.5
bytes / 2^30. It is an idealized uniform four-bit payload, **not an actual GGUF**,
fit measurement or quality prediction. Mixed precision, scales, metadata,
embeddings, KV and compute allocations can increase real memory needs.

| Publisher model | Reported stored parameters | Ideal four-bit payload |
|---|---:|---:|
| [zai-org/GLM-5.3](https://huggingface.co/zai-org/GLM-5.3) | 753.3 B | 350.8 GiB |
| [zai-org/GLM-5.3-Flash](https://huggingface.co/zai-org/GLM-5.3-Flash) | 321.3 B | 149.6 GiB |
| [zai-org/GLM-4.7](https://huggingface.co/zai-org/GLM-4.7) | 358.3 B | 166.9 GiB |
| [deepseek-ai/DeepSeek-V4-Flash](https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash) | 290.9 B | 135.5 GiB |
| [deepseek-ai/DeepSeek-V4-Pro](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro) | 1598.8 B | 744.5 GiB |
| [deepseek-ai/DeepSeek-V4.1-Flash](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash) | 763.2 B | 355.4 GiB |
| [Qwen/Qwen3.5-397B-A17B](https://huggingface.co/Qwen/Qwen3.5-397B-A17B) | 403.4 B | 187.8 GiB |
| [Qwen/Qwen3.8-Flash-Next](https://huggingface.co/Qwen/Qwen3.8-Flash-Next) | 180.0 B | 83.8 GiB |
| [moonshotai/Kimi-K3](https://huggingface.co/moonshotai/Kimi-K3) | 2779.9 B | 1294.5 GiB |
| [meta-llama/Llama-4-Scout-17B-16E-Instruct](https://huggingface.co/meta-llama/Llama-4-Scout-17B-16E-Instruct) | 108.6 B | 50.6 GiB |
| [meta-llama/Llama-4-Maverick-17B-128E-Instruct](https://huggingface.co/meta-llama/Llama-4-Maverick-17B-128E-Instruct) | 401.6 B | 187.0 GiB |

All exceed the current apps-open resident budget at this precision before
cache/scratch headroom. This excludes them from the present Q4-first local
campaign; it is not proof that no lower-precision or disk-streaming experiment
could ever run. Such an experiment has no demonstrated path here to the
20-minute repository-task limit and would require a separate evaluation.

The Qwen3.8 Flash Next card distinguishes a 125B backbone from 51B n-gram
embeddings; its stored metadata totals approximately 180B. Counting only the
headline 125B understates the artifact. The 397B Qwen card likewise has more
stored parameters than its text-backbone name. These distinctions do not make
either model fit this desktop budget. See the linked publisher cards, and the
[pinned metadata snapshot](2026-10-15-excluded-artifacts.json) for revisions.

Active parameters per token are a compute measure, not the number of weights
which must be stored. Llama Scout is not a 17B-sized download simply because
its name includes 17B. This is a capacity decision; no claim that the Llama
family is inherently bad at coding is supported by this local campaign.
