import pygame

G = 9.81


class Circle:
    def __init__(self):
        self.mass = None
        self.initial_vel_x = 0
        self.initial_vel_y = 0
        self.acceleration = G
        self.force_vectors = {'x': 0, 'y': -1}

    def calculate_position(self, time: float):
        displacement_y = (self.initial_vel_y*time)+0.5 * \
            self.acceleration*self.force_vectors['y']*(time**2)

        self.initial_vel_y = self.initial_vel_y + \
            self.acceleration*self.force_vectors['y']*time

        displacement_x = (self.initial_vel_x*time)+0.5 * \
            self.acceleration*self.force_vectors['x']*(time**2)

        self.initial_vel_x = self.initial_vel_x + \
            self.acceleration*self.force_vectors['x']*time

        return [displacement_x, displacement_y]


class ScreenManager:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1920, 1080))
        self.clock = pygame.time.Clock()
        self.running = True
        self.dt = 0

    def create_n_circles(self, n=3):
        """
        For now creating circles with set positions.
        """
        self.objects = []
        for i in range(n):
            self.objects.append([Circle(), pygame.Vector2(
                self.screen.get_width()/2-((i+1)*20), 10)])

    def create_circle(self):
        self.circle = Circle()
        self.circle_coords = pygame.Vector2(self.screen.get_width()/2, 10)

    def draw_circle(self):
        # pygame.draw.circle(self.screen, 'white', self.circle_coords, 5)
        for i in self.objects:
            pygame.draw.circle(self.screen, 'white', i[1], 5)

    def set_screen(self):
        self.screen.fill('black')

    def movements(self):
        for object in self.objects:
            displacement = object[0].calculate_position(self.dt)
            print(displacement)
            object[1].x += displacement[0]
            object[1].y -= displacement[1]


def main():
    sm = ScreenManager()
    sm.create_n_circles()
    while sm.running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sm.running = False

        sm.set_screen()
        sm.draw_circle()
        pygame.display.flip()
        sm.dt = sm.clock.tick(60)/1000

        # sm.movements()
        for object in sm.objects:
            print(object)
            displacement = object[0].calculate_position(sm.dt)
            print(displacement)
            object[1].x += displacement[0]
            object[1].y -= displacement[1]

    pygame.quit()


if __name__ == "__main__":
    main()
