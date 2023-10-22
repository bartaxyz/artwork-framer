import bpy
import os
import sys

# we get blend file path
filepath = bpy.data.filepath

# we get the directory relative to the blend file path
dir = os.path.dirname(filepath)

# we append our path to blender modules path
# we use if not statement to do this one time only
if not dir in sys.path:
   sys.path.append(dir)

from src.constants import FRAME_OBJECT_NAME, PICTURE_OBJECT_NAME, PICTURE_MATERIAL_NAME, PICTURE_MATERIAL_TEXTURE_NAME, TOP_FRAME_EDGE_VERTEX_GROUP, TOP_PICTURE_EDGE_VERTEX_GROUP
from src.utils.get_image_dimensions import get_image_dimensions
from src.exporters.exporter import exporter

# Get the directory of the current script
script_dir = os.path.dirname(os.path.realpath(__file__))

def init():
    # Set object mode
    bpy.ops.object.mode_set(mode='OBJECT')

    # Locate your object by name and collection
    obj = bpy.data.collections['Scene'].objects[FRAME_OBJECT_NAME]

    # Make sure the object is the active object for further operations
    bpy.context.view_layer.objects.active = obj
    obj.select_set(True)


def adjust_frame(amount_to_move):
    obj = bpy.data.collections['Scene'].objects[FRAME_OBJECT_NAME]

    # Access the specific vertex group
    if TOP_FRAME_EDGE_VERTEX_GROUP in obj.vertex_groups:
        vgroup = obj.vertex_groups[TOP_FRAME_EDGE_VERTEX_GROUP]
    else:
        raise Exception("Vertex group " + TOP_FRAME_EDGE_VERTEX_GROUP + " not found!")

    # Iterate over vertices and manipulate those belonging to the vertex group
    for v in obj.data.vertices:
        for g in v.groups:
            if g.group == vgroup.index:
                # Move vertex along the Z-axis
                v.co.y += amount_to_move


def adjust_picture(amount_to_move):
    obj = bpy.data.collections['Scene'].objects[PICTURE_OBJECT_NAME]

    # Access the specific vertex group
    if TOP_PICTURE_EDGE_VERTEX_GROUP in obj.vertex_groups:
        vgroup = obj.vertex_groups[TOP_PICTURE_EDGE_VERTEX_GROUP]
    else:
        raise Exception("Vertex group " + TOP_PICTURE_EDGE_VERTEX_GROUP + " not found!")

    # Iterate over vertices and manipulate those belonging to the vertex group
    for v in obj.data.vertices:
        for g in v.groups:
            if g.group == vgroup.index:
                # Move vertex along the Z-axis
                v.co.y += amount_to_move

def adjust(amount_to_move):
    adjust_frame(amount_to_move)
    adjust_picture(amount_to_move)


def load_image(image_path):
    # Load image into picture object texture
    obj = bpy.data.objects.get(PICTURE_OBJECT_NAME)
    if obj is None:
        raise Exception("Object not found!")
    else:
        mat = bpy.data.materials.get(PICTURE_MATERIAL_NAME)
        if mat is None:
            raise Exception("Material not found!")
        else:
            # Access the shader node tree
            nodes = mat.node_tree.nodes
            tex_image_node = nodes.get(PICTURE_MATERIAL_TEXTURE_NAME)

            if tex_image_node is None:
                raise Exception("'" + PICTURE_MATERIAL_TEXTURE_NAME + "' node not found!")
            else:
                # Update the image
                new_image = bpy.data.images.load(filepath=image_path)
                tex_image_node.image = new_image

    width, height = get_image_dimensions(image_path)
    aspect_ratio = width / height
    amount_to_move = (1 - aspect_ratio) * 4

    # Adjust frame & picture
    adjust(amount_to_move)

    return amount_to_move


def process_images(input_folder, output_folder):
    # Create output directory if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    filetypes = ['.jpg', '.jpeg', '.png']

    format = "gltf"
    
    for filename in os.listdir(input_folder):
        if filename.endswith(tuple(filetypes)):
            print(f"Processing {filename}...")
            
            input_path = os.path.join(input_folder, filename)
            output_filename = os.path.splitext(filename)[0] + "." + format
            output_path = os.path.join(output_folder, output_filename)

            amount_to_move = load_image(input_path)
            exporter(format=format, output_path=output_path)

            # Reset frame & picture
            adjust(-amount_to_move)


if __name__ == "__main__":
    init()
    
    script_dir = os.path.dirname(os.path.abspath(__file__))  # Assuming you have this line
    input_folder = os.path.join(script_dir, 'input')
    output_folder = os.path.join(script_dir, 'output')

    process_images(input_folder, output_folder)
