"""Base classes for the reflex-threejs component library.

This module defines the two foundational component types used across the
whole library:

* :class:`ThreeProvider` -- a thin base for any component that needs the
  ``@react-three/fiber`` / ``@react-three/drei`` npm packages imported.
* :class:`ThreeElement` -- the base for React Three Fiber *host* elements
  (a.k.a. "primitives"), the lowercase JSX tags such as ``<mesh>``,
  ``<boxGeometry>`` or ``<ambientLight>``. These tags are resolved by the
  R3F reconciler at runtime and therefore require **no import**: they only
  exist inside a ``<Canvas>`` tree.

The distinction matters for how Reflex compiles the component:

* Components that wrap a real exported React component (``Canvas``,
  ``OrbitControls`` ...) declare a ``library`` and ``tag`` so Reflex emits an
  ``import`` statement.
* Host elements declare ``library = None`` and only a lowercase ``tag`` so
  Reflex emits the bare JSX tag with no import.
"""

from __future__ import annotations

from typing import Any

import reflex as rx
from reflex.vars import Var

# Pinned npm versions. Keep these in sync with docs/sdd and pyproject.toml.
# React Three Fiber v9 targets React 19 (Reflex >= 0.7). For Reflex apps still
# on React 18, pin fiber@8 / drei@9 instead (see docs/guides/compatibility.md).
# three.js ships breaking changes in minor releases (0.x), so the caret only
# allows patch updates within the pinned minor: bump it deliberately.
FIBER_VERSION = "@react-three/fiber@^9.8.2"
DREI_VERSION = "@react-three/drei@^10.7.9"
THREE_VERSION = "three@^0.186.1"


# ---------------------------------------------------------------------------
# Shared transform / vector typing helpers
# ---------------------------------------------------------------------------
# R3F accepts a scalar or a 3-tuple for transform props. We accept both a
# float (uniform) and a list/tuple of floats.
Vector3 = list[float] | tuple[float, float, float] | float
Euler = list[float] | tuple[float, float, float]
# ``args`` are forwarded to the underlying three.js constructor.
ConstructorArgs = list[Any]


class ThreeProvider(rx.Component):
    """Base for components that need the React Three ecosystem imported."""

    # Subclasses that wrap a real exported component set `library` + `tag`.
    library: str = FIBER_VERSION

    # The list of npm packages required even when not directly imported.
    lib_dependencies: list[str] = [THREE_VERSION]


class ThreeElement(rx.Component):
    """Base for React Three Fiber host elements (lowercase JSX primitives).

    These render as bare JSX tags (e.g. ``<mesh>``) with no import statement.
    They are only valid inside a ``<Canvas>`` provided by
    :class:`reflex_threejs.canvas.Canvas`.
    """

    # No npm import: R3F resolves these intrinsic tags at runtime.
    library = None  # type: ignore[assignment]

    # --- Transform props shared by every Object3D-like element ---------------
    # World-space position [x, y, z].
    position: Var[Vector3]

    # Rotation as Euler angles [x, y, z] in radians.
    rotation: Var[Euler]

    # Scale, scalar or [x, y, z].
    scale: Var[Vector3]

    # Visibility toggle.
    visible: Var[bool]

    # Constructor arguments forwarded to the underlying three.js class.
    # e.g. BoxGeometry(width, height, depth) -> args=[1, 1, 1].
    args: Var[ConstructorArgs]
