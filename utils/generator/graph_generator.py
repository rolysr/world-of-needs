from random import randrange
from matplotlib.style import available
from utils.graph.graph import Graph
from utils.graph.node import Node
from utils.generator.street_length_generator import generate_street_length

def generate_graph(human_agents, destination_agents):
    """
        A method for generating a graph for an environment
        given a list of human and destination agents
    """
    n, m = len(human_agents), len(destination_agents)
    nodes = [] # List of nodes
    final_nodes = [] #List of nodes to be added to the graph

    # generate directions array. 6 possible directions
    dirs = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            dirs.append((i, j))

    # This creates the nodes from a corresponding n x m matrix
    for i in range(n):
        row = []
        for j in range(m):
            row.append(Node([], []))
        nodes.append(row)

    # This create the edges for the nodes
    for i in range(n):
        for j in range(m):
            node = nodes[i][j]

            for dir in dirs: # set adyacents for each node
                adyacent_row = i + dir[0]
                adyacent_column = j + dir[1]
                
                if valid_position_in_matrix(n, m, adyacent_row, adyacent_column): # verify valid position in matrix
                    adyacent = nodes[adyacent_row][adyacent_column]
                    edge_weight = generate_street_length()
                    node.adyacents.append((adyacent, edge_weight))

                    if dir in [(0, 1), (1, 0), (1, 1)]: # generate bidirectional edge if node has not been analized
                        adyacent.adyacents.append((node, edge_weight))
            
            final_nodes.append(node[i][j]) # add node to the final list

    # create the graph
    graph = Graph(final_nodes)

    # locate humans and destinations on the graph
    elems = human_agents + destination_agents
    graph = locate_in_graph(graph, elems)

    return graph

    
    
def valid_position_in_matrix(rows, columns, x, y):
    """
        Method for determining if a pair (x, y) is contained in a matrix of rows x columns size
    """
    return x >= 0 and y >= 0 and x < rows and y < columns

def locate_in_graph(graph, elems):
    """
        Locates randomly a group of elems in a graph
    """
    available_node_indexes = []
    for i, node in enumerate(graph.nodes): # check for available nodes
        if node.value == []:
            available_node_indexes.append(i)

    if len(elems) > len(available_node_indexes): # no space for locating nodes then return given graph
        return graph

    # locate elems in available positions
    for elem in elems:
        rand_index = randrange(0, len(available_node_indexes)) # select a random available position
        graph.nodes[rand_index].values.append(elem) # locate elem
        available_node_indexes.remove(rand_index) # update available indexes

    return graph 