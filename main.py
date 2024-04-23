# main.py
import matplotlib.pyplot as plt
import functions
import json
import numpy as np

# Import truss data from JSON
truss_data = r'C:\dev\TrussSim\truss_data.json'

with open(truss_data) as file:
    json_data = json.load(file)

nodes, connections, supports, loads = functions.import_json(json_data)

for node in nodes:
    print(node)

for connection in connections:
    print(connection)

for support in supports:
    print(support)

for load in loads:
    print(load)


def build_equation_system(supports, loads, nodes):
    num_unknowns = len(supports) + len([support for support in supports if support.support_type == 'pin'])  # Number of unknowns
    num_loads = len(nodes)  # Number of nodes
    A = np.zeros((3, num_unknowns))  # Coefficient matrix
    b = np.zeros(3)  # Constant matrix

    # Sum of forces in x-direction equation
    row_index = 0
    for i, support in enumerate(supports):
        if support.support_type == 'pin':
            A[row_index, i] = 1  # Coefficient for Rx
        elif support.support_type == 'roller':
            A[row_index, i] = 0  # Coefficient for Rx (for roller support)
    for load in loads:
        A[row_index, len(supports) + load.node_index] = 1  # Coefficient for Rx
        b[row_index] -= load.force_x  # External load in x-direction
    row_index += 1

    # Sum of forces in y-direction equation
    for i, support in enumerate(supports):
        if support.support_type == 'pin':
            A[row_index, i] = 0  # Coefficient for Ry
        elif support.support_type == 'roller':
            A[row_index, i] = 1  # Coefficient for Ry
    for load in loads:
        A[row_index, len(supports) + load.node_index] = 1  # Coefficient for Ry
        b[row_index] -= load.force_y  # External load in y-direction
    row_index += 1

    # Sum of moments around origin equation
    for i, support in enumerate(supports):
        A[row_index, i] = nodes[support.node_index].y  # Coefficient for Rx
        A[row_index, len(supports) + i] = -nodes[support.node_index].x  # Coefficient for Ry
        b[row_index] -= nodes[support.node_index].x * 0  # Moment due to Ry (since it's 0 for roller)
    for load in loads:
        A[row_index, len(supports) + load.node_index] = nodes[load.node_index].y  # Coefficient for Rx
        A[row_index, 2 * num_loads + load.node_index] = -nodes[load.node_index].x  # Coefficient for Ry
        b[row_index] -= nodes[load.node_index].x * load.force_y  # Moment due to external load
    return A, b

# Build the equation system
A, b = build_equation_system(supports, loads, nodes)

# Solve the equation system
solution = np.linalg.solve(A, b)

print("Solution (Reaction Forces):")
for i, support in enumerate(supports):
    print(f"Support {support.node_index}: Ry = {solution[i]}")

# Plot the truss structure with loads and forces
functions.plot_truss_structure(connections, supports, nodes, loads, reaction_forces)
