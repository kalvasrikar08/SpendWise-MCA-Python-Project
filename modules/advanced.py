
# List comprehension
def high_expenses(expenses):
    return [e for e in expenses if e["amount"] > 500]

# Dictionary comprehension
def expense_summary(expenses):
    return {
        e["category"]: e["amount"]
        for e in expenses
    }

# Set comprehension
def categories(expenses):
    return {e["category"] for e in expenses}

# Generator function
def expense_generator(expenses):
    for expense in expenses:
        yield expense["amount"]

# Generator expression
def total_expense(expenses):
    return sum(e["amount"] for e in expenses)
