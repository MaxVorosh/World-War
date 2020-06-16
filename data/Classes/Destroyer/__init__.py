import  pygame
from ..Enemy import Enemy, load


class Destroyer(Enemy):
    def __init__(self, attach, x, y, im_name, cell_size, is_axis, hp):
        super().__init__(attach, 1, 14, x, y, im_name, cell_size, is_axis, hp)
        self.image = pygame.transform.scale(load("data\\Sprites\\" + im_name + ".png", colorkey=(255, 255, 255)),
                                            (cell_size, cell_size // 2))
        self.rect.y = cell_size // 4 + cell_size * y

    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y
        self.rect.x = self.x * self.cell_size
        self.rect.y = self.y * self.cell_size + self.cell_size // 4

    def attach(self, other, board, defence, path, k):
        turns = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for i in turns:
            if (0 <= other.x + i[0] < 7 and
                    0 <= other.y + i[1] < 7 and
                    board[other.y + i[1]][other.x + i[0]] is None and
                    self.go_to(self.move_range - 1, self.x, self.y, other.x + i[0], other.y + i[1], board, path)):
                self.move(other.x + i[0], other.y + i[1])
                break
        strength = self.strength * k
        if other.__class__.__name__ == 'Submarine':
            strength = int(strength * 1.5)
        elif other.__class__.__name__ == 'Battleship':
            strength = int(strength * 0.75)
        if defence[other.y][other.x]:
            other.hp -= int(strength // 2)
        else:
            other.hp -= int(strength)
        other.strength = other.hp // 3
        if other.hp <= 0:
            other.kill()
        else:
            strength = other.strength / k
            if other.__class__.__name__ == 'Submarine':
                strength = int(strength * 1.5)
            elif other.__class__.__name__== 'Battleship':
                strength = int(strength * 0.75)
            elif other.__class__.__name__ == 'Transport':
                strength = 0
            if defence[self.y][self.x]:
                self.hp -= int(strength // 2)
            else:
                self.hp -= int(strength)
            self.strength = self.hp // 3
            if self.hp <= 0:
                self.kill()
