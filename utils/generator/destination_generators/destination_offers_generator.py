from numpy.random import *
from math import *


def generate_destination_offers(number_of_needs, store_offers_density, offers_average_price, store_budget):
    """
        Generate destination offers.
        This takes a number of needs and gets random needs to satisfy
        in a random amount
    """
    offers = []

    # select random needs to make offers
    total_cost = 0
    for i in range(number_of_needs):
        final_price = offers_average_price[i]
        amount = store_offers_density[i] * uniform(0,2)
        # a goal need is a tuple (priority, need_id, needed_amount)
        offers.append((i, amount, final_price))
        total_cost += final_price * amount

    if total_cost > 0:
        normalizing_factor = store_budget / total_cost
        for i in range(len(offers)):
            offers[i] = (offers[i][0], offers[i][1] *
                         normalizing_factor, offers[i][2])
    return offers
