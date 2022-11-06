from random import randrange


def generate_destination_offerts(number_of_needs):
    """
        Generate destination offerts.
        This takes a number of needs and gets random needs to satisfy
        in a random amount
    """
    number_of_offerts = randrange(1, number_of_needs + 1) # number of offerts this agent wil supply
    offert_indexes = [i for i in range(number_of_needs)]
    offerts = []
    
    # select random needs to make offerts
    for i in range(number_of_offerts):
        rand_index = randrange(0, len(offert_indexes))
        offerts.append((rand_index, 1000, 10)) # an offert is a tuple (need_id, amount, price)
        offert_indexes.remove(rand_index)

    return offerts
