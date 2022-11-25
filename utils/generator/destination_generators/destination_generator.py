from agents.destination_agent import *

def generate_destination_agents(number_destination_agents, number_of_needs, store_offers_density):
    """
        A method for generating destination agents
    """
    return [DestinationAgent(number_of_needs, store_offers_density) for i in range(number_destination_agents)]