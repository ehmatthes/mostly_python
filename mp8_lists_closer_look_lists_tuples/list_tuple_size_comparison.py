import sys

from matplotlib import pyplot as plt


# What's the longest sequence we want to examine?
max_length = 100

list_sizes = []
tuple_sizes = []
for seq_length in range(max_length):
    # For every sequence length, make a list of squares and a tuple of squares.
    # Record the size of each list.
    squares_list = [x**2 for x in range(seq_length)]
    list_sizes.append(sys.getsizeof(squares_list))

    # Record the size of each tuple.
    squares_tuple = tuple(x**2 for x in range(seq_length))
    tuple_sizes.append(sys.getsizeof(squares_tuple))

# Plot the size of each sequence against the number of items.
#   Note: For Maptlotlib 3.5, use "seaborn".
plt.style.use("seaborn-v0_8")

# X values are the number of items in each sequence.
x_values = list(range(1, max_length+1))

fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(x_values, list_sizes)
ax.plot(x_values, tuple_sizes)

ax.set_title("Size of lists and tuples vs number of items", fontsize=24)
ax.set_xlabel("Number of items", fontsize=14)
ax.set_ylabel("Size (bytes)", fontsize=14)

plt.show()
