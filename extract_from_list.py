# Lab 1


test_list = [[3,2,6], [4,9,3], [9,6,3]]

def extract_from_list(test_list):
    """
    This funtion extracts the elements from their lists within another list.
    """

    return [test_list[0][0], test_list[1][2], test_list[2][1]]

print(extract_from_list(test_list))
