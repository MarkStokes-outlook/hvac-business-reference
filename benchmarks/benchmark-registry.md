# Benchmark Registry

This registry is the suite-level index of benchmark identity, status, ownership and dependency review. It is navigational and administrative; individual benchmark directories remain authoritative for their case, task, rubric and reference reasoning.

## Status meanings

- **draft** — under authoring or dry-run review; results are not comparable release results;
- **active** — approved for administered evaluation against its declared version and baseline;
- **review required** — a dependency or discovered ambiguity may materially affect validity;
- **superseded** — replaced by a newer benchmark while retained for result interpretation;
- **retired** — no longer suitable for new evaluation; reason must be recorded.

## Registry

| ID | Title | Version | Status | Primary capability | Baseline | Owner | Last dependency review |
|---|---|---:|---|---|---|---|---|
| [B001](B001-reactive-callout-triage-and-control/README.md) | Reactive Callout Triage and Control | 1.0.0 | draft — independent dry run required | Cross-domain operational decision control | `72d6a4bc4d2bab5d391e40f6c26470fc94521268` | Benchmark maintainers | 2026-08-02 |

## Registry rules

A benchmark must appear here before it is treated as part of the suite. Registry changes must accompany any change to benchmark ID, version, status, title, baseline, owner or dependency-review date.

The baseline identifies the repository state used for benchmark authoring and validation. It does not mean newer repository commits are automatically incompatible. After a material dependency change, the owner must either:

1. review the benchmark and update the dependency-review date;
2. revise the benchmark and increment its version; or
3. set its status to `review required` until the effect is resolved.

A benchmark marked `draft`, `review required`, `superseded` or `retired` must not be presented as an active current-suite result without clearly identifying that status.

## Suite coverage

The registry should eventually make capability concentration visible. New benchmarks should add meaningful coverage or test a distinct failure mode rather than duplicating an existing scenario with different names.

Current designed coverage:

| Reasoning class | Benchmarks |
|---|---|
| Retrieval | B001 (supporting, draft) |
| Interpretation | B001 (supporting, draft) |
| Cross-domain synthesis | B001 (primary, draft) |
| Decision control | B001 (primary, draft) |
| Operational planning | B001 (primary, draft) |
| Uncertainty handling | B001 (primary, draft) |
| Communication | B001 (supporting, draft) |

Coverage labels are descriptive, not scores. A benchmark's rubric determines what is actually evaluated.