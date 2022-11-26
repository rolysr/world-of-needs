from utils.generator.destination_generators.destination_generator import generate_destination_agents
from utils.generator.environment_schedule_generator import generate_environment_schedule
from utils.generator.graph_generator import *
from utils.generator.human_generators.human_generator import generate_human_agents
from agents.destination_agent import *


class Environment:
    """
        Abstract class representing an Environment
    """

    def __init__(self, number_human_agents, number_destination_agents, number_of_needs,
                 simulation_duration, gini_coef, mean_income, human_needs_density, offers_average_price,
                 store_offers_density, stores_total_budget):  # Class constructor
        # check inputs are valid (to_do)

        # get number of human and destination agents
        self.number_human_agents = number_human_agents
        self.number_destination_agents = number_destination_agents

        # Generate random agents
        self.human_agents = generate_human_agents(
            number_human_agents, number_of_needs, gini_coef, mean_income, human_needs_density)
        self.destination_agents = generate_destination_agents(
            number_destination_agents, number_of_needs, store_offers_density,
            offers_average_price, stores_total_budget)

        # set number of needs
        self.number_of_needs = number_of_needs

        # The graph to represent the environment internally
        # Here we generate a graph and locate generated humans and destinations on it
        self.graph, self.human_agents_locations, self.destination_agents_locations = generate_graph(
            self.human_agents, self.destination_agents)

        # print(self.graph)

        # The main data structure for updating the environment. This field is a priority queue with the actions that have to be executed on the environment
        # Each element has form (time_to_be_executed, human_agent_to_execute_action, other_data)
        self.schedule = generate_environment_schedule(
            self.human_agents, self.human_agents_locations, self.destination_agents_locations, self.graph, self.number_of_needs)

        # Internal time elapsed in minutes
        self.total_time_elapsed = 0

        # set simulation duration in minutes
        self.simulation_duration = simulation_duration

        # list of human dissatisfaction at the of the simulation
        self.dsat_list = dict()

        # Log record in form of tuples (time, narration)
        self.log_record = list()
        # To shorten human and destination agents Ids
        self.human_agents_id_map = dict()
        for i in range(number_human_agents):
            self.human_agents_id_map[self.human_agents[i]] = i
        self.destination_agents_id_map = dict()
        for i in range(number_destination_agents):
            self.destination_agents_id_map[self.destination_agents[i]] = i

    def run(self, time_step=10):
        while self.schedule.qsize() > 0 and self.total_time_elapsed < self.simulation_duration:
            self.execute(time_step)
        for human_agent in self.human_agents:
            if not (human_agent in self.dsat_list.keys()):
                self.dsat_list[human_agent] = human_agent.dissatisfaction(
                    self.total_time_elapsed)

    def execute(self, time_step=10):
        """
            Makes an execution of the environment for a given time step.
            As results, the environment internal state is updated
        """
        if time_step <= 0:  # if time step is non-positive then do nothing
            return

        # update internal total time elapsed
        self.total_time_elapsed += time_step

        # while there is some event to execute that is contained on the internal time elapsed then execute it
        while self.schedule.qsize() > 0 and self.schedule.queue[0][0] < self.total_time_elapsed:
            time, human_agent, action, destination_agent = self.schedule.get()

            # print("Action {0} completed by human agent {1} over destination agent {2} at minutes elapsed {3}\n\n".format(
            #     action, human_agent, destination_agent, time))
            if action == 'arrival':
                self.log_record.append((time, "{3}: The human agent {1} arrived at destination agent {2}.".format(
                    action, self.human_agents_id_map[human_agent], self.destination_agents_id_map[destination_agent], time)))
            elif action == 'negotiation':
                self.log_record.append((time, "{3}: The human agent {1} starts a negotiation with destination agent {2}.".format(
                    action, self.human_agents_id_map[human_agent], self.destination_agents_id_map[destination_agent], time)))

            if action == 'arrival':  # arrival action
                self.arrival(time, human_agent, destination_agent)

            elif action == 'negotiation':  # negotiation action
                self.negotiation(time, human_agent, destination_agent)

    def is_done(self):
        """
            Method that verifies if the simulation ended
        """
        return self.total_time_elapsed >= self.simulation_duration

    def negotiation(self, time, human_agent, destination_agent: DestinationAgent):
        """
            Simulates the process of negotiation between human agent and destination agent.
            The human agent receives the destinations offers and decides to buy or not
            according to his internal needs.
            The destination agent receives human agent offer request and updates internal state
            If destination agent can satisfy human agent's needs, then human agent's internal state
            is updated. Negotiation time is also provided
        """
        offers = destination_agent.offers  # destination agent's offers

        # the agent receives the offers and try to make a valid request of needs
        request = human_agent.offers_requests(offers)

        # the human agent request is processed by the destination agent
        destination_agent.process_offers_requests(request)

        destination_agent.number_current_clients -= 1
        if destination_agent.number_current_clients > 0:
            negotiation_time = destination_agent.attention_time()  # negotiation time
            destination_agent.next_available_time = time + negotiation_time
            actual_human_agent = destination_agent.queue.get()

            # update available time for next agent
            self.schedule.put((destination_agent.next_available_time, actual_human_agent,
                               'negotiation', destination_agent))

        # once the human finishes negotiation process, tries to move to another place in case there is needs left
        if len(human_agent.needs) > 0 and len(human_agent.visited_destinations) != self.number_destination_agents:
            destination, arrival_time = human_agent.next_destination_to_move(
                self.human_agents_locations[human_agent], self.destination_agents_locations, self.graph, self.number_of_needs)
            self.schedule.put(
                (arrival_time + time, human_agent, 'arrival', destination))
        else:
            self.dsat_list[human_agent] = human_agent.dissatisfaction(
                self.total_time_elapsed)

    def arrival(self, time, human_agent, destination_agent):
        """
            This method simulates the human agent arrival to a destination agent.
            The human agent decides if stay at destination agent or go to another destination.
            In case human agent decides to stay, a negotiation process is added to the global schedule
            otherwise, he decides to go to other destination.
            The arrival time is also provided in case it is needed to calculate next arrival time.
        """
        human_agent.visited_destinations.append(
            destination_agent)  # the agent won't get back to this destination

        # update current human agent's position
        self.human_agents_locations[human_agent] = self.destination_agents_locations[destination_agent]

        if destination_agent.total_time_working >= time:  # if agent got there at working time
            destination_agent.number_current_clients += 1
            destination_agent.queue.put(human_agent)

            if destination_agent.number_current_clients == 1:
                negotiation_time = destination_agent.attention_time()  # negotiation time
                destination_agent.next_available_time = time + negotiation_time
                actual_human_agent = destination_agent.queue.get()

                # update available time for next agent
                self.schedule.put((destination_agent.next_available_time, actual_human_agent,
                                   'negotiation', destination_agent))

        # in case the human agent does not want to stay in queue and assuming there is more places to visit, then redifines his plan
        elif len(human_agent.needs) > 0 and len(human_agent.visited_destinations) != self.number_destination_agents:
            destination, arrival_time = human_agent.next_destination_to_move(
                self.human_agents_locations[human_agent], self.destination_agents_locations, self.graph, self.number_of_needs)
            self.schedule.put(
                (arrival_time + time, human_agent, 'arrival', destination))
        else:
            self.dsat_list[human_agent] = human_agent.dissatisfaction(
                self.total_time_elapsed)

    def reset(self, reset_human_agents_flag=True, reset_destination_agents_flag=True):
        """
            Reset function for the environment. This function should be called just before
            running again the environment.
        """
        if reset_human_agents_flag:
            for human_agent in self.human_agents:
                human_agent.reset()
        if reset_destination_agents_flag:
            for destination_agent in self.destination_agents:
                destination_agent.reset()

        self.schedule = generate_environment_schedule(
            self.human_agents, self.human_agents_locations, self.destination_agents_locations, self.graph, self.number_of_needs)
        self.total_time_elapsed = 0
        self.dsat_list = dict()

    def narrate(self, initial_time=0, end_time=None):
        """
            Prints the actions done by the agents in the given time inteval.
            - initial_time is 0 by defualt
            - end_time is the ending time of the simulation by default
        """
        if end_time == None:
            end_time = self.simulation_duration
        for tuple in self.log_record:
            time = tuple[0]
            if initial_time <= time and time <= end_time:
                print(tuple[1])
