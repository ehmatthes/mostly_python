from pathlib import Path

project_root = Path(__file__).parent
path = project_root / "coffees" / "coffees.txt"
contents = path.read_text()

print(contents)