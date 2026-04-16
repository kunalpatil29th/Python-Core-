# cloud_watch_logging_sim.py

"""
Definition: Amazon CloudWatch is a monitoring and observability service that provides data and actionable insights to monitor applications, respond to system-wide performance changes, and optimize resource utilization.
"""

def log_to_cloudwatch(log_group, message):
    print(f"[CloudWatch] {log_group}: {message}")

# Simulation
log_to_cloudwatch("/aws/lambda/my-func", "Function execution started.")
log_to_cloudwatch("/aws/lambda/my-func", "ERROR: Database connection timeout.")
