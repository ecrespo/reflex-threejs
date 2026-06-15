# Usage Guide

## Mental model

A scene is a tree rooted at a `Canvas`. Inside it you nest **host elements**
(meshes, geometries, materials, lights, cameras, helpers) and **drei helpers**
(controls, staging, text, loaders). The Python tree mirrors the JSX tree of a
React Three Fiber app.

```python
import reflex as rx
from reflex_threejs import three


def scene() -> rx.Component:
    return three.canvas(
        three.ambient_light(intensity=0.6),
        three.directional_light(position=[5, 5, 5], intensity=1.0),
        three.mesh(
            three.box_geometry(args=[1, 1, 1]),
            three.mesh_standard_material(color="hotpink"),
        ),
        three.orbit_controls(),
        camera={"position": [3, 3, 3], "fov": 50},
        style={"width": "100%", "height": "600px"},
    )
```

Always give the `Canvas` (or a wrapping box) an explicit height — it fills its
parent, and a zero-height parent renders nothing.

## Host elements and `args`

R3F host elements forward `args` to the underlying three.js constructor:

```python
three.sphere_geometry(args=[1, 32, 32])        # SphereGeometry(radius, wSeg, hSeg)
three.cylinder_geometry(args=[0.5, 0.5, 2, 24]) # radTop, radBottom, height, radialSeg
```

A geometry/material placed as a child of a `mesh` auto-attaches. Other slots use
`attach`:

```python
three.color(attach="background", args=["#0b1020"])  # scene.background
three.fog(attach="fog", args=["#0b1020", 5, 20])    # scene.fog
```

## Transforms

Every host element accepts `position`, `rotation` (Euler radians), `scale`
(scalar or 3-tuple) and `visible`:

```python
three.mesh(..., position=[2, 0, -1], rotation=[0, 0.78, 0], scale=1.5)
```

## Lighting & shadows

```python
three.canvas(
    three.ambient_light(intensity=0.2),
    three.directional_light(position=[5, 5, 5], intensity=1.0, cast_shadow=True),
    three.mesh(..., cast_shadow=True),
    three.mesh(  # ground
        three.plane_geometry(args=[20, 20]),
        three.mesh_standard_material(color="#222"),
        rotation=[-1.5708, 0, 0], receive_shadow=True,
    ),
    shadows=True,  # enable the shadow map on the Canvas
)
```

## Interaction → Reflex events

Meshes raycast pointer events to Reflex event handlers:

```python
class S(rx.State):
    color: str = "#6366f1"

    @rx.event
    def recolor(self):
        self.color = "#ec4899"

three.mesh(
    three.box_geometry(args=[1, 1, 1]),
    three.mesh_standard_material(color=S.color),
    on_click=S.recolor,
    on_pointer_over=lambda: S.set_hovered(True),
)
```

Available mesh events: `on_click`, `on_double_click`, `on_pointer_over`,
`on_pointer_out`, `on_pointer_down`, `on_pointer_up`, `on_pointer_move`,
`on_wheel`.

## Binding state

Any prop accepts a state Var, so the scene reacts to your app:

```python
scale = rx.cond(S.hovered, [1.3, 1.3, 1.3], [1, 1, 1])
three.mesh(..., scale=scale)
```

## drei helpers

```python
three.canvas(
    three.drei.stage(             # auto lights + shadows + centering
        three.mesh(three.torus_knot_geometry(args=[1, 0.3, 160, 32]),
                   three.drei.mesh_distort_material(color="#8b5cf6", distort=0.4)),
        environment="city",
    ),
    three.drei.contact_shadows(position=[0, -1.4, 0], opacity=0.6, blur=2.4),
    three.orbit_controls(auto_rotate=True),
)
```

## Loading a GLTF model

```python
three.canvas(
    three.ambient_light(intensity=0.6),
    three.drei.gltf(src="/models/duck.glb", scale=2),
    three.drei.environment(preset="sunset"),
    three.orbit_controls(),
)
```

Place model/HDRI assets under the app's `assets/` directory and reference them
by URL.

## Animation in v0.1

v0.1 favors client-side animation that needs no per-frame Python callback:

- `three.orbit_controls(auto_rotate=True)`
- `three.drei.float(...)`, `three.drei.mesh_distort_material(...)`,
  `three.drei.mesh_wobble_material(...)`, `three.drei.stars(speed=1)`

A Python `useFrame` bridge for custom per-frame logic is planned (see the
[roadmap](../sdd/05-roadmap-phases.md)).
