"""Process the CLI for add_border.py."""

import sys
from pathlib import Path

def process_cli_args(options):
    """Process all CLI arguments."""
    # Get the filename.
    try:
        path = Path(sys.argv[1])
    except IndexError:
        print("You must provide a target image.")
        sys.exit()

    # Make sure the file exists.
    if not path.exists():
        print(f"{path} does not seem to exist.")
        sys.exit()

    # --- Get optional CLI args. ---
    if len(sys.argv) >= 3:
        options['border_width'] = int(sys.argv[2])
    if len(sys.argv) >= 4:
        options['padding'] = int(sys.argv[3])
    if len(sys.argv) >= 5:
        options['border_color'] = sys.argv[4]

    return path