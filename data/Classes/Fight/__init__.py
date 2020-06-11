import pygame
import sys
from ..Level import make_fon, make_fon_2
from ..Tile import Tile
from ..Fighter import Fighter
from ..Bomber import Bomber
from random import randint
from ..Bullet import Bullet


class Fight:
    def __init__(self, text, right_text, land, is_fighter, is_axis):
        pygame.init()
        self.text = text
        self.right_text = right_text
        self.screen = pygame.display.set_mode((640, 640))
        self.height = 7
        self.width = 7
        self.all_sprites = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()
        for i in range(self.height):
            for j in range(self.width):
                if land == 'W':
                    self.all_sprites.add(Tile(j, i, 80, 'Вода'))
                if land == 'L':
                    self.all_sprites.add(Tile(j, i, 80, 'Поле'))
                if land == 'F':
                    self.all_sprites.add(Tile(j, i, 80, 'Лес'))
                if land == 'M':
                    self.all_sprites.add(Tile(j, i, 80, 'Гора'))
                if land == 'C':
                    self.all_sprites.add(Tile(j, i, 80, 'Город'))
                if land == 'T':
                    self.all_sprites.add(Tile(j, i, 80, 'Деревня'))
        self.running = True
        self.target = Tile(randint(0, 2), randint(0, 2), 80, 'Target')
        self.all_sprites.add(self.target)
        self.is_fighter = is_fighter
        if is_fighter:
            if is_axis:
                bom = Bomber('axis_bom', randint(320, 479), randint(320, 479), self.target)
                self.other = bom
                fig = Fighter('allies_fig', randint(1, 160), randint(1, 160), self.other, self.bullets)
                self.hero = fig
            else:
                bom = Bomber('allies_bom', randint(320, 479), randint(320, 479), self.target)
                self.other = bom
                fig = Fighter('axis_fig', randint(1, 160), randint(1, 160), self.other, self.bullets)
                self.hero = fig
        else:
            if is_axis:
                bom = Bomber('axis_bom', randint(320, 479), randint(320, 479), self.target)
                self.hero = bom
                fig = Fighter('allies_fig', randint(1, 160), randint(1, 160), self.other, self.bullets)
                self.other = fig
            else:
                bom = Bomber('allies_bom', randint(320, 479), randint(320, 479), self.target)
                self.hero = bom
                fig = Fighter('axis_fig', randint(1, 160), randint(1, 160), self.other, self.bullets)
                self.other = fig
        self.all_sprites.add(fig)
        self.all_sprites.add(bom)
        self.run()

    def run(self):
        fps = 30
        clock = pygame.time.Clock()
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.exitFunc()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP or event.key == pygame.K_w:
                        self.hero.last = (0, -1)
                    if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                        self.hero.last = (0, 1)
                    if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                        self.hero.last = (-1, 0)
                    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                        self.hero.last = (1, 0)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1 and self.is_fighter:
                        self.hero.attach()
            self.hero.update()
            self.screen.fill((0, 0, 0))
            for i in self.bullets:
                i.update()
            make_fon(self.screen, self.text)
            make_fon_2(self.screen, self.right_text)
            self.all_sprites.draw(self.screen)
            self.bullets.draw(self.screen)
            clock.tick(fps)
            pygame.display.flip()

    def exitFunc(self):
        pygame.quit()
        sys.exit()
