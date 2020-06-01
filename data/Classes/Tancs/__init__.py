import pygame
from ..Enemy import Enemy


def load(name, colorkey=None):
    image = pygame.image.load(name).convert()
    if colorkey is not None:
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


class Tancs(Enemy):
    def __init__(self, attach, x, y, im_name, cell_size, is_axis, hp):
        super().__init__(attach, 1, 3, x, y, im_name, cell_size, is_axis, hp)
        self.image = pygame.transform.scale(load("data\\Sprites\\" + im_name + ".png", colorkey=(255, 255, 255)),
                                            (cell_size, cell_size // 2))
        self.rect.y = cell_size // 4 + cell_size * y

    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y
        self.rect.x = self.x * self.cell_size
        self.rect.y = self.y * self.cell_size + self.cell_size // 4
