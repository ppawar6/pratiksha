"""Module for classifying triangles based on their side lengths."""


def classify_triangle(side_a, side_b, side_c):
    """
    Classify a triangle based on its three side lengths.

    Determines whether a triangle is valid and classifies it as:
    - Equilateral: all three sides equal
    - Isosceles: exactly two sides equal
    - Scalene: all three sides different
    - Right Scalene/Isosceles: satisfies Pythagorean theorem

    Args:
        side_a: First side length (numeric)
        side_b: Second side length (numeric)
        side_c: Third side length (numeric)

    Returns:
        str: Classification of the triangle:
             "Invalid" if inputs are invalid,
             "Equilateral" for equilateral triangles,
             "Isosceles" for isosceles triangles,
             "Scalene" for scalene triangles,
             "Right Isosceles" for right isosceles triangles,
             "Right Scalene" for right scalene triangles.

    Raises:
        TypeError: If any input cannot be converted to a number.
    """
    # Validate input types
    try:
        side_a = float(side_a)
        side_b = float(side_b)
        side_c = float(side_c)
    except (TypeError, ValueError) as error:
        raise TypeError("All sides must be numeric") from error

    # Check for invalid triangle sides (zero or negative)
    if side_a <= 0 or side_b <= 0 or side_c <= 0:
        return "Invalid"

    # Check triangle inequality theorem
    if side_a + side_b <= side_c or side_a + side_c <= side_b or side_b + side_c <= side_a:
        return "Invalid"

    # Check for equilateral triangle
    if side_a == side_b == side_c:
        return "Equilateral"

    # Determine if isosceles or scalene
    if side_a == side_b or side_b == side_c or side_a == side_c:
        triangle_type = "Isosceles"
    else:
        triangle_type = "Scalene"

    # Check for right triangle using Pythagorean theorem
    sides = sorted([side_a, side_b, side_c])
    if sides[0] ** 2 + sides[1] ** 2 == sides[2] ** 2:
        triangle_type = f"Right {triangle_type}"

    return triangle_type
