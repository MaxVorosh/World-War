import pygame


class Tile(pygame.sprite.Sprite):
    def __init__(self, x, y, cell_size, name):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load("data\\Sprites\\" + name + ".png"),
                                            (cell_size, cell_size))
        self.rect = self.image.get_rect()
        self.rect.x = x * cell_size
        self.rect.y = y * cell_size
        self.name = name
