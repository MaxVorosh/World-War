import pygame


class Border(pygame.sprite.Sprite):
    def __init__(self, x1, y1, x2, y2):
        super().__init__()
        if x1 == x2:
            self.rect = pygame.Rect(x1, y1, 1, y2 - y1)
        else:
            self.rect = pygame.Rect(x1, y1, x2 - x1, 1)
