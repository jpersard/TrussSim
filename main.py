# main.py
import functions
import numpy as np


# Variables to enable modules
# Later to be set in GUI
do_import = True
do_reaction = True
do_print_all = False
do_plot_truss = False

# Import truss data from JSON
if do_import:
    json_path = r'C:\dev\TrussSim\truss_data.json'
    nodes, connections, supports, loads = functions.import_json(json_path)

# Calculate forces
if do_reaction:
    # Initialize reaction forces
    reaction_forces = []
    for support in supports:
        reaction_forces.extend(support.initialize_reaction_forces())

    # Statically determined
    if 2 * len(nodes) != len(reaction_forces) + len(connections):
        print("Truss is not statically determined!")
        input("Press Enter to continue...")
        exit()

    # Initialize the coefficient matrix with zeros
    coefficient_matrix = np.zeros((2 * len(nodes), 2 * len(nodes)))
    # Populate the coefficient matrix based on connections

    # Print the coefficient matrix
    print(coefficient_matrix)

    if False:
        coefficient_matrix = np.array([[1,  0,  0,  0.83,   1,   0,     0,  0], 
                                    [0,  1,  0,  0.55,   1,   0,     0,  0], 
                                    [0,  0,  0,  0.83,   0,  -1, -0.55,  0], 
                                    [0,  0,  0,  0.55,   0,  -1, -0.55,  0], 
                                    [0,  0,  0,     0,   1,   0,     0,  1], 
                                    [0,  0,  0,     0,   0,  -1,     0,  0],
                                    [0,  0,  0,     0,   0,   0,  0.83,  1], 
                                    [0,  0,  1,     0,   0,   0, -0.55,  0]])

        # Constant matrix
        constant_matrix = np.array([0, 0, 0, 0, 0, -100, 0, 0])

        # Solve for the variables
        variables = np.linalg.solve(coefficient_matrix, constant_matrix)
        print(variables)

# Print all objects
if do_print_all:
    functions.print_all(nodes, connections, supports, loads, reaction_forces)

# Plot the truss structure with loads and forces
if do_plot_truss:
    functions.plot_truss_structure(connections, supports, nodes, loads)
