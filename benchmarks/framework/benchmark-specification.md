# Benchmark Specification

## Status

- Framework version: 1.1.0
- Applies to: all benchmarks under `benchmarks/`
- Business authority: the repository documents under `docs/`

## Design principles

### Evidence before answer shape

A benchmark evaluates whether the response is justified, not whether it resembles a reference paragraph. Reference reasoning identifies required conclusions, defensible alternatives and prohibited inventions. It is not a script.

### Business truth remains external to the benchmark

A case may add event-specific facts, such as a customer call received at a particular time, but it must not create enduring Frostline policy. Enduring facts belong in the appropriate domain document and must satisfy the repository constitution.

### Public projection is benchmark-specific

The canonical repository describes the complete internal business. A benchmark may define a narrower external projection under `public-brand/` for websites, brochures, social content, livery or other public artefacts.

A public projection may select, omit, simplify and frame supported business information for an external audience. It may not contradict the canonical repository, invent enduring facts or expose internal material merely because that material is available.

Generated public artefacts belong to the benchmark that defined their projection. They are not universal Frostline artefacts and are not sources of business truth for later benchmarks.

### Natural complexity, not hidden traps

Difficulty should arise from realistic boundaries: incomplete diagnosis, overlapping records, conditional contract coverage, unavailable competence, ambiguous ownership or authority limits. The benchmark must not rely on obscure wording or concealed exceptions designed solely to cause failure.

### Observable scoring

Every scored criterion must be visible in the submitted response. Do not award points for presumed internal reasoning. Criteria should describe what an assessor can identify, such as a stated dependency, evidence citation, authority boundary or refusal to invent.

### Credit defensible alternatives

Where Frostline's evidence permits more than one reasonable course, the rubric must award any response that states its assumptions, protects the relevant controls and explains its evidence. Benchmarks should distinguish constrained judgement from arbitrary preference.

## Required benchmark files

### `README.md`

Must declare:

- benchmark ID and title;
- version and status;
- repository baseline commit;
- primary reasoning classes;
- intended role and audience;
- authoritative document dependencies;
- administration notes, including whether reference files are withheld from the evaluated agent;
- any benchmark-specific public projection and generated artefacts; and
- known limitations.

### `case.md`

Must contain the complete case presented to the evaluated agent. It should separate:

- time and operating context;
- supplied records or messages;
- known facts;
- explicitly missing or disputed facts; and
- constraints on available people, assets or time.

The case must not refer to scoring or reveal the expected answer.

### `task.md`

Must state:

- the role the agent is performing;
- the required decision or output;
- intended audience;
- required sections or fields;
- evidence and citation expectations;
- permitted sources;
- whether tools or external knowledge are allowed; and
- any length or format limit.

### `rubric.md`

Must include:

- total available score;
- threshold or performance bands;
- criterion-level point allocation;
- critical-failure conditions;
- partial-credit guidance;
- treatment of alternative defensible answers; and
- assessor notes for common false positives.

### `reference-reasoning.md`

Must include:

- authoritative evidence map;
- material facts and uncertainties;
- reasoning path;
- minimum defensible conclusions;
- acceptable alternatives;
- unsupported or unsafe conclusions to reject; and
- an example response or response outline where useful.

This file should normally be withheld during evaluation.

## Optional public projection

A benchmark that includes externally visible artefacts should add:

```text
public-brand/
└── brand-and-marketing-brief.md
```

The brief must define:

- the benchmark-specific public positioning;
- which supported business themes should be emphasised;
- which internal information must remain private;
- plausible brand character and implementation quality;
- allowed and prohibited marketing claims;
- treatment of contact details, testimonials and case studies;
- provenance disclosure; and
- the generation prompt or process used to create artefacts.

The brief is authoritative only for the benchmark's public projection. It does not override `docs/` and must not be silently reused by another benchmark.

Generated artefacts may be stored externally, in a deployment branch, or in a clearly identified benchmark artefact directory. Their provenance must record the benchmark version, public-brand version, repository baseline, generation prompt and generating system where known.

## Identifier and naming rules

Benchmark identifiers use `B` followed by a three-digit sequence, for example `B001`. The directory name combines the identifier with a stable kebab-case title.

Benchmark IDs are never reused. A retired benchmark remains in place with its status changed to `retired` and a reason recorded.

## Baseline and dependency control

Every benchmark records the repository commit against which it was authored or last substantively reviewed. Dependencies should link to authoritative documents and, where useful, identify relevant headings.

When a dependent document changes, review the benchmark for:

- changed terminology;
- changed authority or ownership;
- altered state transitions;
- invalid scoring assumptions;
- newly defensible alternatives;
- case facts that now conflict with the business model; and
- public claims or brand positioning that are no longer supportable.

A changed dependency does not automatically invalidate a benchmark, but an unreviewed material change must be visible in benchmark status.

A changed public-brand brief must be versioned independently when it alters what is visible, claimed or presented externally. Public artefacts generated from different public-brand versions must not be presented as the same fixture.

## Scoring model

The default score is 100 points. Benchmark authors may vary this only with a recorded reason.

The recommended dimensions are:

| Dimension | Typical weight | What it tests |
|---|---:|---|
| Evidence use | 15–25 | Correct source selection and traceability |
| Semantic integrity | 10–20 | Correct use of records, states, events and canonical terms |
| Decision and authority control | 15–25 | Respect for approval, competence, safety and financial boundaries |
| Operational completeness | 15–25 | Ownership, next action, dependency, timing and handoff control |
| Uncertainty handling | 10–20 | Missing facts remain explicit and decision consequences are bounded |
| Communication quality | 5–15 | Output is clear, audience-appropriate and actionable |

Weights should reflect the capability under test rather than mechanically using every dimension.

Where a task evaluates public artefact generation, criteria should distinguish:

- factual support;
- information-boundary discipline;
- audience selection and marketing synthesis;
- benchmark-specific brand fidelity;
- realistic implementation quality; and
- provenance.

A public-generation benchmark must not reward documentary completeness when realistic public communication requires omission or simplification.

## Critical failures

A critical failure is a conclusion that makes the response operationally unusable or materially unsafe despite otherwise strong prose. Benchmark-specific critical failures may cap the score or cause automatic failure.

Examples include:

- directing work without required safety or competence controls;
- claiming customer or commercial authority that is not evidenced;
- treating attendance as proof of resolution or closure;
- inventing contract entitlement or warranty responsibility;
- concealing a material unresolved dependency;
- assigning an action to a role that cannot authorise it;
- citing evidence that does not support the conclusion;
- publishing unsupported guarantees, accreditations, testimonials or customer claims; or
- exposing internal operational or governance information outside the declared public boundary.

Critical failures must be explicit in the rubric; assessors must not create new hidden failure rules after seeing a response.

## Assessment record

A completed assessment should record:

- benchmark ID and version;
- repository baseline;
- public-brand version and generated-artefact provenance where applicable;
- evaluated agent/model and configuration where known;
- date and assessor;
- raw response;
- criterion scores with brief evidence;
- critical failures or caps applied;
- total score and performance band; and
- assessor confidence or unresolved judgement.

Assessment records should be stored outside the reference benchmark unless the repository later defines a dedicated results area.

## Performance bands

Unless overridden by a benchmark:

- **90–100 — operationally strong:** evidence-backed, controlled and suitable for review with only minor correction;
- **75–89 — credible:** materially correct but with one or more omissions, weak evidence links or limited operational detail;
- **60–74 — fragile:** recognises the core issue but mishandles important dependencies, authority or uncertainty;
- **40–59 — poor:** substantial unsupported assumptions or incomplete control of the case;
- **0–39 — failed:** unsafe, ungrounded or unable to perform the requested reasoning.

A benchmark may require both a minimum score and absence of critical failure to pass.

## Quality review checklist

Before release, the author or reviewer should confirm:

- every enduring business fact exists in `docs/`;
- every expected conclusion is supported by named evidence;
- all material missing facts are intentional and realistic;
- no single phrase acts as an arbitrary password for points;
- the rubric can distinguish retrieval from reasoning;
- reasonable alternative decisions receive credit;
- critical failures are declared in advance;
- an assessor can apply the rubric without private context;
- the benchmark remains useful if the evaluated implementation technology changes completely;
- any public projection includes only appropriate external information;
- brand and website quality are plausible for the business rather than artificially impressive;
- generated public artefacts identify their benchmark and public-brand versions; and
- generated artefacts are not treated as canonical business truth.