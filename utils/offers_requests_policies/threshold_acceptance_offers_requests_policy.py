from copy import deepcopy
from random import randrange
from utils.offers_requests_policies.common import generate_random_neighbor, generate_random_solution


def threshold_acceptance_offers_requests_policy(offers, income, needs, base_balance, balance, goal_function):
    """
        Threshold acceptance algorithm is a simulated-annealing-based
        optimization algorithm used for combinatorial optimization problems.
        This policy is executed by poor human agents in order to optimize
        their purchase.
    """
    current_offers = deepcopy(offers) # the offers at current time
    current_needs = deepcopy(needs) # the needs at current time
    current_balance = deepcopy(balance) # the balance at current time
    threshold_step = 50 # Threshold annealing step
    best_solution, current_offers, current_needs, current_balance = generate_random_solution(offers, needs, balance) # get an initial solution for the purchase
    best_solution_eval = goal_function(income, current_needs, base_balance, current_balance) # evaluation of initial solution
    q = 700 # starting threshold
    number_of_iterations_per_q = 10 # number of iteration for every value of q (threshold value)

    while q > 50: # while not stopping criteria

        for i in range(number_of_iterations_per_q): # repeat at a fixed q (threshold)
            neighbor = generate_random_neighbor(best_solution, current_offers, current_needs, current_balance) # generate a random valid neighbor
            
            if neighbor is None: #invalid neighbor, there is no possible neighbor
                break
            
            offers_requests, updated_offers, updated_needs, updated_balance = neighbor # get new variables modified after purchase
            neighbor_eval = goal_function(income, updated_needs, base_balance, updated_balance) # how good is the state after purchase
            delta_E = neighbor_eval - best_solution_eval # get the neighbor improvement

            if delta_E <= q: # accept neighbor solution
                best_solution = offers_requests
                best_solution_eval = neighbor_eval

                # accept updated values
                current_offers = updated_offers
                current_balance = updated_balance
                current_needs = updated_needs

        q = q - threshold_step # threshold update

    # return best solution found
    return best_solution, needs, balance

