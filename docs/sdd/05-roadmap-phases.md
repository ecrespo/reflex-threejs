# reflex-threejs — Roadmap & Phases

| Field | Value |
|---|---|
| **Status** | `DRAFT` |
| **Version** | 1.0 |
| **Date** | 2026-06-14 |

This roadmap sequences delivery into phases. Phase 0 and 1 are delivered in this
repository on `main`.

---

## Phase overview

```
Phase 0: Spec & Scaffold ──▶ Phase 1: Core + Demo ──▶ Phase 2: Packaging
                                                            │
                                                            ▼
        Phase 5: Physics ◀── Phase 4: Loaders/Assets ◀── Phase 3: Post-processing
```

## Phase 0 — Spec & Scaffold ✅ (this repo)
**Goal:** establish the methodology, architecture and repository base.
- SDD artifacts (PRD, requirements, architecture, catalog, plan, tasks).
- Repository layout, packaging metadata, `main` branch, README.
- **Done when:** repo compiles statically, SDD complete, README published.

## Phase 1 — Core Components + Demo ✅ (this repo)
**Goal:** a usable, declarative 3D library.
- `Canvas` (NoSSR) + all host element families.
- Pointer events + state binding.
- drei controls/staging/text/loader wrappers.
- `three` namespace.
- Demo app with ≥ 9 example scenes.
- **Done when:** demo compiles and every scene renders interactively.

## Phase 2 — Packaging & Distribution
**Goal:** make the library installable and discoverable.
- Build with `reflex component` tooling; `.pyi` stubs for IDEs.
- Publish `reflex-threejs` to PyPI.
- Versioned docs site / examples gallery.
- **Done when:** `pip install reflex-threejs` works; PyPI page live.

## Phase 3 — Post-processing & Effects
**Goal:** cinematic rendering.
- Wrap `@react-three/postprocessing` (`EffectComposer`, Bloom, DOF, SSAO,
  Outline, Vignette, Glitch).
- `useFrame` animation bridge (client-side) shipped in this phase or v0.2.
- **Done when:** a post-processing demo scene renders with Bloom + DOF.

## Phase 4 — Loaders & Asset Pipeline
**Goal:** robust model and texture loading.
- `useGLTF`/`useTexture`/`useFBX` ergonomic wrappers, draco/meshopt support.
- Asset bundling guidance and `Suspense`/loader-fallback patterns.
- **Done when:** a GLTF model with textures loads with a fallback spinner.

## Phase 5 — Physics & Interaction
**Goal:** simulation and advanced interaction.
- Wrap `@react-three/rapier` (rigid bodies, colliders, joints).
- Gizmos/transform controls, drag interactions.
- **Done when:** a physics demo (falling/colliding bodies) runs.

## Backlog / future
- WebGPU renderer; WebXR (VR/AR); instanced data-viz helpers; typed vector
  helpers and serializers; a high-level `model_viewer` recipe.

## Milestones

| Milestone | Phase | Version |
|---|---|---|
| `main` base + working demo | 0–1 | 0.1.0 |
| PyPI release | 2 | 0.2.0 |
| Post-processing + animation | 3 | 0.3.0 |
| Loaders/assets hardened | 4 | 0.4.0 |
| Physics | 5 | 0.5.0 |
| 1.0 (API stable) | — | 1.0.0 |

---

## Change History

| Version | Date | Author | Changes |
|---|---|---|---|
| 1.0 | 2026-06-14 | Ernesto Crespo | Initial version |
