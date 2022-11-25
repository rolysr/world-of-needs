from numpy.random import *
from math import *


def generate_human_needs(number_of_needs, human_needs_density):
    """
        A method for generating human needs
    """
    goal_needs = []

    # select random needs
    for i in range(number_of_needs):
        X = uniform(0, 1)
        threshold = sqrt(human_needs_density[i])
        if X >= threshold:
            continue
        priority = uniform(0, 100)
        amount = exponential(2) * sqrt(human_needs_density[i])
        # a goal need is a tuple (priority, need_id, needed_amount)
        goal_needs.append((priority, i, amount))

    goal_needs.sort()
    return goal_needs
