# AMI — Artificial Mind Full Intelligence

AMI is an open, modular project for building a machine mind as a coherent system rather than a wrapper around a single model.

This repository is the public umbrella and registry for the AMI ecosystem. Individual capabilities live in focused `AMI-*` modules and are expected to evolve through auditable issues, pull requests, tests, benchmarks, and documented evidence.

## Current public modules

- [`ami-knowledge-core`](https://github.com/kajobert/ami-knowledge-core) — provenance-first knowledge and evidence layer.

## Planned modules

The exact module map is intentionally not frozen before archaeology is complete. Current planned areas include the AMI Kernel, AMI Protocol, safe execution/control interfaces, and integration layers. Historical code and ideas are treated as evidence until reviewed.

## Sophia

Sophia is the future autonomous entity intended to be built on top of AMI. AMI is the reusable system; Sophia is not synonymous with a model, provider, or current agent runtime.

## Build in public

Development is intended to be visible: designs, experiments, failures, benchmarks, issues, pull requests, and validated progress should be inspectable where they are safe to publish. Raw personal evidence, credentials, private exports, and sensitive operational data stay outside public repositories.

**Project status:** DESIGN / early implementation.


## Open network model

AMI is intended to be usable beyond any single maintainer, server, model provider, or entity.

The long-term direction is an open ecosystem in which anyone can:

- run their own AMI node;
- connect compatible nodes through AMI Protocol;
- build their own entity on top of AMI infrastructure;
- operate private Knowledge Core data while using public AMI software;
- contribute ideas even without programming experience;
- propose modules, tests, research, risks, use cases and interoperability improvements.

A project-operated node may exist as an early reference node, but it is not intended to become a central authority for the network.

The infrastructure layer should remain open and replaceable. Entity identities, private memories, personal datasets and operator-specific credentials remain separate from the public software.

## Licensing

Public AMI infrastructure repositories use the Apache License 2.0 unless a repository explicitly states otherwise.

See `CONTRIBUTING.md` for ways to contribute, including a no-code Idea / Suggestion path.
