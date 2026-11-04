
from functools import wraps

# 1. Custom Iterator
class ExpenseIterator:

    def __init__(self, expenses):
        self.expenses = expenses
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.expenses):
            raise StopIteration

        value = self.expenses[self.index]
        self.index += 1
        return value


# 2. Function Decorator
def track_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Executing:", func.__name__)
        result = func(*args, **kwargs)
        print("Execution completed!")
        return result
    return wrapper


# 3. Context Manager
class ExpenseFile:

    def __enter__(self):
        print("Opening expense file")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Closing expense file")
        return False


# Decorator example
@track_time
def calculate_total(expenses):
    return sum(expenses)
