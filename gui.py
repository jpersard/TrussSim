import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox, filedialog
import functions 
import classes

class TrussApp:
    """
    A GUI application for simulating and analyzing truss structures.

    Attributes:
        root (tk.Tk): The root window of the Tkinter application.
        nodes (list): List to store nodes of the truss.
        connections (list): List to store connections between nodes.
        supports (list): List to store supports of the truss.
        loads (list): List to store loads applied to the truss.
        reaction_forces (list): List to store calculated reaction forces.
        frame (ttk.Frame): Main frame of the application.
        import_button (ttk.Button): Button to import truss data.
        process_button (ttk.Button): Button to process truss data.
        output_textbox (scrolledtext.ScrolledText): Textbox to display output and logs.
    """

    def __init__(self, root):
        """
        Initialize the TrussApp with the root window and create the GUI.

        Args:
            root (tk.Tk): The root window of the Tkinter application.
        """
        self.root = root
        self.root.title("Truss Simulation")

        # Data structures to hold truss information
        self.nodes = []
        self.connections = []
        self.supports = []
        self.loads = []
        self.reaction_forces = []

        # Create GUI elements
        self.create_widgets()

    def create_widgets(self):
        """
        Create and layout the GUI elements in the main application window.
        """
        self.frame = ttk.Frame(self.root, padding="10")
        self.frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        self.import_button = ttk.Button(self.frame, text="Import Data", command=self.import_data)
        self.import_button.grid(row=0, column=0, padx=10, pady=10)

        self.process_button = ttk.Button(self.frame, text="Process Truss", command=self.process_truss)
        self.process_button.grid(row=1, column=0, padx=10, pady=10)

        self.save_button = ttk.Button(self.frame, text="Save Calculated Values", command=self.save_calculated_values_dialog)
        self.save_button.grid(row=3, column=0, padx=10, pady=10)

        # Textbox for printing output
        self.output_textbox = scrolledtext.ScrolledText(self.frame, wrap=tk.WORD, width=80, height=20)
        self.output_textbox.grid(row=2, column=0, padx=10, pady=10, sticky=(tk.W, tk.E, tk.N, tk.S))
        self.output_textbox.tag_config("error", foreground="red")  # Configure tag for error messages

        # Configure grid to expand the textbox when window is resized
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        self.frame.columnconfigure(0, weight=1)
        self.frame.rowconfigure(2, weight=1)

    def import_data(self):
        """
        Open a file dialog to select a JSON file and import truss data from it.
        """
        file_path = filedialog.askopenfilename(title="Select JSON Data File", filetypes=[("JSON Files", "*.json")])
        if file_path:
            try:
                self.nodes, self.connections, self.supports, self.loads = functions.import_json(file_path)
                self.output_textbox.insert(tk.END, f"Data imported from {file_path}\n")
                self.output_textbox.insert(tk.END, "Nodes, connections, supports, and loads have been loaded.\n\n")
            except Exception as e:
                self.output_textbox.insert(tk.END, f"Error importing data from {file_path}: {str(e)}\n", "error")

    def process_truss(self):
        """
        Process the truss structure to calculate forces and display the results.
        """
        if not self.nodes or not self.connections or not self.supports or not self.loads:
            messagebox.showwarning("Process Truss", "Please import or add data first.")
            return

        try:
            self.connections, self.reaction_forces = functions.calculate_forces(self.nodes, self.connections, self.supports, self.loads)
            if self.connections is None:
                messagebox.showwarning("Process Truss", "The truss is not statically determined!")
                return

            self.output_textbox.insert(tk.END, "Truss processing started...\n")
            functions.plot_truss_structure(self.connections, self.supports, self.nodes, self.loads, self.reaction_forces)
            self.print_all()
            self.output_textbox.insert(tk.END, "Truss processing completed.\n\n")
        except Exception as e:
            self.output_textbox.insert(tk.END, f"Error processing truss: {str(e)}\n", "error")

    def print_all(self):
        """
        Print all truss data (nodes, connections, supports, loads, and reaction forces) in the output textbox.
        """
        self.output_textbox.insert(tk.END, "Nodes:\n")
        for node in self.nodes:
            self.output_textbox.insert(tk.END, f"{node}\n")
        self.output_textbox.insert(tk.END, "\n")

        self.output_textbox.insert(tk.END, "Connections:\n")
        for connection in self.connections:
            length_rounded = round(connection.length, 2)
            angle_degrees_rounded = round(connection.angle_degrees, 2)
            if hasattr(connection, 'force') and isinstance(connection.force, classes.Force):
                force_magnitude_rounded = round(connection.force.magnitude, 2)
                self.output_textbox.insert(tk.END, f"Connection {connection.node1.name} {connection.node2.name} between {connection.node1.name} and {connection.node2.name} with length {length_rounded} and angle {angle_degrees_rounded} degrees Force: {force_magnitude_rounded}\n")
            else:
                self.output_textbox.insert(tk.END, f"Connection {connection.node1.name} {connection.node2.name} between {connection.node1.name} and {connection.node2.name} with length {length_rounded} and angle {angle_degrees_rounded} degrees\n")
        self.output_textbox.insert(tk.END, "\n")

        self.output_textbox.insert(tk.END, "Supports:\n")
        for support in self.supports:
            self.output_textbox.insert(tk.END, f"{support}\n")
        self.output_textbox.insert(tk.END, "\n")

        self.output_textbox.insert(tk.END, "Loads:\n")
        for load in self.loads:
            self.output_textbox.insert(tk.END, f"{load}\n")
        self.output_textbox.insert(tk.END, "\n")

        self.output_textbox.insert(tk.END, "Reaction forces:\n")
        for force in self.reaction_forces:
            force_magnitude_rounded = round(force.magnitude, 2)
            if isinstance(force, classes.ReactionX):
                self.output_textbox.insert(tk.END, f"Reaction force in the x-direction at node {force.node.name}, magnitude: {force_magnitude_rounded}\n")
            elif isinstance(force, classes.ReactionY):
                self.output_textbox.insert(tk.END, f"Reaction force in the y-direction at node {force.node.name}, magnitude: {force_magnitude_rounded}\n")
        self.output_textbox.insert(tk.END, "\n")

    def save_calculated_values_dialog(self):
            """
            Open a file dialog to select a location to save the calculated values.
            """
            file_path = filedialog.asksaveasfilename(title="Save Calculated Values As", filetypes=[("JSON Files", "*.json")])
            if file_path:
                try:
                    functions.save_calculated_values(self.nodes, self.connections, self.supports, self.loads, self.reaction_forces, file_path)
                    self.output_textbox.insert(tk.END, f"Calculated values saved to {file_path}\n")
                except Exception as e:
                    self.output_textbox.insert(tk.END, f"Error saving calculated values: {str(e)}\n", "error")


if __name__ == "__main__":
    root = tk.Tk()
    app = TrussApp(root)
    app.main()
