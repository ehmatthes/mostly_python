"""Process the CLI for add_border.py."""

import sys, argparse
from pathlib import Path

def process_cli_args(options):
    """Process all CLI arguments."""
    parser = argparse.ArgumentParser()

    # Define arguments.
    parser.add_argument('path',
        help="path to the image file")
    parser.add_argument('border_width',
        nargs='?', type=int,
        help="default: 2px")
    parser.add_argument('--padding', type=int,
        help="padding between image and border")
    parser.add_argument('--border-color', type=str,
        help="default: lightgray")

    # Process arguments.
    args = parser.parse_args()

    path = Path(args.path)
    if not path.exists():
        print(f"{path} does not seem to exist.")
        sys.exit()

    if args.border_width:
        options['border_width'] = args.border_width
    if args.padding:
        options['padding'] = args.padding
    if args.border_color:
        options['border_color'] = args.border_color

    return path