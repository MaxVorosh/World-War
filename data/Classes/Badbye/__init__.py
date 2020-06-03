import pygame
from ..Window import Window
from ..Button import Button
import sys


def make_fon(screen, intro_text, fon):
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 30)
    text_coord = 190
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('white'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = screen.get_width() // 2 - string_rendered.get_width() // 2
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)


class Badbye(Window):
    def __init__(self, window_number, screen):
        super().__init__()
        self.window_number = window_number
        self.running = True
        self.ui()
        self.run(screen)

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

    def run(self, screen):
        pygame.init()
        text = ["Вы проиграли"]
        make_fon(screen, text, self.background)
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.exitFunc()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.click(event.pos)
            self.screen.fill((0, 0, 0))
            make_fon(screen, text, self.background)
            self.sprites.draw(self.screen)
            pygame.display.flip()

    def goToLast(self):
        self.running = False
        if self.window_number == 0:
            pygame.mixer.music.load("data\\Music\\Вермахт.mp3")
        elif self.window_number == 1:
            pygame.mixer.music.load("data\\Music\\Первая мировая война.mp3")
        else:
            pygame.mixer.music.load("data\\Music\\Вторая мировая война.mp3")
        pygame.mixer.music.set_volume(0.05)
        pygame.mixer.music.play()

    def exitFunc(self):
        pygame.quit()
        sys.exit()
