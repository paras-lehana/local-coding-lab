# Prompt log — Local Coding Lab

Last updated: 2026-10-14. Public project history excludes earlier credentials,
private instruction contents and raw editor chats.

| # | Date | Time (IST) | Topic | Type | Status | Link |
|---|---|---|---|---|---|---|
| 1 | 2026-10-14 | 22:35 | Establish reusable research repository | Infrastructure | Done | [Entry](#repository-creation) |

## Repository creation

Project: local-coding-lab. Branch: main. Mode: Default.

### Original request

> lets make a repo for this where you have reports, other docs, model links,
> installation script etc very user-friendly managed so that others can also try
> and test things via our repo.
>
> this also a research doc, shift this to the repo is some bare research folder
> and then plan what to try next
>
> https://share.gemini.google/LadMuhd0ajY0 see if you can read this doc.

Publication choice: Public GitHub repository, selected by the owner.

### Recovered context and pre-flight

- New portable repo on the dedicated installation drive (existing parent lab
  contains private logs, secrets and large artifacts and must not be published).
- Public synthetic fixture instead of personal source contents (owner's main
  evaluation requirement is instruction/file grounding and correct code).
- Whole-prompt limit 1200 seconds and apps remain open (current parent rules).
- Preserve measured/proposed distinctions (recent trials included two memory
  stops; current Qwen reference is not a demonstrated universal winner).
- Use project-owned guidance plus small Claude/Copilot adapters (shared
  context-maintenance workflow); no global adapter changes needed.

### Implementation and validation

See [repository-creation.md](repository-creation.md),
[file inventory](file-inventory.md), and [tasks.md](tasks.md). No dependencies
were added. Offline tests and publication audit passed. Public main was verified after push; both implementation CI jobs passed.

### Canonical closeout

**A. Business summary — Done**

Published [Local Coding Lab](https://github.com/paras-lehana/local-coding-lab): setup instructions, model downloads, benchmarks, reports and a next-test plan. I successfully read and archived the Gemini document, with a separate critical review.

**B. Technical summary — Done**

The repo includes hash-verified downloads, guarded launch profiles, a file-reading benchmark with a 20-minute deadline, and synthetic project files others can safely use. **13 tests passed locally and in Windows/Ubuntu CI.** Implementation commit: `eda5eb5`, branch `main`; no new dependencies.

Start with the [setup guide](https://github.com/paras-lehana/local-coding-lab/blob/main/docs/setup.md). The [file inventory](https://github.com/paras-lehana/local-coding-lab/blob/main/docs/file-inventory.md) and [validation record](https://github.com/paras-lehana/local-coding-lab/blob/main/docs/repository-creation.md) document the changes and checks. No new model inference or editor UI testing occurred during this task.

**C. Request status**

| # | Pointer Task | Original Pointer Text | Status | What Was Done |
|---|---|---|---|---|
| 1 | Shareable repository | “reports, other docs, model links, installation script” | DONE | Public repository with setup and evaluation tooling |
| 2 | Archive research | “shift this to the repo…research folder” | DONE | Source text, provenance and separate review |
| 3 | Next experiments | “plan what to try next” | DONE | Controlled, memory-aware test sequence |
| 4 | Read Gemini | “see if you can read this doc” | DONE | Retrieved through anonymous browser rendering |

**D. Additional findings**

The research incorrectly attributes memory stops to a default prompt cache: your launcher already sets `--cache-ram 0`. Its proposed 1536 MiB cache would increase that allowance. Its predicted speed gains remain unmeasured. Details are in the [research review](https://github.com/paras-lehana/local-coding-lab/blob/main/research/reviews/2026-10-14-gemini.md).

**E. Pending work**

| Item | Status | Reason |
|---|---|---|
| New model comparisons, long-history tests and editor validation | Planned | Repository preparation is complete; these require live experiments |

**F. My recommendation**

Keep Qwen as the measured reference. Test GPU placement separately when memory permits; **Gemma 4 26B QAT is my next smaller candidate**, followed by GLM-4.7-Flash UD-Q4 at 32K. Neither is a proven upgrade yet. Your existing installation, models and private evidence remain intact.

**G. Copyable summary**

```text
Local Coding Lab — public research repository published (v0.1, 14 October 2026)

What's done
- Created a shared home for installation guidance, model choices, benchmark questions and measured reports.
- Preserved the supplied research and added a separate review explaining which claims are supported, uncertain or contradicted by local evidence.
- Added reusable tests focused on instruction following, file references, missing information and coding mistakes.
- Automated tooling checks passed on Windows and Linux. Private credentials and instruction files were excluded from publication.
- Existing models and the original installation remain intact. No new model performance result is claimed from this packaging work.

Suggested next steps
- Retain Qwen as the measured reference and test one setting change at a time.
- Evaluate the smaller Gemma candidate, then GLM if memory allows.
- Require repeatable code correctness, reliable file handling and completion within twenty minutes before choosing a replacement.
```
