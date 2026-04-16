# kubernetes_basics_sim.py

"""
Definition: Kubernetes (K8s) is an open-source system for automating deployment, scaling, and management of containerized applications.
"""

class K8sCluster:
    def deploy_pod(self, name):
        print(f"Deploying Pod: {name}")
        print("Status: Pending -> Running")

    def scale_deployment(self, replicas):
        print(f"Scaling deployment to {replicas} replicas...")

# Simulation
cluster = K8sCluster()
cluster.deploy_pod("python-app-pod")
cluster.scale_deployment(3)
