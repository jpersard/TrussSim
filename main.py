import matplotlib.pyplot as plt

class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Connection:
    def __init__(self, node1, node2):
        self.node1 = node1
        self.node2 = node2

class Support:
    def __init__(self, node_index, support_type):
        self.node_index = node_index
        self.support_type = support_type

class Load:
    def __init__(self, node_index, force_x, force_y):
        self.node_index = node_index
        self.force_x = force_x
        self.force_y = force_y

# define truss nodes
nodes_data = [(0, 0), (1, 1), (2, 0), (3, 1), (4, 0)]
nodes = [Node(x, y) for x, y in nodes_data]

# define connections
connections_data = [(0, 1),(0, 2), (1, 2), (2, 3),(2, 4), (3, 4)]
connections = [Connection(nodes[i], nodes[j]) for i, j in connections_data]

# Define supports
supports_data = {0: 'pin', 4: 'roller'}
supports = [Support(node_index, support_type) for node_index, support_type in supports_data.items()]

# Define loads
loads_data = [(1, 0, -20), (3, 0, -10), (1, -10, 0)]
loads = [Load(node_index, force_x, force_y) for node_index, force_x, force_y in loads_data]


# Plot truss
for connection in connections:
    node1 = connection.node1
    node2 = connection.node2
    plt.plot([node1.x, node2.x], [node1.y, node2.y], 'k-')

# Plot supports
for support in supports:
    node = nodes[support.node_index]
    if support.support_type == 'roller':
        plt.plot(node.x, node.y, 'ro')
    elif support.support_type == 'pin':
        plt.plot(node.x, node.y, 'bo')

# Plot loads
for load in loads:
    node = nodes[load.node_index]
    plt.arrow(node.x, node.y, load.force_x/10, load.force_y/10, head_width=0.1, head_length=0.1, fc='g', ec='g')

plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')
plt.title('Truss Structure')
plt.grid(True)
plt.gca().set_aspect('equal', adjustable='box')
plt.show()
