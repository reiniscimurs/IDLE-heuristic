from math import *
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm


# Heuristics calculation function for a single point
def calculate_heuristic_score(x, y, dist_o, dist_g, dist_l1, dist_l2, map, kernel_size):
    d1 = np.tanh(np.exp((dist_o / dist_l1) ** 2) / exp((dist_l2 / dist_l1) ** 2)) * dist_l2
    d2 = dist_g

    point_information = 0
    count = 1
    for i in range(-int(kernel_size / 2), int(kernel_size / 2)):
        for j in range(-int(kernel_size / 2), int(kernel_size / 2)):
            if 0 <= x + i < len(map) and 0 <= y + j < len(map[0]):
                point_information += map[x + i][y + j]
                count += 1
    I = min(50, exp(point_information / count))

    return d1 + d2 + I


"""Parameters"""
dist_l1 = 5  # Inner distance limit for local heuristics discount
dist_l2 = 10  # Outer distance limit for local heuristics discount
goalX = 15  # Distance to the goal on X axis
goalY = 0 # Distance to the goal on Y axis
originX = 0 # Point of origin on X axis
originY = 0 # Point of origin on Y axis
kernel_size = 15 # Kernel size in pixels for map information heuristic calculation
m_u = 0 # value of the unknown pixels in the map
m_k = 1 # value of the known pixels in the map
m_o = 5 # value of the obstacle pixels in the map


# Create a figure
fig = plt.figure()
ax = fig.gca(projection='3d')

# Generate example map data
X = np.arange(-20, 20, 0.1)
Y = np.arange(-20, 20, 0.1)
map = np.ones((len(X), len(Y)))*m_u
for i in range(125, 400):
    for j in range(0, 250):
        map[i][j] = m_k
for i in range(220, 400):
    for j in range(150, 400):
        map[i][j] = m_k
for i in range(250, 400):
    for j in range(250, 350):
        map[i][j] = m_o
X, Y = np.meshgrid(X, Y)

# Create a holder for output data
output = np.zeros((map.shape))

# Calculate a heuristics score for every individual point in map range
for ox in range(0, len(map)):
    for oy in range(0, len(map[0])):
        dist_o = np.sqrt((X[ox][oy] - originX) ** 2 + (Y[ox][oy] - originY) ** 2)
        dist_g = np.sqrt((X[ox][oy] - goalX) ** 2 + (Y[ox][oy] - goalY) ** 2)
        output[ox][oy] = calculate_heuristic_score(ox, oy, dist_o, dist_g, dist_l1, dist_l2, map, kernel_size)
    print(f'{round((ox / len(map)) * 100, 2)} % Done')
print('100.0 % Done')

# Clip the output values for better visualization
output = np.clip(output, 0, 50)

# Plot the heuristics score and the map
surf = ax.plot_surface(X, Y, output, cmap=cm.turbo_r, linewidth=0, antialiased=False)
surf2 = ax.plot_surface(X, Y, map, cmap=cm.coolwarm, linewidth=0, antialiased=False)

# Customize the z axis
ax.set_zlim(0, 40.0)
ax.set_zlabel('Score', size=15)

# Add a color bar which maps values to colors of the heuristics score
fig.colorbar(surf, shrink=0.5, aspect=10, pad=0.1)
plt.xlabel('x-coordinate', size=15)
plt.ylabel('y-coordinate', size=15)
# plt.show()

# Save the graph as a .png image
plt.savefig("IDLE_score.png")
