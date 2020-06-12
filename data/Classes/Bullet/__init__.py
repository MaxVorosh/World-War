import pygame
from ..Level import load
from ..Border import Border


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, target, last, group):
        super().__init__(group)
        self.image = self.image = pygame.transform.scale(load("data\\Sprites\\bullet.png", colorkey=(255, 255, 255)),
                                                         (5, 5))
        # print(target)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.target = target
        self.route = last
        self.mask = pygame.mask.from_surface(self.image)
        self.v = 15

    def update(self):
        self.rect.x += self.v * self.route[0]
        self.rect.y += self.v * self.route[1]
        if not(0 <= self.rect.x < 560 and 0 <= self.rect.y < 560):
            self.kill()
        else:
            if pygame.sprite.collide_mask(self, self.target):
                self.target.hp = 0
                self.kill()
