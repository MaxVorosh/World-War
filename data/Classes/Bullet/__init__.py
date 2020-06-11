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
        self.target_group = pygame.sprite.Group()
        self.target_group.add(target)
        self.route = last
        self.v = 15
        self.borders = pygame.sprite.Group()
        coords = [(0, 0, 560, 0), (0, 0, 0, 560), (0, 560, 560, 560), (560, 0, 560, 560)]
        for i in range(4):
            self.borders.add(Border(*coords[i]))

    def update(self):
        self.rect.x += self.v * self.route[0]
        self.rect.y += self.v * self.route[1]
        if pygame.sprite.spritecollideany(self, self.borders):
            self.kill()
        else:
            if pygame.sprite.spritecollideany(self, self.target_group):
                self.target.hp = 0
                self.kill()
