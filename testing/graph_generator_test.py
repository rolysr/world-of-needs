from utils.generator.graph_generator import *

def graph_generator_test(human_agents, destination_agents):
    graph = generate_graph(human_agents, destination_agents)

    print(graph)
