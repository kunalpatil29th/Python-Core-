# api_gateway_sim.py

"""
Definition: Amazon API Gateway is a fully managed service that makes it easy for developers to create, publish, maintain, monitor, and secure APIs at any scale.
"""

class APIGateway:
    def __init__(self):
        self.routes = {}

    def add_route(self, path, func):
        self.routes[path] = func

    def handle_request(self, path):
        if path in self.routes:
            return self.routes[path]()
        return "404 Not Found"

# Simulation
gateway = APIGateway()
gateway.add_route("/hello", lambda: "Welcome to our API!")
print(gateway.handle_request("/hello"))
