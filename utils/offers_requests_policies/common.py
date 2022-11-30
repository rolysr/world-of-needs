from copy import deepcopy
from random import randrange


def generate_random_solution(current_offers, current_needs, current_balance):
    """
        Generates an acceptable random initial solution for the problem
        of making a request given some offers
    """
    offers_requests = []
    offers = deepcopy(current_offers)
    needs = deepcopy(current_needs)
    balance = deepcopy(current_balance)

    for i in range(len(offers)):
        offer = offers[i]  # offer at position i

        for j in range(len(needs)):
            need = needs[j]  # need at position j

            # if offer matches the need and then try to satisfy it as possible
            if need[1] == offer[0]:
                need_amount, offer_amount, price = need[2], offer[1], offer[2]
                # product amount to be adquired. Random possible purchase
                amount_to_buy = randrange(0, min(
                    need_amount, offer_amount, balance//price))

                if amount_to_buy > 0:  # if human is going to get some need then update his internal state
                    needs[j] = (need[0], need[1],
                                        need[2]-amount_to_buy)
                    balance -= amount_to_buy*price  # update human balance
                    # add a request with format (<offer_id>, amount_to_buy)
                    offers_requests.append((offer[0], amount_to_buy))
                    offers[i][1] -= amount_to_buy #update offers

    # update needs, just keep track for unsatisfied ones
    needs = [need for need in needs if need[2] > 0]

    return offers_requests, offers, needs, balance

def generate_random_neighbor(current_solution, current_offers, current_needs, current_balance):
    """
        Generates a random neighbor for the given solution.
        This neighbor is based on current state of offers,
        balance and needs.
        Basically this method selects a possible offer to
        purchase and then takes an amount that is best for agent
    """
    offers_requests = deepcopy(current_solution)
    offers = deepcopy(current_offers)
    needs = deepcopy(current_needs)
    balance = deepcopy(current_balance)

    offers_needs_match_indexes = []
    for i in range(len(offers)): # first get all position where needs and offers match
        offer = offers[i]  # offer at position i
        for j in range(len(needs)):
            need = needs[j]  # need at position j
            # if offer matches the need and then try to satisfy it as possible
            if need[1] == offer[0]:
                offers_needs_match_indexes.append((i,j))

    rand_index = randrange(0, len(offers_needs_match_indexes)) # select a random index in order to purchase the corresponding need

    offer, need = offers[offers_needs_match_indexes[rand_index][0]], needs[offers_needs_match_indexes[rand_index][1]] # select offer and need

    need_amount, offer_amount, price = need[2], offer[1], offer[2]
    # product amount to be adquired. Random possible purchase
    amount_to_buy = min(
        need_amount, offer_amount, balance//price)

    if amount_to_buy > 0:  # if human is going to get some need then update his internal state
        needs[j] = (need[0], need[1],
                            need[2]-amount_to_buy)
        balance -= amount_to_buy*price  # update human balance
        # update a request with format (<offer_id>, amount_to_buy)
        for i in range(len(offers_requests)):
            if offer[0] == offers_requests[i][0]:
                offers_requests[i][1] += amount_to_buy
            
        offers[offers_needs_match_indexes[rand_index][0]][1] -= amount_to_buy #update offers

    # update needs, just keep track for unsatisfied ones
    needs = [need for need in needs if need[2] > 0]

    return offers_requests, offers, needs, balance