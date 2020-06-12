import pygame
from ..Aviation import Aviation


class Bomber(Aviation):
    def __init__(self, im_name, x, y, target):
        self.target = pygame.sprite.Group()
        self.target.add(target)
        super().__init__(im_name, x, y)
        self.v = 10

    def is_win(self):
        return pygame.sprite.spritecollideany(self, self.target)

    def update(self):
        super().update(self.v * self.last[0], self.v * self.last[1])
