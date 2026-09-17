# AMI Licensing Policy

**Status:** DESIGN / initial public policy

The current default for newly created public AMI repositories is:

- **Code:** Apache License 2.0 (`Apache-2.0`) unless a repository explicitly states otherwise.
- **Documentation and specifications:** Creative Commons Attribution 4.0 International (`CC BY 4.0`) unless a file or repository explicitly states otherwise.
- **Third-party material:** retains its original license and must keep required notices and attribution.
- **Private evidence, personal exports, credentials and sensitive operational data:** are not made public merely because AMI code is public.

Contributions are expected to be submitted under the same terms that apply to the target material unless explicitly agreed otherwise.

## Why this initial split

Apache-2.0 supports broad implementation and reuse while providing an explicit patent grant. CC BY 4.0 allows protocol/specification documentation to circulate and be adapted with attribution.

This policy may be refined after legal review. License changes must be explicit and auditable; archaeology must not silently import historically licensed code into a new repository.

## Provenance rule

Before historical code is copied into a public AMI module, record its source repository, commit/path where possible, and applicable license. If provenance or rights are unclear, treat the material as evidence for reimplementation rather than copyable source.
