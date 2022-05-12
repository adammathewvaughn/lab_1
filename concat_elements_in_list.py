def concat_elements_in_list(str):
    """
    This function concatenates all the elements in the list together using the join() function.
    """
    result = ""
    for c in str:
        result =  result + c  + " " 
    return result


print(concat_elements_in_list (["Hello,", "everyone", "out", "there!"]))