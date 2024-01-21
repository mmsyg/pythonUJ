import math
import unittest
from points import Point

class Circle:

    def __init__(self, x, y, radius):
        if radius < 0:
            raise ValueError("Negative radius")
        self.pt = Point(x, y)
        self.radius = radius

    def __repr__(self):
        return f"Circle({self.pt.x}, {self.pt.y}, {self.radius})"

    def __eq__(self, other):
        return self.pt == other.pt and self.radius == other.radius

    def __ne__(self, other):
        return not self.__eq__(other)

    def area(self):
        return math.pi * self.radius ** 2

    def move(self, x, y):
        if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
            raise ValueError("Non-numeric coordinates")
        self.pt.x += x
        self.pt.y += y

    def cover(self, other):
        distance = math.hypot(self.pt.x - other.pt.x, self.pt.y - other.pt.y)
        new_radius = (self.radius + other.radius + distance) / 2
        new_x = (self.pt.x + other.pt.x) / 2
        new_y = (self.pt.y + other.pt.y) / 2
        return Circle(new_x, new_y, new_radius)

class TestCircle(unittest.TestCase):
    def setUp(self):
        self.circle1 = Circle(1, 1, 2)
        self.circle2 = Circle(2, 2, 3)
        self.circle3 = Circle(3, 3, 4)
        self.circle4 = Circle(3, 3, 4)

    def test_init(self):
        with self.assertRaises(ValueError):
            Circle(0, 1, -2)

    def test_repr(self):
        self.assertEqual(repr(self.circle1), "Circle(1, 1, 2)")
        self.assertEqual(repr(self.circle2), "Circle(2, 2, 3)")
        self.assertEqual(repr(self.circle3), "Circle(3, 3, 4)")

    def test_eq(self):
        self.assertNotEqual(self.circle1, self.circle2)
        self.assertEqual(self.circle3, self.circle4)

    def test_area(self):
        self.assertAlmostEqual(self.circle1.area(), 12.566370614359172)
        self.assertAlmostEqual(self.circle2.area(), 28.274333882308138)
        self.assertAlmostEqual(self.circle3.area(), 50.26548245743669)

    def test_move(self):
        self.circle1.move(1, 1)
        self.assertEqual(self.circle1.pt, Point(2, 2))
        self.circle2.move(-1, -1)
        self.assertEqual(self.circle2.pt, Point(1, 1))
        with self.assertRaises(ValueError):
            self.circle3.move('a', 'b')

    def test_cover(self):
        covered_circle = self.circle3.cover(self.circle4)
        self.assertEqual(covered_circle, Circle(3, 3, 4))

if __name__ == "__main__":
    unittest.main()
