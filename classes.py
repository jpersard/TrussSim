# classes.py
# Classes for TrussSim

import math


class Node:
    """Class representing a node in the truss structure."""
    def __init__(self, name, x, y):
        """
        Initialize a Node object.

        Parameters:
            name (str): Name of the node.
            x (float): x-coordinate of the node.
            y (float): y-coordinate of the node.
        """
        self.name = name
        self.x = x 
        self.y = y

    def __str__(self):
        return f"Node {self.name} at ({self.x}, {self.y})"

class Connection:
    """Class representing a connection (edge) between two nodes in the truss structure."""
    def __init__(self, node1, node2):
        """
        Initialize a Connection object.

        Parameters:
            node1 (Node): First node connected by the connection.
            node2 (Node): Second node connected by the connection.
        """
        self.node1 = node1
        self.node2 = node2
        self.name = node1.name + node2.name  # Generate name based on connected nodes

    def __str__(self):
        return f"Connection {self.name} between {self.node1.name} and {self.node2.name}"

class Support:
    """Class representing a support node in the truss structure."""
    def __init__(self, node, support_type):
        """
        Initialize a Support object.

        Parameters:
            node (Node): The supported node.
            support_type (str): Type of support (e.g., 'pin' or 'roller').
        """
        self.node = node
        self.support_type = support_type

    def __str__(self):
        return f"Support at node {self.node.name}, type: {self.support_type}"
    
    def initialize_reaction_forces(self):
        """Initialize reaction forces based on the support type."""
        if self.support_type == 'pin':
            return [ReactionX(self.node, 0), ReactionY(self.node, 0)]
        elif self.support_type == 'roller':
            return [ReactionY(self.node, 0)]
        else:
            return []

class Force:
    """Class representing a force applied to a node in the truss structure."""
    def __init__(self, node, magnitude, angle_degrees):
        """
        Initialize a Force object.

        Parameters:
            node (Node): The node where the force is applied.
            magnitude (float): Magnitude of the force.
            angle_degrees (float): Angle of the force in degrees.
        """
        self.node = node
        self.magnitude = magnitude
        self.angle_radians = math.radians(angle_degrees)

    def __str__(self):
        return f"Force applied to node {self.node.name}, magnitude: {self.magnitude}, angle: {math.degrees(self.angle_radians)} degrees"

class Load(Force):
    """Class representing a load applied to a node in the truss structure."""
    def __init__(self, node, magnitude, angle_degrees):
        """
        Initialize a Load object.

        Parameters:
            node (Node): The node where the load is applied.
            magnitude (float): Magnitude of the load.
            angle_degrees (float): Angle of the load in degrees.
        """
        super().__init__(node, magnitude, angle_degrees)
        self.angle_degrees = angle_degrees

class Reaction(Force):
    """Class representing a reaction force at a support node in the truss structure."""
    def __init__(self, node, magnitude, angle_degrees):
        """
        Initialize a Reaction object.

        Parameters:
            node (Node): The node where the reaction force is applied.
            magnitude (float): Magnitude of the reaction force.
            angle_degrees (float): Angle of the reaction force in degrees.
        """
        super().__init__(node, magnitude, angle_degrees)

class ReactionX(Reaction):
    """Class representing a reaction force in the x-direction at a support node."""
    def __init__(self, node, magnitude):
        """
        Initialize a ReactionX object.

        Parameters:
            node (Node): The node where the reaction force is applied.
            magnitude (float): Magnitude of the reaction force in the x-direction.
        """
        super().__init__(node, magnitude, 0)  # Angle is 0 degrees for reaction in x-direction

    def __str__(self):
        return f"Reaction force in the x-direction at node {self.node.name}, magnitude: {self.magnitude}"

class ReactionY(Reaction):
    """Class representing a reaction force in the y-direction at a support node."""
    def __init__(self, node, magnitude):
        """
        Initialize a ReactionY object.

        Parameters:
            node (Node): The node where the reaction force is applied.
            magnitude (float): Magnitude of the reaction force in the y-direction.
        """
        super().__init__(node, magnitude, 90)  # Angle is 90 degrees for reaction in y-direction

    def __str__(self):
        return f"Reaction force in the y-direction at node {self.node.name}, magnitude: {self.magnitude}"