# Amica growth pilot: acceptance gates

Status: REVIEW REQUIRED. This is a review of the operator-supplied implementation report, not a source-code audit or authorization to expose a service.

## Evidence available on 2026-09-17

The operator's report identifies commits `df6e217a39a` and `109c98b95d6`, reports 102 passing tests and one live NO_ACTION response, and reports that the execution service was restarted while the public task endpoint remained disabled. The implementation source and test logs have not yet been independently inspected here.

A live Control Plane read confirmed a healthy Gateway and an idle `github-growth-scout` session under agent `main`. Session metadata corroborates that a session exists; it does not prove tool isolation, output correctness or a running scheduler. The currently exposed ChatGPT MCP surface still only advertises execution of the probe and inventory jobs.

An execution-service restart is a production change even if the public ingress remains off.

## Required before an unattended pilot

1. **Separate execution context.** Preserve Amica's identity but isolate public input from the main workspace, bootstrap context, private memory, history, hooks and plugins. Verify the effective meaning of an empty tools allowlist in the installed runtime rather than assuming that it means no tools. A read-only or incognito label alone is insufficient evidence.
2. **Route-specific RPC boundary.** The reported scout path adds sessions.create, agent.wait, chat.history and sessions.usage. Keep the existing cron.run boundary intact for existing routes. Generate session identifiers and RPC parameters server-side and bind history/usage reads to the scout's own session. Reject references to main or another task's session.
3. **Default-off at both boundaries.** The public workflow now requires exact `AMI_GROWTH_INGRESS_ENABLED == 'true'`; `AMI_GATEWAY_URL` alone never enables inference. Missing/false/malformed gate or missing/invalid `AMI_GROWTH_POLICY_VERSION` produces no inference request. The independent server-side growth execution gate must also default off.
4. **Authentication is not authorization.** Verify JWT signature, fixed issuer/JWKS, allowed algorithms, audience, exp/nbf and replay state. Bind repository_id, repository_owner_id, workflow/ref and event to an explicit policy. Do not authorize from request-body requested_by. Maintainer approval must be checked independently and tied to the immutable input revision.
5. **Correct OIDC subject handling.** Current GitHub documentation describes immutable subjects containing owner/repository IDs for newly created repositories and some renamed/transferred repositories. Do not hardcode the legacy name-only sub format. Validate actual signed claims against reviewed policy; never loosen signature checks to make a fixture pass.
6. **Bounded cost and concurrency.** The server, not GitHub Actions, owns the authoritative concurrency ceiling and global/per-repository budget. Atomically reserve capacity/cost before paid inference so parallel callers cannot oversubscribe shared budget. Missing usage/cost is `UNKNOWN`, never zero, and must block unsafe continuation. The public workflow uses no blind HTTP retries for ambiguous paid calls.
7. **Durable idempotency.** The public request carries repository ID, task kind, immutable input SHA and policy version so the server can derive the semantic key; the server must add a request-content hash and persist the decision durably. Concurrent duplicates converge on one accepted execution/result; changed content with the same key is rejected. Restart, replay, concurrent requests and ambiguous response timeouts must not create duplicate paid work. JWT jti deduplication alone is not semantic task idempotency.
8. **Host validation and privacy.** Validate structured model output and evidence references. Treat all repository text and model output as untrusted. Do not execute proposed commands or expose private context in logs, public comments or artifacts. Log safe metadata and artifact hashes, not credentials or raw transcripts.
9. **Negative tests.** Before enabling the gate, server-side tests must explicitly cover: gate absent, gate false, malformed gate value, concurrent duplicate requests, budget exhausted, independent kill switch active, unknown cost/usage, retry after timeout, effective tool denial, private-context canaries, cross-session access, wrong workflow/ref, expired token, restart and malformed output. Use synthetic canaries and test-only JWT keys; production must not accept a test issuer or verification bypass.
10. **Auditable local result first.** An approved public snapshot and immutable commit SHA may produce one locally saved proposal/NO_ACTION report. No GitHub write, payment, merge or deploy is needed for this test. Review one real bounded inference result before enabling any timer.

## Safe rollout sequence

`source review -> mocked adversarial tests -> one isolated live run -> reviewed report -> capped local pilot -> public OIDC ingress -> optional issue/PR publishing`

Prepare, but do not activate, the reviewed `AMI_GROWTH_INGRESS_ENABLED` gate until the pilot has an explicit expiry, maximum runs, spend cap, independent server-side kill switch, server-side concurrency limit and named owner. Do not register the production host as a runner for public pull-request code. Existing periodic jobs must not gain permissions or change cadence as a side effect of adding an agent.

## Independent contributors

An outside issue or pull request does not authorize paid inference. A successful CI run demonstrates only the tested properties, not usefulness or safety of arbitrary instructions. Financial support and SALT recognition confer no execution, approval or merge authority.

## Source handoff

Preserve the existing bundle privately. Provide a sanitized source diff, lockfile changes and test evidence for independent review. Never upload the entire historic monorepo bundle into a public module merely to move the work between agents.

## References

- GitHub OIDC claims and immutable subject formats: https://docs.github.com/en/actions/reference/security/oidc
- GitHub secure workflow use: https://docs.github.com/en/actions/reference/security/secure-use
- OpenClaw sandboxing background: https://docs.openclaw.ai/gateway/sandboxing

Online runtime documentation can differ from the installed build. The implementation must verify version-specific behavior against the code actually deployed.


## Current public-workflow safety state

The scheduled workflow may exist in source while remaining operationally inert. The exact opt-in variable is independent of gateway configuration and defaults off when absent. This repository does **not** contain the production gateway implementation, so the server-side concurrency limit, atomic reservation, durable idempotency, kill switch and cost-accounting negative tests cannot be honestly claimed from this PR alone. Until those server-side properties are independently evidenced, the reviewed growth enable gate must remain off.

The public workflow adds only a bounded request envelope: repository identity, immutable input SHA and policy version. These values support server-side deduplication but do not grant authority. A caller cannot raise the server concurrency ceiling, reserve extra budget, disable the kill switch, request shell access, merge, deploy, or opt into private Amica/Sophia context.
