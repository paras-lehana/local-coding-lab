# Initial Windows mmap prefetch experiment

This is an isolated, opt-in loader experiment, not the recommended runtime.
The stock b11562 runtime remains the reference. On this workstation, mapping
the 45.20 GiB Coder-Next artifact exhausted physical and commit headroom before
inference, despite a process working-set maximum. The guard stopped that load.
The suspected mechanism is whole-file Windows `PrefetchVirtualMemory` during
initial mapping. Historical candidate outcomes are in the linked task report;
the loader change itself does not establish that a larger model is usable.

`loader.patch` applies to the MIT-licensed
[llama.cpp commit b2f036c0f](https://github.com/ggml-org/llama.cpp/tree/b2f036c0f138414dedc987446f1d9d802f920275).
It disables initial mmap prefetch only when the process environment contains
`LLAMA_LAB_NO_MMAP_PREFETCH=1`. It does not disable subsequent demand paging,
change weight values, increase RAM, or guarantee the model fits. This variable
is a local patch interface, not an upstream llama.cpp flag.

The measured build uses MSVC14.50.35717, CMake4.1.2-msvc8 and Ninja, Release x64.
Initialize the x64 Visual Studio developer environment. In a new checkout of
that exact commit, apply the patch with `git apply`, then configure:

```powershell
cmake -S . -B build-host -G Ninja -DCMAKE_BUILD_TYPE=Release `
  -DBUILD_SHARED_LIBS=ON -DGGML_BACKEND_DL=ON -DGGML_CUDA=OFF `
  -DGGML_OPENMP=OFF -DGGML_NATIVE=OFF -DGGML_CPU_ALL_VARIANTS=OFF `
  -DGGML_AVX2=ON -DGGML_FMA=ON -DGGML_F16C=ON `
  -DLLAMA_BUILD_COMMON=OFF -DLLAMA_BUILD_TESTS=OFF `
  -DLLAMA_BUILD_TOOLS=OFF -DLLAMA_BUILD_EXAMPLES=OFF `
  -DLLAMA_BUILD_SERVER=OFF -DLLAMA_BUILD_APP=OFF -DLLAMA_OPENSSL=OFF `
  -DLLAMA_BUILD_NUMBER=11562 `
  -DLLAMA_BUILD_COMMIT=b2f036c0f138414dedc987446f1d9d802f920275
cmake --build build-host --target llama --parallel 4
```

Extract the verified runtime and CUDA archives into a **new directory**.
Preserve its original `llama.dll` as `llama.stock.dll`; replace only the new
directory's `llama.dll` with the build output. Keep stock ggml and CUDA/CPU
backends. Never overwrite the existing working installation. This mixed
compiler build requires local compatibility validation; a successful build
alone is insufficient.

Record `lab-runtime-variant.json` beside the executable with `id`, `base_commit`,
`llama_sha256`, patch hash, compiler and unchanged stock binary hashes. The
experimental profiles include an explicit `runtime_variant` ID and DLL digest.
Our recorded DLL is `7bf9b3b0549e64c06e2b55bf47235f056838eba7f5b70de62bc48457996d2009`.
A local rebuild can differ; inspect and record its identity in a separate
experimental profile rather than claiming it is the measured binary.

`lab.py` rejects an unrequested variant and a mismatched DLL. It removes inherited
prefetch overrides from ordinary profiles. It enables the switch only for an
explicit matching variant and records that choice in each launch receipt.

Validation so far: CPU and GPU greedy output of pinned `stories260K.gguf` is
byte-identical across stock, modified-default and modified-opt-in runtimes.
Explicit mmap/verbose logs confirm the switch executes. A guarded Qwen Q4 load
and API smoke also complete, with a normal requested stop. These checks do not
prove full numerical equivalence or candidate coding quality. Consult the
[task report](../../docs/tasks/2026-10-16-memory-and-candidate-expansion/2026-10-16-memory-context-and-expanded-model-tests-v0.4.0.md)
for the current result and remaining limitations.

## b11838 port for higher Flint precision

`loader-b11838.patch` applies to exact commit
`4231b23dc2c46661d01157aac5245bdcf03ce4b1`. Use a separate checkout and runtime
directory, the same build recipe above, and replace only `LLAMA_BUILD_NUMBER`
with `11838` and `LLAMA_BUILD_COMMIT` with that full commit. This local patch
adds the same opt-in guard around initial mmap prefetch; it does not change
attention, expert selection or subsequent demand paging.

The measured variant is `b11838-noprefetch-v1`, with DLL SHA256
`10331e86ab5bd3f8c08c486f42d900f1dd09dbab218ce54a8684b7ec7b65c35f`.
For newer variants, the profile and runtime manifest must also match an entry
in `catalog/runtime.json` under `reviewed_runtime_variants`. A locally edited
profile alone cannot authorize an unreviewed DLL. The historical b11562
validation remains supported without changing the production installation.

[Recorded controls](../../reports/2026-10-24-b11838-prefetch-control.json)
confirm 54 other stock binaries are unchanged and all six small-model CPU/GPU
runs match across stock, modified-default and modified-opt-in. Only opt-in
logs disabled prefetch. These controls do not prove full-model equivalence.
Higher-precision Flint profiles and their actual outcomes belong in the
[precision campaign](../../docs/tasks/2026-10-24-precision-and-gaps/2026-10-24-precision-and-coverage-v0.9.0.md).
