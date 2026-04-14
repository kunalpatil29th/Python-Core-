# encapsulation.py

"""
Definition: Encapsulation is the packing of data and functions into a single component. It also involves hiding the internal state of an object and requiring all interaction to be performed through an object's methods.
"""

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance  # Private attribute (denoted by __)

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ${amount}. New balance is ${self.__balance}.")

    def get_balance(self):
        # Getter method to access private attribute
        return self.__balance

account = BankAccount("Kunal", 1000)
account.deposit(500)
print(f"Current Balance: ${account.get_balance()}")

# Trying to access __balance directly will raise an AttributeError:
# print(account.__balance)
