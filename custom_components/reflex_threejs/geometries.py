"""Geometry host elements.

Each class maps to a three.js ``*Geometry`` constructor. Constructor
parameters are passed through the inherited ``args`` prop, e.g.::

    box_geometry(args=[1, 2, 1])          # BoxGeometry(width=1, height=2, depth=1)
    sphere_geometry(args=[1, 32, 32])     # SphereGeometry(radius, widthSeg, heightSeg)

A handful of frequently-tuned parameters are also exposed as named props for
ergonomics, but ``args`` always wins if both are given.
"""

from __future__ import annotations

from reflex.vars import Var

from .base import ThreeElement


class _Geometry(ThreeElement):
    """Common base; geometries take no transform of their own."""


class BoxGeometry(_Geometry):
    """``<boxGeometry>`` -- BoxGeometry(width, height, depth, ...segments)."""

    tag = "boxGeometry"


class SphereGeometry(_Geometry):
    """``<sphereGeometry>`` -- SphereGeometry(radius, widthSeg, heightSeg, ...)."""

    tag = "sphereGeometry"


class PlaneGeometry(_Geometry):
    """``<planeGeometry>`` -- PlaneGeometry(width, height, wSeg, hSeg)."""

    tag = "planeGeometry"


class CircleGeometry(_Geometry):
    """``<circleGeometry>`` -- CircleGeometry(radius, segments)."""

    tag = "circleGeometry"


class RingGeometry(_Geometry):
    """``<ringGeometry>`` -- RingGeometry(innerRadius, outerRadius, segments)."""

    tag = "ringGeometry"


class CylinderGeometry(_Geometry):
    """``<cylinderGeometry>`` -- CylinderGeometry(radTop, radBottom, height, ...)."""

    tag = "cylinderGeometry"


class ConeGeometry(_Geometry):
    """``<coneGeometry>`` -- ConeGeometry(radius, height, radialSeg)."""

    tag = "coneGeometry"


class TorusGeometry(_Geometry):
    """``<torusGeometry>`` -- TorusGeometry(radius, tube, radialSeg, tubularSeg)."""

    tag = "torusGeometry"


class TorusKnotGeometry(_Geometry):
    """``<torusKnotGeometry>`` -- TorusKnotGeometry(radius, tube, tubSeg, radSeg, p, q)."""

    tag = "torusKnotGeometry"


class DodecahedronGeometry(_Geometry):
    """``<dodecahedronGeometry>`` -- DodecahedronGeometry(radius, detail)."""

    tag = "dodecahedronGeometry"


class IcosahedronGeometry(_Geometry):
    """``<icosahedronGeometry>`` -- IcosahedronGeometry(radius, detail)."""

    tag = "icosahedronGeometry"


class OctahedronGeometry(_Geometry):
    """``<octahedronGeometry>`` -- OctahedronGeometry(radius, detail)."""

    tag = "octahedronGeometry"


class TetrahedronGeometry(_Geometry):
    """``<tetrahedronGeometry>`` -- TetrahedronGeometry(radius, detail)."""

    tag = "tetrahedronGeometry"


class CapsuleGeometry(_Geometry):
    """``<capsuleGeometry>`` -- CapsuleGeometry(radius, length, capSeg, radialSeg)."""

    tag = "capsuleGeometry"


class LatheGeometry(_Geometry):
    """``<latheGeometry>`` -- LatheGeometry(points, segments, phiStart, phiLength)."""

    tag = "latheGeometry"


class TubeGeometry(_Geometry):
    """``<tubeGeometry>`` -- TubeGeometry(path, tubularSeg, radius, radialSeg, closed)."""

    tag = "tubeGeometry"


class ExtrudeGeometry(_Geometry):
    """``<extrudeGeometry>`` -- ExtrudeGeometry(shapes, options)."""

    tag = "extrudeGeometry"


class ShapeGeometry(_Geometry):
    """``<shapeGeometry>`` -- ShapeGeometry(shapes, curveSegments)."""

    tag = "shapeGeometry"


class EdgesGeometry(_Geometry):
    """``<edgesGeometry>`` -- EdgesGeometry(geometry, thresholdAngle)."""

    tag = "edgesGeometry"


class WireframeGeometry(_Geometry):
    """``<wireframeGeometry>`` -- WireframeGeometry(geometry)."""

    tag = "wireframeGeometry"


class BufferGeometry(_Geometry):
    """``<bufferGeometry>`` -- a raw geometry you fill with buffer attributes."""

    tag = "bufferGeometry"


class BufferAttribute(ThreeElement):
    """``<bufferAttribute>`` -- attach a typed array attribute to a geometry.

    Use ``attach`` to bind it, e.g.
    ``buffer_attribute(attach="attributes-position", args=[positions, 3])``.
    """

    tag = "bufferAttribute"

    # The slot to attach to, e.g. "attributes-position" or "attributes-color".
    attach: Var[str]

    # ``args`` = [Float32Array, itemSize].
    count: Var[int]
    array: Var[list[float]]
    item_size: Var[int]


# Factory functions.
box_geometry = BoxGeometry.create
sphere_geometry = SphereGeometry.create
plane_geometry = PlaneGeometry.create
circle_geometry = CircleGeometry.create
ring_geometry = RingGeometry.create
cylinder_geometry = CylinderGeometry.create
cone_geometry = ConeGeometry.create
torus_geometry = TorusGeometry.create
torus_knot_geometry = TorusKnotGeometry.create
dodecahedron_geometry = DodecahedronGeometry.create
icosahedron_geometry = IcosahedronGeometry.create
octahedron_geometry = OctahedronGeometry.create
tetrahedron_geometry = TetrahedronGeometry.create
capsule_geometry = CapsuleGeometry.create
lathe_geometry = LatheGeometry.create
tube_geometry = TubeGeometry.create
extrude_geometry = ExtrudeGeometry.create
shape_geometry = ShapeGeometry.create
edges_geometry = EdgesGeometry.create
wireframe_geometry = WireframeGeometry.create
buffer_geometry = BufferGeometry.create
buffer_attribute = BufferAttribute.create
