import numpy as np
import matplotlib.pyplot as plt


# define truss nodes
nodes = np.array([[0, 0], [1, 1], [2, 0], [3, 1], [4, 0]])

# define connections
connections = [(0, 1),(0, 2), (1, 2), (2, 3),(2, 4), (3, 4)]

# Define supports
supports = {0: 'pin', 4: 'roller'}

# Define loads (in the format: (node, force_x, force_y))
loads = [(1, 0, -20), (3, 0, -10)]

# Plot truss
for connection in connections:
    node1 = nodes[connection[0]]
    node2 = nodes[connection[1]]
    plt.plot([node1[0], node2[0]], [node1[1], node2[1]], 'k-')

# Plot supports
for node_index, support_type in supports.items():
    node = nodes[node_index]
    if support_type == 'roller':
        plt.plot(node[0], node[1], 'ro')
    elif support_type == 'pin':
        plt.plot(node[0], node[1], 'bo')

# Plot loads
for load in loads:
    node = nodes[load[0]]
    plt.arrow(node[0], node[1], load[1]/10, load[2]/10, head_width=0.1, head_length=0.1, fc='g', ec='g')

plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')
plt.title('Truss Structure')
plt.grid(True)
plt.gca().set_aspect('equal', adjustable='box')
plt.show()