"""Returns the dart score based on the distance from the center of the target."""

def score(x, y):
    distance = ((x ** 2) + (y ** 2)) ** 0.5
    if 0 <= distance <= 1:
        return 10
    elif 1 < distance <= 5:
        return 5
    elif  5 < distance <= 10:
        return 1
    return 0    
