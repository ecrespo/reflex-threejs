"""Light host elements."""

from __future__ import annotations

from reflex.vars import Var

from .base import ThreeElement


class _Light(ThreeElement):
    """Common light props."""

    color: Var[str]
    intensity: Var[float]


class AmbientLight(_Light):
    """``<ambientLight>`` -- uniform, directionless fill light."""

    tag = "ambientLight"


class DirectionalLight(_Light):
    """``<directionalLight>`` -- parallel rays (sun-like), supports shadows."""

    tag = "directionalLight"

    cast_shadow: Var[bool]
    # Shadow map resolution, e.g. shadow-mapSize via custom_attrs.
    shadow_bias: Var[float]


class PointLight(_Light):
    """``<pointLight>`` -- radiates from a single point in all directions."""

    tag = "pointLight"

    distance: Var[float]
    decay: Var[float]
    cast_shadow: Var[bool]


class SpotLight(_Light):
    """``<spotLight>`` -- a cone of light."""

    tag = "spotLight"

    distance: Var[float]
    angle: Var[float]
    penumbra: Var[float]
    decay: Var[float]
    cast_shadow: Var[bool]


class HemisphereLight(_Light):
    """``<hemisphereLight>`` -- sky/ground gradient ambient light."""

    tag = "hemisphereLight"

    # args = [skyColor, groundColor, intensity]
    ground_color: Var[str]


class RectAreaLight(_Light):
    """``<rectAreaLight>`` -- a soft rectangular area light."""

    tag = "rectAreaLight"

    width: Var[float]
    height: Var[float]


ambient_light = AmbientLight.create
directional_light = DirectionalLight.create
point_light = PointLight.create
spot_light = SpotLight.create
hemisphere_light = HemisphereLight.create
rect_area_light = RectAreaLight.create
