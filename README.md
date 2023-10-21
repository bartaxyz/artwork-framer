# Artwork Framer

Embedding images into a 3D frame using Blender. It scales the frame according to the aspect ratio of each input image and exports the resulting model.

## Requirements

- Blender
- Python 3.x

## File Structure

- `input/`: Folder containing images to be processed.
- `output/`: Folder where processed USDZ models will be stored.
- `frame.blend`: Blender file containing the 3D frame model.
- `main.py`: Python script that handles image embedding, frame scaling, and USDZ export.

## Usage

First, install the required Python packages:

```
pip install -r requirements.txt
```

### Running the Script Inside Blender

- Open frame.blend in Blender.
- Open the main.py script in Blender's text editor.
- Run the script.

### Running the Script via Command Line

Run the following command to process all images in the input_images/ folder:

```
blender frame.blend --background --python main.py
```

## Batch Processing

To run batch processing of images, simply place all images in the `input/` directory before running the script. The script will process all images and store the output models in `output/`.

## Contributing

Feel free to fork this repository or submit PRs for improvements.
