# Recursive Flint on RTX 3080 10 GB

23 October 2026. Work in progress; no inference score yet.

## Requested work and status

| Requirement | Status | Evidence |
|---|---|---|
| Review Claude's new campaign | In progress | Private 20 October campaign, local-llm skill, 21 October records |
| Install and evaluate Flint on latest metrics | In progress | Pinned Unsloth GGUF and llama.cpp b11838 |
| Update comparison and make standalone report | In progress | This report; aggregate to follow |
| Make reporting mandatory for future models | In progress | Project guidance to follow |

## Selection and frozen plan

Production Qwen Q4 is retained. The first Flint configuration is Unsloth
UD-IQ3_XXS, 14,535,427,520 bytes (13.537 GiB), because the initial snapshot has
only about 13 GiB physical RAM and 6.5 GiB dedicated VRAM free with apps open.
This is a constrained quantization trial, not evidence about BF16 or the
publisher's NVFP4 model. The Q4 alternatives are larger than today's prudent
memory budget. Do not infer quality from the bit count alone.

Use the existing scorecard v2 questions and grading: private instructions /36,
public router/history/TypeScript/SQLite /60, twelve coding cases /12. Report
components separately. A weighted composite requires all three; partial
coverage is not comparable to a complete score. Each prompt has a 1200-second
whole-workflow deadline. Preserve reasoning, final text and actual requests.
Publisher sampling is temperature 1.0, top-p 0.95, top-k 20; old baseline uses
temperature 0.6. That difference must remain explicit. No promotion from one
seed, one partial suite or API readiness alone.

The Mac-only rec engine is inapplicable to this Windows/CUDA machine. Install
llama.cpp b11838 separately, leaving the production binary untouched. Check
native Flint support, chat parsing, actual weight/KV allocation and hardware
events before sustained evaluation. Do not weaken memory guards to obtain a score.

## Initial machine snapshot

- GPU: RTX 3080, 10,240 MiB total; 3,439 MiB used, 6,615 MiB free;
  driver 621.01 (different from Claude's 617.42).
- RAM: 63.91 GiB total, approximately 13.08 GiB available.
- Commit: approximately 21.03 GiB available.
- E: approximately 7.81 GiB free before exact-file retirement.
- No llama/Strata/Python experiment process found; Ollama service exists.
  Its loaded-model state still needs checking before launch.
- Boot: 23 October 00:14 local. Current clock/tuning state and incident check
  remain preflight work, not assumed from historical notes.

## Sources

- [Recursive announcement](https://recursive.com/updates/introducing-recursive-flint)
- [Original checkpoint and architecture](https://huggingface.co/RecursiveSI/flint)
- [Selected GGUF publisher](https://huggingface.co/unsloth/flint-GGUF)
- [rec supported hardware](https://github.com/recursive-oss/rec)
- [Pinned runtime release](https://github.com/ggml-org/llama.cpp/releases/tag/b11838)

Vendor benchmark scores and speed claims are not measurements on this machine.
Pin identities are in experiments/flint/pins.json. Raw local evidence is kept
under ignored local-data/2026-10-23-flint/.

## Validation and findings

Pre-inference findings:

- Both b11838 runtime archives pass full SHA256 checks; installed executable
  reports commit 4231b23dc. No production binary was replaced.
- Header inspected independently without loading weights. Architecture is
  flint, 49 blocks, 14 full-attention/35 sliding-window layers, 4 KV heads of
  dimension128. GGUF configured context is262144; the announcement's512K claim
  is not a tested capacity of this artifact/profile.
- Weight spans:8,082,423,808 bytes IQ2_S;4,829,741,056 IQ3_XXS;
  1,567,641,600 Q6_K;49,283,072 BF16;867,456 F32. Labels describe a mixed
  recipe; do not treat UD-IQ3_XXS as uniform3bit or the publisher's NVFP4.
- 36 CPU-MoE blocks estimate8.699GiB CPU expert spans and4.833GiB other
  weights before token-embedding placement and runtime costs. Compact64K
  q8 KV is estimated near1GiB, not the generic16GiB from earlier advice.
- Inspected b11838 source: lazy-mode affects only TENSOR_READ_LAZY tensors;
  Flint's expert tensors are not flagged. Initial lazy-mmap proposal was
  corrected before any run. Selected load-mode none avoids Windows whole-file
  prefetch; 13GiB physical/18GiB available-commit launch gates,2.5GiB RAM and
  400MiB free-VRAM stop floors. No guard was lowered during a measured run.
- Latest private collector uses24576 output tokens; public router/TS-SQL
  use16384 and history4096; coding uses16384. These are retained for comparison,
  below the publisher's suggested32768 hard-task output allowance. The strict
  1200second wall gate remains. Higher-budget diagnostics must be separate.
- Existing lab baseline:38 offline tests pass. Public audit at this checkpoint
  scans223 files with0findings; this is not a final post-change validation.

Raw header receipts: local-data/2026-10-23-flint/header.json and header-v2.json.
The latter reuses the maintained scripts/gguf_metadata.py parser and agrees
on spans. Inference/quality results remain pending.

## Owner request

See the unchanged owner-request.txt alongside this document.
