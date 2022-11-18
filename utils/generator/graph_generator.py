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

            for dir in dirs: # set adjacents for each node
                adjacent_row = i + dir[0]
                adjacent_column = j + dir[1]
                
                if valid_position_in_matrix(n, m, adjacent_row, adjacent_column): # verify valid position in matrix
                    adjacent = nodes[adjacent_row][adjacent_column]
                    edge_weight = generate_street_length()
                    node.adjacents.append((adjacent, edge_weight))

                    if dir in [(0, 1), (1, 0), (1, 1)]: # generate bidirectional edge if node has not been analized
                        adjacent.adjacents.append((node, edge_weight))
            
            final_nodes.append(node[i][j]) # add node to the final list

    # create graph
    graph = Graph(final_nodes)

    # locate human and destinatio agents
    elems = human_agents + destination_agents
    graph.locate_elems(elems)

    return graph
    
def valid_position_in_matrix(rows, columns, x, y):
    """Method for determining if a pair (x, y) is contained in a matrix of rows x columns size"""
    return x >= 0 and y >= 0 and x < rows and y < columns