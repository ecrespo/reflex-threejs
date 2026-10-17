"""The ``three`` namespace -- ergonomic, rx-style access to every component.

Usage::

    from reflex_threejs import three
    three.canvas(three.mesh(three.box_geometry(), three.mesh_normal_material()))

Everything reachable as a flat factory is also reachable as ``three.<name>``.
drei helpers live under ``three.drei.*`` (and the most common ones are also
promoted to the top level, e.g. ``three.orbit_controls``).
"""

from __future__ import annotations

from types import SimpleNamespace

from . import drei as _drei
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
from .canvas import canvas
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

three = SimpleNamespace(
    drei=_drei,
    # root
    canvas=canvas,
    # objects
    group=group,
    mesh=mesh,
    instanced_mesh=instanced_mesh,
    points=points,
    line=line,
    line_segments=line_segments,
    line_loop=line_loop,
    sprite=sprite,
    primitive=primitive,
    # geometries
    box_geometry=box_geometry,
    sphere_geometry=sphere_geometry,
    plane_geometry=plane_geometry,
    circle_geometry=circle_geometry,
    ring_geometry=ring_geometry,
    cylinder_geometry=cylinder_geometry,
    cone_geometry=cone_geometry,
    torus_geometry=torus_geometry,
    torus_knot_geometry=torus_knot_geometry,
    dodecahedron_geometry=dodecahedron_geometry,
    icosahedron_geometry=icosahedron_geometry,
    octahedron_geometry=octahedron_geometry,
    tetrahedron_geometry=tetrahedron_geometry,
    capsule_geometry=capsule_geometry,
    lathe_geometry=lathe_geometry,
    tube_geometry=tube_geometry,
    extrude_geometry=extrude_geometry,
    shape_geometry=shape_geometry,
    edges_geometry=edges_geometry,
    wireframe_geometry=wireframe_geometry,
    buffer_geometry=buffer_geometry,
    buffer_attribute=buffer_attribute,
    # materials
    mesh_basic_material=mesh_basic_material,
    mesh_standard_material=mesh_standard_material,
    mesh_physical_material=mesh_physical_material,
    mesh_phong_material=mesh_phong_material,
    mesh_lambert_material=mesh_lambert_material,
    mesh_toon_material=mesh_toon_material,
    mesh_normal_material=mesh_normal_material,
    mesh_matcap_material=mesh_matcap_material,
    mesh_depth_material=mesh_depth_material,
    line_basic_material=line_basic_material,
    line_dashed_material=line_dashed_material,
    points_material=points_material,
    sprite_material=sprite_material,
    shader_material=shader_material,
    # lights
    ambient_light=ambient_light,
    directional_light=directional_light,
    point_light=point_light,
    spot_light=spot_light,
    hemisphere_light=hemisphere_light,
    rect_area_light=rect_area_light,
    # cameras / helpers
    perspective_camera=perspective_camera,
    orthographic_camera=orthographic_camera,
    grid_helper=grid_helper,
    polar_grid_helper=polar_grid_helper,
    axes_helper=axes_helper,
    box_helper=box_helper,
    fog=fog,
    fog_exp2=fog_exp2,
    color=color,
    # promoted drei helpers
    orbit_controls=_drei.orbit_controls,
    trackball_controls=_drei.trackball_controls,
    environment=_drei.environment,
    stage=_drei.stage,
    contact_shadows=_drei.contact_shadows,
    sky=_drei.sky,
    stars=_drei.stars,
    grid=_drei.grid,
    text=_drei.text,
    html=_drei.html,
    float=_drei.float_,
    center=_drei.center,
    bounds=_drei.bounds,
    gltf=_drei.gltf,
)
