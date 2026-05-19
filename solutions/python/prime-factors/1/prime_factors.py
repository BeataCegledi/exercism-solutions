'''Compute the prime factors of a natural number.'''

def factors(value):
    '''Return the list of prime factors of value in ascending order.'''
    
    prime = 2
    result = []
    while prime <= value:
        if value % prime == 0:
            value = value // prime
            result.append(prime)
        else:
            prime += 1
    return result
            