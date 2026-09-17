# OpenRouter setup for AMI GitHub intelligence

**Status:** bootstrap configuration

The GitHub-native AI reviewer and Growth Scout expect one repository secret:

`OPENROUTER_API_KEY`

Add it in the `kajobert/AMI` repository under:

`Settings -> Secrets and variables -> Actions -> New repository secret`

Do not commit the key to a file, issue, pull request, workflow input or repository variable. Repository **secrets** are the intended storage location; ordinary Actions variables are not secret storage.

No custom GitHub token is required for the bootstrap workflows. GitHub supplies the scoped `GITHUB_TOKEN` automatically. The workflows request only the permissions they need.

## Current model

The bootstrap workflows currently request:

`openai/gpt-5.6-luna`

The model is an implementation choice, not AMI identity, and can be changed through a reviewed workflow change.

## Security model

- PR diff content is treated as untrusted data.
- The AI reviewer executes trusted code from the default branch and never checks out PR code with the OpenRouter secret.
- The Growth Scout runs trusted default-branch code and may only create a proposal issue or return `NO_ACTION`.
- Neither workflow can merge, deploy or access production OpenClaw credentials.

## First activation test

After the secret is configured and GitHub-hosted runners are available:

1. merge the bootstrap workflow only after deterministic CI has actually executed;
2. manually dispatch `AMI Growth Loop` once;
3. verify that the result is either `NO_ACTION` or exactly one proposal issue;
4. open a small documentation PR and verify that `AMI AI Review` posts a review comment;
5. confirm no secret value appears in logs or comments.
