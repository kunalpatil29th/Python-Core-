# middleware_concepts.py

"""
Definition: Middleware is software that acts as a bridge between an operating system or database and applications, especially on a network. In web frameworks, it processes requests before they reach the view.
"""

def middleware_chain():
    print("1. Request Received")
    print("2. Authentication Middleware -> PASS")
    print("3. Logging Middleware -> LOGGED")
    print("4. Routing to View...")
    print("5. Response Sent")

middleware_chain()
