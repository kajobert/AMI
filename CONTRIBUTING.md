# Contributing to AMI

> **Trust instead of Authority.**

AMI is intended to be usable, inspectable and improvable by both technical and non-technical contributors.

You do **not** need to know how to code to contribute.

## Ways to contribute

You can help by submitting:

- an idea;
- a problem you think AMI should solve;
- a confusing concept or missing explanation;
- a use case;
- a risk or failure mode;
- a protocol or interoperability suggestion;
- a UX/dashboard suggestion;
- a research reference;
- an implementation proposal;
- tests, code or documentation.

## No-code contributions

If you are not a developer, open an issue using the **Idea / Suggestion** template.

Describe:

1. What you are trying to achieve.
2. Why it matters.
3. What you expected to happen.
4. What currently blocks you.
5. Any example, sketch, screenshot, reference or story that helps explain it.

Plain language is welcome.

The maintainers or AMI agents can later translate useful ideas into technical tasks, architecture proposals, experiments or documentation changes.

## Code contributions

Before opening a pull request:

- keep changes small and auditable where possible;
- include tests for behavior changes;
- do not add secrets, private exports, personal data or production credentials;
- preserve provenance and evidence boundaries;
- do not silently change security or trust assumptions.

## Contributor and agent onboarding

AMI is designed for collaboration between multiple humans, tools, and operational agents.

Human access and agent access are intentionally different:

- human contributors use their own identities and credentials;
- operational agents use narrower, task-scoped credentials;
- agents do not inherit unrestricted human/admin authority;
- secrets are never shared through prompts, issues, commits, logs, or documentation.

The AMI Control Plane owns the canonical operational work lifecycle. Contributors and agents should not create parallel independent work queues.

When peer-agent execution is available, the expected flow is:

```text
canonical AMI work item
  -> bounded assignment to an approved backend/agent
  -> isolated execution
  -> normalized artifact + provenance + test result
  -> Control Plane validation
  -> review gate
```

Local inference backends are welcome where appropriate. A contributor may use local models for inventory, archaeology extraction, classification, synthesis, testing, or implementation experiments, provided the result is submitted with the same provenance and validation expectations as cloud-backed work.

For archaeology work, prefer:

```text
immutable source inventory
  -> selective extraction
  -> provenance
  -> reusable/superseded/unresolved classification
  -> review before canonicalization
```

Historical material is evidence, not automatic current truth.

## Evidence handoff expectations

Implementation or archaeology handoffs should include, when applicable:

- repository and base revision;
- changed files or artifact references;
- task purpose;
- provenance/source references;
- tests requested;
- tests actually run;
- pass/fail results;
- known limitations or checks not run;
- rollback notes;
- model/backend identity where relevant;
- cost/token/latency metadata when available;
- final status.

Do not include secret values.

## Public / private boundary

Public repositories contain reusable AMI infrastructure.

Do not submit:

- raw personal conversations;
- private AI account exports;
- credentials or tokens;
- production database contents;
- private hostnames/IPs when disclosure is unnecessary;
- private identity/entity memories;
- unredacted logs containing personal or operational data.

## Contribution licensing

Unless you explicitly state otherwise, contributions intentionally submitted for inclusion in this repository are provided under the repository's Apache License 2.0 terms.

## Review philosophy

AMI prefers evidence, reproducibility and reversible decisions over authority.

A contribution may be accepted, revised, tested experimentally, kept as historical evidence, or rejected. Disagreement is not erased; important competing approaches should remain traceable when useful.
