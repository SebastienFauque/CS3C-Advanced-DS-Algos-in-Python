import pytest
from sebastienfauqueLab2 import pascals_triangle

def test_pascals_triangle_1():
    """asserts that output is correct for basecase."""
    assert pascals_triangle(1) == [1]

def test_pascals_triangle_2():
    """asserts that the output is correct for n = 2."""
    assert pascals_triangle(2) == [1, 1]

def test_pascals_triangle_3():
    """asserts that the output is correct for n = 3."""
    assert pascals_triangle(3) == [1, 2, 1]

def test_pascals_triangle_4():
    """asserts that the output is correct for n = 4."""
    assert pascals_triangle(4) == [1, 3, 3, 1]

def test_pascals_triangle_5():
    """asserts that the output is correct for n = 5."""
    assert pascals_triangle(5) == [1, 4, 6, 4, 1]

def test_pascals_triangle_6():
    """asserts that the output is correct for n = 6."""
    assert pascals_triangle(6) == [1, 5, 10, 10, 5, 1]
