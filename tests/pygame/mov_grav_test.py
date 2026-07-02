import pygame

G = 9.81


def calculate_position(time: float):
    # time in seconds
    dis = 0.5*G*(time**2)
    return dis  # How much of the 1000 meters it has fallen


def main():
    pygame.init()
    screen = pygame.display.set_mode((1920, 1080))
    clock = pygame.time.Clock()
    running = True
    dt = 0
    time = 0
    line_left = [0, screen.get_height()-100]
    line_right = [screen.get_width(), screen.get_height()-100]

    player_pos = pygame.Vector2(screen.get_width()/2, 0)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill('black')

        pygame.draw.circle(screen, 'white', player_pos, 5)
        pygame.draw.line(screen, 'white', line_left, line_right, 5)

        pygame.display.flip()
        if player_pos.y < screen.get_height()-110:
            print(player_pos.y)
            player_pos.y = calculate_position(time)
        dt = clock.tick(60)/1000
        print(f"dt = {dt}")
        time += dt
    pygame.quit()


if __name__ == '__main__':
    main()
