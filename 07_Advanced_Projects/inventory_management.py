# inventory_management.py

"""
Project: Inventory Management System
Track products, stock levels, and prices in a simple system.
"""

inventory = {}

def update_stock(product, quantity, price):
    inventory[product] = {"quantity": quantity, "price": price}
    print(f"Updated {product}: {quantity} in stock at ${price}")

def check_stock(product):
    item = inventory.get(product)
    if item:
        return f"{product}: {item['quantity']} available at ${item['price']}"
    return f"{product} not found in inventory"

update_stock("Laptop", 10, 800)
update_stock("Mouse", 50, 20)
print(check_stock("Laptop"))
