class Environment:
    """
        Abstract class representing an Environment
    """

    def __init__(self, number_human_agents, number_destination_agents): # Class constructor
        # Generate random agents
        self.human_agents = self.generate_human_agents(number_human_agents)
        self.destination_agents = self.generate_destination_agents(number_destination_agents)

        # The graph to represent the environment internally
        self.graph = self.generate_graph(number_human_agents, number_destinatio_agents)

        # Locate agents in environment
        self.locate(human_agents)
        self.locate(destination_agents)

        # Internal time elapsed in minutes
        self.total_time_elapsed = 0

    def execute(self, time_step=10):
        self.total_time_elapsed += time_step # Update total time elapsed

        for destination in self.destination_agents:
            destination.update(time_step)

        for human in human_agents: # Execute agents logics or make a request to them to execute an specific method
            pass

    def generate_human_agents(self, number_human_agents):
        pass

    def generate_destination_agents(self, number_destination_agents):
        pass

        

    
