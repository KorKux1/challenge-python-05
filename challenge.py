import math


def square_area(side):
    """Returns the area of a square"""
    # You have to code here
    # REMEMBER: Tests first!!!
    pass


def rectangle_area(base, height):
    """Returns the area of a rectangle"""
    # You have to code here
    # REMEMBER: Tests first!!!
    pass


def triangle_area(base, height):
    """Returns the area of a triangle"""
    # You have to code here
    # REMEMBER: Tests first!!!
    pass


def rhombus_area(diagonal_1, diagonal_2):
    """Returns the area of a rhombus"""
    # You have to code here
    # REMEMBER: Tests first!!!
    pass


def trapezoid_area(base_minor, base_major, height):
    """Returns the area of a trapezoid"""
    # You have to code here
    # REMEMBER: Tests first!!!
    pass


def regular_polygon_area(perimeter, apothem):
    """Returns the area of a regular polygon"""
    # You have to code here
    # REMEMBER: Tests first!!!
    pass


def circumference_area(radius):
    """Returns the area of a circumference"""
    # You have to code here
    # REMEMBER: Tests first!!!
    # Use math.pi for π value
    pass


if __name__ == '__main__':
    import unittest

    class GeometrySuite(unittest.TestCase):

        def setUp(self):
            self.values = {
                'side': 0,
                'base': 0,
                'height': 0,
                'diagonal_1': 0,
                'diagonal_2': 0,
                'base_minor': 0,
                'base_major': 0,
                'perimeter': 0,
                'apothem': 0,
                'radius': 0
            }

        def test_square_area(self):
            """Test the function to find the area of a square with a side greater than zero"""
            self.assertEqual(0, square_area(self.values['side']))

        def test_rectangle_area(self):
            """Test the function to find the area of a rectangle with height and base greater than zero"""
            self.assertEqual(0, rectangle_area(self.values['base'], self.values['height']))

        def test_triangle_area(self):
            """Test the function to find the area of a triangle with height and base greater than zero"""
            self.assertEqual(0, triangle_area(self.values['base'], self.values['height']))

        def test_rhombus_area(self):
            """Test the function to find the area of a rhombus with diagonals greater than zero"""
            self.assertEqual(0, rhombus_area(self.values['diagonal_1'], self.values['diagonal_2']))

        def test_trapezoid_area(self):
            """Test the function to find the area of a rhombus with bases greater than zero and height greater than zero"""
            self.assertEqual(0, trapezoid_area(self.values['base_minor'], self.values['base_major'], self.values['height']))

        def test_regular_polygon_area(self):
            """Test the function to find the area of a polygon with apothem and perimeter greater than zero"""
            self.assertEqual(0, regular_polygon_area(self.values['perimeter'], self.values['apothem']))


        def test_circumference_area(self):
            """Test the function to find the area of a circle with radius greater than zero"""
            self.assertEqual(0, circumference_area(self.values['radius']))

        def tearDown(self):
            del(self.values)

    unittest.main()
