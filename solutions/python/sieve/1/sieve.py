def primes(limit):
    """Gibt alle Primzahlen bis `limit` zurück (Sieve of Eratosthenes).

    Args:
        limit: obere Grenze (inklusive).

    Returns:
        Liste der Primzahlen in aufsteigender Reihenfolge.
    """
    numbers = list(range(2, limit+1))
    prim = numbers.copy()
    for check in numbers:
        if check in prim:
             for multipled in range(check*2, limit+1, check):
                if multipled in prim: 
                    prim.remove(multipled)
    return prim
        