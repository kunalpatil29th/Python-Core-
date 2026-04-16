# cloud_security_groups_sim.py

"""
Definition: A security group acts as a virtual firewall for your EC2 instances to control incoming and outgoing traffic.
"""

class SecurityGroup:
    def __init__(self, name):
        self.name = name
        self.rules = []

    def allow_port(self, port, protocol="tcp"):
        self.rules.append({"port": port, "protocol": protocol})
        print(f"Security Group '{self.name}': Allowing {protocol}/{port}")

# Simulation
sg = SecurityGroup("web-server-sg")
sg.allow_port(80)
sg.allow_port(443)
