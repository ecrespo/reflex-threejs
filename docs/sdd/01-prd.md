# reflex-threejs — Product Requirements Document (PRD)

| Field | Value |
|---|---|
| **Author** | Ernesto Crespo |
| **Status** | `DRAFT` |
| **Version** | 1.0 |
| **Date** | 2026-06-14 |
| **Reviewers** | TBD |
| **Last updated** | 2026-06-14 |

---

## 1. Executive Summary

`reflex-threejs` is a custom component library for [Reflex](https://reflex.dev)
that brings real-time 3D graphics to pure-Python web apps. It wraps
[React Three Fiber (R3F)](https://r3f.docs.pmnd.rs/) — the React renderer for
[three.js](https://threejs.org) — and its helper library
[drei](https://github.com/pmndrs/drei), exposing them as idiomatic Reflex
components.

It is for Python developers and data/AI teams who already build with Reflex and
want to add interactive 3D — product viewers, data visualization, simulations,
generative art, scientific scenes — without leaving Python or hand-writing
JavaScript/JSX. It solves the gap that Reflex ships no 3D primitive and that
wiring three.js by hand requires JavaScript expertise and an imperative render
loop.

## 2. Context and Problem

### 2.1 Current situation
Reflex compiles Python components to React and can wrap any React library.
three.js is the de-facto standard for web 3D, and R3F exposes it as declarative
React components. No maintained Reflex wrapper exists, so Reflex users must drop
to custom JavaScript to render 3D.

### 2.2 Problem
- three.js is imperative (create renderer, scene, camera, animation loop) and
  JS-only — a poor fit for Reflex's declarative, Python-first model.
- R3F makes three.js declarative but is React/JSX, still out of reach for a
  Python-only Reflex developer.
- three.js's official examples gallery (hundreds of demos across geometry,
  materials, lights, loaders, post-processing, etc.) has no Python equivalent.

### 2.3 Opportunity
By wrapping R3F + drei once, every three.js concept becomes available to the
entire Reflex community as Python. A single library can cover the majority of
the three.js example surface declaratively and ship reusable scenes.

## 3. Target Users

### Persona 1: Reflex Application Developer
- **Description:** Python developer building internal tools / dashboards in Reflex.
- **Main need:** drop a 3D viewer or visualization into a page with a few lines.
- **Usage frequency:** Weekly.
- **Technical level:** Medium (Python strong, JS limited).

### Persona 2: Data / AI Engineer
- **Description:** Builds ML demos and data apps in Python.
- **Main need:** 3D point clouds, embeddings, mesh/volume visualization bound to app state.
- **Usage frequency:** Eventual / per-project.
- **Technical level:** Medium-High in Python, low in graphics.

### Persona 3: Creative Technologist
- **Description:** Builds generative/interactive art and product showcases.
- **Main need:** expressive control over materials, lighting, post-processing.
- **Usage frequency:** Project-based.
- **Technical level:** High.

## 4. Objectives and Success Metrics

### 4.1 Product objectives

| Objective | Metric | Target | Horizon |
|---|---|---|---|
| Cover the core three.js surface | Wrapped element families (geometry, material, light, camera, helper, object) | 100% of common families | v0.1 |
| Idiomatic Python API | Example scenes written with zero hand-written JS | All demo scenes | v0.1 |
| Discoverable | Published to PyPI as `reflex-threejs` | Published | v0.2 |
| Breadth vs three.js examples | Demo scenes mapping to three.js example categories | ≥ 9 categories | v0.1 |

### 4.2 User objectives

| User objective | Indicator |
|---|---|
| Render a 3D scene without JS | A scene compiles from Python only |
| Bind 3D to app state | A state Var drives a material/transform and updates live |
| Handle 3D interaction | Click/hover on a mesh triggers a Reflex event handler |

## 5. Scope

### 5.1 In scope (v0.1)
- [x] `Canvas` root (NoSSR / dynamic import).
- [x] Object3D host elements: group, mesh, points, line, sprite, instancedMesh, primitive.
- [x] Geometry, material, light, camera and helper host elements.
- [x] drei wrappers: controls, environment/staging, text, HTML overlay, declarative GLTF.
- [x] `three` namespace for ergonomic access.
- [x] Demo app covering ≥ 9 example categories.
- [x] SDD artifacts and base documentation on `main`.

### 5.2 Out of scope (v0.1)
- Post-processing pipeline (`@react-three/postprocessing`) — planned v0.4.
- Physics (`@react-three/rapier` / cannon) — planned v0.6.
- A custom `useFrame` per-frame animation hook surfaced to Python — planned v0.2
  (v0.1 uses drei's animated materials and `autoRotate` for motion).
- XR / WebXR and WebGPU renderer — backlog.

### 5.3 Future considerations
- Typed `Vector3`/`Euler` Python helpers and serializers.
- A high-level `model_viewer` recipe component.
- Asset pipeline for bundling `.glb`/HDRI files with the app.

## 6. Functional Requirements
See [02-requirements.md](02-requirements.md) for the full list. Summary:

- **RF-001:** Provide a `Canvas` that initializes the renderer client-side only.
- **RF-002:** Provide declarative host elements for objects, geometries,
  materials, lights, cameras and helpers, accepting three.js constructor
  arguments via `args` and common parameters via named props.
- **RF-003:** Support pointer events (click, hover, move) on meshes mapped to
  Reflex event handlers.
- **RF-004:** Bind Reflex state Vars to any prop (color, position, scale, etc.).
- **RF-005:** Provide drei helpers for controls, environment, staging, text and
  model loading.

## 7. Non-Functional Requirements

- **Performance:** wrapping adds no runtime overhead beyond R3F; the `Canvas`
  is code-split so 3D bundles load only on pages that use it.
- **Compatibility:** target Reflex ≥ 0.10 (React 19.3, R3F v9; Python ≥ 3.11) since v0.3; v0.2.x covers Reflex 0.7–0.9. Document a
  React-18 / R3F-v8 fallback.
- **Maintainability:** one module per element family; pinned npm versions.
- **Usability:** API mirrors three.js/R3F naming converted to snake_case so the
  official docs remain a usable reference.
- **Documentation:** every public component carries a docstring; SDD lives in repo.

## 8. Constraints and Dependencies

### Technical constraints
- Must compile through Reflex's React pipeline (no direct DOM control).
- `Canvas` and anything touching `window`/WebGL must be `NoSSRComponent`.
- R3F host elements are intrinsic JSX tags valid only inside `<Canvas>`.

### External dependencies

| Dependency | Type | Owner | Status | Risk |
|---|---|---|---|---|
| reflex | Framework | Reflex | Stable | Low |
| @react-three/fiber | npm | pmndrs | Stable | Low |
| @react-three/drei | npm | pmndrs | Stable | Low |
| three | npm | three.js | Stable | Low |

## 9. User Stories

### Epic: Declarative 3D in Reflex
- **US-001:** As a Reflex dev, I want to render a lit, orbitable cube from
  Python so that I can prototype a 3D view quickly.
  - [x] A `Canvas` + `mesh` + geometry + material + light + controls compiles.
- **US-002:** As a data engineer, I want to bind a state Var to a material color
  so the scene reflects app state.
  - [x] `mesh_standard_material(color=State.color)` updates on event.
- **US-003:** As a creative dev, I want click/hover events on a mesh.
  - [x] `on_click` / `on_pointer_over` route to Reflex event handlers.

## 10. Risks and Mitigations

| Risk | Probability | Impact | Mitigation |
|---|---|---|---|
| React version drift between Reflex and R3F | Medium | High | Pin versions; document v8/v9 matrix |
| Host elements not emitting without import | Low | High | `library=None` base validated in scaffold |
| Per-frame animation needs custom JS hook | High | Medium | Ship drei animated materials in v0.1; `useFrame` bridge in v0.2 |

## 11. Timeline (indicative)

| Phase | Estimate | Deliverable |
|---|---|---|
| Spec & scaffold | done | SDD + repo base on `main` |
| Core components + demo | done (v0.1) | Working library + examples |
| Packaging & PyPI | 1 week | `reflex-threejs` on PyPI |
| Animation bridge | 1–2 weeks | `useFrame` event support |

---

## Change History

| Version | Date | Author | Changes |
|---|---|---|---|
| 1.0 | 2026-06-14 | Ernesto Crespo | Initial version |
