from points import Point
import math

class Circle:
    def __init__(self, x, y, radius):
        if radius < 0:
            raise ValueError("Negative radius is not allowed")
        self.center = Point(x, y)
        self.radius = radius

    def __repr__(self):
        return f"Circle({self.center.x}, {self.center.y}, {self.radius})"

    def __eq__(self, other):
        if not isinstance(other, Circle):
            return NotImplemented
        return self.center == other.center and self.radius == other.radius

    def area(self):
        return math.pi * self.radius ** 2

    def move(self, dx, dy):
        self.center.move(dx, dy)

    def cover(self, other):
        if not isinstance(other, Circle):
            raise TypeError("Argument must be a Circle")

        dx, dy = self.center.x - other.center.x, self.center.y - other.center.y
        distance = math.hypot(dx, dy)
        new_radius = (self.radius + other.radius + distance) / 2
        alpha = self.radius / new_radius
        beta = other.radius / new_radius


        new_center_x = alpha * self.center.x + beta * other.center.x
        new_center_y = alpha * self.center.y + beta * other.center.y

        return Circle(new_center_x, new_center_y, new_radius)

    @classmethod
    def from_points(cls, points):
        if len(points) != 3:
            raise ValueError("Exactly three points are required")

        if Point.are_collinear(*points):
            raise ValueError("Points are collinear, cannot form a circle")

        x1, y1 = points[0].x, points[0].y
        x2, y2 = points[1].x, points[1].y
        x3, y3 = points[2].x, points[2].y

        A = Point.determinant(x1, y1, x2, y2, x3, y3)
        D = -Point.determinant(x1 ** 2 + y1 ** 2, y1, x2 ** 2 + y2 ** 2, y2, x3 ** 2 + y3 ** 2, y3)
        E = Point.determinant(x1 ** 2 + y1 ** 2, x1, x2 ** 2 + y2 ** 2, x2, x3 ** 2 + y3 ** 2, x3)
        F = -Point.determinant(x1 ** 2 + y1 ** 2, x1, y1, x2 ** 2 + y2 ** 2, x2, y2, x3 ** 2 + y3 ** 2, x3, y3)

        center_x, center_y = -D / (2 * A), -E / (2 * A)
        radius = math.sqrt(D ** 2 + E ** 2 - 4 * A * F) / abs(2 * A)


        return cls(center_x, center_y, radius)

    @property
    def top(self):
        return self.center.y + self.radius

    @property
    def bottom(self):
        return self.center.y - self.radius

    @property
    def left(self):
        return self.center.x - self.radius

    @property
    def right(self):
        return self.center.x + self.radius

    @property
    def diameter(self):
        return 2 * self.radius

    def bounding_box(self):
        return self.left, self.top, self.right, self.bottom
