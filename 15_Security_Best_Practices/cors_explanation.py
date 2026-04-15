# cors_explanation.py

"""
Definition: Cross-Origin Resource Sharing (CORS) is a security mechanism that allows a web page from one origin to access resources from a different origin.
"""

def simulate_cors_check(origin, allowed_origins):
    if origin in allowed_origins:
        print(f"Access Granted to {origin}")
        return {"Access-Control-Allow-Origin": origin}
    else:
        print(f"Access Denied to {origin}")
        return {"Error": "CORS Policy Violation"}

# Usage
allowed = ["https://my-app.com", "http://localhost:3000"]
print(simulate_cors_check("https://my-app.com", allowed))
print(simulate_cors_check("https://hacker-site.com", allowed))
