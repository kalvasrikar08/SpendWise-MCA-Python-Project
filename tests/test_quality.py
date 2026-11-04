
import sys
sys.path.insert(0, "/content/SpendWise")

from modules.quality import (
    calculate_total,
    calculate_average,
    category_count
)

def test_total():
    assert calculate_total([100, 200, 300]) == 600

def test_average():
    assert calculate_average([100, 200, 300]) == 200

def test_empty_expenses():
    assert calculate_average([]) == 0

def test_categories():
    result = category_count(["Food", "Food", "Travel"])
    assert result == {"Food": 2, "Travel": 1}
