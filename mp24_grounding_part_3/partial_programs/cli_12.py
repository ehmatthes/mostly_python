"""Process the CLI for add_border.py."""

import sys, argparse
from pathlib import Path


def define_arguments(parser):
    """Define arguments for the CLI."""
    parser.add_argument('path',
        help="path to the image file")
    parser.add_argument('border_width',
        nargs='?', type=int, default=2,
        help="default: 2px")
    parser.add_argument('--padding', type=int, default=0,
        help="default: 0px")
    parser.add_argument('--border-color', type=str,
        default='lightgray', help="default: lightgray")

def validate_path(path):
    """Make sure the path exists."""
    if not path.exists():
        print(f"{path} does not seem to exist.")
        sys.exit()

def get_options(args):
    """Build the options dict from the arguments."""
    options = {
        'border_width': args.border_width,
        'padding': args.padding,
        'border_color': args.border_color,
    }
    return options

def process_cli_args():
    """Process all CLI arguments."""
    parser = argparse.ArgumentParser()

    define_arguments(parser)

    # Process arguments.
    args = parser.parse_args()
    path = Path(args.path)
    validate_path(path)
    options = get_options(args)

    return path, options