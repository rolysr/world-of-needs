from copy import deepcopy
from random import randrange


def csp_offers_requests_policy(offers, needs, balance):
    """
        Basic backtracking auxiliar method for solving
        offers requests policy as a CSP problem
    """

    # first create an array of offers and needs with just the possible options
    valid_offers = [] 
    valid_needs = []
    for offer in offers:
        for need in needs:
            if offer[0] == need[1]: 
                valid_offers.append(offer)
                valid_needs.append(need)

    offers_requests = [offer_request for offer_request in recursive_backtracking([], valid_offers, valid_needs, balance) if offer_request[1] != 0]

    needs, balance = update_needs_balance(offers_requests, offers, needs, balance)

    return offers_requests, needs, balance


def recursive_backtracking(assignment, offers, needs, balance):
    """
        Recursive backtraking that solves the assignment problem
    """
    # if assigment is complete (a possible arrange was selected), then return it
    if len(offers) == len(needs) == 0: 
        return assignment

    # select a random offer that has not been analized
    offer_index, need_index = select_random_offer(offers, needs)
    maximum_value = offers[offer_index][1]
    step = 0.7
    price = offers[offer_index][2]
    offer_id = offers[offer_index]
    need_amount = needs[need_index][2]
    possible_values = [x*step for x in range(int(min(maximum_value, need_amount, balance/price)))]

    # try some possible values
    for value in possible_values:
        # if value is consistent with assignment for the given constraints, added it to assignment
        if value*price <= balance: 
            offer_request = (offer_id, value)
            assignment.append(offer_request)
        
        # try to complete the assignment for the given state
        new_offers, new_needs, new_balance = update_offers_needs_balance(offer_index, need_index, offer_request, offers, needs, balance)
        assignment = recursive_backtracking(assignment, new_offers, new_needs, new_balance)

        # if it is not a failure assignment, then return it
        if assignment != []:
            return assignment

    # failure assignment
    return []

def select_random_offer(offers, needs):
    """
        Select a random offer to be requested. This offers has not
        been analized before and is a valid request. Return the index
        of corresponding offer and need in offers and needs sets respectively.
    """
    if len(offers) == 0 or len(needs) == 0:
        return -1

    offer_index = randrange(0, len(offers))
    need_index = -1
    offer_id = offers[offer_index][0]
    for i in range(len(needs)):
        need_id = needs[i][1]
        if need_id == offer_id:
            need_index = i
            break
        
    return offer_index, need_index

def update_needs_balance(offers_requests, offers, needs, balance):
    """
        Update needs and balance for the given offers
        requests.
    """
    for request in offers_requests:
        for i in range(len(needs)):
            amount_to_buy = request[1]
            if amount_to_buy > 0:  # if human is going to get some need then update his internal state
                needs[i] = (needs[i][0], needs[i][1],
                                    needs[i][2]-amount_to_buy)
                for j in range(len(offers)):
                    if offers[j][0] == needs[i][1]:
                        price = offers[j][2]
                        balance -= amount_to_buy*price  # update human balance
                        # add a request with format (<offer_id>, amount_to_buy)

    return needs, balance


def update_offers_needs_balance(offer_index, need_index, offer_request, offers, needs, balance):
    """
        Update needs and balance for the given offer
        request.
    """
    amount = offer_request[1]
    new_balance = balance - amount*offers[offer_index][2]
    
    new_offers = [offers[i] for i in range(len(offers)) if i != offer_index]
    new_needs = [needs[i] for i in range(len(needs)) if i != need_index]

    return new_offers, new_needs, new_balance