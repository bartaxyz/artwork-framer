import bpy


def gltf_exporter(export_path):
    bpy.ops.export_scene.gltf(filepath=export_path, export_format='GLTF_EMBEDDED')
