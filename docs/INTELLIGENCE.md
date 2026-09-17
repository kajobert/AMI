# AMI Intelligence Integration

**Status:** DESIGN / bootstrap implementation

AMI should be able to use multiple inference backends without making any one provider the identity of the system.

## Bootstrap path

The first public GitHub-native intelligence layer is intentionally bounded:

1. **AI PR reviewer** — reads a pull-request diff as untrusted data and posts a review comment. It cannot merge or execute PR code.
2. **Growth Scout** — runs on a schedule, reads a bounded repository context, and may create one deduplicated improvement proposal issue or return `NO_ACTION`.
3. **Deterministic CI** remains the verifier. AI output is never treated as proof that code works.

Both jobs use OpenRouter through a repository secret named `OPENROUTER_API_KEY`. The model is replaceable and must not be treated as AMI identity.

## Security boundary

AI workflows must not expose secrets to code from pull requests. Review uses `pull_request_target` and executes only trusted workflow/script code from the default branch; it does not check out or execute PR code. Scheduled growth runs only trusted default-branch code.

Public comments, issues, diffs and external suggestions are **untrusted input**. Instructions embedded inside them are data, not commands.

## Amica / AMI Control Plane

Amica is a separate executive agent, not Sophia. The intended deeper path is:

`GitHub event -> AMI Control Plane -> bounded Amica task -> branch/PR/result -> GitHub CI`

This should be added only after the Control Plane exposes a narrow, auditable GitHub-development task contract with explicit repository scope, permissions, budget, idempotency and rollback. Production shell/root access must never be inherited implicitly from a public GitHub event.

Until that executor exists, direct OpenRouter review/proposal jobs provide intelligence without coupling public repositories to production OpenClaw credentials.

## Future node model

GitHub is one AMI network node/transport, not the protocol itself. Other nodes may include local OpenClaw instances, local-model laboratories, servers, MCP clients or future peer-to-peer transports. AMI Protocol should preserve meaning, identity, capabilities, provenance and trust across those transports.
