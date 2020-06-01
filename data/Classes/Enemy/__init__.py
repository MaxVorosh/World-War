import pygame


def load(name, colorkey=None):
    image = pygame.image.load(name).convert()
    if colorkey is not None:
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


class Enemy(pygame.sprite.Sprite):
    def __init__(self, attach, attach_range, move_range, x, y, im_name, cell_size, is_axis, hp):
        super().__init__()
        self.image = pygame.transform.scale(load("data\\Sprites\\" + im_name + ".png", colorkey=(255, 255, 255)),
                                            (cell_size, cell_size))
        self.strength = attach
        self.attach_range = attach_range
        self.move_range = move_range
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        self.cell_size = cell_size
        self.rect.x = x * cell_size
        self.rect.y = y * cell_size
        self.is_axis = is_axis
        self.hp = hp
        self.is_moved = False

    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y
        self.rect.x = self.x * self.cell_size
        self.rect.y = self.y * self.cell_size

    def go_to(self, turns, x, y, need_x, need_y, k, board):
        if x == need_x and y == need_y:
            return True
        if turns == 0 or (not 0 <= x < 7) or (not 0 <= y < 7) or (board[y][x] is not None and board[y][x] != self):
            return False
        return (self.go_to(turns - k, x + 1, y, need_x, need_y, k, board)
                or self.go_to(turns - k, x - 1, y, need_x, need_y, k, board)
                or self.go_to(turns - k, x, y + 1, need_x, need_y, k, board)
                or self.go_to(turns - k, x, y - 1, need_x, need_y, k, board))

    def attach(self, other, board):
        turns = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for i in turns:
            if (0 <= other.x + i[0] < 7 and
                    board[other.y + i[1]][other.x + i[0]] is None and
                    0 <= other.y < 7 and
                    self.go_to(self.move_range, self.x, self.y, other.x + i[0], other.y + i[1], 1, board)):
                self.move(other.x + i[0], other.y + i[1])
                break
        other.hp -= self.strength
        other.strength = other.hp // 3
        if other.hp <= 0:
            other.kill()
        else:
            self.hp -= other.strength
            self.strength = self.hp // 3
            if self.hp <= 0:
                self.kill()

    def can_attach(self, x, y, board):
        return self.go_to(self.attach_range + self.move_range - 1, self.x, self.y, x, y, 1, board)
