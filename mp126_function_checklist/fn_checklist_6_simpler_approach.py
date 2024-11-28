from pathlib import Path
import re
import sys

# Read program file.
path = Path(sys.argv[1])
contents = path.read_text()

# Find all function names.
fn_name_re = r".*def ([a-z_]*)\("
fn_names = re.findall(fn_name_re, contents)

# Generate an issues task list.
for name in fn_names:
    task = f"- [ ] `{name}()`"
    print(task)
