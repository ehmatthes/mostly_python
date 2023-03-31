"""Add a border to any image."""

import sys
from pathlib import Path
from PIL import Image, ImageOps

# Load the image.
path = Path(sys.argv[1])
img = Image.open(path)

# Set the border width and color.
border_width = 2
border_color = "darkgray"

# Add the border.
new_img = ImageOps.expand(img, border=border_width,
        fill=border_color)

# Save new image.
new_path = path.parent / f"{path.stem}_bordered{path.suffix}"
print(new_path)
# new_img.save(new_path)