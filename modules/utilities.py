
import os
from pathlib import Path
from datetime import datetime
from collections import Counter

# Project directory
PROJECT = Path("/content/SpendWise")

# Current date and time
def show_date():
    print("Current Date:", datetime.now().strftime("%d-%m-%Y"))
    print("Current Time:", datetime.now().strftime("%H:%M:%S"))

# Folder information
def show_files():
    print("\nProject Files:")
    for file in PROJECT.iterdir():
        print(file.name)

# Expense category statistics
def category_report(categories):
    result = Counter(categories)
    print("\nCategory Statistics:")
    for category, count in result.items():
        print(category, ":", count)

# Operating system information
def system_info():
    print("\nOperating System:", os.name)
    print("Project Location:", PROJECT.resolve())
