from agents.destination_agent import *

def generate_destination_agents(number_destination_agents, number_of_needs, store_offers_density, offers_average_price, stores_total_budget, store_distribution, destination_agents_names):
    """
        A method for generating destination agents
    """
    return [DestinationAgent(number_of_needs, store_offers_density, offers_average_price, stores_total_budget * store_distribution[i], destination_agents_names[i]) for i in range(number_destination_agents)]