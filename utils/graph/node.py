class Node:
    """
        A class representing a node in a graph
    """

    def __init__(self, values, adyacents):
        self.values = values # The set of values stored by the node
        self.adyacents = adyacents # The node's adyacent nodes