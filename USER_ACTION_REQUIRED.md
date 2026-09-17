# User action required

**Status:** CURRENT diagnostic checklist

The GitHub connector can edit code, branches, pull requests and issues, but it cannot read or change all repository/account-level Actions administration settings. The current public AMI workflows are parsed correctly, jobs are created, but GitHub-hosted runners are not provisioned and no workflow step starts.

Before treating this as a repository bug, the repository owner should verify the following in each new public AMI repository (`AMI`, `AMI-Knowledge-Core`, `AMI-Kernel`, `AMI-Protocol`, `Sophia-AMI`):

1. Open **Settings -> Actions -> General**.
2. Under **Actions permissions**, confirm GitHub Actions is enabled. `Allow all actions and reusable workflows` is the simplest diagnostic setting while the runner problem is being isolated.
3. Under **Workflow permissions**, `Read repository contents and packages permissions` is sufficient for the deterministic CI workflows currently in use. The workflow files grant any narrower permissions they need explicitly.
4. Do **not** enable broad write permissions or automatic PR approval just to fix runner startup.
5. No OpenRouter secret is required. AI workflows are designed for `GitHub OIDC -> AMI Gateway/Control Plane -> Amica` and request `id-token: write` explicitly.
6. Public standard GitHub-hosted runners should not consume private Actions minutes; do not add a production self-hosted runner as a workaround.

If the settings above are already correct and a minimal `runs-on: ubuntu-latest` job still creates a job with no runner/steps/logs, preserve the run/job IDs and treat it as an account/platform runner-provisioning problem for GitHub Support.

## Security rule

Do not connect `sophia-core` as a generic public self-hosted GitHub runner. Public repository content is untrusted input and must reach Amica only through a narrow authenticated task contract and explicit policy/budget gates.
