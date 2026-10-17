"""Audit Git-visible files for accidental private data and generated artifacts."""
from pathlib import Path
import hashlib
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]

# These exact widget-only crops were opened and visually reviewed by Codex.
# Do not allow arbitrary images: every new/changed binary requires a new review.
REVIEWED_IMAGES = {
    "reports/assets/desktop-v0.5.0-ready.png":
        "662f3342fd6206e20be3ee55a34ca273f477f19c8cf59193bf2aae7e2c1e2f3c",
    "reports/assets/desktop-v0.5.0-stopped.png":
        "6eb733db058cac44b671f9f79b437a99ed87a742cc107b53d0b7af7e40dbff7f",
    "reports/assets/desktop-v0.5.0-working.png":
        "2d5fe903c794b61713a496f2dd2092126c624fbf96dc0320b65edafb046871d4",
}


def reviewed_image(name: str, content: bytes) -> bool:
    """Accept only an exact path and digest, not a binary file extension."""
    return (name in REVIEWED_IMAGES and
            hashlib.sha256(content).hexdigest() == REVIEWED_IMAGES[name])


def main() -> int:
    """Scan content without printing matched secrets; this is not a DLP guarantee."""
    paths = subprocess.check_output(
        ["git", "ls-files", "--cached", "--others", "--exclude-standard", "-z"],
        cwd=ROOT).decode().split("\0")
    patterns = {
        "API credential": re.compile(r"(?:sk-or-v1-|gh[pousr]_)[A-Za-z0-9_-]{20,}"),
        "private key": re.compile(r"-----BEGIN (?:RSA |OPENSSH |EC )?PRIVATE KEY-----"),
        "personal home path": re.compile(r"[Cc]:[\\/]+Users[\\/]+(?!EXAMPLE\b|example\b)[\w.-]+"),
    }
    failures = []
    count = 0
    for name in sorted(set(paths) - {""}):
        path = ROOT / name
        if not path.is_file():
            continue
        count += 1
        if path.stat().st_size > 1024 * 1024:
            failures.append((name, "file exceeds public 1 MiB limit"))
            continue
        if reviewed_image(name, path.read_bytes()):
            continue
        if path.suffix.lower() in (".gguf", ".exe", ".dll", ".zip", ".part", ".log", ".html"):
            failures.append((name, "generated/binary artifact"))
        try:
            content = path.read_text(encoding="utf-8")
        except UnicodeError:
            failures.append((name, "non-text content"))
            continue
        for label, pattern in patterns.items():
            if pattern.search(content):
                failures.append((name, label))
    for name, reason in failures:
        print(f"FAIL {name}: {reason}")
    print(f"Audited {count} files; {len(failures)} findings. Review still required.")
    return bool(failures)


if __name__ == "__main__":
    sys.exit(main())
