from random import randrange, uniform
import matplotlib.pyplot as plt

from utils.generator.natural_language_generation.markov_chain_human_name_generator import generate_human_names

if __name__ == "__main__":
    x = [i for i in range(10)]
    m = [1984.22, 1292.63, 1446.48, 1588.34, 1380.58, 1197.93, 1433.65, 1649.65, 1718.68, 1582.93]
    v = [713314.71, 455182.01, 322118.32, 482368.46, 203355.54, 417952.90, 474612.26, 263961.53, 463554.19, 353222.42]
    plt.plot(x, v)
    plt.show()
