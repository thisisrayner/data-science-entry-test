def find_first_negative(lst):
    """
    Go through the list using a while loop and find the first negative number.
    Return it if found, else return "No negatives".
    """

    i = 0  # start at first index
    while i < len(lst):
        if lst[i] < 0:
            # found it!
            return lst[i]
        i += 1  # move to next item

    # if we finish the loop and didn't find any negative
    return "No negatives"

# Test 1: Contains negatives
result1 = find_first_negative([3, 5, -1, 7, -2, 8])
print("Test 1:", result1)  # Should be -1

# Test 2: No negatives
result2 = find_first_negative([2, 10, 7, 0])
print("Test 2:", result2)  # Should be "No negatives"
