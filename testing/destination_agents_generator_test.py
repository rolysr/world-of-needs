from agents.destination_agent import DestinationAgent
from utils.generator.destination_generators.destination_generator import generate_destination_agents

def run_destination_agents_generator_test(number_of_needs):
    """
        Destination agents generator test
        Arguments:
        number_of_needs {int} -- The number of possible needs
    """

    # create an instance of a destination agent
    agent = DestinationAgent(number_of_needs)

    print(agent)

