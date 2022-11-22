from math import inf
from utils.graph.algorithms.astar_heuristic import astar_heuristic
from utils.graph.algorithms.dijkstra import dijkstra
from utils.graph.graph import Graph
from utils.graph.node import Node

def astar(initial_node: Node, destination_agents_locations : dict(), graph: Graph, heuristic_function: dict() = None):
    """
        A-Star return the best destination node and its actual distance
    """

    dist = dijkstra(initial_node, graph) # get minimum distance from initial node to all other nodes
    heuristic_dist = dijkstra(initial_node, graph, heuristic_function) # get minimum heuristic distance
    best_destination_agent = None # best destination agent to go
    best_heuristic_distance = inf
    minimum_distance_destination_agent = inf

    for destination in destination_agents_locations.keys():  # try  to select the best next destination to go
        destination_agent_location = destination_agents_locations[destination]
        destination_agent_heuristic_distance = heuristic_dist[destination_agent_location]

        # is destination is the one with the least distance and is not visited, then got there
        if best_heuristic_distance > destination_agent_heuristic_distance:
            best_heuristic_distance = destination_agent_heuristic_distance
            best_destination_agent = destination
            minimum_distance_destination_agent = dist[destination_agent_location] 

    return minimum_distance_destination_agent, best_destination_agent