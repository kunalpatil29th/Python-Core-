# strategy_pattern.py

"""
Definition: The Strategy Pattern defines a family of algorithms, encapsulates each one, and makes them interchangeable.
"""

class PaymentStrategy:
    def pay(self, amount):
        pass

class CreditCardPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paid ${amount} using Credit Card.")

class PayPalPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paid ${amount} using PayPal.")

class ShoppingCart:
    def __init__(self, strategy):
        self._strategy = strategy

    def checkout(self, amount):
        self._strategy.pay(amount)

# Usage
cart = ShoppingCart(CreditCardPayment())
cart.checkout(100)
cart = ShoppingCart(PayPalPayment())
cart.checkout(200)
