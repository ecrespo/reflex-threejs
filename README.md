# reflex-threejs

**Interactive three.js for [Reflex](https://reflex.dev) — in pure Python.**

`reflex-threejs` wraps [React Three Fiber](https://r3f.docs.pmnd.rs/) (the React
renderer for [three.js](https://threejs.org)) and its helper library
[drei](https://github.com/pmndrs/drei) as idiomatic Reflex components. Build
3D scenes — product viewers, data visualization, generative art, simulations —
without writing a line of JavaScript.

> Status: **alpha (v0.1.0)** — foundation, core components, demo app and full
> [SDD](docs/sdd/00-overview.md) artifacts are in place. See the
> [roadmap](docs/sdd/05-roadmap-phases.md).

---

## Why

three.js is the standard for web 3D, but it is imperative and JavaScript-only.
React Three Fiber makes it declarative — yet still React/JSX. Reflex compiles
Python to React, so wrapping R3F + drei once makes the entire three.js model
available to Python developers as ordinary Reflex components.

```python
import reflex as rx
from reflex_threejs import three


def index() -> rx.Component:
    return rx.box(
        three.canvas(
            three.ambient_light(intensity=0.6),
            three.directional_light(position=[5, 5, 5], intensity=1.0),
            three.mesh(
                three.box_geometry(args=[1.5, 1.5, 1.5]),
                three.mesh_standard_material(color="#6366f1", metalness=0.3),
            ),
            three.orbit_controls(auto_rotate=True),
            camera={"position": [3, 3, 3], "fov": 50},
        ),
        width="100%",
        height="600px",
    )


app = rx.App()
app.add_page(index)
```

## Features

- **Declarative scene graph** — `Canvas`, meshes, groups, points, lines, sprites,
  instancing — all from Python.
- **Full primitive surface** — 22 geometries, 14 materials, 6 lights, cameras and
  helpers, each accepting three.js constructor `args`.
- **Interaction** — pointer events (`on_click`, `on_pointer_over`, …) routed to
  Reflex event handlers.
- **State binding** — drive any prop (color, transform, …) with a Reflex state Var.
- **drei helpers** — OrbitControls, Environment/Stage, ContactShadows, Sky, Stars,
  Text, Html overlay, Float, animated materials and declarative GLTF loading.
- **Ergonomic API** — flat factories *or* the `three.*` namespace mirroring `rx.*`.
- **SSR-safe** — the WebGL `Canvas` is dynamically imported (`ssr:false`).

## Installation

> Not yet on PyPI (planned for v0.2). For now, install from source.

```bash
git clone https://github.com/ecrespo/reflex-threejs.git
cd reflex-threejs
pip install -e .
```

Requires **Reflex ≥ 0.7** (React 19). On an older Reflex/React 18 stack, see the
[compatibility guide](docs/guides/compatibility.md).

## Run the demo

The demo app showcases nine scenes spanning the main three.js example categories.

```bash
cd reflex_threejs_demo
pip install -r requirements.txt   # installs reflex + the local package
reflex init                       # first run only
reflex run
```

Then open http://localhost:3000.

| Route | Scene | Demonstrates |
|---|---|---|
| `/` | Hello Cube | Canvas, lights, mesh, OrbitControls |
| `/geometries` | Geometry Gallery | built-in geometries |
| `/materials` | Materials | material types + environment |
| `/lights` | Lights | ambient/directional/point/spot + shadows |
| `/interactive` | Interactive | click-to-recolor, hover-to-scale (state events) |
| `/particles` | Particles | `points` + buffer geometry |
| `/staging` | Staging & drei | Stage, ContactShadows, distort material |
| `/text` | 3D Text | drei `Text` + `Float` |
| `/space` | Space | drei `Stars`, emissive material |

## Two ways to use the API

```python
# 1. Namespace (rx-style)
from reflex_threejs import three
three.canvas(three.mesh(three.box_geometry(), three.mesh_normal_material()))

# 2. Flat factories
from reflex_threejs import canvas, mesh, box_geometry, mesh_normal_material
canvas(mesh(box_geometry(), mesh_normal_material()))
```

drei helpers live under `three.drei.*` (common ones promoted to `three.*`).

## Documentation

- [Usage guide](docs/guides/usage.md) — host elements, `args`, events, state binding.
- [Compatibility guide](docs/guides/compatibility.md) — React 18/19, R3F v8/v9.
- **Spec-Driven Design (SDD) artifacts** — the design of this project:
  - [Overview](docs/sdd/00-overview.md)
  - [PRD](docs/sdd/01-prd.md)
  - [Requirements & Specs](docs/sdd/02-requirements.md)
  - [Architecture](docs/sdd/03-architecture.md)
  - [Component Catalog](docs/sdd/04-component-catalog.md)
  - [Roadmap & Phases](docs/sdd/05-roadmap-phases.md)
  - [Implementation Plan](docs/sdd/06-implementation-plan.md)
  - [Task Backlog](docs/sdd/07-tasks.md)
  - [Research Notes](docs/sdd/08-research-notes.md)

## Project layout

```
reflex-threejs/
├── custom_components/reflex_threejs/   # the component library
│   ├── base.py        canvas.py        objects.py
│   ├── geometries.py  materials.py     lights.py
│   ├── cameras.py     drei.py          namespace.py
│   └── __init__.py
├── reflex_threejs_demo/                # runnable demo app
├── docs/
│   ├── sdd/                            # SDD artifacts
│   └── guides/                         # usage & compatibility
├── pyproject.toml   README.md   LICENSE   CHANGELOG.md
```

## How it works (in one paragraph)

`Canvas` is wrapped as a Reflex `NoSSRComponent`, so three.js initializes only in
the browser. Everything inside it — `<mesh>`, `<boxGeometry>`,
`<meshStandardMaterial>`, `<ambientLight>` — are React Three Fiber *host
elements*: lowercase intrinsic JSX tags resolved by R3F's reconciler at runtime,
requiring no import. We model these as Reflex components with `library = None`, so
Reflex emits the bare tag. drei helpers are real exported components, so they
declare the `@react-three/drei` package and an explicit tag. See the
[architecture doc](docs/sdd/03-architecture.md) for details.

## Contributing

Issues and PRs welcome. The design lives in [`docs/sdd`](docs/sdd/00-overview.md);
please keep specs and code in sync (it's in the Definition of Done).

## License

[MIT](LICENSE) © 2026 Ernesto Crespo.

## Acknowledgements

Built on the work of [three.js](https://threejs.org),
[pmndrs/react-three-fiber](https://github.com/pmndrs/react-three-fiber),
[pmndrs/drei](https://github.com/pmndrs/drei) and [Reflex](https://reflex.dev).
