
import sqlite3

DB_PATH = "/content/SpendWise/spendwise.db"

def create_table():
    with sqlite3.connect(DB_PATH) as db:
        db.execute("""
            CREATE TABLE IF NOT EXISTS transactions(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                category TEXT,
                amount REAL,
                date TEXT
            )
        """)
    print("Database table created!")

def add_transaction(name, category, amount, date):
    with sqlite3.connect(DB_PATH) as db:
        db.execute("""
            INSERT INTO transactions(name, category, amount, date)
            VALUES (?, ?, ?, ?)
        """, (name, category, amount, date))
    print("Transaction saved!")

def view_transactions():
    with sqlite3.connect(DB_PATH) as db:
        records = db.execute(
            "SELECT * FROM transactions"
        ).fetchall()

    for record in records:
        print(record)

