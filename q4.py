def string_reverse(s):
    """
    Reverse the given string s.
    s must be a string.
    Return the reversed one.
    """

    # quick check - make sure input is string, not something else
    if not isinstance(s, str):
        # sorry, can't reverse non-strings
        return None

    # reverse the string
    reversed_s = s[::-1]  

    return reversed_s

# Test 1: Reverse "Hello World"
result1 = string_reverse("Hello World")
print("Test 1:", result1)

# Test 2: Reverse "Python"
result2 = string_reverse("Python")
print("Test 2:", result2)
