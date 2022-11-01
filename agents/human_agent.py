from agents.agent import Agent

class HumanAgent(Agent):
    """
        Class that represents a human agent
    """

    def __init__(self): # Class constructor
        super().__init__()
        self.needs = [(1, 10, 1), (2, 10, 3)] # This has to be generater using random variables (need_id, amount_to_satisfy, need_priority)
        self.balance = 100 # This has to be generated using random variables
        self.on_queue = False #Denotes if an agent is on a queue
        self.speed = 0.92 # speed on m/s, this mus be generated with a random variable
        self.location = None