# load_balancer_sim.py

"""
Definition: A Load Balancer acts as a "traffic cop" sitting in front of your servers and routing client requests across all servers capable of fulfilling those requests in a manner that maximizes speed and capacity utilization.
"""

class LoadBalancer:
    def __init__(self, servers):
        self.servers = servers
        self.index = 0

    def get_server(self):
        # Round Robin Algorithm
        server = self.servers[self.index]
        self.index = (self.index + 1) % len(self.servers)
        return server

# Usage
lb = LoadBalancer(["Server_1", "Server_2", "Server_3"])
for i in range(5):
    print(f"Request {i+1} routed to: {lb.get_server()}")
