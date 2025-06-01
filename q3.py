def update_dictionary(dct, key, value):
    """
    Add a new key-value to the dictionary.
    If the key is already there, print out the old value first before updating.
    Return the updated dictionary at the end.
    """

    # check if the key exists
    if key in dct:
        print("Original value for key", key, ":", dct[key])
    
    # update or add the key-value
    dct[key] = value
    
    return dct

# Test 1: Add new key to an empty dict
result1 = update_dictionary({}, "name", "Alice")
print("Test 1:", result1)

# Test 2: Update existing key in a dict
result2 = update_dictionary({"age": 25}, "age", 26)
print("Test 2:", result2)
