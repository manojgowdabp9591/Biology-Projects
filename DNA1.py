import matplotlib.pyplot as plt
import numpy as np

# Define the DNA helix parameters
radius = 1.0 # nm
pitch = 3.4 # nm
n_steps = 50
step_size = 0.34 # nm

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Generate the DNA helix
for i in range(n_steps):
    # Calculate the coordinates of the current base pair
    theta = 2 * np.pi * i / n_steps
    x = radius * np.cos(theta)
    y = radius * np.sin(theta)
    z = i * step_size

    # Plot the current base pair as a sphere
    ax.scatter(x, y, z, s=10)

    # Plot the DNA backbone as a line
    if i > 0:
        prev_x = radius * np.cos(2 * np.pi * (i - 1) / n_steps)
        prev_y = radius * np.sin(2 * np.pi * (i - 1) / n_steps)
        ax.plot([prev_x, x], [prev_y, y], [prev_z, z + pitch/2], color='gray')
        ax.plot([prev_x, x], [prev_y, y], [prev_z, z - pitch/2], color='gray')

# Set the plot limits and labels
ax.set_xlim([-radius, radius])
ax.set_ylim([-radius, radius])
ax.set_zlim([0, n_steps * step_size + pitch])
ax.set_xlabel('X (nm)')
ax.set_ylabel('Y (nm)')
ax.set_zlabel('Z (nm)')

# Show the plot
plt.show()