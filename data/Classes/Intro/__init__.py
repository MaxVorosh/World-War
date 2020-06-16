from ..Window import Window
from ..Button import Button
import pygame
import sys


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


class Intro(Window):
    def __init__(self, text):
        super().__init__()
        self.text = text
        self.running = True
        self.ui()
        self.run()

    def ui(self):
        self.resize(640, 640)
        self.exit = Button(self, "data\\Sprites\\exit.png")
        self.exit.resize(80, 80)
        self.exit.move(560, 0)
        self.exit.set_func(self.exitFunc)
        self.last = Button(self, "data\\Sprites\\buttonStart.png")
        self.last.resize(100, 100)
        self.last.move(0, 0)
        self.last.set_func(self.goToLast)

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.exitFunc()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.click(event.pos)
            self.screen.fill((0, 0, 0))
            make_fon(self.screen, self.text)
            # if self.background:
            #     self.screen.blit(self.background, (0, 0))
            self.sprites.draw(self.screen)
            pygame.display.flip()

    def goToLast(self):
        self.running = False

    def exitFunc(self):
        pygame.quit()
        sys.exit()
