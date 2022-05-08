def reverse_string(str):
    """
    This function uses the splice operator to iterate through a string, beginning from the end, and adds each character to a new string that is returned.
    """
    test_string = "Hello Everyone!"
    return test_string[::-1]


print(reverse_string(""))