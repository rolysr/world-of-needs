from random import randrange


def generate_destination_offers(number_of_needs):
    """
        Generate destination offers.
        This takes a number of needs and gets random needs to satisfy
        in a random amount
    """
    number_of_offers = randrange(1, number_of_needs + 1) # number of offers this agent wil supply
    offer_indexes = [i for i in range(number_of_needs)]
    offers = []
    
    # select random needs to make offers
    for i in range(number_of_offers):
        rand_index = randrange(0, len(offer_indexes))
        offers.append((rand_index, 1000, 10)) # an offer is a tuple (need_id, amount, price)
        offer_indexes.remove(rand_index)

    return offers
