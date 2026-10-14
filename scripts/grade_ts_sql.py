"""Grade reviewed TypeScript and SQLite only in Linux/bubblewrap namespaces."""
import argparse
import json
import os
from pathlib import Path
import shutil
import sys

from run_isolated import base_command, bounded


def main() -> int:
    """Refuse missing isolation or an existing report; never run on Windows."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--directory', type=Path, required=True)
    parser.add_argument('--node', type=Path, required=True)
    parser.add_argument('--typescript', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    if sys.platform != 'linux' or not shutil.which('bwrap'):
        parser.error('Linux with bubblewrap required; no Windows fallback')
    if args.output.exists():
        parser.error('Preserve prior grading report')
    files = [args.directory.resolve()/name for name in
             ['candidate.ts', 'migration.sql', 'schema.sql', 'ts_sql_v1.cjs', 'ts_sql_v1.py']]
    if any(not p.is_file() or p.is_symlink() or p.stat().st_size > 100000 for p in files):
        parser.error('Missing, symlinked or oversized grading source')
    node, compiler = args.node.resolve(), args.typescript.resolve()
    if not node.is_file() or not (compiler/'tsc.js').is_file():
        parser.error('Verified Linux Node binary and TypeScript lib directory required')
    base = base_command(files)
    base += ['--ro-bind', str(node), '/node', '--ro-bind', str(compiler), '/typescript']
    outside_net = os.readlink('/proc/self/ns/net')
    inventory = [p.name for p in files]
    probe = (
        'import os,pathlib; '
        "assert not any(pathlib.Path(p).exists() for p in ['/home','/mnt','/root']); "
        f"assert os.readlink('/proc/self/ns/net') != {outside_net!r}; "
        "assert set(os.environ) <= {'PATH','HOME','PWD','LC_CTYPE'}; "
        f"assert sorted(p.name for p in pathlib.Path('/work').iterdir()) == {sorted(inventory)!r}; "
        "print('Separate network/process namespaces; no host homes or drives; input files read-only')")
    record = {'probe': bounded(base+['/usr/bin/python3', '-B', '-c', probe]), 'runs': {}}
    if record['probe']['returncode'] == 0:
        # Node reserves virtual address space beyond its bounded 128 MiB JS heap.
        driver = (
            'import json,subprocess,sys; '
            "node=['/node','--jitless','--max-old-space-size=128','--stack-size=512']; "
            "compile=subprocess.run(node+['/typescript/tsc.js','/work/candidate.ts','--strict',"
            "'--target','ES2020','--module','commonjs','--outDir','/tmp/out'],capture_output=True,text=True); "
            "print(json.dumps({'compile_code':compile.returncode,'stdout':compile.stdout,'stderr':compile.stderr}),flush=True); "
            "sys.exit(compile.returncode) if compile.returncode else None; "
            "sys.exit(subprocess.call(node+['/work/ts_sql_v1.cjs']))")
        record['runs']['typescript'] = bounded(
            base+['/usr/bin/python3', '-B', '-c', driver],
            address_space_mib=8192, cpu_seconds=30, wall_seconds=60)
        record['runs']['sqlite'] = bounded(base+['/usr/bin/python3', '-B', '/work/ts_sql_v1.py'])
    record['limits'] = {'typescript_virtual_address_mib': 8192,
                        'typescript_heap_mib': 128, 'typescript_wall_seconds': 60,
                        'sqlite_address_mib': 512, 'sqlite_wall_seconds': 20}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(record, indent=2), encoding='utf-8')
    print(json.dumps(record, indent=2))
    return 0 if record['probe']['returncode'] == 0 and all(
        run['returncode'] == 0 for run in record['runs'].values()) else 1


if __name__ == '__main__':
    raise SystemExit(main())
