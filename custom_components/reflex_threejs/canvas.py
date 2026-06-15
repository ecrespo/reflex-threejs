"""The ``Canvas`` component -- the entry point of every 3D scene.

``<Canvas>`` from ``@react-three/fiber`` sets up the renderer, a default
scene, camera and render loop. Because it instantiates a WebGL context and
touches the ``window`` object, it cannot be server-side rendered, so we wrap
it as a :class:`reflex.components.component.NoSSRComponent` (dynamic import,
``ssr: false``).
"""

from __future__ import annotations

from typing import Any

import reflex as rx
from reflex.components.component import NoSSRComponent
from reflex.vars import Var

from .base import FIBER_VERSION, THREE_VERSION


class Canvas(NoSSRComponent):
    """Root of an R3F scene graph.

    All three.js host elements (mesh, lights, geometries, materials) and drei
    helpers must be nested inside a ``Canvas``.
    """

    library = FIBER_VERSION
    tag = "Canvas"
    lib_dependencies: list[str] = [THREE_VERSION]

    # Camera configuration, e.g. {"position": [0, 0, 5], "fov": 75}.
    camera: Var[dict[str, Any]]

    # Shadow map configuration. ``True`` enables PCFSoftShadowMap.
    shadows: Var[bool | str | dict[str, Any]]

    # Device pixel ratio. A [min, max] tuple clamps it across displays.
    dpr: Var[float | list[float]]

    # gl (WebGLRenderer) parameters, e.g. {"antialias": True, "alpha": True}.
    gl: Var[dict[str, Any]]

    # Render mode: "always" | "demand" | "never".
    frameloop: Var[str]

    # Enable flat (linear) tone mapping when False; default True (ACESFilmic).
    flat: Var[bool]

    # Orthographic camera instead of the default perspective one.
    orthographic: Var[bool]

    # Whether the canvas should resize to fit its parent.
    resize: Var[dict[str, Any]]

    # NOTE: ``style`` is inherited from ``rx.Component``; do not redeclare it.
    # Redeclaring it drops the inherited default and breaks Reflex's style
    # merge (``**None``). The ``create`` override below sets the fill-parent
    # default instead.

    # Pointer events.
    on_pointer_missed: rx.EventHandler[rx.event.no_args_event_spec]

    # Fired once the canvas is created (R3F `onCreated`).
    on_created: rx.EventHandler[rx.event.no_args_event_spec]

    @classmethod
    def create(cls, *children, **props):
        """Create a Canvas, defaulting to fill its parent container."""
        props.setdefault("style", {"width": "100%", "height": "100%"})
        return super().create(*children, **props)


canvas = Canvas.create
