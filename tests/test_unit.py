import pytest
from src.calculate import add_plus, add_multiply
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
def test__add_plus_wrong_type(num1, num2):
    expected_error = "Error: Both arguments must be float"
    assert add_plus(num1, num2) == expected_error

@pytest.mark.parametrize("num1, num2, expected",[
    (5, 5, 25),
    (5.0, 5.0, 25.0),
    (6, 5.0, 30.0),
    (5.0, 6, 30.0)
])
def test__add_multiply__success(num1, num2, expected): 
    assert add_multiply(num1, num2) == expected
    
@pytest.mark.parametrize("num1, num2", [
    ("สวัสดี", "Test"),
    (1, "Test"),
    ("สวัสดี", 1),
])
def test__add_multiply_wrong_type(num1, num2):
    expected_error = "Error: Both arguments must be float"
    assert add_multiply(num1, num2) == expected_error