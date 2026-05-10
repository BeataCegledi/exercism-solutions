def find(search_list, value):
    
    """Binary search for a value in a sorted list.

    :param search_list: Sorted list to search in
    :param value: Value to find
    :return: Index of the value in the original list
    :raises ValueError: If the value is not found
    """

    list = search_list
    while value in list:
        index = len(list) // 2
        if list[index] > value:
            list = list[:index]
        elif list[index] < value:
            list = list[index+1:]
        else:
            return search_list.index(value)
    raise ValueError('value not in array')
