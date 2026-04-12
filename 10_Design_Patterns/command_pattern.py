# command_pattern.py

"""
Definition: The Command Pattern encapsulates a request as an object, thereby letting you parameterize clients with different requests.
"""

class Light:
    def turn_on(self):
        print("Light is ON")
    def turn_off(self):
        print("Light is OFF")

class Command:
    def execute(self):
        pass

class LightOnCommand(Command):
    def __init__(self, light):
        self._light = light
    def execute(self):
        self._light.turn_on()

# Usage
lamp = Light()
on_command = LightOnCommand(lamp)
on_command.execute()
