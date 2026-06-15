"""Camera and helper host elements."""

from __future__ import annotations

from reflex.vars import Var

from .base import ThreeElement


class PerspectiveCamera(ThreeElement):
    """``<perspectiveCamera>`` -- the default human-eye-like projection.

    Use ``makeDefault`` (via drei's ``PerspectiveCamera``) to make it the
    active camera; the raw host element here is for manual setups.
    """

    tag = "perspectiveCamera"

    fov: Var[float]
    aspect: Var[float]
    near: Var[float]
    far: Var[float]
    zoom: Var[float]


class OrthographicCamera(ThreeElement):
    """``<orthographicCamera>`` -- parallel projection (no perspective)."""

    tag = "orthographicCamera"

    near: Var[float]
    far: Var[float]
    zoom: Var[float]
    left: Var[float]
    right: Var[float]
    top: Var[float]
    bottom: Var[float]


class GridHelper(ThreeElement):
    """``<gridHelper>`` -- a reference grid on the XZ plane.

    ``args`` = [size, divisions, colorCenterLine, colorGrid].
    """

    tag = "gridHelper"


class PolarGridHelper(ThreeElement):
    """``<polarGridHelper>`` -- a circular reference grid."""

    tag = "polarGridHelper"


class AxesHelper(ThreeElement):
    """``<axesHelper>`` -- RGB lines for the X/Y/Z axes. ``args`` = [size]."""

    tag = "axesHelper"


class BoxHelper(ThreeElement):
    """``<boxHelper>`` -- a wireframe bounding box around an object."""

    tag = "boxHelper"


class Fog(ThreeElement):
    """``<fog>`` -- linear distance fog. ``args`` = [color, near, far]."""

    tag = "fog"
    attach = "fog"


class FogExp2(ThreeElement):
    """``<fogExp2>`` -- exponential distance fog. ``args`` = [color, density]."""

    tag = "fogExp2"
    attach = "fog"


class Color(ThreeElement):
    """``<color>`` -- set the scene background. ``args`` = [color]."""

    tag = "color"
    attach = "background"


perspective_camera = PerspectiveCamera.create
orthographic_camera = OrthographicCamera.create
grid_helper = GridHelper.create
polar_grid_helper = PolarGridHelper.create
axes_helper = AxesHelper.create
box_helper = BoxHelper.create
fog = Fog.create
fog_exp2 = FogExp2.create
color = Color.create
