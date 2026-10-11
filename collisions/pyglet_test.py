import pyglet
from typing import Self
# from __future__ import annotations

window = pyglet.window.Window()
WIDTH = window.width
HEIGHT = window.height
LINE_COLOR = (255, 255, 255)

batch = pyglet.graphics.Batch()


def update(dt, object):
    for obj in object:
        obj.update_state(dt)
        obj.calculate_lom()
        # input()


@window.event
def on_draw():
    window.clear()
    batch.draw()


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Line:
    def __init__(self, point1: Point, point2: Point, thickness=2):
        self.p1 = point1
        self.p2 = point2
        self.thickness = thickness
        self.create_object()
        self.calculate_equation()

    def create_object(self):
        self.obj = pyglet.shapes.Line(
            x=self.p1.x, y=self.p1.y,
            x2=self.p2.x, y2=self.p2.y,
            thickness=self.thickness, color=LINE_COLOR, batch=batch)

    def calculate_equation(self):
        temp_vector = Vector(self.p2.x-self.p1.x, self.p2.y-self.p1.y)
        self.eq = ParamtericLine(self.p1, temp_vector)


class oldWall:
    def __init__(self):
        self.left_wall = ParamtericLine(Point(0, 0), Vector(0, 1))
        self.right_wall = ParamtericLine(
            Point(WIDTH, 0), Vector(0, 1))

        self.top_wall = ParamtericLine(Point(0, HEIGHT), Vector(1, 0))
        self.bottom_wall = ParamtericLine(Point(0, 0), Vector(1, 0))
        self.create_walls()

    def create_walls(self):
        pass


class Wall:
    def __init__(self):
        self.left_wall = Line(Point(0, 0), Point(0, HEIGHT))

        self.right_wall = Line(Point(WIDTH, 0), Point(WIDTH, HEIGHT))

        self.top_wall = Line(Point(0, HEIGHT), Point(WIDTH, HEIGHT))

        self.bottom_wall = Line(Point(0, 0), Point(WIDTH, 0))


class ParamtericLine:
    def __init__(self, point: Point, vector: Vector):
        self.p = point
        self.d = vector

    def solve_equations(self, other_line: Self) -> Point:
        '''
        Should take an equation as an input.
        Should then solve it with the current object instance.
        Should return a point.

        Will try to sovle this using Cramer's Rule

        Assuming the line equaitons to look something like this:
        x=x0+t(dx0)=x1+s(dx1)
        y=y0+t(dy0)=y1+s(dy1)
        '''
        # First calculating t and s
        a1 = self.d.x
        b1 = -1*other_line.d.x
        c1 = other_line.p.x-self.p.x

        a2 = self.d.y
        b2 = -1*other_line.d.y
        c2 = other_line.p.y-self.p.y

        # D = a1b2 - a2b1
        # Dx = c1b2 - c2-b1
        # Dy = a1c2 - a2c1

        det = a1*b2 - a2*b1
        if det == 0:
            print('why solve parallel lines stupid??\nNot sure if this is why problem')
            # Need to stop the rest of the funciton here and return an appropriate
            # message to the main loop.
        det_t = c1*b2 - c2*b1
        # det_s = a1*c2 - a2*c1

        t = det_t/det
        # s = det_s/det

        # Now subbing the values of t and s into the equations to get a point
        x = self.p.x+self.d.x*t
        y = self.p.y+self.d.y*t

        return (Point(x, y))

    def print_equation(self):
        print(f"x = {self.p.x} + t{self.d.x}")
        print(f"y = {self.p.y} + t{self.d.y}")


class Circle:
    def __init__(self, v_x, v_y, i_x, i_y):
        self.pos = {}
        self.radius = 0
        self.velocity = Vector(v_x, v_y)
        self.acceleration = Vector(0, 0)
        self._obj_details(i_x, i_y)
        self.create_object()
        self.calculate_lom()

    def _obj_details(self, i_x, i_y):
        self.pos = Point(i_x, i_y)
        self.radius = 10

    def create_object(self):
        self.obj = pyglet.shapes.Circle(
            x=self.pos.x, y=self.pos.y, radius=self.radius,
            color=(255, 255, 255), batch=batch)

    def update_state(self, dt):
        dis_x = self.velocity.x*dt+(0.5*self.acceleration.x*(dt**2))
        dis_y = self.velocity.y*dt+(0.5*self.acceleration.y*(dt**2))

        '''
        For now we gonna update both the self.pos arg and the circle coords
        Will figure something else out later on.
        '''

        self.pos.x += dis_x
        self.pos.y += dis_y
        self.obj.x += dis_x
        self.obj.y += dis_y

    def calculate_lom(self):
        self.eq = ParamtericLine(self.pos, self.velocity)


def main():
    object = []
    circle = Circle(-50, 50, 500, 200)
    circle2 = Circle(-50, 50, WIDTH-500, 200)

    object.append(circle)
    object.append(circle2)

    walls = Wall()
    lines = []
    lines.append(walls.left_wall)
    lines.append(walls.right_wall)
    lines.append(walls.top_wall)
    lines.append(walls.bottom_wall)
    lines.append(circle.eq)
    lines.append(circle2.eq)
    # circle.calculate_lom()
    # circle2.calculate_lom()
    #
    for i in lines:
        i.eq.print_equation()

    pyglet.clock.schedule_interval(update, 1/120, object)

    pyglet.app.run()


if __name__ == "__main__":
    main()
