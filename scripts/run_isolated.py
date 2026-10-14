"""Run reviewed Python files in Linux bubblewrap, never on the Windows host.

Requires an existing bubblewrap installation and enabled user namespaces.
Use a disposable VM for actively hostile code; this is not a kernel boundary.
"""
import argparse
import json
import os
from pathlib import Path
import shutil
import signal
import subprocess
import sys
import tempfile


def limits() -> None:
    """Bound resources before launching the namespace helper."""
    import resource
    resource.setrlimit(resource.RLIMIT_CPU, (10, 10))
    resource.setrlimit(resource.RLIMIT_AS, (512 * 1024**2, 512 * 1024**2))
    resource.setrlimit(resource.RLIMIT_FSIZE, (1024**2, 1024**2))
    resource.setrlimit(resource.RLIMIT_NOFILE, (64, 64))
    resource.setrlimit(resource.RLIMIT_NPROC, (64, 64))
    resource.setrlimit(resource.RLIMIT_CORE, (0, 0))


def base_command(files: list[Path]) -> list[str]:
    """Expose only Linux runtime files and explicitly selected Python sources."""
    command = [shutil.which('bwrap'), '--unshare-all', '--die-with-parent',
               '--new-session', '--cap-drop', 'ALL', '--clearenv',
               '--setenv', 'PATH', '/usr/bin', '--setenv', 'HOME', '/tmp',
               '--ro-bind', '/usr', '/usr', '--symlink', 'usr/bin', '/bin',
               '--symlink', 'usr/lib', '/lib', '--dir', '/etc',
               '--proc', '/proc', '--dev', '/dev', '--tmpfs', '/tmp',
               '--dir', '/work', '--chdir', '/work']
    if Path('/usr/lib64').exists():
        command += ['--symlink', 'usr/lib64', '/lib64']
    if Path('/etc/ld.so.cache').exists():
        command += ['--ro-bind', '/etc/ld.so.cache', '/etc/ld.so.cache']
    for path in files:
        command += ['--ro-bind', str(path), '/work/' + path.name]
    return command


def bounded(command: list[str]) -> dict:
    """Collect at most a bounded process lifetime, terminating the process group."""
    with tempfile.TemporaryFile() as stdout, tempfile.TemporaryFile() as stderr:
        child = subprocess.Popen(command, stdout=stdout, stderr=stderr,
                                 start_new_session=True, preexec_fn=limits)
        try:
            child.wait(timeout=20)
            status = 'exited'
        except subprocess.TimeoutExpired:
            os.killpg(child.pid, signal.SIGKILL)
            child.wait(timeout=5)
            status = 'timeout'
        stdout.seek(0)
        stderr.seek(0)
        out = stdout.read(1024**2).decode('utf-8', errors='replace')
        err = stderr.read(1024**2).decode('utf-8', errors='replace')
    return {'status': status, 'returncode': child.returncode,
            'stdout': out, 'stderr': err}


def main() -> int:
    """Verify the isolation boundary before executing selected reviewed files."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--directory', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    if sys.platform != 'linux' or not shutil.which('bwrap'):
        parser.error('Requires Linux/WSL with bubblewrap; no host fallback')
    directory = args.directory.resolve()
    names = ['candidate.py', 'behavior_checks.py', 'model_tests.py']
    files = [directory / name for name in names]
    if any(not p.is_file() or p.is_symlink() or p.stat().st_size > 100000
           for p in files):
        parser.error('Expected three regular Python files, each under 100 KB')
    if args.output.exists():
        parser.error('Output exists; preserve previous grading evidence')
    outside_net = os.readlink('/proc/self/ns/net')
    probe = (
        "import json,os,pathlib; "
        "assert not pathlib.Path('/home').exists(); "
        "assert not pathlib.Path('/mnt').exists(); "
        "assert not pathlib.Path('/root').exists(); "
        f"assert os.readlink('/proc/self/ns/net') != {outside_net!r}; "
        "print(json.dumps({'environment_keys': sorted(os.environ)})); "
        "assert set(os.environ) <= {'HOME','PATH','LC_CTYPE','PWD'}; "
        "assert os.environ['PWD'] == '/work'; "
        "assert set(p.name for p in pathlib.Path('/work').iterdir()) == "
        "{'candidate.py','behavior_checks.py','model_tests.py'}; "
        "print(json.dumps({'isolated_network': True, 'no_host_homes': True, "
        "'python': os.sys.version.split()[0]}))"
    )
    base = base_command(files)
    record = {'probe': bounded(base + ['/usr/bin/python3', '-B', '-c', probe]),
              'limits': {'wall_seconds_per_process': 20, 'cpu_seconds': 10,
                         'address_space_mib': 512}, 'runs': {}}
    if record['probe']['returncode'] == 0:
        for name in ['behavior_checks.py', 'model_tests.py']:
            record['runs'][name] = bounded(
                base + ['/usr/bin/python3', '-B', '/work/' + name])
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(record, indent=2), encoding='utf-8')
    print(json.dumps(record, indent=2))
    return 0 if (record['probe']['returncode'] == 0 and all(
        run['returncode'] == 0 for run in record['runs'].values())) else 1


if __name__ == '__main__':
    sys.exit(main())
