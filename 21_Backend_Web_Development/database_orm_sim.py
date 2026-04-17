# database_orm_sim.py

"""
Definition: ORM (Object-Relational Mapping) is a technique that lets you query and manipulate data from a database using an object-oriented paradigm.
"""

class UserORM:
    def save(self): print("ORM: Translating object to SQL INSERT statement...")

def simulate_orm():
    user = UserORM()
    user.name = "Kunal"
    user.save()
    print("Database record created via ORM.")

simulate_orm()
