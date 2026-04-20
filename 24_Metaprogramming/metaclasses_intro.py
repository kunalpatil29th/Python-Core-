# metaclasses_intro.py

"""
Definition: A metaclass is a class whose instances are classes. 
Just as an object is an instance of a class, a class is an instance of a metaclass. 
In Python, 'type' is the default metaclass. By creating custom metaclasses, 
we can intercept class creation to enforce rules, automatically add attributes, 
or modify class behavior before it is fully initialized.
"""

# Custom Metaclass
class UppercaseAttributesMetaclass(type):
    """Metaclass that automatically converts all class attribute names to uppercase."""
    def __new__(mcs, name, bases, attrs):
        # Intercept class attributes and capitalize names
        uppercase_attrs = {}
        for attr_name, attr_val in attrs.items():
            if not attr_name.startswith('__'): # Ignore magic methods
                uppercase_attrs[attr_name.upper()] = attr_val
            else:
                uppercase_attrs[attr_name] = attr_val
        
        # Call the super constructor (type.__new__)
        return super().__new__(mcs, name, bases, uppercase_attrs)

# Using the metaclass
class MyClass(metaclass=UppercaseAttributesMetaclass):
    name = "Metaclass Demo"
    version = 1.0
    
    def greet(self):
        return f"Welcome to {self.NAME} (v{self.VERSION})"

def main():
    print("--- Metaclass Introduction ---")
    obj = MyClass()
    
    # Notice how we access attributes with uppercase names
    print(f"Original name 'name' is now 'NAME': {hasattr(obj, 'NAME')}")
    print(f"NAME: {obj.NAME}")
    print(f"VERSION: {obj.VERSION}")
    print(obj.greet())
    
    try:
        print(f"Trying to access 'name': {obj.name}")
    except AttributeError:
        print("Attribute 'name' does not exist because the metaclass changed it to 'NAME'.")

if __name__ == "__main__":
    main()
