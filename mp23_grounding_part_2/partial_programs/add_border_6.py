"""Add a border to any image."""

import sys
from pathlib import Path
from PIL import Image, ImageOps, UnidentifiedImageError

# Get the filename.
try:
    path = Path(sys.argv[1])
except IndexError:
    print("You must provide a target image.")
    sys.exit()

# --- Get optional CLI args. ---
try:
    border_width = int(sys.argv[2])
except IndexError:
    border_width = 2

# Load the image.
try:
    img = Image.open(path)
except FileNotFoundError:
    print(f"{path} does not seem to exist.")
    sys.exit()
except UnidentifiedImageError:
    print(f"{path} does not seem to be an image file.")
    sys.exit()

# Set the border width and color.
border_color = "darkgray"

# Add the border.
new_img = ImageOps.expand(img, border=border_width,
        fill=border_color)

# Save new image.
new_path = path.parent / f"{path.stem}_bordered{path.suffix}"
new_img.save(new_path)