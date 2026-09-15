# Benchmark Authoring Template

Use this template when creating a new benchmark. Replace every bracketed instruction. Delete guidance that is not part of the finished benchmark.

## Directory

```text
benchmarks/B###-stable-kebab-case-title/
├── README.md
├── case.md
├── task.md
├── rubric.md
├── reference-reasoning.md
└── public-brand/                         # optional
    └── brand-and-marketing-brief.md
```

## `README.md`

```markdown
# B### — [Benchmark title]

- Version: 1.0.0
- Status: draft
- Repository baseline: `[full commit SHA]`
- Primary reasoning classes: [classes from the framework taxonomy]
- Evaluated role: [role performed by the agent]
- Intended audience of output: [recipient or decision-maker]
- Benchmark owner: [maintaining role or named owner]
- Last dependency review: [YYYY-MM-DD]

## Capability under test

[State the capability and the failure mode this benchmark is intended to expose.]

## Authoritative dependencies

- [Document title](../../docs/path/to/document.md) — [relevant headings or governed concepts]

## Files

- [Case](case.md)
- [Task](task.md)
- [Rubric](rubric.md)
- [Reference reasoning](reference-reasoning.md)
- [Public brand and marketing brief](public-brand/brand-and-marketing-brief.md) — [include only when this benchmark owns public artefacts]

## Public projection and generated artefacts

[If applicable, explain that the benchmark owns a specific public projection, identify generated artefacts, and state that they are not canonical or automatically reusable by another benchmark.]

## Administration

[State supplied files, withheld files, permitted tools and repository access.]

## Known limitations

[State what the benchmark does not test.]
```

## `case.md`

```markdown
# Case

## Operating context

[Date, time, business context and decision horizon.]

## Supplied information

[Messages, records, observations and constraints visible to the evaluated agent.]

## Known facts

- [Fact explicitly established by the case.]

## Missing or disputed information

- [Material fact that remains unknown, conditional or disputed.]

## Resource and timing constraints

- [Availability, competence, asset, approval or deadline constraint.]
```

Do not include scoring hints, expected conclusions or assessor language in the case.

## `task.md`

```markdown
# Task

## Role

You are acting as [evaluated role].

## Required output

[Decision, plan, record or communication to produce.]

## Audience

[Who will use the output and for what decision.]

## Required structure

1. [Required section or field]
2. [Required section or field]

## Evidence requirements

[Citation granularity, permitted repository sources and treatment of assumptions.]

## Constraints

[External knowledge, tool, length and format constraints.]
```

## `rubric.md`

```markdown
# Rubric

- Total: 100 points
- Pass condition: [score and critical-failure condition]

## Scoring criteria

### 1. [Observable dimension] — [points]

- [points]: [observable behaviour]
- [points]: [observable behaviour]

Partial credit: [how incomplete evidence is scored].

## Critical failures and caps

| Failure | Effect |
|---|---|
| [Declared failure] | [automatic fail or score cap] |

## Defensible alternatives

[Describe control-preserving alternatives that receive credit.]

## Assessor cautions

[Common false positives, seductive but unsupported conclusions, or double-counting risks.]
```

Each point must be traceable to visible response content. Avoid criteria such as "shows good judgement" unless decomposed into observable decisions or controls.

Where the benchmark evaluates public artefact generation, score factual support, information-boundary discipline, marketing synthesis, benchmark-specific brand fidelity, realistic implementation quality and provenance. Do not reward publication of internal detail merely because it is canonically correct.

## `reference-reasoning.md`

```markdown
# Reference Reasoning

## Evidence map

| Issue | Authoritative evidence | Required interpretation |
|---|---|---|
| [Issue] | [document and heading] | [what the evidence establishes] |

## Material facts and uncertainty

- [Fact, uncertainty and consequence.]

## Reasoning path

1. [Evidence-backed reasoning step.]
2. [Evidence-backed reasoning step.]

## Minimum defensible conclusions

- [Conclusion every passing response must reach.]

## Acceptable alternatives

- [Alternative and the assumptions or controls that make it defensible.]

## Conclusions to reject

- [Unsupported, unsafe or semantically invalid conclusion.]

## Example response outline

[Optional structure demonstrating coverage without prescribing wording.]
```

## `public-brand/brand-and-marketing-brief.md`

Use this only when the benchmark includes a website or another public artefact.

```markdown
# B### Public Brand and Marketing Brief

## Status

- Benchmark: B### — [title]
- Public-brand version: 1.0.0
- Applies to: [website, brochure, social content or other artefacts]
- Business authority: repository documents under `docs/`

## Purpose

[Explain the benchmark-specific public projection and confirm that it does not redefine the business.]

## Public positioning

[Describe how the company should appear to external audiences.]

## Appropriate public themes

- [Supported business theme to emphasise.]

## Information that should remain internal

- [Internal knowledge that must not be exposed.]

## Brand character

[Define plausible identity, colour, typography, imagery and sophistication for the company and benchmark.]

## Expected implementation quality

[State what kind of real-world supplier, template or website-builder quality the artefact should resemble.]

## Marketing tone

[Define permitted simplification and prohibited unsupported claims.]

## Calls to action and contact data

[Define appropriate CTAs and how missing contact details must be handled.]

## Provenance treatment

[Define how the fictional and generated nature of the artefact is disclosed without disrupting the public journey.]

## Generation instruction

[Link to the reusable prompt and identify the canonical and benchmark-specific inputs.]
```

A public-brand brief may select and frame canonical information, but it cannot override or add enduring business facts. It belongs only to its benchmark unless another benchmark explicitly adopts and versions it.

## Release check

Before changing status from `draft` to `active`, complete the quality review checklist in the [benchmark specification](benchmark-specification.md), conduct at least one dry-run assessment, and confirm that another assessor can apply the rubric without private explanation.

For benchmarks with public artefacts, also confirm that:

- the public boundary excludes inappropriate internal knowledge;
- the public-brand version is recorded;
- generated artefacts are traceable to the benchmark, repository baseline and generation prompt; and
- the result is plausible for the fictional business rather than optimised merely to look impressive.