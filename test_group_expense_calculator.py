import pytest
from group_expense_calculator import GroupExpenseCalculator

@pytest.fixture
def calculator():
    return GroupExpenseCalculator()

def test_add_expense(calculator):
    calculator.add_expense("John", 100.0, ["John", "Alice", "Bob"])
    assert calculator.groups["John"]["Alice"] == 33.333333333333336
    assert calculator.groups["John"]["Bob"] == 33.333333333333336

def test_update_balance(calculator):
    calculator.update_balance("John", "Alice", 33.33)
    assert calculator.groups["John"]["Alice"] == 33.33

def test_calculate_debts(capfd, calculator):
    calculator.add_expense("John", 100.0, ["John", "Alice", "Bob"])
    calculator.calculate_debts()
    captured = capfd.readouterr()
    assert "Alice owes Rs.33.33 to John" in captured.out

