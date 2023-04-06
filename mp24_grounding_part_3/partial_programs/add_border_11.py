"""Add a border to any image."""

from cli import process_cli_args
import image_functions as img_fns


# Process image.
path, options = process_cli_args()
img = img_fns.load_image(path)
new_img = img_fns.process_image(img, options)
img_fns.save_image(path, new_img)