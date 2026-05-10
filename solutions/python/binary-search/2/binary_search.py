def find(search_list, value):
    
    """Binary search for a value in a sorted list.

    :param search_list: Sorted list to search in
    :param value: Value to find
    :return: Index of the value in the original list
    :raises ValueError: If the value is not found
    """

    part_list = search_list
    while value in part_list:
        index = len(part_list) // 2
        if part_list[index] > value:
            part_list = part_list[:index]
        elif part_list[index] < value:
            part_list = part_list[index+1:]
        else:
            return search_list.index(value)
    raise ValueError('value not in array')
