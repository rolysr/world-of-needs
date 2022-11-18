class Graph:
    """
        A class representing a basic graph
    """

    def __init__(self, nodes):
        self.nodes = nodes # A set of nodes that are in the graph

    def __str__(self) -> str:
        response = "Graph:\n"
        for node in self.nodes:
            response += str(node)