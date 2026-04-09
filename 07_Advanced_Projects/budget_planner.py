# budget_planner.py

"""
Project: Personal Budget Planner
Helps plan and balance monthly income and expenses.
"""

def plan_budget(income, expenses_dict):
    total_expenses = sum(expenses_dict.values())
    savings = income - total_expenses
    
    print(f"Total Income: ${income}")
    print(f"Total Expenses: ${total_expenses}")
    print(f"Projected Savings: ${savings}")
    
    if savings < 0:
        print("Warning: You are over budget!")
    else:
        print("Good job! You are saving money.")

income = 3000
my_expenses = {"Rent": 1000, "Groceries": 400, "Utilities": 200, "Entertainment": 300}
plan_budget(income, my_expenses)
