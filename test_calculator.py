import pytest
from calculator import calculate

# Test addition
def test_addition():
    assert calculate("2 + 3") == 5

# Test subtraction
def test_subtraction():
    assert calculate("5 - 2") == 3

# Test multiplication
def test_multiplication():
    assert calculate("4 * 6") == 24

# Test division
def test_division():
    assert calculate("10 / 2") == 5

# Test exponentiation (^)
def test_exponentiation():
    assert calculate("2^3") == 8

# Test complex expression with parentheses
def test_complex_expression():
    assert calculate("(4 + 2) * 3 / 2 - 1") == 8

# Test division by zero
def test_division_by_zero():
    with pytest.raises(ZeroDivisionError):
        calculate("5 / 0")

# Test invalid input
def test_invalid_input():
    with pytest.raises(Exception):
        calculate("2 + abc")

# Test an unexpected error
def test_unexpected_error():
    with pytest.raises(Exception):
        calculate("2 / (2 - 2)")
        
    # Test the 'off' option to exit the program
def test_exit_program(monkeypatch): #monkeypatch fixture allows you to modify or control certain behaviors during testing.
    # Mock user input to simulate entering 'off'
    monkeypatch.setattr('builtins.input', lambda _: 'off') # uses the monkeypatch fixture to temporarily modify the behavior of the input function. 
                                                           #It replaces the input function with a lambda function that always returns the string 'off'. 
    with pytest.raises(SystemExit) as excinfo: #sets up a context for testing exceptions using pytest.raises.SystemExit exception raised
        calculate("off")  # Pass "off" as the argument
    assert excinfo.type == SystemExit #verifies that an exception of type SystemExit was indeed raised 
