from point import Point
from vector import Vector
from typing import Self


class ParametricLine:
    '''
    This is not a line object in and of itself,
    this is just a class that will help represent and draw lines.
    So this will worry more about the calculations behind the line
    like solving equations, etc.

    So ideally every object that will have to have a line represented
    will use this class.
    Meanwhile the Line class will be used to just represent a line 'object'.
    Emphasis on the object. This is more about the calculations and
    representation of lines.
    Line is more about just representing the manifestation of this calculations

    Thought process behing this is a WIP

    '''

    def __init__(self, point: Point, vector: Vector):
        self.point = point
        self.vector = vector

    def print_equation(self):
        print(f"x = {self.p.x} + t{self.d.x}")
        print(f"y = {self.p.y} + t{self.d.y}")

    def solve_equations(self, other_line: Self):
        a1 = self.vector.x
        b1 = -1*other_line.d.x
        c1 = other_line.point.x-self.point.x

        a2 = self.vector.y
        b2 = -1*other_line.d.y
        c2 = other_line.point.y-self.point.y

        # D = a1b2 - a2b1
        # Dx = c1b2 - c2-b1
        # Dy = a1c2 - a2c1

        det = a1*b2 - a2*b1
        if det == 0:
            return False

        det_t = c1*b2 - c2*b1
        # det_s = a1*c2 - a2*c1

        t = det_t/det
        # s = det_s/det

        # Now subbing the values of t and s into the equations to get a point
        x = self.point.x+self.vector.x*t
        y = self.point.y+self.vector.y*t
        return (Point(x, y))
