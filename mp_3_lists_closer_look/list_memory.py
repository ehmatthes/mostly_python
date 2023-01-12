# list_memory.py

import sys
from random import randint

# Build a list of random numbers, to simulate rolling a die.
rolls = []
for x in range(10):
    roll = randint(1,6)
    rolls.append(roll)

    # Examine the length and size of the list.
    list_length = len(rolls)
    list_size = sys.getsizeof(rolls)
    print(f"Items: {list_length}\tBytes: {list_size}")