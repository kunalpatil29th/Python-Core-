# microservices_sim.py

"""
Definition: Microservices is an architectural style that structures an application as a collection of services that are highly maintainable, testable, loosely coupled, and independently deployable.
"""

class OrderService:
    def create_order(self, item):
        print(f"Order Service: Creating order for {item}")
        return "ORD101"

class InventoryService:
    def check_stock(self, item):
        print(f"Inventory Service: Checking stock for {item}")
        return True

class APIGateway:
    def __init__(self, order, inventory):
        self.order = order
        self.inventory = inventory

    def place_order(self, item):
        if self.inventory.check_stock(item):
            return self.order.create_order(item)
        return "Out of stock"

# Usage
api = APIGateway(OrderService(), InventoryService())
print(f"Result: {api.place_order('Python Course')}")
