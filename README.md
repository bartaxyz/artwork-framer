# Artwork Framer

Embedding images into a 3D frame using Blender. It scales the frame according to the aspect ratio of each input image and exports the resulting model.

![untitled](https://github.com/bartaxyz/artwork-framer/assets/4202010/bbf475e3-ac4d-40b8-97ac-43e5c0ad870d)

## Requirements

- Blender
- Python 3.x

## File Structure

- `input/`: Folder containing images to be processed.
- `output/`: Folder where processed USDZ models will be stored.
- `frame.blend`: Blender file containing the 3D frame model.
- `main.py`: Python script that handles image embedding, frame scaling, and USDZ export.

## Usage

There are two main ways to run the script: via command line or inside Blender.

The command line method is preferred, since it's the easiest to set up and use. The Blender method is useful if you want to make changes to the script and test them out.

Regardless, the script will process all images in the `input/` directory and store the resulting models in the `output/` directory (by default in GLTF format).

_Currently, the format is hard-coded in the script. You can find it in the `main.py` file if you want to change it (`CMD + F` and `Ctrl + F` are your friends)._

### Running the Script via Command Line (preferred)

#### Prerequisites

There are a couple of steps to make this all work.

1. Find out your Blender path ([check official Blender docs for instructions](https://docs.blender.org/manual/en/latest/advanced/command_line/launch/index.html))
2. Create `.env`, and set `BLENDER_PATH` to the path you found in step 1.
3. You might need to make the script executable: `chmod +x artwork-framer.sh`

#### Running the Script

Once you're set up, you can run the script.

```bash
./artwork-framer.sh
```

This will process all the images, and you should see the output models in the `output/` directory.

### Running the Script Inside Blender

- Open frame.blend in Blender.
- Open the main.py script in Blender's text editor.
- Run the script.

## Batch Processing

To run batch processing of images, simply place all images in the `input/` directory before running the script. The script will process all images and store the output models in `output/`.

## Changing the frame

If you want to change the frame, you can do so by opening the `frame.blend` file in Blender and making the changes you want.

The script works by moving the top vertices of the frame upwards to match the aspect ratio of the input image. This means that the frame object must be a rectangle, and you need to follow a couple of rules.

- Keep the frame & picture objects named `Frame` & `Picture` respectively.

- Keep the dimensions of the `Picture` object to `2 x 2` (the default). _You can change the depth of the picture (Y axis), but the width and height must remain the same._

- If you make any changes to the frame, you might need to reassign the vertices at the top of the frame to the `Top Frame Edge` vertex group.

| <img width="822" alt="Screenshot 2023-10-23 at 22 37 08" src="https://github.com/bartaxyz/artwork-framer/assets/4202010/f4b36d3c-a924-4128-97af-b5faab5c61e0"> | <img width="250" alt="Screenshot 2023-10-23 at 22 37 02" src="https://github.com/bartaxyz/artwork-framer/assets/4202010/06d0fc2e-ac0e-4eea-9f48-99a0ee62b873"> |
| --- | --- |

- If you make any changes to the picture, you might need to reassign the vertices at the top of the picture to the `Top Picture Edge` vertex group.

| <img width="831" alt="Screenshot 2023-10-23 at 22 35 00" src="https://github.com/bartaxyz/artwork-framer/assets/4202010/b71bf0bd-d01b-4502-a845-732e0d151ad6"> | <img width="251" alt="Screenshot 2023-10-23 at 22 34 46" src="https://github.com/bartaxyz/artwork-framer/assets/4202010/1be3ed9d-a96d-40c6-a461-21709d9d315c"> |
| --- | --- |

## Contributing

Feel free to fork this repository or submit PRs for improvements.
