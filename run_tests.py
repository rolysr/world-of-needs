from testing.human_agents_generator_test import *
from testing.destination_agents_generator_test import *
from testing.graph_generator_test import *
from testing.income_generator_test import *
from utils.generator.human_generators.human_generator import generate_human_agents
from utils.generator.destination_generators.destination_generator import generate_destination_agents
from environments.environment import *
from environments.experiment import *

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
    gini_coef, mean_income = 0.5, 300
    human_needs_density = [0.4, 0.7, 0.1, 1.5, 2, 1]
    offers_average_price = [100, 100, 100, 100, 100, 100]
    store_offers_density = [1, 1, 1, 1, 1, 1]
    stores_total_budget = 10000
    store_distribution = [0.5, 0.5]
    env = Environment(number_human_agents, number_destination_agents,
                    number_needs, simulation_duration, gini_coef, mean_income, human_needs_density, offers_average_price, 
                    store_offers_density, stores_total_budget, store_distribution)
    
    # def fun(dsat_values):
    #     mean = 0
    #     for x in dsat_values:
    #         mean += x
    #     mean /= len(dsat_values)
    #     return mean

    # print(env.run_x_times(fun, 30, 10))


    exp = Experiment(env)
    
    def pf_offers_price_factor(dsat, factor):
        if dsat < 1e6:
            return exp(1 / factor)
        return dsat - 1e6

    def pf_total_budget_factor(dsat, factor):
        if dsat < 1e6:
            return exp(factor)
        return dsat - 1e6

    # exp.run_simulated_annealing(None,optimization_target.STORE_DISTRIBUTION, [0.5, 0.5], None, 40)
    # exp.run_simulated_annealing(None,optimization_target.STORE_OFFERS_DENSITY, [1, 1, 1, 1, 1, 1], None, 100)
    # exp.run_simulated_annealing(None,optimization_target.OFFERS_PRICE_FACTOR, (1,pf_offers_price_factor), None, 40)
    # exp.run_simulated_annealing(None,optimization_target.TOTAL_BUDGET_FACTOR, (1,pf_total_budget_factor), None, 40)

    # for human_agent in env.human_agents:
    #     print(human_agent)
    #     human_agent.narrate()
    # for destination_agent in env.destination_agents:
    #     print(destination_agent)
    #     destination_agent.narrate()
    # run_income_generator_test()
