def is_valid_triangle(sides):
    #Checking if sides form a valid triangle
    a, b, c = sides
    # All sides must be positive
    if not (a > 0 and b > 0 and c > 0):
        return False
    
    # Tri. inequality
    if not (a + b >= c and b + c >= a and a + c >= b):
        return False
    
    return True


def equilateral(sides):
    a, b, c = sides
    
    return is_valid_triangle(sides) and a == b == c


def isosceles(sides):
    if not is_valid_triangle(sides):
        return False
    
    a, b, c = sides
    
    return a == b or b == c or a == c


def scalene(sides):
    if not is_valid_triangle(sides):
        return False
    
    a, b, c = sides
    # Scalene: all sides different
    return a != b and b != c and a != c
