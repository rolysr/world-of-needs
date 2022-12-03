from numpy.random import *
from enum import *

class optimization_target(Enum):
    STORE_OFFERS_DENSITY = 1
    """
        Specifically, the density of the offers amongst all the destination agents.
    """
    OFFERS_PRICE_FACTOR = 2
    """
        The factor of all the prices.
    """
    TOTAL_BUDGET_FACTOR = 3
    """
        The total money of the city.
    """
    STORE_DISTRIBUTION = 4
    """
        Specifically, the proportion of the city supply a destination agent gets.
    """

class Experiment:
    """
        Abstract class for running a sequence of self improving environment simulations.

        Up to code:
        - a real valued function that analyzes an array of dissatisfaction values 
        from an environment run
        - the params to optimize/check in the experiment
        - the delta function in the params if needed
        - the AI optimization algorithm(s) 
    """

    def __init__(self, number_human_agents, number_destination_agents, number_of_needs,
                 simulation_duration, gini_coef, mean_income, offers_average_price = None, human_needs_density = None, 
                 store_offers_density = None, stores_total_budget = None, store_distribution = None):

        self.base_number_human_agents = number_human_agents
        self.base_number_destination_agents = number_destination_agents
        self.base_number_of_needs = number_of_needs
        self.base_simulation_duration = simulation_duration
        self.base_gini_coef = gini_coef
        self.base_mean_income = mean_income
        self.base_offers_average_price = offers_average_price
        self.base_human_needs_density = human_needs_density
        self.base_store_offers_density = store_offers_density
        self.base_stores_total_budget = stores_total_budget
        self.base_store_distribution = store_distribution

    def run_simulated_annealing(dsat_evaluator: function, optimization_target: optimization_target, 
                                optimization_params, time_function: function, iterations: int):
        """
            Runs a Simulated-Annealing algorithm to optimize some target, minimizing the dissatisfaction 
            function given o saving resources.

            Notes:
            - optimization_params depends on optimization_target
                - if optimization_target=STORE_OFFERS_DENSITY or optimization_target=STORE_DISTRIBUTION
                then you can put here an array of initial values.
                - if optimization_target=OFFERS_PRICE_FACTOR or optimization_target=TOTAL_BUDGET_FACTOR
                then must pass a tuple (initial_values, penalty_function, thresholds). Initial values for 
                these targets is self-explained, just a numeric value. penalty_function is for penalizing 
                trivial improvements and thresholds is a pair <penalty, dissatisfaction> target. A solution
                suffices both constraints. 
        """