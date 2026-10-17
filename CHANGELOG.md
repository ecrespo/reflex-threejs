# Changelog

All notable changes to this project are documented here. The format is based on
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project
adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Changed
- Bumped npm pins in `base.py`: `three` `^0.169.0` → `^0.186.1`,
  `@react-three/fiber` `^9.0.0` → `^9.8.2`, `@react-three/drei` `^10.0.0` →
  `^10.7.9`. Note: with three r182+ `Canvas(shadows=True)` logs a one-time
  `PCFSoftShadowMap` deprecation warning and falls back to the (now soft)
  `PCFShadowMap`; use `shadows="percentage"` to avoid it. `capsule_geometry`
  docs updated for three r176 (`length` → `height`, new `heightSegments`).
- Demo: `/lights` and `/staging` use `shadows="percentage"` (no deprecation
  warning on three r186); `reflex.lock` regenerated against three 0.186.1,
  fiber 9.8.2 and drei 10.7.9. `/particles` drops the redundant `array`/`count`/
  `item_size` props.

### Fixed
- `buffer_attribute` now wraps `args[0]` and `array` (literal lists or state
  Vars) in `new Float32Array(...)`. three.js throws `BufferAttribute: array
  should be a Typed Array` on plain arrays, which left the demo `/particles`
  scene blank (also on three 0.169).
- `scripts/gen_pyi.py` runs the stub generator from `custom_components`, so it
  imports `reflex_threejs.*` and actually rewrites the stubs. Before, every
  import failed silently and the CI "stubs up to date" gate passed vacuously.
- `drei.float` is served by a module `__getattr__` instead of rebinding the
  builtin `float` in `drei.py`, which made `float | list[float]` annotations
  resolve to a method and crashed stub generation intermittently (depending on
  the hash seed). `three.drei.float(...)` keeps working.

## [0.1.0] - 2026-06-15

First release on PyPI: <https://pypi.org/project/reflex-threejs/0.1.0/>.
Install with `pip install reflex-threejs` or `uv add reflex-threejs`.

### Added
- Initial project scaffold, SDD artifacts and base documentation.
- Core component library: `Canvas` (NoSSR), Object3D host elements
  (group, mesh, points, line, sprite, instancedMesh, primitive).
- Full geometry, material, light, camera and helper host elements.
- `@react-three/drei` wrappers: controls, environment, staging, text,
  HTML overlay, and declarative GLTF loading.
- `three` namespace for ergonomic `rx`-style access.
- Demo application with multiple interactive examples.
- Verification suite (Phase 4): 194 tests — full catalog contract coverage
  (`tests/test_catalog.py`) plus quality gates for ruff, byte-compile, demo
  routing and packaging metadata (`tests/test_quality_gates.py`).
- CI `package` job building the wheel/sdist and running `twine check`.
- Packaged as a standard Reflex custom component: generated `.pyi` type stubs and
  a PEP 561 `py.typed` marker (shipped in the wheel), `scripts/gen_pyi.py` to
  regenerate them, a `Makefile` (`install`/`stubs`/`check`/`build`/`publish`), and
  the `reflex-custom-components` keyword. CI rebuilds and diffs the stubs.

### Fixed
- Host elements now actually render. On Reflex's React compiler they were emitted
  as bare identifiers (`jsx(mesh, …)`) instead of string intrinsics
  (`jsx("mesh", …)`), so every scene crashed in the browser with
  `ReferenceError: <tag> is not defined`. Fixed by marking `ThreeElement` with
  `_is_tag_in_global_scope`.
- `Canvas` no longer crashes on Reflex ≥ 0.9: it had redeclared the inherited
  `style` prop, dropping its default and breaking the style merge.
- Removed the invalid `Framework :: Reflex` trove classifier that blocked
  `python -m build`.
- Lint clean-up: dropped unused imports, sorted import blocks, and added the
  missing docstrings flagged by `ruff` across the package and demo.

## [0.1.0-scaffold] - 2026-06-14
- Project bootstrapped on the `main` branch.
