import pygame
from ..Aviation import Aviation
from ..Bullet import Bullet


class Fighter(Aviation):
    def __init__(self, im_name, x, y, other_sprite, bul_group):
        super().__init__(im_name, x, y)
        self.other = other_sprite
        self.bul_group = bul_group
        self.v = 10

    def is_win(self):
        return self.other.hp == 0

    def attach(self):
        bul_1 = Bullet(self.rect.x + 5 * self.last[0], self.rect.y + 5 * self.last[1], self.other, self.last,
                       self.bul_group)
        bul_2 = Bullet(self.rect.x - 5 * self.last[0], self.rect.y - 5 * self.last[1], self.other, self.last,
                       self.bul_group)
        self.bul_group.add(bul_1)
        self.bul_group.add(bul_2)

    def update(self):
        super().update(self.v * self.last[0], self.v * self.last[1])
