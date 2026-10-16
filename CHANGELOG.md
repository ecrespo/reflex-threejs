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

### Added
- Initial project scaffold, SDD artifacts and base documentation.
- Core component library: `Canvas` (NoSSR), Object3D host elements
  (group, mesh, points, line, sprite, instancedMesh, primitive).
- Full geometry, material, light, camera and helper host elements.
- `@react-three/drei` wrappers: controls, environment, staging, text,
  HTML overlay, and declarative GLTF loading.
- `three` namespace for ergonomic `rx`-style access.
- Demo application with multiple interactive examples.

## [0.1.0] - 2026-06-14
- Project bootstrapped on the `main` branch.
