import matplotlib.pyplot as plt

# Generate data.
triangle_nums = [1, 3, 6, 10, 15, 21]
x_values = [1, 2, 3, 4, 5, 6]

# Generate plot.
fig, ax = plt.subplots()
ax.scatter(x_values, triangle_nums)

# Format plot.
ax.set_title("Triangle Numbers")
ax.set_xlabel("N")
ax.set_ylabel("Nth Triangle Number")

# Show plot.
plt.show()