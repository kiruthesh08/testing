import re

def calculate(expression):
    if expression.strip() == "off":
        raise SystemExit

    # Use the '**' operator for exponentiation
    expression = expression.replace('^', '**')

    # Define a custom function to handle exponentiation (^)
    def custom_power(match):
        base, exponent = map(float, match.group(1).split('^'))
        return str(base ** exponent)

    # Use regular expressions to find and replace '^' with the custom_pow function
    expression = re.sub(r'(\d+(\.\d+)?)\s*\^\s*(\d+(\.\d+)?)', custom_power, expression)

    # Use regular expressions to find and replace parentheses with their calculated values
    while '(' in expression:
        expression = re.sub(r'\(([^()]+)\)', lambda x: str(eval(x.group(1))), expression)

    try:
        result = eval(expression)
        return result
    except (ValueError, ZeroDivisionError) as e:
        raise e
    except SyntaxError as e:
        # Handle syntax errors with more specific information
        raise SyntaxError(f"Syntax error in expression: {expression}\n{e}")
    except Exception as e:
        # Handle unexpected errors gracefully
        raise Exception("An unexpected error occurred:", str(e))

if __name__ == "__main__":
    while True:
        print("Options:")
        print("Enter 'off' to end the program")

        user_input = input("Enter any expression: ")

        if user_input == "off":
            break

        try:
            result = calculate(user_input)
            if isinstance(result, (int, float)):
                print("Result:", result)
            else:
                print("Invalid input or calculation error. Please enter a valid expression.")
        except (ValueError, ZeroDivisionError) as e:
            print("Error:", str(e))
        except SyntaxError as e:
            print("Syntax error:", str(e))
        except Exception as e:
            print("An unexpected error occurred:", str(e))
