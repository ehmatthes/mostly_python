# random_numbers.py

from random import randint

# Build a list of random numbers, to simulate rolling a die.
rolls = []
for _ in range(20_000_000):
    roll = randint(1,6)
    rolls.append(roll)

# Verify how many rolls were generated.
print(f"Generated {len(rolls):,} rolls.")

# Print the first ten rolls, and the last ten rolls.
print(f"First ten rolls: {rolls[:10]}")
print(f"Last ten rolls: {rolls[-10:]}")