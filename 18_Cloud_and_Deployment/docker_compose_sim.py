# docker_compose_sim.py

"""
Definition: Docker Compose is a tool for defining and running multi-container Docker applications. With Compose, you use a YAML file to configure your application’s services.
"""

def simulate_docker_compose():
    yaml_config = """
    services:
      web:
        build: .
        ports:
          - "8000:8000"
      db:
        image: postgres
    """
    print("Parsing docker-compose.yml...")
    print("Starting database service...")
    print("Starting web application...")
    print("Multi-container app is UP.")

simulate_docker_compose()
