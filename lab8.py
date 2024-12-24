import bpy
import math
import random

bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(use_global=False)

def create_snake_segment(location, size):
    bpy.ops.mesh.primitive_uv_sphere_add(radius=size, location=location)
    segment = bpy.context.object
    return segment

def create_snake(length, segment_size):
    x, y, z = 0, 0, 0
    for i in range(length):
        segment = create_snake_segment((x, y, z), segment_size)
        segment.name = f"Snake_Segment_{i}"
        x += segment_size * 2  # Сегменты смещаются по оси X
        y += random.uniform(-0.1, 0.1)  # Небольшие отклонения для реализма
        z += random.uniform(-0.1, 0.1)

def create_christmas_tree(location, height, base_radius):
    bpy.ops.mesh.primitive_cylinder_add(radius=base_radius/4, depth=height/5, location=location)
    trunk = bpy.context.object
    trunk.name = "Tree_Trunk"
    trunk.location.z += height / 10

    # Слои ёлки
    for i in range(3):
        bpy.ops.mesh.primitive_cone_add(vertices=32, radius1=base_radius * (1 - 0.2 * i), depth=height / 3,
                                        location=(location[0], location[1], location[2] + (i + 1) * (height / 6)))
        cone = bpy.context.object
        cone.name = f"Tree_Layer_{i}"

def create_christmas_decorations(count):
    for _ in range(count):
        x = random.uniform(-10, 10)
        y = random.uniform(-10, 10)
        z = random.uniform(0, 5)
        bpy.ops.mesh.primitive_ico_sphere_add(radius=random.uniform(0.1, 0.3), location=(x, y, z))
        sphere = bpy.context.object
        sphere.name = "Decoration"
        sphere.material_slots.new()
        sphere.active_material.diffuse_color = (random.random(), random.random(), random.random(), 1)

def create_snow():
    bpy.ops.mesh.primitive_plane_add(size=20, location=(0, 0, 0))
    plane = bpy.context.object
    plane.name = "Ground"
    bpy.ops.object.modifier_add(type='SUBSURF')
    bpy.ops.object.shade_smooth()

def setup_camera(location, rotation):
    bpy.ops.object.camera_add(location=location, rotation=rotation)
    camera = bpy.context.object
    camera.name = "Camera"
    bpy.context.scene.camera = camera

def setup_lighting(location):
    bpy.ops.object.light_add(type='POINT', location=location)
    light = bpy.context.object
    light.name = "Light"
    light.data.energy = 1000

def create_scene():
    create_snow()
    create_snake(length=10, segment_size=0.3)
    create_christmas_tree(location=(0, -2, 0), height=3, base_radius=1)
    create_christmas_decorations(count=20)
    setup_camera(location=(7, -7, 5), rotation=(math.radians(60), 0, math.radians(45)))
    setup_lighting(location=(0, 0, 5))

create_scene()
