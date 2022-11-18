from uuid import uuid1

class Agent:
    """
        A class to denote a generic agent
    """

    def __init__(self):
        self.id = uuid1() # Unique identifier
        
    def __eq__(self, other) -> bool:
        return self.id == other.id
    
    def __hash__(self) -> int:
        return self.id.int
    
    def __lt__(self, other) -> bool:
        return self.id<other.id