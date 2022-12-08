from numpy.random import *

# up to add to settings file
HUMAN_INCOME_PERCENTILE_GENERATOR_PARAMETER_K = 0.5


def generate_human_income(gini_coef: float, mean_income):
    """
        A method for generating the income percentile. 
        This is given in some parameter that means: 
        0 - poorest people 
        1 - richest people
        This generator uses the following articule's work:
        https://www.nature.com/articles/s41599-021-00948-x#:~:text=This%20Lorenz%20curve%20is%20estimated,countries%20and%2For%20international%20organizations.&text=Note%20that%20no%20complicated%20error,to%20estimate%20the%20Lorenz%20curve.
        Specifically:
        y(x)=(1-k)*x^p+k*(1-(1-x)^(1/p))
        which implies:
        y'(x)=p*(1-k)*x^(p-1)+k*(1-(-1/p*(1-x)^((1-p)/p)))

        y'(x) is the derivative of the cumulative income function, the "income" of the person in the x normalized income rank
        p is a parameter directly related to gini coefficient, p>=1
        k is a parameter for weighting the aproaches described in the paper, 0<=k<=1
    """
    x = uniform(0.0, 1.0)
    # print(x)
    k = HUMAN_INCOME_PERCENTILE_GENERATOR_PARAMETER_K
    p = (1.0+gini_coef)/(1.0-gini_coef)
    # print(k)
    # print(gini_coef)
    # print("p vale {} {} {}".format(p, (1.0+gini_coef),(1.0-gini_coef)))
    y = (1.0 - k) * pow(x, p) + k * (1.0 - pow(1.0 - x, 1.0 / p))
    # print("y vale {}".format(y))
    # print("pow1 vale {}".format(pow(x, p)))
    # print("pow2 vale {}".format(pow(1.0 - x, 1.0 / p)))
    y = p * (1 - k) * (x ** (p - 1)) + k * \
        (1 - (- (1 / p) * ((1 - x) ** ((1 - p) / p))))
    return y*mean_income
