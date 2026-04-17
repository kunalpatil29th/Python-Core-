# rest_api_principles.py

"""
Definition: REST (Representational State Transfer) is an architectural style for providing standards between computer systems on the web, making it easier for systems to communicate with each other.
"""

def rest_demo():
    methods = {
        "GET": "Retrieve data",
        "POST": "Create data",
        "PUT": "Update data",
        "DELETE": "Delete data"
    }
    print("RESTful API Principles:")
    for method, desc in methods.items():
        print(f"  {method}: {desc}")

rest_demo()
