def check_divisibility(num, divisor):
    """
    Checks if num is divisible by divisor.
    Returns True, False, or "impossible" if divisor is zero.
    """

    # check if both inputs are numbers (int or float)
    if not (isinstance(num, (int, float)) and isinstance(divisor, (int, float))):
        # umm, not a number!
        return False

    # check for zero divisor (can't divide by zero)
    if divisor == 0:
        return "impossible"

    # main check
    if num % divisor == 0:
        return True
    else:
        return False

# Test 1: 10 divided by 2
result1 = check_divisibility(10, 2)
print("Test 1:", result1)  # Should be True

# Test 2: 7 divided by 3
result2 = check_divisibility(7, 3)
print("Test 2:", result2)  # Should be False

# Test 3: Divide by zero
result3 = check_divisibility(15, 0)
print("Test 3:", result3)  # Should be "impossible"
