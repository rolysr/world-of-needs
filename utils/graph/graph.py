import random

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
        return response

    def locate_elems(self, elems):
        """
            Locate given elems on the graph randomly
            Arguments:
            elems list() -- A list of elements
        """

        if len(elems) > len(self.nodes): # check if number of elements is valid
            return

        random.shuffle(self.nodes) # shuffle the nodes order to add elements

        for index in range(len(elems)): # add elements
            self.nodes[index].values.append(elems[index])