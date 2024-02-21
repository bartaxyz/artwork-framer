#!/bin/bash

# Load environment variables from .env file
export $(grep -v '^#' .env | xargs)

# If .env file does not exist
if [ ! -f .env ]; then
  echo "Please create a .env file."
  exit 1
fi

# Check if BLENDER_PATH is set
if [ -z "$BLENDER_PATH" ]; then
  echo "Please set the BLENDER_PATH in the .env file."
  exit 1
fi

# Parse arguments
while [ $# -gt 0 ]; do

   if [[ $1 == --* ]]; then
     v="${1/--/}"
     declare ${v}="$2"
   fi

  shift
done

# Get --artwork-label argument
ARTWORK_LABEL=${artwork_label:-""}

# Execute the Blender command
$BLENDER_PATH -b $(pwd)/frame.blend -P $(pwd)/main.py -- --artwork_label $ARTWORK_LABEL
