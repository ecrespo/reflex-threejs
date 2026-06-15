"""Material host elements.

Each class maps to a three.js ``*Material``. The most common properties are
exposed as named props; anything else can be passed through ``args`` (a single
parameters object) or via Reflex's ``custom_attrs``.
"""

from __future__ import annotations

from typing import Any

from reflex.vars import Var

from .base import ThreeElement


class _Material(ThreeElement):
    """Common material props shared by most three.js materials."""

    # CSS color string or hex, e.g. "hotpink" or "#ff0066".
    color: Var[str]

    # Render both faces ("THREE.DoubleSide" maps to side=2).
    side: Var[int]

    # Transparency.
    transparent: Var[bool]
    opacity: Var[float]

    # Wireframe rendering.
    wireframe: Var[bool]

    # Flat shading toggle.
    flat_shading: Var[bool]

    # Vertex colors.
    vertex_colors: Var[bool]

    # Depth handling.
    depth_write: Var[bool]
    depth_test: Var[bool]

    # Attach to the parent mesh material slot.
    attach: Var[str]


class MeshBasicMaterial(_Material):
    """``<meshBasicMaterial>`` -- unlit, ignores lights."""

    tag = "meshBasicMaterial"


class MeshStandardMaterial(_Material):
    """``<meshStandardMaterial>`` -- physically based (metalness/roughness)."""

    tag = "meshStandardMaterial"

    metalness: Var[float]
    roughness: Var[float]
    emissive: Var[str]
    emissive_intensity: Var[float]
    env_map_intensity: Var[float]


class MeshPhysicalMaterial(_Material):
    """``<meshPhysicalMaterial>`` -- PBR with clearcoat, transmission, sheen."""

    tag = "meshPhysicalMaterial"

    metalness: Var[float]
    roughness: Var[float]
    clearcoat: Var[float]
    clearcoat_roughness: Var[float]
    transmission: Var[float]
    thickness: Var[float]
    ior: Var[float]
    reflectivity: Var[float]
    sheen: Var[float]


class MeshPhongMaterial(_Material):
    """``<meshPhongMaterial>`` -- shiny (Blinn-Phong) shading."""

    tag = "meshPhongMaterial"

    shininess: Var[float]
    specular: Var[str]
    emissive: Var[str]


class MeshLambertMaterial(_Material):
    """``<meshLambertMaterial>`` -- non-shiny, lit surfaces."""

    tag = "meshLambertMaterial"

    emissive: Var[str]


class MeshToonMaterial(_Material):
    """``<meshToonMaterial>`` -- cel/toon shading."""

    tag = "meshToonMaterial"


class MeshNormalMaterial(_Material):
    """``<meshNormalMaterial>`` -- maps surface normals to RGB."""

    tag = "meshNormalMaterial"


class MeshMatcapMaterial(_Material):
    """``<meshMatcapMaterial>`` -- material captured from a matcap texture."""

    tag = "meshMatcapMaterial"


class MeshDepthMaterial(_Material):
    """``<meshDepthMaterial>`` -- encodes depth."""

    tag = "meshDepthMaterial"


class LineBasicMaterial(_Material):
    """``<lineBasicMaterial>`` -- material for ``<line>`` objects."""

    tag = "lineBasicMaterial"

    linewidth: Var[float]


class LineDashedMaterial(_Material):
    """``<lineDashedMaterial>`` -- dashed line material."""

    tag = "lineDashedMaterial"

    dash_size: Var[float]
    gap_size: Var[float]
    scale: Var[float]


class PointsMaterial(_Material):
    """``<pointsMaterial>`` -- material for particle ``<points>``."""

    tag = "pointsMaterial"

    size: Var[float]
    size_attenuation: Var[bool]


class SpriteMaterial(_Material):
    """``<spriteMaterial>`` -- material for ``<sprite>`` billboards."""

    tag = "spriteMaterial"

    rotation: Var[float]  # type: ignore[assignment]


class ShaderMaterial(_Material):
    """``<shaderMaterial>`` -- custom GLSL vertex/fragment shaders."""

    tag = "shaderMaterial"

    vertex_shader: Var[str]
    fragment_shader: Var[str]
    uniforms: Var[dict[str, Any]]


# Factory functions.
mesh_basic_material = MeshBasicMaterial.create
mesh_standard_material = MeshStandardMaterial.create
mesh_physical_material = MeshPhysicalMaterial.create
mesh_phong_material = MeshPhongMaterial.create
mesh_lambert_material = MeshLambertMaterial.create
mesh_toon_material = MeshToonMaterial.create
mesh_normal_material = MeshNormalMaterial.create
mesh_matcap_material = MeshMatcapMaterial.create
mesh_depth_material = MeshDepthMaterial.create
line_basic_material = LineBasicMaterial.create
line_dashed_material = LineDashedMaterial.create
points_material = PointsMaterial.create
sprite_material = SpriteMaterial.create
shader_material = ShaderMaterial.create
