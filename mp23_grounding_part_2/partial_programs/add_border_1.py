"""Add a border to any image."""

from pathlib import Path
from PIL import Image, ImageOps

# Load the image.
path = Path("willie_mountains.png")
img = Image.open(path)

# Set the border width and color.
border_width = 2
border_color = "darkgray"

# Add the border.
new_img = ImageOps.expand(img, border=border_width,
        fill=border_color)

# Save new image.
new_path = Path("willie_mountains_bordered.png")
new_img.save(new_path)