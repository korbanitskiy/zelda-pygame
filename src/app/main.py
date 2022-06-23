import sys

import pygame
from settings import SCREEN_MODE, FPS
from level import Level


def run_game():
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_MODE)
    pygame.display.set_caption('Zelda')
    clock = pygame.time.Clock()
    level = Level()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill('black')
        level.run()
        pygame.display.update()
        clock.tick(FPS)


if __name__ == '__main__':
    run_game()
