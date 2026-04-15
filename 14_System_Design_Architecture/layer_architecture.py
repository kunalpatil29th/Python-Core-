# layer_architecture.py

"""
Definition: Layered Architecture is a pattern where the components are organized into horizontal layers. Each layer has a specific role and responsibility.
Typical layers: Presentation, Business, Persistence, and Database.
"""

class Database:
    def get_user(self): return "User123"

class PersistenceLayer:
    def __init__(self, db): self.db = db
    def fetch_user(self): return self.db.get_user()

class BusinessLayer:
    def __init__(self, persistence): self.persistence = persistence
    def process_user(self):
        user = self.persistence.fetch_user()
        return f"Processed {user}"

class PresentationLayer:
    def __init__(self, business): self.business = business
    def show(self):
        print(f"UI: {self.business.process_user()}")

# Usage
db = Database()
pl = PersistenceLayer(db)
bl = BusinessLayer(pl)
ui = PresentationLayer(bl)
ui.show()
