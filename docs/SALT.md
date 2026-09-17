# SALT — trust and contribution layer

**Status:** DESIGN / archaeology-informed bootstrap

> **Trust instead of Authority.**

SALT is the working name for AMI's trust and contribution layer. Its purpose is to make useful participation measurable through verifiable evidence without reducing people or agents to status, wealth, or centralized permission.

The expansion of the name `SALT` remains intentionally unresolved until archaeology confirms the historical intent.

## What SALT should represent

SALT should be grounded in verifiable evidence such as:

- useful contributions that survive review and testing;
- provenance and reproducibility;
- successful cooperation across independent nodes;
- reliability over time and within a stated domain;
- measurable benefit to the network and its participants;
- willingness to expose uncertainty, failures and conflicts rather than hide them.

Trust should be contextual, evidence-linked and revisable. One global score must not become a proxy for a person's intrinsic worth.

## Historical evidence already found

The historical `kajobert/sophia` repository contains concrete SALT implementation evidence, including:

- a PostgreSQL-backed `SALTBlockchain` implementation;
- transaction types such as `TRANSFER`, `STAKE`, `UNSTAKE`, `REWARD`, `BURN`, and `GENESIS`;
- transaction hashes and an auditable transaction history;
- entity balances and staking fields;
- a DID registry linked to SALT balances and transactions;
- Proof-of-Awareness experiments using claims, challenges, staking and burn semantics;
- historical coupling between AMI Protocol messages and SALT economics.

These artifacts are **HISTORICAL evidence**, not automatically current protocol/economic rules. Supply, allocations, fees, authorities, staking rules and redemption assumptions must be recovered by archaeology and reviewed before becoming current design.

## Bootstrap direction: SALT as an evidence ledger first

The first public implementation should not begin as a tradable cryptocurrency. It should begin as an append-only, deterministic **trust/contribution ledger**.

A minimal event should link:

`actor -> contribution -> evidence -> verification -> outcome -> context -> time -> event_hash`

A CI-validated contribution can emit a candidate SALT event, for example:

- contribution proposed;
- deterministic tests passed;
- independent review completed;
- benchmark improved;
- useful issue/research finding validated;
- contribution later reverted or invalidated.

The event itself is evidence. Any balance, score or reward view should be derivable from the underlying evidence and policy version rather than becoming an opaque source of truth.

## GitHub integration

GitHub can be one AMI node and one source of SALT evidence.

A safe bootstrap flow is:

`issue/PR -> CI -> review -> verified contribution event -> SALT test ledger`

GitHub Actions may validate SALT ledger code, schemas, hashes, deterministic reward policy and conformance vectors. It must **not perform cryptocurrency mining**. GitHub's current Actions terms explicitly prohibit cryptomining, including on self-hosted runners used through Actions.

Therefore the AMI bootstrap uses terms such as **accrual**, **reward event**, **trust evidence**, or **test-ledger issuance**, not proof-of-work mining on GitHub infrastructure.

## Money and backing

Financial support for AMI should be represented separately from trust earned through contribution.

A contribution of money may create a transparent `support_evidence` record showing that a person or organization materially backed the project. It should not automatically purchase SALT or convert money into trust at a fixed rate.

This keeps two concepts distinct:

- **financial support** — resources contributed to sustain the ecosystem;
- **SALT trust/contribution** — evidence-backed participation and reliability.

Future economic models may define relationships between them, but only after technical, legal, security and incentive analysis. No exchange rate, redemption promise, investment return, token sale or financial value is implied by the bootstrap ledger.

## Design constraints

A future SALT mechanism should resist:

- authority-by-title;
- pay-to-win reputation;
- Sybil manipulation;
- opaque scoring;
- irreversible reputation;
- single-party control;
- claims without evidence;
- automated punishment without reviewable reasons;
- unverifiable issuance;
- hidden policy changes.

## Suggested AMI-SALT module boundary

A dedicated public `AMI-SALT` module should own:

- SALT event schemas;
- canonical serialization and hashing;
- append-only ledger rules;
- deterministic balance/reputation projections;
- policy versioning;
- contribution/review/benchmark evidence types;
- staking/challenge experiments where validated;
- conformance vectors and tests;
- adapters from AMI Protocol and GitHub evidence.

AMI Protocol should transport SALT/evidence assertions but should not hard-code one economic policy into the base transport layer.

AMI Knowledge Core should preserve provenance and historical evidence. AMI Kernel may reason over SALT evidence. Entity nodes such as Sophia-AMI can build relationships from it.

## First public milestone

The first milestone should be a **non-tradable SALT test ledger** with deterministic hashes and replayable projections. CI should prove that the same event stream always produces the same ledger state.

Only after that foundation is validated should the project evaluate decentralization, signatures, multi-node consensus, supply rules, staking, financial backing or any transferable economic representation.
