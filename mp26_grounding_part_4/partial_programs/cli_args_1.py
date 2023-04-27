import sys

def parse_cli_args(argv):
    try:
        path = Path(argv[1])
    except IndexError:
        print("You must provide a target image.")
        sys.exit()

    border_width = int(argv[2]) if len(argv) > 2 else 2
    padding = int(argv[3]) if len(argv) > 3 else 0
    border_color = argv[4] if len(argv) > 4 else "lightgray"

    return path, border_width, padding, border_color