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
