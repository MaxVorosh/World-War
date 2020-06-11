import pygame
from ..Button import Button
from ..Window import Window
from ..Level import load
import sys


def make_fon(screen, intro_text):
    fon = pygame.transform.scale(load('data\\Sprites\\bg.jpg'),
                                 (screen.get_width(), screen.get_height()))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 30)
    text_coord = screen.get_width() // 2 - (len(intro_text) * 21 + (len(intro_text) - 1) * 10) // 2
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('white'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = screen.get_width() // 2 - string_rendered.get_width() // 2
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)


class Info(Window):
    def __init__(self):
        super().__init__()
        self.running = True
        self.ui()
        self.run()

    def ui(self):
        self.resize(640, 640)
        self.exit = Button(self, "data\\Sprites\\exit.png")
        self.exit.resize(80, 80)
        self.exit.move(560, 0)
        self.exit.set_func(self.exitFunc)
        self.last = Button(self, "data\\Sprites\\Last_1.png")
        self.last.resize(80, 80)
        self.last.move(0, 0)
        self.last.set_func(self.goToLast)
        self.set_background("data\\Sprites\\bg.jpg")

    def run(self):
        text = ['Создатель игры:', 'MaxVorosh/MaxVor', 'Т.к. я - единственный создатель, то',
                'изображённые войска могут не в полной мере', 'соответствовать истории',
                'За поиск изображений спасибо Денису Смирнову']
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.click(event.pos)
            self.screen.fill((0, 0, 0))
            make_fon(self.screen, text)
            self.sprites.draw(self.screen)
            pygame.display.flip()

    def goToLast(self):
        self.running = False

    def exitFunc(self):
        pygame.quit()
        sys.exit()
