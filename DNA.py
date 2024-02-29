# Import required libraries
from pymol import cmd
import numpy as np

# Define the number of base pairs in the DNA helix
n_bp = 10

# Define the rise and twist of the DNA helix (in Angstroms and degrees, respectively)
rise = 3.4
twist = 36

# Define the coordinates of the first base pair in the DNA helix
x1, y1, z1 = 0, 0, 0
x2, y2, z2 = rise * np.cos(np.radians(twist)), rise * np.sin(np.radians(twist)), 0

# Create a new PyMOL object and add the first base pair
cmd.create('dna', selection='')
cmd.alter('dna', 'x,y,z', f'{x1},{y1},{z1}')

# Add the remaining base pairs to the DNA helix
for i in range(1, n_bp):
    # Calculate the coordinates of the current base pair
    x1, y1, z1 = x2, y2, z2
    x2, y2, z2 = x1 + rise * np.cos(np.radians(twist + i * 360 / n_bp)), y1 + rise * np.sin(np.radians(twist + i * 360 / n_bp)), z1 + 10

    # Add the current base pair to the DNA helix
    cmd.append('dna', selection='', x=x2, y=y2, z=z2)

# Set the color of the DNA helix to white
cmd.color('white', 'dna')

# Set the background color to black
cmd.bg_color('black')

# Display the DNA helix
cmd.show('cartoon', 'dna')
cmd.zoom('dna')
cmd.run('ray 1000')

