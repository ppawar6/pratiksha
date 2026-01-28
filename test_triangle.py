
from triangle import classify_triangle
import pytest

def test_equilateral_triangle():
    assert classify_triangle(3, 3, 3) == "Equilateral"


def test_isosceles_triangle():
    assert classify_triangle(5, 5, 8) == "Isosceles"


def test_scalene_triangle():
    assert classify_triangle(4, 5, 6) == "Scalene"


def test_right_scalene_triangle():
    assert classify_triangle(3, 4, 5) == "Right Scalene"



def test_invalid_triangle_negative_side():
    assert classify_triangle(-1, 2, 3) == "Invalid"


def test_invalid_triangle_zero_side():
    assert classify_triangle(0, 4, 5) == "Invalid"


def test_invalid_triangle_violates_triangle_inequality():
    assert classify_triangle(1, 2, 10) == "Invalid"

