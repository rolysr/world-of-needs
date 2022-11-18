from uuid import uuid1

class Node:
    """
        A class representing a node in a graph
    """

    def __init__(self, values, adjacents):
        self.id = uuid1() # node identifier
        self.values = values # The set of values stored by the node
        self.adjacents = adjacents # The node's adjacent nodes and an edge cost (destination_node, edge_cost)

    def __eq__(self, other) -> bool:
        return self.id == other.id

    def __str__(self) -> str:
        response = "Node:\n id: {}\n values: {}\n adjacents:\n".format(self.id, self.values)
        for adjacent in self.adjacents:
            response += " Node: id: {}".format(adjacent[0].id)
        return response