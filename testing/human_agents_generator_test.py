from agents.human_agent import HumanAgent
from utils.generator.human_generators.human_generator import generate_human_agents

def run_human_agents_generator_test(number_of_needs):
    """
        Destination agents generator test
        Arguments:
        number_of_needs {int} -- The number of possible needs
    """

    # create an instance of a destination agent
    agent = HumanAgent(number_of_needs)

    print(agent)


def run_multi_human_agents_generator_test(number_of_agents, number_of_needs):
    """
        Destination agents generator test
        Arguments:
        number_of_needs {int} -- The number of possible needs
    """

    # create an instance of a destination agent
    agents = generate_human_agents(number_of_agents, number_of_needs)

    for agent in agents:
        print(agent)
