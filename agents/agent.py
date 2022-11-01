from uuid import uuid1

class Agent:
    """
        A class to denote a generic agent
    """

    def __init__(self):
        self.id = uuid1() # Unique identifier
        