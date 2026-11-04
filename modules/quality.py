from typing import List, Dict


# Type hints
def calculate_total(expenses: List[float]) -> float:
    return sum(expenses)


def calculate_average(expenses: List[float]) -> float:
    if not expenses:
        return 0.0
    return calculate_total(expenses) / len(expenses)


def category_count(categories: List[str]) -> Dict[str, int]:
    result = {}

    for category in categories:
        result[category] = result.get(category, 0) + 1

    return result


# Main function
def main():
    expenses: List[float] = [200, 500, 800, 300]
    categories: List[str] = ["Food", "Travel", "Food", "Shopping"]

    print("Total:", calculate_total(expenses))
    print("Average:", calculate_average(expenses))
    print("Category Count:", category_count(categories))


if __name__ == "__main__":
    main()
