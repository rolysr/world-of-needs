from math import inf
from queue import PriorityQueue
from utils.graph.algorithms.astar_heuristic import astar_heuristic
from utils.graph.algorithms.dijkstra import dijkstra
from utils.graph.graph import Graph
from utils.graph.node import Node

def astar(initial_node: Node, destination_node : Node, graph: Graph, heuristic_function: dict() = None):
    """
        A-Star return the best destination node and its actual distance
    """
    # algorithm initialization

    # heuristic function is None case
    if heuristic_function is None:
        heuristic_function = { node: 0 for node in graph.nodes }

    # a dictionary that stores distance from initial_node to all other nodes in the graph
    distance_to_node = {}

    # a dictionary that denotes if a nodes has been visited or not
    visited_node = {node: False for node in graph.nodes}

    queue = PriorityQueue()  # a data structure for determining the net node to be analized

    for node in graph.nodes:
        # the distance from initial node to destination nodes is infinity and to itself is 0
        distance_to_node[node] = 0 if node == initial_node else inf
        visited_node[node] = False  # initially all nodes are not visited

    queue.put((0, initial_node))  # add node to priority queue
    size = 1
    while size > 0:
        distance, node = queue.get()  # get node with minimum distance
        size -= 1

        if node == destination_node: # if we get to the destination node, then astar stops
            break

        if visited_node[node]:
            continue
        visited_node[node] = True  # set visited node as true

        for adjacent in node.adjacents:  # analize each adjacent node and try to update
            # get adjacent node and its distance from initial
            adjacent_node, distance = adjacent[0], adjacent[1]

            if visited_node[adjacent_node]:  # don't analize visited nodes
                continue

            # new distance for adjacent node
            new_distance = distance + distance_to_node[node] + heuristic_function[node]
            # if distance is improved, then update it and also, update parent node
            if new_distance < distance_to_node[adjacent_node]:
                distance_to_node[adjacent_node] = new_distance
                queue.put((distance_to_node[adjacent_node], adjacent_node))
                size += 1
                
    return distance_to_node[destination_node]



# dist = dijkstra(initial_node, graph) # get minimum distance from initial node to all other nodes
#     heuristic_dist = dijkstra(initial_node, graph, heuristic_function) # get minimum heuristic distance
#     best_destination_agent = None # best destination agent to go
#     best_heuristic_distance = inf
#     minimum_distance_destination_agent = inf

#     for destination in destination_agents_locations.keys():  # try  to select the best next destination to go
#         destination_agent_location = destination_agents_locations[destination]
#         destination_agent_heuristic_distance = heuristic_dist[destination_agent_location]

#         # is destination is the one with the least distance and is not visited, then got there
#         if best_heuristic_distance > destination_agent_heuristic_distance:
#             best_heuristic_distance = destination_agent_heuristic_distance
#             best_destination_agent = destination
#             minimum_distance_destination_agent = dist[destination_agent_location] 

#     return minimum_distance_destination_agent, best_destination_agent