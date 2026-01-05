import argparse

parser = argparse.ArgumentParser()

parser.add_argument(
    "-v",
    "--verbose",
    action="store_true",
    help="Verbose output, including showing computer cards.",
)
parser.add_argument(
    "--seed",
    action="store_true",
    help="Seed the random number generator.",
)
parser.add_argument(
    "--auto-play",
    action="store_true",
    help="Automatically play through games.",
)
parser.add_argument(
    "--num-games",
    type=int,
    default=1,
    help="When using --auto-play, how many games to play.",
)

cli_args = parser.parse_args()
