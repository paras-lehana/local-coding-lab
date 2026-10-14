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
    provider: openai
    model: qwen36-lab
    apiBase: http://127.0.0.1:8080/v1
    apiKey: local-unused
    defaultCompletionOptions:
      contextLength: 40000
      maxTokens: 24576
```

This budget is specifically for the 64K Qwen reference: prior inspection of
Continue 2.0.0 found its history pruner reserved only 1000 tokens, so the input
budget was reduced to leave room for the larger output. It is **not** suitable
for the proposed 32K Gemma profile. For that profile start with a conservative
24000 input / 8192 output budget and verify the actual request; wrappers and
tool definitions also consume context. Check the schema for your installed
Continue version. [Continue configuration reference](https://docs.continue.dev/reference).

Start in a small project workspace and a fresh chat. Ask the model to read the
entry instruction file, follow one linked rule, inspect a code file and cite
all three. Inspect tool logs and the final answer. An API test does not prove
the editor sends history/tools correctly; a spinner does not prove inference.

Earlier private evidence includes a real three-file Copilot reply. Continue UI
success remains unverified. This repository creation did not rerun either UI.
The benchmark's 1200-second deadline applies to its own worker; editor socket
timeouts do not automatically enforce the same whole-conversation limit.
