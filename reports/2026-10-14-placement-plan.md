# Qwen placement experiment — frozen plan

Planned before collecting answers, 14 October 2026, 23:12 IST.
Source research: research/raw/2026-10-14-gemini/report.txt, SHA256
7b8fca4934e47b6a0bfd281d91d3790e9aa3253faf11c9719966610b6ae7cc71.

Question: does moving all eligible non-expert computation onto the GPU, with
all routed experts on CPU, improve file-tool work within the memory/deadline
limits compared with the existing Qwen profile?

Reference: qwen36-reference. Treatment: qwen36-all-attention-proposed. Both use
the exact existing Qwen3.6 UD-Q4_K_M and llama.cpp b11562, 64K context, q8 K/V,
4/8 generation/prompt threads, b256/u64, native thinking/preservation enabled,
temperature 0.6, top-p 0.95, top-k 20, min-p 0, repeat penalty 1, non-mmap and
cache-ram 0. Only GPU/expert placement changes. The treatment's larger preload
gate is a safety condition, not a performance-setting change.

Begin with health/model identity and a short smoke request. Then collect the
public router-v1 tools task at seed73, per-request reasoning budget2048,
max output8192 and whole-prompt deadline1200seconds. This bounded first comparison
does not promote a global 2048 ceiling or replace native reasoning controls.
Record uncached/reused prompt tokens; do not call this a cold microbenchmark
without verifying actual cache state. Record each successful file read and
compare final citations and absent-fact handling against the frozen snapshot.

If available memory prevents the treatment, report that preflight outcome.
Do not lower the guards or infer the performance from another machine's result.
Do not add prompt cache, alter sampling or increase batches in this comparison.
No model-produced code runs on the Windows host. Behavioral scoring needs a
separate restricted environment; manual code review is explicitly provisional.

Memory: record total free RAM/VRAM, owned process working set/private bytes,
loader model/KV/state/compute buffers and GPU temperature. Stop on 2.5GiB RAM,
400MiB VRAM, 84C or a new WHEA event. Preserve logs and incomplete responses.
One server at a time on isolated localhost:8081; production8080 remains unchanged.

This is the first public-fixture placement comparison, not the historical private
36-point audit, a full long-history test or proof of a universally better model.
