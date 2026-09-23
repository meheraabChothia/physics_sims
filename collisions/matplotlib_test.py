import matplotlib.pyplot as plt
import numpy as np

# Create a figure containing a single Axes.
# fig, ax = plt.subplots()
fig = plt.figure()
ax = fig.subplots()
# ax.plot(1, 1)
ax.plot([1, 2, 3, 4], [0, 0.5, 1, 0.2])

plt.show()                           # Show the figure.
