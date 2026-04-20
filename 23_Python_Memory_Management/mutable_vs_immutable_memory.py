# mutable_vs_immutable_memory.py

"""
Definition: Memory management differs between mutable objects (like lists, dictionaries) 
and immutable objects (like strings, integers, tuples). 
When a mutable object is modified, its memory address remains the same, but its content changes. 
When an immutable object is 'modified', a new object is created in memory, 
and the variable is updated to point to the new address.
"""

def test_mutable_memory():
    """Demonstrates memory behavior of mutable objects."""
    print("--- Mutable Objects (List) ---")
    my_list = [1, 2, 3]
    print(f"Initial List: {my_list}, Memory Address: {id(my_list)}")
    
    my_list.append(4)
    print(f"Modified List: {my_list}, Memory Address: {id(my_list)}")
    print("Memory address remains the SAME after modification.")

def test_immutable_memory():
    """Demonstrates memory behavior of immutable objects."""
    print("\n--- Immutable Objects (String) ---")
    my_string = "Hello"
    print(f"Initial String: '{my_string}', Memory Address: {id(my_string)}")
    
    my_string += " World"
    print(f"Modified String: '{my_string}', Memory Address: {id(my_string)}")
    print("Memory address CHANGES after 'modification'. A new object was created.")

    print("\n--- Immutable Objects (Integer) ---")
    num = 10
    print(f"Initial Number: {num}, Memory Address: {id(num)}")
    
    num += 1
    print(f"Modified Number: {num}, Memory Address: {id(num)}")
    print("Memory address CHANGES after 'modification'.")

def main():
    test_mutable_memory()
    test_immutable_memory()

if __name__ == "__main__":
    main()
