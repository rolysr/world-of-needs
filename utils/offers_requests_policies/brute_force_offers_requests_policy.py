def brute_force_offers_requests_policy(offers, needs, balance):
    """
        Brute force policy for making offers requests.
        This policy is used to be executed by rich human
        agents.
    """
    offers_requests = []

    for i in range(len(offers)):
        offer = offers[i]  # offer at position i

        for j in range(len(needs)):
            need = needs[j]  # need at position j

            # if offer matches the need and then try to satisfy it as possible
            if need[1] == offer[0]:
                need_amount, offer_amount, price = need[2], offer[1], offer[2]
                # product amount to be adquired
                amount_to_buy = min(
                    need_amount, offer_amount, balance//price)

                if amount_to_buy > 0:  # if human is going to get some need then update his internal state
                    needs[j] = (need[0], need[1],
                                        need[2]-amount_to_buy)
                    balance -= amount_to_buy*price  # update human balance
                    # add a request with format (<offer_id>, amount_to_buy)
                    offers_requests.append((offer[0], amount_to_buy))

    # update needs, just keep track for unsatisfied ones
    needs = [need for need in needs if need[2] > 0]

    return offers_requests, needs, balance