from pathlib import Path
import re

path = Path(__file__).parent / "deploy.py"

# Get all lines with a function definition.
lines = [
    line
    for line in path.read_text().splitlines()
    if ' def ' in line
]

# Extract each function name.
fn_name_re = r".*def ([a-z_]*)\("
fn_names = [
    re.match(fn_name_re, line).group(1)
    for line in lines
]

breakpoint()