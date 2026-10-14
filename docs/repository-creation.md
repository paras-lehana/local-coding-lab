# Repository creation — validation and migration record

Date: 14 October 2026. This task packaged earlier work into a reusable repository;
it did not conduct new model inference. The public repository is published at
https://github.com/paras-lehana/local-coding-lab on branch main.

## Content migration

Historical private reports remain intact outside the repository. A reviewed
public digest and selected numeric results were copied into reports/, with
SHA256 identifiers for the source reports. Private instruction snapshots, raw
editor transcripts, existing credentials, model weights and runtime binaries
were not imported. Public fixtures are new synthetic material, clearly labeled.

The Gemini report was successfully rendered anonymously and extracted into
research/raw/. Its conclusions were preserved with limited personal-path/name
redactions. Google application HTML, session values and browser files remain
ignored locally. A separate review corrects stale memory assumptions, overstrong
quantization conclusions and unmeasured tuning predictions. No existing research
file or weight was deleted to make this repository.

## Validation actually run

| Check | Result |
|---|---|
| `python -m unittest discover -s tests -v` | 13 passed on Windows / Python 3.12 |
| PowerShell parser for scripts/setup.ps1 | Passed |
| setup.ps1 plan with a spaced data directory | Passed; no download/destination creation |
| lab.py run plan against existing runtime/model | Printed argument array; no inference started |
| benchmark.py --prepare-only | Frozen question/source/hash files saved; no model request |
| Silent SSE mock | Parent deadline enforced; exit 124 and unscored evidence |
| Mock tool round trip / truncated final | Allowed source returned; truncation unscored |
| Mock download resume / wrong checksum | Verified resume; wrong bytes never published |
| Archive traversal / symlink / collision | Rejected |
| Local endpoint redirect | Rejected before outbound forwarding |
| Windows RAM/VRAM doctor and WHEA query | Read-only queries passed |
| Pinned runtime --version | Existing binary identifies build 11562 / b2f036c0f |
| Four model revisions, sizes, LFS SHA256 values | Match publisher API |
| Both runtime archive sizes and digests | Match GitHub release API |
| Relative documentation links | No missing targets at validation |
| Public-content audit | 47 files, no findings after metadata redaction fix |
| GitHub CI on implementation eda5eb5 | Windows and Ubuntu jobs passed, including all 13 offline tests on each |

No new Python dependency was introduced. The browser retrieval used existing
headless Edge. The [completed CI run](https://github.com/paras-lehana/local-coding-lab/actions/runs/38603982863)
verified Windows and Ubuntu on implementation commit eda5eb5. Hardware-dependent server startup,
actual model downloads, new model scores, isolated answer-code execution and
editor UI are explicitly unrun here.

## Instructions/context actually inspected

Recovered the parent project's AGENTS and current tasks/reports; maintained
Codex guide, shared topic router, platform and logging protocol, Python/testing
and Git/discovery guidance; the context-maintenance skill and browser-testing
guidance. Inspected current runtime settings/launcher/help and historical
research/flag evidence. The new repo's self-contained AGENTS is the authoritative
portable guide, with small Claude/Copilot adapters. Shared global adapters were
reviewed; their routing needed no change. No unrelated private agent file was read.

## Limitations and next step

The startup gates are conservative profiles, not proof of fit on every PC. A
new model must pass tokenizer/template, allocation and editor checks before a
quality claim. Existing pipeline guards and preserved original evidence remain
the fallback. See next-experiments.md for the actual sequence.

## Git publication

Public repository: https://github.com/paras-lehana/local-coding-lab, branch main.
Initial implementation: eda5eb549fb6fde6fbdfef2dc029e2e76643fa37.
Remote main matched the local implementation commit after push. A subsequent
documentation-only commit records publication and this canonical closeout;
the implementation CI result above belongs specifically to eda5eb5.

Outside this repository, the private parent lab's AGENTS.md and docs/tasks.md
received routing/migration pointers. No parent runtime configuration, model,
credential, editor setting or original experiment report was changed.
