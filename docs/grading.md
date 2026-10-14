# Verify code in isolation

The collector never executes model output. Review an answer first, then place
its implementation in `candidate.py` and its proposed tests in `model_tests.py`
inside a new ignored local-data grading directory. Preserve the original code;
do not repair it before recording the initial result. Copy
`benchmarks/checks/router_v1.py` into that directory as `behavior_checks.py`.
Only those three regular files are exposed to the optional grading runner.

On Linux, or an existing WSL Ubuntu installation with `bubblewrap` and Python:

```bash
python3 scripts/run_isolated.py \
  --directory local-data/my-run/grading \
  --output local-data/my-run/grading-result.json
```

From Windows, use the corresponding Linux paths, for example:

```powershell
wsl -d Ubuntu --exec python3 /mnt/e/llm/local-coding-lab/scripts/run_isolated.py --directory /mnt/e/llm/local-coding-lab/local-data/my-run/grading --output /mnt/e/llm/local-coding-lab/local-data/my-run/grading-result.json
```

The runner does not install WSL or packages and has **no Windows-host fallback**.
It refuses an existing output. Its preflight checks namespace separation,
absence of host home/mount directories, the three-file input inventory and the
cleared environment. A failed preflight saves evidence and executes no test
file. The process namespace is isolated; the host network namespace is not
shared. Only the system runtime and selected source files are bound read-only.
The candidate cannot see the rest of your checkout, Windows drives or home.

Each process has a 20-second wall limit, 10-second CPU limit, 512 MiB address
space, capped descriptors/processes and 1 MiB per captured output file. Review
the saved return codes and unittest output; a generated test can fail while
the separately checked implementation passes. Do not call such a failure a
model syntax error. The runner returns nonzero on either failed grading pass.

This is a restricted environment for reviewed simple Python answers, not a
guarantee against actively hostile native code or a kernel exploit. Use a
disposable VM for that threat model. Do not mount credentials or run unknown
answers on the normal workstation to work around unavailable isolation.

The six contract groups correspond to the existing 12 behavior points. The
checks were added after the first answers were collected; they are not held out.
Score instruction discovery, grounding, absent facts, test quality and actual
reads separately using the rubric. Do not award behavior points for syntax alone.
