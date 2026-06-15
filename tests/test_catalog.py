"""Contract tests: the component catalog as an executable specification.

Each assertion here mirrors a row of ``docs/sdd/04-component-catalog.md`` — the
project's data model. For every component we verify the two invariants that
make the R3F wrapping work:

* **host elements** (objects, geometries, materials, lights, cameras, helpers)
  emit a lowercase JSX ``tag`` and declare **no** npm ``library`` (R3F resolves
  the intrinsic tag at runtime);
* **drei** helpers declare the ``@react-three/drei`` ``library`` and an explicit
  PascalCase ``tag``.

Plus the prop surface required by the requirements doc (RF-002/003/005/006).
"""

from __future__ import annotations

import pytest

pytest.importorskip("reflex")

from reflex_threejs import three  # noqa: E402

# ---------------------------------------------------------------------------
# Catalog §3-7 — host elements: (factory_name, expected_tag)
# ---------------------------------------------------------------------------
HOST_ELEMENTS: list[tuple[str, str]] = [
    # Objects (§3)
    ("group", "group"),
    ("mesh", "mesh"),
    ("instanced_mesh", "instancedMesh"),
    ("points", "points"),
    ("line", "line"),
    ("line_segments", "lineSegments"),
    ("line_loop", "lineLoop"),
    ("sprite", "sprite"),
    ("primitive", "primitive"),
    # Geometries (§4)
    ("box_geometry", "boxGeometry"),
    ("sphere_geometry", "sphereGeometry"),
    ("plane_geometry", "planeGeometry"),
    ("circle_geometry", "circleGeometry"),
    ("ring_geometry", "ringGeometry"),
    ("cylinder_geometry", "cylinderGeometry"),
    ("cone_geometry", "coneGeometry"),
    ("torus_geometry", "torusGeometry"),
    ("torus_knot_geometry", "torusKnotGeometry"),
    ("dodecahedron_geometry", "dodecahedronGeometry"),
    ("icosahedron_geometry", "icosahedronGeometry"),
    ("octahedron_geometry", "octahedronGeometry"),
    ("tetrahedron_geometry", "tetrahedronGeometry"),
    ("capsule_geometry", "capsuleGeometry"),
    ("lathe_geometry", "latheGeometry"),
    ("tube_geometry", "tubeGeometry"),
    ("extrude_geometry", "extrudeGeometry"),
    ("shape_geometry", "shapeGeometry"),
    ("edges_geometry", "edgesGeometry"),
    ("wireframe_geometry", "wireframeGeometry"),
    ("buffer_geometry", "bufferGeometry"),
    ("buffer_attribute", "bufferAttribute"),
    # Materials (§5)
    ("mesh_basic_material", "meshBasicMaterial"),
    ("mesh_standard_material", "meshStandardMaterial"),
    ("mesh_physical_material", "meshPhysicalMaterial"),
    ("mesh_phong_material", "meshPhongMaterial"),
    ("mesh_lambert_material", "meshLambertMaterial"),
    ("mesh_toon_material", "meshToonMaterial"),
    ("mesh_normal_material", "meshNormalMaterial"),
    ("mesh_matcap_material", "meshMatcapMaterial"),
    ("mesh_depth_material", "meshDepthMaterial"),
    ("line_basic_material", "lineBasicMaterial"),
    ("line_dashed_material", "lineDashedMaterial"),
    ("points_material", "pointsMaterial"),
    ("sprite_material", "spriteMaterial"),
    ("shader_material", "shaderMaterial"),
    # Lights (§6)
    ("ambient_light", "ambientLight"),
    ("directional_light", "directionalLight"),
    ("point_light", "pointLight"),
    ("spot_light", "spotLight"),
    ("hemisphere_light", "hemisphereLight"),
    ("rect_area_light", "rectAreaLight"),
    # Cameras & helpers (§7)
    ("perspective_camera", "perspectiveCamera"),
    ("orthographic_camera", "orthographicCamera"),
    ("grid_helper", "gridHelper"),
    ("polar_grid_helper", "polarGridHelper"),
    ("axes_helper", "axesHelper"),
    ("box_helper", "boxHelper"),
    ("fog", "fog"),
    ("fog_exp2", "fogExp2"),
    ("color", "color"),
]

# ---------------------------------------------------------------------------
# Catalog §8 — drei helpers: (factory_name, expected_tag)
# ---------------------------------------------------------------------------
DREI_HELPERS: list[tuple[str, str]] = [
    ("orbit_controls", "OrbitControls"),
    ("trackball_controls", "TrackballControls"),
    ("fly_controls", "FlyControls"),
    ("map_controls", "MapControls"),
    ("perspective_camera", "PerspectiveCamera"),
    ("orthographic_camera", "OrthographicCamera"),
    ("environment", "Environment"),
    ("stage", "Stage"),
    ("contact_shadows", "ContactShadows"),
    ("sky", "Sky"),
    ("stars", "Stars"),
    ("cloud", "Cloud"),
    ("grid", "Grid"),
    ("text", "Text"),
    ("text_3d", "Text3D"),
    ("html", "Html"),
    ("billboard", "Billboard"),
    ("float", "Float"),
    ("center", "Center"),
    ("bounds", "Bounds"),
    ("edges", "Edges"),
    ("outlines", "Outlines"),
    ("wireframe", "Wireframe"),
    ("gradient_texture", "GradientTexture"),
    ("mesh_distort_material", "MeshDistortMaterial"),
    ("mesh_wobble_material", "MeshWobbleMaterial"),
    ("gltf", "Gltf"),
]


def props_of(factory_name: str, namespace=three) -> set[str]:
    """Return the set of prop names declared by a factory's component class."""
    return set(type(getattr(namespace, factory_name)()).get_props())


@pytest.mark.parametrize("factory_name,tag", HOST_ELEMENTS, ids=[t for _, t in HOST_ELEMENTS])
def test_host_element_tag_and_no_library(factory_name: str, tag: str) -> None:
    factory = getattr(three, factory_name)
    cmp = factory()
    assert cmp.tag == tag, f"{factory_name} should emit <{tag}>"
    assert cmp.library is None, f"{factory_name} is a host element and must not import"


@pytest.mark.parametrize("factory_name,tag", DREI_HELPERS, ids=[t for _, t in DREI_HELPERS])
def test_drei_tag_and_library(factory_name: str, tag: str) -> None:
    factory = getattr(three.drei, factory_name)
    cmp = factory()
    assert cmp.tag == tag, f"drei.{factory_name} should emit <{tag}>"
    assert "@react-three/drei" in cmp.library


def test_no_duplicate_host_tags() -> None:
    # Each catalog row maps to a distinct tag (the data model has no collisions).
    tags = [tag for _, tag in HOST_ELEMENTS]
    assert len(tags) == len(set(tags))


# ---------------------------------------------------------------------------
# RF-002/003 — required prop surfaces
# ---------------------------------------------------------------------------
MESH_EVENTS = [
    "on_click",
    "on_double_click",
    "on_pointer_over",
    "on_pointer_out",
    "on_pointer_down",
    "on_pointer_up",
    "on_pointer_move",
    "on_wheel",
]


def test_mesh_exposes_all_pointer_events() -> None:
    triggers = type(three.mesh()).get_event_triggers()
    for event in MESH_EVENTS:
        assert event in triggers, f"mesh is missing the {event} event trigger"


def test_object_transform_props_present() -> None:
    props = props_of("mesh")
    assert {"position", "rotation", "scale", "visible", "args"} <= props


@pytest.mark.parametrize(
    "factory_name",
    [name for name, _ in HOST_ELEMENTS if name.endswith("_material")],
)
def test_material_shared_props(factory_name: str) -> None:
    # RF-002: materials accept color/opacity/transparent/wireframe/side.
    props = props_of(factory_name)
    assert {"color", "opacity", "transparent", "wireframe", "side"} <= props


@pytest.mark.parametrize(
    "factory_name",
    [name for name, _ in HOST_ELEMENTS if name.endswith("_light")],
)
def test_light_shared_props(factory_name: str) -> None:
    # RF-002: lights accept color and intensity.
    props = props_of(factory_name)
    assert {"color", "intensity"} <= props


def test_standard_material_pbr_props() -> None:
    props = props_of("mesh_standard_material")
    assert {"metalness", "roughness", "emissive", "emissive_intensity"} <= props


# ---------------------------------------------------------------------------
# RF-006 — namespace completeness
# ---------------------------------------------------------------------------
def test_namespace_exposes_every_host_factory() -> None:
    for factory_name, _tag in HOST_ELEMENTS:
        assert hasattr(three, factory_name), f"three.{factory_name} missing"
        assert callable(getattr(three, factory_name))


def test_namespace_exposes_every_drei_factory() -> None:
    for factory_name, _tag in DREI_HELPERS:
        assert hasattr(three.drei, factory_name), f"three.drei.{factory_name} missing"
        assert callable(getattr(three.drei, factory_name))


def test_public_all_factories_resolve_on_namespace() -> None:
    # Every flat factory advertised in __all__ is reachable via the namespace.
    import reflex_threejs as rt

    non_factories = {"three", "drei", "ThreeElement", "ThreeProvider", "Canvas"}
    for name in rt.__all__:
        if name in non_factories:
            continue
        assert hasattr(three, name), f"__all__ exports {name} but three.{name} is missing"
