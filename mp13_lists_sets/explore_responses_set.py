from pathlib import Path
import json

path = Path('responses.json')
contents = path.read_text()
responses = json.loads(contents)

num_responses = len(responses)
print(f"Found {num_responses:,} responses.")

# Find the unique responses.
unique_responses = set(responses)

num_unique = len(unique_responses)
print(f"Found {num_unique} unique responses.")
print(unique_responses)