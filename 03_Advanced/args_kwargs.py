# args_kwargs.py

"""
Definition: *args and **kwargs allow a function to accept a variable number of arguments. 
*args is used for non-keyworded, variable-length argument lists, while **kwargs is used for keyworded, variable-length argument lists.
"""

def multi_arg_func(*args, **kwargs):
    print("Positional arguments (*args):", args)
    print("Keyword arguments (**kwargs):", kwargs)

# Calling with various arguments
multi_arg_func(1, 2, 3, name="Kunal", role="Developer")
