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

# Calculate reaction forces
coefficients_matrix = np.array([[1, 0, 0, 0, 0], [0, 1, 1, 0, 1], [0, 0, 6, 0, 3]])
constants_vector = np.array([0, 0, 0])
reaction_forces = np.linalg.solve(coefficients_matrix, constants_vector)

# Plot the truss structure with loads and forces
functions.plot_truss_structure(connections, supports, nodes, loads)
