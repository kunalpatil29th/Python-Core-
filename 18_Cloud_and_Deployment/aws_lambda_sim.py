# aws_lambda_sim.py

"""
Definition: AWS Lambda is a serverless, event-driven compute service that lets you run code for virtually any type of application or backend service without provisioning or managing servers.
"""

def lambda_handler(event, context):
    print(f"Received event: {event}")
    return {
        'statusCode': 200,
        'body': 'Hello from AWS Lambda!'
    }

# Simulation
mock_event = {"key": "value"}
print(lambda_handler(mock_event, None))
