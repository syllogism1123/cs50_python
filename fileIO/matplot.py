
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Create plot
fig, ax = plt.subplots()
x = np.linspace(0, 2 * np.pi, 100)
line, = ax.plot(x, np.sin(x))

# Update function for the animation
def update(frame):
    line.set_ydata(np.sin(x + frame / 10))  # Update Y-axis data
    return line,

# Animation function
ani = animation.FuncAnimation(fig, update, frames=100, interval=50, blit=True)

plt.show()
