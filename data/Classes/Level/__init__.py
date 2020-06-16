import pygame
from ..Tile import Tile
from ..Infanitry import Infanitry
from ..Artilery import Artillery
from ..Tancs import Tancs
import sys
from ..Goodbye import Goodbye
from ..Badbye import Badbye
from ..Submarine import Submarine
from ..Transport import Transport
from ..Battleship import Battleship
from ..Destroyer import Destroyer
from random import randint
from ..Fight import Fight
from ..Intro import Intro


def upndown(let):
    if let == 'U':
        return 150
    if let == 'M':
        return 100
    return 50


def load(name, colorkey=None):
    image = pygame.image.load(name).convert()
    if colorkey is not None:
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


def make_fon(screen, intro_text):
    font = pygame.font.Font(None, 30)
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('white'))
        intro_rect = string_rendered.get_rect()
        text_coord = 560 + 40 - string_rendered.get_height() // 2
        intro_rect.top = text_coord
        intro_rect.x = screen.get_width() // 2 - string_rendered.get_width() // 2 - 40
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)


def make_fon_2(screen, intro_text):
    font = pygame.font.Font(None, 30)
    text_coord = 300
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('white'))
        intro_rect = string_rendered.get_rect()
        intro_rect.top = text_coord
        intro_rect.x = 600 - string_rendered.get_width() // 2
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)


class Level:
    def __init__(self, music_name, title, is_axis, window_number, need_turns, desc):
        pygame.init()
        pygame.mixer.music.load("data\\Music\\" + music_name + ".mp3")
        pygame.mixer.music.set_volume(0.05)
        pygame.mixer.music.play()
        self.screen = pygame.display.set_mode((640, 640))
        self.is_clicked = False
        self.left = 0
        self.top = 0
        self.turns = 1
        self.title = title
        self.description = desc
        self.cell_size = 80
        self.window_number = window_number
        self.need_turns = need_turns
        self.width = 7
        self.height = 7
        self.text, self.text_r = '', ''
        self.last_x = None
        self.last_y = None
        self.can_move = []
        self.can_attach = []
        self.is_axis = is_axis
        self.board = [[None for j in range(self.height)] for i in range(self.width)]
        self.defence = [[False for j in range(self.height)] for i in range(self.width)]
        self.path = [[100 for j in range(self.height + 1)] for i in range(self.width + 1)]
        self.all_sprites = pygame.sprite.Group()
        self.techs_sprites = pygame.sprite.Group()
        next_turn_button = pygame.sprite.Sprite()
        next_turn_button.image = pygame.transform.scale(load("data\\Sprites\\next.png"),
                                                        (self.cell_size, self.cell_size))
        next_turn_button.rect = next_turn_button.image.get_rect()
        next_turn_button.rect.x = self.width * self.cell_size
        next_turn_button.rect.y = self.height * self.cell_size
        go_to_last_button = pygame.sprite.Sprite()
        go_to_last_button.image = pygame.transform.scale(load("data\\Sprites\\Last_1.png"),
                                                         (self.cell_size, self.cell_size))
        go_to_last_button.rect = go_to_last_button.image.get_rect()
        go_to_last_button.rect.y = 0
        go_to_last_button.rect.x = self.height * self.cell_size
        self.all_sprites.add(next_turn_button)
        self.all_sprites.add(go_to_last_button)
        f = open("data\\Maps\\Land\\" + title + ".txt")
        data_land = [i.split() for i in f.readlines()]
        self.data_land = data_land
        f = open("data\\Maps\\Army\\" + title + ".txt")
        data_army = [i.split() for i in f.readlines()]
        for i in range(self.height):
            for j in range(self.width):
                if data_land[i][j] == 'WW':
                    self.all_sprites.add(Tile(j, i, 80, 'Вода'))
                    self.path[i][j] = 7
                if data_land[i][j] == 'LL':
                    self.all_sprites.add(Tile(j, i, 80, 'Поле'))
                    self.path[i][j] = 1
                if data_land[i][j] == 'FF':
                    self.all_sprites.add(Tile(j, i, 80, 'Лес'))
                    self.path[i][j] = 1.5
                if data_land[i][j] == 'MM':
                    self.all_sprites.add(Tile(j, i, 80, 'Гора'))
                if data_land[i][j] == 'CC':
                    self.all_sprites.add(Tile(j, i, 80, 'Город'))
                    self.path[i][j] = 1.5
                if data_land[i][j] == 'TT':
                    self.all_sprites.add(Tile(j, i, 80, 'Деревня'))
                    self.path[i][j] = 1
                if data_land[i][j][1] == 'D':
                    self.path[i][j] = 1.5
                    self.defence[i][j] = True
                    if data_land[i][j] == 'LD':
                        self.all_sprites.add(Tile(j, i, 80, 'Поле_укреп'))
                    if data_land[i][j] == 'FD':
                        self.all_sprites.add(Tile(j, i, 80, 'Лес_укреп'))
                    if data_land[i][j] == 'CD':
                        self.all_sprites.add(Tile(j, i, 80, 'Город_укреп'))
                    if data_land[i][j] == 'TD':
                        self.all_sprites.add(Tile(j, i, 80, 'Деревня_укреп'))
        for i in range(len(data_army)):
            for j in range(len(data_army[i])):
                strength = upndown(data_army[i][j][1])
                enem = None
                if data_army[i][j][0] == 'I':
                    if data_army[i][j][2] == 'L':
                        enem = Infanitry(strength // 3, j, i, 'allies_inf_1', 80, False, strength)
                    else:
                        enem = Infanitry(strength // 3, j, i, 'axis_inf_1', 80, True, strength)
                if data_army[i][j][0] == 'P':
                    if data_army[i][j][2] == 'L':
                        enem = Tancs(strength // 3, j, i, 'allies_tan_1', 80, False, strength)
                    else:
                        enem = Tancs(strength // 3, j, i, 'axis_tan_1', 80, True, strength)
                if data_army[i][j][0] == 'A':
                    if data_army[i][j][2] == 'L':
                        enem = Artillery(strength // 3, j, i, 'allies_art_1', 80, False, strength)
                    else:
                        enem = Artillery(strength // 3, j, i, 'axis_art_1', 80, True, strength)
                if data_army[i][j][0] == 'W':
                    if data_army[i][j][2] == 'L':
                        enem = Submarine(strength // 3, j, i, 'allies_sub_1', 80, False, strength)
                    else:
                        enem = Submarine(strength // 3, j, i, 'axis_sub_1', 80, True, strength)
                if data_army[i][j][0] == 'T':
                    if data_army[i][j][2] == 'L':
                        enem = Transport(strength // 3, j, i, 'allies_tra_1', 80, False, strength)
                    else:
                        enem = Transport(strength // 3, j, i, 'axis_tra_1', 80, True, strength)
                if data_army[i][j][0] == 'D':
                    if data_army[i][j][2] == 'L':
                        enem = Destroyer(strength // 3, j, i, 'allies_des_1', 80, False, strength)
                    else:
                        enem = Destroyer(strength // 3, j, i, 'axis_des_1', 80, True, strength)
                if data_army[i][j][0] == 'B':
                    if data_army[i][j][2] == 'L':
                        enem = Battleship(strength // 3, j, i, 'allies_bat_1', 80, False, strength)
                    else:
                        enem = Battleship(strength // 3, j, i, 'axis_bat_1', 80, True, strength)
                if enem is not None:
                    self.techs_sprites.add(enem)
                self.board[i][j] = enem
        n = int(data_land[self.height][0])
        self.key_positions = [(int(data_land[self.height + 1 + i][0]), int(data_land[self.height + 1 + i][1])) for i in
                              range(n)]
        self.is_visited = {i: False for i in self.key_positions}
        self.run()

    def run(self):
        self.running = True
        win = 0
        while self.running:
            self.text_r = ['Ход ', str(self.turns), '/', str(self.need_turns)]
            self.text = [self.title + ' - ' + self.description]
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.exitFunc()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.get_click(event.pos)
                    if event.pos[0] > self.width * self.cell_size and event.pos[1] > self.height * self.cell_size:
                        self.next_turn()
                    if event.pos[1] < self.cell_size and event.pos[0] > self.height * self.cell_size:
                        self.go_to_last()
            self.screen.fill((0, 0, 0))
            make_fon(self.screen, self.text)
            make_fon_2(self.screen, self.text_r)
            self.all_sprites.draw(self.screen)
            self.techs_sprites.draw(self.screen)
            if self.turns > self.need_turns:
                self.running = False
                win = 1
            for i in range(self.width):
                for j in range(self.height):
                    if self.board[i][j] is not None:
                        self.draw_number(i, j)
            for i in self.key_positions:
                pygame.draw.circle(self.screen, pygame.Color('yellow'),
                                   (self.cell_size * i[0] + self.cell_size // 2,
                                    self.cell_size * i[1] + self.cell_size // 2), 15)
                if self.board[i[1]][i[0]] is not None:
                    if self.board[i[1]][i[0]].is_axis == self.is_axis:
                        self.is_visited[i] = True
                    else:
                        self.is_visited[i] = False
            if all(self.is_visited.values()):
                self.running = False
                win = 2
            if self.is_clicked:
                pygame.draw.circle(self.screen, pygame.Color('green'),
                                   (self.cell_size * self.last_x + self.cell_size // 2,
                                    self.cell_size * self.last_y + self.cell_size // 2), 10)
            for i in self.can_move:
                pygame.draw.circle(self.screen, pygame.Color('blue'),
                                   (self.cell_size * i[0] + self.cell_size // 2,
                                    self.cell_size * i[1] + self.cell_size // 2), 10)
            for i in self.can_attach:
                pygame.draw.circle(self.screen, pygame.Color('red'),
                                   (self.cell_size * i[0] + self.cell_size // 2,
                                    self.cell_size * i[1] + self.cell_size // 2), 10)
            pygame.display.flip()
        if win == 2:
            Goodbye(self.window_number, self.turns, self.screen)
        elif win == 1:
            Badbye(self.window_number, self.screen)

    def exitFunc(self):
        pygame.quit()
        sys.exit()

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        if cell is None:
            return None
        self.on_click(cell)

    def get_cell(self, pos):
        x, y = pos
        if x > self.width * self.cell_size + self.left or y > self.height * self.cell_size + self.top or x < self.left or y < self.top:
            return None
        ans = (x - self.left) // self.cell_size, (y - self.top) // self.cell_size
        return ans

    def on_click(self, cell):
        if self.is_clicked:
            self.is_clicked = False
            if cell in self.can_move:
                self.board[self.last_y][self.last_x].is_moved = True
                self.board[self.last_y][self.last_x].move(cell[0], cell[1])
                self.board[self.last_y][self.last_x], self.board[cell[1]][cell[0]] = self.board[cell[1]][cell[0]], \
                                                                                     self.board[self.last_y][
                                                                                         self.last_x]
                self.can_move = []
                self.can_attach = []
            elif cell in self.can_attach:
                self.board[self.last_y][self.last_x].is_moved = True
                enem = self.board[self.last_y][self.last_x]
                a = randint(0, 10)
                k = 1
                if a == 0:
                    t = randint(0, 1)
                    if t == 0:
                        Intro(['Ваша задача - разбомбить цель', 'Для этого подлетите к указанной цели',
                               'Остерегайтесь пуль вражеского истребителя',
                               'От Вашего результата зависит урон, нанесённый Вами',
                               'Изначально Вы находитесь в левом нижнем углу'])
                        tile = self.data_land[cell[1]][cell[0]]
                    else:
                        Intro(['Ваша задача - подбить вражеский бомбардировщик',
                               'Для этого стреляйте по нему, с помощью ЛКМ',
                               'От вашего результата зависит урон, нанесённый Вами',
                               'Изначально Вы находитесь в правом верхнем углу'])
                        tile = self.data_land[enem.y][enem.x]
                    f = Fight(self.text, self.text_r, tile[0], t, self.is_axis)
                    k = f.run()
                enem.attach(self.board[cell[1]][cell[0]], self.board, self.defence, self.path, k)
                x = enem.x
                y = enem.y
                self.board[self.last_y][self.last_x], self.board[y][x] = self.board[y][x], self.board[self.last_y][
                    self.last_x]
                self.can_move = []
                self.can_attach = []
                if enem.hp <= 0:
                    self.board[y][x] = None
                if self.board[cell[1]][cell[0]].hp <= 0:
                    self.board[cell[1]][cell[0]] = None
            else:
                self.can_move = []
                self.can_attach = []
        else:
            if (self.board[cell[1]][cell[0]] is not None and self.board[cell[1]][cell[0]].is_axis == self.is_axis and
                    not self.board[cell[1]][cell[0]].is_moved):
                self.is_clicked = True
                self.last_x = cell[0]
                self.last_y = cell[1]
                for i in range(self.last_y - 3, self.last_y + 4):
                    if self.height > i >= 0:
                        for j in range(self.last_x - 3, self.last_x + 4):
                            if self.width > j >= 0 and not (i == self.last_y and j == self.last_x):
                                if self.board[i][j] is None:
                                    if self.board[cell[1]][cell[0]].go_to(self.board[cell[1]][cell[0]].move_range,
                                                                          self.board[cell[1]][cell[0]].x,
                                                                          self.board[cell[1]][cell[0]].y, j, i,
                                                                          self.board, self.path):
                                        self.can_move.append((j, i))
                                elif self.board[i][j].is_axis != self.board[cell[1]][cell[0]].is_axis:
                                    if self.board[cell[1]][cell[0]].can_attach(j, i, self.board, self.path):
                                        self.can_attach.append((j, i))

    def next_turn(self):
        for sprite in self.techs_sprites:
            minim = None
            min_hp = 10000
            sprite.is_moved = False
            if sprite.is_axis != self.is_axis and (sprite.x, sprite.y) in self.key_positions:
                turns = [(1, 0), (-1, 0), (0, 1), (0, -1)]
                for i in turns:
                    if 0 <= sprite.x + i[0] < 7 and 0 <= sprite.y + i[1] < 7:
                        if (self.board[sprite.y + i[1]][sprite.x + i[0]] is not None and
                                self.board[sprite.y + i[1]][sprite.x + i[0]].is_axis != sprite.is_axis):
                            if self.board[sprite.y + i[1]][sprite.x + i[0]].hp < min_hp:
                                minim = self.board[sprite.y + i[1]][sprite.x + i[0]]
                                min_hp = minim.hp
            else:
                is_moved = False
                if sprite.is_axis != self.is_axis:
                    for i in self.key_positions:
                        if self.is_visited[i] and sprite.go_to(sprite.move_range, sprite.x, sprite.y, i[0], i[1],
                                                               self.board, self.path):
                            if self.board[i[1]][i[0]] is None:
                                self.board[sprite.y][sprite.x], self.board[i[1]][i[0]] = self.board[i[1]][i[0]], \
                                                                                         self.board[sprite.y][sprite.x]
                                sprite.move(i[0], i[1])
                            else:
                                x = sprite.x
                                y = sprite.y
                                a = randint(0, 10)
                                k = 1
                                if sprite.__class__.__name__ != 'Transport':
                                    if a == 0:
                                        t = randint(0, 1)
                                        if t == 0:
                                            Intro(['Ваша задача - разбомбить цель', 'Для этого подлетите к указанной цели',
                                                   'Остерегайтесь пуль вражеского истребителя',
                                                   'От Вашего результата зависит урон, нанесённый по Вам',
                                                   'Изначально Вы находитесь в левом нижнем углу'])
                                            tile = self.data_land[i[1]][i[0]]
                                        else:
                                            Intro(['Ваша задача - подбить вражеский бомбардировщик',
                                                   'Для этого стреляйте по нему, с помощью ЛКМ',
                                                   'От вашего результата зависит урон, нанесённый по Вам',
                                                   'Изначально Вы находитесь в правом верхнем углу'])
                                            tile = self.data_land[y][x]
                                        f = Fight(self.text, self.text_r, tile[0], t, self.is_axis)
                                        k = 1 / f.run()
                                sprite.attach(self.board[i[1]][i[0]], self.board, self.defence, self.path, k)
                                self.board[y][x], self.board[sprite.y][sprite.x] = self.board[sprite.y][sprite.x], \
                                                                                   self.board[y][x]
                                if sprite.hp <= 0:
                                    self.board[sprite.y][sprite.x] = None
                                if self.board[i[1]][i[0]].hp <= 0:
                                    self.board[i[1]][i[0]] = None
                            is_moved = True
                            break
                    if is_moved:
                        continue
                if sprite.is_axis != self.is_axis:
                    for i in range(sprite.y - 3, sprite.y + 4):
                        if self.height > i >= 0:
                            for j in range(sprite.x - 3, sprite.x + 4):
                                if self.width > j >= 0 and not (i == sprite.y and j == sprite.x):
                                    if self.board[i][j] is not None and self.board[i][j].is_axis == self.is_axis:
                                        if self.board[sprite.y][sprite.x].can_attach(j, i, self.board, self.path):
                                            if self.board[i][j].hp < min_hp:
                                                minim = self.board[i][j]
                                                min_hp = minim.hp
            if minim is not None:
                x = sprite.x
                y = sprite.y
                a = randint(0, 10)
                k = 1
                if sprite.__class__.__name__ != 'Transport':
                    if a == 0:
                        t = randint(0, 1)
                        if t == 0:
                            Intro(['Ваша задача - разбомбить цель', 'Для этого подлетите к указанной цели',
                                   'Остерегайтесь пуль вражеского истребителя',
                                   'От Вашего результата зависит урон, нанесённый по Вам',
                                   'Изначально Вы находитесь в левом нижнем углу'])
                            tile = self.data_land[minim.y][minim.x]
                        else:
                            Intro(['Ваша задача - подбить вражеский бомбардировщик',
                                   'Для этого стреляйте по нему, с помощью ЛКМ',
                                   'От вашего результата зависит урон, нанесённый по Вам',
                                   'Изначально Вы находитесь в правом верхнем углу'])
                            tile = self.data_land[y][x]
                        f = Fight(self.text, self.text_r, tile[0], t, self.is_axis)
                        k = 1 / f.run()
                sprite.attach(minim, self.board, self.defence, self.path, k)
                self.board[y][x], self.board[sprite.y][sprite.x] = self.board[sprite.y][sprite.x], self.board[y][x]
                if self.board[sprite.y][sprite.x].hp <= 0:
                    self.board[sprite.y][sprite.x] = None
                if self.board[minim.y][minim.x].hp <= 0:
                    self.board[minim.y][minim.x] = None
        self.turns += 1

    def draw_number(self, i, j):
        font = pygame.font.Font(None, self.cell_size // 2)
        text = font.render(str(self.board[i][j].hp), 0, pygame.Color('red'))
        text_x = self.left + self.cell_size * j
        text_y = self.top + self.cell_size * i
        self.screen.blit(text, (text_x, text_y))

    def go_to_last(self):
        self.running = False
