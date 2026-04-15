# docker_basics_sim.py

"""
Definition: Docker is a platform for developing, shipping, and running applications in containers.
Simulation: This module simulates building and running a Docker container.
"""

def simulate_docker():
    print("Reading Dockerfile...")
    print("Building image: python-core-app:latest")
    print("Layer 1: FROM python:3.12-slim")
    print("Layer 2: COPY . /app")
    print("Layer 3: RUN pip install -r requirements.txt")
    print("Image built successfully.")
    
    print("\nStarting container...")
    print("Container ID: 7a8b9c0d1e2f")
    print("App running at http://localhost:8000")

simulate_docker()
