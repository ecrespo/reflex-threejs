# reflex-threejs — Implementation Plan

## Metadata

| Field | Value |
|---|---|
| **Author** | Ernesto Crespo |
| **Status** | `IN_PROGRESS` |
| **Version** | 1.0 |
| **Date** | 2026-06-14 |
| **PRD** | [01-prd.md](01-prd.md) |
| **Tech Design** | [03-architecture.md](03-architecture.md) |
| **Catalog** | [04-component-catalog.md](04-component-catalog.md) |

---

## 1. Implementation Summary

Five phases. Phases 1–2 (foundation + core) are delivered in this repository on
`main`; phases 3–5 are exposed as the API surface and demo, with packaging,
post-processing, loaders and physics following. The approach is "wrap R3F/drei,
one module per element family, verify by compiling the demo app."

**Total estimate (to v1.0):** ~8–10 weeks part-time.
**Team:** 1 maintainer (+ community).
**Target for v0.1 on `main`:** 2026-06-14 (done).

## 2. Pre-requisites

| Pre-requisite | Owner | Status | Due |
|---|---|---|---|
| SDD approved | Maintainer | ✅ Done | 2026-06-14 |
| Reflex ≥ 0.7 environment | Maintainer | ✅ | 2026-06-14 |
| Node/npm available to Reflex | Maintainer | ☐ (CI) | — |
| GitHub repository | Maintainer | ☐ | — |

## 3. Phases

### Phase 1 — Foundation & Scaffold ✅
**Objective:** repository, packaging, base classes.

| ID | Task | Est. | Dependency | Status |
|---|---|---|---|---|
| F1-01 | Repo layout + `custom_components` package | 0.5d | — | ✅ |
| F1-02 | `pyproject.toml`, LICENSE, .gitignore, CHANGELOG | 0.5d | F1-01 | ✅ |
| F1-03 | `base.py`: `ThreeProvider`, `ThreeElement`, pinned versions | 0.5d | F1-01 | ✅ |
| F1-04 | `Canvas` as `NoSSRComponent` | 0.5d | F1-03 | ✅ |
| F1-05 | SDD artifacts authored | 1d | — | ✅ |
| F1-06 | Git init on `main` | 0.1d | F1-02 | ✅ |

**Done criteria:** package syntax-compiles; SDD complete; README on `main`.

### Phase 2 — Core Components ✅
**Objective:** the full declarative host-element surface + drei.

| ID | Task | Est. | Dependency | Status |
|---|---|---|---|---|
| F2-01 | Objects (group, mesh, points, line, sprite, instanced, primitive) | 0.5d | F1-03 | ✅ |
| F2-02 | Geometry host elements | 0.5d | F1-03 | ✅ |
| F2-03 | Material host elements | 0.5d | F1-03 | ✅ |
| F2-04 | Light host elements | 0.3d | F1-03 | ✅ |
| F2-05 | Cameras + helpers (grid/axes/fog/color) | 0.3d | F1-03 | ✅ |
| F2-06 | drei wrappers (controls/staging/text/loader) | 0.7d | F1-03 | ✅ |
| F2-07 | `three` namespace + public API | 0.3d | F2-01…06 | ✅ |
| F2-08 | Pointer events on mesh | 0.2d | F2-01 | ✅ |

**Done criteria:** every catalog entry implemented; imports resolve.

### Phase 3 — Demo App ✅
**Objective:** prove breadth with runnable scenes.

| ID | Task | Est. | Dependency | Status |
|---|---|---|---|---|
| F3-01 | Demo project (`rxconfig`, app, state) | 0.3d | F2-07 | ✅ |
| F3-02 | Scenes: hello, geometries, materials, lights | 0.5d | F3-01 | ✅ |
| F3-03 | Scenes: interactive, particles | 0.4d | F3-02 | ✅ |
| F3-04 | Scenes: staging, text, space | 0.4d | F3-02 | ✅ |
| F3-05 | Shared layout + routing | 0.3d | F3-02 | ✅ |

**Done criteria:** ≥ 9 routes; one interactive scene; app compiles.

### Phase 4 — Verification & Packaging
**Objective:** quality gates and distribution.

| ID | Task | Est. | Dependency | Status |
|---|---|---|---|---|
| F4-01 | `ruff` + `py_compile` clean | 0.3d | F2-* | ✅ |
| F4-02 | Unit tests: component spec assertions | 1d | F2-07 | ✅ |
| F4-03 | Demo imports + registers 9 routes (`reflex export` needs Node) | 0.5d | F3-* | ✅ |
| F4-04 | GitHub Actions CI (lint+test matrix + package job) | 0.3d | F4-01 | ✅ |
| F4-05 | `python -m build` + `twine check` pass; PyPI publish pending | 0.5d | F4-02 | ⏳ |

**Done criteria:** CI green; distribution builds and passes `twine check`. PyPI
upload is the remaining manual, credentialed step.

**Bugs found and fixed during verification (TDD):**
- `Canvas` redeclared the inherited `style` prop, which dropped its default and
  crashed component construction on Reflex ≥ 0.9 (`'NoneType' is not a mapping`).
  Removed the redeclaration; the `create` override keeps the fill-parent default.
- `pyproject.toml` declared `Framework :: Reflex`, which is not a valid PyPI
  trove classifier and blocked `python -m build`. Removed it.

### Phase 5 — Effects, Loaders, Physics
See [roadmap](05-roadmap-phases.md) phases 3–5. Tracked as epics post-v0.1.

## 4. Dependency map

```
Phase 1: Foundation
  └─▶ Phase 2: Core ──▶ Phase 3: Demo ──▶ Phase 4: Verify & Package
                                              └─▶ Phase 5: Effects/Loaders/Physics
```

## 5. Implementation risks

| Risk | Prob. | Impact | Mitigation | Owner |
|---|---|---|---|---|
| Reflex/React/R3F version mismatch | Med | High | Pin versions; compatibility guide; CI matrix | Maintainer |
| `bufferAttribute` array passing across the bridge | Med | Med | Document typed-array pattern; provide helper later | Maintainer |
| Per-frame animation expectations | High | Med | Ship drei animation now; `useFrame` bridge in Phase 3 | Maintainer |

## 6. Global Definition of Done

- [ ] Code merged to `main`.
- [x] `py_compile` + `ruff` pass.
- [x] Demo app imports and registers all routes (full Reflex export needs Node).
- [x] Public components documented (docstrings + catalog).
- [x] SDD updated if the API changed.

---

## Change History

| Version | Date | Author | Changes |
|---|---|---|---|
| 1.0 | 2026-06-14 | Ernesto Crespo | Initial version |
