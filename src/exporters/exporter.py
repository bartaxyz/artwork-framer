import bpy
import logging

from src.constants import EXPORTABLE_OBJECTS
from src.exporters.fbx_exporter import fbx_exporter
from src.exporters.gltf_exporter import gltf_exporter
from src.exporters.obj_exporter import obj_exporter
from src.exporters.usd_exporter import usd_exporter
from src.exporters.usdz_exporter import usdz_exporter


def exporter(format, output_path):
    # De-select all objects
    for obj in bpy.context.scene.objects:
        obj.select_set(False)

    # Select the exportable objects
    for obj_name in EXPORTABLE_OBJECTS:
        bpy.context.view_layer.objects.active = bpy.context.scene.objects[obj_name]
        bpy.context.selected_objects.append(
            bpy.context.scene.objects[obj_name])

    if format == "fbx":
        fbx_exporter(output_path)
    elif format == "gltf":
        gltf_exporter(output_path)
    elif format == "obj":
        obj_exporter(output_path)
    elif format == "usd":
        usd_exporter(output_path)
    elif format == "usdz":
        usdz_exporter(output_path)
    else:
        raise Exception("Unsupported format " + format)
