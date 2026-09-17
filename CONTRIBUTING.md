# Contributing to AMI

AMI welcomes useful contributions from humans, AI agents and mixed human/AI workflows.

> **Trust instead of Authority.**

A contribution earns trust through evidence, reproducibility and observed outcomes — not because of who or what submitted it.

## Before a PR

State:

- the problem or capability being addressed;
- expected benefit;
- measurable success criteria;
- risks/failure modes;
- the smallest test or experiment that can validate the change.

## Pull requests

PRs should be focused and auditable. Include tests when applicable, preserve provenance, avoid secrets/private evidence and do not label work `IMPLEMENTED` or `VALIDATED` without evidence.

AI-assisted contributions are welcome. When material, disclose the agent/model/runtime or workflow used so results can be reproduced and compared. AI output is not evidence by itself.

## External humans and agents

Autonomous agents may open issues and PRs, but they receive no implicit merge/deploy authority. Repository policy and CI apply equally to human and machine contributors.

Opening a public PR does **not** automatically spend AMI inference budget. Deterministic CI may run normally, while server-side AI review is explicitly gated by a maintainer action such as the `ami-ai-review` label. This keeps the network open to contribution without allowing arbitrary public input to create unlimited provider cost.

Useful contributors can earn more contextual trust over time through reproducible, validated work. Trust is evidence-linked and revisable; stars, titles, identity or claimed model capability are not substitutes for evidence.

## Archaeology

Historical AMI material should be cited by source repository/path/commit where possible. If licensing or provenance is unclear, use it as evidence for a clean reimplementation rather than copying it directly.

Historical implementation claims remain `HISTORICAL`/`UNKNOWN` until current evidence validates them.

## Status language

Implementation: `DESIGN / RESEARCH / EXPERIMENT / PoC / IMPLEMENTED / VALIDATED / UNKNOWN`

Lifecycle: `CURRENT / SUPERSEDED / REJECTED / DEAD_END / HISTORICAL / UNRESOLVED`
