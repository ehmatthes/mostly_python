from pathlib import Path

path = Path(__file__).parent / "deploy.py"

# Get all lines with a function definition.
lines = [
    line
    for line in path.read_text().splitlines()
    if ' def ' in line
]

breakpoint()