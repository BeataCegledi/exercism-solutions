def is_triangle(sides):
    """Check if three sides form a valid triangle."""
    return all(s > 0 for s in sides) and sides[0] + sides[1] >= sides[2] and sides[0] + sides[2] >= sides[1] and sides[1] + sides[2] >= sides[0]

def equilateral(sides):
    """Return True if the triangle is equilateral (all sides equal)."""
    return is_triangle(sides) and sides[0] == sides[1] == sides[2]

def isosceles(sides):
    """Return True if the triangle is isosceles (at least two sides equal)."""
    return is_triangle(sides) and (sides[0] == sides[1] or sides[0] == sides[2] or sides[2] == sides[1])

def scalene(sides):
    """Return True if the triangle is scalene (all sides different)."""
    return is_triangle(sides) and sides[0] != sides[1] and sides[0] != sides[2] and sides[2] != sides[1]