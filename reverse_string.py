def reverse_string(str):
    """
    This function uses the splice operator to iterate through a string, beginning from the end, and adds each character to a new string that is returned.
    """
    new_str = ""
    for c in str:
        new_str = c + new_str
    return new_str


print(reverse_string("Hello Everyone!"))