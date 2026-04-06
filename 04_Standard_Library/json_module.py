# json_module.py

"""
Definition: The 'json' module provides methods for parsing JSON (JavaScript Object Notation) strings into Python objects and vice-versa.
"""

import json

# Python dictionary to JSON string (serialization)
data = {
    "name": "Kunal",
    "age": 20,
    "skills": ["Python", "Git", "DSA"]
}

json_string = json.dumps(data, indent=4)
print("JSON String:\n", json_string)

# JSON string to Python dictionary (deserialization)
parsed_data = json.loads(json_string)
print("\nParsed dictionary name:", parsed_data["name"])

# Writing JSON to a file
with open("data.json", "w") as f:
    json.dump(data, f, indent=4)
