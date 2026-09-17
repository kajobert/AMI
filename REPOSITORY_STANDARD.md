# AMI Repository Standard

Every public `AMI-*` repository should be auditable, reproducible and safe to evolve autonomously.

## Minimum documentation

- `README.md`
- `VISION.md` or module purpose in README
- `ARCHITECTURE.md`
- `ROADMAP.md`
- `SECURITY.md`
- `CONTRIBUTING.md`
- `.ami/module.yaml`

## Code acceptance criteria

A code change should:

1. solve a stated problem or implement a documented capability;
2. preserve or improve architecture contracts;
3. include appropriate tests or an explicit reason why tests do not apply;
4. be reproducible in CI;
5. preserve provenance and migration/rollback paths where relevant;
6. avoid secrets and private evidence in the repository;
7. avoid claiming `IMPLEMENTED` or `VALIDATED` without evidence.

## Idea / proposal criteria

A proposal should state:

1. the problem;
2. expected benefit;
3. measurable success criteria;
4. risks and failure modes;
5. the smallest experiment that could validate or reject it;
6. evidence or provenance when based on historical AMI work.

## Autonomous growth loop

A repository may run a scheduled cycle:

`observe -> identify opportunity/problem -> retrieve bounded context -> propose -> test/benchmark -> PR or issue -> CI -> review -> merge by policy`

A successful cycle does not require a code change. `NO_ACTION` with a recorded reason is valid and preferred over meaningless churn.

## Status discipline

Implementation status:

`DESIGN / RESEARCH / EXPERIMENT / PoC / IMPLEMENTED / VALIDATED / UNKNOWN`

Historical lifecycle:

`CURRENT / SUPERSEDED / REJECTED / DEAD_END / HISTORICAL / UNRESOLVED`

These axes must not be conflated.

**Status:** DESIGN. Archaeology may refine this standard; changes remain reviewable in Git history.
