def sum_characters_in_list(elements):  
    """
    Write a functuon to sum all the elements in a list. You can assume all the elements are of type int.
    Params: elements (list), list of integers
    Returns: int, the sum of all the integers
    """
    count = 0
    for i in elements:
        count = count + i
    return count

print(sum_characters_in_list(int))
