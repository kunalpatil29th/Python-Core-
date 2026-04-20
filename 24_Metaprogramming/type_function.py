# type_function.py

"""
Definition: In Python, 'type()' is more than just a function to check an object's type. 
When called with three arguments—'type(name, bases, dict)'—it acts as a dynamic constructor 
for creating new classes on the fly. This is a core concept in metaprogramming, 
where code can generate or modify other code (in this case, classes).
"""

def dynamic_class_creation():
    """Demonstrates creating a class dynamically using type()."""
    
    # Standard class definition
    class StandardPerson:
        def __init__(self, name):
            self.name = name
        def greet(self):
            return f"Hello, my name is {self.name}."

    print("--- Standard Class Creation ---")
    p1 = StandardPerson("Alice")
    print(f"Object: {p1}, Type: {type(p1)}")
    print(p1.greet())

    # Dynamic class creation using type()
    # type(name, bases, attributes_dict)
    def dynamic_greet(self):
        return f"Hi there! I am {self.name}, created dynamically."

    DynamicPerson = type(
        'DynamicPerson', # class name
        (object,),       # base classes (tuple)
        {                # attributes and methods
            '__init__': lambda self, name: setattr(self, 'name', name),
            'greet': dynamic_greet,
            'species': 'Human'
        }
    )

    print("\n--- Dynamic Class Creation with type() ---")
    p2 = DynamicPerson("Bob")
    print(f"Object: {p2}, Type: {type(p2)}")
    print(f"Class Name: {p2.__class__.__name__}")
    print(p2.greet())
    print(f"Species: {p2.species}")

if __name__ == "__main__":
    dynamic_class_creation()
