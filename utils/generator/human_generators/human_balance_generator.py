from numpy.random import *


def generate_human_balance(income):
    """
        A method for generating human balance in currency units    
    """
    return income*(0.8+uniform(0.0, 0.4))
