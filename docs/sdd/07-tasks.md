# reflex-threejs — Task Backlog

Granular, ID'd tasks derived from the [implementation plan](06-implementation-plan.md).
Legend: ✅ done · ⏳ in progress · ☐ todo.

---

## Epic A — Foundation (Phase 1)
- A-01 ✅ Create repository structure and `custom_components/reflex_threejs` package.
- A-02 ✅ Add `pyproject.toml` with build metadata and ruff config.
- A-03 ✅ Add LICENSE (MIT), `.gitignore`, `CHANGELOG.md`.
- A-04 ✅ Implement `base.py` (`ThreeProvider`, `ThreeElement`, pinned versions, typing).
- A-05 ✅ Implement `Canvas` as `NoSSRComponent`.
- A-06 ✅ Initialize git on `main`.

## Epic B — Core host elements (Phase 2)
- B-01 ✅ `objects.py`: group, mesh, points, line(+segments/loop), sprite, instancedMesh, primitive.
- B-02 ✅ `geometries.py`: 22 geometry elements + bufferGeometry/bufferAttribute.
- B-03 ✅ `materials.py`: 14 material elements incl. shaderMaterial.
- B-04 ✅ `lights.py`: 6 light elements.
- B-05 ✅ `cameras.py`: perspective/orthographic cameras, grid/axes/box helpers, fog, color.
- B-06 ✅ Mesh pointer events (`on_click`, `on_pointer_over`, …).

## Epic C — drei layer (Phase 2)
- C-01 ✅ Controls: Orbit, Trackball, Fly, Map.
- C-02 ✅ Cameras with `make_default`.
- C-03 ✅ Staging: Environment, Stage, ContactShadows, Sky, Stars, Cloud, Grid.
- C-04 ✅ Abstractions: Text, Text3D, Html, Billboard, Float, Center, Bounds, Edges, Outlines, Wireframe, GradientTexture.
- C-05 ✅ Animated materials: MeshDistortMaterial, MeshWobbleMaterial.
- C-06 ✅ Declarative `Gltf` loader.

## Epic D — Public API (Phase 2)
- D-01 ✅ `namespace.py` `three` SimpleNamespace.
- D-02 ✅ `__init__.py` flat exports + `__all__` + `__version__`.

## Epic E — Demo app (Phase 3)
- E-01 ✅ Demo project scaffold (`rxconfig.py`, app module, `state.py`).
- E-02 ✅ Scene: Hello Cube.
- E-03 ✅ Scene: Geometry Gallery.
- E-04 ✅ Scene: Materials.
- E-05 ✅ Scene: Lights (+ shadows).
- E-06 ✅ Scene: Interactive (click/hover → state).
- E-07 ✅ Scene: Particles (points + bufferGeometry).
- E-08 ✅ Scene: Staging & drei.
- E-09 ✅ Scene: 3D Text.
- E-10 ✅ Scene: Space (stars).
- E-11 ✅ Shared layout + multi-route registration.

## Epic F — Verification & packaging (Phase 4)
- F-01 ✅ `py_compile` + `ruff` clean across all modules (whole repo passes).
- F-02 ✅ Unit tests asserting tag/library/props per component (`tests/test_catalog.py`,
  114 parametrized cases covering every catalog row + prop surfaces).
- F-03 ✅ Demo app imports and registers all 9 scene routes
  (`tests/test_quality_gates.py::test_demo_app_imports_with_nine_routes`). A full
  `reflex export` additionally needs Node/bun + network to build the frontend.
- F-04 ✅ GitHub Actions CI: `lint-and-test` (ruff + py_compile + pytest, py3.10–3.12)
  and a `package` job (`python -m build` + `twine check`).
- F-05 ⏳ Distribution **build validated** as a Reflex custom component: `.pyi` type
  stubs + `py.typed` generated (`scripts/gen_pyi.py`, mirrors `reflex component
  build`) and shipped in the wheel; `python -m build` + `twine check` pass; CI
  rebuilds and diffs the stubs. PyPI upload itself remains a manual, credentialed
  step (`make publish` / `twine upload`).

## Epic G — Documentation
- G-01 ✅ SDD artifacts (this directory).
- G-02 ✅ README with quickstart and examples.
- G-03 ✅ Compatibility guide (React 18/19, R3F v8/v9).
- G-04 ✅ Usage guide (host elements, events, state binding).
- G-05 ☐ Per-scene annotated walkthroughs.

## Epic H — Post-v0.1 (Phases 3–5, roadmap)
- H-01 ☐ `useFrame` client-side animation bridge.
- H-02 ☐ `@react-three/postprocessing` wrappers (Bloom, DOF, SSAO…).
- H-03 ☐ Loader hooks (`useTexture`, `useFBX`) + `Suspense` fallbacks.
- H-04 ☐ `@react-three/rapier` physics wrappers.
- H-05 ☐ Typed `Vector3`/`Euler` helpers + serializers.

---

## Summary

| Epic | Done | Total |
|---|---|---|
| A Foundation | 6 | 6 |
| B Core host | 6 | 6 |
| C drei | 6 | 6 |
| D Public API | 2 | 2 |
| E Demo | 11 | 11 |
| F Verify/Package | 4 | 5 |
| G Docs | 4 | 5 |
| H Post-v0.1 | 0 | 5 |
