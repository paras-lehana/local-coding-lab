# Contributing

Start with AGENTS.md and docs/methodology.md. Keep proposals separate from
measurements and preserve exact model/runtime/fixture versions. Smaller reports
with complete evidence are more useful than unsupported leaderboards.

No paid APIs, GPU or downloaded weights are required for the offline checks:

```powershell
python -m unittest discover -s tests -v
python scripts/audit_public.py
```

Before a pull request, inspect every Git-visible file. Do not add private
instruction files, prompts, editor screenshots, tokens, browser HTML, weights or
binaries. Put experiment artifacts in ignored local-data/ and publish a reviewed
digest using reports/TEMPLATE.md. The audit catches common patterns; it is not
a substitute for reviewing content and Git history.

For a new downloadable model, record repository, immutable revision, exact file,
byte count, SHA256, publisher/model/license links and the date checked. For a
runtime update, pin both binary and CUDA-library archives and their SHA256s.
Explain which capabilities required the update. Never silently change the
runtime for an existing comparison.

Add meaningful offline regression coverage for installer, path, process or
deadline behavior. No executing model-generated code in CI. Keep fixture answers
and evaluator material out of the model's source allowlist. Before changing a
fixture, give it a new version so earlier results remain interpretable.
