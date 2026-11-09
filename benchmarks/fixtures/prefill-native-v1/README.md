# Native prefill diagnostic v1

This public synthetic fixture supports the 9 November microbatch, RAM-residency
and expert-cache experiments. It is a performance and cache-invalidation
diagnostic, not a coding or instruction-following benchmark. Prepared inputs
are not results; consult the dated experiment report for actual run status.

`requests.json` contains the exact three request bodies, in order:

1. `cold`: a 6,844-byte prefix containing 64 synthetic records, with prompt
   caching disabled.
2. `repeat`: the identical prefix with prompt caching requested.
3. `changed-middle`: only record032's marker changes from `MARKER_032` to
   `CHANGED_032`; caching remains requested.

Send each `payload` to the owned llama-server **`/completion`** endpoint. These
are native completion bodies, not `/v1/chat/completions` messages. They do not
apply a chat template. The fixed settings are greedy generation, seed73,
32generated-token ceiling, five token probabilities, non-streaming output and
slot0. Keep one server slot and one request at a time. No expected answer is
included in the final question; the model must obtain the marker from the prefix.

Use a fresh guarded server for each profile and preserve its admission/stop
receipts. The original seven `flint-q3xl-prefill-*` profiles separately vary microbatch,
RAM residency, expert-cache budget or runtime. Model identity, context and
remaining settings must match the documented control. Never load these profiles
beside an existing inference engine, bypass memory floors or close someone
else's applications to force admission.

Later `u64-cache1536-resident3` and `u128-cache1536-resident3` profiles are
combined follow-ups. They change multiple controls and must be reported as
such; preparing them does not establish either fit or an additive speedup.

The later `short2k-windowed` / `short2k-fullswa` pair uses the same fixture
inside a2,048-token context. Both use b64/u64, cache1536 and resident3;
only `--swa-full` differs within that pair. This stores sliding-window KV
for older positions to investigate rollback; it does not extend the model's
trained attention window. Estimated KV is57.64 versus104.125MiB before
alignment/checkpoints. Actual allocation, cache reuse and timings must be
measured. Both profiles completed9November; the aggregate records actual
buffers and partial-prefix reuse. Their short context does not qualify the
real private source audit, and changed short outputs are not quality scores.

Save the full response, `timings`, token probabilities, request wall time,
tokenized input length and contemporaneous RAM/commit/VRAM samples. Inspect
the actual `cache_n`, `prompt_n` and `predicted_n`: a requested cache hit is
not proof of reuse. Record marker correctness and every output/deadline/resource
limit separately; these outcomes carry no private-audit points.32tokens may
truncate output, so output differences require inspection, not an assumed
semantic regression. The fixture is much smaller than a real instruction audit.

"Cold" here means prompt-cache cold. The launcher verifies the weight hash
before loading, which can warm Windows' file cache. No OS cache flush is used.
The private controller's `load_seconds` measures launcher start to API readiness,
including that verification; it is not an isolated deserialization measurement.
Desktop load remains a source of variance. Repeat the initial u16/resident1
control after the seven profiles, using a fresh output directory, to expose
drift. A single sequence remains exploratory even with this stability check.

After all three timed requests, these diagnostic profiles use60second native
idle sleep to expose expert-cache destructor counters. Observe passive `/props`
and native `llama_moe_cache:` statistics together; an early sleeping flag alone
does not establish completed destruction. Unexpected sleep between requests
invalidates cache comparison. Wait at most120seconds for the counters and mark
missing data explicitly. This time is excluded from request latency. Production
idle behavior is a separate configuration and is not changed by this fixture.
