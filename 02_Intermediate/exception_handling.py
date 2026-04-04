# exception_handling.py

"""
Definition: Exception handling is the process of responding to the occurrence of anomalous or exceptional conditions 
(runtime errors) during execution. Python uses try, except, finally blocks.
"""

try:
    num = int(input("Enter a number to divide 10 by: "))
    result = 10 / num
    print("Result:", result)
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")
except ValueError:
    print("Error: Please enter a valid integer!")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
finally:
    print("Execution of the try-except block is complete.")
