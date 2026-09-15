# Benchmark Assessment Record

Create one copy of this record for each scored run. Store completed records outside the benchmark definition unless a dedicated results area has been approved.

## Run identity

- Assessment ID: `[unique run identifier]`
- Benchmark: `[B###]`
- Benchmark version: `[x.y.z]`
- Repository baseline: `[full commit SHA]`
- Evaluation date and time: `[ISO 8601]`
- Assessor: `[name or stable identifier]`
- Assessment method: `[human, panel, automated, hybrid]`

## Evaluated system

- Agent or model: `[name and version]`
- Provider or runtime: `[where relevant]`
- System instructions or profile: `[reference or hash]`
- Tool access: `[repository search, filesystem, web, none, other]`
- Context supplied: `[files, branch, commit and exclusions]`
- Sampling or generation settings: `[temperature, seed or equivalent where known]`
- Execution notes: `[timeouts, retries, truncation, tool failure or intervention]`

Unknown configuration must be recorded as unknown rather than omitted.

## Submission

Preserve the raw response exactly as evaluated.

```text
[raw response]
```

Where the response includes tool calls, attach or reference the complete trace and identify which content was visible to the final decision-maker.

## Criterion scoring

| Criterion | Available | Awarded | Response evidence | Assessor rationale |
|---|---:|---:|---|---|
| [criterion name] | [points] | [points] | [quotation or location] | [brief explanation] |

- Raw score: `[number] / [total]`
- Critical failures identified: `[none or declared failures]`
- Cap applied: `[none or cap and reason]`
- Final score: `[number] / [total]`
- Performance band: `[band]`
- Pass result: `[pass/fail]`

## Material strengths

- [Evidence-backed strength relevant to the benchmark capability.]

## Material weaknesses

- [Evidence-backed omission, unsupported conclusion or control failure.]

## Assessor judgement

- Confidence: `[high, medium, low]`
- Ambiguous rubric points: `[none or details]`
- Alternative interpretation considered: `[details]`
- Second review required: `[yes/no and reason]`

## Reproducibility

Record enough information for another evaluator to understand what was tested and why the score was awarded.

- Benchmark files verified against declared version: `[yes/no]`
- Repository baseline available: `[yes/no]`
- Raw trace retained: `[yes/no]`
- Assessment artefacts location: `[stable reference]`
- Known reproducibility limits: `[details]`

## Follow-up classification

Assessment findings must be classified rather than immediately changing a benchmark:

- **evaluated-system failure** — the response failed despite a valid case and rubric;
- **benchmark ambiguity** — wording or scoring permits materially inconsistent assessment;
- **repository gap** — the business reference does not provide enough authority to resolve the case;
- **dependency drift** — repository changes have altered the benchmark's assumptions;
- **administration failure** — incorrect files, tools, baseline or configuration were supplied.

Any proposed benchmark or repository change should identify this classification and preserve the original run record.