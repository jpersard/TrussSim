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


class Force:
    """Class representing a force applied to a node in the truss structure."""
    def __init__(self, node, force_x, force_y):
        """
        Initialize a Force object.

        Parameters:
            node (Node): The node where the force is applied.
            force_x (float): Magnitude of the force in the x-direction.
            force_y (float): Magnitude of the force in the y-direction.
        """
        self.node = node
        self.force_x = force_x
        self.force_y = force_y

    def __str__(self):
        return f"Force applied to node {self.node.name}, force: ({self.force_x}, {self.force_y})"


class Load(Force):
    """Class representing a load applied to a node in the truss structure."""
    def __init__(self, node, force_x, force_y):
        """
        Initialize a Load object.

        Parameters:
            node (Node): The node where the load is applied.
            force_x (float): Magnitude of the force in the x-direction.
            force_y (float): Magnitude of the force in the y-direction.
        """
        super().__init__(node, force_x, force_y)


class Reaction(Force):
    """Class representing a reaction force at a support node in the truss structure."""
    def __init__(self, node, force_x, force_y):
        """
        Initialize a Reaction object.

        Parameters:
            node (Node): The node where the reaction force is applied.
            force_x (float): Magnitude of the reaction force in the x-direction.
            force_y (float): Magnitude of the reaction force in the y-direction.
        """
        super().__init__(node, force_x, force_y)
