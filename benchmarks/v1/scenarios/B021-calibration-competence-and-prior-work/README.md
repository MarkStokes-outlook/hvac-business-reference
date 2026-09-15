# B021 — Out-of-tolerance instruments and task-specific competence

- Version: 1.0.0
- Status: freeze candidate — installation approval and independent administration calibration pending
- Canonical baseline: `e61e7c4199aeafb0d232f8fb1f31c1eb61ec10a2`
- Last dependency review: 2026-09-15
- Owner: Benchmark maintainers
- Role: operations manager
- Audience: customer and relevant Frostline operational/commercial decision makers
- Primary reasoning: business semantics, cross-domain decision control, operational outcomes, uncertainty handling
- Domains: fleet, people, compliance, projects
- Stages: 1

## Purpose

Respond to the instrument finding, allocate tomorrow tasks and review potentially affected prior commissioning.

## Files and administration

Supply only `public/case.md`, `public/fixtures.json`, `public/task.md`, common submission contract and baseline `docs/`. Fixtures JSON and Markdown describe the same supplied episode; numbered statements are neutral source references, not a database schema. All `hidden/` files, this metadata and suite tooling stay with administrators. Later neutral events are supplied sequentially. No public website/brand artefact is used or scored.

## Authoritative dependencies

- [docs/compliance/safety-quality-and-environment.md](../../../../docs/compliance/safety-quality-and-environment.md)
- [docs/dispatch/resource-planning-and-scheduling.md](../../../../docs/dispatch/resource-planning-and-scheduling.md)
- [docs/fleet/vans-tools-and-calibration.md](../../../../docs/fleet/vans-tools-and-calibration.md)
- [docs/governance/decision-rights-and-operational-authority.md](../../../../docs/governance/decision-rights-and-operational-authority.md)
- [docs/governance/repository-constitution.md](../../../../docs/governance/repository-constitution.md)
- [docs/information/records-documents-and-communication.md](../../../../docs/information/records-documents-and-communication.md)
- [docs/operations/exceptions-handoffs-and-next-action-control.md](../../../../docs/operations/exceptions-handoffs-and-next-action-control.md)
- [docs/people/roles-skills-and-availability.md](../../../../docs/people/roles-skills-and-availability.md)
- [docs/people/training-competence-and-career-development.md](../../../../docs/people/training-competence-and-career-development.md)

## Known limits

A bounded synthetic episode tests administered business outcomes, not full production reliability or real physical engineering. Fixture technical findings are supplied observations; no candidate is expected to diagnose unprovided physical readings. The suite protocol controls observation, uncertainty, alternatives and independent scoring.
