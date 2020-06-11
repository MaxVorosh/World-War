import pygame


def load(name, colorkey=None):
    image = pygame.image.load(name).convert()
    if colorkey is not None:
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


class Tile(pygame.sprite.Sprite):
    def __init__(self, x, y, cell_size, name):
        super().__init__()
        self.image = pygame.transform.scale(load("data\\Sprites\\" + name + ".png", colorkey=(255, 255, 255)),
                                            (cell_size, cell_size))
        self.rect = self.image.get_rect()
        self.rect.x = x * cell_size
        self.rect.y = y * cell_size
        self.name = name
