from __future__ import annotations

from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]

REQUIRED = [
    "README.md",
    "VISION.md",
    "ARCHITECTURE.md",
    "ROADMAP.md",
    "SECURITY.md",
    "CONTRIBUTING.md",
    "REPOSITORY_STANDARD.md",
    "MODULES.md",
    "LICENSE",
    "docs/NAMING.md",
    "docs/SALT.md",
    "docs/LICENSING.md",
    "docs/INTELLIGENCE.md",
    ".ami/modules.yaml",
]

SECRET_PATTERNS = {
    "OpenRouter/API-style key": re.compile(r"sk-or-v1-[A-Za-z0-9_-]{20,}"),
    "GitHub token": re.compile(r"gh[pousr]_[A-Za-z0-9]{20,}"),
    "private key": re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
}

errors: list[str] = []

for relative in REQUIRED:
    if not (ROOT / relative).is_file():
        errors.append(f"missing required file: {relative}")

readme = (ROOT / "README.md").read_text(encoding="utf-8") if (ROOT / "README.md").is_file() else ""
if "Trust instead of Authority" not in readme:
    errors.append("README.md must contain the project motto: Trust instead of Authority")

registry_path = ROOT / ".ami/modules.yaml"
registry = registry_path.read_text(encoding="utf-8") if registry_path.is_file() else ""
for expected in ("kajobert/AMI", "kajobert/ami-knowledge-core", "kajobert/AMI-Kernel", "kajobert/AMI-Protocol", "kajobert/Sophia-AMI"):
    if expected not in registry:
        errors.append(f"module registry missing repository: {expected}")

for path in ROOT.rglob("*"):
    if not path.is_file() or ".git" in path.parts:
        continue
    try:
        if path.stat().st_size > 1_000_000:
            continue
        text = path.read_text(encoding="utf-8")
    except (UnicodeDecodeError, OSError):
        continue
    for label, pattern in SECRET_PATTERNS.items():
        if pattern.search(text):
            errors.append(f"possible committed secret ({label}) in {path.relative_to(ROOT)}")

if errors:
    print("AMI repository contract: FAIL")
    for error in errors:
        print(f"- {error}")
    sys.exit(1)

print("AMI repository contract: PASS")
print(f"checked_required_files={len(REQUIRED)}")
print("public_secret_scan=PASS")
print("motto=Trust instead of Authority")
