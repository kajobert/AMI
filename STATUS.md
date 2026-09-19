# AMI Project Status

**Last verified:** 2026-09-19  
**Purpose:** public, auditable snapshot of what exists now versus what is planned.

> **Trust instead of Authority.**

This page is intentionally conservative. A feature is listed as implemented only when there is a repository, commit, pull request, test result, or live control-plane observation supporting it.

## Public ecosystem

| Repository | Visibility | License | Current role |
|---|---|---|---|
| `kajobert/AMI` | Public | Apache-2.0 | Umbrella, ecosystem map, contribution entry point |
| `kajobert/AMI-Protocol` | Public | Apache-2.0 | Interoperability / node communication design |
| `kajobert/AMI-Kernel` | Public | Apache-2.0 | Future orchestration/runtime layer |
| `kajobert/AMI-Knowledge-Core` | Public | Apache-2.0 | Provenance-first knowledge/evidence infrastructure |
| `kajobert/AMI-SALT` | Public | Apache-2.0 | Trust / verification / contribution layer |
| `kajobert/Sophia-AMI` | Public | Apache-2.0 | Future entity layer built on AMI |

Private project coordination, personal/entity memory, raw archaeology evidence, credentials and production data are intentionally outside the public repositories.

## Knowledge Core implementation stack

The current implementation is review-gated and not merged to the default branch yet.

### PR #6 — Knowledge Core vertical slice

- branch: `cursor/knowledge-core-vertical-slice-a2d9`
- commit: `23b340e5aa87cc78df6a2b6fafaa68c574b0d14e`
- state: open draft
- contains: PostgreSQL schema, deterministic/idempotent ingest, provenance validation, read API, Encyclopedia v0, synthetic fixtures, tests.

### PR #7 — Encyclopedia UI v1

- branch: `cursor/encyclopedia-ui-v1-a2d9`
- commit: `5acc9d80a7a21c08a36fc9977008a8ccb5e80186`
- state: open draft, stacked on PR #6
- contains: global search, lazy graph, Inspector, Evidence/Reality Matrix, read-model endpoints.

### PR #9 — Continuous archaeology worker v0.1

- branch: `cursor/archaeology-worker-v01-a2d9`
- commit: `35c1659c82e33737e314789eb048ebb60120461d`
- state: open draft, stacked on PR #7
- contains: per-source queue, processing fingerprints, extraction/synthesis contracts, read-only Amica adapter, worker status API/UI, tests.

Cursor reported local validation for the PR #9 stack:

- `ruff`: pass
- `mypy`: pass
- `pytest`: 25 passed, 1 skipped

These are developer-reported local results. GitHub Actions currently fail before normal steps execute, so CI is **not yet independent confirmation**.

## CI status

Current GitHub Actions runs for the Knowledge Core stack fail at the platform/workflow startup layer with jobs completing before normal test steps.

Status:
- application test failure: **not demonstrated**
- GitHub CI health: **BLOCKED**
- local deterministic test results: **reported passing**

CI must be repaired before the stack is considered merge-ready.

## Live Control Plane

Last verified through the AMI Control Plane:

- health: **healthy**
- reported runtime version: `2026.9.4`
- controlled growth loop: **enabled**
- recent growth runs: producing bounded proposals / no-action decisions
- archaeology inventory mode: `metadata_inventory_partial`
- archaeology registered item count: 16

The live growth loop currently proposes changes; it is not an unrestricted autonomous merge/deploy system.

## Archaeology

Current state:

- Drive discovery has identified historical AMI/Sophia/SALT/VGL/router/memory material.
- Seven NotebookLM notebooks have derived inventory exports registered for archaeology.
- Google Takeout for Gemini/My Activity is ready; large raw archives remain outside public Git.
- Perplexity export is ready for acquisition.
- OpenAI/ChatGPT export was still pending at the last verified check.
- Continuous archaeology worker code exists in draft PR #9.
- Real private source ingestion into a deployed Knowledge Core instance has **not yet been completed**.

## Encyclopedia

A local Encyclopedia implementation exists in the PR stack.

Implemented in code:
- Search
- source/claim inspection
- evidence/revision navigation
- lazy graph
- Evidence/Reality Matrix
- worker/ingest status

Verified deployed preview:
- host: private AMI reference node
- loopback service: `http://127.0.0.1:8765`
- private tailnet URL: verified, intentionally not published
- health verified over Tailscale with HTTP 200
- preview uses sanitized fixtures only; no private archaeology bodies are published.

Target deployment boundary:

```text
operator browser
  -> private overlay network
  -> AMI node
  -> loopback-bound Knowledge Core / Encyclopedia
```

No public evidence endpoint is intended.

## Amica

Current verified direction:

- Amica is the current executive/technical agent.
- Knowledge Core access is designed through a bounded read-only adapter, not direct SQL.
- continuous archaeology is intended to become Amica-owned recurring work.
- automatic canonical promotion remains prohibited.
- production capability expansion remains review-gated.

## AMI network direction

The public infrastructure goal is not a single central server.

The intended direction is:

- anyone can run an AMI-compatible node;
- human and AI participants can contribute ideas, evidence, verification, implementation and review;
- trust should follow evidence and contribution history rather than origin or central authority;
- private entity memories/data remain local or operator-controlled;
- AMI Protocol carries interoperable envelopes;
- SALT provides the trust/verification/contribution layer.

The exact governance, economics and protocol-level participation rules are still under design and must not be presented as finished implementation.

## Next technical milestones

1. Repair/replace broken GitHub CI startup path.
2. Review the stacked Knowledge Core PRs #6 -> #7 -> #9.
3. ~~Deploy a private Knowledge Core / Encyclopedia preview on the AMI node.~~ **DONE**
4. Ingest the first real archaeology batch privately.
5. Connect Amica to the read-only Knowledge Core adapter.
6. Run the first bounded Amica archaeology extraction/synthesis cycle.
7. Add recurring host-owned scheduling only after the manual vertical slice is verified.
8. Expand AMI Protocol from design into interoperable node/contribution/trust envelopes.

## How to verify progress

Do not rely on chat summaries alone.

Verify through:
- public repository commit history;
- open PRs and diffs;
- deterministic test output;
- Control Plane health/status;
- later, the private Encyclopedia/Observatory UI.

If a claim is not visible through one of those channels, treat it as planned or unverified.
