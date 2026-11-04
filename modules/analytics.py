
from .transactions import Expense, Income

def calculate_expenses(transactions):
    return sum(
        t.amount for t in transactions
        if isinstance(t, Expense)
    )

def calculate_income(transactions):
    return sum(
        t.amount for t in transactions
        if isinstance(t, Income)
    )

def calculate_balance(transactions):
    return calculate_income(transactions) - calculate_expenses(transactions)
