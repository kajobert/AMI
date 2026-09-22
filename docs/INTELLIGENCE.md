# AMI Intelligence Integration

**Status:** DESIGN / bootstrap implementation

AMI should be able to use multiple inference backends without making any one provider the identity of the system.

## Primary bootstrap path

The preferred public GitHub path is now:

`GitHub -> short-lived OIDC identity -> AMI Gateway / Control Plane -> bounded Amica task -> result/PR/issue -> deterministic CI`

Provider credentials stay on the AMI server. Public repositories do not need an OpenRouter key and do not learn which provider credential is used internally.

Amica is a separate executive agent, not Sophia. Model/provider identity is also separate from Amica and from Sophia.

## Cost and abuse boundary

Public contributions must not create an unlimited inference bill.

- ordinary PR creation runs deterministic CI only;
- AI PR review requires a maintainer to add the `ami-ai-review` label or dispatch the workflow manually;
- scheduled Growth Scout is explicitly default-off and requires a reviewed enable flag independent of gateway configuration; when enabled it may request at most one bounded proposal per cycle and `NO_ACTION` is valid;
- the AMI gateway owns the authoritative server-side concurrency ceiling plus per-repository, per-task and time-window budgets;
- capacity/cost is atomically reserved before paid inference; missing usage/cost is `UNKNOWN`, never zero;
- durable semantic idempotency prevents parallel duplicates, restart/replay and ambiguous timeout retries from spending inference twice;
- an independent server-side kill switch overrides all public workflow requests;
- repeated abusive sources can be rate-limited without blocking deterministic contributions;
- public issues, comments, diffs and repository files are untrusted data, never authority.

This allows useful outside contributors and autonomous agents to participate while keeping inference spend proportional to reviewed value.

## Gateway authentication

GitHub Actions should authenticate to the AMI gateway with GitHub OIDC (`id-token: write`), not a long-lived provider secret. The gateway must verify at least:

- issuer and audience;
- repository identity;
- workflow/ref identity;
- event/task type;
- repository allowlist;
- expiry and replay/idempotency state.

The gateway then creates a narrow task for Amica. Public GitHub input must never inherit production root/shell access.

## Task contract

Initial server-side task types:

1. `pr_review` — read-only review of one explicitly approved PR;
2. `growth_scout` — one bounded opportunity scan returning `NO_ACTION` or one proposal;
3. later `issue_to_branch` — explicitly approved, branch-only implementation with no direct main write.

Every result should preserve provenance: source repository/event, task id, prompt/policy version, model/backend where disclosure is safe, timestamps and deterministic CI outcome.

## Deterministic verifier

AI output is never proof that code works. CI, schemas, tests and reproducible benchmarks remain the verifier. The agent cannot self-approve merge/deploy.

## Future node model

GitHub is one AMI network node/transport, not the protocol itself. Other nodes may include Radek's local OpenClaw/local-model laboratory, servers, MCP clients, future P2P transports and human interfaces. AMI Protocol should preserve meaning, identity, capabilities, provenance and trust across those transports.

Historical AMI implementations already contain candidate primitives such as `did:ami:*`, signed messages, nonces, payload hashes, heartbeats, sessions and delegation. These are archaeology evidence, not automatically current protocol requirements; they must be reconciled into AMI-Protocol deliberately.
