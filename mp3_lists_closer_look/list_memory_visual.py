# list_memory_visual.py

import sys
from random import randint

import matplotlib.pyplot as plt

# Build a list of random numbers, to simulate rolling a die.
rolls = []
sizes = []
for x in range(100):
    roll = randint(1,6)
    rolls.append(roll)

    # Record the size of the list on each pass through the loop.
    list_size = sys.getsizeof(rolls)
    sizes.append(list_size)

# Plot the size of the list vs the number of items.
plt.style.use("seaborn")
fig, ax = plt.subplots()

x_values = list(range(1, 101))
ax.plot(x_values, sizes)

ax.set_title("Size of list vs number of items in list", fontsize=24)
ax.set_xlabel("Number of items", fontsize=14)
ax.set_ylabel("Size of list (bytes)", fontsize=14)

plt.show()