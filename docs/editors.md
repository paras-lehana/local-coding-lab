# VS Code integration

## Copilot rejects a request before inference

The17October user report exposed a failure that a healthy API cannot detect:
Agent Host rejected system instructions plus tool schemas with
`compaction_static_context_blocked`, then showed `No response was returned`.
The local server never received that request. Check Agent Host logs and current
server activity before blaming reasoning speed or restarting the model.

The installed1.141.1 build does not enable native tool-search deferral for Qwen.
A model-specific `excludedTools: ["mcp:*"]` override was applied to the owner's
local Qwen alias to reduce static context while preserving built-in/custom
coding tools and instructions. It excludes external MCP tools for that model;
other models are unchanged. This mitigation has **not yet passed a fresh UI
test**, because the owner requested no editor typing. See the
[failure/defaults report](tasks/2026-10-17-copilot-context-defaults/2026-10-17-copilot-context-and-defaults-v0.4.1.md)
for exact settings, evidence and limitations.

For users who want persistent autonomous defaults, this build's newer Copilot
harness reads `chat.defaultConfiguration` with `mode: "autopilot"` and
`approvals: "allowAll"`; the Local harness uses
`chat.permissions.default: "autopilot"`. Merely enabling the older global
auto-approval/Autopilot switches did not configure the newer session defaults.
These are optional user preferences, not portable installer defaults. Existing
chats can retain prior values. Recheck the installed schema after upgrades.

## Configure and verify the connection

First verify the API and exact model alias using the setup guide. This repository
does not rewrite existing VS Code or Continue settings. Keep a backup and add a
new local model entry so existing providers remain available.

For VS Code Copilot, use the installed model manager's local/custom OpenAI-
compatible endpoint option, where available. Set base URL
`http://127.0.0.1:8080/v1` and the alias returned by `/v1/models`. UI labels and
provider capabilities vary by extension version. Do not advertise unsupported
reasoning effort levels or invent arbitrary `modelOptions` fields.

For Continue, a starter YAML model entry is:

```yaml
name: Local Coding Lab
version: 1.0.0
schema: v1
models:
  - name: Qwen lab
    provider: deepseek
    model: qwen36-lab
    apiBase: http://127.0.0.1:8080/v1/
    apiKey: local-unused
    defaultCompletionOptions:
      contextLength: 48000
      maxTokens: 16384
    requestOptions:
      timeout: 1200000
```

For the inspected **Continue 2.0.0**, this deliberately uses its Deepseek adapter
with an explicit loopback URL. The installed adapter enables transport of prior
`reasoning_content`; its generic OpenAI adapter leaves that capability disabled.
The provider name here selects a serializer, not a hosted DeepSeek model. Keep
the loopback URL explicit. This is source/configuration evidence; successful
multi-turn UI file/history transport now succeeds, while exact prior-reasoning
wire serialization was not captured. Recheck this behavior for a
different Continue release rather than assuming the workaround is permanent.

This budget is specifically for the64K Qwen working profile. The completed
finalist suite used16384 output tokens for coding and succeeded on a separate
roughly52K-input history case. Continue2.0.0's history pruner reserves only1000
tokens, so the48000 input budget leaves room for the16384 output allowance
and some overhead. These are client budgets, not extra model context. It is **not** suitable
for the proposed 32K Gemma profile. For that profile start with a conservative
24000 input / 8192 output budget and verify the actual request; wrappers and
tool definitions also consume context. Check the schema for your installed
Continue version. [Continue configuration reference](https://docs.continue.dev/reference).

Start in a small project workspace and a fresh chat. Ask the model to read the
entry instruction file, follow one linked rule, inspect a code file and cite
all three. Inspect tool logs and the final answer. An API test does not prove
the editor sends history/tools correctly; a spinner does not prove inference.

For automatic file discovery in Continue, use **Plan** for the read-only test:
Chat mode offers no tools, whereas Plan exposes built-in reading/searching
tools. Chat can still receive explicitly attached context. Agent mode adds
editing and execution tools. Plan does not filter third-party MCP tools, so
the test's actual tool inventory must still match its read-only scope.
[Continue mode behavior](https://docs.continue.dev/ide-extensions/agent/how-it-works),
[Plan mode details](https://github.com/continuedev/continue/blob/main/docs/ide-extensions/plan/how-it-works.mdx).

Instruction discovery also depends on the selected VS Code harness. The current
official documentation places personal Copilot instructions in
`~/.copilot/copilot-instructions.md`; the Local harness has separate discovery
settings. Its `chat.includeReferencedInstructions` default is **false** and
applies to Markdown links, not arbitrary paths written in backticks.
[Instruction locations](https://code.visualstudio.com/docs/agent-customization/custom-instructions),
[setting defaults](https://code.visualstudio.com/docs/agents/reference/ai-settings#custom-instructions-settings).

The inspected Windows adapters already tell the model to read the project
entry, shared router and applicable sources explicitly. Their presence is
configuration evidence; actual delivered files and successful tool reads still
need verification in a fresh editor conversation. Do not mistake an instruction
index for the contents of every listed document. Loading an entire shared
library would also consume prompt time and context that the coding task needs.

Configuration2.0 now has actual Copilot and Continue greeting, source-read and
changed-file/history evidence. All six observed completions were under five
minutes, including Continue's manual read approvals and observation delays.
Both retained the earlier marker and returned the fresh file values. Both also
missed the Python-specific instruction target; Copilot cited an unread report
in its follow-up. These are integration results, not a claim of perfect answers.
[Reviewed editor results](../reports/2026-10-15-editor-results.json).
The benchmark's 1200-second deadline applies to its own worker; editor socket
timeouts do not automatically enforce the same whole-conversation limit.

The installed Continue 2.0.0 bundle also has a timeout-unit mismatch: its
OpenAI-compatible adapter passes `requestOptions.timeout` directly to the SDK
in **milliseconds**, while its custom fetch agent multiplies that same value
by 1000. For this adapter, `86400` therefore permits only 86.4 seconds at the
SDK layer; `1200` would mean 1.2 seconds there. The installed local entry now
uses `1200000`, a20-minute SDK request timeout. This source finding is specific to the
inspected build; it is not an observed editor timeout test, nor a total deadline
across streaming and multiple tool rounds. Keep an explicit elapsed-time limit
when validating a conversation. Recheck the installed implementation on upgrade.

For read-only Copilot integration checks, the existing Local Files custom agent
offers only file reading/searching. Custom agents can declare an explicit tool
list; select the intended local model and inspect actual calls. The saved editor
test plan checks a greeting, real instruction/runtime files, then a changed-file
read plus an earlier chat marker. This sequence was actually completed on15October.
[VS Code custom-agent tools](https://code.visualstudio.com/docs/agent-customization/custom-agents#header-optional).

## What the live checks revealed

Copilot's greeting sent13,216input tokens and needed71.48seconds of server work;
Continue sent4,744tokens and needed29.58seconds. Most of each greeting was input
processing, not thinking. Workspace instructions and tools affect even a short
message. The source questions took264.44seconds of server work in Copilot versus
105.72seconds in Continue, but Continue's five separate read approvals increased
observed elapsed time to an upper bound of286.08seconds. These are sequential
workflow observations with different harnesses and cache reuse, not cold-start
throughput comparisons.

Check for a pending **Read File / Accept** control before diagnosing an idle GPU.
Approve the intended source read; the experiment did not enable blanket tool
permissions. Plan mode and no configured MCP servers were verified. The Copilot
large-file tool twice returned a size-limit message with a success flag; only a
later lines1–150 read returned source bytes. Inspect returned content, not only
the tool's green completion label.

For instruction-heavy work, make retrieval explicit before implementation:

> Read the project AGENTS.md, the shared topic router, and its applicable
> language-specific v2 rules. List the exact files and ranges actually read;
> identify missing sources before editing. Re-read any changed file. Separate
> historical observations from current measurements, and cite only sources you
> received. A path mentioned in an index does not count as a file read.

This is a recommended prompt pattern, not a measured fix for the routing defects.
Keep independent syntax/type/behavior tests. The six probes did not test editing
or execution tools, long repository implementation, or arbitrary128K conversations.
