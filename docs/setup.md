# Windows setup and first run

## 1. Check the machine

Run `nvidia-smi` and `python lab.py doctor`. The CUDA version displayed by
nvidia-smi describes driver capability, not an installed toolkit. The pinned
runtime comes with a separate CUDA DLL archive; a full developer CUDA toolkit
is not required for this binary workflow. No drivers or BIOS settings are changed.

Python must be 3.11 or newer. If it is absent, install Python from
[python.org](https://www.python.org/downloads/windows/), choosing a location on
your installation drive. This bootstrap intentionally does not install Python,
Git, drivers or machine-wide packages for you.

Check available disk space too. Gemma's GGUF is 13.448 GiB; runtime downloads
are about 626 MiB, and extraction needs additional space. Reserve at least
18 GiB for that first installation, more for comparison models/results.
GPU memory already used by your desktop is unavailable to the model.

## 2. Preview, then install

From the repository root:

```powershell
.\scripts\setup.ps1 -Model gemma4-26b-qat
.\scripts\setup.ps1 -Model gemma4-26b-qat -Apply
```

Or use the cross-platform planning/downloading CLI directly:

```powershell
python lab.py --data-dir E:\llm\lab-data install-runtime --apply
python lab.py --data-dir E:\llm\lab-data download-model gemma4-26b-qat --apply
```

These install **Windows** binaries even when planning/download code runs on
another OS. Review publisher model licenses linked in the catalog before use.
The downloader is anonymous; gated repositories require separately obtaining the
exact permitted file. Never put a token in a URL or commit one to this repository.

Downloads resume via HTTP Range and verify full byte size and SHA256 before
publishing the final file. An existing file is verified, not overwritten.
On a hash mismatch, preserve the `.part` file for inspection; remove only that
specific invalid partial when ready to retry. No automatic weight deletion occurs.
Runtime installation refuses an existing destination. Use `-SkipRuntime` on a
later setup call to download another model with the same installed runtime.

## 3. Preview a launch

```powershell
python lab.py run --profile gemma4-smoke-proposed --experimental
```

This profile is **not validated on this PC**. It proposes 32K context, q8 K/V,
all non-expert blocks on GPU, CPU experts, small batches and thinking enabled.
The default sampling/template behavior must be recorded and checked on the
first load. Its 16 GiB RAM / 6500 MiB VRAM preload gates are conservative
starting estimates, not guarantees. Stop if fit or parser behavior is wrong.

Start explicitly after inspecting the printed command:

```powershell
python lab.py run --profile gemma4-smoke-proposed --experimental --apply
```

Keep that terminal open. It owns the child server. Ctrl+C stops that child.
For an automated experiment, pass `--stop-file local-data/experiment.stop`
at launch, then create that file from another terminal to request a stop.
The file must not exist before launch; use a fresh name for each experiment.
The launcher saves the owned PID in `process.json`, samples its resident and
private memory, and records `requested_stop` when this stop method is used.
There is no boot service or restart loop. Logs/telemetry live under
`local-data/runs/server-.../`. On this host the launcher stops when physical RAM
falls below 2.5 GiB, dedicated free VRAM below 400 MiB, GPU core reaches 84 C,
or a new WHEA hardware event is observed. Polling cannot prevent sudden hardware
faults; a process stop is not a diagnosis of any historical PC restart.

You can reuse known local assets without copying them:

```powershell
python lab.py run --profile qwen36-reference --runtime-dir E:\llm\llama.cpp --model-path E:\llm\models\Qwen3.6-35B-A3B-UD-Q4_K_M.gguf
```

Add `--apply` only to start it. This profile requires 20.5 GiB free RAM and
6500 MiB free VRAM. Reusing files does not change the original installation.
An occupied port is a stop condition, not permission to kill another server.

For a dedicated GPU-memory snapshot of the PID from `process.json`, run:

```powershell
.\scripts\capture-gpu.ps1 -ServerPid 12345 -OutputPath local-data/gpu-snapshot.json
```

Use the actual PID. This reads Windows dedicated-memory counters, not shared
system RAM. A missing counter is an error, not a zero-use measurement. System
free VRAM also includes desktop applications, so it is a separate measurement.

## 4. Verify before opening an editor

From a second terminal:

```powershell
Invoke-RestMethod http://127.0.0.1:8080/health
Invoke-RestMethod http://127.0.0.1:8080/v1/models
```

Wait for successful health and the expected alias (`gemma4-lab` or `qwen36-lab`).
The launcher printing a PID means loading began, not that the API is ready.
Start with a small prompt, inspect actual model/KV/compute allocations and
native reasoning output, then try the [benchmark](methodology.md).

## Troubleshooting

| Symptom | Check |
|---|---|
| PowerShell blocks the script | Use the equivalent Python CLI; no policy change is necessary |
| DLL missing | Both pinned archives must be present; inspect installation.json and server log |
| Download 401/403 | Publisher access/license restrictions; do not substitute random mirrors |
| RAM gate fails | Keep the server stopped or select a smaller measured profile; do not bypass the floor |
| Low VRAM usage / editor spins | Check process, health, model alias, resource-stop logs and prompt-processing counters |
| OOM despite a small GGUF | Include host buffers, KV, compute, desktop VRAM and loading transients |
| Syntax looks good but behavior fails | Test type conflicts, false values and nested mutable aliases |

No model was installed or loaded by the repository creation task. The install
path has been exercised with fake HTTP archives and dry runs, not a clean-PC
end-to-end download of every multi-gigabyte model.
