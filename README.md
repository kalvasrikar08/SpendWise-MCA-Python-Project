# SpendWise – Personal Expense Management System

## MCA Python Capstone Project

**Student Name:** Kalwa Srikar  
**Roll Number:** 2620600021  
**Project:** SpendWise – Personal Expense Management System  
**Language:** Python

## 1. Project Overview

SpendWise is a Python-based personal finance management application designed to record income and expenses and calculate financial summaries.

It helps users understand their spending patterns and remaining balance through transaction management and category-wise analysis.

## 2. Features

- Income and expense management
- Transaction categorization
- Automatic expense calculation
- Total income calculation
- Remaining balance calculation
- Category-wise analysis
- JSON and CSV data handling
- SQLite database support
- Exception handling and input validation
- Automated testing using pytest

## 3. Technologies Used

- Python 3
- Object-Oriented Programming
- SQLite
- JSON
- CSV
- pytest
- Git and GitHub
- GitHub Actions
- mypy, Black and Ruff

## 4. Project Structure

```text
SpendWise/
│
├── main.py
├── modules/
│   ├── __init__.py
│   ├── transactions.py
│   ├── analytics.py
│   ├── database.py
│   ├── file_handler.py
│   ├── errors.py
│   ├── utilities.py
│   └── quality.py
│
├── tests/
├── reports/
├── expenses.json
├── expenses.csv
└── spendwise.db
```

## 5. Sample Output

```text
===== SPENDWISE SYSTEM =====

Food: Rs.500
Travel: Rs.300
Salary: Rs.15000

Total Expenses: 800
Total Income: 15000
Remaining Balance: 14200
```

## 6. How to Run

Install Python 3 and required development dependencies.

```bash
pip install pytest
```

Run the application:

```bash
python main.py
```

Run tests:

```bash
pytest -q
```

## 7. GitHub Actions

GitHub Actions is used for Continuous Integration (CI).

The workflow automatically runs configured checks when code is pushed to GitHub.

## 8. Academic Modules Covered

1. Python Fundamentals and Algorithmic Thinking
2. Object-Oriented Programming
3. Modules, Packages and Project Structure
4. Exceptions, File I/O and Standard Library
5. Idiomatic Python
6. Testing, Git and AI-Assisted Coding

## 9. Future Enhancements

- Monthly expense reports
- Graphical dashboard
- Budget planning
- Spending alerts
- Advanced financial analytics

## 10. Author

**Kalwa Srikar**  
MCA – Python Capstone Project  
Roll Number: 2620600021
