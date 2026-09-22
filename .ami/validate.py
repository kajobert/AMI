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
    "docs/AMICA_GROWTH_ACCEPTANCE.md",
    ".github/workflows/growth-loop.yml",
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

# Growth ingress contract: deterministic regression guard for the public workflow.
growth_path = ROOT / ".github/workflows/growth-loop.yml"
growth = growth_path.read_text(encoding="utf-8") if growth_path.is_file() else ""
growth_requirements = {
    "explicit default-off gate": "AMI_GROWTH_INGRESS_ENABLED",
    "exact opt-in comparison": '[ "$AMI_GROWTH_INGRESS_ENABLED" != "true" ]',
    "policy version gate": "AMI_GROWTH_POLICY_VERSION",
    "repository identity": '"repository_id": os.environ["REPOSITORY_ID"]',
    "immutable input SHA": '"input_sha": os.environ["INPUT_SHA"]',
    "policy version in request": '"policy_version": os.environ["POLICY_VERSION"]',
    "GitHub concurrency boundary": "concurrency:",
    "no blind HTTP retry": "--retry 0",
}
for label, needle in growth_requirements.items():
    if needle not in growth:
        errors.append(f"growth workflow missing {label}")

if "steps.gateway.outputs.enabled" in growth:
    errors.append("growth workflow must not use gateway presence as the enable gate")

if growth.count("--retry 0") < 2:
    errors.append("growth workflow must disable blind retries for OIDC and task submission")

if errors:
    print("AMI repository contract: FAIL")
    for error in errors:
        print(f"- {error}")
    sys.exit(1)

print("AMI repository contract: PASS")
print(f"checked_required_files={len(REQUIRED)}")
print("public_secret_scan=PASS")
print("growth_ingress_contract=PASS")
print("motto=Trust instead of Authority")
