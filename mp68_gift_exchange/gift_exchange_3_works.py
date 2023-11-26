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
    matches = []

    # Keep track of first giver.
    giver = names.pop()
    first_giver = giver

    while names:
        # Receiver is next name in list.
        receiver = names.pop()
        match = (giver, receiver)

        # Bail if it's a bad match.
        if not check_match(match):
            return False

        # Store match.
        matches.append(match)

        # Current receiver becomes next giver.
        giver = receiver

    # The last giver receives a gift from
    #   the first giver.
    match = (receiver, first_giver)
    if not check_match(match):
        return False

    # If we're still here, all matches are good.
    return matches

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