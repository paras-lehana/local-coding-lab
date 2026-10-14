# Data and execution boundaries

The default benchmark accepts only explicit loopback HTTP endpoints, blocks
redirects and ignores system HTTP proxies. Its file tool serves only frozen
public fixture text. It has no shell, file-write or generated-code execution
tool. Do not add private source files to a public fixture.

Downloads use pinned publisher URLs, full sizes and SHA256 hashes. ZIP
extraction rejects traversal, symlinks and collisions. These checks establish
integrity against the catalog, not the trustworthiness of a publisher. Review
catalog changes before downloading or running third-party binaries.

The server launcher binds to loopback, owns one process, stops only its child,
and leaves existing models/editor configuration alone. Resource polling is a
practical stop mechanism, not a hardware-stability guarantee.

Keep API keys in your own secret store outside this repository. The local lab
needs no OpenRouter or cloud key. Never paste a key into an issue or benchmark
answer. Raw answers and requests may contain sensitive content if you customize
the harness; ignored local-data/ is not encrypted storage.

Report security issues privately through GitHub's security advisory workflow
when enabled, or contact the maintainer without posting exploit data or secrets
publicly. Ordinary bug reports may use GitHub issues with sanitized evidence.
