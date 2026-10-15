# Qwen placement: faster generation, one broken generated test

14 October 2026, Windows 11 / RTX 3080 10 GB / Ryzen 7 5800X / 64 GB RAM.
One controlled pair on the public router-v1 fixture. This is **not a model
leaderboard or a long-context evaluation**.

## Decision

Keep Qwen3.6-35B-A3B UD-Q4_K_M as the installed reference. The research's
`--gpu-layers all --cpu-moe` placement merits repeat testing: it finished in
3m25s versus 9m36s and generated about 23.7 versus 13.3 tokens/second. Both
implementations passed the independent merge-contract checks. However, the
faster answer supplied one failing test and a less complete bug explanation.
Do not promote it solely from this pair or delete the current weights.

The alternative spends more **system RAM**, not more VRAM. Its measured process
working set peaked at 19.76 GiB versus 17.18 GiB; its dedicated VRAM snapshot was
3.30 GiB versus 5.88 GiB. All routed experts are on CPU, including those that
previously occupied the GPU. Filling VRAM is not a useful target by itself.

## What was actually changed

| Setting | Reference | Alternative |
|---|---|---|
| Profile | qwen36-reference | qwen36-all-attention-proposed |
| GPU layers | 30 | all |
| Routed CPU experts | first 33 layers | all layers, using cpu-moe |
| Context / K and V cache | 65536 / q8_0 | Same |
| Generation / prompt threads | 4 / 8 | Same |
| Batch / microbatch | 256 / 64 | Same |
| Temperature / top-p / top-k / min-p | 0.6 / 0.95 / 20 / 0 | Same |
| Repeat penalty / seed | 1 / 73 | Same |
| Thinking / preservation | enabled / enabled | Same |
| Reasoning ceiling in benchmark | 2048 per model request | Same |
| Maximum output / whole-prompt deadline | 8192 per request / 1200 seconds total | Same |
| Loading / host prompt cache | non-mmap / cache-ram 0 | Same |

The default server reasoning ceiling remains unrestricted. The benchmark's
2048 ceiling was explicit and local to this comparison; it is **not native
xhigh**, and it has not been selected as a global quality setting. Runtime
properties advertise no reasoning_effort capability for this template.

Both used the full-hash-verified 22,134,528,992-byte GGUF and llama.cpp b11562,
commit b2f036c0f138414dedc987446f1d9d802f920275, CUDA 12.4. The
[numeric evidence](2026-10-14-placement-results.json) contains exact artifact
identity, flags, source hashes, output hashes and per-turn timings. The
[plan](2026-10-14-placement-plan.md) preceded answer collection.

The source research was read, not inferred from its title. Its archived text
hash is 7b8fca4934e47b6a0bfd281d91d3790e9aa3253faf11c9719966610b6ae7cc71.
See the [archive](../research/raw/2026-10-14-gemini/README.md) and separate
[critical review](../research/reviews/2026-10-14-gemini.md). We tested placement
alone, not its bundled temperature, min-p, batching and host-cache changes.

## Results

| Measurement | Reference | Alternative |
|---|---:|---:|
| Whole prompt | 576.453 s (9m36s) | 204.891 s (3m25s) |
| First final-answer text | 424.062 s | 127.828 s |
| Model requests | 3 | 2 |
| Successful file reads / unique files | 14 / 7 | 7 / 7 |
| Total generated tokens, including thinking/tools | 7475 | 4614 |
| Weighted generation speed | 13.34 tok/s | 23.67 tok/s |
| First-turn uncached prefill, 654 tokens | 153.56 tok/s | 149.21 tok/s |
| Peak sampled process working set | 17.18 GiB | 19.76 GiB |
| Dedicated process VRAM snapshot | 5.88 GiB | 3.30 GiB |
| Minimum system free RAM | 7.11 GiB | 6.01 GiB |
| Minimum system free VRAM | 1322 MiB | 4083 MiB |
| Peak sampled GPU core temperature | 53 C | 53 C |
| Independent behavior groups | 6/6 | 6/6 |
| Model-written unittest tests | 7/7 pass | 6/7 pass |
| Provisional Codex-assessed rubric | 39/40 | 38/40 |

Generation speed aggregates server timings as sum(predicted_n - 1) divided by
sum(predicted_ms / 1000). The roughly 2.81x whole-prompt improvement includes
fewer generated tokens and one fewer file-reading round. It is not a 2.81x
kernel-speed measurement. Generation throughput improved about 1.77x; the
first short prefill did not improve. No conclusion about 39K-token editor
requests follows from this 654-token initial prompt.

All seven synthetic files were successfully returned. The reference requested
the same seven again after receiving them. Inspection of the runtime's rendered
second-request prompt confirmed the contract, code, host facts and prior
reasoning were present. The redundant turn reached the 2048 thinking ceiling,
but that association does not establish why the repeat occurred. It recovered
and completed normally. Both runs reused live prefix KV across tool turns;
neither is a fully cold multi-turn prefill benchmark.

## Quality findings and grading

Both answers identified v2 precedence, explained that a path mention is not a
file read, cited the actual synthetic files, and declined to invent the absent
Redis sentinel port or PostgreSQL failover timeout. Both explicitly admitted
they had not executed tests. The evaluator ran their code only afterward.

Both corrected functions use deepcopy and recurse only when both values are
dictionaries. Each passed the six rubric groups: nested defaults/unknown keys,
false and empty values, dict/scalar conflicts, deep mutable isolation, repeated
calls and invalid roots. This is evidence against claiming that this particular
Q4 cannot produce correct alias-safe code. It says nothing causal about another
quantization's errors.

The reference tests pass, but their nested-list check mutates a result copied
from overrides and then checks only defaults. It does not actually assert that
the corresponding nested override stayed unchanged. Empty-string/empty-dict
and scalar-to-dict cases are also missing from its own tests.

The alternative includes this contradictory assertion:

```python
# res["items"] was [3, 4]
res["items"].append(5)
self.assertNotIn(5, res["items"][:3])
```

The slice is [3, 4, 5], so the assertion fails even for the correct function.
It checks the result, not the original override. Its explanation also omits
explicit unknown-key dropping and does not clearly describe both type-conflict
directions. Both answers overgeneralize the buggy function's invalid-root
behavior; some inputs raise incidental errors, rather than silently succeeding.

| Rubric category | Maximum | Reference | Alternative |
|---|---:|---:|---:|
| Instruction discovery | 8 | 8 | 8 |
| File grounding | 6 | 6 | 6 |
| Unknown-fact honesty | 6 | 6 | 6 |
| Verified code behavior | 12 | 12 | 12 |
| Test assertions + execution honesty | 5 | 4 | 3 |
| Actual-read inventory | 3 | 3 | 3 |

The one-point difference is reviewer judgment about test quality, not a
statistically established quality difference. The existing rubric does not
separately score exhaustive prose bug enumeration. Its high totals should not
hide those omissions. Both requested all advertised files in one batch rather
than establishing a sequential AGENTS-to-router discovery trace. The reference
describes that sequence more confidently than the trace supports. Inventory
credit means the listed files were actually read, not that this demonstrated
unassisted exploration of an unseen repository.

The Codex-authored [behavior checks](../benchmarks/checks/router_v1.py) were
written **after answer collection**, from the pre-existing contract/rubric.
They are transparent verification, not a held-out evaluation. A negative
control using the deliberately buggy fixture failed all six groups (11 failed
subtests and 14 errors), confirming the checks reject the known broken code.

Execution used existing Ubuntu 26.04.1 under WSL, Python 3.14.4 and bubblewrap:
separate namespaces, no shared network, no host homes/Windows mounts, only
three selected read-only source files, 512 MiB address-space/10-second CPU/
20-second process limits. Two initial preflight attempts rejected bubblewrap's
PWD environment variable before any candidate ran; the allowlist was corrected
and checked against /work. See [grading instructions](../docs/grading.md).

## Memory, KV and stability interpretation

Apps stayed open; CPU/GPU were reported stock and RAM remained at the accepted
2800 setting. Unloaded free RAM was about 22.9 GiB before the reference and
25.1 GiB before the alternative. Desktop usage changed; minimum system-free
numbers are observations, not clean model-allocation deltas. Light maintenance
and two brief test-suite runs occurred during the reference, so this is a
desktop pilot, not a noise-free microbenchmark.

The exact current weight/KV/state/compute buffer split is unavailable at the
saved log verbosity. Do not substitute historical allocation numbers for a
fresh measurement. Process private commit was about 23.52 GiB in both runs;
that is not resident RAM and must not be added to working-set measurements.
VRAM figures are Windows dedicated process-counter snapshots, not peaks or
shared system memory. The 5-second telemetry may miss short transients.

KV remained q8_0 at 64K in both profiles. This was **not an all-RAM-KV test**.
The alternative already leaves substantial VRAM free while using more host RAM;
moving KV to RAM is not the obvious next improvement. A configured 64K window
does not prove 64K recall, preserve every file automatically, or keep a session
alive after the server stops. Files must reach the prompt, and client pruning
and output reservations still matter. cache-ram 0 does not disable live-slot
prefix KV reuse; the runtime measured reuse in both runs.

No new WHEA event or reboot was observed during the experiment window. This
does not diagnose previous restarts or prove hardware stability. Both owned
servers stopped on explicit stop-file requests after collection; no load/stop
guard was bypassed. No editor configuration, driver, clocks or weights changed.
No cloud calls or API budget were used. Production port 8080 remains unchanged
and no experiment server remains loaded.

## What to try next

1. Repeat the alternative and reference before promotion; add a held-out task
   and measure a larger prefill. Compare 2048 against unrestricted native
   thinking under the same 20-minute whole-prompt deadline. Do not combine
   sampling, batching, KV placement and reasoning changes in that comparison.
2. Next distinct model: **Gemma 4 26B-A4B IT, official QAT Q4_0**, pinned fixed
   revision in [the catalog](../catalog/models.json), initially 32K/q8. Its
   13.45 GiB file is substantially smaller than Qwen's 20.61 GiB file, making
   it a useful memory-headroom candidate while apps remain open. That is a fit
   rationale, not a coding-quality claim. Verify load/template/native thinking
   and at least three tool rounds before the full task.
3. Then test GLM-4.7-Flash UD-Q4_K_XL if its measured host allocation fits. Keep
   Q5, dense models and all-RAM KV deferred until their memory/prefill cost is
   justified. Long-history and stale-file tasks plus real editor completion
   remain required before choosing a replacement.

New weights have not been downloaded or deleted. Raw requests, reasoning,
answers and host logs remain in ignored local-data; this report and its JSON
are reviewed public aggregates.

## Reproduction and tooling validation

Use a fresh output directory for every collection. With the existing verified
assets, the reference was started with the equivalent command below (the local
Python executable was selected explicitly):

```powershell
python lab.py --data-dir local-data/placement/reference run --profile qwen36-reference --runtime-dir E:\llm\llama.cpp --model-path E:\llm\models\Qwen3.6-35B-A3B-UD-Q4_K_M.gguf --port 8081 --stop-file local-data/placement/reference.stop --apply
python benchmark.py --endpoint http://127.0.0.1:8081/v1 --model qwen36-lab --mode tools --deadline 1200 --reasoning-budget 2048 --max-tokens 8192 --temperature 0.6 --seed 73 --output local-data/placement/reference-tools
```

After collection, create the stop file, wait for the owned child to exit and
recheck free memory. For the second load, change the profile to
`qwen36-all-attention-proposed`, use distinct alternative data/stop/output paths,
and keep every benchmark argument identical. The original alternative launch
also used `--experimental`; its profile now records the completed load test.
Do not run both servers at once. Dedicated-memory snapshots use
`scripts/capture-gpu.ps1`; grading commands are in [grading.md](../docs/grading.md).

`python -m unittest discover -s tests -v` passed all 16 local Windows checks.
Both PowerShell scripts parsed, `python scripts/audit_public.py` reported zero
findings across 55 Git-visible files, relative documentation links resolved and
`git diff --check` passed. The implementation's [Windows and Ubuntu CI jobs](https://github.com/paras-lehana/local-coding-lab/actions/runs/38613307654)
passed; the Windows-only lifecycle test is skipped on Linux. There were no new
Python or system package installations. The model-test failure reported above
is evaluation evidence, not a failing lab-tooling test.

The collector's original result files remain `scored: false`; reviewed scoring
is recorded separately in this report and the aggregate JSON. Do not rewrite
the raw collector result to make it appear to have performed source grading.
Attribution correction, 15 October: these semantic assessments and independent
checks were produced by Codex, not independently reviewed by a human. Original
scores and raw evidence remain unchanged.
