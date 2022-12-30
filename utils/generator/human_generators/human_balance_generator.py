from numpy.random import *


def generate_human_balance(income):
    """
        A method for generating human balance in currency units    
    """
    return income*(uniform(0.8, 1.2))
