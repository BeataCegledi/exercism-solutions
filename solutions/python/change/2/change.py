"""Find the fewest coins needed to make a given amount of change."""

def find_fewest_coins(coins, target):
    """Return the fewest coins from `coins` that sum to `target`.
    Args:
        coins: Available coin denominations.
        target: Amount of change to make.
    Returns:
        Sorted list of coin values.
    Raises ValueError: If `target` is negative or unreachable."""
    
    if target < 0:
        raise ValueError("target can't be negative")
    if target == 0:
        return []
    best = [None] * (target + 1)
    best[0] = []    
    for small in range(1,target+1):
        for coin in coins:
            if coin <= small and best[small - coin] is not None:
                current = best[small - coin] + [coin]
                if best[small] is None or len(current)<len(best[small]):
                    best[small] = current
    if best[target] is None:
        raise ValueError("can't make target with given coins")
    return sorted(best[target])
            