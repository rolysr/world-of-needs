from agents.destination_agent import *

def generate_destination_agents(number_destination_agents, number_of_needs):
    """
        A method for generating destination agents
    """
    return [DestinationAgent(number_of_needs) for i in range(number_destination_agents)]