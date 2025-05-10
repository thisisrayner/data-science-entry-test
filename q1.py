# q1.py
# Problem: Basic Arithmetic and User Input
# Write a Python script that asks the user for two numbers and then prints their sum,
# difference, product, and quotient.

def perform_arithmetic():
    """
    Asks the user for two numbers and performs basic arithmetic operations.
    """
    print("--- Arithmetic Operations ---")

    # Get input from the user
    try:
        num1_str = input("Enter the first number: ")
        num1 = float(num1_str)  # Convert input to a floating-point number

        num2_str = input("Enter the second number: ")
        num2 = float(num2_str)  # Convert input to a floating-point number
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return

    # Perform calculations
    sum_result = num1 + num2
    difference_result = num1 - num2
    product_result = num1 * num2

    # Handle division by zero for quotient
    if num2 != 0:
        quotient_result = num1 / num2
    else:
        quotient_result = "undefined (division by zero)"

    # Print the results
    print(f"\nResults for {num1} and {num2}:")
    print(f"Sum:        {num1} + {num2} = {sum_result}")
    print(f"Difference: {num1} - {num2} = {difference_result}")
    print(f"Product:    {num1} * {num2} = {product_result}")
    print(f"Quotient:   {num1} / {num2} = {quotient_result}")

if __name__ == "__main__":
    # This block ensures the function runs only when the script is executed directly
    perform_arithmetic()

# Test Cases:
# 1. num1 = 10, num2 = 5
#    Expected: Sum=15, Diff=5, Prod=50, Quot=2.0
# 2. num1 = 7.5, num2 = 2.5
#    Expected: Sum=10.0, Diff=5.0, Prod=18.75, Quot=3.0
# 3. num1 = 8, num2 = 0
#    Expected: Sum=8, Diff=8, Prod=0, Quot="undefined (division by zero)"
# 4. num1 = "abc", num2 = 5
#    Expected: "Invalid input. Please enter numeric values."
