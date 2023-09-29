import pytest

from hello_world import helloworld

# Define a test function using 'test_' 
def test_hello_world():
    # Call function and store result
    result = helloworld()

    # Define expected result
    expected_result = "hello_world"

    #assertion to check if the result matches the expected result
    assert result == expected_result
    
