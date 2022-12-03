from numpy.random import *
from enum import *
from agents.human_agent import GLOBAL_HUMAN_AVERAGE_INCOME
from environments.environment import *

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

    def default_dsat_evaluator(self, dsat_values):
        mean = 0
        for x in dsat_values:
            mean += x
        mean /= len(dsat_values)
        return mean

    def default_temperature_function(self, iteration_index):
        return 1.0/(iteration_index+1)

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

    def next_list(self, ini_vector, iteration):
        """
            Returns a random vector close to ini_vector.
            Maintains the sum of the ini_vector components.
            Paramater iteration might be used in further implementations.
        """
        ini_sum = 0
        end_sum = 0
        close_vector = ini_vector
        for i in range(len(close_vector)):
            ini_sum += close_vector[i]
            close_vector[i] *= uniform(0.8, 1.2)
            end_sum += close_vector[i]

        for i in range(len(close_vector)):
            close_vector[i] *= ini_sum/end_sum
        return close_vector

    def next_value(self, ini_value, iteration):
        """
            Returns a random value close to ini_value.
            Paramater iteration might be used in further implementations.
        """
        return ini_value * uniform(0.8, 1.2)

    def run_SA_store_offers_density(self, dsat_evaluator, initial_store_offers_density, temperature_function, iterations):
        (offers_average_price, human_needs_density, store_offers_density, stores_total_budget, store_distribution, dsat_evaluator,
         temperature_function, price_factor, budget_factor) = self.default_settings(dsat_evaluator, temperature_function)

        if initial_store_offers_density != None:
            store_offers_density = initial_store_offers_density

        # The environment this optimization is going to use.
        env = Environment(self.number_human_agents, self.number_destination_agents, self.number_of_needs,
                          self.simulation_duration, self.gini_coef, self.mean_income, human_needs_density,
                          offers_average_price, store_offers_density, stores_total_budget, store_distribution)
        eval = env.run_x_times(dsat_evaluator, 30, 10)

        print("The initial state is:\n store_offers_density: {}\n with evaluation: {}".format(
            store_offers_density, eval))

        for it_index in range(iterations):
            temperature = temperature_function(it_index)
            if temperature < EPS:
                break

            new_store_offers_density = self.next_list(
                store_offers_density, it_index)

            env.store_offers_density = new_store_offers_density

            delta_eval = eval - env.run_x_times(dsat_evaluator, 30, 10)

            if delta_eval > EPS:  # improve!
                store_offers_density = new_store_offers_density
                eval -= delta_eval
                continue
            
            if delta_eval / temperature < -40: # Means the probability is 0
                continue
            
            threshold = exp(delta_eval / temperature)
            if uniform(0, 1) < threshold:
                store_offers_density = new_store_offers_density
                eval -= delta_eval

        print("The final state is:\n store_offers_density: {}\n with evaluation: {}".format(
            store_offers_density, eval))

    def run_SA_store_distribution(self, dsat_evaluator, initial_store_distribution, temperature_function, iterations):
        (offers_average_price, human_needs_density, store_offers_density, stores_total_budget, store_distribution, dsat_evaluator,
         temperature_function, price_factor, budget_factor) = self.default_settings(dsat_evaluator, temperature_function)

        if initial_store_distribution != None:
            store_distribution = initial_store_distribution

        # The environment this optimization is going to use.
        env = Environment(self.number_human_agents, self.number_destination_agents, self.number_of_needs,
                          self.simulation_duration, self.gini_coef, self.mean_income, human_needs_density,
                          offers_average_price, store_offers_density, stores_total_budget, store_distribution)
        eval = env.run_x_times(dsat_evaluator, 30, 10)

        print("The initial state is:\n store_distribution: {}\n with evaluation: {}".format(
            store_distribution, eval))

        for it_index in range(iterations):
            temperature = temperature_function(it_index)
            if temperature < EPS:
                break

            new_store_distribution = self.next_list(
                store_distribution, it_index)

            env.store_distribution = new_store_distribution

            delta_eval = eval - env.run_x_times(dsat_evaluator, 30, 10)

            if delta_eval > EPS:  # improve!
                store_offers_density = new_store_distribution
                eval -= delta_eval
                continue
            
            if delta_eval / temperature < -40: # Means the probability is 0
                continue

            threshold = exp(delta_eval / temperature)
            if uniform(0, 1) < threshold:
                store_offers_density = new_store_distribution
                eval -= delta_eval

        print("The final state is:\n store_distribution: {}\n with evaluation: {}".format(
            store_distribution, eval))

    def run_SA_price_factor(self, dsat_evaluator, initial_price_factor, penalty_function, temperature_function, iterations):
        (offers_average_price, human_needs_density, store_offers_density, stores_total_budget, store_distribution, dsat_evaluator,
         temperature_function, price_factor, budget_factor) = self.default_settings(dsat_evaluator, temperature_function)

        price_factor = initial_price_factor
        base_offers_average_price = offers_average_price
        offers_average_price = [price_factor *
                                price for price in base_offers_average_price]

        # The environment this optimization is going to use.
        env = Environment(self.number_human_agents, self.number_destination_agents, self.number_of_needs,
                          self.simulation_duration, self.gini_coef, self.mean_income, human_needs_density,
                          offers_average_price, store_offers_density, stores_total_budget, store_distribution)
        eval = penalty_function(env.run_x_times(
            dsat_evaluator, 30, 10), price_factor)

        print("The initial state is:\n price_factor: {}\n with evaluation: {}".format(
            price_factor, eval))

        for it_index in range(iterations):
            temperature = temperature_function(it_index)
            if temperature < EPS:
                break

            new_price_factor = self.next_value(price_factor, it_index)

            env.offers_average_price = [new_price_factor *
                                        price for price in base_offers_average_price]

            delta_eval = eval - penalty_function(env.run_x_times(
                dsat_evaluator, 30, 10), price_factor)

            if delta_eval > EPS:  # improve!
                price_factor = new_price_factor
                eval -= delta_eval
                continue
            
            if delta_eval / temperature < -40: # Means the probability is 0
                continue

            threshold = exp(delta_eval / temperature)
            if uniform(0, 1) < threshold:
                price_factor = new_price_factor
                eval -= delta_eval

        print("The final state is:\n price_factor: {}\n with evaluation: {}".format(
            price_factor, eval))

    def run_SA_budget_factor(self, dsat_evaluator, initial_budget_factor, penalty_function, temperature_function, iterations):
        (offers_average_price, human_needs_density, store_offers_density, stores_total_budget, store_distribution, dsat_evaluator,
         temperature_function, price_factor, budget_factor) = self.default_settings(dsat_evaluator, temperature_function)

        budget_factor = initial_budget_factor
        base_stores_total_budget = stores_total_budget

        # The environment this optimization is going to use.
        env = Environment(self.number_human_agents, self.number_destination_agents, self.number_of_needs,
                          self.simulation_duration, self.gini_coef, self.mean_income, human_needs_density,
                          offers_average_price, store_offers_density, base_stores_total_budget * budget_factor, store_distribution)
        eval = penalty_function(env.run_x_times(
            dsat_evaluator, 30, 10), budget_factor)

        print("The initial state is:\n budget_factor: {}\n with evaluation: {}".format(
            budget_factor, eval))

        for it_index in range(iterations):
            temperature = temperature_function(it_index)
            if temperature < EPS:
                break

            new_budget_factor = self.next_value(budget_factor, it_index)

            env.stores_total_budget = new_budget_factor * base_stores_total_budget

            delta_eval = eval - penalty_function(env.run_x_times(
                dsat_evaluator, 30, 10), budget_factor)

            if delta_eval > EPS:  # improve!
                budget_factor = new_budget_factor
                eval -= delta_eval
                continue
            
            if delta_eval / temperature < -40: # Means the probability is 0
                continue

            threshold = exp(delta_eval / temperature)
            if uniform(0, 1) < threshold:
                budget_factor = new_budget_factor
                eval -= delta_eval

        print("The final state is:\n budget_factor: {}\n with evaluation: {}".format(
            budget_factor, eval))

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
                factor value in that order. 
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
