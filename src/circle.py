from point import Point
from vector import Vector


class Circle:
    def __init__(self, position: Point, radius: float, velocity: Vector,
                 acceleration: Vector):
        self.position = position
        self.radius = radius
        self.velocity = velocity
        self.acceleration = acceleration

    def update_state_kinematic(self, time):
        dis_x = self.velocity.x*time+(0.5*self.acceleration.x*(time**2))
        dis_y = self.velocity.y*time+(0.5*self.acceleration.y*(time**2))

        self.pos.x += dis_x
        self.pos.y += dis_y

    def create_lom_equation(self):
        '''
        Note here, I need to try to understand what I need from this 'Line'
        Do I want to draw it? Or just use it for calculations.
        Since we decided to use the Line class to draw an object.

        So lets make the LOM an object of the Line class.
        The problem with that is, we do not have 2 points
        '''
        pass
