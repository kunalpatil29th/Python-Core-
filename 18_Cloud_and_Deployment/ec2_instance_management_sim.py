# ec2_instance_management_sim.py

"""
Definition: Amazon Elastic Compute Cloud (Amazon EC2) is a web service that provides secure, resizable compute capacity in the cloud. It is designed to make web-scale cloud computing easier for developers.
"""

class EC2Manager:
    def start_instance(self, instance_id):
        print(f"Starting EC2 instance: {instance_id}")

    def stop_instance(self, instance_id):
        print(f"Stopping EC2 instance: {instance_id}")

# Simulation
manager = EC2Manager()
manager.start_instance("i-0abcdef1234567890")
manager.stop_instance("i-0abcdef1234567890")
