from http import client
from agents.agent import Agent
from utils.random_variables import poisson

class DestinationAgent(Agent):
    """
        A class to denote a destination agent
    """

    def __init__(self): # class constructor
        self.offerts = generate_destination_offerts() # The needs this can satisfy by offerts. (need_id, need_available_amout)
        self.attention_time = generate_attention_time() # Attention time for a given client is Poisson-distributed
        self.total_time_working_in_minutes = generate_working_time() # Total time the agent works
        self.elapsed_time_working = 0 # Start time      

