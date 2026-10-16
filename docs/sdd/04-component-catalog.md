# reflex-threejs — Component Catalog (Data Model)

This is the "schema" of the library: every component, the React tag it emits,
the npm package it imports (if any), and its primary props. In an SDD data
model, components are our entities and props are our fields.

| Field | Value |
|---|---|
| **Status** | `DRAFT` |
| **Version** | 1.0 |
| **Date** | 2026-06-14 |

---

## 1. Conventions

- **Tag**: the JSX tag emitted. Lowercase ⇒ R3F host element (no import).
- **Import**: the npm package, or `—` for host elements.
- **`args`**: positional three.js constructor arguments, passed as a list.
- Every host element inherits: `position`, `rotation`, `scale`, `visible`, `args`.

## 2. Root

| Component | Factory | Tag | Import | Key props |
|---|---|---|---|---|
| Canvas | `three.canvas` | `Canvas` | `@react-three/fiber` | `camera`, `shadows`, `dpr`, `gl`, `frameloop`, `orthographic`, `flat`, `on_created` |

`Canvas` is a `NoSSRComponent` (dynamic import, `ssr:false`).

## 3. Objects (Object3D)

| Component | Factory | Tag | Notes |
|---|---|---|---|
| Group | `three.group` | `group` | transform container |
| Mesh | `three.mesh` | `mesh` | geometry+material; full pointer events; `cast_shadow`, `receive_shadow` |
| InstancedMesh | `three.instanced_mesh` | `instancedMesh` | `args=[geometry, material, count]` |
| Points | `three.points` | `points` | particle cloud |
| Line | `three.line` | `line` (alias) | three.js line |
| LineSegments | `three.line_segments` | `lineSegments` | discrete segments |
| LineLoop | `three.line_loop` | `lineLoop` | closed polyline |
| Sprite | `three.sprite` | `sprite` | camera-facing billboard |
| Primitive | `three.primitive` | `primitive` | attach a pre-built three.js object (`object=`) |

**Mesh events:** `on_click`, `on_double_click`, `on_pointer_over`,
`on_pointer_out`, `on_pointer_down`, `on_pointer_up`, `on_pointer_move`,
`on_wheel`.

## 4. Geometries

All emit lowercase `*Geometry` tags; tune via `args` (constructor params).

| Factory | Tag | `args` signature |
|---|---|---|
| `box_geometry` | `boxGeometry` | width, height, depth, …segments |
| `sphere_geometry` | `sphereGeometry` | radius, widthSeg, heightSeg |
| `plane_geometry` | `planeGeometry` | width, height, wSeg, hSeg |
| `circle_geometry` | `circleGeometry` | radius, segments |
| `ring_geometry` | `ringGeometry` | inner, outer, segments |
| `cylinder_geometry` | `cylinderGeometry` | radTop, radBottom, height, radialSeg |
| `cone_geometry` | `coneGeometry` | radius, height, radialSeg |
| `torus_geometry` | `torusGeometry` | radius, tube, radialSeg, tubularSeg |
| `torus_knot_geometry` | `torusKnotGeometry` | radius, tube, tubSeg, radSeg, p, q |
| `dodecahedron_geometry` | `dodecahedronGeometry` | radius, detail |
| `icosahedron_geometry` | `icosahedronGeometry` | radius, detail |
| `octahedron_geometry` | `octahedronGeometry` | radius, detail |
| `tetrahedron_geometry` | `tetrahedronGeometry` | radius, detail |
| `capsule_geometry` | `capsuleGeometry` | radius, height, capSeg, radialSeg, heightSeg |
| `lathe_geometry` | `latheGeometry` | points, segments, phiStart, phiLength |
| `tube_geometry` | `tubeGeometry` | path, tubularSeg, radius, radialSeg, closed |
| `extrude_geometry` | `extrudeGeometry` | shapes, options |
| `shape_geometry` | `shapeGeometry` | shapes, curveSegments |
| `edges_geometry` | `edgesGeometry` | geometry, thresholdAngle |
| `wireframe_geometry` | `wireframeGeometry` | geometry |
| `buffer_geometry` | `bufferGeometry` | (filled with `buffer_attribute` children) |
| `buffer_attribute` | `bufferAttribute` | `attach`, `args=[array, itemSize]` |

## 5. Materials

Shared props: `color`, `opacity`, `transparent`, `wireframe`, `side`,
`flat_shading`, `vertex_colors`, `depth_write`, `depth_test`, `attach`.

| Factory | Tag | Extra props |
|---|---|---|
| `mesh_basic_material` | `meshBasicMaterial` | (unlit) |
| `mesh_standard_material` | `meshStandardMaterial` | `metalness`, `roughness`, `emissive`, `emissive_intensity`, `env_map_intensity` |
| `mesh_physical_material` | `meshPhysicalMaterial` | `clearcoat`, `transmission`, `thickness`, `ior`, `sheen`, `reflectivity` |
| `mesh_phong_material` | `meshPhongMaterial` | `shininess`, `specular`, `emissive` |
| `mesh_lambert_material` | `meshLambertMaterial` | `emissive` |
| `mesh_toon_material` | `meshToonMaterial` | — |
| `mesh_normal_material` | `meshNormalMaterial` | — |
| `mesh_matcap_material` | `meshMatcapMaterial` | — |
| `mesh_depth_material` | `meshDepthMaterial` | — |
| `line_basic_material` | `lineBasicMaterial` | `linewidth` |
| `line_dashed_material` | `lineDashedMaterial` | `dash_size`, `gap_size`, `scale` |
| `points_material` | `pointsMaterial` | `size`, `size_attenuation` |
| `sprite_material` | `spriteMaterial` | `rotation` |
| `shader_material` | `shaderMaterial` | `vertex_shader`, `fragment_shader`, `uniforms` |

## 6. Lights

Shared props: `color`, `intensity`.

| Factory | Tag | Extra props |
|---|---|---|
| `ambient_light` | `ambientLight` | — |
| `directional_light` | `directionalLight` | `cast_shadow`, `shadow_bias` |
| `point_light` | `pointLight` | `distance`, `decay`, `cast_shadow` |
| `spot_light` | `spotLight` | `angle`, `penumbra`, `distance`, `decay`, `cast_shadow` |
| `hemisphere_light` | `hemisphereLight` | `ground_color` |
| `rect_area_light` | `rectAreaLight` | `width`, `height` |

## 7. Cameras & Helpers (host)

| Factory | Tag | Notes |
|---|---|---|
| `perspective_camera` | `perspectiveCamera` | `fov`, `near`, `far`, `zoom` |
| `orthographic_camera` | `orthographicCamera` | `left`/`right`/`top`/`bottom`, `zoom` |
| `grid_helper` | `gridHelper` | `args=[size, divisions, c1, c2]` |
| `polar_grid_helper` | `polarGridHelper` | — |
| `axes_helper` | `axesHelper` | `args=[size]` |
| `box_helper` | `boxHelper` | — |
| `fog` | `fog` | `attach="fog"`, `args=[color, near, far]` |
| `fog_exp2` | `fogExp2` | `attach="fog"`, `args=[color, density]` |
| `color` | `color` | `attach="background"`, `args=[color]` |

## 8. drei helpers (`@react-three/drei`)

| Group | Factory | Tag |
|---|---|---|
| Controls | `three.drei.orbit_controls` | `OrbitControls` |
| | `three.drei.trackball_controls` | `TrackballControls` |
| | `three.drei.fly_controls` | `FlyControls` |
| | `three.drei.map_controls` | `MapControls` |
| Cameras | `three.drei.perspective_camera` | `PerspectiveCamera` (`make_default`) |
| | `three.drei.orthographic_camera` | `OrthographicCamera` (`make_default`) |
| Staging | `three.drei.environment` | `Environment` (`preset`) |
| | `three.drei.stage` | `Stage` |
| | `three.drei.contact_shadows` | `ContactShadows` |
| | `three.drei.sky` | `Sky` |
| | `three.drei.stars` | `Stars` |
| | `three.drei.cloud` | `Cloud` |
| | `three.drei.grid` | `Grid` |
| Abstractions | `three.drei.text` | `Text` |
| | `three.drei.text_3d` | `Text3D` |
| | `three.drei.html` | `Html` |
| | `three.drei.billboard` | `Billboard` |
| | `three.drei.float` | `Float` |
| | `three.drei.center` | `Center` |
| | `three.drei.bounds` | `Bounds` |
| | `three.drei.edges` | `Edges` |
| | `three.drei.outlines` | `Outlines` |
| | `three.drei.wireframe` | `Wireframe` |
| | `three.drei.gradient_texture` | `GradientTexture` |
| Animated materials | `three.drei.mesh_distort_material` | `MeshDistortMaterial` |
| | `three.drei.mesh_wobble_material` | `MeshWobbleMaterial` |
| Loaders | `three.drei.gltf` | `Gltf` (`src=`) |

## 9. Mapping to three.js example categories

| three.js example category | Covered by | Demo scene |
|---|---|---|
| geometry | geometry host elements | Geometry Gallery |
| materials | material host elements + drei animated | Materials, Staging |
| lights / shadows | lights + `Canvas(shadows=True)` | Lights |
| points / particles | `points` + `bufferGeometry` | Particles |
| interaction / raycast | mesh pointer events | Interactive |
| loaders (GLTF) | `drei.gltf` | (guide example) |
| helpers | grid/axes helpers | Geometry Gallery |
| environment / staging | drei `Environment`, `ContactShadows` | Staging |
| sprites / text | `sprite`, drei `Text` | 3D Text |
| sky / stars | drei `Sky`, `Stars` | Space |
| post-processing | _planned v0.3_ | — |
| physics | _planned v0.4_ | — |

---

## Change History

| Version | Date | Author | Changes |
|---|---|---|---|
| 1.0 | 2026-06-14 | Ernesto Crespo | Initial version |
