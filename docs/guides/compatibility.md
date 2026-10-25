# Compatibility Guide

`reflex-threejs` wraps React Three Fiber (R3F) and drei, which are tied to a
React major version. Reflex bundles a specific React, so align the npm pins with
your Reflex version.

## Version matrix

| Reflex | React | `@react-three/fiber` | `@react-three/drei` | three | `reflex-threejs` |
|---|---|---|---|---|---|
| ≥ 0.10 (default) | 19.3 | `^9.8.2` | `^10.7.9` | `^0.186.1` | 0.3.x |
| 0.7 – 0.9 | 19 | `^9.8.2` | `^10.7.9` | `^0.186.1` | 0.2.x |
| 0.4 – 0.6 | 18 | `^8` | `^9` | `^0.169` | 0.2.x + pin override |

The library defaults to the **fiber v9 / drei v10 / React 19** line (top row).

## Runtime requirements (Reflex 0.10)

- **Python ≥ 3.11** — Reflex 0.10 dropped Python 3.10.
- **Node.js ≥ 22.22** — required by Reflex 0.10 (react-router 8) to build the
  frontend. CI uses Node 24 LTS.
- `rx.App(theme=...)` is deprecated since Reflex 0.9; configure the theme with
  `rx.plugins.RadixThemesPlugin(theme=rx.theme(...))` in `rxconfig.py` (see the
  demo app).
- The `reflex component` CLI was removed in Reflex 0.10. That only affects
  packaging; using `reflex-threejs` in an app is unchanged.

## Switching to the React 18 line

If your Reflex app runs on React 18, override the pinned versions before using
the components. The pins live in `reflex_threejs/base.py`:

```python
# base.py
FIBER_VERSION = "@react-three/fiber@^8.0.0"
DREI_VERSION = "@react-three/drei@^9.0.0"
THREE_VERSION = "three@^0.169.0"
```

You can also set them at runtime in your app's entry module before pages are
built, or fork and pin. A future release will expose these as configuration.

## Notes

- R3F has **no hard upper pin** on three.js; fiber 9 requires `three >= 0.156`
  and drei 10 `three >= 0.159`. We pin `^0.186.1` for a known-good baseline.
  three.js is still `0.x` and breaks APIs in minor releases, so `^0.186.1` only
  admits `0.186.x`; moving to a newer three.js is a deliberate bump.
- The React 18 row keeps `^0.169` as its tested baseline (fiber 8 accepts
  `three >= 0.133`, drei 9 `three >= 0.137`).
- Since three r182, `PCFSoftShadowMap` is deprecated in `WebGLRenderer` and
  `PCFShadowMap` is soft by default. `three.canvas(shadows=True)` still asks for
  `PCFSoftShadowMap` (R3F's default), so three logs a one-time
  `PCFSoftShadowMap has been removed. Using PCFShadowMap instead.` warning and
  falls back automatically. Pass `shadows="percentage"` to request
  `PCFShadowMap` directly and silence it.
- fiber 9.8.2 still drives its frame loop with `THREE.Clock`, which three
  r183+ deprecates in favour of `THREE.Timer`, so every page logs a one-time
  `THREE.Clock: This module has been deprecated` warning. It is harmless and
  will go away once R3F switches to `Timer`.
- three r176 renamed `CapsuleGeometry`'s second constructor argument from
  `length` to `height` (positional order unchanged) and added a fifth
  `heightSegments` argument.
- `Canvas` is a `NoSSRComponent`: it is dynamically imported with `ssr:false`, so
  three.js never runs during server rendering.
- If you see peer-dependency errors during `reflex init`/compile, they almost
  always mean the fiber/drei major does not match the bundled React — switch
  lines using the table above.
