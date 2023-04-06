"""Functions to process the image."""

from PIL import Image, ImageOps, UnidentifiedImageError

def load_image(path):
    """Load the image file."""
    try:
        return Image.open(path)
    except UnidentifiedImageError:
        print(f"{path} does not seem to be an image file.")
        sys.exit()

def process_image(img, options):
    """Modify the original image."""

    # Add some padding before adding the border.
    # The padding is just a white border added before
    #   the actual border.
    new_img = ImageOps.expand(img, border=options['padding'],
                fill="white")

    # Add the border.
    new_img = ImageOps.expand(new_img,
        border=options['border_width'],
        fill=options['border_color'])

    return new_img

def save_image(path, new_img):
    """Save the new image."""
    new_path = path.parent / f"{path.stem}_bordered{path.suffix}"
    new_img.save(new_path)