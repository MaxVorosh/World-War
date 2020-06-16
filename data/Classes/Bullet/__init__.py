import pygame
from ..Border import Border


def load(name, colorkey=None):
    image = pygame.image.load(name).convert()
    if colorkey is not None:
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


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
