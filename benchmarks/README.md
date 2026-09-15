# Frostline Reasoning Benchmarks

## Purpose

This directory turns the Frostline business reference into a set of reproducible reasoning evaluations. The benchmarks test whether an agent can use the repository as evidence, preserve uncertainty, respect operational authority and produce a decision that could survive review by the people who run the business.

The benchmark layer does not redefine Frostline. Business truth remains owned by the documents under [`docs/`](../docs/). A benchmark selects and combines those facts into a controlled case. Where a benchmark conflicts with a domain document, the domain document wins and the benchmark must be corrected.

## What the benchmarks measure

The benchmark suite is intended to distinguish between an agent that merely retrieves relevant passages and one that can reason across them. A strong response should:

1. identify the material facts and unresolved evidence;
2. distinguish records, events, states and outcomes rather than collapsing them;
3. apply Frostline's canonical terminology consistently;
4. respect technical, safety, customer and financial authority boundaries;
5. identify the accountable owner, next action and dependency for open work;
6. avoid inventing customer approval, contract terms, technical findings or commercial authority;
7. explain which repository evidence supports each material conclusion; and
8. communicate a practical, reviewable course of action.

## Structure

```text
benchmarks/
├── README.md
├── benchmark-registry.md
├── framework/
│   ├── benchmark-specification.md
│   ├── benchmark-template.md
│   └── assessment-record-template.md
└── B001-reactive-callout-triage-and-control/
    ├── README.md
    ├── case.md
    ├── task.md
    ├── rubric.md
    ├── reference-reasoning.md
    └── public-brand/
        └── brand-and-marketing-brief.md
```

The separation is deliberate:

- the [benchmark registry](benchmark-registry.md) controls suite membership, status and dependency review;
- the [benchmark specification](framework/benchmark-specification.md) defines mandatory design and scoring rules;
- the [authoring template](framework/benchmark-template.md) provides the reusable file contract;
- the [assessment record template](framework/assessment-record-template.md) preserves scored-run provenance;
- `case.md` contains only the information supplied to the agent for the case;
- `task.md` defines the requested output and submission contract;
- `rubric.md` defines observable scoring criteria;
- `reference-reasoning.md` records the benchmark author's evidence-backed interpretation without requiring a single prescribed wording;
- `public-brand/` defines the benchmark-specific external projection used to generate websites and other public artefacts; and
- the benchmark `README.md` declares scope, dependencies, version, ownership and administration notes.

Future machine-readable fixtures may be added alongside these files, but Markdown remains the human-auditable source of truth.

## Benchmark classes

Benchmarks may test one or more reasoning classes:

- **retrieval** — locating authoritative evidence;
- **interpretation** — applying definitions and distinguishing similar concepts;
- **cross-domain synthesis** — reconciling facts owned by different documents;
- **decision control** — applying authority, release and escalation rules;
- **operational planning** — assigning ownership, next action and dependency;
- **uncertainty handling** — preserving missing, disputed or conditional information;
- **communication** — producing an actionable output for a stated audience.

A benchmark must state its primary classes. Scores should not reward confident prose that is unsupported by repository evidence.

## Evidence boundary

Unless a benchmark explicitly says otherwise, the permitted knowledge base is the repository at the benchmark's recorded baseline commit. General HVAC knowledge may be used only to interpret ordinary language; it must not be used to invent Frostline policy, customer entitlement, asset condition, contract coverage, delegated authority or historical facts.

Any assumption that materially changes the decision must be stated and treated as unresolved rather than silently promoted to fact.

## Public projections and generated artefacts

The complete repository is an internal business knowledge model. A public website should not expose all of that knowledge.

Each benchmark may therefore define its own public projection under `public-brand/`. That brief controls which supported facts are visible, how the company is positioned, what branding is plausible and what information must remain internal.

The derivation chain is:

```text
Canonical business knowledge
        ↓
Benchmark scenario and public-brand brief
        ↓
Generation assignment
        ↓
Benchmark-specific website or public artefact
```

A generated website is not canonical and does not automatically apply to another benchmark. Later benchmarks may represent a different brand, different public content, a redesigned website or a different stage of the fictional company's development.

The reusable generation assignment is [`prompts/website-generation.md`](../prompts/website-generation.md). It must be combined with the relevant benchmark's public-brand brief.

## Initial benchmark

[B001 — Reactive callout triage and control](B001-reactive-callout-triage-and-control/README.md) is the first reference implementation. It tests a deceptively ordinary service call that crosses contract interpretation, SLA handling, engineer competence, commercial authority, customer communication and next-action control.

It is intentionally not a trivia test. The case can only be handled well by combining evidence from several domains while refusing to close gaps that the case does not resolve.

B001 also defines the first Frostline public-brand projection. Its website should look like a credible regional HVAC contractor's mainstream brochure site, not an internal knowledge dump or an implausibly polished technology-company showcase.

## Adding a benchmark

New benchmarks must follow the [benchmark specification](framework/benchmark-specification.md) and should begin from the [authoring template](framework/benchmark-template.md). They should be created because they expose a material reasoning capability, ambiguity or failure mode—not merely to increase the benchmark count.

A new benchmark should be rejected or revised when:

- the answer is available from one obvious paragraph with no meaningful interpretation;
- success depends on undocumented industry knowledge;
- planted contradictions exist only to trick the agent;
- the rubric rewards a preferred software design rather than business reasoning;
- the case has no defensible evidence trail into `docs/`; or
- multiple reasonable decisions exist but the rubric recognises only one.

A benchmark becomes part of the active suite only when it is entered in the [registry](benchmark-registry.md), has completed a dry-run assessment and has an identified owner and dependency-review date.

## Running and recording an assessment

Administer the exact case and task declared by the benchmark. Do not expose the rubric or reference reasoning unless the protocol explicitly evaluates self-assessment. Record the evaluated system, tools, repository baseline, raw response and criterion-level scoring using the [assessment record template](framework/assessment-record-template.md).

Where a generated public artefact is supplied, also record its benchmark version, public-brand version, generation prompt, generating system and deployment or artefact reference.

Results from different benchmark versions, repository baselines, public-brand versions or materially different tool configurations must not be presented as directly comparable without disclosing those differences.

## Versioning and change control

Each benchmark records a semantic version and repository baseline. Increment:

- the **patch** version for wording or scoring clarification that does not change the task;
- the **minor** version when evidence, case facts or criteria change while preserving the benchmark's intent; and
- the **major** version when the capability being tested or submission contract changes materially.

Public-brand briefs carry their own version because a changed public projection may alter what an evaluated agent can observe or infer without changing the internal business model.

Changes to domain documents must trigger a review of dependent benchmarks. Benchmark evidence maps and public-brand briefs are dependencies, not copied truth. The registry must show benchmarks awaiting review rather than allowing silent drift.