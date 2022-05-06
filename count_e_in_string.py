def count_e_in_string(str):
    """
    This function iterates through a string and counts the number of "E"s in it.

    Params: string(str), string to count the number of E's
    Returns: int, the number of E's in the string
    """
    return int(str.count("E"))
print(count_e_in_string("Hello, Eric!"))