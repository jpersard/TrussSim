import matplotlib.pyplot as plt
import classes # type: ignore
import functions # type: ignore
import json


# Import truss data from JSON
truss_data = r'C:\dev\TrussSim\truss_data.json'

with open(truss_data, 'r') as file:
    json_data = json.load(file)

nodes, connections, supports, loads = functions.import_json(json_data)


# Plot the truss structure with loads and forces
functions.plot_truss_structure(connections, supports, nodes, loads)