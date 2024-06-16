# functions.py
# Functions for TrussSim

import numpy as np
import math
import matplotlib.pyplot as plt
import classes # type: ignore
import json


def plot_truss_structure(connections, supports, nodes, loads, reaction_forces):
    """
    Plot the truss structure.

    Parameters:
        connections (list): List of Connection objects representing connections between nodes.
        supports (list): List of Support objects representing support nodes.
        nodes (list): List of Node objects representing nodes in the truss structure.
        loads (list): List of Load objects representing loads applied to nodes.
        reaction_forces (list): List of Reaction objects representing reaction forces.
    """
    # Plot nodes
    for node in nodes:
        plt.plot(node.x, node.y, 'ko')  # Black dot at node coordinates
        plt.text(node.x + 0.1, node.y + 0.1, node.name, fontsize=12)  # Name of node

    # Plot truss with colored forces
    for connection in connections:
        node1 = connection.node1
        node2 = connection.node2
        if hasattr(connection, 'force'):  # Check if connection has a force attribute
            force = connection.force
            if isinstance(force, classes.Force):
                if force.magnitude > 0:
                    color = 'b'  # Blue for positive forces
                else:
                    color = 'r'  # Red for negative forces
                plt.plot([node1.x, node2.x], [node1.y, node2.y], color=color)  # Color coded connection line
                plt.text((node1.x + node2.x) / 2, (node1.y + node2.y) / 2, f"{force.magnitude:.2f}", fontsize=10, color=color)  # Display force magnitude
        else:
            plt.plot([node1.x, node2.x], [node1.y, node2.y], 'k-')  # Default black connection line

    # Plot supports
    for support in supports:
        node = support.node  # Access the node attribute
        if support.support_type == 'roller':
            plt.plot(node.x, node.y, marker='o', markersize=10, markerfacecolor='none', markeredgewidth=2, markeredgecolor='r', label='Roller Support')
        elif support.support_type == 'pin':
            plt.plot(node.x, node.y, marker='o', markersize=10, markerfacecolor='none', markeredgewidth=2, markeredgecolor='b', label='Pin Support')

    # Plot loads with fixed arrow length
    arrow_length = 1.0  # Set the fixed arrow length
    for load in loads:
        node = load.node  # Access the node attribute
        angle_radians = math.radians(load.angle_degrees)  # Convert angle to radians
        dx = arrow_length * math.cos(angle_radians)  # Calculate change in x
        dy = arrow_length * math.sin(angle_radians)  # Calculate change in y
        plt.arrow(node.x, node.y, dx, dy, linewidth=4, head_width=0.1, head_length=0.1, fc='r', ec='r', label='Load')
        plt.text(node.x + dx / 2, node.y + dy / 2, f"{load.magnitude:.2f}", fontsize=10, color='r')  # Display load magnitude

    # Plot reaction forces with fixed arrow length
    for force in reaction_forces:
        node = force.node  # Access the node attribute
        angle_radians = force.angle_radians  # Angle in radians
        dx = arrow_length * math.cos(angle_radians)  # Calculate change in x
        dy = arrow_length * math.sin(angle_radians)  # Calculate change in y
        plt.arrow(node.x, node.y, dx, dy, linewidth=4, head_width=0.1, head_length=0.1, fc='g', ec='g', label='Reaction Force')
        plt.text(node.x + dx / 2, node.y + dy / 2, f"{force.magnitude:.2f}", fontsize=10, color='g')  # Display reaction force magnitude

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
    loads = []
    for load_data in loads_data:
        node_index, magnitude, angle_degrees = load_data
        node = nodes[node_index]
        load = classes.Load(node, magnitude, angle_degrees)
        loads.append(load)

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
        length_rounded = round(connection.length, 2)
        angle_degrees_rounded = round(connection.angle_degrees, 2)
        if hasattr(connection, 'force'):  # Check if connection has a force attribute
            force = connection.force
            if isinstance(force, classes.Force):
                force_magnitude_rounded = round(force.magnitude, 2)
                print(f"Connection {connection.node1.name}{connection.node2.name} between {connection.node1.name} and {connection.node2.name} with length {length_rounded} and angle {angle_degrees_rounded} degrees Force: {force_magnitude_rounded}")
        else:
            print(f"Connection {connection.node1.name}{connection.node2.name} between {connection.node1.name} and {connection.node2.name} with length {length_rounded} and angle {angle_degrees_rounded} degrees")
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
        force_magnitude_rounded = round(force.magnitude, 2)
        if isinstance(force, classes.ReactionX):
            print(f"Reaction force in the x-direction at node {force.node.name}, magnitude: {force_magnitude_rounded}")
        elif isinstance(force, classes.ReactionY):
            print(f"Reaction force in the y-direction at node {force.node.name}, magnitude: {force_magnitude_rounded}")
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
            # For pin support, create ReactionX and ReactionY objects
            reaction_force_x = classes.ReactionX(support.node, 0)  # Initial magnitude set to 0
            reaction_force_y = classes.ReactionY(support.node, 0)  # Initial magnitude set to 0
            reaction_forces.extend([reaction_force_x, reaction_force_y])
        elif support.support_type == 'roller':
            # For roller support, create only a ReactionY object
            reaction_force_y = classes.ReactionY(support.node, 0)  # Initial magnitude set to 0
            reaction_forces.append(reaction_force_y)

    return reaction_forces

def calculate_forces(nodes, connections, supports, loads):
    """
    Calculate forces in the truss structure.

    Parameters:
        nodes (list): List of Node objects representing nodes in the truss structure.
        connections (list): List of Connection objects representing connections between nodes.
        supports (list): List of Support objects representing support nodes.
        loads (list): List of Load objects representing loads applied to nodes.

    Returns:
        tuple: A tuple containing updated lists of connections and reaction forces.
               Returns None if the truss is not statically determined.
    """
    # Calculate reaction forces
    reaction_forces = calculate_reaction_forces(supports)

    # Statically determined check
    if 2 * len(nodes) != len(reaction_forces) + len(connections):
        print("Truss is not statically determined!")
        return None, None  # Return None if truss is not statically determined

    # Initialize the coefficient matrix with zeros
    coefficient_matrix_rows = 2 * len(nodes)
    coefficient_matrix_columns = len(connections) + len(reaction_forces)
    coefficient_matrix = np.zeros((coefficient_matrix_rows, coefficient_matrix_columns))

    # Initialize the constant matrix
    constant_matrix = np.zeros(coefficient_matrix_rows)

    # Populate the coefficient matrix based on connections and supports
    for connection_index, connection in enumerate(connections):
        node1_index = nodes.index(connection.node1)
        node2_index = nodes.index(connection.node2)
        L = connection.length
        cos_theta = (connection.node2.x - connection.node1.x) / L
        sin_theta = (connection.node2.y - connection.node1.y) / L

        # Equilibrium at node1
        coefficient_matrix[2 * node1_index][connection_index] = cos_theta
        coefficient_matrix[2 * node1_index + 1][connection_index] = sin_theta

        # Equilibrium at node2
        coefficient_matrix[2 * node2_index][connection_index] = -cos_theta
        coefficient_matrix[2 * node2_index + 1][connection_index] = -sin_theta

    # Add reaction forces to the coefficient matrix
    reaction_force_index = len(connections)
    for reaction_force in reaction_forces:
        node_index = nodes.index(reaction_force.node)
        if isinstance(reaction_force, classes.ReactionX):
            coefficient_matrix[2 * node_index][reaction_force_index] = 1
        elif isinstance(reaction_force, classes.ReactionY):
            coefficient_matrix[2 * node_index + 1][reaction_force_index] = 1
        reaction_force_index += 1

    # Add loads to the constant matrix
    for load in loads:
        node_index = nodes.index(load.node)
        constant_matrix[2 * node_index] -= load.magnitude * np.cos(load.angle_radians)
        constant_matrix[2 * node_index + 1] -= load.magnitude * np.sin(load.angle_radians)

    # Solve for the variables
    variables = np.linalg.solve(coefficient_matrix, constant_matrix)

    # Assign calculated forces to the connections as Force objects
    for connection_index, connection in enumerate(connections):
        force_magnitude = variables[connection_index]
        angle_degrees = connection.angle_degrees
        force = classes.Force(connection.node1, force_magnitude, angle_degrees)
        connection.force = force

    # Update reaction forces with calculated values
    for reaction_force in reaction_forces:
        node_index = nodes.index(reaction_force.node)
        reaction_force.magnitude = variables[len(connections) + reaction_forces.index(reaction_force)]

    return connections, reaction_forces