# Benchmark Registry

This registry is the suite-level index of benchmark identity, status, ownership and dependency review. It is navigational and administrative; individual benchmark directories remain authoritative for their case, task, rubric and reference reasoning.

## Status meanings

- **staged** — coverage is frozen in outline but evidence maps and rubrics are not yet complete; no scored results;
- **draft** — under authoring or dry-run review; results are not comparable release results;
- **active** — approved for administered evaluation against its declared version and baseline;
- **review required** — a dependency or discovered ambiguity may materially affect validity;
- **superseded** — replaced by a newer benchmark while retained for result interpretation;
- **retired** — no longer suitable for new evaluation; reason must be recorded.

## Registry

| ID | Title | Version | Status | Primary capability | Baseline | Owner | Last dependency review |
|---|---|---:|---|---|---|---|---|
| [B001](B001-reactive-callout-triage-and-control/README.md) | Reactive Callout Triage and Control | 1.0.0 | draft — independent dry run required | Cross-domain operational decision control | `72d6a4bc4d2bab5d391e40f6c26470fc94521268` | Benchmark maintainers | 2026-08-02 |
| [Application V1](application-suite-v1.md) | Frostline Application Fit-for-Purpose Suite | 0.1.0 | staged — evidence authoring required | Complete-system semantic fitness | `82bb7c433481b0ea3dcd54df7a24022bc28c0802` | Benchmark maintainers | 2026-09-15 |

## Registry rules

A benchmark must appear here before it is treated as part of the suite. Registry changes must accompany any change to benchmark ID, version, status, title, baseline, owner or dependency-review date.

The baseline identifies the repository state used for benchmark authoring and validation. It does not mean newer repository commits are automatically incompatible. After a material dependency change, the owner must either:

1. review the benchmark and update the dependency-review date;
2. revise the benchmark and increment its version; or
3. set its status to `review required` until the effect is resolved.

A benchmark marked `staged`, `draft`, `review required`, `superseded` or `retired` must not be presented as an active current-suite result without clearly identifying that status.

## Suite coverage

The registry should eventually make capability concentration visible. New benchmarks should add meaningful coverage or test a distinct failure mode rather than duplicating an existing scenario with different names.

Current designed coverage:

| Reasoning class | Benchmarks |
|---|---|
| Retrieval | B001 (supporting, draft); Application V1 (supporting, staged) |
| Interpretation | B001 (supporting, draft); Application V1 (primary, staged) |
| Cross-domain synthesis | B001 (primary, draft); Application V1 (primary, staged) |
| Decision control | B001 (primary, draft); Application V1 (primary, staged) |
| Operational planning | B001 (primary, draft); Application V1 (primary, staged) |
| Uncertainty handling | B001 (primary, draft); Application V1 (primary, staged) |
| Communication | B001 (supporting, draft); Application V1 (supporting, staged) |
| Complete-system state integrity | Application V1 (primary, staged) |
| Authority/governance | Application V1 (primary, staged) |
| Product/software fitness | Application V1 (secondary, staged) |

Coverage labels are descriptive, not scores. A benchmark's rubric determines what is actually evaluated.