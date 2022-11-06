from random import randrange


def generate_destination_working_time():
    """
        Method for generating destination working time.
        This method returns the minutes of the day a destination will work
    """
    # select a random working time from some options
    working_times = [4, 8, 10, 12, 16, 24]
    rand_index = randrange(0, len(working_times))
    return working_times[rand_index]*60