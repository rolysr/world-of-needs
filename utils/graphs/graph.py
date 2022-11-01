class Graph:
    """
        A class representing a basic graph
    """

    def __init__(self, nodes, edges):
        self.nodes = nodes # A set of nodes that are in the graph
        self.edges = edges # A set of edges between the nodes from the graph (a, b, w) This represents an edge from a to b with weight w