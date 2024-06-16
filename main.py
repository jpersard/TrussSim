# main.py
import functions
import classes
import numpy as np

# Variables to enable modules
# Later to be set in GUI
do_import = True
do_calculation = True
do_print_all = True
do_plot_truss = True

# Import truss data from JSON
if do_import:
    json_path = r'C:\dev\TrussSim\truss_data.json'
    nodes, connections, supports, loads = functions.import_json(json_path)

# Calculate forces
if do_calculation:
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

    # Print the coefficient matrix
    print("Coefficient Matrix:")
    np.set_printoptions(precision=8, suppress=True)
    print(coefficient_matrix)

    # Print the constant matrix
    print("Constant Matrix:")
    print(constant_matrix)

    # Solve for the variables
    variables = np.linalg.solve(coefficient_matrix, constant_matrix)
    print("Variables (Member Forces and Reactions):")
    print(variables)

    # Assign calculated reaction forces to the support objects for plotting
    for idx, reaction_force in enumerate(reaction_forces):
        reaction_force.magnitude = variables[len(connections) + idx]

# Print all objects
if do_print_all:
    functions.print_all(nodes, connections, supports, loads, reaction_forces)

# Plot the truss structure with loads and forces
if do_plot_truss:
    functions.plot_truss_structure(connections, supports, nodes, loads)

