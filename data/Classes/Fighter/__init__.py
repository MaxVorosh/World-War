import pygame
from ..Aviation import Aviation
from ..Bullet import Bullet


class Fighter(Aviation):
    def __init__(self, im_name, x, y, other_sprite, bul_group):
        super().__init__(im_name, x, y)
        self.other = other_sprite
        self.bul_group = bul_group
        self.v = 11

    def is_win(self):
        return self.other.hp == 0 and not self.other.is_win()

    def attach(self):
        if self.last == (0, 1):
            bul_1 = Bullet(self.rect.x + 10, self.rect.y + 70, self.other, self.last,
                           self.bul_group)
            bul_2 = Bullet(self.rect.x + 70, self.rect.y + 70, self.other, self.last,
                           self.bul_group)
        elif self.last == (0, -1):
            bul_1 = Bullet(self.rect.x + 10, self.rect.y + 10, self.other, self.last,
                           self.bul_group)
            bul_2 = Bullet(self.rect.x + 70, self.rect.y + 10, self.other, self.last,
                           self.bul_group)
        elif self.last == (1, 0):
            bul_1 = Bullet(self.rect.x + 70, self.rect.y + 10, self.other, self.last,
                           self.bul_group)
            bul_2 = Bullet(self.rect.x + 70, self.rect.y + 70, self.other, self.last,
                           self.bul_group)
        else:
            bul_1 = Bullet(self.rect.x + 10, self.rect.y + 10, self.other, self.last,
                           self.bul_group)
            bul_2 = Bullet(self.rect.x + 10, self.rect.y + 70, self.other, self.last,
                           self.bul_group)
        self.bul_group.add(bul_1)
        self.bul_group.add(bul_2)

    def update(self):
        super().update(self.v * self.last[0], self.v * self.last[1])
