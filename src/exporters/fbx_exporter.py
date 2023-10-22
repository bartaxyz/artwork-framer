import bpy
import logging


def fbx_exporter(export_path):
    bpy.ops.export_scene.fbx(
        filepath=export_path,
        use_mesh_modifiers=True,
        path_mode='COPY',
        embed_textures=True
    )
