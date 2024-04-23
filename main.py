# main.py
import functions

# Variables to enable modules
# Later to be set in GUI
do_import = True
do_reaction = True
do_print_all = True
do_plot_truss = False

# Import truss data from JSON
if do_import:
    json_path = r'C:\dev\TrussSim\truss_data.json'
    nodes, connections, supports, loads = functions.import_json(json_path)

# Calculate reaction forces
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

# Print all objects
if do_print_all:
    functions.print_all(nodes, connections, supports, loads, reaction_forces)

# Plot the truss structure with loads and forces
if do_plot_truss:
    functions.plot_truss_structure(connections, supports, nodes, loads)
