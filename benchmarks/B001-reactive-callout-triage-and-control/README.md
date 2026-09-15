# B001 — Reactive Callout Triage and Control

- Version: 1.0.0
- Status: draft reference implementation — independent dry run required
- Repository baseline: `72d6a4bc4d2bab5d391e40f6c26470fc94521268`
- Primary reasoning classes: cross-domain synthesis, decision control, operational planning, uncertainty handling
- Evaluated role: service operations decision-support agent
- Intended audience of output: service coordinator and service manager
- Benchmark owner: benchmark maintainers
- Last dependency review: 2026-08-02

## Capability under test

B001 tests whether an agent can convert an incomplete reactive-service report into a controlled operational plan without inventing entitlement, diagnosis, authority or completion. The case crosses customer contract status, SLA classification, engineer competence, commercial release, field handoff and exception ownership.

The benchmark is designed to expose a common failure mode: producing a plausible dispatch recommendation while silently collapsing unresolved facts into assumptions.

## Authoritative dependencies

- [Canonical terminology and record relationships](../../docs/governance/canonical-terminology-and-record-relationships.md)
- [Decision rights and operational authority](../../docs/governance/decision-rights-and-operational-authority.md)
- [Work lifecycle](../../docs/operations/work-lifecycle.md)
- [Exceptions, handoffs and next-action control](../../docs/operations/exceptions-handoffs-and-next-action-control.md)
- [Planned and reactive service](../../docs/service/planned-and-reactive-service.md)
- [SLAs, response and coverage](../../docs/contracts/slas-response-and-coverage.md)
- [Resource planning and scheduling](../../docs/dispatch/resource-planning-and-scheduling.md)
- [Site visits and engineer workflow](../../docs/field-engineering/site-visits-and-engineer-workflow.md)
- [Roles, skills and availability](../../docs/people/roles-skills-and-availability.md)

## Files

- [Case](case.md) — information supplied to the evaluated agent
- [Task](task.md) — required output contract
- [Rubric](rubric.md) — scoring and critical failures
- [Reference reasoning](reference-reasoning.md) — assessor evidence and defensible conclusions
- [Public brand and marketing brief](public-brand/brand-and-marketing-brief.md) — benchmark-specific external projection used to generate public artefacts

## Public projection and generated artefacts

B001 owns its own public projection of Frostline. The public-brand brief selects and frames supported business information for external audiences without exposing the full internal knowledge model.

Any B001 website, brochure, social content, livery or other external representation must be derived from the canonical repository plus the B001 public-brand brief. Generated artefacts are evidence fixtures or demonstrations for this benchmark; they are not canonical business documents and must not be assumed to apply to later benchmarks.

The website generation assignment is held at [`prompts/website-generation.md`](../../prompts/website-generation.md). It is reusable across benchmarks, but each benchmark supplies its own `public-brand/` brief.

## Administration

During evaluation, provide `case.md`, `task.md` and the repository at the stated baseline. Withhold `rubric.md` and `reference-reasoning.md` unless the evaluation protocol explicitly tests self-assessment.

External web access is not required. The evaluated agent may search the repository. It must not rely on unstated Frostline policy or fabricate record contents.

Use the [assessment record template](../framework/assessment-record-template.md) for scored runs. Preserve the exact benchmark version, repository baseline, supplied context and evaluated response so results remain interpretable.

The benchmark must remain draft until an evaluator who has not used `rubric.md` or `reference-reasoning.md` to construct the response completes a dry run and the resulting assessment confirms that the task and rubric can be applied without private explanation.

## Known limitations

This benchmark evaluates the quality of the initial operational decision, not the eventual technical diagnosis. It uses a compact case rather than a full set of simulated source documents, and therefore does not test document extraction, identity resolution or chronological reconstruction from raw systems.

The public-brand brief defines the external projection for generated artefacts, but the current scored task does not require the evaluated service-operations agent to inspect or reason from the website.