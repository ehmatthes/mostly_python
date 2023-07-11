import matplotlib.pyplot as plt

x_vals = list(range(100))
squares = [x**2 for x in x_vals]

plt.style.use('classic')
fig, ax = plt.subplots()
ax.scatter(x_vals, squares)

plt.show()