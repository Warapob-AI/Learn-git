import pytest
from src.calculate import add_plus
from unittest.mock import MagicMock 

@pytest.mark.parametrize("num1, num2, expected", [
    (1, 2, 3),
    (1.0, 2.0, 3.0),
    (1.0, 2, 3.0),
    (1, 2.0, 3.0)
])
def test__add_plus__success(num1, num2, expected):
    assert add_plus(num1, num2) == expected

    
@pytest.mark.parametrize("num1, num2", [
    ("สวัสดี", "Test"),
    (1, "Test"),
    ("สวัสดี", 1),
])
def test_add_plus_wrong_type(num1, num2):
    expected_error = "Error: Both arguments must be float"
    assert add_plus(num1, num2) == expected_error
