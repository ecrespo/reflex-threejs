# reflex-threejs — SDD Overview

This directory contains the **Spec-Driven Design (SDD)** artifacts for
`reflex-threejs`, a Reflex component library that wraps
[three.js](https://threejs.org) through
[React Three Fiber](https://r3f.docs.pmnd.rs/) and
[drei](https://github.com/pmndrs/drei).

In SDD, the specification — not the code — is the primary artifact. These
documents are written *before* and maintained *alongside* the implementation,
and live in the repository under version control.

## Reading order

| # | Document | Purpose |
|---|----------|---------|
| 01 | [Product Requirements (PRD)](01-prd.md) | What we build, for whom, and why |
| 02 | [Requirements & Specifications](02-requirements.md) | Functional / non-functional requirements, acceptance criteria |
| 03 | [Technical Design / Architecture](03-architecture.md) | How the wrapping works, key decisions |
| 04 | [Component Catalog (Data Model)](04-component-catalog.md) | The "schema" of components, tags and props |
| 05 | [Roadmap & Phases](05-roadmap-phases.md) | Delivery phases and milestones |
| 06 | [Implementation Plan](06-implementation-plan.md) | Phase-by-phase task tables and dependencies |
| 07 | [Task Breakdown](07-tasks.md) | Granular backlog with IDs |
| 08 | [Research Notes](08-research-notes.md) | Source findings on Reflex, three.js, R3F, drei |

## The SDD flow applied here

```
PRD (the What)
  → Requirements & Specs (the contract)
    → Technical Design (the How)
      → Component Catalog (the data model / schema)
        → Roadmap → Implementation Plan → Tasks
```

## Project at a glance

- **Goal:** let Reflex (pure-Python) developers build interactive 3D scenes
  without writing JavaScript, by exposing R3F/drei as idiomatic Reflex
  components.
- **Strategy:** wrap the React ecosystem rather than three.js directly. R3F is
  a React renderer for three.js; Reflex compiles to React; the two compose
  naturally.
- **First deliverable (this repo):** SDD artifacts, repository scaffold, a
  working core component set, and a multi-example demo app on `main`.

## Status

| Field | Value |
|-------|-------|
| Version | 0.1.0 |
| Stage | Alpha — foundation laid |
| Branch | `main` |
| Last updated | 2026-06-14 |
