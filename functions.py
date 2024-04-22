# Functions for TrussSim


import matplotlib.pyplot as plt


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
