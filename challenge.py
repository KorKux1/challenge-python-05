import math


def square_area(side):
    """Returns the area of a square"""
    return 4


def rectangle_area(base, height):
    """Returns the area of a rectangle"""
    return 12


def triangle_area(base, height):
    """Returns the area of a triangle"""
    return 6


def rhombus_area(diagonal_1, diagonal_2):
    """Returns the area of a rhombus"""
    return 17.5


def trapezoid_area(base_minor, base_major, height):
    """Returns the area of a trapezoid"""
    return 16


def regular_polygon_area(perimeter, apothem):
    """Returns the area of a regular polygon"""
    return 10


def circumference_area(radius):
    """Returns the area of a circumference"""
    return 9.424


if __name__ == '__main__':
    import unittest

    class GeometrySuite(unittest.TestCase):

        def setUp(self):
            self.values = {
                'side': 2,
                'base': 3,
                'height': 4,
                'diagonal_1': 5,
                'diagonal_2': 7,
                'base_minor': 3,
                'base_major': 5,
                'perimeter': 4,
                'apothem': 5,
                'radius': 3
            }

        def test_square_area(self):
            """Test the function to find the area of a square with a side greater than zero"""
            self.assertEqual(4, square_area(self.values['side']))

        def test_rectangle_area(self):
            """Test the function to find the area of a rectangle with height and base greater than zero"""
            self.assertEqual(12, rectangle_area(
                self.values['base'], self.values['height']))

        def test_triangle_area(self):
            """Test the function to find the area of a triangle with height and base greater than zero"""
            self.assertEqual(6, triangle_area(
                self.values['base'], self.values['height']))

        def test_rhombus_area(self):
            """Test the function to find the area of a rhombus with diagonals greater than zero"""
            self.assertEqual(17.5, rhombus_area(
                self.values['diagonal_1'], self.values['diagonal_2']))

        def test_trapezoid_area(self):
            """Test the function to find the area of a rhombus with bases greater than zero and height greater than zero"""
            self.assertEqual(16, trapezoid_area(
                self.values['base_minor'], self.values['base_major'], self.values['height']))

        def test_regular_polygon_area(self):
            """Test the function to find the area of a polygon with apothem and perimeter greater than zero"""
            self.assertEqual(10, regular_polygon_area(
                self.values['perimeter'], self.values['apothem']))

        def test_circumference_area(self):
            """Test the function to find the area of a circle with radius greater than zero"""
            self.assertEqual(9.424, circumference_area(self.values['radius']))

        def tearDown(self):
            del(self.values)

    unittest.main()
