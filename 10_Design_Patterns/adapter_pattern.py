# adapter_pattern.py

"""
Definition: The Adapter Pattern allows incompatible interfaces to work together by wrapping an existing class with a new interface.
"""

class OldSystem:
    def old_method(self):
        return "Data from old system"

class NewInterface:
    def request(self):
        pass

class Adapter(NewInterface):
    def __init__(self, old_system):
        self._old_system = old_system

    def request(self):
        return f"Adapted: {self._old_system.old_method()}"

# Usage
old = OldSystem()
adapter = Adapter(old)
print(adapter.request())
