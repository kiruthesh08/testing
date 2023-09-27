import unittest
import re

def calculate(expression):
    # Define a custom function to handle exponentiation (^)
    def custom_power(match):
        base, exponent = map(float, match.group(1).split('^'))
        return str(base ** exponent)
    
    # Use regular expressions to find and replace '^' with the custom_pow function, ustom_pow to handle exponentiation (^) using a regular expression
    expression = re.sub(r'(\d+(\.\d+)?)\s*\^\s*(\d+(\.\d+)?)', custom_power, expression)
    
    # Use regular expressions to find and replace parentheses with their calculated values
    while '(' in expression:
        expression = re.sub(r'\(([^()]+)\)', lambda x: str(eval(x.group(1))), expression)
    
    return eval(expression)

while True:
    print("Options:")
    print("Enter 'off' to end the program")

    user_input = input("Enter any expression: ")

    if user_input == "off":
        break

    try:
        result = calculate(user_input)
        if isinstance(result, (int, float)):  #check whether the result is an instance of either an int or a float to see if value is numeric. 
            print("Result:", result)
        else:
            print("Invalid input or calculation error. Please enter a valid expression.")
    except (ValueError, ZeroDivisionError) as e:
        print("Error:", str(e))
    except Exception as e:
        print("An unexpected error occurred:", str(e))




"""
class TestCalculate(unittest.TestCase):

    def test_addition(self):
        result = calculate("5+3")
        self.assertEqual(result, 8)

    def test_subtraction(self):
        result = calculate("10-4")
        self.assertEqual(result, 6)

    def test_multiplication(self):
        result = calculate("3*4")
        self.assertEqual(result, 12)

    def test_division(self):
        result = calculate("8/2")
        self.assertEqual(result, 4)

    def test_exponentiation(self):
        result = calculate("2^3")
        self.assertEqual(result, 8)

    def test_complex_expression(self):
        result = calculate("(5+3)*2")
        self.assertEqual(result, 16)

    def test_complex_expression(self):
        result = calculate("(9+3)*3")
        self.assertEqual(result, 36)

if __name__ == "__main__":
    unittest.main()

"""