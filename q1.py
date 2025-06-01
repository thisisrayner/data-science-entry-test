def swap(x, y):
    """
    swap(x, y) swaps the values of x and y.
    If both are numbers, print them swapped. If not, return -1.
    """

    # check if x and y are numbers (ints or floats) 
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        # not numbers
        return -1
    
    # swapping
    temp = x
    x = y
    y = temp

    # print result
    print("Swapped values:", x, y)

# Test case 1: not both numbers
result1 = swap("Apple", 10)
print("Result1:", result1)  # Should be -1

# Test case 2: both numbers
result2 = swap(9, 17)
print("Result2:", result2)  # Should print swapped values and None (because the function doesn't return anything)
