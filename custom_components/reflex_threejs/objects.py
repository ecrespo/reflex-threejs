"""Object3D host elements: groups, meshes, points, lines, sprites, instancing.

These are the "container" / renderable nodes of the scene graph. They are
host elements (lowercase JSX), so they extend :class:`ThreeElement`.
"""

from __future__ import annotations

from typing import Any

import reflex as rx
from reflex.vars import Var

from .base import ThreeElement


class Group(ThreeElement):
    """A ``<group>`` -- a transform container for other objects."""

    tag = "group"


class Mesh(ThreeElement):
    """A ``<mesh>`` -- a geometry + material pair, the most common object.

    Supports the full R3F pointer event suite, which three.js exposes through
    raycasting against the mesh.
    """

    tag = "mesh"

    # Cast/receive shadows (requires `shadows` on the Canvas).
    cast_shadow: Var[bool]
    receive_shadow: Var[bool]

    # Render order override for transparent sorting.
    render_order: Var[int]

    # --- Pointer events (R3F raycasted events) ------------------------------
    on_click: rx.EventHandler[rx.event.no_args_event_spec]
    on_double_click: rx.EventHandler[rx.event.no_args_event_spec]
    on_pointer_over: rx.EventHandler[rx.event.no_args_event_spec]
    on_pointer_out: rx.EventHandler[rx.event.no_args_event_spec]
    on_pointer_down: rx.EventHandler[rx.event.no_args_event_spec]
    on_pointer_up: rx.EventHandler[rx.event.no_args_event_spec]
    on_pointer_move: rx.EventHandler[rx.event.no_args_event_spec]
    on_wheel: rx.EventHandler[rx.event.no_args_event_spec]


class InstancedMesh(ThreeElement):
    """An ``<instancedMesh>`` for rendering many copies of one mesh cheaply.

    ``args`` is ``[geometry, material, count]`` (geometry/material may be null
    when supplied as children).
    """

    tag = "instancedMesh"

    cast_shadow: Var[bool]
    receive_shadow: Var[bool]

    on_click: rx.EventHandler[rx.event.no_args_event_spec]
    on_pointer_over: rx.EventHandler[rx.event.no_args_event_spec]
    on_pointer_out: rx.EventHandler[rx.event.no_args_event_spec]


class Points(ThreeElement):
    """A ``<points>`` element -- renders a geometry as a particle cloud."""

    tag = "points"


class Line(ThreeElement):
    """A ``<line>`` element -- the three.js Line host element (not SVG).

    Emitted as the intrinsic ``<line>`` tag, which R3F resolves to THREE.Line.
    """

    tag = "line"


class LineSegments(ThreeElement):
    """A ``<lineSegments>`` element -- pairs of vertices as discrete segments."""

    tag = "lineSegments"


class LineLoop(ThreeElement):
    """A ``<lineLoop>`` element -- a closed polyline."""

    tag = "lineLoop"


class Sprite(ThreeElement):
    """A ``<sprite>`` -- a camera-facing 2D plane (billboard)."""

    tag = "sprite"

    on_click: rx.EventHandler[rx.event.no_args_event_spec]


class Primitive(ThreeElement):
    """A ``<primitive>`` -- attaches an already-constructed three.js object.

    Used to mount the result of a loader (e.g. a GLTF scene) directly:
    ``primitive(object=State.gltf_scene)``.
    """

    tag = "primitive"

    # The pre-built three.js object to attach.
    object: Var[Any]


# Convenience factory functions (Reflex convention).
group = Group.create
mesh = Mesh.create
instanced_mesh = InstancedMesh.create
points = Points.create
line = Line.create
line_segments = LineSegments.create
line_loop = LineLoop.create
sprite = Sprite.create
primitive = Primitive.create
