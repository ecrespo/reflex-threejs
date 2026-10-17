"""reflex-threejs -- React Three Fiber & drei, wrapped as Reflex components.

Two ways to use the library:

1. Flat factory functions::

    from reflex_threejs import canvas, mesh, box_geometry, mesh_standard_material

2. Namespaced access (mirrors Reflex's own ``rx.*`` style)::

    from reflex_threejs import three

    three.canvas(
        three.ambient_light(intensity=0.6),
        three.mesh(
            three.box_geometry(args=[1, 1, 1]),
            three.mesh_standard_material(color="hotpink"),
        ),
        three.orbit_controls(),
    )
"""

from __future__ import annotations

from . import drei
from .base import ThreeElement, ThreeProvider
from .cameras import (
    axes_helper,
    box_helper,
    color,
    fog,
    fog_exp2,
    grid_helper,
    orthographic_camera,
    perspective_camera,
    polar_grid_helper,
)
from .canvas import Canvas, canvas
from .geometries import (
    box_geometry,
    buffer_attribute,
    buffer_geometry,
    capsule_geometry,
    circle_geometry,
    cone_geometry,
    cylinder_geometry,
    dodecahedron_geometry,
    edges_geometry,
    extrude_geometry,
    icosahedron_geometry,
    lathe_geometry,
    octahedron_geometry,
    plane_geometry,
    ring_geometry,
    shape_geometry,
    sphere_geometry,
    tetrahedron_geometry,
    torus_geometry,
    torus_knot_geometry,
    tube_geometry,
    wireframe_geometry,
)
from .lights import (
    ambient_light,
    directional_light,
    hemisphere_light,
    point_light,
    rect_area_light,
    spot_light,
)
from .materials import (
    line_basic_material,
    line_dashed_material,
    mesh_basic_material,
    mesh_depth_material,
    mesh_lambert_material,
    mesh_matcap_material,
    mesh_normal_material,
    mesh_phong_material,
    mesh_physical_material,
    mesh_standard_material,
    mesh_toon_material,
    points_material,
    shader_material,
    sprite_material,
)
from .namespace import three
from .objects import (
    group,
    instanced_mesh,
    line,
    line_loop,
    line_segments,
    mesh,
    points,
    primitive,
    sprite,
)

__version__ = "0.2.0"

__all__ = [
    "three",
    "drei",
    "ThreeElement",
    "ThreeProvider",
    "Canvas",
    "canvas",
    # objects
    "group",
    "mesh",
    "instanced_mesh",
    "points",
    "line",
    "line_segments",
    "line_loop",
    "sprite",
    "primitive",
    # geometries
    "box_geometry",
    "sphere_geometry",
    "plane_geometry",
    "circle_geometry",
    "ring_geometry",
    "cylinder_geometry",
    "cone_geometry",
    "torus_geometry",
    "torus_knot_geometry",
    "dodecahedron_geometry",
    "icosahedron_geometry",
    "octahedron_geometry",
    "tetrahedron_geometry",
    "capsule_geometry",
    "lathe_geometry",
    "tube_geometry",
    "extrude_geometry",
    "shape_geometry",
    "edges_geometry",
    "wireframe_geometry",
    "buffer_geometry",
    "buffer_attribute",
    # materials
    "mesh_basic_material",
    "mesh_standard_material",
    "mesh_physical_material",
    "mesh_phong_material",
    "mesh_lambert_material",
    "mesh_toon_material",
    "mesh_normal_material",
    "mesh_matcap_material",
    "mesh_depth_material",
    "line_basic_material",
    "line_dashed_material",
    "points_material",
    "sprite_material",
    "shader_material",
    # lights
    "ambient_light",
    "directional_light",
    "point_light",
    "spot_light",
    "hemisphere_light",
    "rect_area_light",
    # cameras / helpers
    "perspective_camera",
    "orthographic_camera",
    "grid_helper",
    "polar_grid_helper",
    "axes_helper",
    "box_helper",
    "fog",
    "fog_exp2",
    "color",
]
