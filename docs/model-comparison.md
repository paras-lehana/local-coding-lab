# Current model comparison

Updated 24 October 2026. Components and completion gates matter more than a
single leaderboard number. Claude's newer campaign was private; this table
brings its reviewed summary into the public lab. Results are agent-assessed,
not independently human-reviewed. It is not a controlled universal ranking.

| Candidate | Private /36 | Public /60 | Coding /12 | Practical result |
|---|---:|---:|---:|---|
| Qwen3.6 35B-A3B UD-Q4_K_M, mapped64 | 31 | 52 | Not collected | Retained leader on available components; private 699.7 s; SQL failure and aliasing diagnostics remain |
| Qwen3.6 Q4, historical2GiB expert cache |27 |Separate historical cases |Not collected |Private402.703s; strict TypeScript and SQL defects; different placement/non-mapped profile, not evidence that expert caching intrinsically lowers intelligence |
| Qwen3.6 Q5 | 28 | Separate historical cases | Not comparable | Lower private score; retired |
| Qwen3.6 UD-Q6_K_XL | 28 | Historical completed cases | Not comparable | Private 2099.7 s, exceeds current gate; retired. Plain UD-Q6_K is a different, untested artifact |
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
| Qwen3.6 UD-IQ4_XS,CPU35 bounded64K,24October |29 |55 |Pending |Private725.4s,code6/6 plus extra4/4. Instruction omissions/path contradiction/control-flow misexplanation remain. Public SQL uniqueness/FK and TS object validation fail; prior RAM stop preserved |
| Qwen3.6 UD-IQ3_S,38 CPU expert blocks |29 |52 |Two reasoning-only16K output limits; later cases interrupted/unrun |24October: private638.6s, all public workflows complete; alias, TS validation and SQL migration bugs; exact smoke punctuation fails. Separate capped controls appear below |
| Qwen3.6 UD-IQ3_S,4096 reasoning ceiling |Not collected on this variant |Not collected on this variant |Two completed passes; deliberately stopped before full suite |Intervals105/105 and TTL34/34; native scores above cannot be transferred. Redundant interval work and extra NaN TTL finding remain |
| Qwen3.6 UD-IQ3_S,4096 ceiling plus1536MiB GPU expert cache |Not collected on this variant |Not collected on this variant |6/12; all twelve complete |Median134s,31–37tok/s. Interval,CSV,money,strictTS,worker-pool and deep-merge defects. Worker-pool lexical false alarm corrected by hash-scoped unchanged-source recheck; six task passes unchanged. Extra NaN TTL fails |
| K2 Horizon MoVA 36B-A4B Q4 | Not run | Not run | Not run | Downloaded, queued; no demonstrated apps-open fit |
| Nemotron 3.5 Bolt 74B-A9B 24GB | Not run | Not run | Not run |Verified file rotated off disk24October for Flint Q4; quality still queued |
| Recursive Flint UD-IQ3_XXS, uncapped reasoning | Not run after gate failure | Router deadline | Not run after gate failure | 1200.031 s, seven reads, zero final text; clean shutdown, unscored |
| Recursive Flint UD-IQ3_XXS, CPU KV, 2048 cap | Not run after gate failure | Router deadline | Not run after gate failure | 1200.016 s; visible planning after cap, no finished answer |
| Recursive Flint UD-IQ3_XXS, GPU KV | 29 | Router 39/40; TS/SQL tool limit; history output limit | **11 completed passes of 12** | All 374 frozen checks on eleven complete answers pass; CSV produces no code before output limit. Private 692.5 s; separate NaN TTL bug; no full public total or promotion |
| Recursive Flint UD-Q4_K_XL, CPU44/GPU KV |Not run after gate failure |Router1200.031s deadline |Not run after gate failure |Seven valid reads, no final answer; resource/hardware guards clear |
| Recursive Flint UD-Q4_K_XL, CPU48/cache1536 |Not run after gate failure |Router1200.031s deadline |Not run after gate failure |Seven valid reads, partial visible answer starts1137s but remains unfinished; memory guards clear |

## What changed in Claude's work

The active [precision and coverage campaign](tasks/2026-10-24-precision-and-gaps/2026-10-24-precision-and-coverage-v0.9.0.md)
reopens the unfinished candidates. IQ3_S's earlier capacity/VRAM failures remain
valid historical trials; its new38-CPU-expert profile completes public/private
collection with conservative guards. Higher Flint Q4 is verified; its uncached
CPU44 profile and CPU48/1536MiB expert-cache variant both miss the router
deadline. No higher-Flint-precision quality score exists yet. IQ3 capped/cached
coding completes6/12 passes; its native settings remain a separate experiment.
IQ4's new bounded-memory router completes536seconds and awaits isolated
grading while the other public cases collect. Missing compatible components
still prevent a composite.

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

Flint's GPU-KV profile is more promising than its CPU-KV variants: the router
finishes in 523 seconds and its private audit in 693 seconds. The latter scores
29/36 versus Qwen Q4's 31/36. Its deep merge passes the frozen checks and all four
extra nested-alias/local-only-key diagnostics. The lost audit points concern
instruction omissions, incomplete platform guidance and unsupported citations.
However, the public TypeScript/SQLite tool loop and history output limit prevent
a complete public score. Good code on the finished merge tasks is not sufficient
evidence for replacing the owner's instruction-heavy coding assistant.

The twelve direct coding prompts show a different strength: Flint completes
and passes eleven, including both SQLite queries, strict TypeScript, exact-money
changes across two files, and JavaScript concurrency/deep cloning. CSV uses its
16,384-token allowance without delivering code. Median completed-task time is
225.6 seconds; the worker pool takes 688.1 seconds. All 374 frozen behavior and
compiler checks on the eleven complete answers pass, but a separate positive-TTL
diagnostic exposes acceptance of NaN and non-expiring entries. This is not
bug-free certification. It is 11 completed passes versus LFM's 6 on the same
questions, under different recorded sampling/runtime/desktop conditions; Qwen
still lacks this component, so there is no matched all-model coding ranking.

Flint's direct SQL and TypeScript success does not erase the file-driven
TS/SQL tool-loop failure. The distinction is important for this owner's work:
being given a precise function contract is easier to use reliably than having
to discover files, recover from missing paths and maintain project instructions.

A separate fresh-server history diagnostic raises the output allowance to
8,192 tokens and passes 8/8 in 328.016 seconds. It does not replace the original
4K-output failure or establish tool-error recovery/maximum context. Flint's
tested weights were retired after a fresh full hash, while its installer,
runtime and evidence remain. Qwen Q4 stays selected for the owner's workflow.

## Reports and provenance

- [Qwen3.6 model record and active coverage](tasks/2026-10-24-qwen-coverage/2026-10-24-qwen36-v0.9.0.md)
- [Higher precision and offload research](../research/reviews/2026-10-24-precision-and-offload.md)
- [Flint standalone record](tasks/2026-10-23-flint/2026-10-23-recursive-flint-v0.8.0.md)
- [All-model inventory through 17 October](tasks/2026-10-17-complete-model-inventory/2026-10-17-all-models-gemini-and-availability-v0.4.1.md)
- [Matched Q4/Q6 and expanded candidates](tasks/2026-10-16-memory-and-candidate-expansion/2026-10-16-memory-context-and-expanded-model-tests-v0.4.0.md)
- [Strata](tasks/2026-10-18-strata/2026-10-18-strata-on-10gb-v0.6.0.md)
- [TurboQuant](tasks/2026-10-19-azllm/2026-10-19-azllm-and-turboquant-v0.7.0.md)

Private source records reviewed: the 20 October local-LLM campaign v1.0,
local-llm skill evaluation/runtime/hardware/leaderboard references, 21 October
IQ3_S attempt/stop receipts and Claude's current catalog/profile changes.
Private instructions and raw answers are intentionally not copied here.
