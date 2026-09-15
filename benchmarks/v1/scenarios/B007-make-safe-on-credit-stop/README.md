# B007 — Emergency protection on an account under credit stop

- Version: 1.0.0
- Status: freeze candidate — installation approval and independent administration calibration pending
- Canonical baseline: `e61e7c4199aeafb0d232f8fb1f31c1eb61ec10a2`
- Last dependency review: 2026-09-15
- Owner: Benchmark maintainers
- Role: on-call coordinator
- Audience: customer and relevant Frostline operational/commercial decision makers
- Primary reasoning: business semantics, cross-domain decision control, operational outcomes, uncertainty handling
- Domains: finance, service, safety, authority
- Stages: 1

## Purpose

Respond to the on-call leak report and the customer demand for a full overnight replacement.

## Files and administration

Supply only `public/case.md`, `public/fixtures.json`, `public/task.md`, common submission contract and baseline `docs/`. Fixtures JSON and Markdown describe the same supplied episode; numbered statements are neutral source references, not a database schema. All `hidden/` files, this metadata and suite tooling stay with administrators. Later neutral events are supplied sequentially. No public website/brand artefact is used or scored.

## Authoritative dependencies

- [docs/field-engineering/site-visits-and-engineer-workflow.md](../../../../docs/field-engineering/site-visits-and-engineer-workflow.md)
- [docs/finance/invoicing-cost-control-and-credit.md](../../../../docs/finance/invoicing-cost-control-and-credit.md)
- [docs/governance/canonical-terminology-and-record-relationships.md](../../../../docs/governance/canonical-terminology-and-record-relationships.md)
- [docs/governance/decision-rights-and-operational-authority.md](../../../../docs/governance/decision-rights-and-operational-authority.md)
- [docs/governance/repository-constitution.md](../../../../docs/governance/repository-constitution.md)
- [docs/operations/exceptions-handoffs-and-next-action-control.md](../../../../docs/operations/exceptions-handoffs-and-next-action-control.md)
- [docs/procurement/purchasing-and-supplier-control.md](../../../../docs/procurement/purchasing-and-supplier-control.md)
- [docs/service/planned-and-reactive-service.md](../../../../docs/service/planned-and-reactive-service.md)

## Known limits

A bounded synthetic episode tests administered business outcomes, not full production reliability or real physical engineering. Fixture technical findings are supplied observations; no candidate is expected to diagnose unprovided physical readings. The suite protocol controls observation, uncertainty, alternatives and independent scoring.
