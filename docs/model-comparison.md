# Current model comparison

Updated 23 October 2026. Components and completion gates matter more than a
single leaderboard number. Claude's newer campaign was private; this table
brings its reviewed summary into the public lab. Results are agent-assessed,
not independently human-reviewed. It is not a controlled universal ranking.

| Candidate | Private /36 | Public /60 | Coding /12 | Practical result |
|---|---:|---:|---:|---|
| Qwen3.6 35B-A3B UD-Q4_K_M, mapped64 | 31 | 52 | Not collected | Retained leader on available components; private 699.7 s; SQL failure and aliasing diagnostics remain |
| Qwen3.6 Q5 | 28 | Separate historical cases | Not comparable | Lower private score; retired |
| Qwen3.6 Q6 | 28 | Historical completed cases | Not comparable | Private 2099.7 s, exceeds current gate; retired |
| GLM-4.7-Flash UD-Q4_K_XL, f16 KV | 27 | Separate historical cases | Not comparable | Private 942 s, below Qwen on this audit; retired |
| Gemma 4 26B-A4B QAT Q4_0 | 19 | Separate historical cases | Not comparable | Retained lower-memory fallback; private 400 s |
| Gemma 4 31B dense QAT Q4_0 | 26 | Historical completed cases | Not comparable | Private 7234 s; fails current latency gate; retired |
| Qwen3-Coder-Next 80B Q4 | Unscored | Separate historical cases | Not comparable | Private tool-loop limit after 4075 s; retired |
| Qwen3-Coder-30B UD-Q4_K_XL | Deadline | Separate historical cases | Not comparable | Public cases complete, private 1200 s deadline |
| Kimi-Linear 48B Q4 | Capacity rejection | Separate historical cases | Not comparable | Not evidence of poor answer quality; retired |
| Qwen3.8 27B dense Q6 / TQ3 | Unscored | Interrupted | Not collected | Roughly 1.4-2.1 decode tok/s; long requests/restart, not promoted |
| Qwen3.8-Flash-Next 125B, Strata IQ3_XXS | Not completed | Coding deadlines; empty history final | Not collected | Separate replays recover facts; not a retroactive workflow pass; retired |
| Bonsai 2 27B PQ2_0 | Not run | Stopped | Not run | Partial CPU placement only 2.3 tok/s; retired |
| Bonsai 2 27B PTQ1_0 | Not run | Deadline | Not run | Full GPU, router exceeds 1200 s after one tool turn; retired |
| LFM2.5 24B-A2B QAD Q4_0 | Deadline | 48 | 6 completed passes of 12 | Private reasoning loop; coding includes deadline/truncation, so 6/12 is task completion, not twelve completed correctness grades; retired 23 October |
| Qwen3.6 UD-IQ4_XS | Not run | Router 39/40 only | Not run | TS/SQL interrupted by RAM guard; not a complete public score |
| Qwen3.6 UD-IQ3_S | Not run | No complete router answer | Not run | First attempt capacity-rejected; second stopped below 400 MiB free VRAM; stale running manifest corrected in this summary |
| K2 Horizon MoVA 36B-A4B Q4 | Not run | Not run | Not run | Downloaded, queued; no demonstrated apps-open fit |
| Nemotron 3.5 Bolt 74B-A9B 24GB | Not run | Not run | Not run | Downloaded, queued; no demonstrated apps-open fit |
| Recursive Flint UD-IQ3_XXS, uncapped reasoning | Not run after gate failure | Router deadline | Not run after gate failure | 1200.031 s, seven reads, zero final text; clean shutdown, unscored |
| Recursive Flint UD-IQ3_XXS, CPU KV, 2048 cap | Not run after gate failure | Router deadline | Not run after gate failure | 1200.016 s; visible planning after cap, no finished answer |
| Recursive Flint UD-IQ3_XXS, GPU KV | In progress | Router39/40; TS/SQL tool limit; history output limit | Pending | Router522.985 s,6/6independent groups; only1of3public workflows completes, no valid /60total or promotion |

## What changed in Claude's work

- Added the twelve-task executable suite and a consistent 50/30/20 scorecard;
  regraded the public baseline as 52/60 and LFM as 48/60.
- Returned to a strict 1200-second gate. Earlier two-hour or six-hour runs
  remain useful diagnostics but cannot rank as usable everyday completions.
- Demonstrated paging/thrashing with apps occupying about 56 GiB: a roughly
  20 GiB model slowed to 0.3-2 tok/s. Commit capacity did not establish RAM fit.
- Used CPU affinity excluding logical CPUs 0/1 after core-0 machine-check
  records. This is a precaution, not proof of the faulty component or a cure.
- Added candidate/runtime pins and exact-file retirement receipts. These
  unpublished changes are preserved; report coverage is still incomplete.

## Our assessment

Qwen Q4 remains the retained quality reference, not a guarantee of fit under
today's application load. More quantization bits have not consistently improved
these tasks. Fast generation did not rescue Bonsai's incomplete workflow; LFM's
good public router score did not predict private instruction reliability. Test
the actual file-reading and code contracts, not a greeting or tokens/second alone.

Claude's displayed 86.3 for Qwen combines only private and public components
after renormalization. No complete three-suite leader exists. Keep component
scores visible and collect comparable missing components before declaring a
new composite winner. Current driver 621.01 differs from the earlier 617.42;
timing comparisons across those conditions are observational.

On this desktop,10GiB GPU memory is not all available to inference: applications
already occupy roughly3GiB. Flint's short probe uses5.097GiB dedicated GPU memory
and10.377GiB peak process RAM, leaving about1.4GiB device VRAM at its lowest
sample. Filling the remaining VRAM is not itself an optimization target; the
profile must retain scratch/headroom under real prompts. Its13.537GiB mixed
GGUF is a constrained experiment, not the publisher's distilled NVFP4 artifact.
No conclusion about higher Flint quantizations follows from this one profile.

## Reports and provenance

- [Flint standalone record](tasks/2026-10-23-flint/2026-10-23-recursive-flint-v0.8.0.md)
- [All-model inventory through 17 October](tasks/2026-10-17-complete-model-inventory/2026-10-17-all-models-gemini-and-availability-v0.4.1.md)
- [Matched Q4/Q6 and expanded candidates](tasks/2026-10-16-memory-and-candidate-expansion/2026-10-16-memory-context-and-expanded-model-tests-v0.4.0.md)
- [Strata](tasks/2026-10-18-strata/2026-10-18-strata-on-10gb-v0.6.0.md)
- [TurboQuant](tasks/2026-10-19-azllm/2026-10-19-azllm-and-turboquant-v0.7.0.md)

Private source records reviewed: the 20 October local-LLM campaign v1.0,
local-llm skill evaluation/runtime/hardware/leaderboard references, 21 October
IQ3_S attempt/stop receipts and Claude's current catalog/profile changes.
Private instructions and raw answers are intentionally not copied here.
