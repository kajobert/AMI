# Amica growth pilot: acceptance gates

Status: REVIEW REQUIRED. This is a review of the operator-supplied implementation report, not a source-code audit or authorization to expose a service.

## Evidence available on 2026-09-17

The operator's report identifies commits `df6e217a39a` and `109c98b95d6`, reports 102 passing tests and one live NO_ACTION response, and reports that the execution service was restarted while the public task endpoint remained disabled. The implementation source and test logs have not yet been independently inspected here.

A live Control Plane read confirmed a healthy Gateway and an idle `github-growth-scout` session under agent `main`. Session metadata corroborates that a session exists; it does not prove tool isolation, output correctness or a running scheduler. The currently exposed ChatGPT MCP surface still only advertises execution of the probe and inventory jobs.

An execution-service restart is a production change even if the public ingress remains off.

## Required before an unattended pilot

1. **Separate execution context.** Preserve Amica's identity but isolate public input from the main workspace, bootstrap context, private memory, history, hooks and plugins. Verify the effective meaning of an empty tools allowlist in the installed runtime rather than assuming that it means no tools. A read-only or incognito label alone is insufficient evidence.
2. **Route-specific RPC boundary.** The reported scout path adds sessions.create, agent.wait, chat.history and sessions.usage. Keep the existing cron.run boundary intact for existing routes. Generate session identifiers and RPC parameters server-side and bind history/usage reads to the scout's own session. Reject references to main or another task's session.
3. **Default-off at both boundaries.** The GitHub ingress feature flag and growth execution feature flag must default to false. Verify disabled behavior independently in the Control Plane and execution worker.
4. **Authentication is not authorization.** Verify JWT signature, fixed issuer/JWKS, allowed algorithms, audience, exp/nbf and replay state. Bind repository_id, repository_owner_id, workflow/ref and event to an explicit policy. Do not authorize from request-body requested_by. Maintainer approval must be checked independently and tied to the immutable input revision.
5. **Correct OIDC subject handling.** Current GitHub documentation describes immutable subjects containing owner/repository IDs for newly created repositories and some renamed/transferred repositories. Do not hardcode the legacy name-only sub format. Validate actual signed claims against reviewed policy; never loosen signature checks to make a fixture pass.
6. **Bounded cost.** Atomically reserve a global and per-repository budget before inference. Limit input size, calls, output tokens, time and concurrency. Missing usage/cost is UNKNOWN, not zero. Disable blind retries of ambiguous paid calls.
7. **Durable idempotency.** Store a semantic task key tied to repository ID, task kind, input SHA and policy version, plus request-content hash. Identical retries reuse the result; changed content with the same key is rejected. Restart, replay, concurrent requests and response timeouts must not create duplicate paid work. JWT jti deduplication alone is not semantic task idempotency.
8. **Host validation and privacy.** Validate structured model output and evidence references. Treat all repository text and model output as untrusted. Do not execute proposed commands or expose private context in logs, public comments or artifacts. Log safe metadata and artifact hashes, not credentials or raw transcripts.
9. **Negative tests.** Test effective tool denial, private-context canaries, cross-session access, wrong workflow/ref, expired token, concurrent requests, restart, timeout, budget exhaustion and malformed output. Use synthetic canaries and test-only JWT keys; production must not accept a test issuer or verification bypass.
10. **Auditable local result first.** An approved public snapshot and immutable commit SHA may produce one locally saved proposal/NO_ACTION report. No GitHub write, payment, merge or deploy is needed for this test. Review one real bounded inference result before enabling any timer.

## Safe rollout sequence

`source review -> mocked adversarial tests -> one isolated live run -> reviewed report -> capped local pilot -> public OIDC ingress -> optional issue/PR publishing`

Prepare, but do not activate, a timer until the pilot has an explicit expiry, maximum runs, spend cap, kill switch and named owner. Do not register the production host as a runner for public pull-request code. Existing periodic jobs must not gain permissions or change cadence as a side effect of adding an agent.

## Independent contributors

An outside issue or pull request does not authorize paid inference. A successful CI run demonstrates only the tested properties, not usefulness or safety of arbitrary instructions. Financial support and SALT recognition confer no execution, approval or merge authority.

## Source handoff

Preserve the existing bundle privately. Provide a sanitized source diff, lockfile changes and test evidence for independent review. Never upload the entire historic monorepo bundle into a public module merely to move the work between agents.

## References

- GitHub OIDC claims and immutable subject formats: https://docs.github.com/en/actions/reference/security/oidc
- GitHub secure workflow use: https://docs.github.com/en/actions/reference/security/secure-use
- OpenClaw sandboxing background: https://docs.openclaw.ai/gateway/sandboxing

Online runtime documentation can differ from the installed build. The implementation must verify version-specific behavior against the code actually deployed.
