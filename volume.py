import numpy as np
# Define the number of points in each dimension for the grid
n_points = 1000
# Create equally spaced points between 0 and 1 for x and y
x = np.linspace(0, 1, n_points)
y = np.linspace(0, 1, n_points)
# Create a meshgrid for x and y
X, Y = np.meshgrid(x, y)
# Calculate the function values at each (x, y)
Z = X**2 * Y**2
# Calculate the spacing between points
dx = x[1] - x[0]
dy = y[1] - y[0]
# Approximate the double integral using the sum of function values times the area of each small rectangle
volume = np.sum(Z) * dx * dy
print(f"Approximate volume under the surface z = x^2 * y^2 over [0,1]x[0,1]: {volume}")