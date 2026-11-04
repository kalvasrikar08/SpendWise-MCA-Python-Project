
import sys
import pytest
from unittest.mock import patch

sys.path.insert(0, "/content/SpendWise")

from modules.quality import calculate_total, calculate_average

# 1. Pytest Fixture
@pytest.fixture
def expenses():
    return [100, 200, 300]

# 2. Parameterized Testing
@pytest.mark.parametrize("values, expected", [
    ([100, 200], 300),
    ([500, 500], 1000),
    ([50, 50, 50], 150)
])
def test_total(values, expected):
    assert calculate_total(values) == expected

# 3. Fixture Testing
def test_expense_fixture(expenses):
    assert calculate_total(expenses) == 600

# 4. Mocking
def test_mock_average(expenses):
    with patch(
        "modules.quality.calculate_total",
        return_value=900
    ):
        assert calculate_average(expenses) == 300
