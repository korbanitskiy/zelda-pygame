import pygame

from settings import WORLD_MAP, TILESIZE
from tile import Tile
from player import Player

from debug import debug


class Level:

    def __init__(self) -> None:
        self.display_surface = pygame.display.get_surface()
        self.visible_sprites = pygame.sprite.Group()
        self.obstacle_sprites = pygame.sprite.Group()
        self.create_map()

    def create_map(self):
        for row_idx, row in enumerate(WORLD_MAP):
            for col_idx, col in enumerate(row):
                x = col_idx * TILESIZE
                y = row_idx * TILESIZE

                if col == "x":
                    Tile((x, y), [self.visible_sprites, self.obstacle_sprites])

                if col == "p":
                    self.player = Player((x, y), [self.visible_sprites])

    def run(self):
        self.visible_sprites.draw(self.display_surface)
        self.visible_sprites.update()
        debug(self.player.direction)
