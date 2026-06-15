"""Wrappers for ``@react-three/drei`` helpers.

drei is the official "useful helpers" companion to React Three Fiber. Unlike
host elements, these are real exported React components, so each declares the
``@react-three/drei`` library and an explicit ``tag``.
"""

from __future__ import annotations

from typing import Any

import reflex as rx
from reflex.vars import Var

from .base import DREI_VERSION, THREE_VERSION


class DreiComponent(rx.Component):
    """Base for every drei helper."""

    library = DREI_VERSION
    lib_dependencies: list[str] = [THREE_VERSION]


# ---------------------------------------------------------------------------
# Controls
# ---------------------------------------------------------------------------
class OrbitControls(DreiComponent):
    """``OrbitControls`` -- drag to orbit, scroll to zoom, right-drag to pan."""

    tag = "OrbitControls"

    make_default: Var[bool]
    enable_zoom: Var[bool]
    enable_pan: Var[bool]
    enable_rotate: Var[bool]
    enable_damping: Var[bool]
    damping_factor: Var[float]
    auto_rotate: Var[bool]
    auto_rotate_speed: Var[float]
    min_distance: Var[float]
    max_distance: Var[float]
    min_polar_angle: Var[float]
    max_polar_angle: Var[float]
    target: Var[list[float]]

    on_change: rx.EventHandler[rx.event.no_args_event_spec]
    on_start: rx.EventHandler[rx.event.no_args_event_spec]
    on_end: rx.EventHandler[rx.event.no_args_event_spec]


class TrackballControls(DreiComponent):
    """``TrackballControls`` -- free-rotation trackball camera controls."""

    tag = "TrackballControls"
    make_default: Var[bool]


class FlyControls(DreiComponent):
    """``FlyControls`` -- first-person fly-through navigation."""

    tag = "FlyControls"
    movement_speed: Var[float]
    roll_speed: Var[float]


class MapControls(DreiComponent):
    """``MapControls`` -- pan-first controls suited to top-down maps."""

    tag = "MapControls"
    make_default: Var[bool]


# ---------------------------------------------------------------------------
# Cameras (drei, with makeDefault support)
# ---------------------------------------------------------------------------
class PerspectiveCamera(DreiComponent):
    """drei ``PerspectiveCamera`` -- supports ``makeDefault``."""

    tag = "PerspectiveCamera"
    make_default: Var[bool]
    position: Var[list[float]]
    fov: Var[float]
    near: Var[float]
    far: Var[float]
    zoom: Var[float]


class OrthographicCamera(DreiComponent):
    """drei ``OrthographicCamera`` -- supports ``makeDefault``."""

    tag = "OrthographicCamera"
    make_default: Var[bool]
    position: Var[list[float]]
    zoom: Var[float]


# ---------------------------------------------------------------------------
# Staging / environment
# ---------------------------------------------------------------------------
class Environment(DreiComponent):
    """``Environment`` -- image-based lighting from an HDRI preset or file."""

    tag = "Environment"
    # One of: city, dawn, forest, lobby, night, park, studio, sunset, warehouse...
    preset: Var[str]
    background: Var[bool]
    files: Var[str | list[str]]
    blur: Var[float]


class Stage(DreiComponent):
    """``Stage`` -- automatic lighting, shadows and centering for a model."""

    tag = "Stage"
    intensity: Var[float]
    environment: Var[str]
    shadows: Var[bool | str | dict[str, Any]]
    adjust_camera: Var[bool]


class ContactShadows(DreiComponent):
    """``ContactShadows`` -- soft blurred ground shadow plane."""

    tag = "ContactShadows"
    position: Var[list[float]]
    opacity: Var[float]
    scale: Var[float | list[float]]
    blur: Var[float]
    far: Var[float]
    resolution: Var[int]
    color: Var[str]


class Sky(DreiComponent):
    """``Sky`` -- a physically-based procedural sky dome."""

    tag = "Sky"
    sun_position: Var[list[float]]
    distance: Var[float]
    inclination: Var[float]
    azimuth: Var[float]
    turbidity: Var[float]
    rayleigh: Var[float]


class Stars(DreiComponent):
    """``Stars`` -- an animated star field."""

    tag = "Stars"
    radius: Var[float]
    depth: Var[float]
    count: Var[int]
    factor: Var[float]
    saturation: Var[float]
    fade: Var[bool]
    speed: Var[float]


class Cloud(DreiComponent):
    """``Cloud`` -- a volumetric-looking billboard cloud."""

    tag = "Cloud"
    opacity: Var[float]
    speed: Var[float]
    segments: Var[int]


class Grid(DreiComponent):
    """``Grid`` -- a high-quality infinite reference grid."""

    tag = "Grid"
    args: Var[list[float]]
    cell_size: Var[float]
    cell_thickness: Var[float]
    cell_color: Var[str]
    section_size: Var[float]
    section_thickness: Var[float]
    section_color: Var[str]
    fade_distance: Var[float]
    infinite_grid: Var[bool]


# ---------------------------------------------------------------------------
# Abstractions / helpers
# ---------------------------------------------------------------------------
class Text(DreiComponent):
    """``Text`` -- SDF text rendered in 3D (troika-three-text)."""

    tag = "Text"
    color: Var[str]
    font_size: Var[float]
    max_width: Var[float]
    line_height: Var[float]
    letter_spacing: Var[float]
    text_align: Var[str]
    anchor_x: Var[str]
    anchor_y: Var[str]
    position: Var[list[float]]
    font: Var[str]


class Text3D(DreiComponent):
    """``Text3D`` -- extruded 3D text from a typeface JSON font."""

    tag = "Text3D"
    font: Var[str]
    size: Var[float]
    height: Var[float]
    curve_segments: Var[int]
    bevel_enabled: Var[bool]


class Html(DreiComponent):
    """``Html`` -- project regular HTML/Reflex content into the 3D scene."""

    tag = "Html"
    position: Var[list[float]]
    center: Var[bool]
    distance_factor: Var[float]
    transform: Var[bool]
    occlude: Var[bool]


class Billboard(DreiComponent):
    """``Billboard`` -- always faces the camera."""

    tag = "Billboard"
    follow: Var[bool]


class Float(DreiComponent):
    """``Float`` -- gently floats/rotates its children for a lively feel."""

    tag = "Float"
    speed: Var[float]
    rotation_intensity: Var[float]
    float_intensity: Var[float]
    floating_range: Var[list[float]]


class Center(DreiComponent):
    """``Center`` -- centers its children around the origin."""

    tag = "Center"
    top: Var[bool]
    disable_y: Var[bool]


class Bounds(DreiComponent):
    """``Bounds`` -- frames its children in the camera view."""

    tag = "Bounds"
    fit: Var[bool]
    clip: Var[bool]
    observe: Var[bool]
    margin: Var[float]


class Edges(DreiComponent):
    """``Edges`` -- crisp outline edges for the parent mesh."""

    tag = "Edges"
    scale: Var[float]
    threshold: Var[float]
    color: Var[str]


class Outlines(DreiComponent):
    """``Outlines`` -- an inverted-hull outline around the parent mesh."""

    tag = "Outlines"
    thickness: Var[float]
    color: Var[str]


class Wireframe(DreiComponent):
    """``Wireframe`` -- a configurable shader wireframe overlay."""

    tag = "Wireframe"
    stroke: Var[str]
    thickness: Var[float]


class GradientTexture(DreiComponent):
    """``GradientTexture`` -- a gradient applied to the parent material's map."""

    tag = "GradientTexture"
    stops: Var[list[float]]
    colors: Var[list[str]]


class MeshDistortMaterial(DreiComponent):
    """``MeshDistortMaterial`` -- animated noise-distorted standard material."""

    tag = "MeshDistortMaterial"
    color: Var[str]
    speed: Var[float]
    distort: Var[float]
    radius: Var[float]
    roughness: Var[float]
    metalness: Var[float]


class MeshWobbleMaterial(DreiComponent):
    """``MeshWobbleMaterial`` -- animated wobble standard material."""

    tag = "MeshWobbleMaterial"
    color: Var[str]
    speed: Var[float]
    factor: Var[float]


class Gltf(DreiComponent):
    """``Gltf`` -- declaratively load and display a .glb/.gltf model.

    ``src`` is a URL to the model. Internally uses drei's ``useGLTF`` loader.
    """

    tag = "Gltf"
    src: Var[str]
    position: Var[list[float]]
    scale: Var[float | list[float]]
    rotation: Var[list[float]]


# Factory functions.
orbit_controls = OrbitControls.create
trackball_controls = TrackballControls.create
fly_controls = FlyControls.create
map_controls = MapControls.create
perspective_camera = PerspectiveCamera.create
orthographic_camera = OrthographicCamera.create
environment = Environment.create
stage = Stage.create
contact_shadows = ContactShadows.create
sky = Sky.create
stars = Stars.create
cloud = Cloud.create
grid = Grid.create
text = Text.create
text_3d = Text3D.create
html = Html.create
billboard = Billboard.create
float_ = Float.create
# `float` shadows the builtin only at module scope and only after all class
# bodies (which use `Var[float]`) are defined, so it is safe and ergonomic.
float = Float.create  # noqa: A001
center = Center.create
bounds = Bounds.create
edges = Edges.create
outlines = Outlines.create
wireframe = Wireframe.create
gradient_texture = GradientTexture.create
mesh_distort_material = MeshDistortMaterial.create
mesh_wobble_material = MeshWobbleMaterial.create
gltf = Gltf.create
