import pygame
import sys
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


class Aviation(pygame.sprite.Sprite):
    def __init__(self, im_name, x, y):
        super().__init__()
        self.image = pygame.transform.scale(load("data\\Sprites\\" + im_name + ".png", colorkey=(255, 255, 255)),
                                            (80, 80))
        self.im_name = im_name
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.hp = 1
        self.last = (0, 1)
        self.mask = pygame.mask.from_surface(self.image)
        self.borders = pygame.sprite.Group()
        coords = [(0, 0, 560, 0), (0, 0, 0, 560), (0, 560, 560, 560), (560, 0, 560, 560)]
        for i in range(4):
            self.borders.add(Border(*coords[i]))

    def update(self, add_x, add_y):
        if self.last == (0, 1):
            self.image = pygame.transform.scale(
                load("data\\Sprites\\" + self.im_name + "_d.png", colorkey=(255, 255, 255)),
                (80, 80))
        elif self.last == (0, -1):
            self.image = pygame.transform.scale(
                load("data\\Sprites\\" + self.im_name + ".png", colorkey=(255, 255, 255)),
                (80, 80))
        elif self.last == (1, 0):
            self.image = pygame.transform.scale(
                load("data\\Sprites\\" + self.im_name + "_r.png", colorkey=(255, 255, 255)),
                (80, 80))
        else:
            self.image = pygame.transform.scale(
                load("data\\Sprites\\" + self.im_name + "_l.png", colorkey=(255, 255, 255)),
                (80, 80))
        self.rect.x += add_x
        self.rect.y += add_y
        if pygame.sprite.spritecollideany(self, self.borders):
            self.rect.x -= add_x
            self.rect.y -= add_y
        if self.hp == 0:
            self.kill()
