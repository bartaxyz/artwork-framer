import bpy


def get_image_dimensions(blender_image_path):
    image = bpy.data.images.load(blender_image_path)
    width = image.size[0]
    height = image.size[1]

    # Remove the image from memory
    bpy.data.images.remove(image)

    return width, height
