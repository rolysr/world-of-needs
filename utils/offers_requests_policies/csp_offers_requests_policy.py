def backtracking_search(offers, needs, balance):
    """
        Basic backtracking auxiliar method for solving
        offers requests policy as a CSP problem
    """
    return [offer_request for offer_request in recursive_backtracking([], offers, needs, balance) if offer_request[1] != 0]

def recursive_backtracking(assignment, offers, needs, balance):
    """
        Recursive backtraking that solves the assignment problem
    """
    # if assigment is complete (a possible arrange was selected), then return it
    if len(assignment) == len(offers): 
        return assignment

    # select a random offer that has not been analized
    offer_index, need_index = select_random_offer(assignment, offers, needs)
    maximum_value = offers[offer_index][1]
    step = 0.7
    possible_values = [x*step for x in range(maximum_value)]
    price = offers[offer_index[2]]
    offer_id = offers[offer_index]
    need_amount = needs[need_index][2]

    # try some possible values
    for value in possible_values:
        # if value is consistent with assignment for the given constraints, added it to assignment
        if value*price <= balance and value < need_amount: 
            offer_request = (offer_id, value)
            assignment.append(offer_request)
        
        # try to complete the assignment for the given state
        new_offers, new_needs, new_balance = update_offers_needs_balance(offer_request, offers, needs, balance)
        assignment = recursive_backtracking(assignment, new_offers, new_needs, new_balance)

        # if it is not a failure assignment, then return it
        if assignment != []:
            return assignment

    # failure assignment
    return []

def select_random_offer(assignment, offers, needs):
    """
        Select a random offer to be requested. This offers has not
        been analized before and is a valid request. Return the index
        of corresponding offer and need in offers and needs sets respectively.
    """
    pass

def update_offers_needs_balance(offer_request, offers, needs, balance):
    """
        Update offers, needs and balance for the given offer
        request.
    """
    pass