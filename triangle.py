"""
equilateral triangles have all three sides with the same length
isosceles triangles have two sides with the same length
scalene triangles have three sides with different lengths
right triangles have three sides with lengths, a, b, and c where a2 + b2 = c2
"""
def classify_triangle(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return "Invalid"

    if a + b <= c or a + c <= b or b + c <= a:
        return "Invalid"

    if a == b == c:
        return "Equilateral"


    if a == b or b == c or a == c:
        triangle_type = "Isosceles"
    else:
        triangle_type = "Scalene"

    sides = sorted([a, b, c])
    if sides[0]**2 + sides[1]**2 == sides[2]**2:
        triangle_type = "Right " + triangle_type

    return triangle_type
