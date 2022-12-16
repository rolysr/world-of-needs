from random import randrange, uniform

from utils.generator.natural_language_generation.markov_chain_human_name_generator import generate_human_names

if __name__ == "__main__":
    print(generate_human_names(10, 3, 14))