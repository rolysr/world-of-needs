from agents.human_agent import HumanAgent


def generate_human_agents(number_human_agents, number_of_needs):
    """
        A method for generating human agents
    """
    return [HumanAgent(number_of_needs) for i in range(number_human_agents)]