import numpy as np
import matplotlib.pyplot as plt


# define dimensions
dim = 2

# define truss nodes
nodes = np.array([[0, 0], [1, 1], [2, 0], [3, 1], [4, 0]])

# define connections
connections = [(0, 1),(0, 2), (1, 2), (2, 3),(2, 4), (3, 4)]

# Define supports
supports = {0: 'pin', 4: 'roller'}

# Define loads (in the format: (node, force_x, force_y))
loads = [(1, 0, -20), (3, 0, -10)]

# Calculate reactions
reaction_forces = np.zeros((len(nodes), dim))  # Initialize array to store reaction forces

# Loop through supports to calculate reactions
for node_index, support_type in supports.items():
    if support_type == 'pin':
        reaction_forces[node_index] = [0, 0]  # Pin support does not produce reaction forces
    elif support_type == 'roller':
        connected_connections = [connection for connection in connections if node_index in connection]
        for connection in connected_connections:
            other_node_index = connection[0] if connection[0] != node_index else connection[1]
            dx = nodes[other_node_index][0] - nodes[node_index][0]
            dy = nodes[other_node_index][1] - nodes[node_index][1]
            length = np.sqrt(dx**2 + dy**2)
            angle = np.arctan2(dy, dx)
            reaction_forces[node_index][0] += loads[0][2] * np.cos(angle)  # Reaction force in x-direction
            reaction_forces[node_index][1] += loads[0][2] * np.sin(angle)  # Reaction force in y-direction

# Print reaction forces
for node_index, reaction_force in enumerate(reaction_forces):
    print(f"Node {node_index}: Reaction Force = {reaction_force}")

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