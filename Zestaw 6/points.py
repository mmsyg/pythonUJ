import unittest

class Point:
    """Klasa reprezentująca punkty na płaszczyźnie."""

    def __init__(self, x, y):  # konstuktor
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return not self == other

    # Punkty jako wektory 2D.
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return self.x * other.x + self.y * other.y

    def cross(self, other):
        return self.x * other.y - self.y * other.x

    def length(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def __hash__(self):
        return hash((self.x, self.y))  # bazujemy na tuple, immutable points

class TestPoint(unittest.TestCase):
    def test_str_representation(self):
        p = Point(3, 4)
        self.assertEqual(str(p), "(3, 4)")

    def test_repr_representation(self):
        p = Point(3, 4)
        self.assertEqual(repr(p), "Point(3, 4)")

    def test_equality(self):
        p1 = Point(3, 4)
        p2 = Point(3, 4)
        p3 = Point(5, 6)
        self.assertEqual(p1, p2)
        self.assertNotEqual(p1, p3)

    def test_addition(self):
        p1 = Point(3, 4)
        p2 = Point(1, 2)
        p3 = p1 + p2
        self.assertEqual(p3, Point(4, 6))

    def test_subtraction(self):
        p1 = Point(3, 4)
        p2 = Point(1, 2)
        p3 = p1 - p2
        self.assertEqual(p3, Point(2, 2))

    def test_dot_product(self):
        p1 = Point(3, 4)
        p2 = Point(1, 2)
        result = p1 * p2
        self.assertEqual(result, 11)

    def test_cross_product(self):
        p1 = Point(3, 4)
        p2 = Point(1, 2)
        result = p1.cross(p2)
        self.assertEqual(result, 2)

    def test_length(self):
        p = Point(3, 4)
        self.assertAlmostEqual(p.length(), 5.0)

    def test_hashing(self):
        p1 = Point(3, 4)
        p2 = Point(3, 4)
        point_set = {p1, p2}
        self.assertEqual(len(point_set), 1)

if __name__ == "__main__":
    unittest.main()
