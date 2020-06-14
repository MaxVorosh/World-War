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
                fig = Fighter('allies_fig', randint(1, 160), randint(1, 160), self.hero, self.bullets)
                self.other = fig
            else:
                bom = Bomber('allies_bom', randint(320, 479), randint(320, 479), self.target)
                self.hero = bom
                fig = Fighter('axis_fig', randint(1, 160), randint(1, 160), self.hero, self.bullets)
                self.other = fig
        self.all_sprites.add(bom)
        self.all_sprites.add(fig)

    def run(self):
        fps = 60
        clock = pygame.time.Clock()
        k = 1
        t = 0
        while self.running:
            t += 1
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
            if t == 5:
                self.other_turn()
                t = 0
            self.hero.update()
            if t != 0:
                self.other.update()
            self.screen.fill((0, 0, 0))
            for i in self.bullets:
                i.update()
            if self.hero.is_win():
                k = 1.5
                self.running = False
            if self.other.is_win():
                k = 0.6
                self.running = False
            make_fon(self.screen, self.text)
            make_fon_2(self.screen, self.right_text)
            self.all_sprites.draw(self.screen)
            self.bullets.draw(self.screen)
            clock.tick(fps)
            pygame.display.flip()
        return k

    def other_turn(self):
        if self.is_fighter:
            x = self.other.rect.x
            y = self.other.rect.y
            lasts = [(-1, 0), (0, -1), (1, 0), (0, 1)]
            if self.target.rect.x + 80 <= self.other.rect.x:
                lasts[0] = (-1, 0)
                lasts[2] = (1, 0)
                if self.target.rect.y + 80 <= self.other.rect.y:
                    lasts[1] = (0, -1)
                    lasts[3] = (0, 1)
                else:
                    lasts[1] = (0, 1)
                    lasts[3] = (0, -1)
            elif self.target.rect.x > self.other.rect.x:
                lasts[2] = (-1, 0)
                lasts[0] = (1, 0)
                if self.target.rect.y + 80 <= self.other.rect.y:
                    lasts[1] = (0, -1)
                    lasts[3] = (0, 1)
                else:
                    lasts[1] = (0, 1)
                    lasts[3] = (0, -1)
            else:
                lasts[1] = (-1, 0)
                lasts[3] = (1, 0)
                if self.target.rect.y + 80 <= self.other.rect.y:
                    lasts[0] = (0, -1)
                    lasts[2] = (0, 1)
                else:
                    lasts[0] = (0, 1)
                    lasts[2] = (0, -1)
            for i in lasts:
                self.other.last = i
                self.other.rect.x = x
                self.other.rect.y = y
                fl = True
                for j in range(10):
                    self.other.rect.x += self.other.v * i[0]
                    self.other.rect.y += self.other.v * i[1]
                    new_bullet = pygame.sprite.Group()
                    for bul in self.bullets:
                        Bullet(bul.rect.x + bul.v * i[0], bul.rect.y + bul.v * i[1], bul.target, bul.route, new_bullet)
                    if pygame.sprite.spritecollideany(self.other, new_bullet):
                        fl = False
                        break
                if fl:
                    break
            self.other.rect.x = x
            self.other.rect.y = y
            self.other.update()
        else:
            if self.hero.rect.x + 80 <= self.other.rect.x:
                self.other.last = (-1, 0)
            elif self.hero.rect.y + 80 <= self.other.rect.y:
                self.other.last = (0, -1)
            elif self.hero.rect.x >= self.other.rect.x + 80:
                self.other.last = (1, 0)
            else:
                self.other.last = (0, 1)
            self.other.update()
            if self.other.rect.x - 70 <= self.hero.rect.x <= self.other.rect.x - 10 or self.other.rect.y - 70 <= self.hero.rect.y <= self.other.rect.y - 10:
                self.other.attach()

    def exitFunc(self):
        pygame.quit()
        sys.exit()
