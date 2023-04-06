"""Add a border to any image."""

import sys
from pathlib import Path
from PIL import Image, ImageOps, UnidentifiedImageError

def process_cli_args(options):
    """Process all CLI arguments."""
    # Get the filename.
    try:
        path = Path(sys.argv[1])
    except IndexError:
        print("You must provide a target image.")
        sys.exit()

    # --- Get optional CLI args. ---
    if len(sys.argv) >= 3:
        options['border_width'] = int(sys.argv[2])
    if len(sys.argv) >= 4:
        options['padding'] = int(sys.argv[3])
    if len(sys.argv) >= 5:
        options['border_color'] = sys.argv[4]

    return path

# Set default options.
options = {
    'border_width': 2,
    'padding': 0,
    'border_color': 'lightgray'
}
path = process_cli_args(options)

# Load the image.
try:
    img = Image.open(path)
except FileNotFoundError:
    print(f"{path} does not seem to exist.")
    sys.exit()
except UnidentifiedImageError:
    print(f"{path} does not seem to be an image file.")
    sys.exit()

# Add some padding before adding the border.
# The padding is just a white border added before
#   the actual border.
new_img = ImageOps.expand(img, border=options['padding'],
            fill="white")

# Add the border.
new_img = ImageOps.expand(new_img,
    border=options['border_width'],
    fill=options['border_color'])

# Save new image.
new_path = path.parent / f"{path.stem}_bordered{path.suffix}"
new_img.save(new_path)