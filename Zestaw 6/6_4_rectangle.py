from points import Point
import unittest

class Rectangle:
    """Klasa reprezentująca prostokąt na płaszczyźnie."""

    def __init__(self, x1, y1, x2, y2):
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)

    def __str__(self):
        return "[({}, {}), ({}, {})]".format(self.pt1.x, self.pt1.y, self.pt2.x, self.pt2.y)

    def __repr__(self):
        return "Rectangle({}, {}, {}, {})".format(self.pt1.x, self.pt1.y, self.pt2.x, self.pt2.y)

    def __eq__(self, other):
        return self.pt1 == other.pt1 and self.pt2 == other.pt2

    def __ne__(self, other):
        return not self == other

    def center(self):
        return Point((self.pt1.x + self.pt2.x) / 2, (self.pt1.y + self.pt2.y) / 2)

    def area(self):
        return abs((self.pt2.x - self.pt1.x) * (self.pt2.y - self.pt1.y))

    def move(self, x, y):
        self.pt1.x += x
        self.pt2.x += x
        self.pt1.y += y
        self.pt2.y += y

class TestRectangle(unittest.TestCase):
    def test_str(self):
        rect = Rectangle(1, 2, 3, 4)
        print(f"Test str: {str(rect)}")
        self.assertEqual(str(rect), "[(1, 2), (3, 4)]")

    def test_repr(self):
        rect = Rectangle(1, 2, 3, 4)
        print(f"Test repr: {repr(rect)}")
        self.assertEqual(repr(rect), "Rectangle(1, 2, 3, 4)")

        def test_eq(self):
        rect1 = Rectangle(1, 2, 3, 4)
        rect2 = Rectangle(1, 2, 3, 4)
        rect3 = Rectangle(0, 5, 2, 2)

    def test_center(self):
        rect = Rectangle(1, 2, 5, 6)
        print(f"Test center: {rect.center()}")
        self.assertEqual(rect.center(), Point(3.0, 4.0))

    def test_area(self):
        rect = Rectangle(1, 2, 5, 6)
        print(f"Test area: {rect.area()}")
        self.assertEqual(rect.area(), 16)

    def test_move(self):
        rect = Rectangle(1, 2, 3, 4)
        rect.move(2, 5)
        print(f"Test move: {str(rect)}")
        self.assertEqual(rect.pt1, Point(3, 7))
        self.assertEqual(rect.pt2, Point(5, 9))

if __name__ == '__main__':
    unittest.main()
