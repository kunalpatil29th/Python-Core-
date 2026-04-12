# observer_pattern.py

"""
Definition: The Observer Pattern defines a one-to-many dependency between objects so that when one object changes state, all its dependents are notified.
"""

class Subject:
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        self._observers.append(observer)

    def notify(self, message):
        for observer in self._observers:
            observer.update(message)

class Observer:
    def update(self, message):
        pass

class EmailAlert(Observer):
    def update(self, message):
        print(f"Email Alert: {message}")

# Usage
sub = Subject()
sub.attach(EmailAlert())
sub.notify("System Shutdown in 5 minutes!")
