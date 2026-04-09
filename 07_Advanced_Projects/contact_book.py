# contact_book.py

"""
Project: Contact Book
A simple application to save and search for contact information.
"""

contacts = {}

def add_contact(name, phone, email):
    contacts[name] = {"phone": phone, "email": email}
    print(f"Contact {name} added successfully.")

def search_contact(name):
    info = contacts.get(name)
    if info:
        return f"Name: {name}, Phone: {info['phone']}, Email: {info['email']}"
    return "Contact not found."

add_contact("Kunal", "1234567890", "kunal@example.com")
print(search_contact("Kunal"))
