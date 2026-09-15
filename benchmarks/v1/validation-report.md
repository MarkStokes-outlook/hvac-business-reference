# V1 authoring validation report

Date: 2026-09-15. Canonical baseline: `e61e7c4199aeafb0d232f8fb1f31c1eb61ec10a2`. Method: local author review plus deterministic standard-library administration checks. **No candidate application or independent evaluator model was used.**

## Content and evidence checks

- 27 scenario IDs B001–B027, with B001 2.0.0 lineage retained and B002–B027 1.0.0.
- 270 independently scored semantic checkpoints; five 20-point groups/100 primary points per scenario, 2,700 total available primary points. Every checkpoint and declared critical/prohibited outcome maps to canonical section IDs. Alternatives/uncertainties retain canonical dependency maps.
- 217 evidence sections checked against actual path, exact heading, source lines, full section text and SHA-256. All 37 canonical Markdown documents are pinned; Finder `.DS_Store` metadata is excluded from canonical authority/export.
- Required public/hidden files, JSON/Markdown fixture equality, rubric/oracle/reference consistency, source dependencies and later-stage completeness checked.
- 620 local Markdown links checked against proposed installed paths; no broken links. Two dated October fixture day/window checks passed.
- Manual business review checked source support, non-equivalence of completion events, scope/cost authority separation, preservation of outstanding obligations and stock/evidence custody, alternatives, and unknown-policy boundaries. Found and corrected an initially stage-inappropriate B019 audit checkpoint and clarified B005 critical-failure wording before freezing.

## Administration and scoring checks

**85 local smoke checks passed.** Reproduce with:

```sh
python3 .daemoncore/outbox/frostline-benchmark-v1/benchmarks/v1/tools/benchmark.py validate --repo .
python3 .daemoncore/outbox/frostline-benchmark-v1/benchmarks/v1/tools/smoke_checks.py .
```

The checks cover the exact candidate allowlist and absence of hidden/metadata/later-stage files for all 30 exported stages; stale and symlink destinations; forbidden repository output; undeclared stages; canonical document drift before any export; frozen-release tampering; all-checkpoint scores; stage-history critical failure/raw score/cap; score and critical disagreements on identical bundles; rejection of non-comparable bundles, undeclared failures, duplicate/missing checkpoints, unevidenced scores, unknown policy IDs and invalid score values; incomplete/unresolved judgement; and full-suite aggregation with failed/missing/pending/duplicated scenarios.

The synthetic early-charge scoring fixture has raw 60/effective 59 with B019-CF1. Contradicted controls earn zero, rather than partial credit for a later request mentioning the missing approval. Synthetic all-100 final records produce the scoped verdict; replacing B019 with that critical event leaves mean above 95 yet produces a material-business-gaps verdict. Missing B027 or pending independent adjudication withholds the suite verdict. These are arithmetic/administration fixtures, not claimed real-world candidate results.

## Freeze and practical limits

`release-lock.json` records the exact final file hashes/fingerprint; default validation and export reject changed content. All export/scoring checks passed after the final authoring changes. Tool syntax/help commands were checked, and repository-tracked benchmark/domain files were not changed during this draft pass. The outbox is ignored by the existing repository `.gitignore`.

Local structural/calculation/export checks and synthetic author calibration anchors cannot establish independent assessor agreement, actual app operation, production safety/reliability or empirical threshold validity. Independent calibration and installation approval remain explicitly pending under `freeze-checklist.md` and the project instructions. Pilot administration can use this locked content and must retain that status in reported results. Canonical gaps and the complaint/reporting definition conflict are disclosed in `evidence-gaps.md`.
