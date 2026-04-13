# json_advanced.py

"""
Definition: Advanced JSON handling involves working with complex nested structures, 
custom encoders/decoders, and efficient parsing of large JSON files.
"""

import json

data = {
    "project": "Python-Core-",
    "stats": {
        "stars": 10,
        "forks": 2,
        "active": True
    },
    "tags": ["learning", "python", "fundamentals"]
}

# Pretty printing JSON
pretty_json = json.dumps(data, indent=4, sort_keys=True)
print("Pretty JSON Output:\n", pretty_json)

# Accessing nested data
parsed = json.loads(pretty_json)
print(f"\nProject Status: {'Active' if parsed['stats']['active'] else 'Inactive'}")
