# reflex-threejs — Research Notes

Source findings that informed the design. Captured 2026-06-14.

---

## 1. Reflex — wrapping React components

From the official Reflex docs (`reflex.dev/docs/wrapping-react/*`):

- A wrapped component subclasses `rx.Component` or `rx.NoSSRComponent`.
- Key attributes:
  - `library` — npm package name (pin a version: `"pkg@x.y.z"`).
  - `tag` — exported component name to import.
  - `alias` — optional import alias (avoid name clashes).
  - `lib_dependencies` — extra npm packages needed but not directly imported.
  - `is_default` — `True` if the component is a default export.
- Props are typed `rx.Var[...]`. Custom dict-like prop types use `TypedDict`
  (verbatim keys) or `rx.PropsBase` (auto camelCase).
- Event handlers are `rx.EventHandler[spec]`. Built-in specs:
  `rx.event.no_args_event_spec`, `rx.event.passthrough_event_spec(T)`,
  `rx.event.input_event`, `rx.event.key_event`; custom specs map/transform the
  JS event payload before it reaches the Python handler.
- Custom code / imports: `_get_custom_code()` (e.g. import a CSS file) and
  `add_custom_code()` (inject JS functions). `create()` can override
  construction to transform props.
- **NoSSR:** components that touch `window`/WebGL must subclass
  `NoSSRComponent`; the docs explicitly list **3D graphics** among the cases
  that require dynamic import (`ssr:false`). This drives our `Canvas` design.
- Custom components are scaffolded/published via the `reflex component` CLI;
  PyPI packages are conventionally prefixed `reflex-`.

**Implication:** `Canvas` → `NoSSRComponent`; host elements → components with
`library=None` so Reflex emits the bare lowercase JSX tag with no import.

## 2. three.js

- The de-facto WebGL 3D engine. Imperative core: `WebGLRenderer`, `Scene`,
  `Camera`, geometries, materials, lights, an animation loop, raycasting for
  interaction, loaders (GLTF/OBJ/FBX…), and post-processing (`EffectComposer`).
- The official `threejs.org/examples` gallery is organized by category:
  animation, camera, controls, geometry, helpers, lights, loaders, materials,
  objects, modifiers, physics, post-processing, raycast, shadows, sprites,
  water/sky, and newer WebGPU/TSL demos. The repo (`mrdoob/three.js`) hosts the
  `examples/` sources and `src/` engine.
- Our catalog mirrors these families so the official examples remain a usable
  reference for what each Python factory does.

## 3. React Three Fiber (R3F)

- A React renderer for three.js (`@react-three/fiber`). Inside `<Canvas>` it runs
  a custom reconciler that maps **lowercase intrinsic JSX tags** to three.js
  classes: `<mesh>`, `<boxGeometry>`, `<meshStandardMaterial>`, `<ambientLight>`.
- Conventions used by our wrapper:
  - `args={[...]}` → constructor arguments of the underlying three.js class.
  - `position`/`rotation`/`scale` accept a scalar or a 3-tuple.
  - Child geometry/material auto-attach to the parent mesh; other slots use
    `attach="..."` (e.g. `attach="background"`, `attach="attributes-position"`).
  - Pointer events (`onClick`, `onPointerOver`…) are raycasted by R3F.
- **Versions (June 2026):** `@react-three/fiber` latest **9.6.x**;
  `@react-three/drei` latest **10.7.x**. Fiber **v9 ↔ React 19**, fiber **v8 ↔
  React 18**. No hard three.js pin; requires `three >= 0.156` (we pin
  `^0.169`).
- **Update (October 2026):** pins raised to `@react-three/fiber@^9.8.2`,
  `@react-three/drei@^10.7.9` and `three@^0.186.1` (r169 → r186 migration
  notes reviewed; no wrapped API removed).

**Implication:** default to fiber v9 / drei v10 / React 19 (Reflex ≥ 0.7), with
a documented v8/React-18 fallback.

## 4. drei

- `@react-three/drei`: official helpers on top of R3F. We wrap the highest-value
  set: controls (Orbit/Trackball/Map/Fly), cameras with `makeDefault`, staging
  (`Environment`, `Stage`, `ContactShadows`, `Sky`, `Stars`, `Grid`),
  abstractions (`Text`, `Html`, `Float`, `Center`, `Bounds`, `Edges`),
  animated materials (`MeshDistortMaterial`, `MeshWobbleMaterial`) and a
  declarative `Gltf` loader (wraps `useGLTF`).

## 5. Design consequences

1. Wrap **R3F + drei**, not three.js directly (declarative, matches Reflex).
2. `Canvas` is the single `NoSSRComponent`; everything else nests inside it.
3. Host elements are `library=None` components emitting bare JSX tags.
4. State binds through normal `rx.Var` props; interaction through
   `rx.EventHandler` props on meshes.
5. v0.1 animation via drei + `autoRotate`; a client-side `useFrame` bridge is a
   later, injected-JS feature.

## Sources

- Reflex — Wrapping React: overview, library-and-tags, props, example
  (`https://reflex.dev/docs/wrapping-react/`).
- Reflex — Custom Components overview & command reference
  (`https://reflex.dev/docs/custom-components/`).
- three.js — site, examples gallery, repository
  (`https://threejs.org`, `https://threejs.org/examples/`,
  `https://github.com/mrdoob/three.js`).
- React Three Fiber docs & releases (`https://r3f.docs.pmnd.rs`,
  `https://github.com/pmndrs/react-three-fiber`).
- drei (`https://github.com/pmndrs/drei`), npm version pages for
  `@react-three/fiber` and `@react-three/drei`.
