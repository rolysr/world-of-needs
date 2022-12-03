from numpy.random import *
from enum import *
from agents.human_agent import GLOBAL_HUMAN_AVERAGE_INCOME
from environment import *

# Up to add to settings file
EPS = 1e-9

class optimization_target(Enum):
    STORE_OFFERS_DENSITY = 1
    """
        The function will optimize on the density of the offers amongst all the destination agents.
    """
    OFFERS_PRICE_FACTOR = 2
    """
        The function will optimize on the factor of all the prices.
    """
    TOTAL_BUDGET_FACTOR = 3
    """
        The function will optimize on the total money of the city.
    """
    STORE_DISTRIBUTION = 4
    """
        The function will optimize on the proportion of the city supply a destination agent gets.
    """


class Experiment:
    """
        Abstract class for running a sequence of self improving environment simulations.

        Up to code:
        - the delta function in the params if needed
        - the AI optimization algorithm(s) 
    """

    def __init__(self, number_human_agents, number_destination_agents, number_of_needs,
                 simulation_duration, gini_coef, mean_income, offers_average_price=None, human_needs_density=None,
                 store_offers_density=None, stores_total_budget=None, store_distribution=None):

        self.number_human_agents = number_human_agents
        self.number_destination_agents = number_destination_agents
        self.number_of_needs = number_of_needs
        self.simulation_duration = simulation_duration
        self.gini_coef = gini_coef
        self.mean_income = mean_income
        self.base_offers_average_price = offers_average_price
        self.base_human_needs_density = human_needs_density
        self.base_store_offers_density = store_offers_density
        self.base_stores_total_budget = stores_total_budget
        self.base_store_distribution = store_distribution

    def default_dsat_evaluator(dsat_values):
        mean = 0
        for x in dsat_values:
            mean += x
        mean /= len(dsat_values)
        return mean

    def default_temperature_function(iteration_index):
        return 1.0/iteration_index

    def default_settings(self, dsat_evaluator, temperature_function):
        """
            This function completes initial parameters if not assigned by the constructor fo the experiment.
        """
        offers_average_price = self.base_offers_average_price
        human_needs_density = self.base_human_needs_density
        store_offers_density = self.base_store_offers_density
        stores_total_budget = self.base_stores_total_budget
        store_distribution = self.base_store_distribution

        if self.base_offers_average_price == None:
            base_price = ((GLOBAL_HUMAN_AVERAGE_INCOME +
                          self.mean_income)/2.0)/(self.number_of_needs)
            offers_average_price = [
                base_price for i in range(self.number_of_needs)]
        if self.base_human_needs_density == None:
            human_needs_density = [exponential(1)
                                   for i in range(self.number_of_needs)]
        if self.base_store_offers_density == None:
            store_offers_density = [exponential(
                1) for i in range(self.number_of_needs)]
        if self.base_stores_total_budget == None:
            stores_total_budget = 0
            for price in offers_average_price:
                stores_total_budget += price * self.number_human_agents
        if self.base_store_distribution == None:
            store_distribution = [
                1.0/self.number_destination_agents for i in range(self.number_destination_agents)]

        # Setting default dsat_evaluator if None passed
        if dsat_evaluator == None:
            dsat_evaluator = self.default_dsat_evaluator

        # Setting default temperature_function if None passed
        if temperature_function == None:
            temperature_function = self.default_temperature_function

        # Setting initial factors
        price_factor = 1
        budget_factor = 1

        return (offers_average_price, human_needs_density, store_offers_density, stores_total_budget, store_distribution, dsat_evaluator, temperature_function, price_factor, budget_factor)

    def run_SA_store_offers_density(self, dsat_evaluator, initial_store_offers_density, temperature_function, iterations):
        # Switching optimization_target initial settings
        (offers_average_price, human_needs_density, store_offers_density, stores_total_budget, store_distribution, dsat_evaluator,
         temperature_function, price_factor, budget_factor) = self.default_settings(dsat_evaluator, temperature_function)
        
        if initial_store_offers_density != None:
            store_offers_density = initial_store_offers_density

        actual = Environment(self.number_human_agents, self.number_destination_agents, self.number_of_needs,
                             self.simulation_duration, self.gini_coef, self.mean_income, human_needs_density,
                             offers_average_price, store_offers_density, stores_total_budget, store_distribution)
        eval = actual.run_x_times(dsat_evaluator, 30, 10)

        for it_index in range(iterations):
            temperature = temperature_function(it_index)
            if temperature < EPS:
                break

            new_store_offers_density = self.next_list(
                store_offers_density, it_index, self.number_of_needs)

            actual.sto
            
            delta_eval = 

    def run_simulated_annealing(self, dsat_evaluator, optimization_target: optimization_target,
                                optimization_params, temperature_function, iterations: int = 100):
        """
            Runs a Simulated-Annealing algorithm to optimize some target, minimizing the dissatisfaction 
            function given o saving resources.

            Notes:
            - dsat_evaluator is a function that evaluates a list of dissatisfaction values and returns 
            a real value.
            - optimization_params depends on optimization_target
                - if optimization_target=STORE_OFFERS_DENSITY or optimization_target=STORE_DISTRIBUTION
                then you can put here an array of initial values.
                - if optimization_target=OFFERS_PRICE_FACTOR or optimization_target=TOTAL_BUDGET_FACTOR
                then must pass a tuple (initial_values, penalty_function). Initial values for 
                these targets are self-explained, just a numeric value. penalty_function is for penalizing 
                trivial improvements and the optimization objective is to minimize the penalty function. 
                The penalty function should have two parameters: the evaluation of dissatisfaction and the 
                factor actual value. 
            - temperature_function: evaluates the index of the current iteration an returns a real value.
            Must converge to 0 when the argument increases.
            - iterations is an upperbound on the number of iterations of the simulated annealing algo.
         """
        if optimization_target == optimization_target.STORE_OFFERS_DENSITY:
            self.run_SA_store_offers_density(
                dsat_evaluator, optimization_params, temperature_function, iterations)
        if optimization_target == optimization_target.OFFERS_PRICE_FACTOR:
            self.run_SA_price_factor(
                dsat_evaluator, optimization_params[0], optimization_params[1], temperature_function, iterations)
        if optimization_target == optimization_target.TOTAL_BUDGET_FACTOR:
            self.run_SA_budget_factor(
                dsat_evaluator, optimization_params[0], optimization_params[1], temperature_function, iterations)
        if optimization_target == optimization_target.STORE_DISTRIBUTION:
            self.run_SA_store_distribution(
                dsat_evaluator, optimization_params, temperature_function, iterations)
