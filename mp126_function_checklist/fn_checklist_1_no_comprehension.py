from pathlib import Path

path = Path(__file__).parent / "deploy.py"

# Get all lines with a function definition.
lines = []
for line in path.read_text().splitlines():
    if ' def ' in line:
        lines.append(line)

breakpoint()