from math import inf
from turtle import distance
from agents.agent import Agent
from utils.generator.human_generators.human_balance_generator import generate_human_balance
from utils.generator.human_generators.human_needs_generator import generate_human_needs
from utils.generator.human_generators.human_speed_generator import generate_human_speed
from utils.graph.dijkstra import dijkstra

class HumanAgent(Agent):
    """
        Class that represents a human agent
    """

    def __init__(self, number_of_needs): # Class constructor
        super().__init__() 
        self.needs = generate_human_needs(number_of_needs) # This has to be generater using random variables (need_priority, need_id, amount_to_satisfy)
        self.balance = generate_human_balance() # This has to be generated using random variables
        self.speed = generate_human_speed() # speed on m/s, this mus be generated with a random variable
        self.visited_destination = [] # destinations visited by the human agent

    def offers_requests(self, offers):
        """
            With this method the agent receives a list of offers
            and makes a request for adquire some of those offers in order
            to satisfy his needs.
            The returned request will be used by destination agents
        """
        offers_requests = []

        for i in range(len(offers)):
            offer = offers[i] # offer at position i

            for j in range(len(self.needs)):
                need = self.needs[j] # need at position j

                if need[1] == offer[0]: # if offer matches the need and then try to satisfy it as possible
                    need_amount, offer_amount, price = need[2], offer[1], offer[2]
                    amount_to_buy = self.balance//(min(need_amount, offer_amount)*price) # product amount to be adquired
                    
                    if amount_to_buy > 0: # if human is going to get some need then update his internal state
                        need[2] -= amount_to_buy # update human need
                        self.balance -= amount_to_buy*price # update human balance
                        offers_requests.append((offer[0], amount_to_buy)) # add a request with format (<offer_id>, amount_to_buy)

        self.needs = [need for need in self.needs if need[2] > 0] # update needs, just keep track for unsatisfied ones

        return offers_requests

    def next_destination_to_move(self, human_location, destination_agents_locations, graph):
        """
            This method receives a location that is the current (initial) agent
            position, a group of destination agents and a graph.  The output is the next destination
            for the agent to moving according to his needs, and the time of arrival having on an account
            the destination distance and human agent speed 
        """
        distance_from_initial = dijkstra(human_location, graph) # get distance to all nodes
        minimum_distance = inf # best distance to destination location
        best_destination_agent = None # best destination agent

        for destination in destination_agents_locations.keys(): # try  to select the best next destination to go
            destination_agent_location = destination_agents_locations[destination]
            destination_agent_distance = distance_from_initial[destination_agent_location]

            if minimum_distance > destination_agent_distance and (destination not in self.visited_destination): # is destination is the one with the least distance and is not visited, then got there
                minimum_distance = destination_agent_distance
                best_destination_agent = destination

        travel_time = minimum_distance / self.speed # calculate time for the travel

        return best_destination_agent, travel_time # return best destination to go and the travel time it consumes

    def __str__(self) -> str:
        return "Human Agent:\n id: {}\n needs: {}\n balance: {}\n speed: {}\n visited_destination: {}\n".format(self.id, self.needs, self.balance, self.speed, self.visited_destination)