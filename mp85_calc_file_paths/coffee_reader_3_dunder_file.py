from pathlib import Path

path = Path(__file__).parent / "coffees.txt"
contents = path.read_text()

print(contents)