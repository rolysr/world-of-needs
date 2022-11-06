from random import randrange


def generate_destination_attention_time():
    """
        A method for generating attention time of a destination.
        This time is given in minutes and could receive a hour of the day
    """
    return randrange(5, 13)