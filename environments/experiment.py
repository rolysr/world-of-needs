from numpy.random import *

class Experiment:
    """
        Abstract class for running a sequence of self improving environments simulations.
    """
    def __init__(self, number_human_agents, number_destination_agents, number_of_needs, 
        simulation_duration, gini_coef, mean_income, offers_average_price, human_needs_density = None):
        if human_needs_density == None:
            human_needs_density = [uniform(0,1) for i in range(number_of_needs)]