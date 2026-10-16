# What these results support

These are practical limits from this lab's small coding and file-reading cases,
not a claim about every task in a language. The
[campaign report](../reports/2026-10-15-campaign.md) records exact profiles,
deadlines, failed attempts and independent checks. The15October working profile
and editor checks are recorded there. The16October expanded candidates remain
unpromoted pending their separate quality and integration evidence.

| Work | Evidence so far | How to use the model |
|---|---|---|
| Small Python utilities and configuration helpers | Qwen Q4/Q5 and Gemma 26B pass repeated public merge-contract checks; their generated tests can still be wrong. The separate private merge task exposes additional bugs. | Supply the actual contract and nearby code, run independent tests, and inspect copying, mutation, type conflicts and falsy values. |
| Questions about instruction files and setup | Qwen has the strongest completed historical private case, but newer settings vary. Candidates sometimes claim unread sources or omit required guides. | Require actual reads, line-supported answers, a truthful read inventory and explicit unknowns. A path list is insufficient. |
| TypeScript input validation | Held-out answers miss plain-object or integer checks; several fail strict compilation. | Compile with strict settings and test invalid values. Do not accept a plausible interface or an unexecuted self-test as proof. |
| SQLite schema changes | Several GLM answers delete existing data; other candidates fail foreign-key migration. One Gemma unrestricted answer passes all six checks. | Inspect data preservation and transaction order on a disposable copy before considering a real migration. A constraint-only score can conceal data loss. |
| Long-document questions and changed files | Gemma and the historical Qwen profile retrieve all requested facts and counts correctly at roughly52K input tokens in separate two-phase cases. Smaller cases sometimes return correct facts but wrong record counts. | Keep important decisions in versioned notes, retrieve relevant sections, and re-read changed files. This does not establish unlimited chat memory. |
| Running code, applying edits and deployment | Collection offers read-only file tools; generated code is graded separately in isolation. | Treat these results as drafting and diagnosis evidence. They do not establish an unattended implementation/deployment success rate. |

Always distinguish the model's answer from its self-tests. For example, GLM Q6
passed all twelve tests it wrote for one Python answer while an independent check
found missing input validation. In another case the implementation passed, but
the model's own empty-dictionary expectation contradicted the supplied contract.

Native thinking should stay available for the selected reasoning model. There
is no verified universal "ultra" switch: a runtime token ceiling limits thought
length, and removing a nonbinding ceiling can produce exactly the same answer.
The ordinary default remains20minutes for the whole prompt, including input
processing and tools. For the16October expansion, the owner explicitly accepts
slower Coder-Next80B, Gemma31 and QwenQ6 tests; these experimental tasks use a
six-hour whole-prompt ceiling. A completed answer must still pass review before
it supports a recommendation. See [memory and reasoning controls](memory-and-context.md).

Coder-Next80B illustrates why isolated code quality is insufficient for this
workflow: its public Python implementation passes6/6 behavior groups, while
TypeScript passes4/6 and its SQLite migration fails. Its real-instruction audit
repeats incorrect paths until the16-tool-turn limit, with no final answer after
67m55s. More waiting did not produce a completed repository audit in that run.
[Measured attempt and limits](../reports/2026-10-16-coder-next.json).

Dense Gemma31 improves the private merge helper to6/6, including mutable-copy
isolation, but its overall instruction audit is26/36 after2h00m34s. It omits
required guidance and misreports its read inventory. Public Python also passes
6/6, while TypeScript passes5/6 and SQLite fails on foreign keys. Its separate
test block lacks an import; combining the unchanged code and tests passes all
six self-tests. Long reasoning and a dense architecture did not establish a
better complete workflow in this case. [Dense results](../reports/2026-10-16-gemma31.json).
