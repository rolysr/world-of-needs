from agents.agent import Agent
from utils.generator.destination_generators.destination_attention_time_generator import generate_destination_attention_time
from utils.generator.destination_generators.destination_offers_generator import generate_destination_offers
from utils.generator.destination_generators.destination_working_time_generator import generate_destination_working_time

class DestinationAgent(Agent):
    """
        A class to denote a destination agent
    """

    def __init__(self, number_of_needs): # class constructor
        super().__init__() # init parent Agent class
        self.offers = generate_destination_offers(number_of_needs) # The needs this can satisfy by offers. (need_id, need_available_amout, price)
        self.attention_time = generate_destination_attention_time() # Attention time for a given client is Poisson-distributed
        self.total_time_working = generate_destination_working_time() # Total time the agent works
        self.next_available_time = 0 # During execution it denotes the time the system will be available for the next client  

    def process_offers_requests(self, offers_requests):
        """
            This method checks if the offers request is valid and
            updates destination agent internal state
        """
        for request in offers_requests:
            for j in range(len(self.offers)):
                offer = self.offers[j] # offer at position j
                if offer[0] == request[0]: # offer id matches offer request id
                    offer[1] -= request[1] # update amount of remaining offers

        self.offers = [offer for offer in self.offers if offer[1] > 0] # update offers by keeping track of offers with amount greater than zero

    def __str__(self) -> str:
        return "Destination Agent:\n id: {}\n offers: {}\n attention_time: {}\n total_time_working: {}\n next_available_time: {}\n".format(self.id, self.offers, self.attention_time, self.total_time_working, self.next_available_time)