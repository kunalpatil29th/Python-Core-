# jwt_token_sim.py

"""
Definition: JSON Web Token (JWT) is a compact, URL-safe means of representing claims to be transferred between two parties.
"""

import base64
import json
import hashlib
import hmac

def create_jwt(payload, secret):
    header = {"alg": "HS256", "typ": "JWT"}
    header_encoded = base64.urlsafe_b64encode(json.dumps(header).encode()).decode().rstrip("=")
    payload_encoded = base64.urlsafe_b64encode(json.dumps(payload).encode()).decode().rstrip("=")
    
    signature = hmac.new(secret.encode(), f"{header_encoded}.{payload_encoded}".encode(), hashlib.sha256).digest()
    signature_encoded = base64.urlsafe_b64encode(signature).decode().rstrip("=")
    
    return f"{header_encoded}.{payload_encoded}.{signature_encoded}"

# Usage
secret_key = "my_super_secret"
user_payload = {"user_id": 1, "username": "kunal"}
token = create_jwt(user_payload, secret_key)
print(f"Generated JWT: {token}")
