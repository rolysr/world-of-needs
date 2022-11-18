from queue import PriorityQueue


def generate_environment_schedule(human_agents, human_agents_locations, destination_agents_locations, graph):
    """
        Method for generate an environment schedule given a list of previously
        generated human agents. This method returns a priority queue with actions to execute
        Action: (time_to_be_executed, executor_agent, action, goal_agent)

        The are two types of actions at the moment:
        (<time>, <human_agent>, 'arrival', <destination_agent>) : In this action an agent decide if is good to spend time or resources at destination
        (<time>, <human_agent>, 'negotiation', <destination_agent>): Execution of negotiation process
    """
    schedule = PriorityQueue() # The output priority queue
    for human_agent in human_agents:
        destination, arrival_time = human_agent.next_destination_to_move(human_agents_locations[human_agent], destination_agents_locations, graph)
        schedule.put((arrival_time, human_agent, 'arrival', destination))
    return schedule