# FrostLine fit-for-purpose Benchmark V1

Version 1.0.0 · 27 scenarios · canonical baseline `e61e7c4199aeafb0d232f8fb1f31c1eb61ec10a2` · dependency review 2026-09-15 · owner: Benchmark maintainers.

**Authoring complete, frozen review candidate.** The release can be administered as a labelled pilot. Installation requires the project approval described in the outbox proposal. Comparable approved-release results additionally require independent administrator/evaluator calibration and the sign-off in `freeze-checklist.md`. No candidate application has been inspected or assumed, and no candidate performance or independent model validation is claimed.

The primary question is whether FrostLine could correctly and safely operate its business using the application. The suite tests business outcomes against canonical `docs/`, with ordinary successful work as well as situations requiring clarification, bounded action, refusal, escalation or inaction. It evaluates an application used by authorised people; it does not assume autonomous software, AI, a UI, a technology, a database model or an internal workflow design.

Start with [coverage](coverage.md), [administration protocol](administration-protocol.md), [scoring](scoring-policy.md), [evidence gaps](evidence-gaps.md) and [framework supplement](framework-supplement.md). `suite-manifest.json` fixes IDs, versions, dependencies and document hashes. `release-lock.json` fixes this review candidate's exact files.

## Structure and separation

```text
v1/
  submission-contract.md          common candidate instructions
  scenarios/B###-title/
    README.md                     administrator metadata
    public/case.md                initial episode only
    public/fixtures.json           same initial facts with neutral references
    public/task.md                 scenario request
    hidden/oracle.json             semantic checkpoints and failures
    hidden/rubric.md               human-readable scoring
    hidden/reference-reasoning.md  canonical evidence map and alternatives
    hidden/admin-events.json       neutral later inputs for staged episodes
  hidden/evidence-index.json       exact canonical sections/lines/hashes
  hidden/evaluator-instructions.md
  templates/                     observation and assessment contracts
  tools/                         standard-library administration utilities
```

Never give a candidate the full checkout containing this suite's hidden material. Use the allowlist exporter. The candidate gets **all canonical `docs/`**, common instructions and the selected public scenario files; it does not get oracle, rubric, reasoning, suite metadata, tooling, later stages, assessment examples or legacy B001 references. Later event facts are supplied only at their declared stage boundary.

Fixture contracts, events, amounts and individual assignments are explicit synthetic episode facts permitted by the repository constitution; they are not enduring FrostLine policies. Canonical policy remains external. Technical tests are administered source evidence, not tasks requiring invented physical diagnosis. Numbered fixture statements and observation templates are interchange aids, not an application schema.

## Run commands

From the repository root, after installation:

```sh
python3 benchmarks/v1/tools/benchmark.py validate --repo .
python3 benchmarks/v1/tools/benchmark.py export --repo . --scenario B002 --stage 1 --destination /tmp/frostline-b002-input
python3 benchmarks/v1/tools/benchmark.py export --repo . --scenario B002 --stage 2 --destination /tmp/frostline-b002-next-event
python3 benchmarks/v1/tools/benchmark.py check-assessment /tmp/assessor-a.json
python3 benchmarks/v1/tools/benchmark.py compare /tmp/assessor-a.json /tmp/assessor-b.json
python3 benchmarks/v1/tools/benchmark.py aggregate /tmp/final-assessments
```

While reviewing the draft, replace `benchmarks/v1` in the command path with `.daemoncore/outbox/frostline-benchmark-v1/benchmarks/v1`. Keep run inputs, outputs and assessment records outside the frozen suite. Export destinations must be absent or empty and cannot be the repository, the suite or a directory inside them. The exporter validates canonical and release hashes before creating candidate files. Stage 2 export contains only neutral later event facts and common instructions; apply it to the same scenario's existing state.

## V1 limits

A controlled pilot establishes bounded demonstrated fitness across these scenarios, not complete production certification. The suite does not simulate physical engineering, establish new legal requirements, test every service variant, measure long-run reliability or prove adoption under actual workload. Exact financial delegations, certain retention rules and some KPI boundaries are not supplied by `docs/`; [gaps](evidence-gaps.md) explains where a case supplies explicit authority or where uncertainty must remain. Secondary product/engineering observations are reported separately and cannot offset business failures.

B001 version 2.0.0 preserves the existing reactive-callout intent and initial episode; its major submission/scoring change makes old B001 1.0.0 scores non-comparable. Its legacy website and public-brand projection are not V1 input or business authority. Other identifiers B002–B027 introduce distinct episodes; no IDs are retired/reused here.
