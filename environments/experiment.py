from numpy.random import *

class Experiment:
    """
        Abstract class for running a sequence of self improving environment simulations.

        Up to code:
        - set the initial environment
        - a real valued function that analyzes an array of dissatisfaction values 
        from an environment run
        - the params to optimize/check in the experiment
        - the delta function in the params if needed
        - the AI optimization algorithm(s) 
    """
    def __init__(self, number_human_agents, number_destination_agents, number_of_needs, 
        simulation_duration, gini_coef, mean_income, offers_average_price, human_needs_density = None):
        if human_needs_density == None:
            human_needs_density = [exponential(1) for i in range(number_of_needs)]
        
