class Node:
    """
        A class representing a node in a graph
    """

    def __init__(self, adjacents, id):
        self.id = id # node identifier
        self.adjacents = adjacents # The node's adjacent nodes and an edge cost (destination_node, edge_cost)

    def __eq__(self, other) -> bool:
        return self.id == other.id

    def __str__(self) -> str:
        response = "Node:\n id: {}\n adjacents:\n".format(self.id)
        for adjacent in self.adjacents:
            response += " Node: id: {0}, edge length: {1}\n".format(adjacent[0].id,adjacent[1])
        return response
    
    def __hash__(self) -> int:
        return self.id
    
    def __lt__(self, other) -> bool:
        return self.id<other.id