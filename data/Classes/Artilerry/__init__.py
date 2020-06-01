import pygame
from ..Enemy import Enemy


class Artillery(Enemy):
    def __init__(self, attach, x, y, im_name, cell_size, is_axis, hp):
        super().__init__(attach, 2, 1, x, y, im_name, cell_size, is_axis, hp)

    def attach(self, other):
        other.hp -= self.strength
        other.strength = other.hp // 3
        if other.hp <= 0:
            other.kill()
        else:
            self.hp -= other.strength
            self.strength = self.hp // 3
            if self.hp <= 0:
                self.kill()
