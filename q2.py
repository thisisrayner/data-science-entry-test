def find_and_replace(lst, find_val, replace_val):
    """
    Go thru the list and swap every find_val with replace_val.
    Return the new list (modifed).
    """

    # make sure it's a list, otherwise we can't continue
    if not isinstance(lst, list):
        # not a list!! abort mission
        return None

    # let's go thru the list and do the replacing
    for i in range(len(lst)):
        if lst[i] == find_val:
            lst[i] = replace_val  # swap it!

    return lst

# Test 1: replace 2s with 5s
result1 = find_and_replace([1, 2, 3, 4, 2, 2], 2, 5)
print("Test 1:", result1)

# Test 2: replace 'apple' with 'orange'
result2 = find_and_replace(["apple", "banana", "apple"], "apple", "orange")
print("Test 2:", result2)
