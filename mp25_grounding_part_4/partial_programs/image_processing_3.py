from pathlib import Path
from PIL import Image, ImageOps, UnidentifiedImageError
from cli_args import ImageBorderArgs

def add_border_to_image(args: ImageBorderArgs):
    try:
        img = Image.open(args.path)
    except FileNotFoundError:
        print(f"{args.path} does not seem to exist.")
        sys.exit()
    except UnidentifiedImageError:
        print(f"{args.path} does not seem to be an image file.")
        sys.exit()

    new_img = ImageOps.expand(img, border=args.padding, fill="white")
    new_img = ImageOps.expand(new_img, border=args.border_width,
            fill=args.border_color)

    new_path = (args.path.parent /
            f"{args.path.stem}_bordered{args.path.suffix}")
    new_img.save(new_path)

    return new_path