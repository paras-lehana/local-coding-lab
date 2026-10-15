# Local Coding Lab

**Find a local coding model that follows your project instructions, reads the
right files, and finishes useful work on your actual PC.**

This is a Windows + NVIDIA + llama.cpp research lab, with pinned downloads,
guarded launch profiles, public benchmark questions, and honest experiment
reports. It grew out of testing on an RTX 3080 10 GB / Ryzen 7 5800X / 64 GB RAM
PC with everyday applications left open. Other hardware needs its own profile.

**Status: v0.3.9, experimental; model campaign reviewed, editor UI pending.** Follow the
[live campaign evidence](reports/2026-10-15-campaign.md). Repeated coding,
long-document, changed-file and actual-instruction tests now cover Qwen,
Gemma, GLM, Kimi and Qwen Coder. A working Qwen profile is selected and its
production API/tool calls pass. Fresh editor validation is blocked by an
unavailable interactive desktop. Clean-machine installation remains unvalidated.

## Start here

| I want to… | Read / run |
|---|---|
| Install and try a model | [Windows walkthrough](docs/setup.md) |
| Understand which model to try | [Shortlist and exact links](docs/models.md) |
| Know which coding tasks need extra checking | [Measured use cases and limitations](docs/coding-use-cases.md) |
| See what actually worked | [Current campaign](reports/2026-10-15-campaign.md), [placement experiment](reports/2026-10-14-placement.md), [historical results](reports/2026-10-14-findings.md) |
| Share the campaign outcome | [Forwardable task report](docs/tasks/2026-10-15-autonomous-model-campaign/2026-10-15-model-comparison-and-editor-validation-v0.3.9.md) |
| Understand RAM, VRAM and KV cache | [Memory guide](docs/memory-and-context.md) |
| Connect VS Code | [Editor guide](docs/editors.md) |
| Compare models fairly | [Run a comparison](docs/run-a-comparison.md), [methodology](docs/methodology.md), [questions](benchmarks/questions/router-v1.txt), [rubric](benchmarks/rubrics/router-v1.md) |
| Check generated code | [Optional isolated grading](docs/grading.md) |
| Read the supplied research | [Original research](research/raw/2026-10-14-gemini/README.md), [critical review](research/reviews/2026-10-14-gemini.md) |
| See what comes next | [Experiment plan](docs/next-experiments.md) |

## Quick start

Requires Windows 11, a CUDA-compatible NVIDIA driver, Git and Python 3.11+.
The lab's Python tools use the standard library; no pip installation is needed.
For this workstation, clone and keep every downloaded artifact under `E:\llm`:

```powershell
git clone https://github.com/paras-lehana/local-coding-lab.git E:\llm\local-coding-lab
cd E:\llm\local-coding-lab
python lab.py doctor
python lab.py list
# Preview only: does not download or start inference.
.\scripts\setup.ps1 -Model gemma4-26b-qat
# After reviewing the model license, disk space and memory requirements:
.\scripts\setup.ps1 -Model gemma4-26b-qat -Apply
```

Use `-Python E:\llm\python\Scripts\python.exe` if Python is not on PATH.
Use `-DataDir E:\llm\lab-data` to choose another data directory. Otherwise
downloads go to ignored `local-data/` inside the clone. Existing installations,
models and editor settings are never overwritten. The runtime is pinned to
**b11562 / CUDA 12.4**, including its CUDA DLL bundle; this is a reproducibility
choice, not a claim that it is the latest or best build.

The [setup guide](docs/setup.md) continues through explicit server start, health
checks, benchmark collection, and stopping. Installation does not start a model.
Gemma's Python checks pass. Its unrestricted 64K follow-up also passes all six
SQL groups and five of six TypeScript groups, but its capped actual-instruction
audit misses files and produces a different merge bug. It is not a demonstrated
upgrade across the full workflow or real editors. Follow the evidence above.

## What the evidence says

- On router-v1, Qwen's alternative GPU/CPU placement finished in **3m25s versus
  9m36s**, at **23.7 versus 13.3 generation tok/s**. Both implementations passed
  the independent behavior checks; its generated tests scored 6/7 versus 7/7.
  Process RAM rose from 17.18 to 19.76 GiB. One pair does not establish quality
  superiority or long-context reliability. [Full results and limits](reports/2026-10-14-placement.md).
- Qwen3.6-35B-A3B UD-Q4_K_M is the current measured reference. An older profile
  completed the private instruction/code audit at **31/36 in 14m24s**, with bugs.
- A short follow-up produced **3/7, 5/7 and 7/7** code checks with different
  thinking budgets. The 7/7 run also changed placement/context and still made
  instruction/citation mistakes. This is not a clean reasoning ranking.
- The previous dense Qwen3.8 setup missed the **20-minute whole-prompt limit**.
  That rejects the tested setup, not every possible dense model.
- Recent memory pressure stopped inference twice. Today's free memory must be
  checked; installed RAM and yesterday's fit are insufficient.

**Working choice:** Qwen3.6 UD-Q4 with the
[`qwen36-instructions-64k`](profiles/qwen36-instructions-64k.json) profile:
30GPU layers,34CPU expert blocks,64K q8 KV and native thinking. It uses about
5.38GiB dedicatedVRAM and peaks at18.09GiB processRAM in the finalist suite.
Its31/36 private answer is a byte-identical historical replay, not an independent
accuracy sample. Three public Python answers score6/6,6/6,4/6; TypeScript5/6,
SQL fails;52K history passes. This is supervised drafting assistance, not
unattended coding certification.

The [2GiB expert-cache alternative](profiles/qwen36-cache2048-batch512-candidate.json)
is much quicker and passes all three public Python implementations, but scores
27/36 on the private audit and fails strict TypeScript. Gemma26QAT is retained
for lower RAM use; its private audit scores19/36 despite good public Python and
one passing SQL migration. Higher weight precision did not establish a complete
workflow improvement. [Selection and exact evidence](reports/2026-10-15-campaign.md#final-profile-comparison-and-working-choice).

After downloading the pinned Qwen artifact using the setup guide, preview the
selected profile with `python lab.py run --profile qwen36-instructions-64k`.
Add `--apply` to start after reviewing available memory. Stop the existing
server before trying another profile. The lab never loads two copies together.

A later unexpected shutdown interrupted GLM Q5's private audit. Its cause is
unresolved; do not interpret the crash monitor's popup as a component diagnosis.
The earlier planned Windows Update restart is a separate event. Recovery checks
and interrupted-attempt records are in the current report.

## Repository map

```text
catalog/                 pinned model and runtime metadata
profiles/                historical reference and explicitly proposed settings
scripts/                 Windows bootstrap and publication audit
benchmarks/fixtures/     synthetic project with deliberate bugs
benchmarks/questions/    frozen evaluation prompts
benchmarks/rubrics/      source-review criteria, never sent to the model
reports/                 curated measurements and their limitations
research/raw/            external research, preserved separately
research/reviews/        fact checks and decisions
docs/                    setup, methodology, plans and project log
local-data/              ignored downloads, binaries, answers and telemetry
```

Run `python -m unittest discover -s tests -v` and
`python scripts/audit_public.py` before contributing. See [CONTRIBUTING.md](CONTRIBUTING.md)
and [SECURITY.md](SECURITY.md). Original lab code/docs are MIT; external research,
model weights and llama.cpp retain their respective rights/licenses.
