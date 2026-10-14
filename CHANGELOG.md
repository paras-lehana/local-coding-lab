# Changelog

## 0.2.0 — 2026-10-14

- Run and publish the first controlled Qwen placement pair, including source
  grounding, separate prefill/generation timings, memory and score limitations.
- Add process RAM telemetry, an explicit owned-server stop file and Windows
  dedicated GPU-memory capture. Preserve all existing resource thresholds.
- Add optional Linux/bubblewrap grading with no host fallback, six independent
  contract checks and failure-boundary tests. One model-written test fails even
  though both corrected functions pass the independent contract checks.
- Expand PowerShell CI parsing and update measured profile evidence and docs.

No new weights, editor changes or production profile promotion in this release.

## 0.1.0 — 2026-10-14

- Establish a public Windows/CUDA local coding research repository.
- Add pinned, hash-verified runtime/model downloads and explicit launch plans.
- Add resource monitoring, child-process ownership and local-only serving.
- Add a synthetic instruction/router/code fixture and bounded streaming/tool
  collector; generated code is not executed by the collector.
- Preserve sanitized historical evidence separately from the new public fixture.
- Import the supplied Gemini research with provenance/redactions and a critical
  review; define the next controlled experiments.
- Add offline tests, publication audit, CI and contributor documentation.

No new model inference or public-fixture quality score is part of this release.
