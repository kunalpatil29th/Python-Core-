# simple_atm.py

"""
Project: Simple ATM Simulator
Simulates basic ATM operations like balance check, deposit, and withdrawal.
"""

balance = 1000

def check_balance():
    print(f"Current Balance: ${balance}")

def deposit(amount):
    global balance
    balance += amount
    print(f"Deposited ${amount}. New balance: ${balance}")

check_balance()
deposit(500)
