import  pygame
from ..Enemy import Enemy, load


class Transport(Enemy):
    def __init__(self, attach, x, y, im_name, cell_size, is_axis, hp):
        super().__init__(attach, 0, 0, x, y, im_name, cell_size, is_axis, hp)
        if is_axis:
            self.image = pygame.transform.scale(load("data\\Sprites\\" + im_name + ".png", colorkey=(255, 255, 255)),
                                                (cell_size, cell_size // 2))
            self.rect.y = cell_size // 4 + cell_size * y

    def move(self, new_x, new_y):
        if self.is_axis:
            self.x = new_x
            self.y = new_y
            self.rect.x = self.x * self.cell_size
            self.rect.y = self.y * self.cell_size + self.cell_size // 4
        else:
            super().move(new_x, new_y)

    def can_attach(self, x, y, board, path):
        return False

    def attach(self, other, board, defence, path, k):
        pass
