from math import inf
from utils.graph.algorithms.dijkstra import dijkstra

def astar_heuristic(destination_nodes, graph, human_agent, destination_agents, number_of_needs):
    """
        Calculate a node heuristic function to each node on a graph
    """
    destination_agents_qualities = get_destination_agents_quality(human_agent, destination_agents, number_of_needs) # get destinations qualities
    heuristic = { node: inf for node in graph.nodes } # initialize heuristic
    
    for dest in destination_nodes.keys(): # calculte distance between destination and all other nodes and recalculate partial heuristic 
        dest_node = destination_nodes[dest] # get destination node in the graph
        dist = dijkstra(dest_node, graph) # get minimum distance from destination to all other nodes
        
        for node in heuristic.keys(): # update best value for node heuristic
            heuristic[node] = min(heuristic[node], dist[node] * (destination_agents_qualities[dest] * 0.5)) 

    # return heuristic
    return heuristic

def jaccard_coefficient(binary_vector1: list(), binary_vector2: list()):
    """
        A function to calculate similarity between two 
        binary nodes. In the case of the problem, it is used 
        to determine how much a binary vector representing a human
        agent's needs is similar to a biary vector representing
        a destination agent's offers.
        To see the idea of the coefficient please got to https://hmong.es/wiki/Jaccard_index
        The output is a value between 0 and 1
    """
    if len(binary_vector1) != binary_vector2:
        return 0

    m00 = m01 = m10 = m11 = 0 # 

    for i in range(len(binary_vector1)):
        if binary_vector1[i] == binary_vector2[i] == 1:
            m11 += 1
        elif binary_vector1[i] == binary_vector2[i] == 0:
            m00 += 1
        elif binary_vector1[i] != binary_vector2[i] and binary_vector1[i] == 1:
            m10 += 1
        else:
            m01 += 1

    return m11/(m10 + m01 + m00)

def get_destination_agents_quality(human_agent, destination_agents, number_of_needs):
    """
        A method that returns the quality value for each 
        destination agent for a given human agent.
        The output is a dict() that contains for each
        destination agent, its quality value.
    """
    # the output dictionary
    quality = dict()

    # get needs binary vector
    needs_binary_vector = [0] * len(number_of_needs)
    for need in human_agent.needs: # set to 1 the needs that are part of human agent's needs
        needs_binary_vector[need[1]] = 1

    for d in destination_agents:
        # get offers binary vector
        offers_binary_vector = [0] * len(number_of_needs)
        for offer in d.offers:
            offers_binary_vector[offer[0]] = 1

        # calculate jaccard coefficient
        quality[d] = jaccard_coefficient(needs_binary_vector, offers_binary_vector)

    # return the quality for each destination
    return quality