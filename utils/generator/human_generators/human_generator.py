from agents.human_agent import HumanAgent


def generate_human_agents(names, number_human_agents, number_of_needs, gini_coef, mean_income, human_needs_density):
    """
        A method for generating human agents
    """
    return [HumanAgent(name, number_of_needs, gini_coef, mean_income, human_needs_density) for name in names]