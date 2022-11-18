from testing.human_agents_generator_test import *
from testing.destination_agents_generator_test import *
from testing.graph_generator_test import *
from utils.generator.human_generators.human_generator import generate_human_agents
from utils.generator.destination_generators.destination_generator import generate_destination_agents

if __name__ == "__main__":
    # run_human_agents_generator_test(6)
    # run_multi_human_agents_generator_test(10,6)
    # run_destination_agents_generator_test(5, 6)
    human_agents = generate_human_agents(10, 6)
    destination_agents = generate_destination_agents(4, 6)
    graph_generator_test(human_agents, destination_agents)
