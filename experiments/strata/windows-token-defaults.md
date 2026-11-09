# Windows frontend token-default ACL correction

9 November 2026. This is a separately identified frontend experiment, not an
engine change or a completed quality comparison. The original checkout and
engine remain intact.

The pinned frontend at `4b9e05a2a806a3fe24f7b2560d98626c37dade35`
calls `private_files.adopt_user_defaults()` before creating its engine. That
function applies `FA` (file-all access) to the process token's default ACL.
The default also applies to newly created process objects. File access bits
omit `PROCESS_QUERY_INFORMATION`, which the independent working-set monitor
requests alongside `PROCESS_SET_QUOTA`.

Two static Q2 serving attempts consequently stopped with Windows error 5 at
`OpenProcess`, before sending any question. A direct guarded engine load
reached `READY32768` in a 9.390-second load-and-exit diagnostic. It did not run
inference. The differing parent setup was the clue; this was not a measured
out-of-memory failure.

## Isolated correction and evidence

The [patch](windows-token-defaults.patch) changes the token default's access
type from file-all to generic-all. Windows maps generic rights to the object
being created. The user, SYSTEM and administrators are still the only
trustees. File-specific protection methods are unchanged. The lab's resource
floors, working-set enforcement and owned-process cleanup remain unchanged.

Harmless owned-child controls reproduce the failure and recovery:

| Parent token defaults | Set/read back a 128 MiB working-set cap | Result |
|---|---|---|
| Ordinary Windows defaults | Maximum 134217728 bytes, flags 6 | Pass |
| Original Strata file-all default | `OpenProcess` returns error 5 | Reproduced |
| Corrected generic-all default | Maximum 134217728 bytes, flags 6 | Pass |

The isolated checkout's original `tests/terminal/test_private_files.py` ran
13 cases in 0.270 seconds: 12 Windows cases passed, one POSIX-only case skipped.
These include private directories/files, detecting widened ACLs, access
repair scope and repeated default adoption. No Linux/macOS run or GUI test is
claimed. Subsequent model serving outcomes belong in the Flash model report;
these controls alone establish neither inference quality nor performance.

Apply only to the exact source revision in a separate checkout, after
`git apply --check`. Use the existing pinned Python environment and native
engine; point the frontend working directory at that checkout. Record the
diff and updated source hashes with each new plan. Never bypass the external
guard to get past this error.

Primary references: [Windows process access rights](https://learn.microsoft.com/en-us/windows/win32/procthread/process-security-and-access-rights),
[SDDL access types](https://learn.microsoft.com/en-us/windows/win32/secauthz/ace-strings),
and [working-set query rights](https://learn.microsoft.com/en-us/windows/win32/api/memoryapi/nf-memoryapi-getprocessworkingsetsizeex).
Private evidence: `local-data/2026-11-09-merge/token-acl-controls/results.json`,
the two failed static serving receipts, and the isolated frontend prelaunch
receipt. No broad machine permission change or administrator elevation was used.
