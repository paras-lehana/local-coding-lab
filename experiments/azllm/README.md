# azllm / TurboQuant on 10 GB

Started 19 October 2026. This is an experiment, not a production replacement.
The owner's attached Andrew Zhu article is a lead; reported 3090 Ti results
are not measurements on this RTX 3080. Raw pasted text stays private.

## Frozen plan

1. Pin azllm and inspect dense weight placement, KV placement, formats and
   platform support. Read exact artifact metadata before downloading.
2. Measure available physical RAM, commit, VRAM and disk with apps open.
   Do not force an all-GPU load whose weights exceed physical capacity.
3. Try the same TQ3_4S-v2 artifact in the author's llama.cpp-tq3 fork with
   partial GPU layers and CPU q8 KV. This is a different engine path from
   azllm/DFlash2; neither its timings nor quality establish the headline claim.
4. Start at 16K context/16 GPU layers, then tune within observed headroom.
   Use one slot, a separate loopback port, no drafts, conservative buffers,
   and the lab's owned-process resource/WHEA guard. Never change production.
5. If readiness succeeds, freeze router-v1, changed-file/history and TS/SQL
   collection at seed 73, temperature 0.6/top_p0.95/top_k20, 8192 output,
   2048 reasoning per turn, and a1200second whole-case deadline. Incomplete
   answers remain unscored. Run generated code only in the isolated grader.
6. Compare with existing source-grounded reports, distinguishing model,
   weights, engine, context, placement, cache state and output length. Restore
   the regular Qwen endpoint through its controller when capacity allows.

Before inference, source review adds a conditional native-MTP probe. The GGUF
already contains one prediction block. After a no-draft fit, compare the same
bounded greedy inline probe with draft max 2 and the pinned40,960-token draft
vocabulary if measured headroom permits. MTP and DFlash2 are distinct draft
methods; a short correct answer does not establish general token equivalence.
Keep any MTP speed/quality result separate from the no-draft baseline.

The pinned compatible fork also implements `draft-dflash`. Before collection,
the plan adds the official z-lab1.143 GB Q4_K_M drafter, with 24target GPU layers
and 20as a guarded fallback. This is the same drafting family, but another
draft quant/runtime from the article's0.785 GB TQ3 file. Download it explicitly
with `--artifact dflash`. Never start it alongside another engine. Test load,
memory and bounded greedy probes first; a short token match is not a general
equivalence proof. Do not download BF16/Q8 variants for this 10 GB trial.

Pinned sources and weight identities are in `artifacts.json`. Installation
and models stay under the owner's E:/llm directory; binaries are not published.
The upstream download helper resolves main and is therefore not used for
reproducible collection. `download.py` reuses the lab's bounded range transport.

## Reproduction

Read the final report before starting; planned settings in `settings.json`
are not proof of fit. Download without inference:

```powershell
python experiments/azllm/download.py --data-dir E:/llm/models --connections 16
```

For the fallback engine, check out the manifest's exact llama.cpp-tq3 commit
in a separate directory. From an x64 Visual Studio developer environment,
with CMake, Ninja and a compatible CUDA toolkit on PATH:

```powershell
cmake -S E:/llm/llama-tq3-source -B E:/llm/build/llama-tq3 -G Ninja `
  -DCMAKE_BUILD_TYPE=Release -DGGML_CUDA=ON -DCMAKE_CUDA_ARCHITECTURES=86 `
  -DCMAKE_CUDA_RUNTIME_LIBRARY=Shared -DGGML_NATIVE=OFF -DGGML_AVX2=ON `
  -DGGML_FMA=ON -DGGML_F16C=ON -DLLAMA_BUILD_TESTS=OFF `
  -DLLAMA_BUILD_EXAMPLES=OFF -DLLAMA_BUILD_APP=OFF -DLLAMA_OPENSSL=OFF `
  "-DCMAKE_C_FLAGS=/DWIN32 /D_WINDOWS /experimental:c11atomics"
cmake --build E:/llm/build/llama-tq3 --target llama-server llama-bench -j 4
```

The explicit C flags matter for this fork's C11 atomic include under MSVC;
changing `CFLAGS` after CMake has cached a value does not update that cache.
Keep the resulting DLLs together and use the same isolated CUDA libraries.
Do not replace the production runtime. The sm86 build does not enable the
fork's Blackwell FP4 path: the RTX3080 is Ampere, not Blackwell.

## Measured selection and remaining gates

The19October calibration selects28target GPU layers,32K context and no draft
before workflow scoring. The same tiny greedy probe takes27.296seconds; native
MTP at24layers gives30.094seconds, and Q4 DFlash2 at24gives26.594seconds but only
817MiB free device VRAM. These single samples do not demonstrate a worthwhile
drafting advantage over the simpler placement.30layers add pressure without
a token-rate gain and produce different formatting. All probe facts are
supplied inline: they are not a retrieval or coding score.

Use the shared `experiments/strata/guard.py` only with an explicit configuration
and a new output directory. It depends on the separately installed Strata
environment's reviewed `serve/winjob.py` and `psutil`; it is not a standalone
installer. Its owned Windows job, RAM/commit/VRAM/temperature/WHEA checks and
stop receipt are required for these live trials. Do not infer safety from a
successful `--list-devices`: CUDA reports more free memory here than NVML.

The effective main command uses the manifest's target and built executable,
`--gpu-layers 28 --ctx-size 32768 --parallel 1 --threads 8 --threads-batch 8`,
`--batch-size 256 --ubatch-size 128 --flash-attn on`,
`--cache-type-k q8_0 --cache-type-v q8_0 --no-kv-offload`,
`--load-mode mmap --no-repack --fit off --jinja`,
`--reasoning on --reasoning-format deepseek --reasoning-preserve`,
`--reasoning-budget 2048 --predict 8192`, the xhigh template instruction,
`--seed 73 --temp 0.6 --top-p 0.95 --top-k 20 --min-p 0 --repeat-penalty 1`,
and `--spec-type none --cache-ram 0 --ctx-checkpoints 4`.
Exact structured values are in `settings.json`. CPU KV is allocated
as capacity at load; slots and checkpoints can still reuse prior prefixes when
the separate multi-prompt RAM cache is disabled.

The prepared28-layer/131072-context capacity probe was not launched. Windows
restarted during the router case, before its deadline or a final answer. A
corrected processor-cache hardware record was logged during startup. Remaining
history/TS-SQL/512-budget/131K inference and production restart are withheld
under the host's existing hardware-stop rule. This is not a model quality score
or proof of the reboot's cause. Read the final report before resuming anything;
no automatic retry is configured and no production model was replaced.
