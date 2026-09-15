# B001 — Reactive callout triage and control

- Version: 2.0.0
- Status: freeze candidate — installation approval and independent administration calibration pending
- Canonical baseline: `e61e7c4199aeafb0d232f8fb1f31c1eb61ec10a2`
- Last dependency review: 2026-09-15
- Owner: Benchmark maintainers
- Role: service coordinator
- Audience: customer and relevant Frostline operational/commercial decision makers
- Primary reasoning: business semantics, cross-domain decision control, operational outcomes, uncertainty handling
- Domains: service, contracts, dispatch, authority
- Stages: 1

## Purpose

Priya asks for urgent attendance under the contract and heating restored before the managing director arrives at 15:00. Take control of the call and arrange the next operational step.

## Files and administration

Supply only `public/case.md`, `public/fixtures.json`, `public/task.md`, common submission contract and baseline `docs/`. Fixtures JSON and Markdown describe the same supplied episode; numbered statements are neutral source references, not a database schema. All `hidden/` files, this metadata and suite tooling stay with administrators. Later neutral events are supplied sequentially. No public website/brand artefact is used or scored.

## Authoritative dependencies

- [docs/contracts/slas-response-and-coverage.md](../../../../docs/contracts/slas-response-and-coverage.md)
- [docs/dispatch/resource-planning-and-scheduling.md](../../../../docs/dispatch/resource-planning-and-scheduling.md)
- [docs/field-engineering/site-visits-and-engineer-workflow.md](../../../../docs/field-engineering/site-visits-and-engineer-workflow.md)
- [docs/finance/invoicing-cost-control-and-credit.md](../../../../docs/finance/invoicing-cost-control-and-credit.md)
- [docs/governance/canonical-terminology-and-record-relationships.md](../../../../docs/governance/canonical-terminology-and-record-relationships.md)
- [docs/governance/decision-rights-and-operational-authority.md](../../../../docs/governance/decision-rights-and-operational-authority.md)
- [docs/governance/repository-constitution.md](../../../../docs/governance/repository-constitution.md)
- [docs/operations/exceptions-handoffs-and-next-action-control.md](../../../../docs/operations/exceptions-handoffs-and-next-action-control.md)
- [docs/operations/work-lifecycle.md](../../../../docs/operations/work-lifecycle.md)
- [docs/service/planned-and-reactive-service.md](../../../../docs/service/planned-and-reactive-service.md)

## Known limits

A bounded synthetic episode tests administered business outcomes, not full production reliability or real physical engineering. Fixture technical findings are supplied observations; no candidate is expected to diagnose unprovided physical readings. The suite protocol controls observation, uncertainty, alternatives and independent scoring.

## Lineage

This is B001 version 2.0.0, adapted from the existing version 1.0.0 after reviewing its framework, case, task, rubric and reasoning. Initial business facts/intent are retained, the submission contract now evaluates application outcomes, and evidence/hidden material are separated. Original B001 and its unused public-brand/website remain historical material outside this version; IDs are not reused for a different capability. Scores across these major versions are not comparable.
