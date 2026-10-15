# What these results support

These are practical limits from this lab's small coding and file-reading cases,
not a claim about every task in a language. The
[campaign report](../reports/2026-10-15-campaign.md) records exact profiles,
deadlines, failed attempts and independent checks. Final profile selection and
editor validation are still in progress.

| Work | Evidence so far | How to use the model |
|---|---|---|
| Small Python utilities and configuration helpers | Qwen Q4/Q5 and Gemma 26B pass repeated public merge-contract checks; their generated tests can still be wrong. The separate private merge task exposes additional bugs. | Supply the actual contract and nearby code, run independent tests, and inspect copying, mutation, type conflicts and falsy values. |
| Questions about instruction files and setup | Qwen has the strongest completed historical private case, but newer settings vary. Candidates sometimes claim unread sources or omit required guides. | Require actual reads, line-supported answers, a truthful read inventory and explicit unknowns. A path list is insufficient. |
| TypeScript input validation | Held-out answers miss plain-object or integer checks; several fail strict compilation. | Compile with strict settings and test invalid values. Do not accept a plausible interface or an unexecuted self-test as proof. |
| SQLite schema changes | Several GLM answers delete existing data; other candidates fail foreign-key migration. One Gemma unrestricted answer passes all six checks. | Inspect data preservation and transaction order on a disposable copy before considering a real migration. A constraint-only score can conceal data loss. |
| Long-document questions and changed files | Gemma retrieves all requested facts and counts correctly at roughly 52K input tokens in one two-phase case. Smaller cases sometimes return correct facts but wrong record counts. | Keep important decisions in versioned notes, retrieve relevant sections, and re-read changed files. This does not establish unlimited chat memory. |
| Running code, applying edits and deployment | Collection offers read-only file tools; generated code is graded separately in isolation. | Treat these results as drafting and diagnosis evidence. They do not establish an unattended implementation/deployment success rate. |

Always distinguish the model's answer from its self-tests. For example, GLM Q6
passed all twelve tests it wrote for one Python answer while an independent check
found missing input validation. In another case the implementation passed, but
the model's own empty-dictionary expectation contradicted the supplied contract.

Native thinking should stay available for the selected reasoning model. There
is no verified universal "ultra" switch: a runtime token ceiling limits thought
length, and removing a nonbinding ceiling can produce exactly the same answer.
The owner's practical limit remains 20 minutes for the whole prompt, including
input processing and tools. See [memory and reasoning controls](memory-and-context.md).
