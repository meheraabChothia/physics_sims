import matplotlib
import matplotlib.pyplot as plt
import numpy as np

matplotlib.use('Agg')  # Use 'TkAgg' if you installed Tkinter instead

x = np.linspace(0, 2 * np.pi, 200)
y = np.sin(x)


fig, ax = plt.subplots()
ax.plot(x, y)
plt.savefig('test.png')
