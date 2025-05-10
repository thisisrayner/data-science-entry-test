# q3.py
# Problem: Loops and Lists - Sum of Even Numbers
# Write a Python script that takes a list of integers and calculates
# the sum of all even numbers in that list using a for loop.

def sum_even_numbers(numbers):
    """
    Calculates the sum of even numbers in a given list of integers.

    Args:
        numbers (list of int): A list of integers.

    Returns:
        int: The sum of all even numbers in the list. Returns 0 if list is empty
             or contains no even numbers.
    """
    even_sum = 0  # Initialize sum of even numbers
    if not numbers: # Check if the list is empty
        print("The list is empty.")
        return 0

    print(f"Processing list: {numbers}")
    for number in numbers:
        # Check if the number is an integer (or can be treated as one)
        if isinstance(number, int) or (isinstance(number, float) and number.is_integer()):
            if number % 2 == 0:  # Check if the number is even
                even_sum += number
        else:
            print(f"Skipping non-integer value: {number}")

    return even_sum

if __name__ == "__main__":
    print("--- Sum of Even Numbers in a List ---")

    # Example list of numbers
    num_list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    result1 = sum_even_numbers(num_list1)
    print(f"Sum of even numbers in {num_list1}: {result1}\n") # Expected: 2 + 4 + 6 + 8 + 10 = 30

    num_list2 = [11, 13, 15, 17]
    result2 = sum_even_numbers(num_list2)
    print(f"Sum of even numbers in {num_list2}: {result2}\n") # Expected: 0

    num_list3 = []
    result3 = sum_even_numbers(num_list3)
    print(f"Sum of even numbers in {num_list3}: {result3}\n") # Expected: 0 (with "The list is empty." message)

    num_list4 = [2, 4, 6.0, 8, "text", 10, 3.5]
    result4 = sum_even_numbers(num_list4)
    print(f"Sum of even numbers in {num_list4}: {result4}\n") # Expected: 2+4+6+8+10 = 30 (with "Skipping..." messages)

# Test Cases:
# 1. [1, 2, 3, 4, 5, 6] -> Expected: 12
# 2. [10, 20, 30]      -> Expected: 60
# 3. [1, 3, 5]          -> Expected: 0
# 4. []                 -> Expected: 0
# 5. [2, "a", 4, 5.0]   -> Expected: 6 (with skip message for "a" and 5.0 if not integer)
