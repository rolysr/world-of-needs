from uuid import uuid1
from math import inf


class Agent:
    """
        A class to denote a generic agent
    """

    def __init__(self):
        self.id = uuid1()  # Unique identifier
        # Log record in form of tuples (time, narration)
        self.log_record = list()
        self.name = str()

    def __eq__(self, other) -> bool:
        return self.id == other.id

    def __hash__(self) -> int:
        return self.id.int

    def __lt__(self, other) -> bool:
        return self.id < other.id

    def narrate(self, initial_time=0, end_time=None):
        """
            Prints the actions done by the agent in the given time inteval.
            - initial_time is 0 by defualt
            - end_time is inf by default
        """
        if end_time == None:
            end_time = inf
        for tuple in self.log_record:
            time = tuple[0]
            if initial_time <= time and time <= end_time:
                print(tuple[1])
