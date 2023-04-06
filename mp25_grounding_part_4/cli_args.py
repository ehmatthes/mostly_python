import sys
import argparse
from pathlib import Path
from dataclasses import dataclass

@dataclass
class ImageBorderArgs:
    path: Path
    border_width: int
    padding: int
    border_color: str

def parse_cli_args():
    parser = argparse.ArgumentParser(
            description="Add a border to any image.")
    parser.add_argument("filename", type=Path,
            help="The target image.")
    parser.add_argument("border_width", type=int,
            nargs="?",default=2,
            help="The border width (default: 2).")
    parser.add_argument("--padding", type=int, default=0,
            help="The padding (default: 0).")
    parser.add_argument("--border-color",
            dest="border_color", default="lightgray",
            help="The border color (default: lightgray).")

    args = parser.parse_args()

    return ImageBorderArgs(args.filename, args.border_width,
            args.padding, args.border_color)