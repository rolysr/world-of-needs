from queue import PriorityQueue
from utils.generator.destination_generators.destination_offerts_generator import generate_destination_offerts
from utils.generator.environment_schedule_generator import generate_environment_schedule
from utils.generator.graph_generator import *
from utils.generator.human_generators.human_generator import generate_human_agents

class Environment:
    """
        Abstract class representing an Environment
    """

    def __init__(self, number_human_agents, number_destination_agents): # Class constructor
        # Generate random agents
        self.human_agents = generate_human_agents(number_human_agents)
        self.destination_agents = generate_destination_offerts(number_destination_agents)

        # The graph to represent the environment internally
        # Here we generate a graph and locate generated humans and destinations on it
        self.graph = generate_graph(self.human_agents, self.destination_agents)

        # The main data structure for updating the environment. This field is a priority queue with the actions that have to be executed on the environment
        self.schedule = generate_environment_schedule(self.human_agents)

        # Internal time elapsed in minutes
        self.total_time_elapsed = 0

    def execute(self, time_step=10):
        pass

    
