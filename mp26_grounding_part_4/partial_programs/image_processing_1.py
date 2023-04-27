from pathlib import Path
from PIL import Image, ImageOps, UnidentifiedImageError

def add_border_to_image(path, border_width, padding, border_color):
    try:
        img = Image.open(path)
    except FileNotFoundError:
        print(f"{path} does not seem to exist.")
        sys.exit()
    except UnidentifiedImageError:
        print(f"{path} does not seem to be an image file.")
        sys.exit()

    new_img = ImageOps.expand(img, border=padding, fill="white")
    new_img = ImageOps.expand(new_img, border=border_width,
            fill=border_color)

    new_path = path.parent / f"{path.stem}_bordered{path.suffix}"
    new_img.save(new_path)

    return new_path