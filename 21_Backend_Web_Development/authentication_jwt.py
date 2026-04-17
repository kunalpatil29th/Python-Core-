# authentication_jwt.py

"""
Definition: JWT (JSON Web Token) authentication is a stateless authentication mechanism where a token is used to identify the user on subsequent requests.
"""

def simulate_jwt_auth():
    print("User logging in...")
    token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
    print(f"Generated JWT: {token}")
    print("Attaching token to 'Authorization' header: Bearer <token>")

simulate_jwt_auth()
