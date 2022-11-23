from math import inf, sqrt
from utils.graph.algorithms.dijkstra import dijkstra

def astar_heuristic(destination_node, graph, human_agent, destination_agent, number_of_needs):
    """
        Calculate a node heuristic function to a node on a graph
    """
    destination_agent_quality = get_destination_agent_quality(human_agent, destination_agent, number_of_needs) # get destinations qualities
    heuristic = { node: inf for node in graph.nodes } # initialize heuristic
    
    dist = dijkstra(destination_node, graph) # get minimum distance from destination to all other nodes
    
    for node in heuristic.keys(): # update best value for node heuristic
        heuristic[node] = min(heuristic[node], dist[node] * destination_agent_quality * 0.5) 

    # return heuristic
    return heuristic

def quality_coefficient(vector1: list(), vector2: list()):
    """
        A function to calculate the quality of
        two vectors of needs and offers
        The output is a value between 0 and 1
    """
    if len(vector1) != len(vector2): # if vectors don't have same length then return 0 quality
        return 0

    return 1/(1 + (scalar_product(vector1, vector2) / (vector_norm(vector1)**2)))

def scalar_product(vector1, vector2):
    """
        Scalar producto between two real vectors
    """
    result = 0

    if len(vector1) != len(vector2): # return 0 if the lengths are no equal
        return result

    for i in range(len(vector1)):
        result += (vector1[i]*vector2[i])

    return result

def vector_norm(vector):
    """
        Calculate vector norm of a real vector
    """
    result = 0

    for i in range(len(vector)):
        result += (vector[i])**2

    result = sqrt(result)
    
    return result


def get_destination_agent_quality(human_agent, destination_agent, number_of_needs):
    """
        A method that returns the quality value for each 
        destination agent for a given human agent.
        The output is a quality value.
    """
    # the output dictionary
    quality = 0 # a value between 0 and 1
    need_priorities = {}

    # get needs binary vector
    needs_binary_vector = [0] * number_of_needs
    for need in human_agent.needs: # set to 1 the needs that are part of human agent's needs
        needs_binary_vector[need[1]] = need[0]*need[2]
        need_priorities[need[1]] = need[2]

    # get offers binary vector
    offers_binary_vector = [0] * number_of_needs
    for offer in destination_agent.offers:
        try:
            offers_binary_vector[offer[0]] = offer[1]*need_priorities[offer[0]]
        except:
            offers_binary_vector[offer[0]] = offer[1]*0

    # calculate jaccard coefficient
    quality = quality_coefficient(needs_binary_vector, offers_binary_vector)

    # return the quality for each destination
    return quality