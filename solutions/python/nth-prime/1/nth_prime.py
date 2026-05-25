'''Find the nth prime number.'''

def prime(number):
    '''Return the nth prime number.
    Args: number: 1-based index of the prime to return.
    Raises: ValueError: If number < 1.'''
    
    if number < 1:
        raise ValueError('there is no zeroth prime')
    count = 0
    current = 1
    while count < number:
        current += 1
        is_prime = True
        for divider in range(2, int(current**0.5) + 1):
            if current % divider == 0:
                is_prime = False
                break
        if is_prime:
            count += 1
    return current