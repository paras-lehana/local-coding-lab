# azllm, TurboQuant and Strata on 10 GB

19 October 2026. In progress; do not treat planned trials as measurements.
Production recommendation remains Qwen3.6-35B-A3B UD-Q4_K_M in llama.cpp.

## Starting evidence

The supplied Andrew Zhu article describes azllm, a tqllm fork, running dense
Qwen3.8-27B with custom weight formats, low-bit KV, DFlash2 speculation and
prefix reuse on 24GB/32GB GPUs. Pinned source adds host embeddings, output-head
and KV-tail placement, but does not provide general dense layer CPU offload.
Dense body matrices use the GPU uploader. The smallest published TQ_XS file
is11.85GB; the selected TQ3_4S-v2 file is14,495,191,008bytes. A smaller context
does not shrink these weights. Native Windows serving also uses POSIX APIs;
its mapped-GGUF implementation explicitly requires Linux/WSL or macOS.

The same TQ3_4S weights have a separate CPU/GPU-capable llama.cpp-tq3 path.
That is the practical measured fallback, not an azllm/DFlash2 reproduction.
See the [frozen plan](../../../experiments/azllm/README.md).

Initial Windows snapshot:22.7GiB free physical RAM, about33.2GiB available
commit,7315MiB free VRAM,14.0GiB free disk. No inference server is running
after the18October22:04 reboot. No stop was issued by this experiment.
Apps, clocks, editor settings and remote tunnel configuration remain unchanged.

## Previous Strata result

The [completed Strata report](../2026-10-18-strata/2026-10-18-strata-on-10gb-v0.6.0.md)
is the authority. Same-Qwen32K workflows complete1.14-1.76x faster in single
practical runs, but SQL migration fails, both engines retain TypeScript defects,
and Strata's Qwen128K path was not validated. Flash-Next fits10GB; four coding
trials time out.128K/int8 with32K GPU-resident KV really uses1.55GiB pinned RAM
and processes51K input, but the original history workflow ends with empty final
content. Two diagnostic replays recover6/6facts; they do not pass that workflow.
