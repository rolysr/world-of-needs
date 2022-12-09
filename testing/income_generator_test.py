from utils.generator.human_generators.human_income_generator import generate_human_income

def run_income_generator_test():
    gini_coefs=[0.0, 0.5, 0.6]
    mean_income=[300, 300, 300]
    for i in range(len(gini_coefs)):
        print("Gini: {}, mean income: {}".format(gini_coefs[i],mean_income[i]))
        sum = 0
        for j in range(10000):
            sum+=generate_human_income(gini_coefs[i], mean_income[i])
        sum/=10000
        print(sum)
    