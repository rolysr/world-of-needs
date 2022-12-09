from math import inf
from agents.agent import Agent
from utils.generator.human_generators.human_balance_generator import generate_human_balance
from utils.generator.human_generators.human_needs_generator import generate_human_needs
from utils.generator.human_generators.human_speed_generator import generate_human_speed
from utils.generator.human_generators.human_income_generator import generate_human_income
from utils.next_destination_logic.destination_agents_quality import get_destination_agents_quality
from utils.next_destination_logic.distances_from_destination_agents import get_distances_from_destination_agents
from utils.offers_requests_policies.brute_force_offers_requests_policy import brute_force_offers_requests_policy
from utils.offers_requests_policies.genetic_offers_requests_policy import genetic_offers_requests_policy
from utils.offers_requests_policies.threshold_acceptance_offers_requests_policy import threshold_acceptance_offers_requests_policy

# up to add to settings file (value taken from https://news.gallup.com/poll/166211/worldwide-median-household-income-000.aspx)
# 2920 is the annual value
GLOBAL_HUMAN_AVERAGE_INCOME = 2920/12
# up to tune for better results, such be done in the testing of the whole simulation to check how it works
TIME_DISSATISFACTION_WEIGHTING_FACTOR = 5
MONEY_DISSATISFACTION_WEIGHTING_FACTOR = 1


class HumanAgent(Agent):
    """
        Class that represents a human agent
    """

    def __init__(self, number_of_needs, gini_coef, mean_income, human_needs_density):  # Class constructor
        super().__init__()
        # Parameters for the creation of this instance of human agent
        self.number_of_needs = number_of_needs
        self.gini_coef = gini_coef
        self.mean_income = mean_income
        self.human_needs_density = human_needs_density
        # This has to be generater using random variables (need_priority, need_id, amount_to_satisfy)
        self.needs = generate_human_needs(number_of_needs, human_needs_density)
        # speed on m/s, this mus be generated with a random variable
        self.speed = generate_human_speed()
        self.visited_destinations = []  # destinations visited by the human agent
        self.income = generate_human_income(gini_coef, mean_income)
        self.balance = generate_human_balance(self.income)
        # This has to be generated using random variables
        self.base_balance = self.balance
        self.social_class = "high" if self.income >= 2 * \
            mean_income else ('low' if self.income < mean_income else 'medium')

    def offers_requests(self, offers):
        """
            With this method the agent receives a list of offers
            and makes a request for adquire some of those offers in order
            to satisfy his needs.
            The returned request will be used by destination agents
        """
        offers_requests = []

        if self.social_class == "low":
            offers_requests, self.needs, self.balance = threshold_acceptance_offers_requests_policy(
                offers, self.income, self.needs, self.base_balance, self.balance, self.purchase_dissatisfaction)

        elif self.social_class == "medium":
            offers_requests, self.needs, self.balance = genetic_offers_requests_policy(
                offers, self.income, self.needs, self.base_balance, self.balance, self.purchase_dissatisfaction)

        else:
            offers_requests, self.needs, self.balance = brute_force_offers_requests_policy(
                offers, self.needs, self.balance)

        return offers_requests

    def next_destination_to_move(self, human_location, destination_agents_locations, number_of_needs, distances_from_destination_agents):
        """
            This method receives a location that is the current (initial) agent
            position, a group of destination agents and a graph.  The output is the next destination
            for the agent to moving according to his needs, and the time of arrival having on an account
            the destination distance and human agent speed 
        """
        best_destination_agent = None  # best destination agent
        best_destination_quality = inf
        minimum_real_distance = inf
        destination_agents_locations = {destination_agent: destination_agents_locations[destination_agent]
                                        for destination_agent in destination_agents_locations.keys()
                                        if destination_agent not in self.visited_destinations}
        # set possible destination to go if not visited
        destinations_qualities = get_destination_agents_quality(
            self, destination_agents_locations.keys(), number_of_needs)

        # select best destination agent
        for destination in destination_agents_locations.keys():
            # get destination location
            destination_location = destination_agents_locations[destination]
            # get destination distance
            destination_distance_to_human = distances_from_destination_agents[
                destination_location][human_location]
            destination_quality = destination_distance_to_human * \
                destinations_qualities[destination]

            if destination_quality < best_destination_quality:
                best_destination_agent = destination
                best_destination_quality = destination_quality
                minimum_real_distance = destination_distance_to_human

        # calculate time for the travel
        travel_time = minimum_real_distance / (self.speed * 60)

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
        # time dissatisfaction formula
        time_dissatisfaction = time*normalized_income_rate * \
            TIME_DISSATISFACTION_WEIGHTING_FACTOR

        purchase_dissatisfaction = self.purchase_dissatisfaction(
            self.income, self.needs, self.base_balance, self.balance)
            
        return time_dissatisfaction + purchase_dissatisfaction

    def purchase_dissatisfaction(self, income, needs, base_balance, balance):
        """
            Purchase dissatisfaction for getting the
            quality after a human agent purchase process
        """
        # Let's use time, actual needs and balance to find a satisfaction function
        # Also uses the income rate of the human agent
        normalized_income_rate = income / GLOBAL_HUMAN_AVERAGE_INCOME

        # needs dissatisfaction formula
        needs_dissatisfaction = 0
        for tuple in needs:
            needs_dissatisfaction += normalized_income_rate * \
                tuple[0]*(tuple[2]**2)

        # money dissatisfaction formula
        money_dissatisfaction = (base_balance-balance)*(
            1 + 1.0/normalized_income_rate)*MONEY_DISSATISFACTION_WEIGHTING_FACTOR
        return needs_dissatisfaction+money_dissatisfaction

    def reset(self, accumulate_flag=True):
        """
            Reset function for the human agent. This function should be called just 
            before running again the environment. 
        """
        new_needs = generate_human_needs(
            self.number_of_needs, self.human_needs_density)
        if accumulate_flag:
            for new_need in new_needs:
                ok = False
                for i in range(len(self.needs)):
                    actual_need = self.needs[i]
                    if new_need[1] == actual_need[1]:
                        updated_amount = new_need[2] + actual_need[2]
                        self.needs[i] = (
                            actual_need[0], actual_need[1], updated_amount)
                        ok = True
                        break
                if not ok:
                    self.needs.append(new_need)
        else:
            self.needs = new_needs

        self.needs.sort()
        self.needs.reverse()

        self.visited_destinations = []
        if accumulate_flag:
            self.balance += generate_human_balance(self.income)
        else:
            self.balance = generate_human_balance(self.income)
        self.base_balance = self.balance
        self.log_record = list()
