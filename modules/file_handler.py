
import json
import csv

# Save expenses in JSON
def save_json(expenses):

    with open("/content/SpendWise/expenses.json", "w") as file:
        json.dump(expenses, file, indent=4)

    print("JSON file saved successfully!")

# Read JSON
def read_json():

    with open("/content/SpendWise/expenses.json", "r") as file:
        data = json.load(file)

    print("JSON Records:", data)

# Export CSV
def save_csv(expenses):

    with open("/content/SpendWise/expenses.csv", "w", newline="") as file:
        writer = csv.DictWriter(
            file, fieldnames=["name", "category", "amount"]
        )

        writer.writeheader()
        writer.writerows(expenses)

    print("CSV report exported successfully!")
