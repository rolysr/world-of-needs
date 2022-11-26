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
        X = uniform(0, 1)
        threshold = sqrt(store_offers_density[i])
        if X >= threshold:
            continue
        price_factor = uniform(0.8, 1.2)
        final_price = offers_average_price[i]*price_factor
        amount = exponential(2) * sqrt(store_offers_density[i])
        # a goal need is a tuple (priority, need_id, needed_amount)
        offers.append((i, amount, final_price))
        total_cost += offers_average_price[i] * amount

    normalizing_factor = store_budget / total_cost
    for i in range(len(offers)):
        offers[i] = (offers[i][0], offers[i][1] * normalizing_factor, offers[i][2])
    return offers
