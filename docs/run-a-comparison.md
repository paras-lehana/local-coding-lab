# Run a reproducible model comparison

Install a pinned model/runtime using the [setup guide](setup.md), then choose a
profile whose memory gates fit your machine. The profiles are experiment records,
not automatic hardware detection. Check their `evidence` and the
[current campaign report](../reports/2026-10-15-campaign.md) before using them.

The trial runner owns one monitored server, verifies its model alias, sends a
small smoke prompt, collects the selected tasks and stops that server afterward.
An existing llama-server on any port prevents another launch. It never stops
another application's server, restarts Windows or changes clock settings.

For example, with existing artifacts under `E:\llm`:

```powershell
python trial.py --profile gemma4-balanced-campaign --runtime-dir E:\llm\llama.cpp --model-path E:\llm\models\gemma-4-26B_q4_0-it.gguf --tasks benchmarks/plans/gemma-thinking-tasks.json --output local-data/my-gemma-attempt-1 --apply
```

This is a live inference command. It defaults to loopback port 8081 and refuses
an occupied port. Use a fresh output directory for every attempt. The trial
records its exact profile and tasks before loading; failed and interrupted runs
remain available for inspection. After a reboot, read `trial.json`, launcher
logs, server logs and Windows events before starting a new attempt. A `running`
checkpoint from an earlier boot does not mean the process still exists.

| Plan | What it collects |
|---|---|
| `full-thinking-tasks.json` | Three core seeds, unrestricted thinking, changed-file history, TypeScript/SQLite |
| `full-nonthinking-tasks.json` | Three core seeds and both scenarios, with no thinking budget |
| `gemma-thinking-tasks.json` | Thinking plan plus temperature 1.0, with the profile's top-k 64/top-p 0.95 |
| `glm-thinking-tasks.json` | Thinking plan plus temperature 0.7; this alone is not the full publisher sampling configuration |
| `dense-calibration-tasks.json` | One 500-token inline probe, capped at five minutes; no autonomous file-discovery score |
| `placement-tasks.json` | One core seed and changed-file history for placement comparisons |
| `long-history-tasks.json` | 320- and 640-record ledgers; use a sufficiently large context and record model-specific token counts |

The ordinary whole-task deadline is 1200 seconds across all tool calls and user
phases. A per-request reasoning ceiling is separate from that deadline and does
not create a model-native "ultra" effort setting. A deadline or token-limit
answer is incomplete and unscored. `collected` means answers were saved; it does
not mean the model passed. A deadline, worker error or harness error stops
further tasks in that attempt; an answer with code bugs is still collected.

For explicitly slower experiments, a task's `deadline` may be increased to at
most 21600 seconds. The default stays 1200. `trial.py --load-timeout` and
`--smoke-timeout` control the separate startup probes; neither changes a task's
whole-prompt allowance. Keep all settings in the saved task/profile record.

To measure growing input on a server you explicitly started and own:

```powershell
python context_growth.py --endpoint http://127.0.0.1:8081/v1 --model qwen36-lab --pid YOUR_SERVER_PID --targets 2048 16000 32000 60000 --output local-data/context-attempt-1
```

Replace `YOUR_SERVER_PID` with the PID in that launcher's `process.json`.
Use a context limit above the largest input plus chat overhead and output.
The collector freezes requests and records actual tokenizer counts, slot state,
process RAM, dedicated VRAM, timing, source-marker recall, changed-file history
and a request that deliberately omits history. It does not launch or stop a
server, alter editor settings, or execute generated code. Its request worker is
cancelled at the explicit deadline; confirm the owned server is idle afterward.

Review `request-*.json`, successful file reads, final text, reasoning, timings
and memory telemetry. Grade source claims against the bytes actually delivered.
Then review generated code and use the [isolated graders](grading.md). The
collector never executes that code. Do not replace a failed answer with a fixed
version before preserving its initial grade.

Keep raw results in ignored `local-data/`. Publish only reviewed aggregates with
artifact SHA256, profile, case identity, completion status and limitations. The
public questions and scenarios contain synthetic project instructions, not the
maintainer's private files. They are a useful controlled test, not a guarantee
that a model will follow every real repository or editor prompt.
