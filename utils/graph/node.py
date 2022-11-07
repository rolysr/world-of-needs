from uuid import uuid1

class Node:
    """
        A class representing a node in a graph
    """

    def __init__(self, values, adyacents):
        self.id = uuid1() # node identifier
        self.values = values # The set of values stored by the node
        self.adyacents = adyacents # The node's adyacent nodes and an edge cost (destination_node, edge_cost)

    def __eq__(self, other) -> bool:
        return self.id == other.id