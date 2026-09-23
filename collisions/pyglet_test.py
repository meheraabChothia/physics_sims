import pyglet

window = pyglet.window.Window()

batch = pyglet.graphics.Batch()


def update(dt, object):
    for obj in object:
        obj.update_state(dt)
        # input()


@window.event
def on_draw():
    window.clear()
    batch.draw()


class Circle:
    def __init__(self, v_x, v_y, i_x, i_y):
        self.velocity = {"x": v_x, "y": v_y}
        self.acceleration = {"x": 0, "y": 0}
        self._obj_details(i_x, i_y)
        self.create_object()

    def _obj_details(self, i_x, i_y):
        self.pos = {"x": i_x, "y": i_y}
        self.radius = 4

    def create_object(self):
        self.obj = pyglet.shapes.Circle(
            x=self.pos['x'], y=self.pos['y'], radius=self.radius,
            color=(255, 255, 255), batch=batch)

    def update_state(self, dt):
        dis_x = self.velocity['x']*dt+(0.5*self.acceleration['x']*(dt**2))
        dis_y = self.velocity['y']*dt+(0.5*self.acceleration['y']*(dt**2))

        '''
        For now we gonna update both the self.pos arg and the circle coords
        Will figure something else out later on.
        '''

        self.pos['x'] += dis_x
        self.pos['y'] += dis_y
        self.obj.x += dis_x
        self.obj.y += dis_y


def main():
    object = []
    circle = Circle(100, 60, 200, 200)
    circle2 = Circle(10, 10, 250, 250)

    object.append(circle)
    object.append(circle2)

    pyglet.clock.schedule_interval(update, 1/120, object)

    pyglet.app.run()


if __name__ == "__main__":
    main()
