import pygame
import random
import math
import threading

BIAS = [0, -1]

MOVES = [
    [0, 0], [0, 1], [0, -1],
    [1, 0], [1, 1], [1, -1],
    [-1, 0], [-1, 1], [-1, -1],
    BIAS, BIAS, BIAS  # adding bias
]

MOUSE_POS = []


class ScreenManager:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1920, 1080))
        self.clock = pygame.time.Clock()
        self.running = True
        self.dt = 0

    def set_screen(self):
        # self.screen.fill('black')
        self.screen.fill('white')

    def movements(self):
        for object in self.objects:
            displacement = object[0].calculate_position(self.dt)
            print(displacement)
            object[1].x += displacement[0]
            object[1].y -= displacement[1]


class Walker:
    def __init__(self, screen):
        self.x = int(screen.get_width()/2)
        self.y = int(screen.get_height()/2)

    def calculate_position(self):
        self.x += random.randint(-1, 1)
        self.y += random.randint(-1, 1)

        print(self.x, self.y)
        return self.x, self.y

    def biased_move(self):

        choice = random.choice(MOVES)
        self.x += choice[0]
        self.y += choice[1]
        print(self.x, self.y)
        return self.x, self.y

    def mouse_move(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        movement_x = 0
        movement_y = 0
        print(self.x-mouse_x)
        print(self.y-mouse_y)
        if mouse_x != self.x:
            movement_x = (self.x-mouse_x)/abs(self.x-mouse_x)
        if mouse_y != self.y:
            movement_y = (self.y-mouse_y)/abs(self.y-mouse_y)
            print(movement_x, movement_y)
        self.x -= int(movement_x)
        self.y -= int(movement_y)
        return self.x, self.y

    def mouse_record_follow(self):
        mx = my = 0
        if (MOUSE_POS):
            mx, my = MOUSE_POS.pop(0)

        return (mx, my)


def mouse_recorder():
    while (True):
        mouse_pos = pygame.mouse.get_pos()
        if MOUSE_POS and mouse_pos != MOUSE_POS[-1]:
            MOUSE_POS.append(mouse_pos)
        elif not MOUSE_POS:
            MOUSE_POS.append(mouse_pos)


def walker_main():
    sm = ScreenManager()
    sm.set_screen()
    # thread = threading.Thread(target=mouse_recorder, daemon=True)
    # thread.start()
    wk = Walker(sm.screen)
    while sm.running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sm.running = False

        # sm.screen.set_at(wk.mouse_record_follow(), (255, 255, 255))
        sm.screen.set_at(wk.mouse_move(), (0, 0, 0))

        pygame.display.flip()
        sm.dt = sm.clock.tick(60)/1000

    pygame.quit()


if __name__ == "__main__":
    walker_main()
