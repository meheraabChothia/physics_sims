from point import Point
# from vector import Vector
from paramteric_line import ParametricLine


class Line:
    def __init__(self, point1: Point, point2: Point, thickness: float):
        self.point1 = point1
        self.point2 = point2
        self.thickness = thickness
        self.vector = self.point2-self.point1

    def initialise_equation(self):
        # Using Parametric equations for this case.
        self.eq = ParametricLine(self.point1, self.vector)
