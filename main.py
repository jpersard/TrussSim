# main.py
import functions
import classes
import numpy as np

# Import truss data from JSON
if 1:
    json_path = r'C:\dev\TrussSim\truss_data.json'
    nodes, connections, supports, loads = functions.import_json(json_path)

# Print all objects
if 1:
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

# Calculate reaction forces
if 0:
    reaction_forces = []
    # Iterate through supports to populate reaction forces
    for support in supports:
        # For pin support, create a Reaction object with x and y components
        if support.support_type == 'pin':
            reaction_force = classes.Reaction(support.node, 1, 1)
        # For roller support, create a Reaction object with only y component
        elif support.support_type == 'roller':
            reaction_force = classes.Reaction(support.node, 0, 1)
        reaction_forces.append(reaction_force)

    #coefficients_matrix = np.array([[1, 0, 0], 
    #                                [0, 1, 1], 
    #                               [0, 0, 6]])
    #constants_vector = np.array([0, 
    #                             100, 
    #                             100*3])
    #reaction_forces = np.linalg.solve(coefficients_matrix, constants_vector)

    print("Reaction forces:")
    for force in reaction_forces:
        print(force)
    print("\n")

# Plot the truss structure with loads and forces
if 1:
    functions.plot_truss_structure(connections, supports, nodes, loads)
