import bpy


def obj_exporter(export_path):
    bpy.ops.export_scene.obj(filepath=export_path)
