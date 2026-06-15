# reflex-threejs — Technical Design / Architecture

## Metadata

| Field | Value |
|---|---|
| **Author** | Ernesto Crespo |
| **Status** | `DRAFT` |
| **Version** | 1.0 |
| **Date** | 2026-06-14 |
| **Related PRD** | [01-prd.md](01-prd.md) |
| **Requirements** | [02-requirements.md](02-requirements.md) |

---

## 1. Context

Reflex compiles Python component trees to a React/Next.js frontend and runs
application state on a Python backend synchronized over WebSocket. three.js is
an imperative WebGL engine; React Three Fiber (R3F) turns it into a declarative
React renderer, and drei adds high-level helpers. Because Reflex already targets
React, the cheapest and most complete way to bring three.js to Reflex is to
**wrap R3F + drei**, not three.js directly.

The central engineering challenge is that R3F is not an ordinary React
component library: inside `<Canvas>` it runs its own reconciler that resolves
**lowercase intrinsic JSX tags** (`<mesh>`, `<boxGeometry>`, `<ambientLight>`)
to three.js objects. These tags have no npm import. The design must let Reflex
emit such tags verbatim while still emitting real imports for the components
that *are* exported (`Canvas`, `OrbitControls`, ...).

## 2. Technical Objectives

- **Correctness:** host elements emit as bare JSX with no import; exported
  components emit a pinned import.
- **Completeness:** cover the common three.js element families declaratively.
- **Maintainability:** one module per family; versions pinned in one place.
- **Operability:** code-split 3D so non-3D pages stay light.

## 3. Proposed Architecture

### 3.1 High-level diagram

```
                 Python (author)                         Browser (runtime)
 ┌───────────────────────────────────────┐      ┌──────────────────────────────┐
 │  reflex_threejs                        │      │  React tree (compiled)       │
 │                                        │      │                              │
 │  three.canvas(                         │      │  <Canvas> (dynamic, ssr:off) │
 │    three.ambient_light(...),           │ ───▶ │    <ambientLight/>           │
 │    three.mesh(                         │ Reflex│    <mesh>                    │
 │      three.box_geometry(args=[1,1,1]), │compile│      <boxGeometry args=.../>│
 │      three.mesh_standard_material(...),│      │      <meshStandardMaterial/> │
 │    ),                                  │      │    </mesh>                   │
 │    three.orbit_controls(),             │      │    <OrbitControls/>          │
 │  )                                     │      │  </Canvas>                   │
 └───────────────────────────────────────┘      └──────────────┬───────────────┘
                                                                │
                                              @react-three/fiber│reconciler
                                                                ▼
                                                        three.js / WebGL
```

### 3.2 Component classes

| Component | Base | Library import | Emits |
|---|---|---|---|
| `Canvas` | `NoSSRComponent` | `@react-three/fiber` | `<Canvas>` via `dynamic(..., {ssr:false})` |
| Host elements (mesh, geometries, materials, lights, cameras, helpers) | `ThreeElement` (`library=None`) | none | bare lowercase JSX tag |
| drei helpers | `DreiComponent` (`rx.Component`) | `@react-three/drei` | `<OrbitControls>`, `<Environment>`, ... |

`three` is required as a `lib_dependencies` entry so npm installs it even though
it is never imported directly by our generated code (R3F imports it internally).

### 3.3 Host elements — the key mechanism

`ThreeElement` sets `library = None` and only a lowercase `tag`. Reflex then
renders the tag without an import statement, e.g. `tag = "mesh"` →
`<mesh ...>`. Every host element inherits transform props (`position`,
`rotation`, `scale`, `visible`) and an `args` prop that maps to the three.js
constructor arguments (`<boxGeometry args={[1,1,1]} />`).

Geometry/material attachment uses R3F's child-attach convention: a geometry or
material placed as a child of a `mesh` is auto-attached to `geometry` /
`material`. For non-default slots we set the `attach` prop (e.g. `<color
attach="background">`, `<fog attach="fog">`, `<bufferAttribute
attach="attributes-position">`).

### 3.4 Events

R3F implements pointer events by raycasting against objects. We expose them as
Reflex `EventHandler` props on `mesh`/`sprite`/`instancedMesh`
(`on_click`, `on_pointer_over`, ...). They use `rx.event.no_args_event_spec` by
default; richer specs (intersection point, instanceId) can be added with custom
event specs as needed.

### 3.5 State binding

Because each prop is an `rx.Var`, any Reflex state Var can be passed in and is
compiled to a reactive binding. Example: `color=State.active_color`, or a
transform driven by `rx.cond(State.hovered, [1.3,1.3,1.3], [1,1,1])`. Updates
flow through Reflex's normal state → re-render path.

### 3.6 drei layer

drei helpers are real exported React components, so `DreiComponent` declares
`library = "@react-three/drei@^10"` and each subclass a `tag`. They cover four
needs: camera controls, scene staging/environment, abstractions (Text, Html,
Float, Bounds), and declarative asset loading (`Gltf` wraps `useGLTF`).

### 3.7 Namespace

`namespace.py` assembles a `SimpleNamespace` named `three` that maps every
factory function, mirroring Reflex's `rx.*` ergonomics. drei lives under
`three.drei.*`; the most-used helpers are promoted to `three.*`.

## 4. Design Decisions

### DD-001: Wrap React Three Fiber, not three.js directly
- **Decision:** Build on R3F + drei.
- **Context:** three.js is imperative and JS-only; R3F is declarative React.
- **Alternatives:**

| Option | Pros | Cons |
|---|---|---|
| **A. Wrap R3F + drei (chosen)** | Declarative, matches Reflex's model, huge ecosystem, drei helpers free | Inherits React/R3F version coupling |
| B. Wrap three.js in a hand-written React component | Full control | Re-implements R3F; imperative bridge; large effort |
| C. Embed via `Html`/iframe | Simple | Not integrated with Reflex state/events |

- **Justification:** R3F gives a declarative surface that compiles cleanly
  through Reflex and unlocks drei for free.
- **Consequences:** we must track R3F/React compatibility (see DD-003).

### DD-002: Host elements as `library = None` components
- **Decision:** Represent R3F intrinsic tags as `ThreeElement` with no library.
- **Context:** intrinsic tags must render without an import and only inside `Canvas`.
- **Consequences:** clean JSX output; misuse outside a `Canvas` fails at runtime
  (documented), not compile time.

### DD-003: Pin to React 19 / R3F v9 by default
- **Decision:** Default to `@react-three/fiber@^9`, `@react-three/drei@^10`,
  matching Reflex ≥ 0.7 (React 19).
- **Alternatives:** target React 18 / fiber v8 (older Reflex).
- **Justification:** newer Reflex ships React 19; aligning avoids peer-dependency
  conflicts.
- **Consequences:** provide a documented fallback matrix for React-18 apps
  ([compatibility guide](../guides/compatibility.md)).

### DD-004: Animation via drei in v0.1, `useFrame` bridge later
- **Decision:** v0.1 motion uses `OrbitControls(auto_rotate=True)` and drei
  animated materials (`MeshDistortMaterial`, `Float`); a Python `useFrame`
  bridge is deferred to v0.2.
- **Justification:** a per-frame callback into Python state would be chatty over
  WebSocket; client-side animation is the correct default. The bridge will use
  injected custom JS hooks for purely client-side animation.

## 5. Patterns and Conventions

### 5.1 Code structure

```
custom_components/reflex_threejs/
├── __init__.py        # public flat API + `three` namespace
├── base.py            # ThreeProvider, ThreeElement, pinned versions, typing
├── canvas.py          # Canvas (NoSSRComponent)
├── objects.py         # group, mesh, points, line, sprite, instancedMesh, primitive
├── geometries.py      # *Geometry host elements
├── materials.py       # *Material host elements
├── lights.py          # *Light host elements
├── cameras.py         # cameras + helpers (grid/axes/fog/color)
├── drei.py            # @react-three/drei wrappers
└── namespace.py       # the `three` SimpleNamespace
```

### 5.2 Applied patterns

| Pattern | Where | Why |
|---|---|---|
| Base class + mixins | `ThreeElement`, `_Material`, `_Light` | Share transform/common props |
| Factory functions | `mesh = Mesh.create` | Match Reflex idiom |
| Facade / namespace | `three` | Single ergonomic entry point |
| Version pinning | `base.py` constants | One place to bump npm deps |

### 5.3 Error handling
- SSR safety: WebGL components are `NoSSRComponent`.
- Misuse (host element outside `Canvas`) surfaces as an R3F runtime error;
  documented in the guides.

## 6. Security
- No backend data crosses into generated JS beyond bound state Vars.
- External assets (HDRI, `.glb`) are loaded by URL the developer controls; the
  library adds no third-party network calls of its own.

## 7. Testing Strategy

| Level | Target | Tools | Covers |
|---|---|---|---|
| Static | syntax + lint | `py_compile`, `ruff` | all modules |
| Unit | component construction | `pytest` | tag/library/props compile to expected spec |
| Build | app compiles | `reflex export`/compile | demo app renders to JS without error |
| Manual | visual | browser | each demo scene renders and is interactive |

## 8. Rollout
- v0.1 on `main` (this repo): scaffold + core + demo + SDD.
- v0.2: PyPI publish via `reflex component` tooling; `useFrame` bridge.
- Backward compatibility: additive props; pinned npm avoids surprise breaks.

## 9. Open Questions
- [ ] Surface richer event specs (intersection, instanceId)? — v0.2
- [ ] Ship typed `Vector3`/`Euler` helpers + serializers? — v0.2
- [ ] Bundle a default typeface/HDRI asset, or require URLs? — v0.2

---

## Change History

| Version | Date | Author | Changes |
|---|---|---|---|
| 1.0 | 2026-06-14 | Ernesto Crespo | Initial version |
