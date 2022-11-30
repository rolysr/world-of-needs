from copy import deepcopy
from math import inf
from random import randrange, uniform
from utils.offers_requests_policies.common import generate_random_neighbor, generate_random_solution


def genetic_offers_requests_policy(offers, income, needs, base_balance, balance, goal_function):
    """
        genetic algorithm is used as a solution of a variation
        of knapsack problem with repetition applied to this problem.
        This policy is executed by mean class human agents in order to optimize
        their satisfaction over the money they spend.
    """
    population, mean_fitness = generate_initial_population(offers, income, needs, base_balance, balance, goal_function) # generate initial population
    number_iterations = 100
    
    for i in range(number_iterations): # stopping criteria: number of iterations
        new_population = []

        for i in range(len(population)):
            x = random_selection(population, mean_fitness)
            y = random_selection(population, mean_fitness)
            if x != y: # if x is different from y as individual
                child = reproduce(x, y, offers, needs, balance)

            if uniform(0, 1) < 1/3:
                child = mutate(child)

            new_population.append(child)
        
        population = new_population # update population

    answer = best_individual(population) # get best solution
    offers_requests, needs, balance = answer[0], answer[2], answer[3] # get the updated return variables

    return offers_requests, needs, balance

def generate_initial_population(offers, income, needs, base_balance, balance, goal_function, population_lenght=10):
    """
        Generates initial population of the genetic algorithm.
        A population is a set of possible solutions for the
        given problem
    """
    population = []
    mean_fitness = 0
    for i in range(population_lenght):
        individual = generate_random_solution(offers, needs, balance)
        if individual not in population:
            fitness = goal_function(income, individual[2], base_balance, individual[3]) # get individual fitness
            mean_fitness += fitness
            population.append((individual, fitness))

    mean_fitness = mean_fitness/len(population)

    return population, mean_fitness

def random_selection(population, goal_function, threshold):
    """
        Selects a random individual randomly based on a given threshold
    """
    best_individuals = [(individual, fitness) for (individual, fitness) in population if fitness < threshold] # select a group of individuals whose fitness is better than some threshold
    rand_index = randrange(0, len(best_individuals))
    individual = best_individuals[rand_index][1]
    
    return individual

def reproduce(x, y, offers, needs, balance):
    """
        Reproduces two individuals (solutions) in order
        to get a child who is the result of the defined
        reproduction. Children are part of new population
    """
    offers_requests = []
    index_not_matching_offers = set() # indexes of offers that did not matched in offers requests
    current_offers, current_needs, current_balance = deepcopy(offers), deepcopy(needs), deepcopy(balance)

    offers_requests_x, offers_requests_y = x[0], y[0] # get individual's offers requests
    for i in range(len(offers_requests_x)):
        offer_request_x = offers_requests_x[i]
        for j in range(len(offers_requests_y)):
            offer_request_y = offers_requests_y[j]

            if offer_request_x[0] == offer_request_y[0]: # in case there is a common offert, create a new offert with the average selection
                amount_to_buy = (offer_request_x[1] + offer_request_y[1]) / 2
                if amount_to_buy > 0:
                    offers_requests.append((offer_request_x[0], amount_to_buy))
            
            else: # if they do not match
                index1 = offer_request_x[0]
                index2 = offer_request_y[0]
                index_not_matching_offers.add(index1)
                index_not_matching_offers.add(index2)

    # update the matching requests
    for request in offers_requests:
        need_index = get_needs_index_with_id(request[0], needs)
        offer_index = get_offers_index_with_id(request[0], offers)
        amount_to_buy = request[1]
        current_balance -= amount_to_buy*offers[offer_index][2]
        current_needs[need_index] = (current_needs[need_index][0], current_needs[need_index][1], current_needs[need_index][2]-amount_to_buy)
        current_offers[offer_index][1] -= amount_to_buy

    # update needs, just keep track for unsatisfied ones
    current_needs = [need for need in current_needs if need[2] > 0]
    index_not_matching_offers = list(index_not_matching_offers)

    for i in range(len(current_offers)): # analize all not matching offers for the given requests
        offer = current_offers[i]
        for j in range(len(current_needs)):
            need = current_needs[j]
            if offers[i][0] == needs[j][0] and (offers[i][0] in index_not_matching_offers):
                need_amount, offer_amount, price = need[2], offer[1], offer[2]
                # product amount to be adquired
                amount_to_buy = min(
                    need_amount, offer_amount, current_balance//price)

                if amount_to_buy > 0:  # if human is going to get some need then update his internal state
                    needs[j] = (need[0], need[1],
                                        need[2]-amount_to_buy)
                    current_balance -= amount_to_buy*price  # update human balance
                    # add a request with format (<offer_id>, amount_to_buy)
                    offers_requests.append((offer[0], amount_to_buy))

    return offers_requests, current_offers, current_needs, current_balance


def best_individual(population):
    """
        Method for getting the individual
        with the best fitness value (least fitness value).
        This individual is the algorithm final answer
    """
    best_i, best_fitness = None, inf
    for individual, fitness in population:
        if fitness < best_fitness: # if better individual found, then update best individual
            best_fitness = fitness
            best_i = individual

    return best_i

def get_offers_index_with_id(id, offers):
    """
        Get index for element with the given id
        in the offers
    """
    for i in range(len(offers)):
        if offers[0] == id:
            return i
    
    return -1

def get_needs_index_with_id(id, needs):
    """
        Get index for element with the given id
        in the needs
    """
    for i in range(len(needs)):
        if needs[1] == id:
            return i
    
    return -1

def mutate(individual):
    """
        Mutate method in order to make a difference
        for new population with some probability
    """
    individual = generate_random_neighbor(*individual)
    return individual