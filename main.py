
from modules import (
    Expense, Income,
    calculate_expenses,
    calculate_income,
    calculate_balance
)

def main():

    transactions = [
        Expense("Food", 500, "Food"),
        Expense("Travel", 300, "Transport"),
        Income("Salary", 15000, "Job")
    ]

    print("===== SPENDWISE SYSTEM =====")

    for t in transactions:
        print(t.display())

    print("\nTotal Expenses:",
          calculate_expenses(transactions))

    print("Total Income:",
          calculate_income(transactions))

    print("Remaining Balance:",
          calculate_balance(transactions))


if __name__ == "__main__":
    main()
