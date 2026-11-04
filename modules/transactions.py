
class Transaction:

    def __init__(self, title, amount, category):
        self.title = title
        self.amount = amount
        self.category = category

    def display(self):
        return f"{self.title}: Rs.{self.amount}"


class Expense(Transaction):
    pass


class Income(Transaction):
    pass
