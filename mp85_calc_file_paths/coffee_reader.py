from pathlib import Path

path = Path("coffees.txt")
contents = path.read_text()

print(contents)