# Groot-19B-A3B-261023 Q4_K_M with apps open on an RTX 3080 10 GB

Trials run by Claude on 3 November 2026, 20:33-20:39 IST. This record was written
the same evening from the saved run evidence. No engine was started for the
record itself.

**Status: capacity-limited apps-open; no quality score.** Both runs were stopped
by the RAM guard before any workflow finished. Neither has a correctness result,
so nothing here says how good the model is.

9November source refresh: the live [publisher card](https://huggingface.co/GrootTeam/Groot-19B-A3B-261023)
distinguishes precise-coding sampling (temperature0.6, presence penalty0)
from general thinking (temperature1, presence penalty1.5). The old coding
choice remains consistent with that recipe; it is not the only publisher
default. The card recommends at least128K for long thinking and reports
multi-hour agent evaluations. This does not make64K technically incapable
of reasoning: a frozen64K workflow must fit without context shifting and
be judged on its actual answers. A later128K comparison remains separate.
The historical table below keeps its original card snapshot and test dates.

Prepared9November retry, **not run**:
[groot-q4-resident4-guarded64](../../../profiles/groot-q4-resident4-guarded64.json).
Same pinned weights/runtime and CPU36/GPUq8/cache512/b128-u32/coding sampler,
resident maximum4GiB with3.5GiB reserve. Admission is now7.5GiB RAM,
9GiB commit and6000MiB VRAM; runtime floors2.5GiB/1GiB/400MiB/84C.
Explicit no-context-shift protects the64K workload; the21600s server socket
timeout allows separately labelled extended collection while each collector
retains its own whole-case deadline. Actual resident allowance and desktop
conditions must be measured again. No floor is lowered and no owner app is
closed. Plain600s greetings precede any scored file workflow.

| Run | Profile | Outcome | Score |
|---|---|---|---|
| A, `groot-q4-20261103` | `groot-19b-q4-moe36-mmap64`, no working-set cap, RAM floor 0.5 GiB | Smoke `READY.`; RAM guard stop 5.1 s into the router prefill, with available RAM at 0.42 GiB | Unscored (frozen-1200 cohort, interrupted) |
| B, `groot-q4-resident4-20261103` | `groot-19b-q4-moe36-cache512-resident4-mmap64`: 3.31 GiB working-set cap, 512 MiB GPU expert cache, batches 128/32, RAM floor 2.0 GiB | Smoke `READY.`; router turn 1 finished (2 of 7 files requested); RAM guard stop during turn 2 prefill, at 1.946 GiB available, 227.6 s into the workflow | Unscored (diagnostic cohort, interrupted) |

## Why this candidate

The 3 November deep research ranked Groot second, after a read-only log audit
([research report](../2026-11-03-deep-research/2026-11-03-deep-research-v1.0.md),
section 2, experiment 2). It looked like the only new candidate that could run at
4-5 bits within the apps-open budget. It is a smaller derivative of the Qwen3.6
reference, uses the same `qwen35moe` architecture and the same tool and thinking
template, and its publisher claims 23% shorter output. To be kept, it had to at
least match Qwen3.6 UD-IQ3_S on the private audit (29/36), with no strict
TypeScript or SQLite regressions. All three suites had to run at 1200 s per
prompt.

## Model facts

**Publisher and research claims.** These were not measured here.
- GrootTeam, Apache-2.0, created 23 October 2026. The card says it is built from
  Qwen3.6-35B-A3B and post-trained on fewer than 0.1B tokens of open data. It
  does not name the compression method.
- About 19.4B total and about 3B active parameters, plus a 0.4B MTP layer. 128
  routed experts plus 1 shared expert, with 8 active per token. 40 layers: 10
  full-attention and 30 linear-attention.
- Vendor claims: it wins 12 of 16 benchmarks against Qwen3.6-35B-A3B and
  Gemma-4-26B-A4B (16-benchmark averages 41.44, 38.08 and 30.05). Terminal-Bench
  2.1 is 52.10 against Qwen3.6's 43.82. Output is 23.1% shorter.
- The card has no SWE-bench Verified, IFBench, IFEval or tau2 score. No
  independent evaluation existed when the research was done.
- Recommended settings: thinking on, with `preserve_thinking`; temperature 0.6,
  top_p 0.95, top_k 20 and presence penalty 0.

**Read from the GGUF by llama.cpp b11562.** These are local observations.
- Architecture `qwen35moe`, 41 blocks (40 plus one `nextn` MTP block). Embedding
  2048; 16 heads with 2 KV heads; head size 256.
- 128 experts with 8 used per token. Expert and shared-expert FFN widths are 512.
  Full attention every fourth layer. Trained context 262,144.
- 18.99B parameters, 11.62 GiB at 5.26 bits per weight, imatrix-quantized.
  Tensor types: 370 f32, 254 q8_0, 104 q4_K, 14 q6_K and 11 q4_0.
- Vocabulary 248,320 with pre-tokenizer `qwen35`. Byte-level identity with
  Qwen3.6's tokenizer was not checked.
- The GGUF's `general.sampling.temp` is 1.0, but the card recommends 0.6. Both
  runs sent 0.6 explicitly, to match the Qwen reference settings.
- b11562 loads the MTP block's 20 tensors as unused (`blk.40.*`, "ignoring"). No
  speculative decoding ran.
- q8 KV at 64K is 680 MiB over 10 attention layers, plus 62.81 MiB of recurrent
  state. Both figures equal Qwen3.6's, as expected from the shared attention
  layout.

## Artifact and runtime identity

- Repository `bartowski/GrootTeam_Groot-19B-A3B-261023-GGUF`, revision
  `0025df0d03fb385344394f4e5afd73ce47da0680`, quantized with b11845 (repo dated
  25 October). Upstream is `GrootTeam/Groot-19B-A3B-261023`, revision
  `d089dadfe280289b2f3cd2ae9ef9796c2495529a`.
- File `GrootTeam_Groot-19B-A3B-261023-Q4_K_M.gguf`: 12,484,339,584 bytes, SHA256
  `c941e12a231b40b8fb9f6ad7f6601878d72db39c2c62aefb185fbe5c7d0c2e29`. It is pinned
  in `catalog/models.json` as `groot-19b-a3b-q4`.
- The download was staged on C: and verified there at 20:26. `lab.py run` checks
  the full size and SHA256 again before every launch, so the installed E: copy
  passed the pin twice, at 20:33 and 20:35.
- Runtime: `runtimes/b11562-noprefetch-v1`, build b11562 (b2f036c0f), `llama.dll`
  SHA256 `7bf9b3b0...`. This is the reviewed lab runtime with the initial mmap
  prefetch turned off.
- Template: the GGUF's own chat template, with `--jinja`, `--reasoning on`,
  deepseek reasoning format, `--reasoning-preserve` and no reasoning budget.
  Server props report tool calls, parallel tool calls and preserve-reasoning as
  supported, and reasoning effort as unsupported. Thinking is boolean only.
- Effective controls, from the server's sampler lines: temperature 0.6, top_p
  0.95, top_k 20, min_p 0, repeat penalty 1.0 and presence penalty 0. Requests
  carried seed 73, temperature 0.6 and `max_tokens` 16384; the smoke used
  temperature 0 and a reasoning budget of 0.

## Hardware, placement and conditions

The machine was an RTX 3080 10 GB on driver 621.01, a Ryzen 7 5800X, and 64 GB of
RAM at 3000 MT/s (mixed modules). PBO was at motherboard limits, the GPU was
stock, and CPU core 0 was excluded (`--cpu-mask 0x5554`, strict). The owner was
working. The run records list Edge (about 24 GB), VS Code (about 12 GB) and the
Hyper-V VM, plus Gradle builds earlier. The 20:40 budget check also saw the
Android emulator. The commit limit was 115.36 GiB; the page file is system-managed.

| | Run A (uncapped) | Run B (resident4) |
|---|---|---|
| Preflight free RAM / commit / VRAM | 5.37 GiB / 8.44 GiB / 5,676 MiB | 5.67 GiB / 8.25 GiB / 5,886 MiB |
| Admission gates | 5 GiB / 6 GiB / 5,500 MiB | Same |
| Stop floors (RAM / commit / VRAM / GPU temp) | **0.5 GiB** / 1.0 GiB / 400 MiB / 84 C | 2.0 GiB / 1.0 GiB / 400 MiB / 84 C |
| Placement | `--gpu-layers all --n-cpu-moe 36`: attention, shared experts and the experts of layers 36-39 on the GPU; the routed experts of 36 layers on the CPU (mmap) | Same, plus a 512 MiB GPU expert cache (489.61 MiB allocated for 8,205 MiB of host experts, about 6% of slots per layer) |
| Buffers | CPU_Mapped 10,054 MiB; CUDA0 model 2,937 MiB; KV 680 MiB; RS 62.81 MiB; compute 226 MiB | Same, with compute 206.5 MiB |
| Context / KV | 65,536, q8_0 K and V on the GPU, flash attention, 1 slot | Same |
| Batch / micro-batch / threads | 512 / 128 / 4 generation, 8 batch | 128 / 32 / 4, 8 |
| Working-set cap | None | `min(4, free RAM - 2.5)` = 3.308 GiB (3,551,862,784 bytes) |
| Prompt cache | `--cache-ram 0` | Same |

Run A's 0.5 GiB RAM floor is below the campaign's current minimum of 2.0 GiB and
below the lab default of 2.5 GiB. The guard tripped as designed, and no hardware
event followed. Any rerun should keep a floor of at least 2.0 GiB.

## Frozen inputs and budgets

Both runs used the public router-v1 fixture with the frozen seven-file snapshot.
The question SHA256 was `097b3d020d4133cc...`, delivery was tools mode, the seed
73, output capped at 16,384 tokens, and the whole-workflow deadline 1200 s. The
`ts-sql-v1` (16,384 output) and `context-v1` (4,096 output) tasks were queued but
never reached. The private audit and the twelve coding tasks did not start. Each
smoke was the frozen `Reply with exactly READY.` prompt. The prompt cache was off,
and each run started a fresh server.

## Results

**Run A (uncapped).**
- Launch: the record started at 20:33:06; the server process began at 20:33:19
  after the hash and preflight. It was listening 7.7 s later.
- Smoke: `READY.` in 4.813 s. Prompt 15 tokens at 4.60 tok/s; 5 output tokens at
  2.74 tok/s. Five tokens are not a decode benchmark.
- Router: the 654-token prompt began prefilling. About 5 s later the guard
  stopped the server with "ram_free_gib below 0.5 or unavailable". The collector
  reported `worker_error` (WinError 10054) at 5.125 s. There was no output.

**Run B (resident4).**
- Launch: the server was listening 9.8 s after it started. Smoke: `READY.` in
  6.625 s (prompt 3.17 tok/s, decode 2.17 tok/s).
- Router turn 1, prompt: 654 tokens prefilled in 107.7 s, at 6.07 tok/s. The
  first 128 tokens ran at only 3.84 tok/s.
- Router turn 1, output: reasoning began at 107.8 s and visible text at 163.5 s.
  The turn decoded 232 tokens in 99.2 s at 2.33 tok/s: 539 reasoning characters
  and 131 visible characters. It ended with one parallel tool call reading
  `AGENTS.md` and `.claude/CLAUDE.md`, the correct starting files. The server
  logged 206.96 s for the turn.
- Router turn 2: a 1,180-token prompt, 885 of them cached, began at 227.5 s
  server time. About 20 s later, with 295 new tokens still prefilling and no
  output, the guard stopped the server with "ram_free_gib below 2.0 or
  unavailable".
- The collector reported `worker_error` (WinError 10054) at 227.641 s. The last
  memory sample was at 20:39:34 IST, and the run record finished at 20:39:37.

Neither run delivered a final answer, so neither has an instruction, citation,
code, history or syntax result. Two correct first reads are not a router score.
Both records report `hardware_clean: true` for the public phase.

## Memory timelines

From each run's `memory.jsonl` (about 1 s sampling, then 5 s in run B after
120 s). Times are seconds after the first sample.

**Run A**, from 20:33:19, 22 samples:

| t (s) | Available RAM GiB | Commit available GiB | VRAM free MiB | Process working set / private GiB | Event |
|---:|---:|---:|---:|---:|---|
| 0.0 | 5.25 | 8.28 | 5,666 | 0.01 / 0.00 | process start |
| 3.3 | 4.96 | 4.88 | 2,554 | 0.41 / 3.41 | CUDA buffers allocated |
| 6.6 | 1.39 | 3.33 | 1,540 | 3.98 / 4.97 | weights touched; minimum commit |
| 13.2 | 1.60 | 4.28 | 1,547 | 4.80 / 5.01 | smoke |
| 18.8 | 0.92 | 5.10 | 1,736 | 6.35 / 5.20 | router prefill starts |
| 23.3 | 0.42 | 5.99 | 1,707 | 7.82 / 5.16 | last sample; stop below 0.5 GiB |

The working set was still rising at the stop. The CPU-mapped weights total
10,054 MiB, so full residency was not reached.

**Run B**, from 20:35:27, 132 samples:

| t (s) | Available RAM GiB | Commit available GiB | VRAM free MiB | Process working set / private GiB | Event |
|---:|---:|---:|---:|---:|---|
| 0.0 | 5.74 | 8.30 | 5,889 | 0.03 / 0.12 | process start |
| 2.2 | 5.42 | 5.07 | 2,762 | 0.40 / 3.41 | CUDA buffers allocated |
| 5.5 | 2.38 | 3.13 | 1,545 | 3.28 / 5.46 | cap nearly full |
| 6.6-241.6 | 2.14-2.72 (median 2.48) | 2.44-3.20 | 1,421-1,535 | 3.308 flat / 5.50-5.85 | smoke, router turn 1, turn 2 prefill |
| 246.7 | 1.946 | 3.79 | 2,226 | 3.308 / 5.84 | last sample; stop below 2.0 GiB |

- The final 5 s brought a 0.29 GiB drop in available RAM. In the same interval
  777 MiB of VRAM and 1.08 GiB of commit were released. Neither change is
  attributed to the model or to the desktop applications.
- Page faults grew from 7,401 to 27,139,251, about 110,000 per second. The count
  includes soft faults, so it does not equal SSD reads.
- GPU temperature stayed between 51.8 and 52.9 C. No sample has a GPU read
  error.

**GPU allocations charged commit about one to one.** Run A's load took 4.03 GiB
of VRAM (5,666 to 1,540 MiB) and 4.94 GiB of commit. Run B took 4.24 GiB of VRAM
and 5.21 GiB of commit. The roughly 1 GiB extra matches the process's private
host buffers. This repeats the WDDM finding in
[memory-and-context.md](../../memory-and-context.md#vram-allocations-also-consume-windows-commit).
WDDM process counters after load read 4.04 and 4.51 GiB dedicated. They are
indicative only.

## Why it failed with apps open

1. **The CPU-resident part is about 8 GiB, not 3.** The 36 CPU expert layers
   hold 8,205 MiB of host experts, inside a 10,054 MiB CPU-mapped buffer. The
   apps-open budget is about 6 GiB of available RAM. Holding the 2.0 GiB floor
   leaves the model roughly 2.5-3 GiB of RAM.
2. **Uncapped, the mapped weights simply filled RAM.** Run A's working set
   reached 7.8 GiB in 23 s and pushed available RAM to 0.42 GiB. A 2.0 GiB
   floor would have tripped at the 6.6 s sample, before readiness.
3. **Capped, the arithmetic leaves almost no slack.** The cap is
   `min(limit, ram_free - reserve)` = `min(4, 5.81 - 2.5)` = 3.31 GiB. In
   principle that keeps 2.5 GiB available, 0.5 GiB above the floor, at the
   moment of the snapshot. In practice, after the cap filled, available RAM sat
   0.14-0.72 GiB above the floor (median 0.48 GiB). Desktop activity (Gradle, the
   emulator, Edge) moves by more than that within minutes. One later dip ended
   the run. The campaign log's "~0.2 GiB above the floor" is the low end of
   this measured range.
4. **The cap also makes the model too slow for the deadline.** Each token
   routes to 8 of 128 experts in each of 36 CPU layers, so the active pages keep
   changing. Only about 40% of the CPU experts fit under the cap, and the rest
   are refaulted from the file cache or the disk; that is where the 27 million
   page faults come from. Decode was 2.33 tok/s and prefill 6.07 tok/s.
   - Earlier Qwen3.6-35B-A3B profiles with fuller residency reached about
     13-20 tok/s. That is a different model and profile, not a matched
     comparison.
   - At 2.33 tok/s the 1200 s deadline allows about 2,800 output tokens for the
     whole workflow, before prefill. Turn 1 alone took 207 s for two file reads.
     So even without the guard, the router could not plausibly have finished in
     time (inference).
5. **Moving more experts to the GPU cannot close the gap with apps open.** This
   is an estimate from the logged buffers, about 228 MiB of experts per layer.
   - Getting the CPU part below 3 GiB needs at most about 13 CPU layers, which
     puts about 27 expert layers on the GPU. The GPU would then hold about
     8.8 GiB of weights, KV and compute buffers, against the 5.8-6.2 GiB VRAM
     that is free with apps open. It would also take the same amount of commit.
   - IQ4_XS (10.94 GB) is about 12% smaller and does not change this.
   - A few more GPU layers (`--n-cpu-moe` 30-32) would cost about 1-1.4 GiB of
     VRAM and commit each way, and would still leave about 7 GiB of CPU experts.

This is a host-capacity disposition. It is not evidence about Groot's
instruction-following or coding quality.

## What an apps-closed run needs

**Gates** for profile `groot-19b-q4-moe36-mmap64`. These are estimates from the
logged buffers and memory peaks.
- Raise its stop floor from 0.5 GiB to at least 2.0 GiB, preferably the lab
  default of 2.5 GiB.
- Use no working-set cap, or a cap of at least 11 GiB.
- **RAM:** at least 14 GiB available at admission. That covers about 10.3 GiB of
  mapped weights plus host buffers fully resident, the 2.5 GiB reserve, and
  about 1 GiB for growth.
- **Commit:** at least 8 GiB available. The measured charge was 4.9-5.2 GiB,
  plus the 1.0 GiB floor and a margin. The current 6 GiB gate leaves less than
  1 GiB of slack.
- **VRAM:** at least 5,500 MiB free. The measured use was 4.0-4.2 GiB, and the
  lowest free reading was 1,421-1,531 MiB, well above the 400 MiB floor.
- **Disk:** none needed; the weights are already installed.
- A matching window means closing Edge, the emulator and the VM, or rebooting.
  That is the owner's call.

**Controls**
- Batches 512/128.
- No expert cache in the frozen-cohort run. A cache arm is a separate
  diagnostic.
- The same native thinking, sampling, seed and request settings as these runs.

**Sequence**
1. Preflight: `scripts/preflight.ps1`, with no engine and nothing on port 8081.
2. Launch: guarded launch on port 8081, smoke, then a plain greeting cold and
   warm (600 s ceiling).
3. Public suites: router, TS/SQL and history, at 1200 s each.
4. Private audit: `run.py --port 8081 --temperature 0.6 --deadline-seconds 1200`.
5. Coding: `collect_coding.py --deadline 1200 --max-tokens 16384`.
6. Grading: review every turn before any isolated grading.
7. Stop: stop on any new WHEA error or bugcheck.

## Failed, interrupted and unrun configurations

| Item | Actual reason |
|---|---|
| Run A, uncapped router | RAM guard at 0.42 GiB (0.5 GiB floor), 5.1 s into prefill; no output |
| Run B, resident4 router | RAM guard at 1.946 GiB (2.0 GiB floor) during turn 2 prefill at 227.6 s; turn 1 delivered two correct reads, no answer |
| TS/SQL and history, both runs | Not run after the router failed (controller `stopped_after_failed_task`) |
| Private audit and 12 coding tasks | Not run |
| Apps-closed full residency | Not run; needs the gates above |
| Groot MTP self-speculation, IQ4_XS, Q5_K_S and b12069 | Not run |

## Assessment

**Strengths seen here.**
- The file loads and answers on the reviewed b11562 runtime without errors.
- The template's tool and thinking support works: one parallel tool call,
  visible text separate from reasoning.
- The first two reads were the right files.
- GPU memory needs are modest (about 4.0-4.2 GiB with a 64K q8 KV cache).

**Weaknesses seen here.**
- With about 8 GiB of CPU experts, it does not fit the about 6 GiB apps-open RAM
  budget.
- Paging under a cap drops it to 2.33 tok/s decode, far too slow for the 1200 s
  workflow.
- The research note's "it is smaller than the 13.7 GB IQ3_S that already runs"
  was true of file size. However, the 21 October IQ3_S run B loaded with
  12.13 GiB free RAM, not today's 5-6 GiB.

**Comparison limits.**
- One seed and one task, with the run ending during the first workflow.
- Placement and residency differ between the two runs.
- Run B changed batches and added an expert cache, so it is a diagnostic.
- No quality claim in either direction.

**Recommendation.**
- Keep the weights installed. Run the frozen suites only in an apps-closed
  window that passes the gates above.
- Do not retry apps-open with a smaller cap or a lower floor. A smaller cap
  slows it further, and lowering the floor is not allowed.
- Production is unchanged.

## Reproduction, evidence and cleanup

The command is reconstructed from the run records; the exact driver command line
was not saved:

```powershell
cd E:/llm/local-coding-lab
$env:PYTHONPATH = 'E:/llm/local-coding-lab'
E:/llm/python/Scripts/python.exe E:/llm/.claude/skills/local-llm/scripts/run_candidate.py `
  --profile groot-19b-q4-moe36-cache512-resident4-mmap64 --name <fresh-name> `
  --temperature 0.6 --suites public,private `
  --conditions "RAM 3000 mixed; PBO motherboard limits; GPU stock; driver 621.01; core-0 pinning; apps open"
```

- **Profiles:** `profiles/groot-19b-q4-moe36-mmap64.json` and
  `profiles/groot-19b-q4-moe36-cache512-resident4-mmap64.json`. Both are
  untracked local files; their full argument lists are in each `trial.json`.
- **Raw evidence** (ignored, private):
  - `local-data/2026-11-03-campaign/groot-q4-20261103-*`
  - `local-data/2026-11-03-campaign/groot-q4-resident4-20261103-*` (each holds
    `server/runs/*/memory.jsonl`, `server.log`, `stop.json` and
    `core-seed73/turns.json`)
  - the driver logs `local-data/2026-11-03-campaign-groot-driver.log` and
    `-groot-resident4-driver.log`
  - the download log `local-data/2026-11-03-queue/groot-download.log`
- **Scorecard:** runs `groot-q4-20261103` (frozen-1200, interrupted) and
  `groot-q4-resident4-20261103` (diagnostic, interrupted), unranked. See the
  [current comparison](../../model-comparison.md).
- **Cleanup:** no file was deleted and the weights stay installed. Both owned
  servers were stopped by the guard.
- **Production:** it has been off since 24 October 13:23 and was not touched. At
  20:51:18 IST no `llama-server` process was running and nothing was listening on
  port 8080 or 8081.
