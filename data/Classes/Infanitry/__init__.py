import pygame
from ..Enemy import Enemy


class Infanitry(Enemy):
    def __init__(self, attach, x, y, im_name, cell_size, is_axis, hp):
        super().__init__(attach, 1, 2, x, y, im_name, cell_size, is_axis, hp)
