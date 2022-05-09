def reverse_string(str):
    """
    This function uses the splice operator to iterate through a string, beginning from the end, and adds each character to a new string that is returned.
    """
    
    return str[::-1]


print(reverse_string("Hello Everyone!"))