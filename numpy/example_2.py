import numpy as np

# Create an array to describe a velocity vector of a robot that moves 3km/h to X axis and 4 km/h to Y axis
velocity = np.array([3.0, 4.0])

# Calculate the vector module defined as speed of the robot
speed = np.linalg.norm(velocity)

# Print the result
print(f"Speed = {speed}")
