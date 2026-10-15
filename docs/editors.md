# VS Code integration

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
multi-turn UI transport still needs observation. Recheck this behavior for a
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

Earlier private evidence includes a real three-file Copilot reply. Current
configuration2.0 is installed, but fresh Copilot/Continue UI validation remains
blocked while Windows exposes no interactive desktop. Configuration/API success
does not establish the editor flow. Continue UI success remains unverified.
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
read plus an earlier chat marker. Preparing that plan is not a completed UI test.
[VS Code custom-agent tools](https://code.visualstudio.com/docs/agent-customization/custom-agents#header-optional).
