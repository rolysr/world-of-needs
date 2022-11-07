from http import client
from agents.agent import Agent
from utils.generator.destination_generators.destination_attention_time_generator import generate_destination_attention_time
from utils.generator.destination_generators.destination_offerts_generator import generate_destination_offerts
from utils.generator.destination_generators.destination_working_time_generator import generate_destination_working_time

class DestinationAgent(Agent):
    """
        A class to denote a destination agent
    """

    def __init__(self, number_of_needs): # class constructor
        self.offerts = generate_destination_offerts(number_of_needs) # The needs this can satisfy by offerts. (need_id, need_available_amout, price)
        self.attention_time = generate_destination_attention_time() # Attention time for a given client is Poisson-distributed
        self.total_time_working_in_minutes = generate_destination_working_time() # Total time the agent works
        self.elapsed_time_working = 0 # Start time     
