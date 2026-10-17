# Strata on a 10 GB Windows GPU

Experiment started 18 October 2026. No production model selection has changed.
The requested article is a research lead, not a benchmark on this machine.

Pinned upstream: `Niko1221/Strata` v0.1.45, source
`477ac13cbe8e582c20484871ce459d20d82df09d`.
Windows CUDA archive: 165243142 bytes, SHA256
`a1d4cafb8319c253f3010ff118dbd5ed07c232056b939ac7735819559f3b859e`.

## Frozen starting plan

1. Verify whether 12 GB is enforced. Current upstream setup explicitly accepts
   the RTX 3080 10 GB with a speed warning; its agent guide mentions 8 GB.
2. Try our existing Qwen3.6 Q4 GGUF with MTP off. First use an 8K context,
   small GPU expert budget and a short native benchmark under resource guards.
3. If it fits, compare source-grounded coding and changed-file/history prompts
   using the lab's existing frozen fixtures. Record KV placement and actual
   inference controls; Strata's Qwen3.6 path does not use Flash-Next KV flags.
4. Evaluate Flash-Next memory/disk requirements with apps open before choosing
   its artifact. Favor correctness; a smaller pruned Coder is a different model.
5. Compare completed results to the existing llama.cpp baseline, separating
   runtime, quantization, model and context changes. Do not claim a 6x speedup
   from unlike models or incomplete answers. Retain the working Qwen baseline.
6. Consider a fork only if an identified limitation needs code changes. An 8 GB
   capacity simulation on a 10 GB card is not a real 8 GB hardware validation.

`guard.py` runs an explicit private JSON command in a Windows kill-on-close job,
checks free physical/commit/VRAM headroom and new WHEA events, and saves telemetry.
It requires Strata's installed Python environment and reviewed upstream
`serve/winjob.py`. A `stop.request` in the run folder stops only this owned tree.
It refuses a concurrent llama-server. It is experimental, not a generic launcher
or a replacement for production lifecycle controls.

## Source fork and actual progress

[Experimental fork](https://github.com/paras-lehana/Strata/tree/experiment/qwen36-no-mtp),
with separate compatibility, pageable-arena and Windows source-view-trimming
commits. Its README explains the CUDA-only validation and remaining limits.
Read the [full task report](../../docs/tasks/2026-10-18-strata/2026-10-18-strata-on-10gb-v0.6.0.md)
before attempting a profile. A32K native smoke pass did not make the first API
profile safe: a later tool request crossed the VRAM floor. The64-token/no-graph
profile completes router-v1, history and TypeScript/SQLite collection. Results
include correct Python/history and observed TypeScript/SQLite defects.

The same-weight llama control also passes Python/history and scores TS5/6,
but its SQLite migration passes6/6. See [measured results](../../reports/2026-10-18-strata-qwen.json).
These are single-sample32K practical configurations. Keep the128K production
baseline; no editor or actual8GB result is implied.

The successful source build used CMake Release, CUDA enabled, sm86,
`STRATA_PORTABLE=ON`, `STRATA_Q6K_EXPERTS=ON`, `STRATA_MMQ_KQUANTS=ON`,
`STRATA_BUILD_TESTS=ON`, shared CUDA runtime and the manifest's pinned GGML.
Build target `strata-q36` with four jobs. CUDA13.3.33/MSVC14.50/CMake4.4.3
were isolated for this host; do not treat those paths as a global installer.
The fork document gives the native smoke command. For API serving use:

```text
--native <verified-Qwen-GGUF> --max-context 32768 --prefill 64
--mtp 0 --expert-vram 0.25 --cpu-threads 8 --no-graph
```

Set `STRATA_Q8_PACKED=0`, `STRATA_Q36_NO_MMQ=1` and
`STRATA_Q36_TRIM_GGUF=1` in the experiment child environment. The winning
serving profile does not use pageable experts. Strata's server JSON selects
the source-built executable, a tokenizer extracted from that GGUF, loopback
host, a separate port and the correct isolated CUDA DLL directory. The tested
template copy explicitly enables reasoning preservation; upstream frontend
kwargs do not forward that option. Preserve the original template/hash.

Run the explicit server command through `guard.py --config <private.json>
--output <new-private-run-directory>`. The configuration supplies `strata_root`,
absolute `command`, `lib_dirs`, child `env`, `max_seconds`, and the same guard
keys used in lab profiles. Tested load floors:22GiB RAM,24GiB available commit,
6000MiB VRAM; runtime floors:2.5GiB RAM,2GiB commit,600MiB VRAM,84C maximum.
The output directory's `stop.request` ends only that job. Stop production
through its ownership-aware controller before starting; restore it afterward.
Do not paste an experimental command into the production launcher.

## Pinned downloads

`artifacts.json` identifies exact revisions, byte counts and hashes. The download
helpers do not run an installer or start inference:

```powershell
python experiments/strata/download.py --data-dir E:/llm/Strata-data/models/flash-next
# Alternative: bounded parallel HTTP ranges, resumable completion journals.
python experiments/strata/range_download.py --data-dir E:/llm/Strata-data/models/flash-next --connections 8
```

Run only one downloader against a destination. Stop the first before switching.
The range helper can adopt a contiguous `.part` from the simple HTTP helper;
it cannot resume a sparse/random Xet incomplete file. Range files can have the
full final length before any range completes: use the journal's completed ranges,
not file length, to report progress. Only a complete byte-count/SHA256 match
publishes a `.gguf`. No model quantization or conversion occurs in a download.
Default concurrency is8; up to64 is accepted for a high-latency route. Each
connection reads at most1MiB at once. On this host64connections used about
140MiB RSS; this is a snapshot, not a portable memory ceiling.

Use `tools/iq_pack.py` from the pinned Strata checkout after both shards verify;
omit `--experts-bin` for direct GGUF views to avoid another roughly40GiB copy.
Its float conversion helpers and the optional MTP tools need llama.cpp's
`gguf-py` at the pinned commit in `setup.py`. If installing components manually,
set `STRATA_GGUF_PY` in the preparation process to that checkout's `gguf-py`
directory. This host reuses the already verified GGML/llama source checkout;
the Python import and Q2_0 enum check pass. No global Python package is replaced.
The experimental Flash-Next configuration must use a bounded resident expert
budget with apps open. Its `--kv-resident` and `--kv-grow` are different modes;
elastic growth requires every expert in RAM and cannot be assumed compatible
with the bounded resident tier. These controls do not apply to the Qwen3.6 path.

The native Flash pack requires `--spec 2` or greater even without MTP. To
measure no-draft inference, omit `--mtp`, use `--suffix-draft 0` and confirm
zero proposed drafts in the native timing log. This host's1200MiB reserve
crossed the600MiB free-device guard;3072MiB loaded. The quality profile sets
`STRATA_ROUTE_TAIL_SKIP=0` because the default7 omits some missed lower-ranked
expert contributions. Automatic prefill resolves to2304tokens here; record its
effective value. The32K/int8,10GiB expert-budget run passes the history case
but times out on both coding cases. It is not a recommended replacement.
See [Flash evidence](../../reports/2026-10-18-strata-flash.json) for every trial.

## Monitor checks

Use the isolated Strata Python environment for `guard.py` and `check_guard.py`:
they need `psutil` and the pinned checkout's `serve/winjob.py`. The latter checks
a forced preflight refusal, an owned-job resource stop and a nonzero deadline;
a separate harmless process must survive. Its evidence belongs outside Git.

`python -m unittest tests.test_strata_download -v` serves tiny synthetic HTTP
ranges, rejects wrong ranges and a wrong whole-file hash, and resumes
interrupted allocation/download state.
