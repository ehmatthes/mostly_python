from pathlib import Path

path = Path("/Users/eric/projects/coffee_project/coffees.txt")
contents = path.read_text()

print(contents)