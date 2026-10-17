"""Smoke tests asserting each component compiles to the expected React spec.

These tests require ``reflex`` to be installed (CI installs it via the package's
dependencies). They verify the two invariants that make the wrapper work:

* host elements emit a lowercase ``tag`` and **no** npm import (``library`` None);
* drei / Canvas components declare their npm ``library`` and an explicit ``tag``.
"""

from __future__ import annotations

import pytest

reflex = pytest.importorskip("reflex")

from reflex_threejs import three  # noqa: E402
from reflex_threejs.base import ThreeElement  # noqa: E402
from reflex_threejs.canvas import Canvas  # noqa: E402
from reflex_threejs.drei import OrbitControls  # noqa: E402


def test_canvas_is_nossr_with_library():
    from reflex.components.component import NoSSRComponent

    assert issubclass(Canvas, NoSSRComponent)
    assert "@react-three/fiber" in Canvas.library
    assert Canvas.tag == "Canvas"


def test_canvas_creates_and_defaults_to_fill_parent():
    # RF-001: Canvas instantiates and defaults to width/height 100%.
    # Style values compile to Reflex Vars, so compare their rendered form.
    cmp = three.canvas()
    assert str(cmp.style["width"]) == '"100%"'
    assert str(cmp.style["height"]) == '"100%"'


def test_canvas_accepts_root_props():
    # RF-001: camera/shadows/dpr/gl/frameloop/orthographic are accepted.
    cmp = three.canvas(
        camera={"position": [0, 0, 5], "fov": 75},
        shadows=True,
        dpr=[1, 2],
        gl={"antialias": True},
        frameloop="demand",
        orthographic=True,
    )
    assert cmp.tag == "Canvas"


def test_host_element_has_no_library():
    cmp = three.mesh()
    assert isinstance(cmp, ThreeElement)
    assert cmp.library is None
    assert cmp.tag == "mesh"


@pytest.mark.parametrize(
    "factory,tag",
    [
        (three.box_geometry, "boxGeometry"),
        (three.sphere_geometry, "sphereGeometry"),
        (three.mesh_standard_material, "meshStandardMaterial"),
        (three.ambient_light, "ambientLight"),
        (three.directional_light, "directionalLight"),
        (three.points, "points"),
        (three.grid_helper, "gridHelper"),
    ],
)
def test_host_tags(factory, tag):
    cmp = factory()
    assert cmp.tag == tag
    assert cmp.library is None


def test_drei_declares_library():
    cmp = three.drei.orbit_controls()
    assert isinstance(cmp, OrbitControls)
    assert "@react-three/drei" in cmp.library
    assert cmp.tag == "OrbitControls"


def test_namespace_exposes_factories():
    assert callable(three.canvas)
    assert callable(three.mesh)
    assert callable(three.drei.environment)


def test_scene_composes():
    scene = three.canvas(
        three.ambient_light(intensity=0.6),
        three.mesh(
            three.box_geometry(args=[1, 1, 1]),
            three.mesh_standard_material(color="hotpink"),
        ),
        three.orbit_controls(),
    )
    # Children render under the Canvas.
    assert scene.children


def test_buffer_attribute_wraps_literal_args_in_float32array():
    # three.js BufferAttribute rejects plain arrays ("array should be a Typed
    # Array"), so a Python list in args[0] must compile to a Float32Array.
    cmp = three.buffer_attribute(attach="attributes-position", args=[[0.0, 1.0, 2.0], 3])
    rendered = str(cmp.args)
    assert "new Float32Array([0.0, 1.0, 2.0])" in rendered.replace(" ,", ",")
    assert rendered.rstrip("]").endswith("3")


def test_buffer_attribute_wraps_array_prop_and_state_vars():
    from reflex.vars.base import Var

    state_list = Var(_js_expr="positions", _var_type=list[float])
    cmp = three.buffer_attribute(
        attach="attributes-position", args=[state_list, 3], array=[0.0, 1.0, 2.0]
    )
    assert "new Float32Array(positions)" in str(cmp.args)
    assert str(cmp.array).startswith("new Float32Array(")


def test_drei_float_alias_does_not_shadow_builtin_in_annotations():
    # `three.drei.float` must stay available without rebinding the builtin in
    # the module globals, where `float | list[float]` annotations are evaluated
    # (the .pyi generator crashed on ContactShadows when it did).
    from reflex_threejs import drei

    assert three.drei.float is drei.float_
    for annotation in drei.ContactShadows.__dict__["__annotations__"].values():
        eval(annotation, vars(drei))  # raised TypeError: 'method' | GenericAlias
