import matplotlib.pyplot as plt
import classes
import functions


# define truss nodes
nodes_data = [(0, 0), (3, 2), (3, 0), (6, 0)]
nodes = [classes.Node(x, y) for x, y in nodes_data]

# define connections
connections_data = [(0, 1),(0, 2), (1, 2), (1, 3),(2, 3)]
connections = [classes.Connection(nodes[i], nodes[j]) for i, j in connections_data]

# Define supports
supports_data = {0: 'pin', 3: 'roller'}
supports = [classes.Support(node_index, support_type) for node_index, support_type in supports_data.items()]

# Define loads
loads_data = [(2, 0, -100)]
loads = [classes.Load(node_index, force_x, force_y) for node_index, force_x, force_y in loads_data]

functions.plot_truss_structure(connections, supports, nodes, loads)