from testing.human_agents_generator_test import *
from testing.destination_agents_generator_test import *

if __name__ == "__main__":
    run_human_agents_generator_test(6)
    run_multi_human_agents_generator_test(10,6)
    run_destination_agents_generator_test(5, 6)
