# Truss Simulation Application

## Overview
The Truss Simulation Application is a graphical user interface (GUI) tool designed to simulate and analyze truss structures. It allows users to import truss data from a JSON file, process the truss to calculate forces, and visualize the truss structure with various forces and supports.

## Features
- **Import Truss Data**: Load truss data from a JSON file.
- **Process Truss**: Calculate forces within the truss and identify reaction forces at supports.
- **Visualization**: Display the truss structure, including nodes, connections, supports, loads, and calculated forces.
- **Detailed Output**: Print detailed information about nodes, connections, supports, loads, and reaction forces.

## Getting Started

### Prerequisites
- Python 3.x
- Required Python packages:
  - `numpy`
  - `matplotlib`
  - `tkinter`
  - `scipy`
  - `sphinx` for docs
  - `sphinx_rtd_theme` for docs

You can install the required packages using `pip`:
```bash
pip install numpy matplotlib tk scipy sphinx sphinx_rtd_theme
```

### Installation
1. Clone this repository:
```bash
git clone https://github.com/yourusername/truss-simulation.git
```
2. Navigate to the project directory:
```bash
cd truss-simulation
```

### Building the Documentation
1. Navigate to the `docs` directory in your repository:
2. Run the following command to build the HTML documentation:
```bash
make html
```
3. View the Documentation
The generated HTML files will be located in the `_build/html` directory. Open `index.html` in a web browser to view the documentation.

### Running the Application
Run the main application script:
```bash
python main.py
```

## Usage
### Importing Truss Data
1. Click on the Import Data button.
2. Select a JSON file containing the truss data.
### Processing the Truss
1. After importing the data, click on the Process Truss button.
2. The application will calculate the forces within the truss   and display the results.
### Truss Data Format
The JSON file should contain the following structure:
```bash
{
    "nodes": [
        [x1, y1],
        [x2, y2],
        ...
    ],
    "connections": [
        [node_index1, node_index2],
        [node_index3, node_index4],
        ...
    ],
    "supports": {
        "node_index": "support_type",
        ...
    },
    "loads": [
        [node_index, magnitude, angle_degrees],
        ...
    ]
}
```

See examples folder for further examples.

## File Descriptions

### main.py
The entry point of the application. It initializes and runs the Truss Simulation GUI.

### classes.py
Defines the core classes for the truss simulation:

- Node: Represents a node in the truss.
- Connection: Represents a connection (edge) between two nodes.
- Support: Represents a support node.
- Force: Represents a force applied to a node.
- Load: Represents a load applied to a node.
- Reaction: Represents a reaction force at a support node.
- ReactionX and ReactionY: Represent reaction forces in the x and y directions, respectively.

### functions.py
Contains the core functions for the truss simulation:

- plot_truss_structure(): Plots the truss structure.
- import_json(): Imports truss data from a JSON file.
- print_all(): Prints all truss data.
- calculate_reaction_forces(): Calculates reaction forces for supports.
- calculate_forces(): Calculates forces in the truss structure.

### gui.py
Defines the TrussApp class, which creates and manages the GUI for the truss simulation application.

## Roadmap
*   Define input format
    *  Input as JSON - Done
    *  Input by GUI - TBD
*   Implement formulas and equations
    *   reaction forces - Done
    *   connection forces - Done
*   2D-Simulation
    *   calculate all forces and reactions - Done
*   3D-Simulation
    *   TBD
*   Visualization
    *   matplotlib graph with truss, forces and values - Done
    *   color coded - Done
*   Graphical User Interface
    *   load Data - Done
    *   process Truss - Done
    *   text output - Done
    *   create new truss - TBD