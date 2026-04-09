# expense_tracker.py

"""
Project: Expense Tracker
A tool to track daily expenses with category and amount.
"""

expenses = []

def add_expense(amount, category, description):
    expenses.append({"amount": amount, "category": category, "description": description})
    print(f"Added expense: {description} (${amount})")

def show_summary():
    total = sum(e['amount'] for e in expenses)
    print(f"\nTotal Expenses: ${total}")
    for e in expenses:
        print(f"- {e['category']}: ${e['amount']} ({e['description']})")

add_expense(50, "Food", "Lunch at cafe")
add_expense(20, "Transport", "Bus fare")
show_summary()
