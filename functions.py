# Functions for TrussSim


import matplotlib.pyplot as plt
import classes # type: ignore


def plot_truss_structure(connections, supports, nodes, loads):
    """
    Plot the truss structure.

    Parameters:
        connections (list): List of Connection objects representing connections between nodes.
        supports (list): List of Support objects representing support nodes.
        nodes (list): List of Node objects representing nodes in the truss structure.
        loads (list): List of Load objects representing loads applied to nodes.
    """
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

def import_json(truss_data):
    """
    Import truss data from JSON.

    Args:
        truss_data (dict): Dictionary containing truss data in JSON format.

    Returns:
        tuple: A tuple containing lists of nodes, connections, supports, and loads.
    """
    # Extract truss data from JSON
    nodes_data = truss_data.get('nodes', [])
    connections_data = truss_data.get('connections', [])
    supports_data = truss_data.get('supports', {})
    loads_data = truss_data.get('loads', [])

    # Create Node instances
    nodes = [classes.Node(x, y) for x, y in nodes_data]

    # Create Connection instances
    connections = [classes.Connection(nodes[i], nodes[j]) for i, j in connections_data]

    # Create Support instances
    supports = [classes.Support(int(node_index), support_type) for node_index, support_type in supports_data.items()]

    # Create Load instances
    loads = [classes.Load(node_index, force_x, force_y) for node_index, force_x, force_y in loads_data]

    return nodes, connections, supports, loads