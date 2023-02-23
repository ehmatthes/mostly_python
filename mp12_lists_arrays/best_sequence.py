import random

def get_flips(num_flips=10):
    """Return a random sequence of coin flips."""
    outcomes = ('H', 'T')
    return random.choices(outcomes, k=num_flips)

# Generate flips.
all_flips = get_flips()
print(f"Generated {len(all_flips):,} flips.")
print(all_flips)