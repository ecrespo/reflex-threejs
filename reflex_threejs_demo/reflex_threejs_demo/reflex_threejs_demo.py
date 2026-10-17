"""reflex-threejs demo app.

A gallery of interactive 3D scenes that exercises the wrapped React Three
Fiber / drei components. Each route renders one scene inside a shared layout.
"""

from __future__ import annotations

import reflex as rx
from reflex_threejs import three

from .state import DemoState

# ---------------------------------------------------------------------------
# Scene catalog: (slug, title, description)
# ---------------------------------------------------------------------------
EXAMPLES: list[tuple[str, str, str]] = [
    ("/", "Hello Cube", "A lit, orbitable cube — the 'hello world' of 3D."),
    ("/geometries", "Geometry Gallery", "A row of three.js built-in geometries."),
    ("/materials", "Materials", "One sphere, many material types."),
    ("/lights", "Lights", "Ambient, directional, point and spot lights."),
    ("/interactive", "Interactive", "Click to recolor, hover to scale."),
    ("/particles", "Particles", "A points cloud built from a buffer geometry."),
    ("/staging", "Staging & drei", "Environment, contact shadows and float."),
    ("/text", "3D Text", "SDF text rendered in the scene with drei."),
    ("/space", "Space", "A procedural sky of stars."),
]

SCENE_HEIGHT = "70vh"


# ---------------------------------------------------------------------------
# Scenes
# ---------------------------------------------------------------------------
def scene_hello() -> rx.Component:
    """Hello Cube: a lit, orbitable cube — the canonical 3D scene."""
    return three.canvas(
        three.color(attach="background", args=["#0b1020"]),
        three.ambient_light(intensity=0.5),
        three.directional_light(position=[5, 5, 5], intensity=1.2),
        three.mesh(
            three.box_geometry(args=[1.5, 1.5, 1.5]),
            three.mesh_standard_material(color="#6366f1", metalness=0.3, roughness=0.4),
        ),
        three.orbit_controls(auto_rotate=True, auto_rotate_speed=1.5),
        camera={"position": [3, 3, 3], "fov": 50},
    )


def scene_geometries() -> rx.Component:
    """Geometry Gallery: a row of three.js built-in geometries."""
    specs = [
        (three.box_geometry(args=[1, 1, 1]), -4.5),
        (three.sphere_geometry(args=[0.7, 32, 32]), -3),
        (three.cone_geometry(args=[0.7, 1.4, 32]), -1.5),
        (three.torus_geometry(args=[0.6, 0.25, 16, 48]), 0),
        (three.torus_knot_geometry(args=[0.5, 0.18, 96, 16]), 1.5),
        (three.icosahedron_geometry(args=[0.8, 0]), 3),
        (three.cylinder_geometry(args=[0.5, 0.5, 1.3, 32]), 4.5),
    ]
    meshes = [
        three.mesh(
            geom,
            three.mesh_normal_material(flat_shading=True),
            position=[x, 0, 0],
        )
        for geom, x in specs
    ]
    return three.canvas(
        three.color(attach="background", args=["#11131a"]),
        three.ambient_light(intensity=0.8),
        *meshes,
        three.orbit_controls(auto_rotate=True, auto_rotate_speed=0.8),
        camera={"position": [0, 1.5, 9], "fov": 50},
    )


def scene_materials() -> rx.Component:
    """Materials: one sphere rendered with several material types."""
    mats = [
        (three.mesh_standard_material(color="#e11d48", metalness=0.1, roughness=0.2), -4.5),
        (three.mesh_physical_material(color="#22d3ee", clearcoat=1.0, roughness=0.1), -2.25),
        (three.mesh_phong_material(color="#a3e635", shininess=100), 0),
        (three.mesh_toon_material(color="#f59e0b"), 2.25),
        (three.mesh_normal_material(), 4.5),
    ]
    meshes = [
        three.mesh(three.sphere_geometry(args=[0.9, 64, 64]), m, position=[x, 0, 0])
        for m, x in mats
    ]
    return three.canvas(
        three.color(attach="background", args=["#0b1020"]),
        three.ambient_light(intensity=0.4),
        three.directional_light(position=[5, 5, 5], intensity=1.5),
        three.point_light(position=[-5, -2, -3], intensity=0.6, color="#ff66cc"),
        *meshes,
        three.environment(preset="city"),
        three.orbit_controls(),
        camera={"position": [0, 0, 9], "fov": 50},
    )


def scene_lights() -> rx.Component:
    """Lights: ambient, directional, point and spot lights with shadows."""
    return three.canvas(
        three.color(attach="background", args=["#05070d"]),
        three.ambient_light(intensity=0.15),
        three.directional_light(position=[5, 5, 5], intensity=1.0, cast_shadow=True),
        three.point_light(position=[-3, 2, 2], intensity=0.8, color="#60a5fa"),
        three.spot_light(
            position=[0, 6, 0], angle=0.4, penumbra=0.6, intensity=1.2, cast_shadow=True
        ),
        three.mesh(
            three.torus_knot_geometry(args=[1, 0.32, 160, 32]),
            three.mesh_standard_material(color="#e5e7eb", metalness=0.5, roughness=0.2),
            cast_shadow=True,
        ),
        three.mesh(
            three.plane_geometry(args=[30, 30]),
            three.mesh_standard_material(color="#1f2937"),
            rotation=[-1.5708, 0, 0],
            position=[0, -2.2, 0],
            receive_shadow=True,
        ),
        three.orbit_controls(),
        # three r182+ deprecates PCFSoftShadowMap (R3F's `shadows=True`); the
        # default PCFShadowMap is now soft, so request it directly.
        shadows="percentage",
        camera={"position": [0, 2, 7], "fov": 50},
    )


def scene_interactive() -> rx.Component:
    """Interactive: click to recolor and hover to scale, driven by state."""
    scale = rx.cond(DemoState.hovered, [1.3, 1.3, 1.3], [1.0, 1.0, 1.0])
    return three.canvas(
        three.color(attach="background", args=["#0b1020"]),
        three.ambient_light(intensity=0.6),
        three.directional_light(position=[4, 5, 3], intensity=1.2),
        three.mesh(
            three.dodecahedron_geometry(args=[1.2, 0]),
            three.mesh_standard_material(color=DemoState.active_color, roughness=0.35),
            scale=scale,
            on_click=DemoState.next_color,
            on_pointer_over=lambda: DemoState.set_hovered(True),
            on_pointer_out=lambda: DemoState.set_hovered(False),
        ),
        three.orbit_controls(enable_pan=False),
        camera={"position": [0, 0, 5], "fov": 50},
    )


def scene_particles() -> rx.Component:
    """Particles: a points cloud built from a buffer geometry."""
    # 2000 points scattered in a cube via a buffer attribute.
    import random

    random.seed(7)
    positions: list[float] = []
    for _ in range(2000):
        positions += [random.uniform(-5, 5) for _ in range(3)]
    return three.canvas(
        three.color(attach="background", args=["#05070d"]),
        three.points(
            three.buffer_geometry(
                # args=[array, itemSize]; the flat list compiles to a Float32Array.
                three.buffer_attribute(attach="attributes-position", args=[positions, 3]),
            ),
            three.points_material(color="#22d3ee", size=0.05, size_attenuation=True),
        ),
        three.orbit_controls(auto_rotate=True, auto_rotate_speed=0.4),
        camera={"position": [0, 0, 10], "fov": 60},
    )


def scene_staging() -> rx.Component:
    """Staging & drei: Stage, ContactShadows and an animated distort material."""
    return three.canvas(
        three.drei.stage(
            three.mesh(
                three.torus_knot_geometry(args=[1, 0.3, 160, 32]),
                three.drei.mesh_distort_material(
                    color="#8b5cf6", speed=2, distort=0.4, roughness=0.1, metalness=0.2
                ),
            ),
            environment="city",
            intensity=0.6,
        ),
        three.drei.contact_shadows(
            position=[0, -1.4, 0], opacity=0.6, scale=12, blur=2.4, far=4.5
        ),
        three.orbit_controls(auto_rotate=True),
        # three r182+ deprecates PCFSoftShadowMap (R3F's `shadows=True`); the
        # default PCFShadowMap is now soft, so request it directly.
        shadows="percentage",
        camera={"position": [0, 1.5, 6], "fov": 50},
    )


def scene_text() -> rx.Component:
    """3D Text: SDF text floating in the scene via drei Text and Float."""
    return three.canvas(
        three.color(attach="background", args=["#0b1020"]),
        three.ambient_light(intensity=0.7),
        three.directional_light(position=[3, 4, 5], intensity=1.0),
        three.drei.float(
            three.drei.text(
                "reflex-threejs",
                color="#e2e8f0",
                font_size=1.2,
                anchor_x="center",
                anchor_y="middle",
            ),
            speed=2,
            rotation_intensity=0.6,
            float_intensity=1.2,
        ),
        three.orbit_controls(enable_zoom=False),
        camera={"position": [0, 0, 6], "fov": 50},
    )


def scene_space() -> rx.Component:
    """Space: a procedural star field around an emissive sphere."""
    return three.canvas(
        three.color(attach="background", args=["#01010a"]),
        three.drei.stars(radius=80, depth=50, count=6000, factor=4, fade=True, speed=1),
        three.ambient_light(intensity=0.3),
        three.point_light(position=[0, 0, 0], intensity=2, color="#fef08a"),
        three.mesh(
            three.sphere_geometry(args=[1.2, 64, 64]),
            three.mesh_standard_material(
                color="#fbbf24", emissive="#f59e0b", emissive_intensity=0.6
            ),
        ),
        three.orbit_controls(auto_rotate=True, auto_rotate_speed=0.3),
        camera={"position": [0, 0, 6], "fov": 60},
    )


SCENES = {
    "/": scene_hello,
    "/geometries": scene_geometries,
    "/materials": scene_materials,
    "/lights": scene_lights,
    "/interactive": scene_interactive,
    "/particles": scene_particles,
    "/staging": scene_staging,
    "/text": scene_text,
    "/space": scene_space,
}


# ---------------------------------------------------------------------------
# Layout
# ---------------------------------------------------------------------------
def sidebar_link(slug: str, title: str, desc: str) -> rx.Component:
    """Render one navigation link in the sidebar."""
    return rx.link(
        rx.box(
            rx.text(title, weight="bold", size="2"),
            rx.text(desc, size="1", color_scheme="gray"),
            padding="0.6em 0.8em",
            border_radius="8px",
            _hover={"background": rx.color("indigo", 3)},
            width="100%",
        ),
        href=slug,
        width="100%",
        text_decoration="none",
        color="inherit",
    )


def layout(slug: str, scene: rx.Component) -> rx.Component:
    """Wrap a scene in the shared sidebar + heading layout."""
    current = next((t for s, t, _ in EXAMPLES if s == slug), "Demo")
    return rx.hstack(
        rx.vstack(
            rx.heading("reflex-threejs", size="5"),
            rx.text("React Three Fiber × Reflex", size="1", color_scheme="gray"),
            rx.divider(),
            rx.vstack(
                *[sidebar_link(s, t, d) for s, t, d in EXAMPLES],
                spacing="1",
                width="100%",
            ),
            rx.spacer(),
            rx.link("GitHub", href="https://github.com/ecrespo/reflex-threejs", size="1"),
            width="280px",
            height="100vh",
            padding="1.2em",
            border_right=f"1px solid {rx.color('gray', 5)}",
            align="start",
            overflow_y="auto",
        ),
        rx.vstack(
            rx.heading(current, size="6"),
            rx.box(
                scene,
                width="100%",
                height=SCENE_HEIGHT,
                border_radius="12px",
                overflow="hidden",
                border=f"1px solid {rx.color('gray', 5)}",
            ),
            rx.text(
                "Drag to orbit · scroll to zoom · right-drag to pan",
                size="1",
                color_scheme="gray",
            ),
            width="100%",
            padding="1.5em",
            spacing="3",
        ),
        width="100%",
        align="start",
        spacing="0",
    )


# ---------------------------------------------------------------------------
# App + routes
# ---------------------------------------------------------------------------
app = rx.App(
    theme=rx.theme(appearance="dark", accent_color="indigo", radius="large"),
)

for _slug, _title, _desc in EXAMPLES:
    def _make_page(slug=_slug):
        return lambda: layout(slug, SCENES[slug]())

    app.add_page(_make_page(), route=_slug, title=f"reflex-threejs · {_title}")
