from http import client
from agents.agent import Agent
from utils.probabilities.random_variables import poisson

class DestinationAgent(Agent):
    """
        A class to denote a destination agent
    """

    def __init__(self): # class constructor
        super().__init__()
        self.needs = [(1, 1000), (2, 1000)] # The needs this can satisfy. (need_id, need_available_amout)
        self.clients = [] # Group of human agents that arrives to the destination agent
        self.attention_time = 3 # Attention time for a given client is Poisson-distributed
        self.total_time_working_in_minutes = 240 # Total time the agent works
        self.elapsed_time_working = 0 # Start time

    def add_clients(self, clients, arrival_time): # Add clients (human agent) that arrives at a certain time
        if arrival_time < self.total_time_working_in_hours: 
            self.clients.extend([(client, arrival_time) for client in clients])

    def update(self, elapsed_time): # Update internal state given an elapsed time and return a client that comes out at a given time       
        satisfied_clients = []

        if elapsed_time < self.elapsed_time_working or elapsed_time > self.total_time_working_in_minutes: # Invalid update time
            return satisfied_clients

        # Update internal time elapsed
        self.elapsed_time_working += elapsed_time

        next_time = self.clients[0][1]

        # Try to satisfy all possible clients
        while len(self.clients) > 0:
            next_time += self.attention_time
            if next_time <= elapsed_time:
                client = self.clients.pop()[0]
                client.on_queue = False

                # Update needs for client and server. This is the negotiation part
                for i in range(len(client.needs)):
                    need_id = client.needs[i][0]
                    need_necessary_amount = client.needs[i][1]

                    for j in lself.needs:
                        dest_need_id = client.needs[j][0]
                        dest_need_amount = client.needs[j][1]
                    
                        if need_id == dest_need_id: # make exchange
                            # update need in human

                            # update need in destination 



                satisfied_clients.append((client, next_time)) # Add client to satisfy clients and departure time
            else: # if time is not enough to update queue, then do nothing
                break

        return satisfied_clients
            

