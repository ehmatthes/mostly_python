# random_numbers_insert.py

from random import randint

# Build a list of random numbers, to simulate rolling a die.
#   The most recent roll is always first in the list.
rolls = []
for _ in range(220_000):
    roll = randint(1,6)
    rolls.insert(0, roll)

# Verify how many rolls we generated.
print(f"Generated {len(rolls):,} rolls.")