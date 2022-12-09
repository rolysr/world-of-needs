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
        threshold = human_needs_density[i]/(human_needs_density[i]+1)
        if X >= threshold:
            continue
        priority = uniform(0, 100)
        amount = 0
        for i in range(10):
            amount += exponential(human_needs_density[i]+1)
        amount /= 10
        # a goal need is a tuple (priority, need_id, needed_amount)
        goal_needs.append((priority, i, amount))

    goal_needs.sort()
    goal_needs.reverse()
    return goal_needs
