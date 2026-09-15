# Repository Constitution

## Purpose

This repository exists to describe a believable fictional HVAC business independently of any later software implementation, benchmark, engineering methodology or technology choice.

## Principles

### 1. Business before solution

The repository describes what Frostline is, does, knows and experiences. It must not begin from an assumed software answer.

### 2. Reality before convenience

Business facts must be plausible for a growing UK HVAC contractor. Convenience for a demonstration, test or implementation is not sufficient justification for adding them.

### 3. No hidden traps

Operational complexity may exist, but it must arise naturally from the company's history, workforce, customers, contracts, assets and working practices. Facts must not be planted solely to catch out one delivery approach.

### 4. Preserve uncertainty

Where the business has not decided something, where records conflict, or where different people hold different understandings, that uncertainty must be represented rather than silently resolved.

### 5. Preserve perspective

Marketing, finance, sales, operations and engineering may describe the same business differently. Those perspectives may coexist provided the underlying facts remain reconcilable.

### 6. Public information is incomplete by nature

The public website and other outward-facing material should describe the company honestly, but they are not expected to expose its full operating model, internal constraints or commercial detail.

### 7. Every material fact needs provenance

Significant business facts should be explainable through the company's history, operating model, contractual position, workforce or commercial reality—not through the needs of a future experiment.

### 8. Changes must preserve coherence

A change to one part of the business must be reconciled with dependent facts elsewhere, including headcount, reporting lines, locations, services, customers, finances and working practices.

### 9. The business may be imperfect

Frostline may have duplicated records, informal practices, inconsistent terminology, legacy habits and key-person dependencies. These should be credible consequences of growth, not caricatures of incompetence.

### 10. The repository must stand alone

If every software-development artefact and experiment disappeared, this repository should still read as a coherent description of a real company.

## Benchmark boundary

Benchmarks may select, combine and test reasoning from Frostline's business facts, and may introduce case-specific events needed to create an evaluation. They do not become an alternative source of enduring business truth.

If a benchmark requires a policy, authority rule, state definition or stable company fact that is not present in the domain documents, that gap must be resolved in the business reference on its own merits before the benchmark depends on it. Benchmark convenience is never sufficient provenance.

The benchmark framework and reference implementations are documented under [`benchmarks/`](../../benchmarks/README.md).

## Companion governance documents

This constitution is supported by two operational governance documents:

- [Canonical terminology and record relationships](canonical-terminology-and-record-relationships.md) — defines precise meanings for recurring concepts and their structural relationships.
- [Decision rights and operational authority](decision-rights-and-operational-authority.md) — separates technical judgement, safety authority, customer authority and financial authority.

Domain documents should reference these where their content depends on the definitions or authority model.

## Quality test

The scenario succeeds when someone familiar with regional engineering contractors can reasonably say: "I have worked with companies like this."
