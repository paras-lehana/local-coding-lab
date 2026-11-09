# Merged model research, article ledger and resumed experiments

**9 November restart update:** Flash-Next Q2 / Strata 0.1.50's 64K
GPU-KV growth trial ended in a confirmed 0x116 NVIDIA timeout-recovery crash
at 10:10:57 IST. Its 8K/17K fact answers and allocation growth are observations;
the interrupted 33K case and unrun shrink/private audit have no score. The exact
configuration is quarantined, no engine is running, and production remains off.
See the [incident and configuration](../../../reports/2026-11-09-flash-q2-gpu-restart.md).
This records workload association, not a proven parameter-level cause.

9 November 2026 · v0.11.0 checkpoint · **work in progress**

## At a glance

| Owner request | Result / current state |
|---|---|
| Merge Claude's work | Run C grades and campaign audit retained; pending code reviewed; newest preparation separated from actual inference |
| Every model and configuration, with pros/cons | [Model index](../../models.md), seven new historical standalone records, existing candidate reports and [complete configuration matrix](../2026-11-03-master-summary/2026-11-03-all-models-and-combinations-v1.0.md) |
| Summarize all supplied articles in a table | [articles.md](../../../articles.md): fourteen rows including earlier AI advice; corrections, local measurements and next decisions. Full fusion article recovered and reviewed |
| Try useful article suggestions | Six b12069 compatibility controls pass. Flint72K/cap1024 private25/36; fifteen performance controls complete safely. Tuned native72K/u128 private31/36 in1h46m,6/6merge checks. Several controls changed; no causal reasoning-only claim. Resident3/6/3 complete: cached repeat improves, cold gain inconclusive |
| Merged final summary and validation | Model/article summaries updated; remaining controlled trials, publication checks and final closeout pending |

## Business summary

The tuned native Flint follow-up finishes08:25IST with31/36 in1h46m and
all six merge behavior groups passing. This improves on the capped run's
25/36 in2h53m, while still omitting some instruction details. Several
settings changed, so the result supports this complete profile, not a claim
that one flag caused the improvement. It is an extended single-seed result
and does not establish a replacement for the Qwen reference.

Qwen Q4 remains the reference for this instruction-heavy use case. There is
still no complete matched comparison that establishes a replacement. Higher
precision, longer thinking and full GPU residency have each failed to guarantee
better answers in our trials. We now have one article ledger and a model index
that keep measured results separate from proposals and capacity failures.

Claude's most useful completed contribution was finishing Flint run C's code
review and isolated checks: its two capped answers satisfy the same frozen
behavior checks, but the larger reasoning cap takes much longer. His newer
runtime and Flash Q2 preparation were valuable setup work, not new quality
scores. The new higher-quant Flint private audit now completes in2h53m but
scores25/36. Reading all15sources did not prevent code, rule and citation
errors. Its full-prefix reuse8/8 also shows why cache fixes alone cannot make
that answer correct. The separate performance controls test which changes
reduce delay without claiming a quality improvement.

## What was read and reconciled

The review used the two newest owner attachments; project and parent AGENTS;
the local-llm skill, candidate definitions, leaderboard and recovery brief;
the model comparison, methodology and reporting rules; Claude's master and
deep-research records; saved run C grades; runtime build and Flash pack receipts;
the historical model-specific reports; and the seven-article and earlier
Gemini/Strata/azllm reviews. Selected sections of long research records were
read on demand; this is not a claim to have re-read every raw transcript.
Shared Codex routing, platform and logging sources were recovered as directed.

| Claude contribution | Merge decision | Limitation / correction |
|---|---|---|
| Flint run C grading | Retain38/40 at1024 and37/40 at8192 as agent-assessed extended router parts | Both6/6 behavior and6/7 self-tests; one-point difference within judgment uncertainty. No public /60 or new composite |
| Native32K run C stop | Retain unscored RAM stop at6136.2s with11,221reasoning tokens and no visible answer | Attribution to desktop versus model growth is not established by the stop alone |
| WDDM commit analysis | Retain empirical near1:1 GPU-buffer/commit observation | This host's measured behavior, not a universal CUDA allocation identity |
| Re-prefill audit | Retain historical scope and method; link raw derivations | Qwen's0.057% denominator is prefill **plus decode**. “Never re-prefilled” applies only to224 audited continuations, not all future editor traffic |
| Groot trials | Retain both RAM stops and exact historical low floors | No quality score. “Needs apps closed” is not the only possible future path and does not authorize closing apps |
| Stop-floor enforcement in lab.py | Accept the reviewed minimum RAM floor and reject explicitly lower commit floors | Legacy profiles without a commit field remain legacy; no permission to launch an unchecked Strata queue with0.5GiB floors |
| Remote/local artifact filename split | Retain URL correctness for recorded staged files | A C: junction does not make a file physically installed on E:. Do not add new C: installations |
| b12069 side runtime | All56 recorded binary hashes rechecked; six tiny-model CPU/GPU controls pass | Not production; no full-model numerical equivalence or speed improvement established |
| Flash Q2 download and pack | Verified/packed3Nov;11artifacts rehashed9Nov; static32K greetings now complete31.813/9.437s | Two frontend ACL failures preserved and a narrow isolated fix qualified; no coding score.64K growth interrupted by0x116 during33K prefill, unscored |
| Six-item unattended queue | Do not arm unchanged | Completed pack step is redundant; stale native hashes and low Strata stop floors need review. Each trial needs current admission |

The remote-path unit case now includes a publisher subdirectory. The previous
test's blanket slash prohibition was too restrictive: a local staging path
and an upstream path may both contain directories. URL construction still uses
the explicit upstream path; no download behavior is changed by this correction.
Its updated check passes in the52-test post-inference suite.

Additional Strata fork review9Nov: the clean working tree is at1beb824e on
`experiment/win-vram-budget`. Its Windows Qwen VRAM helper uses the smaller
of CUDA's and NVML's free-memory values, falling back to DXGI and then raw
CUDA if reads fail. The independent monitor remains necessary; this is not
an atomic reservation of VRAM. Current source and the older compiled binary
must be pinned separately before a comparison.

The expert-pack filename hashes the GGUF **path and layout**, not its weight
contents. The engine reuses a same-size pack without a content hash. Therefore
replacing weights in place could silently reuse stale experts. The lab must
use a fresh artifact-specific E: pack directory and verify both source-model
and derived-pack identities before reuse. This source observation is not a
locally reproduced corruption or a merged runtime fix. The old queue's C:
write-or-reuse target,0.5GiB RAM floor and stale guard hash cannot be reused.

## Model-wise conclusions

The [model table](../../models.md) lists every family, its tested quants and
placements, strengths, bugs, incomplete suites and links to individual records.
The [historical matrix](../2026-11-03-master-summary/2026-11-03-all-models-and-combinations-v1.0.md)
retains row IDs, timing, runtime, cache and reasoning combinations. New rows
below are added rather than silently replacing historical settings.

The strongest available frozen-cohort instruction result remains Qwen3.6 Q4 mapped64:
private31/36, public52/60, exact-profile coding missing. Gemma26's later public
57/60 and separate extended coding10/12 are useful, but private23/36 and
sampler/profile differences prevent combining them into a superior overall score.
Flint IQ3's eleven completed coding passes are encouraging; unfinished CSV and
the NaN-TTL defect prevent calling it fully reliable. More expensive Flint/Qwen
quants have not supplied a clean full replacement.

Dense Gemma31, Coder-Next80, Kimi and the original Next80 now have explicit
standalone historical records, so a capacity rejection or retirement cannot be
mistaken for “never tried.” Bolt and K2 remain genuinely untested for quality.

## New experiments and exact controls

The 3 / 6 / 3 GiB residency control is now complete. It keeps the combined128
inference settings and changes only the process resident allowance, with a
6.5 GiB startup reserve and 12.5 GiB admission for the larger allowance.
The cached reply improves at 6 GiB, but cold and changed-input improvements
do not exceed baseline drift. Keep 3 GiB for the remaining quality tests.
This measures weight-page residency, not chat KV growth.

The next Flint TS/SQL collection is prepared for the completed native 72K /
microbatch128 profile, with the frozen questions and a 24,576-token output
allowance. A separate cap1024 variant is also prepared, but neither has run.
Three ownership checks for the dated collectors passed before the Flash
experiment; collection and isolated grading still need to finish.

The later coding collector can use the separate
[capped quality profile](../../../profiles/flint-q3xl-quality72k-u128-budget1024.json),
which retains the native audit's placement but sets the engine ceiling to
1024 per reasoning block. This profile is prepared only. The Flash growth
generator and its exact-token validation are complete. Its independently
armed trial has finished the 8K and 17K requests and is processing the 33K
request; the final 8K shrink request remains. Final recall grading waits for
normal cleanup and review of every available answer. The
[file inventory](../../file-inventory.md) now enumerates every public change.

| Experiment | Artifact / runtime / settings | Outcome |
|---|---|---|
| b12069 loader compatibility | stories260K, SHA270cba1b…; b12069 stock versus rebuilt-default versus opt-in; CPU0/GPUall;512context,64greedy tokens,seed73,4threads, core0excluded | Six complete runs. Outputs identical within CPU and GPU groups; opt-out log appears only when enabled; no new hardware event |
| Flint private 72K/cap1024 | Q3_K_XL SHA91b8d85a…; b11838-noprefetch; GPU attention, CPU49 experts, 256 MiB expert cache, 1 GiB resident cap, GPU q8 KV, 73,728 context, b64/u16, 4 decode/8 prefill threads, masks5554/FFFC, no context shift, temp1/.95/20, 24,576 output, reasoning cap1024 per block | Load20.486s. Greetings95.652/85.138s; first visible78.603/68.034s. Completed private25/36 in10,380.106s; normal stop, no new hardware event |
| Flint fixed-prefix u16/resident1 baseline | Same weights/runtime/placement; native1895-token fixture, greedy32-token output, three request variants, 60s post-request idle | Cold267.437s; identical repeat9.641s with1894cached tokens; changed middle259.765s with zero cached tokens. All32-token limits, no quality score. Cache destruction reports zero hits/29,581 misses in the <=8 bucket; normal stop |
| Flint fixed-prefix u4/resident1 | Same baseline, physical microbatch4 | Cold514.454s, repeat8.859s, changed524.047s; normal stop, no new hardware event. Smaller microbatch nearly doubles fresh-input latency; no quality score |
| Flint fixed-prefix u32/resident1 | Same baseline, physical microbatch32 | Cold265.391s, repeat9.704s, changed286.968s; normal stop, no new hardware event |
| Flint fixed-prefix u64/resident1 | Same baseline, physical microbatch64 | Cold175.953s, repeat11.250s, changed195.281s; normal stop, no new hardware event; later baseline repeat required |
| Flint fixed-prefix u16/resident3 | Same baseline, resident cap3GiB/reserve4.5GiB | Cold245.000s, repeat6.828s, changed241.390s; normal stop, no new hardware event |
| Flint fixed-prefix u16/cache1536 | Same baseline, expert-cache budget1536MiB/resident1GiB | Cold334.500s, repeat6.765s, changed307.594s; normal stop, no new hardware event. Slower prefill, faster decode; actual cache1531.97MiB |
| Flint fixed-prefix b12069/u16/resident1 | Same original baseline settings; newer pinned opt-out runtime | Cold263.984s, repeat9.984s, changed259.203s; normal stop/no new hardware event. No material fresh-input speed gain in this single run |
| Flint fixed-prefix original-baseline repeat | Original b11838/u16/cache256/resident1 controls, fresh owned server | Cold261.641s, repeat9.735s, changed263.781s; normal stop/no new hardware event; cold/middle timings within about2.2% of initial baseline |
| Flint combined64 | b11838/u64/cache1536/resident3, same72K/frozen native fixture; admission9.5/11/6200 | Cold191.937s, repeat5.296s, changed149.844s; normal stop/no new hardware event.36.23%small-batch expert hits; no quality score |
| Flint combined128 | Same combined settings, b128/u128 | Cold128.406s, repeat5.171s, changed97.157s; normal stop/no new hardware event. No quality score |
| Flint short2K rollback pair | b64/u64/cache1536/resident3; identical settings except full-SWA storage; same frozen native fixture | Windowed191.922/5.359/145.562s; full-SWA194.547/7.922/95.562s. Both normal stop/no new hardware event. Full-SWA middle edit reuses962tokens versus zero and adds46.484MiB KV; all three short outputs differ. No quality or72K capacity qualification |
| Flint native72K/u128 private audit | Same Q3XL/b11838; GPUq8,CPU49,cache1536,resident3/reserve6.5,b128/u128,4/8threads,masks5554/FFFC,no context shift,temp1/.95/20,24576output,reasoning budget-1,21600s whole case | Completed08:25IST,31/36(19/6/6),6386.703s. Load20.453s; greetings57.907/37.672s. Audit first visible5995.230s, prefill3215.777s/generation3168.581s. All15sources,5/6full-prefix continuations. Normal stop/no new hardware event; several controls differ from capped audit |
| Flint resident3/6/3 control | Same combined128 native fixture; only resident allowance changes, three sequential owned loads | Cold123.016/117.203/113.735s; repeat5.297/3.500/5.391s; middle-edit90.719/84.312/83.907s. Normal stops/no hardware event.6GiB helps cached repeat, but cold/changed benefit is smaller than baseline drift. Keep3GiB for matched quality follow-up |
| FlashQ2 original frontend, two attempts | Same model/0.1.50/512cache/static32K, guard4GiB, frontend4b9e05a2 | Both stop at Windows OpenProcess with error5 before questions; no quality score. Direct native guarded load reaches READY32768 and exits0 on EOF in9.390s |
| FlashQ2 corrected frontend static32K | Same engine/model/settings; isolated token-default FA→GA patch for unchanged trustees;12Windows privacy cases pass/onePOSIXskip | Load82.953s incl frontend setup; greetings31.813/9.437s, first visible26.250/6.906s. Native RSS4GiB,dedicatedGPU5.243GiB; minimum freeRAM5.989GiB,commit13.305GiB,VRAM1294MiB. Normal stop/no hardware event; not coding evidence |
| FlashQ2 native KV growth | Same corrected frontend/512cache/prefill64/xhigh; maximum64K,initial16K,step8K,floor128,hold0,int8 GPU KV;7200s per input | Four offline-validated inputs8178/17356/33788/8178tokens. Startup confirms16384of65536cells,0.23of0.80GiB. 8K/17K fact answers completed; allocation grew0.23/0.33/0.52GiB;0x116 during33K prefill, shrink unrun, entire trial unscored |

The second trial's fresh admission was8.843GiB RAM /21.236GiB commit /
6474MiB VRAM; required7.5/8.5GiB/5500MiB. Stop floors remain2.5GiB RAM,
1GiB commit,400MiB VRAM and84C. The six-hour allowance is explicitly an
extended diagnostic. A per-block cap is an engine stopping control, not trained
“ultra/high/low” reasoning. The question, source snapshots and rubric are unchanged.

No download, large hashing, build, isolated grading or offline test overlaps
this inference. The launcher verifies the model before loading. Only owned
experiment processes are stopped. User applications, BIOS, clocks and drivers
are untouched.

The private-audit greeting requests both report zero cached prompt tokens.
"Warm" there means a repeated request with caching requested, not a measured
cache hit. The small resident cap is associated with about six prompt tokens
per second in that audit. The later performance controls use a6,844-byte
synthetic prefix, greedy32-token native completion and cold/repeated/changed-
middle requests. Their completed timings are in the table above; none inherits
the private instruction score. Its source fixture and original run stay unchanged.

Actual server buffers differ from requested budgets: the256MiB expert-cache
budget allocates243.08MiB, covering1.6% of slots in its cached layer groups;
two groups each contain one uncached layer. This is slot capacity, not a
measured hit rate. The attention buffers are1071MiB for14global-attention
layers at73,728cells, plus27.89MiB for35sliding-window layers at768cells.
The latter is sliding-window KV, not recurrent state; the article ledger and
shared runtime note now use the actual server labels.

Logged head geometry also reconciles those allocations: four KV heads,
128dimensions for both K and V, and q8_0's34bytes per32values give exactly
1071MiB for73728cells across14global layers and27.890625MiB for768cells
across35sliding-window layers. Total KV is about1.073GiB on GPU; neither the
18.495GB weight file nor the process's1GiB resident cap is this KV measurement.

All seven original prefill profiles include60second native idle sleep solely
after their timed requests, to flush destructor cache statistics. Their
completed runs observed both native statistics and passive sleeping status.
The helper rejects unexpected sleep between requests. Source review found a
32-token direct-cache boundary; microbatch64 uses a different cache path.
Seven offline helper checks passed before these controls. Production's idle
policy is unchanged. See the [detailed speed review](../../../research/reviews/2026-11-09-fusion-and-speed.md).

The seventh profile is source-driven: the logged six selected experts require
96slots for a full microbatch16, exceeding every current36/61/86slot group.
The direct cached-expert path is therefore bypassed for those full batches.
Microbatch4 requires24slots and qualifies in the three cached groups, while
the separate1536MiB control increases capacity. Neither change is assumed to
improve speed; the fixed-prefix measurements and actual counters decide.

### Chronological private-audit checkpoints (superseded by the completed result)

The following paragraphs retain observations made during collection. The
audit has since completed25/36; their "pending" labels are historical.

Interim tool behavior through turn02:12 distinct frozen sources delivered,
including the installer implementation and selected Python rules. One wrong
README path was unavailable; two later range requests exceeded the tool's
documented200-line limit and were rejected. The next turn is allowed to
recover these errors. This is observed tool behavior, not a final score or
proof of a quantization defect. Turn02 reused14,114prompt tokens and processed
7,472new ones in1,216.483s;248generated tokens took134.254s. Its reasoning
ended naturally below the1024cap, so that turn's range mistakes cannot simply
be described as the engine truncating its thinking.

Turn03 recovered both oversized reads by asking for200-line ranges, giving
14distinct delivered sources so far (some partially read). Completed
continuations01–03 report3,082/14,114/21,833cached tokens, each exactly the
previous reported KV length (`cache_n + prompt_n + predicted_n - 1`). Their
new input counts are10,653/7,472/2,859. This fresh timing reconciliation supports
new-file prefill as the current delay; it does not prove semantic recall or
eliminate separate editor-prefix problems. The audit still has no final answer.

Turn04 then obtained the remaining logging and coding-documentation ranges;
the earlier oversized-read errors were recoverable. Its request used31,484
input tokens, including24,903cached, and finished in1,238.732s with208generated
tokens. Turn05 is processing the new source content. No final answer is present
at this checkpoint, so neither successful reads nor cached prefixes become
instruction-quality points on their own.

The upcoming Flash qualification now has a separate, unrun one-shot wrapper
around the hash-pinned historical lifecycle driver. It refuses an unarmed
plan, a mismatched validation receipt, changed artifact metadata and unknown
Ollama inventory. The historical queue treated an unreachable Ollama endpoint
as empty and checked only whether prerequisite marker files existed. Its
original file is preserved. The wrapper also propagates unavailable hardware
event queries instead of allowing a successful postflight. Nine new offline
refusal controls are prepared,
alongside the seven prefill-controller checks; none runs beside inference.

03:41IST checkpoint: turn05 corrected the earlier README path;15distinct
source documents have now been delivered. Its timing is964.098s prefill for
5,629new tokens plus513.709s generation for929tokens, with31,691cached tokens.
Turn06 has39,624input tokens and is generating. All preceding reasoning segments
ended naturally, rather than exhausting the1024cap. There is still no final
answer to grade. The actual private requests use seed73, temperature1,
top-p.95, top-k20, min-p0, repeat penalty1, max_tokens24576 and cache_prompttrue.
The older streaming client does not record an exact first-visible-token time;
occasional progress observations are only coarse observations, not that metric.

03:44IST update: turn06 is the first audit response whose native log reports
budget exhaustion and a forced closing sequence. It then requests logging
line200, already delivered earlier. This redundant read is preserved without
inferring its cause from a single observation. Turn07 is active; no final
answer exists. Source inspection also clarifies that this sampler can re-arm
the1024budget on another reasoning start tag: it is a per-block ceiling, not
a guaranteed aggregate thinking limit for the whole workflow. Earlier turns
each ended their reasoning naturally; the audit is still within its six-hour
whole-case allowance.

## Article conclusions and next experiments

### 04:18 IST completed private result

The nine-turn Flint Q3XL/cache256/resident1/cap1024 audit completes in
10,380.106seconds (2h53m), then its owned launcher stops normally. No new
hardware event. Reviewed against the frozen rubric: **25/36 =18semantic +
3citation +4code**. All15sources are delivered and all three failed reads are
recovered. The answer nevertheless gives the wrong exact merged JSON, omits
required instruction/adapter details, supplies a citation beyond the named
source, and promises a deepcopy correction it never supplies. The latest
complete delivered function, selected by its stated role before execution,
passes4/6isolated behavior groups; it overwrites an existing null and aliases
mutable inputs. Earlier drafts and prose contradictions remain preserved.

This is an extended single-seed result, not a1200second score or evidence that
a quantization label or cap caused the defects. It does not justify replacing
Qwen. [Sanitized measurement](../../../reports/2026-11-09-flint-q3xl-private72k.json).

Measured prefill totals6,140.370s and generation4,236.126s. Every one of eight
continuations reports the complete available previous prefix reused, exactly
matching previous cache+fresh+generated−1. The final request has42,290input
tokens and4,368generated. This does not demonstrate72K/128K recall. The legacy
collector does not measure exact first-visible-delivery time; no exact value
is invented from coarse polls. All source files being delivered did not ensure
correct instruction application.

Whole-trial minima:6.711GiB available RAM,10.839GiB commit and2,896MiB free
VRAM; maximum49.38C. Process working set stays near1GiB, private commit peaks
3.991GiB. These differ from total model file size and total PC memory usage.
Post-stop available RAM14.462GiB, commit27.968GiB, freeVRAM6,709MiB. Apps stay
open. The cap was exhausted on turns06–08 and can rearm per reasoning block;
the launch's old "per turn" evidence wording is not a semantic guarantee.

After engine exit, the52-test offline suite passes in19.920s; seven prefill
controller controls, nine Strata one-shot refusal controls and nine actual
template/frontend render checks pass. Harmless-process Strata checks confirm
preflight refusal, owned cleanup, deadline, missing/exited native process and
unrelated-peer survival. Model-generated-code grading is isolated in WSL with
no host home/mount/network access; its expected behavior failures are model
results, not failures of these maintainer checks. Performance controls follow.

The new speed article's prefill/decode distinction is useful. Its absolute
claims about removing all CPU offload, diagnosing a low rate from bandwidth,
and general MTP gains are not justified for this deliberately offloaded setup.
Microbatch size is worth measuring, but increasing it directly to2048 ignores
workspace and commit. Cache reuse and checkpoint rollback need separate analysis.
The [article ledger](../../../articles.md) documents these corrections beside
the earlier high-throughput, low-VRAM, Flash/RAM and fusion proposals.

The recovered fusion article also needs correction: its weighted log-softmax
product does not calibrate cross-model scales. Its three 7B models exceed the
currently available GPU budget before cache overhead. The
[separate review](../../../research/reviews/2026-11-09-fusion-and-speed.md)
provides the derivation and a bounded compatibility-first experiment design.
The two smaller staged candidates now have individual preparation records:
[Qwen3.5-9B](../2026-11-09-qwen35-9b/2026-11-09-qwen35-9b-v0.11.0.md) and
[Dory4B](../2026-11-09-dory4b/2026-11-09-dory4b-v0.11.0.md).

| Next action | Why | Gate / current reason unfinished |
|---|---|---|
| Finish and source-review Flint72K private audit | Completes a genuinely missing higher-quant instruction result | Both complete: cap1024 gives25/36 and4/6merge groups; tuned native gives31/36 and6/6. Extended, multiple settings changed, not promoted |
| Microbatch/cache/residency/runtime and rollback controls | Directly test useful speed-article ideas | Completed15controls. Native72K quality follow-up31/36; no promotion. Residency3/6/3helps repeat-cache response but cold gain remains inconclusive |
| Qwen exact mapped64 coding component | Required for a fair complete reference | Reference admission needs more RAM than the recovery snapshot; no score transfer from nativeQ4 |
| Flash Q2 static32K, then actual KV growth | Test the 75GB/RAM hypothesis with available SSD-backed storage | Static greetings qualify after an isolated frontend ACL correction.64K growth interrupted by0x116 during33Kprefill;8K/17K observations and16K/24K/40K allocation preserved unscored; shrink/private unrun |
| Strata Qwen expert pack | Test whether reduced commit can avoid copying/touching all expert pages | New fork identity and minimum stop floors; no unchanged0.5GiB queue launch |
| Groot bounded fit, then full suite if qualified | Smaller model can be more useful with apps open | Prior runs resource-stopped; needs fresh admission and stronger floor, no quality assumption |
| Dense Qwen Q4 / K2 / Bolt / Dory | Coverage and precision hypotheses | Disk, placement/runtime and resource constraints; no new C: installs |
| Fusion | Possible ensemble accuracy experiment | Full source recovered; mathematical normalization claim disproved. Tokenizer compatibility and a tiny implementation control precede any larger ensemble; no evidence of gain yet |

## Storage and availability

No prior llama/Strata engine was left loaded on recovery; Ollama's loaded list
was empty. Six verified redundant installer archives were removed, recovering
2,168,377,560bytes and leaving2,665,594,880bytes free on E:. Installed runtimes,
weights and evidence were preserved. A final console-total error occurred
after cleanup; receipt verification confirmed all six deletions and the exact
free-space result. Only the reporting expression was fixed, without repeating
deletion. Full cleanup evidence is private, aggregate receipt is publishable.

A 01:53 IST memory sample during Flint shows 9,137 MiB available, roughly
79.1 GiB committed, and about 106 MiB/s of system-wide page input. Both physical
disks were active. This is one sample, not a per-model hard-fault measurement.
The largest process working sets include several editor/browser processes and
Java; the owned model's working set is capped around 1 GiB with 3.93 GiB private
commit. Shared pages and kernel allocations prevent adding that list into a
unique RAM total. No leftover model or application leak is established by it.

At02:35IST, during the next tool-result prefill, a separate sample shows32% GPU utilization,
6,821MiB device memory used/3,233MiB free,43.1C and36.4W. The server's aggregate
CPU counter is631% (about6.3 logical processors, not631% of the whole PC),
with339,553process page faults/s. System-wide page input is61,108pages/s,
about239MiB/s at4KiB per page. Faults include soft faults; these counters do
not attribute every hard page read to Flint. Process IOReadBytes/s being zero
does not rule out memory-mapped page traffic. This is a single sample, not
average utilization or proof that one proposed cache change will fix latency.
The sampling label initially assumed generation; the collector shows turn03
began02:34:42.977, so its phase annotation is corrected to prefill. Raw counter
values and the original annotation remain preserved.

Production Qwen Q4/128KCPUq8/1800-second idle remains selected and off. Its
18GiB RAM/12GiB commit/6000MiB VRAM gate must pass before restoration. A saved
“ready” value is not live availability. No fresh Copilot/Continue typing or UI
pass is claimed. Capacity constraints do not justify closing the owner's apps.

## Validation and evidence

- `python -m unittest discover -s tests -v`:51passed in29.612s before inference.
- After the private engine stopped:52passed in19.920s, including the reviewed
  guard-floor and publisher-subdirectory cases. Seven prefill-controller,
  nine Strata-wrapper and nine actual template-marker checks also passed.
  Harmless native-process tests covered admission, owned stop, deadline,
  missing/exited native process and preservation of an unrelated process.
- Private-audit code was selected after source review and ran only inside
  WSL/bubblewrap:4/6behavior groups passed. Its two failures are recorded
  contract defects, not harness errors or syntax failures.
- Six b12069 compatibility controls passed, with56recorded binary hashes checked.
  [Public receipt](../../../reports/2026-11-09-b12069-prefetch-controls.json).
- Runtime source checked for batch defaults and cache-shift restriction; official
  pinned server documentation and Flint launch article fetched9Nov.
- No new WHEA/bugcheck/unclean restart in preflight or tiny-control postflight.
- After all12performance engines stopped:52offline tests pass19.502s,
  four PowerShell files parse, public audit406files/zero findings, and
  diffcheck passes after one trailing blank line was removed. Five derived
  private timing/ownership checks pass before the instrumented audit starts.
- Final changed-document/link checks, commit/push/CI remain pending. No UI
  changes in this task; no offline tests or grading beside live inference.

Private new evidence: `local-data/2026-11-09-merge/`. Earlier raw article text,
instruction snapshots, answers and secrets remain outside Git. Historical
model records are documentation extractions; they do not imply new tests.

## Decisions and limits

### Post-restart continuation, 9 November

The confirmed GPU0x116 interruption is recorded in the
[incident report](../../../reports/2026-11-09-flash-q2-gpu-restart.md). Earlier statements of a clean
hardware postflight describe the then-used WHEA-only check unless independent
crash evidence was reviewed. The expanded checker now rejects the actual
crashed interval. It cannot guarantee crash prevention.

58offline tests pass in21.378s; five private-adapter refusal/ownership checks
pass in0.035s. A portability-only mock correction was then made so the new
Windows-event tests can run in Linux CI; its targeted rerun is recorded in
the final validation. No inference ran after reboot. No source instruction,
answer, credential or dump is published; only sanitized facts and hashes.

| Candidate / remaining experiment | Current reason it is not a completed result |
|---|---|
| Flash Q2 dynamic64K and private128K | GPU crash during33K prefill; shrink unrun; private plan never armed. Exact profile quarantined |
| Flint Q3XL native72K TS/SQL and twelve coding questions | Collectors prepared; sustained GPU continuation held after the workstation crash. Private31/36 and short controls do not fill these gaps |
| Qwen Q4 historical mapped64 matched coding | Missing exact-profile baseline remains; newer native9/12-attempt record uses different conditions and cannot replace it |
| Groot Q4 resident4/64K | Prepared reduced-residency profile; two older RAM-stopped profiles have no quality result; no fresh load after GPU incident |
| Dense Qwen3.8-27B Q4 | Metadata pinned; about16.464GB artifact not downloaded, with only1.79GiB free on E: at13:20. Previous Q6/Q8 long-input failures retained |
| Qwen3.5-9B Q4 CPU-KV64K | Prepared, legacy artifact staged on C:; needs verified physical E: installation, more disk space and fresh qualification |
| K2 Horizon MoVA | Parked artifact needs verified restoration to E:; no fit or quality result |
| Dory4B | Prepared candidate, no compatible verified runtime/installed E: artifact; old runtime pin does not include the later placement fixes |
| New Strata Qwen expert pack | Requires roughly21GB staging headroom; old metadata-only pack reuse is not a sufficient identity check |
| Three-model fusion / article-specific GPU stacks | No ensemble or incompatible-kernel reproduction; source/capacity critique retained, not an empirical ranking |

The next useful quality work is Flint's prepared native TS/SQL and coding
suite, plus the exact Qwen reference coding suite, once a changed-condition
short qualification is justified by the GPU incident review. A blind Flash
retry or arbitrary switch to a higher quant would confound diagnosis and
could repeat the reboot. Current production admission also fails:11.4GiB
available RAM versus18GiB required at the post-restart check. Apps remain open.

No new owner decision is needed for the authorized bounded experiments.
Do not request another “continue,” close apps or lower floors to force a fit.
If capacity prevents remaining trials, preserve their exact reason and planned
configuration. No complete campaign or replacement-model claim is made here.

## Screenshots

Not applicable: this checkpoint changes reports and experiment preparation;
it does not claim editor or widget UI verification.

## Appendix: owner request

Continue the local-LLM work; review and merge Claude's changes; complete useful
pending trials; produce the full merged, model-wise and tabulated summary with
configs; summarize every earlier and newly supplied article in `articles.md`
with claims, our findings, errors, experiments, improvements and suggestions.
New inputs: Claude's stopped-loop handoff and “Why Is My Local LLM So Slow?”
Full pasted articles are retained privately, not republished.


### Historical 9 November pre-serving checkpoint

9November recovery checkpoint: all fifteen Flint performance controls now finish normally.
The resident3/6/3GiB comparison gives cold wall123.016/117.203/113.735s,
cached-repeat5.297/3.500/5.391s and changed-input90.719/84.312/83.907s.
Extra residency helps cached repeat, but cold/changed improvement is smaller
than baseline drift; retain3GiB for matched quality follow-ups. No quality
score follows from these short32-token controls. Native private31/36 remains.
Flash Q2's11artifacts pass fresh full hashes. Direct guarded native loading
reaches READY32768 and exits normally on stdin EOF in9.390s; no questions.
Two serving attempts stop fail-closed before requests with WinError5 at
OpenProcess in the working-set guard. All descendants are cleaned up, no
new hardware event. A source lead is frontend adopt_user_defaults using file
access bits in the process token default ACL; harmless reproduction pending.
Guard now preserves traceback/error.json without changing floors or cleanup.
52offline tests and6harmless lifecycle checks pass. Four Flash growth inputs
8178/17356/33788/8178tokens match the real pinned frontend encoder offline;
no growth inference. Production remains off; no model retired or promotion.
