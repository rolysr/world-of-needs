class Environment:
    """Abstract class representing an Environment. 'Real' Environment classes
    inherit from this. Your Environment will typically need to implement:
        percept:           Define the percept that an agent sees.
        execute_action:    Define the effects of executing an action.
                           Also update the agent.performance slot.
    The environment keeps a list of .things and .agents (which is a subset
    of .things). Each agent has a .performance slot, initialized to 0.
    Each elem has a .location slot, even though some environments may not
    need this."""

    def __init__(self):
        self.agents = []

    def objects_classes(self):
        return []  # List of classes that can go into environment

    def percept(self, agent):
        """Return the percept that the agent sees at this point. (Implement this.)"""
        raise NotImplementedError

    def execute_action(self, agent, action):
        """Change the world to reflect this action. (Implement this.)"""
        raise NotImplementedError

    def default_location(self, elem):
        """Default location to place a new elem with unspecified location."""
        raise NotImplementedError

    def exogenous_change(self):
        """If there is spontaneous change in the world, override this."""
        raise NotImplementedError

    def is_done(self):
        """By default, we're done when we can't find a live agent."""
        raise NotImplementedError

    def step(self):
        """Run the environment for one time step. If the
        actions and exogenous changes are independent, this method will
        do. If there are interactions between them, you'll need to
        override this method."""
        raise NotImplementedError

    def run(self, steps=1000):
        """Run the Environment for given number of time steps."""
        raise NotImplementedError

    def add_object(self, elem, location=None):
        """Add an element to the environment, setting its location. For
        convenience, if elem is an agent program we make a new agent
        for it. (Shouldn't need to override this.)"""
        raise NotImplementedError

    def delete_object(self, elem):
        """Remove an element from the environment."""
        raise NotImplementedError
