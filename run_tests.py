from testing.human_agents_generator_test import *
from testing.destination_agents_generator_test import *
from testing.graph_generator_test import *
from testing.income_generator_test import *
from utils.generator.human_generators.human_generator import generate_human_agents
from utils.generator.destination_generators.destination_generator import generate_destination_agents
from environments.environment import *

if __name__ == "__main__":
    # run_human_agents_generator_test(6)
    # run_multi_human_agents_generator_test(10,6)
    # run_destination_agents_generator_test(5, 6)
    # human_agents = generate_human_agents(10, 6)
    # destination_agents = generate_destination_agents(4, 6)
    # graph_generator_test(human_agents, destination_agents)
    number_human_agents = 3
    number_destination_agents = 2
    number_needs = 6
    simulation_duration = 100000
    gini_coef, mean_income = 0.5, 1000
    human_needs_density = [0.4, 0.7, 0.1, 1.5, 2, 1]
    offers_average_price = [100, 100, 100, 100, 100, 100]
    store_offers_density = [1, 1, 1, 1, 1, 1]
    stores_total_budget = 10000
    env = Environment(number_human_agents, number_destination_agents,
                    number_needs, simulation_duration, gini_coef, mean_income, human_needs_density, offers_average_price, 
        store_offers_density, stores_total_budget)
    env.run(5)
    # run_income_generator_test()
