# Imports
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches # Required for legend customization
import matplotlib.animation as animation
import numpy as np

# Init
fig, ax = plt.subplots() # Initialize figure and subplot axes
ax.set(xlim=(-3,3), ylim=(-1.1,1.1)) # Sets boundaries of axes

# Plotting axes
x = np.linspace(-np.pi, np.pi) # x-axis values for sine function
line, = ax.plot(
    x, # x-axis
    np.sin(x), # y-axis
    color='k',
    lw=4 # Line width
)

def animate(i):
    line.set_ydata(np.sin(x + i / 100)) # Update data to animate graph
    return line,

ani = animation.FuncAnimation(
    fig,
    animate,
    frames=1000, # Animation frame length if repeat=False
    interval=20, # Delay in milliseconds between frames
    blit=True, # Blitting moves data into memory to quickly animate 2D images
    repeat=True,
    save_count=100 # Used if number of frames is not determinable
)

# Labels
plt.title("Sine Function")
plt.xlabel('Angle (radians)')
plt.ylabel('sine(x)', rotation=0) # Rotate ylabel to appear horizontally

# Legend
plt.legend(handles=[mpatches.Patch(color="black", label="Sine")])

# Save plot
ani.save("animated_sine_plot.gif")

# Show plot
plt.show()
