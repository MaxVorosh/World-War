import  pygame
from ..Enemy import Enemy


class Transport(Enemy):
    def __init__(self, attach, x, y, im_name, cell_size, is_axis, hp):
        super().__init__(attach, 0, 0, x, y, im_name, cell_size, is_axis, hp)
