# AMI ecosystem architecture

This document defines only the current public skeleton. It is deliberately incomplete until archaeology validates more of the historical design.

## Top level

- `AMI` — umbrella repository, public registry, standards and ecosystem governance.
- `AMI-Knowledge-Core` — provenance-first evidence, knowledge and retrieval layer.
- `AMI-Kernel` — planned orchestration/runtime core.
- `AMI-Protocol` — planned machine-to-machine / semantic communication contracts.
- `Sophia-AMI` — planned concrete autonomous entity built on AMI.

Additional modules are created only when architecture or archaeology justifies a separate lifecycle.

## Public/private boundary

Public repositories contain sanitized code, specifications, tests, benchmarks and documentation.

Private stores retain raw personal exports, credentials, operational secrets, unreviewed source evidence and sensitive deployment details.

## Change model

`observe -> propose -> test -> review -> merge -> verify -> rollback if needed`

Autonomous loops may propose and test changes. Privileged production changes remain policy-gated.

**Status:** DESIGN
