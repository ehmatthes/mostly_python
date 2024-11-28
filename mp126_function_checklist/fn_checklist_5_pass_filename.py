from pathlib import Path
import re
import sys

path = Path(sys.argv[1])

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

# Generate an issues task list.
for name in fn_names:
    task = f"- [ ] `{name}()`"
    print(task)
