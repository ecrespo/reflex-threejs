# reflex-threejs — Requirements & Specifications

| Field | Value |
|---|---|
| **Status** | `DRAFT` |
| **Version** | 1.0 |
| **Date** | 2026-06-14 |
| **Related PRD** | [01-prd.md](01-prd.md) |

This document refines the PRD into verifiable requirements. Each requirement
has an ID, a priority (`MUST` / `SHOULD` / `COULD` / `WONT`) and acceptance
criteria.

---

## 1. Functional Requirements

### RF-001 — Canvas root (`MUST`)
- **Description:** The library must provide a `Canvas` component that sets up the
  WebGL renderer, default scene, camera and render loop, rendered **client-side
  only**.
- **Acceptance criteria:**
  - [ ] `Canvas` subclasses `NoSSRComponent` (dynamic import, `ssr: false`).
  - [ ] Accepts `camera`, `shadows`, `dpr`, `gl`, `frameloop`, `orthographic`.
  - [ ] Defaults to fill its parent (`width/height: 100%`).
  - [ ] Children render inside the R3F scene graph.

### RF-002 — Host element primitives (`MUST`)
- **Description:** Provide declarative host elements for objects, geometries,
  materials, lights, cameras and helpers.
- **Acceptance criteria:**
  - [ ] Each host element renders as a bare lowercase JSX tag with **no import**.
  - [ ] Every element accepts `args` forwarded to the three.js constructor.
  - [ ] Object3D-like elements accept `position`, `rotation`, `scale`, `visible`.
  - [ ] Materials accept `color`, `opacity`, `transparent`, `wireframe`, `side`.
  - [ ] Lights accept `color`, `intensity` and light-specific props.

### RF-003 — Pointer interaction (`MUST`)
- **Description:** Meshes must expose pointer events mapped to Reflex handlers.
- **Acceptance criteria:**
  - [ ] `on_click`, `on_double_click`, `on_pointer_over`, `on_pointer_out`,
    `on_pointer_down`, `on_pointer_up`, `on_pointer_move`, `on_wheel` exist on `mesh`.
  - [ ] A handler bound to `on_click` fires a Reflex event and mutates state.

### RF-004 — State binding (`MUST`)
- **Description:** Any prop must accept a Reflex state Var.
- **Acceptance criteria:**
  - [ ] `mesh_standard_material(color=State.color)` recompiles to a bound prop.
  - [ ] Transform props accept Vars (`scale=rx.cond(...)`).

### RF-005 — drei helpers (`SHOULD`)
- **Description:** Provide wrappers for the most-used drei helpers.
- **Acceptance criteria:**
  - [ ] Controls: `OrbitControls`, `TrackballControls`, `MapControls`, `FlyControls`.
  - [ ] Staging: `Environment`, `Stage`, `ContactShadows`, `Sky`, `Stars`, `Grid`.
  - [ ] Abstractions: `Text`, `Html`, `Float`, `Center`, `Bounds`, `Edges`.
  - [ ] Loading: declarative `Gltf` for `.glb`/`.gltf` models.

### RF-006 — Namespace access (`SHOULD`)
- **Description:** Provide a `three` namespace mirroring `rx.*` ergonomics.
- **Acceptance criteria:**
  - [ ] `from reflex_threejs import three` exposes every factory.
  - [ ] drei helpers reachable via `three.drei.*` and common ones promoted.

### RF-007 — Demo coverage (`SHOULD`)
- **Description:** A demo app must showcase the breadth of the library.
- **Acceptance criteria:**
  - [ ] ≥ 9 routes, each a distinct three.js example category.
  - [ ] At least one interactive (event-driven) scene.

### RF-008 — Per-frame animation bridge (`COULD`, v0.2)
- **Description:** Expose R3F's `useFrame` loop to Python.
- **Acceptance criteria:** deferred to v0.2 (see roadmap).

## 2. Non-Functional Requirements

### Performance
- The 3D bundle must be code-split; pages without a `Canvas` must not load three.js.
- Instanced rendering available via `instancedMesh` for large object counts.

### Compatibility
- Primary target: Reflex ≥ 0.7 → React 19 → `@react-three/fiber@^9`, `@react-three/drei@^10`.
- Fallback documented for Reflex on React 18 → fiber `^8`, drei `^9`.
- `three >= 0.169` (no hard upper pin; R3F is renderer-version tolerant).

### Maintainability
- One module per element family (`geometries.py`, `materials.py`, ...).
- npm versions pinned centrally in `base.py`.
- ≥ 80% docstring coverage on public classes.

### Usability
- Naming = three.js/R3F names converted to `snake_case`, so the official
  three.js and R3F docs remain authoritative references.

### Reliability
- `Canvas` and any `window`/WebGL-touching component are `NoSSRComponent` to
  avoid SSR crashes.

## 3. Traceability Matrix

| Requirement | Design (03) | Catalog (04) | Demo scene |
|---|---|---|---|
| RF-001 | §3.2 Canvas | `Canvas` | all |
| RF-002 | §3.3 Host elements | geometries/materials/lights | Geometry Gallery, Materials |
| RF-003 | §3.4 Events | `mesh` events | Interactive |
| RF-004 | §3.5 State binding | props as Vars | Interactive |
| RF-005 | §3.6 drei | drei catalog | Staging, Text, Space |
| RF-006 | §3.7 Namespace | `three` | all |
| RF-007 | §4 | — | 9 scenes |

---

## Change History

| Version | Date | Author | Changes |
|---|---|---|---|
| 1.0 | 2026-06-14 | Ernesto Crespo | Initial version |
