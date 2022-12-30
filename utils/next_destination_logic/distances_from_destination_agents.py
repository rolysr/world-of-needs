from utils.graph.algorithms.dijkstra import dijkstra


def get_distances_from_destination_agents(destination_agents_locations, graph):
    """
        This method returns a dictionary that maps
        a destination agent location to its distance to
        other graph location
    """
    distances_from_destination_agents = {} # answer variable
    destination_agents = list(destination_agents_locations.keys()) # destination agents

    # calculate distance between each pair of destination agents
    for i in range(len(destination_agents)):
        # get destination agent
        destination_agent_1 = destination_agents[i]

        # get destination agent location
        destination_agent_location_1 = destination_agents_locations[destination_agent_1]

        # get distance to all others nodes in the graph
        distance_destination_agent_to_other_nodes = dijkstra(destination_agent_location_1, graph)

        distances_from_destination_agents[destination_agent_location_1] = distance_destination_agent_to_other_nodes 

    return distances_from_destination_agents   