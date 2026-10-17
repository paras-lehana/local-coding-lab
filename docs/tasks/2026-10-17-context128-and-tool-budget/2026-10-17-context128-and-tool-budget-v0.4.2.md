# 128K context and Copilot tool-budget repair

17 October 2026, local Windows installation. Closed as a partial integration
repair when the owner redirected work to idle unloading and desktop controls.
This report's v0.4.2 draft is published with the v0.5.0 desktop release.

| Owner request | Status | Result |
|---|---|---|
| Local Copilot is still not working | Response observed; latency unacceptable | Earlier static-context failure mitigated. Owner's later greeting reached Qwen but took about7m42s to final text. |
| More context for instruction files | 128K loaded; partial validation | Installed-engine source test completed;70K probe deliberately interrupted for the owner's chat. |
| Preserve no editor typing | Honored | No clicks, typing, chat clearing or window focus changes. Separate installed-engine tests only. |

## Why 64K was shown

64K was a conservative deployed profile, not the model's native limit. The
loaded GGUF reports262144 training context. Previous128K synthetic recall
completed near120K input, but with another placement/load profile. Those tests
did not establish that every editor instruction/tool set would fit or work.

Server capacity, client input budget and maximum output are separate values.
Before this repair the server was65536, client input48000 and output16384.
Now the server is131072, client input98304 and output16384, leaving16384 tokens
of additional margin. Copilot's explicit contextWindow is131072. Continue's
input budget is98304; its installed history pruner has a separate output
reserve behavior. No unsupported reasoning-effort level was invented.

The first validation used110000 input tokens. It was then reduced to98304
because the same captured system text measured16139 tokens with Qwen versus
15241 with the SDK tokenizer. A displayed token estimate is not necessarily
the model's exact count. The16K reserve is a conservative margin, not a proven
universal upper bound on tokenizer differences.

## The repeated client failure and the revised tool scope

The active VS Code build changed from1.141.1 to1.142.0. New Agent Host logs
confirm the original `mcp:*` override was applied, then repeated
`compaction_static_context_blocked` warnings. The server remained idle on its
old task; no corresponding greeting reached it.

Installed source distinguishes native MCP tools from external editor tools,
which can arrive under the `custom` category. An MCP-only exclusion does not
cover that entire path. This is a concrete gap in the earlier mitigation; the
complete failed editor tool inventory was not captured, so its exact total
token count and largest individual contributors remain unknown.

The local Qwen model now has `availableTools: ["builtin:*"]` and
`excludedTools: ["mcp:*", "custom:*"]`. This retains native file reading,
search, creation, editing and PowerShell tools. Extension-provided and MCP
tools are excluded for this model only. Other model profiles remain unchanged.
Explicit model capability limits match the actual server and client budgets.

A separate loopback protocol fixture used the installed Copilot engine with
the captured68,818-character system message and native tools. Both64K and128K
configurations reached that fixture without a static-context warning. The
engine counted15,245 system tokens,6,737 tool tokens across17 native tools,
and67 conversation tokens. **This is a budgeting/transport check with a fixed
fixture answer, not a model quality result or successful editor UI test.**
It demonstrates that the instruction text plus native tools fits even64K;
128K provides substantially more room for files and conversation history.

## Loaded128K RAM-KV profile

Model remains Qwen3.6-35B-A3B UD-Q4_K_M, pinned artifact and isolated
prefetch-opt-out runtime unchanged.37 CPU expert blocks, all other eligible
tensors GPU,4/8threads,512/128 batches and native thinking retained.
New flags: `--ctx-size 131072 --no-kv-offload`, retaining q8 K and V.

Loader evidence:1360MiB CPU q8 attention KV,62.81MiB CPU f32 recurrent state,
3381.34MiB GPU weights,439MiB GPU compute workspace. Allocated KV capacity
does not grow linearly as occupied tokens increase. RAM cache is not a durable
memory of omitted chat messages or files that were never read.

Early loaded RAM was17.16GiB; during actual instruction prefill the resident
cap reached22.00GiB and dedicated-process GPU memory measured4.00GiB.
One later monitor sample had5.80GiB free physical RAM,28.15GiB available commit
and2904MiB free device VRAM. These are timestamped observations, not guaranteed
future capacity. Existing RAM/VRAM/commit/temperature/WHEA stops remain active.

## Completed and interrupted validation

- Six DPAPI encrypted configuration/launcher backups passed roundtrip checks.
-27 offline tests passed in10.444seconds before model inference.
- The idle64K server was gracefully stopped through its owned stop file;
  new128K production server loaded with one slot and the same alias.
- A real installed-engine greeting returned exactlyREADY with native reasoning.
- Real system-text/four-file instruction test completed in378.437seconds:
  all four allowlisted files read, required facts answered correctly, no SDK
  warnings/errors. One citation was wrong: it linked a shared instruction
  statement to an unreturned adapter path and labeled that the project file.
  This remains a grounding defect; successful transport is not perfect quality.
- This live test used the actual captured system text but one controlled
  read-only tool, rather than the complete editor tool inventory. The native
  tool fixture separately covered17 built-ins without invoking them.
- The70K probe was deliberately canceled after16384 processed tokens to release
  the single slot for the owner's actual chat. It is unscored, not an OOM or a
  completed capacity/recall/history test. An interruption receipt accompanies
  the raw worker-error result. No further comparison was started.
- The owner clarified the chat is in the same local window. Its real greeting
  supplied28659 prompt tokens. Server input processing took372.689s at76.90tok/s;
  the first generation took3.248s for35tokens. It also waited behind our probe
  until we canceled it. The observed final greeting arrived about7m42s after
  the owner's send; the native session then called its task-complete tool.
  The response is confirmed by editor events, not by new assistant typing.
- Actual session began on Auto before switching to Qwen. The installed source
  applies tool selection on session creation/resumption; the complete actual
  editor inventory is still not captured. Do not claim that the intended
  builtin-only filter was proven for this session solely from saved settings.

The later [idle/widget task](../2026-10-17-idle-widget/2026-10-17-idle-widget-v0.5.0.md)
retains these inference settings and changes lifecycle only. Larger context
does not make a large prompt quick, and spare VRAM is not an automatic cure
for CPU expert execution. No full new quality score was collected.

Private evidence: ignored `local-data/2026-10-17-context128/`. No raw private
instructions, editor transcript, credential or encrypted backup is published.
No new model download, cloud evaluation, hardware change or app closure.

Primary references: [VS Code custom endpoint configuration](https://code.visualstudio.com/docs/agent-customization/language-models)
documents explicit contextWindow and input/output budgets. Separate upstream
[tool-catalog pressure report](https://github.com/github/copilot-cli/issues/5151)
and [BYOK budget forwarding issue](https://github.com/microsoft/vscode/issues/336980)
describe related failure modes; they do not establish this host's exact cause.
