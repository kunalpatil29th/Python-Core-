# external_lib.py

"""
Definition: External libraries are pre-written code packages that extend Python's functionality.
'pyjokes' is a simple library that provides random programming jokes.
To use an external library, you must first install it (e.g., pip install pyjokes) and then import it.
"""

import pyjokes

# Get a random programming joke
joke = pyjokes.get_joke()

print("Here's a programming joke for you:")
print(joke)
