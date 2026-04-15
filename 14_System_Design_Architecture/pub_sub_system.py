# pub_sub_system.py

"""
Definition: Publish-Subscribe is a messaging pattern where senders (publishers) do not send messages directly to specific receivers (subscribers), but instead categorize published messages into classes without knowledge of which subscribers there may be.
"""

class Broker:
    def __init__(self):
        self.topics = {}

    def subscribe(self, topic, subscriber):
        if topic not in self.topics: self.topics[topic] = []
        self.topics[topic].append(subscriber)

    def publish(self, topic, message):
        if topic in self.topics:
            for sub in self.topics[topic]:
                sub.receive(topic, message)

class Subscriber:
    def __init__(self, name): self.name = name
    def receive(self, topic, message):
        print(f"{self.name} received from {topic}: {message}")

# Usage
b = Broker()
s1 = Subscriber("User A")
b.subscribe("news", s1)
b.publish("news", "New Python version released!")
