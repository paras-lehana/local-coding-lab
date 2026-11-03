# Ternary Bonsai 2 27B (PQ2_0 and PTQ1_0) on an RTX 3080 10 GB

Trials run by Claude on 20 October 2026. This record was written on 3 November
2026 from the saved evidence, as an audit. No engine was started, no model file
was touched and no model output was executed for this record.
**Neither file produced a score. Both exact files were retired on 21 October.**

| Configuration | Runtime | Outcome | Score |
|---|---|---|---|
| PQ2_0, `--gpu-layers 52` | llama.cpp b11669 (mainline) | Load failed: `tensor 'output.weight' has invalid ggml type 142` | None; no inference |
| PQ2_0, 52 of 65 GPU layers, K/V on CPU | Prism fork b10787 | Loaded; router decoded at 2.3–2.7 tok/s; manually stopped at about 82 s | Unscored |
| PTQ1_0, all 65 layers on GPU, K/V on CPU | Prism fork b10787 | Router reads complete, then a partial answer at the 1200.016 s deadline | Unscored; later suites skipped |

## Why this candidate

Claude's 20 October scan ranked it first: a ternary rendition of the dense
Qwen3.8-27B. The PTQ1_0 file is 5.54 GiB, so a 27B-class reasoning model could
sit entirely in VRAM while the owner's applications kept their RAM.

The publisher claims "98.2% of FP16 intelligence retained" across 14
thinking-mode benchmarks and about 47 tok/s on an Apple M5 Max laptop. Those
are publisher claims, not local measurements. The model would have earned a
place by finishing the frozen workflows within 1200 s at a quality comparable
to Qwen Q4.

## Artifact and runtime identity

- Repository `prism-ml/Ternary-Bonsai-2-27B-gguf`, tested revision
  `b072e1d3b35a0a630cece372c2127528e0994386`. The license is Apache-2.0 per
  the card metadata, and the base model is `Qwen/Qwen3.8-27B`. The quantizer is
  Prism's own: ternary g128 weights in a Hadamard-rotated basis.
- `Ternary-Bonsai-2-27B-PQ2_0.gguf`: 7,206,168,928 bytes, SHA256
  `3907dc1658db1f78a9826bf8d5bcb8dc65db0d466388937af57f2294fae62ec1`
  (2.13 bits per weight).
- `Ternary-Bonsai-2-27B-PTQ1_0.gguf`: 5,946,648,928 bytes, SHA256
  `53107f530aa52eb00912263ab1ee29bd199261c87cd7b4ad4ca1318c1fe33ee3`
  (1.75 bits per weight).
- Upstream on 3 November: revision `94dd51cdbbec`, dated 30 October. It adds
  `Ternary-Bonsai-2-27B-Q2_0.gguf` (7,626,008,928 bytes, SHA256 `4f99aed0…`)
  "for stock llama.cpp" from b11556 onward. The two tested files are
  byte-identical in that revision (same LFS SHA256). The new Q2_0 file is a
  different artifact and has not been tested.
- Runtime: Prism fork release `prism-b10787-73bfe6c`, commit `73bfe6cc4855`,
  published 19 October, release zip SHA256 `64ca6810…`. The installed
  `llama-server.exe` had SHA256 `691d739a…` and `llama.dll` `8091b982…`.
  Another session removed the installed folder at about 19:11 IST on 3
  November, after this audit hashed it; the audit deleted nothing. The pinned
  release zip remains in `E:/llm/downloads` with a matching hash. Mainline
  b11669 cannot load ggml type 142. GitHub's compare shows the tested
  commit contains Prism PR #206 (AVX2/AVX-VNNI PQ2_0 CPU kernels, merged 21
  September).
- Template: Qwen-style, whose default system text sets reasoning effort to
  `xhigh`. The template accepts low, medium and xhigh. Runs used
  `--reasoning on`, deepseek reasoning format, preserved reasoning history and
  an unlimited reasoning budget.
- Effective sampling, per the server sampler lines: temperature 1.0, top_p
  0.95, top_k 20, min_p 0.05, repeat penalty 1.0. That is the publisher's
  thinking-mode recommendation. Requests carried only seed 73, temperature and
  `max_tokens`.

## Hardware, placement and conditions

The machine was an RTX 3080 on driver 617.42, a Ryzen 7 5800X and 64 GB of RAM
at 3000 MT/s, with PBO at motherboard limits and the GPU at stock. The owner's
applications stayed open, CPU core 0 was excluded and no new hardware event was
recorded.

| | PQ2_0 (Prism) | PTQ1_0 (Prism) |
|---|---|---|
| Free before load: RAM / commit / VRAM | 14.41 GiB / 18.06 GiB / 6,538 MiB | 15.38 GiB / 13.02 GiB / 6,848 MiB |
| Layers on GPU | 52/65 | 65/65 |
| CUDA weights / CPU-mapped weights | 5,275.79 / 1,585.95 MiB | 5,395.33 / 265.23 MiB |
| K/V (64K, q8, `--no-kv-offload`) | 2,176 MiB on CPU plus 149.62 MiB recurrent state | Same |
| Batch / micro-batch / threads | 512 / 128 / 4+8 | 512 / 64 / 4+8 |
| Load time | 8.25 s | 5.38 s |
| Lowest free RAM / commit / VRAM | 5.31 GiB / 6.91 GiB / 1,061 MiB | 7.31 GiB / 3.99 GiB / 1,040 MiB |
| Peak working set / private | 9.96 / 9.80 GiB | 8.67 / 9.64 GiB |
| Peak GPU temperature | 41 C | 59 C |

Even with every layer on the GPU, the PTQ1_0 process held 9.64 GiB of private
host memory for the whole 20-minute run. CPU K/V accounts for only 2.1 GiB of
that. The rest has no established cause, and it should be measured before
calling this model an apps-open fit.

## Frozen inputs and budgets

Both trials used the public router-v1 fixture: question SHA256
`097b3d020d4133cc…` with the frozen seven-file snapshot, tools mode, seed 73,
16,384 output tokens and a 1200 s whole-workflow deadline. The TypeScript/SQLite
and history tasks (16K and 4K outputs) were queued but never reached. Neither
model reached the private audit or the twelve coding tasks.

## Results

**PQ2_0 on mainline b11669.** The loader rejected the custom tensor type within
2 s. This is a runtime incompatibility, not a model result, and it led to
installing the reviewed Prism release.

**PQ2_0 on Prism b10787.** The smoke answered `READY` in 19.64 s at 1.53 tok/s.
In the router task, the 688-token prompt was processed at about 172 tok/s, but
decoding ran at only 2.3 to 2.7 tok/s.

The trial was stopped by hand after about 82 s, while the first turn was still
reasoning. The stop request already existed when `trial.py` tried to create it,
so the controller raised `FileExistsError`. That is a harness side effect of the
intentional stop, not an engine fault.

Claude's profile note blames the slowness on CPU-side expansion of ternary
layers; that has not been verified. The tested build already contains the
AVX2/AVX-VNNI PQ2_0 kernels, so the publisher's known issue about missing fast
CPU kernels does not explain it either. The cause is unestablished. No quality
conclusion follows.

**PTQ1_0 on Prism b10787, all layers on GPU.** The smoke answered `READY` in
3.03 s at 12.73 tok/s.

- Turn 0 of the router processed 692 prompt tokens at 340 tok/s and generated
  452 tokens at 13.08 tok/s. It requested all seven files in one parallel batch,
  every read succeeded, and the superseded v1 rule was read only so the answer
  could label it.
- Turn 1 then reasoned from 38.6 s onward: 36,531 reasoning characters, at a
  mean of 9.3 streamed chunks per second.
- Visible text began at 998.2 s. A structured answer was still writing its
  replacement code, at 6,622 visible characters, when the 1200.016 s deadline
  cancelled it.

The partial answer is not graded and no code was executed. The trial stopped
after this gate failure, and the private and coding suites were skipped.

## Failed, interrupted and unrun configurations

| Item | Actual reason |
|---|---|
| PQ2_0 on mainline | Unsupported ggml type 142; no load |
| PQ2_0 with 12 CPU layers | Manually stopped for decode at 2.3–2.7 tok/s; unscored |
| PTQ1_0 router | 1200.016 s deadline with an unfinished visible answer; unscored |
| TypeScript/SQLite, history, private audit, coding | Not run after the gate failure |
| Medium reasoning effort | Not run. This is the publisher's advice for budgets around 16K (below) |
| Stock-llama.cpp Q2_0 file (added 30 October) | Not downloaded or tested; a distinct artifact |
| GPU K/V placement, repeated seeds, editor use | Not run |

## Assessment

**Strengths seen here.** PTQ1_0 is the smallest file tested in the 20–21
October campaign, and all 65 of its layers fit in VRAM with the owner's
applications open. Turn 0 discovered the files correctly, completely and in
parallel, and full-GPU decode reached about 13 tok/s.

**Weaknesses seen here.** At the template's default `xhigh` effort, the
remaining 18 minutes went on reasoning, and only a partial answer appeared in
the last 202 s. Partial CPU offload of PQ2_0 is far too slow for the 1200 s
gate. The process kept a large private host-memory footprint even when fully on
the GPU. PQ2_0 and PTQ1_0 need the Prism fork.

**Publisher context, which these runs did not test.** The publisher's
known-issues page says that with output limits around 16K, `xhigh` runs out of
budget mid-reasoning more often than `medium`, and that medium is "about as
accurate". It also reports occasional looping at `xhigh`. That matches the
observed long reasoning, but the medium setting was never measured here.

**Comparison limits.** Each configuration is one seed on one task. Placement
and K/V location differ between the two files. Fast generation did not rescue
an incomplete workflow, as the current comparison already records.

**Recommendation.** Both files stay retired and unscored. Any new trial should
be separately labelled and address a concrete cause. Candidates are medium
effort, or the stock-llama.cpp Q2_0 file fully on the GPU with the K/V cache on
the GPU (the production b11562 is newer than the b11556 minimum). The first gate
should be the full frozen router, not a smoke test. An unchanged retry adds no
evidence.

## Reproduction, evidence and cleanup

The runs are reconstructed from the run records and launcher logs:

```powershell
E:/llm/python/Scripts/python.exe E:/llm/.claude/skills/local-llm/scripts/run_candidate.py `
  --profile bonsai2-ptq1-gpu99 --name <fresh-name> --temperature 1.0 `
  --runtime-dir E:/llm/runtimes/prism-b10787 --suites public,private `
  --conditions "RAM 3000 mixed; PBO motherboard limits; GPU stock; core-0 pinning; apps open"
```

The PQ2_0 profile is `profiles/bonsai2-pq2-gpu52.json`; the PTQ1_0 profile is
`profiles/bonsai2-ptq1-gpu99.json`. Both are untracked local files, and their
argument lists are reproduced in each trial manifest. Runtime pins are in
`catalog/runtime.json` (`prism-b10787-73bfe6c`) and artifact pins in
`catalog/models.json`.

- Public receipt: [exact-file retirement](../../../reports/2026-10-21-retirement.json),
  with exact paths, bytes, pinned SHA256 values, revision, reasons and
  redownload keys. See also the [current comparison](../../model-comparison.md).
- Raw evidence, ignored and private: `local-data/2026-10-20-campaign/bonsai2-*`.
- Derived numbers and audit notes F8–F9:
  `local-data/2026-11-03-campaign-audit/derived-measurements.json` and
  `audit-findings.json`.

Cleanup: on 21 October, under the owner's quoted authority, both exact files
were deleted to free space for Qwen IQ4_XS. The Qwen Q4 production file was
kept. No production availability check was made for this documentation audit,
because engines must not be started or stopped in this task.
