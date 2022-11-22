from math import inf
from utils.graph.algorithms.astar_heuristic import astar_heuristic
from utils.graph.algorithms.dijkstra import dijkstra
from utils.graph.graph import Graph
from utils.graph.node import Node

def astar(initial_node: Node, graph: Graph, heuristic_function: dict() = None):
    """
        A-Star return the best destination node and its actual distance
    """

    dist = dijkstra(initial_node, graph) # get minimum distance from initial node to all other nodes
    heuristic_dist = dijkstra(initial_node, graph, heuristic_function) # get minimum heuristic distance
    best_destination_node = None # best destination node
    best_heuristic_distance = inf

    for node in heuristic_dist.keys():
        if best_heuristic_distance > heuristic_dist[node]:
            best_destination_node = node
            best_heuristic_distance[node]

    return dist[best_destination_node], best_destination_node 
