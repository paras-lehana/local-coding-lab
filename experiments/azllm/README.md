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
   collection at seed73, temperature0.6/top_p0.95/top_k20, 8192 output,
   2048 reasoning per turn, and a1200second whole-case deadline. Incomplete
   answers remain unscored. Run generated code only in the isolated grader.
6. Compare with existing source-grounded reports, distinguishing model,
   weights, engine, context, placement, cache state and output length. Restore
   the regular Qwen endpoint through its controller when capacity allows.

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
