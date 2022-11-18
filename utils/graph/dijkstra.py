from math import inf
from queue import PriorityQueue
from utils.graph.graph import Graph
from utils.graph.node import Node

def dijkstra(initial_node : Node, graph : Graph):
    """
        Basic Dijkstra algorithm for calculating minimum paths
        from a node to all other nodes on a graph.
        This method receives a graph and returns an array d that
        stores the minimum distance from initial node to a certain node
        on the graph (d is a dict() with values 
        <destination_node, minimum_distance_initial_node_to_destiation_node>)
    """
    # algorithm initialization
    distance_to_node = {} # a dictionary that stores distance from initial_node to all other nodes in the graph
    visited_node = { node : False for node in graph.nodes } # a dictionary that denotes if a nodes has been visited or not
    queue = PriorityQueue() # a data structure for determining the net node to be analized

    for node in graph.nodes:
        distance_to_node[node] = 0 if node == initial_node else inf # the distance from initial node to destination nodes is infinity and to itself is 0
        visited_node[node] = True if node == initial_node else False # initially all nodes are not visited
        queue.put((distance_to_node[node], node)) # add node to priority queue

    while not len(queue) > 0:
        distance, node = queue.get() # get node with minimum distance
        visited_node[node] = True # set visited node as true
        
        for adjacent in node.adjacents: # analize each adjacent node and try to update
            adjacent_node, distance = adjacent[0], adjacent[1] # get adjacent node and its distance from initial
            
            if visited_node[adjacent[0]]: # don't analize visited nodes
                continue
            
            new_distance = distance + distance_to_node[node] # new distance for adjacent node
            if new_distance < distance_to_node[adjacent_node]: # if distance is improved, then update it
                distance_to_node[adjacent_node] = new_distance

    return distance_to_node