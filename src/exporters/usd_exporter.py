import bpy


def usd_exporter(export_path):
    bpy.ops.export_scene.usd(filepath=export_path)
