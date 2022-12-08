from utils.generator.human_generators.human_income_generator import generate_human_income

def run_income_generator_test():
    print("Gini: 0.0, income: 1000")
    for i in range(20):
        print(generate_human_income(0.0, 1000))
        # print("")
    print("Gini: 0.5, income: 1000")
    for i in range(20):
        print(generate_human_income(0.5, 1000))
        # print("")
    print("Gini: 0.9, income: 1000")
    for i in range(100):
        print(generate_human_income(0.9, 1000))
        # print("")