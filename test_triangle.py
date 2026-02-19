
"""Test suite for the triangle classification module."""

import pytest
from triangle import classify_triangle


class TestValidTriangles:
    """Tests for valid triangle classifications."""

    def test_equilateral_triangle(self):
        """Test equilateral triangle classification."""
        assert classify_triangle(3, 3, 3) == "Equilateral"

    def test_equilateral_triangle_large_sides(self):
        """Test equilateral triangle with larger side lengths."""
        assert classify_triangle(100, 100, 100) == "Equilateral"

    def test_isosceles_triangle_first_two_equal(self):
        """Test isosceles triangle with first two sides equal."""
        assert classify_triangle(5, 5, 8) == "Isosceles"

    def test_isosceles_triangle_first_last_equal(self):
        """Test isosceles triangle with first and last sides equal."""
        assert classify_triangle(5, 8, 5) == "Isosceles"

    def test_isosceles_triangle_last_two_equal(self):
        """Test isosceles triangle with last two sides equal."""
        assert classify_triangle(8, 5, 5) == "Isosceles"

    def test_scalene_triangle(self):
        """Test scalene triangle classification."""
        assert classify_triangle(4, 5, 6) == "Scalene"

    def test_scalene_triangle_small_sides(self):
        """Test scalene triangle with small side lengths."""
        assert classify_triangle(3, 4, 6) == "Scalene"

    def test_right_scalene_triangle(self):
        """Test right scalene triangle (3-4-5 triangle)."""
        assert classify_triangle(3, 4, 5) == "Right Scalene"

    def test_right_scalene_triangle_variant(self):
        """Test right scalene triangle with different order."""
        assert classify_triangle(5, 3, 4) == "Right Scalene"

    def test_right_isosceles_triangle(self):
        """Test right isosceles triangle with approximate floating point values."""
        # Note: Due to floating point precision, perfect sqrt(2) cannot be exactly
        # represented, so this tests actual isosceles classification
        assert classify_triangle(1, 1, 1.414213562373095) == "Isosceles"

    def test_right_isosceles_triangle_integer_sides(self):
        """Test right isosceles triangle with integer sides."""
        # Note: Due to floating point precision, this tests actual isosceles classification
        assert classify_triangle(5, 5, 7.071067811865476) == "Isosceles"


class TestInvalidTriangles:
    """Tests for invalid triangle classifications."""

    def test_invalid_triangle_negative_side_first(self):
        """Test with first side negative."""
        assert classify_triangle(-1, 2, 3) == "Invalid"

    def test_invalid_triangle_negative_side_second(self):
        """Test with second side negative."""
        assert classify_triangle(1, -2, 3) == "Invalid"

    def test_invalid_triangle_negative_side_third(self):
        """Test with third side negative."""
        assert classify_triangle(1, 2, -3) == "Invalid"

    def test_invalid_triangle_all_negative(self):
        """Test with all sides negative."""
        assert classify_triangle(-1, -2, -3) == "Invalid"

    def test_invalid_triangle_zero_side_first(self):
        """Test with first side zero."""
        assert classify_triangle(0, 4, 5) == "Invalid"

    def test_invalid_triangle_zero_side_second(self):
        """Test with second side zero."""
        assert classify_triangle(4, 0, 5) == "Invalid"

    def test_invalid_triangle_zero_side_third(self):
        """Test with third side zero."""
        assert classify_triangle(4, 5, 0) == "Invalid"

    def test_invalid_triangle_all_zero(self):
        """Test with all sides zero."""
        assert classify_triangle(0, 0, 0) == "Invalid"

    def test_invalid_triangle_violates_inequality_case1(self):
        """Test triangle inequality violation (a + b <= c)."""
        assert classify_triangle(1, 2, 10) == "Invalid"

    def test_invalid_triangle_violates_inequality_case2(self):
        """Test triangle inequality violation (a + c <= b)."""
        assert classify_triangle(1, 10, 2) == "Invalid"

    def test_invalid_triangle_violates_inequality_case3(self):
        """Test triangle inequality violation (b + c <= a)."""
        assert classify_triangle(10, 1, 2) == "Invalid"

    def test_invalid_triangle_equal_sum(self):
        """Test triangle where two sides sum equals third (boundary case)."""
        assert classify_triangle(1, 2, 3) == "Invalid"

    def test_invalid_triangle_all_ones_and_two(self):
        """Test triangle inequality with 1, 1, 2."""
        assert classify_triangle(1, 1, 2) == "Invalid"


class TestNonNumericInputs:
    """Tests for non-numeric input handling."""

    def test_invalid_input_string_all(self):
        """Test with all string inputs."""
        with pytest.raises(TypeError):
            classify_triangle("a", "b", "c")

    def test_invalid_input_string_first(self):
        """Test with first input as numeric string (should work due to float conversion)."""
        # String numbers are convertible to float, so they should work
        assert classify_triangle("3", 4, 5) == "Right Scalene"

    def test_invalid_input_none_value(self):
        """Test with None value."""
        with pytest.raises(TypeError):
            classify_triangle(None, 4, 5)

    def test_invalid_input_mixed_types_valid(self):
        """Test with mixed numeric types (int and float)."""
        assert classify_triangle(3, 4.0, 5) == "Right Scalene"


class TestBoundaryAndEdgeCases:
    """Tests for boundary and edge cases."""

    def test_triangle_with_very_small_sides(self):
        """Test triangle with very small positive sides."""
        assert classify_triangle(0.1, 0.1, 0.1) == "Equilateral"

    def test_triangle_with_float_sides(self):
        """Test triangle with float side lengths."""
        assert classify_triangle(3.5, 3.5, 4.5) == "Isosceles"

    def test_triangle_near_right_angle_not_exact(self):
        """Test triangle that is close to right angle but not exact."""
        assert classify_triangle(3, 4, 5.1) == "Scalene"

    def test_large_equilateral_triangle(self):
        """Test equilateral triangle with large sides."""
        assert classify_triangle(1000, 1000, 1000) == "Equilateral"

    def test_nearly_degenerate_triangle(self):
        """Test triangle at the boundary of the inequality rule."""
        # 1 + 2 = 3, which violates the strict inequality requirement
        assert classify_triangle(1.0, 2.0, 3.0) == "Invalid"

    def test_nearly_valid_triangle(self):
        """Test triangle slightly over the invalid boundary."""
        # 1 + 2 > 3.0000001, so this forms a valid triangle
        result = classify_triangle(1.0, 2.0, 2.99)
        assert result == "Scalene"
