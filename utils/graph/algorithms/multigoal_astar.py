from math import inf
from queue import PriorityQueue
from utils.graph.graph import Graph
from utils.graph.node import Node

def multigoal_astar(initial_node: Node, destination_nodes : Node, graph: Graph, heuristic_function: dict() = None):
    """
        A-Star return the best destination node and its actual distance
    """
    # algorithm initialization
    best_first_node = None # best node in distance

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

        if node in destination_nodes: # if we get to the destination node, then astar stops
            best_first_node = node
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
                
    # return best destination node
    return best_first_node