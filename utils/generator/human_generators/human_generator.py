from agents.human_agent import HumanAgent


def generate_human_agents(number_human_agents, number_of_needs, gini_coef, mean_income):
    """
        A method for generating human agents
    """
    return [HumanAgent(number_of_needs, gini_coef, mean_income) for i in range(number_human_agents)]