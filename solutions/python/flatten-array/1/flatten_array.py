def flatten(iterable):
    '''Return a flat list from a nested list of any depth.'''
    
    result = []
    for item in iterable:
        if isinstance(item, list):
            result.extend(flatten(item))
        else: 
            if item is not None and item != '':
                result.append(item)
    return result

 