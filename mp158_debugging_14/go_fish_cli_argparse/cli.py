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

cli_args = parser.parse_args()
