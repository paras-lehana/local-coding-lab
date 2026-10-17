# Copilot context rejection and persistent defaults

17 October 2026, 11:43 IST · Local Coding Lab v0.4.1.

| Request | Status | Result |
|---|---|---|
| Fix the failed local-model chat | Mitigation applied; fresh-chat verification pending | Copilot rejected static context before sending to the healthy server. Applied a Qwen-only MCP-tool exclusion. |
| Make Autopilot and Allow all defaults | Configuration done; fresh-chat UI not verified | Added the installed build's new-harness and Local-harness default settings. |
| Continue without typing in the editor | Done | No prompt was sent and no chat was cleared. Read-only inspection and configuration checks continued. |

## What actually failed

At 11:30:58, the active Copilot Agent Host logged:

> Static system messages and tool definitions exceed the model's usable context budget. Reduce static context or switch to a larger-context model.

Its warning type was `compaction_static_context_blocked`. Immediately afterward,
it returned the exact `No response was returned` error shown in the screenshot.
The selected BYOK model was the installed local Qwen alias, in the broad
Hackathons workspace. This was an upstream context rejection, **before model
inference**, not evidence of Qwen taking 20 minutes to answer a greeting.

The server was still the same owned process from the 11:07 restoration. Health
was `ok`; its last inference task was still 385 from the earlier API check, and
the server log contained no corresponding new model request. At 11:32 it had
13.31 GiB resident RAM, 4.70 GiB dedicated VRAM and 8.49 GiB system free RAM. It had
not unloaded or restarted. It remained healthy at 11:42.

The saved failed session's system-message body contained 53,305 characters.
Tokenizing that body with the local Qwen tokenizer produced 12,291 tokens.
This excludes chat framing, tools and other request components. **The total
tool-definition token count was not captured**, so no exact attribution of the
remaining budget is claimed.

A separate Chrome DevTools MCP startup error referenced an unresolved
`${input:browser_url}`. That tool configuration was not repaired or identified
as the primary cause of this chat failure. No browser or unrelated MCP service
was reconfigured.

## Why the permission choices kept resetting

The running application was VS Code 1.141.1, with bundled Copilot 0.69.0. Newer
build directories existed on disk, but the running process used the 1.141.1
resources; no update/restart was performed.

The user already had `chat.tools.global.autoApprove: true` and
`chat.autopilot.enabled: true`. Those did not establish the newer Copilot
harness's default mode and permissions. The installed workbench registers
`chat.defaultConfiguration`, whose defaults were interactive/manual. Its
new-session implementation reads that setting. The separate Local harness
uses `chat.permissions.default`.

The following settings were added to the owner's VS Code User settings:

```json
{
  "chat.defaultConfiguration": {
    "mode": "autopilot",
    "approvals": "allowAll"
  },
  "chat.permissions.default": "autopilot"
}
```

These are the requested defaults for **new sessions**, not a rewrite of
existing session state. The saved selections can still differ in existing
chats. Enterprise policy, if present, remains authoritative; no policy or
consent storage was bypassed. The owner's explicit request authorizes these
preferences. The portable installer does not enable them for other users.

[Microsoft's permissions guide](https://code.visualstudio.com/docs/agents/run/approvals)
distinguishes the newer Copilot mode picker from the Local harness permission
picker. The exact new-harness setting and allowed enum values above were
verified in the **running installed bundle**, rather than inferred from a
different VS Code version's documentation.

## Context mitigation applied

The installed Agent Host's native tool-search deferral checks supported model
families. Qwen does not pass that check. Enabling the generic tool-search
switch therefore does not demonstrate deferred MCP schemas for this model.

Applied the installed model-specific capability setting:

```json
{
  "chat.agentHost.copilot.modelCapabilityOverrides": {
    "customendpoint/Local llama.cpp/qwen3.6-35b-a3b-q4": {
      "excludedTools": ["mcp:*"]
    }
  }
}
```

The installed source reads overrides by the selected model ID, accepts tool
patterns and passes exclusions into the SDK session configuration. This limits
the mitigation to this Qwen model. Built-in/custom coding tools and the user's
instructions are unchanged; other models retain their tool settings. MCP tools
are excluded for this local model, so external MCP capabilities should not be
expected in that profile. This does not necessarily stop MCP connection startup.

The intended effect is a smaller static tool set while retaining file reads,
edits and terminal operations. This is a **mitigation awaiting a fresh-chat
test**, not a measured guarantee that every workspace now fits. No model
family was spoofed and no context limit was falsely enlarged. The server
remains 64K, the client 48000 input/16384 output, with native thinking unchanged.

## What was verified, and what was not

- Windows DPAPI encrypted backups of User settings and model configuration
  were created under ignored local evidence storage; decrypt/hash round trips
  passed. No credential content was printed or committed.
- Compared the final parsed settings with the decrypted original. **Exactly
  three new keys** were added; every pre-existing value was unchanged.
- Read the actual registered schemas, new-session default handling, BYOK model
  identity mapping, tool-pattern handling and Qwen's tool-search family check.
- 27 offline tests passed in 10.168s, with server slots idle before the run.
  Four PowerShell scripts parsed. No benchmark-generated code or new model
  inference was executed during these checks.
- Read-only UI inspection found the dedicated Local LLM window, existing local
  model selection and Autopilot/Allow all labels. Those were **existing-session
  values**, so they do not prove that the new defaults took effect.
- A guarded attempt to bring that window forward failed while Edge held focus;
  it aborted before opening a chat or sending a prompt. The owner then explicitly
  requested continuing without typing. No further editor input was attempted.
- Consequently, neither a fresh-session default selection nor a successful
  Copilot response after the exclusion is claimed. The earlier API pass remains
  valid within its narrower scope.

## Changes, evidence and next check

Local functional change: only
`%APPDATA%/Code/User/settings.json`.
Model configuration and Continue settings were not edited; no server restart,
download, deletion, cloud evaluation, hardware or binary patch occurred.
The server is intentionally left running.

Raw evidence remains ignored under
`local-data/2026-10-17-copilot-repair/`: encrypted backups, settings-change and
validation receipts, source hashes, exact failure excerpts and read-only UI
inventory. The failed native session transcript was inspected locally, not
published. Public changes are this report/request, editor guidance, lifecycle
regression guidance and prompt/task indexes. The context-maintenance skill was
used for the project lesson; shared Codex/Claude routing remains unchanged.

The next actual check is a **new Copilot chat** with this local model: verify
Autopilot/Allow all are already selected, send a greeting, confirm it reaches
llama-server, then request a cited file read. Do not use the old failed chat as
proof that session-construction changes were applied. If static context still
exceeds capacity, capture the actual remaining tool inventory and budget before
further exclusions or a context increase.

The attached screenshots are owner-provided symptom evidence. No new screenshot
or successful UI result was generated. Original request is preserved in
[owner-request.txt](owner-request.txt).

## File inventory and validation closeout

| File | Change |
|---|---|
| Local VS Code User `settings.json` | Three new settings: new-harness defaults, Local-harness default, Qwen-specific MCP exclusion. |
| Parent installation `AGENTS.md` | Local operational reminder of the client failure and deferred UI check. |
| Project `AGENTS.md` | Fresh-chat regression and client-budget diagnostic guidance. |
| `README.md` | Link to this follow-up with partial status. |
| `docs/editors.md` | Installed-version defaults and context-failure troubleshooting. |
| `docs/tasks.md` | Decisions, evidence and deferred checks. |
| `docs/tasks/README.md` | Report index entry. |
| `docs/prompts.md` | Owner request, constraint and canonical closeout. |
| This report and `owner-request.txt` | Reviewed findings and original request. |

The project guidance, README, task log, methodology and editor guide were read.
The shared Codex guide, platform rules, logging protocol, Claude topic router,
Codex setup guide and context-maintenance skill were reviewed or recovered from
the same session; this closeout does not claim newly reading every linked rule.
Installed VS Code workbench, Agent Host and Copilot SDK source were inspected.
No dependency was introduced or removed. No web application changed, so mobile
browser validation is inapplicable; the actual desktop regression remains open.

At 11:46 IST, health and model identity still passed, and both production server
and manager were alive. The public-content audit caught one personal home path
in this draft; it was replaced with an environment-relative path before commit.
The checked-in report contains no raw transcript or credential material.

Evidence commit `581ba52` is published on public `main`. The corrected audit
checked 155 files with zero findings; 181 relative file targets resolved and
the staged whitespace check passed. CI run 39009418382 was still running at
closeout preparation; no new CI success is claimed here. The exact prepared
A-G response is preserved in the prompt log before the final reply.
