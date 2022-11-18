from queue import PriorityQueue
from random import randrange


def generate_human_needs(number_of_needs):
    """
        A method for generating human needs
    """
    number_of_goal_needs = randrange(1, number_of_needs + 1) # number of needs the agent needs to satisfy
    goal_need_indexes = [i for i in range(number_of_needs)]
    goal_needs = []
    
    # select random needs
    for i in range(number_of_goal_needs):
        rand_need_id = goal_need_indexes[randrange(0, len(goal_need_indexes))]
        goal_needs.append((rand_need_id, rand_need_id, 5)) # a goal need is a tuple (priority, need_id, needed_amount)
        goal_need_indexes.remove(rand_need_id)

    goal_needs.sort()
    return goal_needs