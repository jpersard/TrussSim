# functions.py
# Functions for TrussSim

import numpy as np
import matplotlib.pyplot as plt
import classes # type: ignore
import json


def plot_truss_structure(connections, supports, nodes, loads):
    """
    Plot the truss structure.

    Parameters:
        connections (list): List of Connection objects representing connections between nodes.
        supports (list): List of Support objects representing support nodes.
        nodes (list): List of Node objects representing nodes in the truss structure.
        loads (list): List of Load objects representing loads applied to nodes.
        reaction_forces (tuple): Tuple containing reaction forces.
    """
    # Plot truss
    for connection in connections:
        node1 = connection.node1
        node2 = connection.node2
        plt.plot([node1.x, node2.x], [node1.y, node2.y], 'k-')

    # Plot supports
    for support in supports:
            node = support.node  # Access the node attribute
            if support.support_type == 'roller':
                plt.plot(node.x, node.y, marker='o', markersize=10, markerfacecolor='none', markeredgewidth=2, markeredgecolor='r')
            elif support.support_type == 'pin':
                plt.plot(node.x, node.y, marker='o', markersize=10, markerfacecolor='none', markeredgewidth=2, markeredgecolor='b')

    # Plot loads
    for load in loads:
        node = load.node  # Access the node attribute
        plt.arrow(node.x, node.y, load.force_x/10, load.force_y/10, head_width=0.1, head_length=0.1, fc='g', ec='g')

    plt.xlabel('X-Axis')
    plt.ylabel('Y-Axis')
    plt.title('Truss Structure')
    plt.grid(True)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.show()

def import_json(file_path):
    """
    Import truss data from JSON.

    Args:
        file_path (str): Path to the JSON file containing truss data.

    Returns:
        tuple: A tuple containing lists of nodes, connections, supports, and loads.
    """
    with open(file_path) as file:
        truss_data = json.load(file)

    # Extract truss data from JSON
    nodes_data = truss_data.get('nodes', [])
    connections_data = truss_data.get('connections', [])
    supports_data = truss_data.get('supports', {})
    loads_data = truss_data.get('loads', [])

    # Create Node instances with names A, B, C...
    nodes = [classes.Node(chr(65 + i), x, y) for i, (x, y) in enumerate(nodes_data)]

    # Create Connection instances
    connections = [classes.Connection(nodes[i], nodes[j]) for i, j in connections_data]

    # Create Support instances
    supports = [classes.Support(nodes[int(node_index)], support_type) for node_index, support_type in supports_data.items()]

    # Create Load instances
    loads = [classes.Load(nodes[node_index], force_x, force_y) for node_index, force_x, force_y in loads_data]

    return nodes, connections, supports, loads

def print_all(nodes, connections, supports, loads, reaction_forces):
    """
    Print all truss data.

    Parameters:
        nodes (list): List of Node objects representing nodes in the truss structure.
        connections (list): List of Connection objects representing connections between nodes.
        supports (list): List of Support objects representing support nodes.
        loads (list): List of Load objects representing loads applied to nodes.
        reaction_forces (list): List of Reaction objects representing reaction forces.
    """
    print("Nodes:")
    for node in nodes:
        print(node)
    print("\n")

    print("Connections:")
    for connection in connections:
        print(connection)
    print("\n")

    print("Supports:")
    for support in supports:
        print(support)
    print("\n")

    print("Loads:")
    for load in loads:
        print(load)
    print("\n")

    print("Reaction forces:")
    for force in reaction_forces:
        print(force)
    print("\n")

def calculate_reaction_forces(supports):
    """
    Calculate reaction forces for the supports.

    Parameters:
        supports (list): List of Support objects representing support nodes.

    Returns:
        list: List of Reaction objects representing reaction forces.
    """
    reaction_forces = []

    for support in supports:
        if support.support_type == 'pin':
            # For pin support, create a Reaction object with x and y components
            reaction_force = classes.Reaction(support.node, 1, 1)
        elif support.support_type == 'roller':
            # For roller support, create a Reaction object with only y component
            reaction_force = classes.Reaction(support.node, 0, 1)
        reaction_forces.append(reaction_force)

    return reaction_forces