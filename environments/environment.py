from utils.generator.destination_generators.destination_generator import generate_destination_agents
from utils.generator.environment_schedule_generator import generate_environment_schedule
from utils.generator.graph_generator import *
from utils.generator.human_generators.human_generator import generate_human_agents
from agents.destination_agent import *

class Environment:
    """
        Abstract class representing an Environment
    """

    def __init__(self, number_human_agents, number_destination_agents, number_of_needs, simulation_duration):  # Class constructor
        # check inputs are valid (to_do)

        # Generate random agents
        self.human_agents = generate_human_agents(
            number_human_agents, number_of_needs)
        self.destination_agents = generate_destination_agents(
            number_destination_agents, number_of_needs)

        # The graph to represent the environment internally
        # Here we generate a graph and locate generated humans and destinations on it
        self.graph = generate_graph(self.human_agents, self.destination_agents)

        print(self.graph)

        # A correlation between agents and nodes on the internal graph
        self.human_agents_locations = self.get_agents_locations(
            self.human_agents, self.graph)
        self.destination_agents_locations = self.get_agents_locations(
            self.destination_agents, self.graph)

        # The main data structure for updating the environment. This field is a priority queue with the actions that have to be executed on the environment
        # Each element has form (time_to_be_executed, human_agent_to_execute_action, other_data)
        self.schedule = generate_environment_schedule(
            self.human_agents, self.human_agents_locations, self.destination_agents_locations, self.graph)

        # Internal time elapsed in minutes
        self.total_time_elapsed = 0

        # set simulation duration in minutes
        self.simulation_duration = simulation_duration

    def run(self, time_step=10):
        while self.schedule.qsize() > 0 and self.total_time_elapsed < self.simulation_duration:
            self.execute(time_step)

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

            print("Se realizo la accion {0} por el agente humano {1} sobre el agente de destino {2} en el tiempo {3}\n\n".format(
                action, human_agent, destination_agent, time))

            if action == 'arrival':  # arrival action
                self.arrival(time, human_agent, destination_agent)

            elif action == 'negotiation':  # negotiation action
                self.negotiation(time, human_agent, destination_agent)

    def is_done(self):
        """
            Method that verifies if the simulation ended
        """
        return self.total_time_elapsed >= self.simulation_duration

    def get_agents_locations(self, agents, graph):
        """
            Given an environment graph returns a dict[agent] = node
            which represents a location in the graph for each agent
        """
        agent_location = dict()
        for node in graph.nodes:
            for elem in node.values:
                if elem in agents:
                    agent_location[elem] = node

        return agent_location

    def negotiation(self, time, human_agent, destination_agent : DestinationAgent):
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
            actual_human_agent=destination_agent.queue.get()

            # update available time for next agent
            self.schedule.put((destination_agent.next_available_time, actual_human_agent,
                               'negotiation', destination_agent))

        # once the human finishes negotiation process, tries to move to another place in case there is needs left
        destination, arrival_time = human_agent.next_destination_to_move(
            self.human_agents_locations[human_agent], self.destination_agents_locations, self.graph)
        self.schedule.put(
            (arrival_time + time, human_agent, 'arrival', destination))

    def arrival(self, time, human_agent, destination_agent):
        """
            This method simulates the human agent arrival to a destination agent.
            The human agent decides if stay at destination agent or go to another destination.
            In case human agent decides to stay, a negotiation process is added to the global schedule
            otherwise, he decides to go to other destination.
            The arrival time is also provided in case it is needed to calculate next arrival time.
        """
        human_agent.visited_destination.append(
            destination_agent)  # the agent won't get back to this destination

        if destination_agent.total_time_working >= time:  # if agent got there at working time
            destination_agent.number_current_clients += 1
            destination_agent.queue.put(human_agent)

            if destination_agent.number_current_clients == 1:
                negotiation_time = destination_agent.attention_time()  # negotiation time
                destination_agent.next_available_time = time + negotiation_time
                actual_human_agent=destination_agent.queue.get()

                # update available time for next agent
                self.schedule.put((destination_agent.next_available_time, actual_human_agent,
                                   'negotiation', destination_agent))

        else:  # in case the human agent does not want to stay in queue redifines his plan
            destination, arrival_time = human_agent.next_destination_to_move(
                self.human_agents_locations[human_agent], self.destination_agents_locations, self.graph)
            self.schedule.put(
                (arrival_time + time, human_agent, 'arrival', destination))
