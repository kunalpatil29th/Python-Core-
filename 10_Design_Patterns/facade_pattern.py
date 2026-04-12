# facade_pattern.py

"""
Definition: The Facade Pattern provides a simplified interface to a complex system of classes, library, or framework.
"""

class SubsystemA:
    def operation_a(self): print("Subsystem A active.")

class SubsystemB:
    def operation_b(self): print("Subsystem B active.")

class Facade:
    def __init__(self):
        self._a = SubsystemA()
        self._b = SubsystemB()

    def start(self):
        self._a.operation_a()
        self._b.operation_b()

# Usage
facade = Facade()
facade.start()
