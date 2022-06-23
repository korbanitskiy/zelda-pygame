import pygame
from pygame.sprite import Sprite


class Tile(Sprite):

    def __init__(self, pos, groups) -> None:
        super().__init__(groups)
        self.image = pygame.image.load("static/graphics/test/rock.png").convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
