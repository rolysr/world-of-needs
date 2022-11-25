from numpy.random import *
from math import *


def generate_destination_offers(number_of_needs, store_offers_density, offers_average_price):
    """
        Generate destination offers.
        This takes a number of needs and gets random needs to satisfy
        in a random amount
    """
    offers = []

    # select random needs to make offers
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

    return offers
