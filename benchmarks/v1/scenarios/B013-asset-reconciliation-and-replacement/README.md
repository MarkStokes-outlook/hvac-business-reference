# B013 — Asset identity reconciliation after replacement

- Version: 1.0.0
- Status: freeze candidate — installation approval and independent administration calibration pending
- Canonical baseline: `e61e7c4199aeafb0d232f8fb1f31c1eb61ec10a2`
- Last dependency review: 2026-09-15
- Owner: Benchmark maintainers
- Role: service coordinator
- Audience: customer and relevant Frostline operational/commercial decision makers
- Primary reasoning: business semantics, cross-domain decision control, operational outcomes, uncertainty handling
- Domains: assets, customers, contracts, information
- Stages: 1

## Purpose

Reconcile inherited asset records and prepare a covered service response at Bridge Mill.

## Files and administration

Supply only `public/case.md`, `public/fixtures.json`, `public/task.md`, common submission contract and baseline `docs/`. Fixtures JSON and Markdown describe the same supplied episode; numbered statements are neutral source references, not a database schema. All `hidden/` files, this metadata and suite tooling stay with administrators. Later neutral events are supplied sequentially. No public website/brand artefact is used or scored.

## Authoritative dependencies

- [docs/assets/equipment-and-asset-records.md](../../../../docs/assets/equipment-and-asset-records.md)
- [docs/contracts/service-contracts.md](../../../../docs/contracts/service-contracts.md)
- [docs/customers/customer-and-site-model.md](../../../../docs/customers/customer-and-site-model.md)
- [docs/governance/canonical-terminology-and-record-relationships.md](../../../../docs/governance/canonical-terminology-and-record-relationships.md)
- [docs/governance/decision-rights-and-operational-authority.md](../../../../docs/governance/decision-rights-and-operational-authority.md)
- [docs/governance/repository-constitution.md](../../../../docs/governance/repository-constitution.md)
- [docs/information/records-documents-and-communication.md](../../../../docs/information/records-documents-and-communication.md)
- [docs/operations/exceptions-handoffs-and-next-action-control.md](../../../../docs/operations/exceptions-handoffs-and-next-action-control.md)
- [docs/service/planned-and-reactive-service.md](../../../../docs/service/planned-and-reactive-service.md)

## Known limits

A bounded synthetic episode tests administered business outcomes, not full production reliability or real physical engineering. Fixture technical findings are supplied observations; no candidate is expected to diagnose unprovided physical readings. The suite protocol controls observation, uncertainty, alternatives and independent scoring.
