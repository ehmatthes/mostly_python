# random_numbers_deque.py

from random import randint
from collections import deque

# Build a list of random numbers, to simulate rolling a die.
#   The most recent roll is always first in the list.
rolls = deque()
for _ in range(20_000_000):
    roll = randint(1,6)
    rolls.appendleft(roll)

# Verify how many rolls were generated.
print(f"Generated {len(rolls):,} rolls.")