from testing.human_agents_generator_test import *
from testing.destination_agents_generator_test import *
from testing.graph_generator_test import *
from testing.income_generator_test import *
from utils.generator.human_generators.human_generator import generate_human_agents
from utils.generator.destination_generators.destination_generator import generate_destination_agents
from environments.environment import *
from environments.experiment import *
import random, math

if __name__ == "__main__":
    # run_human_agents_generator_test(6)
    # run_multi_human_agents_generator_test(10,6)
    # run_destination_agents_generator_test(5, 6)
    # human_agents = generate_human_agents(10, 6)
    # destination_agents = generate_destination_agents(4, 6)
    # graph_generator_test(human_agents, destination_agents)
    # run_income_generator_test()
    number_human_agents = 6
    number_destination_agents = 2
    number_needs = 6
    simulation_duration = 100000
    gini_coef = 0.2
    mean_income = 400
    human_needs_density = [0.1, 0.1, 0.1, 2, 2, 2]
    offers_average_price = [50, 50, 50, 50, 50, 50]
    store_offers_density = [1, 1, 1, 1, 1, 1]
    stores_total_budget = 1800
    store_distribution = [0.5, 0.5]
    env = Environment(number_human_agents, number_destination_agents,
                    number_needs, simulation_duration, gini_coef, mean_income, human_needs_density, offers_average_price, 
                    store_offers_density, stores_total_budget, store_distribution)
    
    def fun(dsat_values):
        mean = 0
        for x in dsat_values:
            mean += x
        mean /= len(dsat_values)
        return mean

    # print(env.run_x_times(fun, 30, 10))

    # env.print_agents()
    # env.run()
    # env.narrate()

    # print(env.run_x_times(fun, 100, 10))

    # env.store_offers_density = human_needs_density

    # print("\n\n**********************************************\n\n")

    # env.reset(accumulate_flag=False)
    # print(env.run_x_times(fun, 100, 10))
    

    # env.print_agents()
    # env.run()
    # env.narrate()
    # env.reset(accumulate_flag=False)

    # env.store_offers_density = store_offers_density

    exp = Experiment(env)

    # def pf_offers_price_factor(dsat, price_factor):
    #     if dsat < 1e6:
    #         return math.exp(1/price_factor)
    #     return dsat - 1e6

    # def pf_total_budget_factor(dsat, budget_factor):
    #     if dsat < 1e6:
    #         return math.exp(budget_factor)
    #     return dsat - 1e6

    # exp.run_hill_climbing(None,optimization_target.STORE_DISTRIBUTION, [0.5, 0.5], 40)
    exp.run_hill_climbing(None,optimization_target.STORE_OFFERS_DENSITY, [1, 1, 1, 1, 1, 1], 40)
    # exp.run_hill_climbing(None,optimization_target.OFFERS_PRICE_FACTOR, (1,pf_offers_price_factor), 40)
    # exp.run_hill_climbing(None,optimization_target.TOTAL_BUDGET_FACTOR, (1,pf_total_budget_factor), 40)

    # for human_agent in env.human_agents:
    #     print(human_agent)
    #     human_agent.narrate()
    # for destination_agent in env.destination_agents:
    #     print(destination_agent)
    #     destination_agent.narrate()
    # run_income_generator_test()
