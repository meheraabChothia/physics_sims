from point import Point
from vector import Vector
from line import Line


class Wall:
    def __init__(self, width, height):
        self.left_wall = Line(Point(0, 0), Point(0, height))

        self.right_wall = Line(Point(width, 0), Point(width, height))

        self.top_wall = Line(Point(0, height), Point(width, height))

        self.bottom_wall = Line(Point(0, 0), Point(width, 0))
