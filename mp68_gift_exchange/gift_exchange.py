import random, sys

names = [
    "Sherri",
    "Eric",
    "Terri",
    "Joel",
    "Joshua",
    "Catherine",
    "Jasmine",
    "Alexandra",
    "Jeremiah",
]

partners = [
    ("Sherri", "Eric"),
    ("Terri", "Joel"),
    ("Joshua", "Catherine"),
    ("Jasmine", "Alexandra"),
]

def check_match(match):
    if match in partners:
        return False
    if tuple(reversed(match)) in partners:
        return False
    return True

def attempt_match(names):
    random.shuffle(names)

    # Match each person with the next, then match the last
    #   person with the first.
    matches = [(names[i], names[i+1]) for i in range(len(names)-1)]
    matches.append((names[-1], names[0]))

    # Check all matches.
    if all([check_match(match) for match in matches]):
        return matches
    return False

def summarize_matches(matches):
    for giver, receiver in matches:
        print(f"{giver} will give to {receiver}.")


num_attempts = 0
while num_attempts < 10:
    num_attempts += 1

    matches = attempt_match(names[:])
    if matches:
        # Print summary, and exit.
        print(num_attempts)
        summarize_matches(matches)
        sys.exit()

# Failed to find a good match.
print("Couldn't make a good set of matches.")