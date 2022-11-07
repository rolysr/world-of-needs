from agents.agent import Agent
from utils.generator.human_generators.human_balance_generator import generate_human_balance
from utils.generator.human_generators.human_needs_generator import generate_human_needs
from utils.generator.human_generators.human_speed_generator import generate_human_speed

class HumanAgent(Agent):
    """
        Class that represents a human agent
    """

    def __init__(self, number_of_needs): # Class constructor
        self.needs = generate_human_needs(number_of_needs) # This has to be generater using random variables (need_id, amount_to_satisfy, need_priority)
        self.balance = generate_human_balance() # This has to be generated using random variables
        self.speed = generate_human_speed() # speed on m/s, this mus be generated with a random variable