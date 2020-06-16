import pygame
from ..Enemy import Enemy


class Artillery(Enemy):
    def __init__(self, attach, x, y, im_name, cell_size, is_axis, hp):
        super().__init__(attach, 2, 1.5, x, y, im_name, cell_size, is_axis, hp)

    def attach(self, other, board, defence, path, k):
        if defence[other.y][other.y]:
            other.hp -= int(self.strength * k // 2)
        else:
            other.hp -= int(self.strength * k)
        other.strength = other.hp // 3
        if other.hp <= 0:
            other.kill()

    def can_attach(self, x, y, board, path):
        return abs(self.x - x) + abs(self.y - y) <= self.attach_range
