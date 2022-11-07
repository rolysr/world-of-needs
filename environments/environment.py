from utils.generator.destination_generators.destination_generator import generate_destination_agents
from utils.generator.environment_schedule_generator import generate_environment_schedule
from utils.generator.graph_generator import *
from utils.generator.human_generators.human_generator import generate_human_agents

class Environment:
    """
        Abstract class representing an Environment
    """

    def __init__(self, number_human_agents, number_destination_agents, number_of_needs): # Class constructor
        # Generate random agents
        self.human_agents = generate_human_agents(number_human_agents, number_of_needs)
        self.destination_agents = generate_destination_agents(number_destination_agents, number_of_needs)

        # The graph to represent the environment internally
        # Here we generate a graph and locate generated humans and destinations on it
        self.graph = generate_graph(self.human_agents, self.destination_agents)

        # A correlation between agents and nodes on the internal graph
        self.human_agents_location = self.get_agents_location(self.human_agents, self.graph)
        self.destination_agents_location = self.get_agents_location(self.destination_agents, self.graph)

        # The main data structure for updating the environment. This field is a priority queue with the actions that have to be executed on the environment
        # Each element has form (time_to_be_executed, human_agent_to_execute_action, other_data)
        self.schedule = generate_environment_schedule(self.human_agents)

        # Internal time elapsed in minutes
        self.total_time_elapsed = 0

    def execute(self, time_step=10):
        """
            Makes an execution of the environment for a given time step.
            As results, the environment internal state is updated
        """
        pass

    def get_agents_location(self, agents, graph):
        """
            Given an environment graph returns a dict[agent] = node
            which represents a location in the graph for each agent
        """
        agent_location = dict()
        for node in graph.nodes:
            for elem in node.values:
                if elem in agents:
                    agent_location[elem] = node

        return agent_location

    def negotiate(self, human_agent, destination_agent):
        """
            Negotiation logic between a human agent and a destination agent.
            This method will be executed when the human agent is the current
            person to negotiate with the destination
        """
        pass

    def make_decision(self, human_agent, destination_agent):
        """
            When an agent arrives to a destination he decides if 
            it is better to satisfy his need or to continue his planned journey
        """
        pass

    def best_destination_to_go(self, human_agent):
        """
            In this method, agent decides the best place to go in order to 
            satisfy his needs right now
        """

    
