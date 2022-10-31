class Environment:
    """Abstract class representing an Environment. 'Real' Environment classes
    inherit from this. Your Environment will typically need to implement:
        percept:           Define the percept that an agent sees.
        execute_action:    Define the effects of executing an action.
                           Also update the agent.performance slot.
    The environment keeps a list of .things and .agents (which is a subset
    of .things). Each agent has a .performance slot, initialized to 0.
    Each obj has a .location slot, even though some environments may not
    need this."""

    def __init__(self):
        self.objs = []
        self.agents = []

    def objects_classes(self):
        return []  # List of classes that can go into environment

    def percept(self, agent):
        """Return the percept that the agent sees at this point. (Implement this.)"""
        raise NotImplementedError

    def execute_action(self, agent, action):
        """Change the world to reflect this action. (Implement this.)"""
        raise NotImplementedError

    def default_location(self, obj):
        """Default location to place a new obj with unspecified location."""
        return None

    def exogenous_change(self):
        """If there is spontaneous change in the world, override this."""
        pass

    def is_done(self):
        """By default, we're done when we can't find a live agent."""
        return not any(agent.is_alive() for agent in self.agents)

    def step(self):
        """Run the environment for one time step. If the
        actions and exogenous changes are independent, this method will
        do. If there are interactions between them, you'll need to
        override this method."""
        if not self.is_done():
            actions = []
            for agent in self.agents:
                if agent.alive:
                    actions.append(agent.program(self.percept(agent)))
                else:
                    actions.append("")
            for (agent, action) in zip(self.agents, actions):
                self.execute_action(agent, action)
            self.exogenous_change()

    def run(self, steps=1000):
        """Run the Environment for given number of time steps."""
        for step in range(steps):
            if self.is_done():
                return
            self.step()

    def add_object(self, obj, location=None):
        """Add an element to the environment, setting its location. For
        convenience, if obj is an agent program we make a new agent
        for it. (Shouldn't need to override this.)"""
        if not isinstance(obj, Object):
            obj = Agent(obj)
        if obj in self.objs:
            print("Can't add the same obj twice")
        else:
            obj.location = location if location is not None else self.default_location(obj)
            self.objs.append(obj)
            if isinstance(obj, Agent):
                obj.performance = 0
                self.agents.append(obj)

    def delete_object(self, obj):
        """Remove an element from the environment."""
        try:
            self.objs.remove(obj)
        except ValueError as e:
            print(e)
            print("  in Environment delete_object")
            print("  Thing to be removed: {} at {}".format(obj, obj.location))
            print("  from list: {}".format([(obj, obj.location) for obj in self.things]))
        if obj in self.agents:
            self.agents.remove(obj)
