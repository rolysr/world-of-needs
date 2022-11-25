from math import inf
from turtle import distance
from agents.agent import Agent
from utils.generator.human_generators.human_balance_generator import generate_human_balance
from utils.generator.human_generators.human_needs_generator import generate_human_needs
from utils.generator.human_generators.human_speed_generator import generate_human_speed
from utils.generator.human_generators.human_income_generator import generate_human_income
from utils.graph.algorithms.astar import astar
from utils.graph.algorithms.astar_heuristic import astar_heuristic
from utils.graph.algorithms.dijkstra import dijkstra

# up to add to settings file (value taken from https://news.gallup.com/poll/166211/worldwide-median-household-income-000.aspx)
# 2920 is the annual value
GLOBAL_HUMAN_AVERAGE_INCOME = 2920/12
# up to tune for better results, such be done in the testing of the whole simulation to check how it works
TIME_DISSATISFACTION_WEIGHTING_FACTOR = 100
MONEY_DISSATISFACTION_WEIGHTING_FACTOR = 100


class HumanAgent(Agent):
    """
        Class that represents a human agent
    """

    def __init__(self, number_of_needs, gini_coef, mean_income, human_needs_density):  # Class constructor
        super().__init__()
        # This has to be generater using random variables (need_priority, need_id, amount_to_satisfy)
        self.needs = generate_human_needs(number_of_needs, human_needs_density)
        # speed on m/s, this mus be generated with a random variable
        self.speed = generate_human_speed()
        self.visited_destinations = []  # destinations visited by the human agent
        self.income = generate_human_income(gini_coef, mean_income)
        self.balance = generate_human_balance(self.income)
        # This has to be generated using random variables
        self.base_balance = self.balance

    def offers_requests(self, offers):
        """
            With this method the agent receives a list of offers
            and makes a request for adquire some of those offers in order
            to satisfy his needs.
            The returned request will be used by destination agents
        """
        offers_requests = []

        for i in range(len(offers)):
            offer = offers[i]  # offer at position i

            for j in range(len(self.needs)):
                need = self.needs[j]  # need at position j

                # if offer matches the need and then try to satisfy it as possible
                if need[1] == offer[0]:
                    need_amount, offer_amount, price = need[2], offer[1], offer[2]
                    # product amount to be adquired
                    amount_to_buy = min(
                        need_amount, offer_amount, self.balance//price)

                    if amount_to_buy > 0:  # if human is going to get some need then update his internal state
                        self.needs[j] = (need[0], need[1],
                                         need[2]-amount_to_buy)
                        self.balance -= amount_to_buy*price  # update human balance
                        # add a request with format (<offer_id>, amount_to_buy)
                        offers_requests.append((offer[0], amount_to_buy))

        # update needs, just keep track for unsatisfied ones
        self.needs = [need for need in self.needs if need[2] > 0]

        return offers_requests

    def next_destination_to_move(self, human_location, destination_agents_locations, graph, number_of_needs):
        """
            This method receives a location that is the current (initial) agent
            position, a group of destination agents and a graph.  The output is the next destination
            for the agent to moving according to his needs, and the time of arrival having on an account
            the destination distance and human agent speed 
        """
        best_destination_agent = None  # best destination agent
        destination_agents_locations = {destination_agent: destination_agents_locations[destination_agent] for destination_agent in destination_agents_locations.keys(
        ) if destination_agent not in self.visited_destinations}  # set possible destination to go if not visited
        # get real distance for all destination agents
        destinations_real_distances = dijkstra(human_location, graph)
        minimum_real_distance, minimum_heuristic_distance = inf, inf  # minimum distances

        for destination_agent in destination_agents_locations.keys():  # for each desination
            # destination agent location
            location = destination_agents_locations[destination_agent]
            real_dist = destinations_real_distances[location]
            heuristic_function = astar_heuristic(
                location, graph, self, destination_agent, number_of_needs)  # get astar heuristic function
            heuristic_distance = astar(
                human_location, location, graph, heuristic_function)

            if heuristic_distance < minimum_heuristic_distance:  # update the node with the best heuristic distance
                best_destination_agent = destination_agent
                minimum_heuristic_distance = heuristic_distance
                minimum_real_distance = real_dist

        travel_time = minimum_real_distance / self.speed  # calculate time for the travel

        # return best destination to go and the travel time it consumes
        return best_destination_agent, travel_time

    def __str__(self) -> str:
        return "Human Agent:\n id: {}\n needs: {}\n balance: {}\n speed: {}\n visited_destinations: {}\n".format(self.id, self.needs, self.balance, self.speed, self.visited_destinations)

    def dissatisfaction(self, time):
        """
            This is the goal function of a human agent.

            This method receives the actual time of the simulation. Should be called just 
            after a human agent ends its movement in the environment to get the actual 
            dissatisfaction.
        """
        # Let's use time, actual needs and balance to find a satisfaction function
        # Also uses the income rate of the human agent
        normalized_income_rate = self.income / GLOBAL_HUMAN_AVERAGE_INCOME
        # needs dissatisfaction formula
        needs_dissatisfaction = 0
        for tuple in self.needs:
            needs_dissatisfaction += normalized_income_rate*tuple[0]*tuple[2]
        # time dissatisfaction formula
        time_dissatisfaction = time*normalized_income_rate * TIME_DISSATISFACTION_WEIGHTING_FACTOR
        # money dissatisfaction formula
        money_dissatisfaction = (self.base_balance-self.balance)*(
            1 + 1.0/normalized_income_rate)*MONEY_DISSATISFACTION_WEIGHTING_FACTOR
        return needs_dissatisfaction+time_dissatisfaction+money_dissatisfaction
