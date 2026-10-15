from vector import Vector
from typing import Self


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __sub__(self, point: Self):
        v_x = self.x-point.x
        v_y = self.y-point.y
        # Distance can be calculated using the magnitude of the
        # resulting vector
        return Vector(v_x, v_y)

    def __str__(self):
        return f"Point({self.x},{self.y})"


if __name__ == "__main__":
    point1 = Point(1, 1)
    point2 = Point(0, 0)
    print(point1-point2)
