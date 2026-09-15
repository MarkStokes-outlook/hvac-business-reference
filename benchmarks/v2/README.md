# FrostLine fit-for-purpose Benchmark V2

Version **2.0.0**. Content-locked administration release, with independent administrator/evaluator calibration pending. No candidate application, source, screenshots, transcripts or evaluation results were inspected. V1 and canonical `docs/` remain unchanged.

V2 asks whether the application preserves FrostLine meaning and constraints, supports ordinary users, maintains coherent state and can credibly operate as business software. A competent operator's successful outcome is valuable evidence of Operational Fitness; it does not establish application enforcement or intuitive usability.

Start with [coverage](coverage.md), [administration](administration.md), [scoring](scoring-policy.md), [semantic methodology](semantic-fidelity.md), [evidence contract](evidence-contract.md), [gaps](evidence-gaps.md), [validation](validation-report.md) and [freeze checklist](freeze-checklist.md).

| Dimension | Evidence |
|---|---|
| OF — Operational Fitness | Existing frozen V1 result, separately attached without reinterpretation; otherwise not assessed. |
| BR — Business-Rule Resilience | R01–R17: deliberate wrong-action attempts and appropriately authorised continuation. |
| IU — Intuitive Usability | U01–U08: two fresh role-appropriate users/sessions per task, normal UI without application instructions. |
| SF — Semantic Fidelity / Application Hallucination | R scenario meanings plus S01 census and actively tested consequential concepts/defaults. |
| SI — State and Process Integrity | R repeated/interrupted/stale/concurrent workflows and T02 persisted restart consequences. |
| PT — Product and Technical Fitness | T01–T04: actual access boundaries, interruption/recovery, dirty/untrusted data and delivered operation/accessibility. |

**30 additional scenarios / 102 checkpoints**. V1 remains 27 scenarios / 270 operational checkpoints and is never added to a V2 arithmetic mean. Each new checkpoint scores one dimension; separate assertions can legitimately use shared observations. Public case facts and staged events are synthetic source evidence, not new enduring policy. The exact JSON oracle is the scoring contract; Markdown is its auditable view.

```text
v2/
  public/operator-contract.md
  scenarios/{R01..R17,U01..U08,T01..T04,S01}/
    public/{case.md,task.md,fixtures.json}
    hidden/{oracle.json,rubric.md,reference-reasoning.md,admin-events.json}
    README.md
  hidden/{evidence-index.json,scenario-source.json,evaluator-instructions.md}
  templates/{observation.json,assessment.json,adjudication.json,semantic-inventory.json,v1-attachment.json}
  tools/{benchmark.py,self_checks.py}
  suite-manifest.json
  release-lock.json
```

Never give operators or developers this complete checkout: hidden material is evaluator-only. Use the exporter, which supplies canonical business documents and the selected public task, but excludes suite metadata, oracles, events before release, tools and all other scenarios. Usability exports have their own instruction contract; no app help, source, APIs or setup guidance is supplied to the user.

```sh
python3 benchmarks/v2/tools/benchmark.py validate
python3 benchmarks/v2/tools/self_checks.py
python3 benchmarks/v2/tools/benchmark.py export --scenario R01 --dimension SI --destination /tmp/frostline-r01-state
python3 benchmarks/v2/tools/benchmark.py export --scenario U02 --destination /tmp/frostline-u02
python3 benchmarks/v2/tools/benchmark.py export --scenario R05 --stage 2 --destination /tmp/frostline-r05-event
python3 benchmarks/v2/tools/benchmark.py seal --record /tmp/run/observation.json --artifacts /tmp/run/artifacts --output /tmp/run/bundle.json
python3 benchmarks/v2/tools/benchmark.py check-bundle /tmp/run/bundle.json
python3 benchmarks/v2/tools/benchmark.py check-assessment /tmp/run/judge-a.json --bundle /tmp/run/bundle.json
python3 benchmarks/v2/tools/benchmark.py compare /tmp/run/judge-a.json /tmp/run/judge-b.json --bundle /tmp/run/bundle.json
python3 benchmarks/v2/tools/benchmark.py finalize --first /tmp/run/judge-a.json --second /tmp/run/judge-b.json --bundle /tmp/run/bundle.json --adjudication /tmp/run/adjudication.json --output /tmp/run/final.json
python3 benchmarks/v2/tools/benchmark.py scorecard /tmp/final-assessments --bundles /tmp/sealed-bundles
```

Run artefacts must live outside the locked suite/repository. `lock` intentionally creates a content fingerprint after authoring validation; it does not constitute independent calibration, human approval or production certification. This release can be administered as a labelled pilot now; claims of calibrated cross-methodology comparison require the remaining independent sign-off. No candidate evaluation is part of authoring.
