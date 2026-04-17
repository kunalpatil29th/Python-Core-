# graphql_basics.py

"""
Definition: GraphQL is a query language for APIs and a runtime for fulfilling those queries with your existing data. It provides a complete and understandable description of the data in your API.
"""

def simulate_graphql():
    query = "{ user(id: 1) { name, email } }"
    print(f"Executing GraphQL Query: {query}")
    response = {"data": {"user": {"name": "Kunal", "email": "kunal@example.com"}}}
    print(f"Response: {response}")

simulate_graphql()
