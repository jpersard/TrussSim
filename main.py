import functions


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
    # Calculate forces and get updated connections and reaction forces
    connections, reaction_forces = functions.calculate_forces(nodes, connections, supports, loads)

# Print all objects
if do_print_all:
    functions.print_all(nodes, connections, supports, loads, reaction_forces)

# Plot the truss structure with loads and forces
if do_plot_truss:
    functions.plot_truss_structure(connections, supports, nodes, loads, reaction_forces)
