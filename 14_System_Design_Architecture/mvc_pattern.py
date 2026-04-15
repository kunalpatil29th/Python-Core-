# mvc_pattern.py

"""
Definition: Model-View-Controller (MVC) is a software design pattern commonly used for developing user interfaces that divides the related program logic into three interconnected elements.
- Model: Manages data and business logic.
- View: Handles display and user interface.
- Controller: Processes input and coordinates Model and View.
"""

class Model:
    def __init__(self):
        self.data = "Hello MVC!"

class View:
    def display(self, data):
        print(f"View showing: {data}")

class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def update_view(self):
        self.view.display(self.model.data)

# Usage
m = Model()
v = View()
c = Controller(m, v)
c.update_view()
