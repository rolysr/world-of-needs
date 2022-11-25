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

    def locate_agents(self, human_agents, destination_agents):
        """
            Locate given elems on the graph randomly
            Arguments:
            elems list() -- A list of elements
        """
        human_agents_locations, destination_agents_locations = {}, {}
        len_human_agents, len_destination_agents = len(human_agents), len(destination_agents)
        len_total_agents = len_human_agents + len_destination_agents

        if len_total_agents > len(self.nodes): # check if number of elements is valid
            return

        random.shuffle(self.nodes) # shuffle the nodes order to add elements

        for index in range(len_total_agents): # add location to each element
            location = self.nodes[index] # location selected

            if index < len(human_agents): # select agent according to corresponding type
                elem = human_agents[index] 
                human_agents_locations[elem] = location
            else:
                elem = destination_agents[index - len_human_agents]
                destination_agents_locations[elem] = location

        return human_agents_locations, destination_agents_locations