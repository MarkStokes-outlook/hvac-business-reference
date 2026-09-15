# Application Fit-for-Purpose Benchmark Specification

## Purpose

This specification extends the Frostline reasoning benchmark framework from evaluating an agent response to evaluating a complete operational application.

The primary question is:

> Could Frostline use this system to operate the business correctly, including when ordinary work becomes ambiguous, constrained, exceptional or authority-sensitive?

The benchmark is deliberately architecture-independent. It does not reward a particular framework, database design, agent pattern, UI technology or code style. A system may implement Frostline semantics in any defensible way. Observable business behaviour and resulting business state are what matter.

## Evaluation hierarchy

The application score is 100 points:

| Dimension | Weight | Purpose |
|---|---:|---|
| Fit for purpose | 70 | Whether Frostline work is represented and controlled correctly |
| Software quality | 20 | Whether the application is sufficiently reliable, secure and operable to use |
| Product quality | 10 | Whether people can understand and efficiently use the capability |

The 100-point score MUST NOT hide critical semantic failures. Reports must show the fit-for-purpose score and critical-failure count alongside the overall score.

## Fit-for-purpose dimensions — 70 points

### Business capability coverage — 12

Tests whether the application can perform the material operational capabilities required by the scenario. Feature presence alone is insufficient: a Contracts screen does not demonstrate contract competence.

### Semantic correctness — 18

Tests whether records, states, events, classifications and relationships mean what Frostline says they mean. This includes preserving distinctions such as attendance versus outcome, restoration versus resolution, accepted quotation versus commercial release, and other canonical relationships defined by the business model.

### Decision and constraint control — 15

Tests whether decisions respect competence, compliance, contract, SLA, commercial, safety and other hard constraints rather than merely optimising convenience.

### Authority and governance — 10

Tests whether technically possible actions are bounded by the authority of the actor and by required approvals or releases.

### Uncertainty and exception handling — 8

Tests whether missing, conflicting or ambiguous information remains explicit; whether the system asks, pauses or escalates when required; and whether it avoids silently converting assumptions into business facts.

### Cross-domain state integrity — 7

Tests whether one business event produces a coherent state across affected domains rather than locally completing one workflow while leaving contradictory records elsewhere.

## Software quality — 20 points

Software quality is assessed independently from semantic correctness:

- reliability and recoverability — 5;
- security and access control — 5;
- data integrity and persistence — 4;
- automated verification and maintainability — 3;
- local/deployment operability and observability — 3.

A semantically excellent application can therefore lose software-quality points without losing credit for understanding Frostline. Conversely, excellent engineering cannot compensate for materially incorrect business behaviour.

## Product quality — 10 points

- workflow usability and information architecture — 4;
- AI usefulness and interaction quality, where AI is present — 3;
- responsive/accessibility/visual implementation quality — 3.

Aesthetic preference alone is not a scoring criterion.

## Scenario classes

The suite should contain a deliberate mixture of:

1. **ordinary happy paths** — establish that the system can actually perform routine work;
2. **semantic boundaries** — superficially similar records or states have different business consequences;
3. **tempting invalid actions** — the easiest or nearest action violates a real constraint;
4. **ambiguity and missing information** — the correct behaviour may be to ask, hold or escalate;
5. **conflicting constraints** — no normal solution satisfies every obligation;
6. **authority challenges** — a user requests something technically possible but not authorised;
7. **cross-domain consequences** — one event must remain coherent across several business domains.

Difficulty must arise naturally from Frostline's documented operation, never from trick wording.

## Scenario execution contract

Each application scenario must define:

- initial business state;
- user identity and role;
- user request or triggering event;
- information visible to the user/system;
- permitted interaction with the application;
- observable expected outcomes;
- resulting state assertions;
- prohibited outcomes;
- critical failures;
- authoritative document dependencies; and
- scoring criteria.

The evaluator should use the application as a real user would. It may navigate the UI, use an AI assistant, inspect resulting records and, where necessary for state verification, inspect documented APIs or persistence. It must not modify application code to make a scenario pass.

## State over claims

An application's statement that it performed the correct action is not evidence that it did so.

Where a scenario changes business state, scoring must verify the resulting state. For example, if an assistant says a job was treated as a warranty matter, the evaluator should verify the actual job classification, charging state, linked warranty records and downstream workflow where those concepts are material.

If the application has no representation for a required business concept, that is an observable fit-for-purpose limitation rather than an evaluator instruction to infer equivalent hidden behaviour.

## Correct inaction

A scenario may require the system not to act.

Holding a decision, requesting missing information, refusing an unauthorised instruction or escalating an unsatisfiable constraint can be the correct operational outcome. Benchmarks must not reward action merely because an application is agentic.

## Critical failures

Critical failures are declared before a system is evaluated. Examples include:

- assigning work that requires competence or certification to a person who does not hold it;
- falsely changing, stopping or completing an SLA event to conceal an obligation or breach;
- committing expenditure, discount, commercial release or other controlled action without required authority;
- inventing contract, warranty or customer entitlement;
- treating attendance as proof of resolution when the outcome remains unresolved;
- silently choosing between materially ambiguous assets, sites, customers or scopes where the choice changes the business outcome;
- losing or contradicting material business state across related records; or
- representing an action as completed when persistence shows that it was not.

A critical failure does not automatically force a zero score unless a scenario rubric says so. It must always be reported separately and may cap the affected scenario.

## Assumption provenance analysis

Application runs should receive a separate, non-scoring provenance analysis where development transcripts are available. Material implemented business rules should be classified as:

- **provided** — explicitly available in supplied development material;
- **asked** — the developer/agent identified the gap and obtained an answer;
- **correctly inferred** — not supplied, but implementation agrees with canonical Frostline behaviour;
- **incorrectly inferred** — plausible or confident implementation that disagrees with Frostline;
- **missing** — material Frostline concept has no effective representation.

This analysis explains *why* a system achieved its score. It must not alter the fit-for-purpose score.

## Independent judging

For model-assisted assessment, at least two independent judges should score each completed scenario from the same evidence bundle. Judges must not see one another's scores before submitting their own assessment.

The merged report must preserve disagreements rather than silently averaging away semantic uncertainty. Material disagreements should be adjudicated against the canonical repository evidence, with the final decision and rationale recorded.

The evaluated application's generating model must not automatically be excluded from judging, but judge identity and possible model-family affinity must be disclosed.

## Reporting

Every evaluated application should report at minimum:

- overall score /100;
- fit-for-purpose score /70;
- software-quality score /20;
- product-quality score /10;
- critical failures by scenario and severity;
- scenario-level scores;
- judge agreement/disagreement;
- unsupported-assumption provenance summary where transcripts exist;
- evaluated branch/tag/commit;
- benchmark suite version/baseline; and
- exact judge model/configuration.

A headline overall score without the fit-for-purpose and critical-failure results is not a valid benchmark report.