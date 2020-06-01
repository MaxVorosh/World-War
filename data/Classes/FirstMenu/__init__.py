from data.Classes.Window import *
from data.Classes.Button import *
import sys
from data.Classes.LevelMenu import *


class FirstMenu(Window):
    def __init__(self):
        super().__init__()
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
        self.oso = Button(self, "data\\Sprites\\Osovets.jpg")
        self.oso.resize(350, 200)
        self.oso.move(100, 10)
        self.oso.set_func(self.Osovets)
        self.ver = Button(self, "data\\Sprites\\Verden.jpg")
        self.ver.resize(350, 200)
        self.ver.move(100, 220)
        self.ver.set_func(self.Verden)
        self.som = Button(self, "data\\Sprites\\Somma.jpg")
        self.som.resize(350, 200)
        self.som.move(100, 430)
        self.som.set_func(self.Somma)
        self.set_background("data\\Sprites\\bg.jpg")

    def exitFunc(self):
        pygame.quit()
        sys.exit()

    def Osovets(self):
        pass

    def Verden(self):
        pass

    def Somma(self):
        pass

    def goToLast(self):
        self.running = False
        pygame.mixer.music.load("data\\Music\\Вермахт.mp3")
        pygame.mixer.music.set_volume(0.05)
        pygame.mixer.music.play()

    def run(self):
        pygame.init()
        pygame.mixer.music.load("data\\Music\\Первая мировая война.mp3")
        pygame.mixer.music.set_volume(0.05)
        pygame.mixer.music.play()
        self.running = True
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.exitFunc()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.click(event.pos)
            self.screen.fill((0, 0, 0))
            if self.background:
                self.screen.blit(self.background, (0, 0))
            self.sprites.draw(self.screen)
            pygame.display.flip()
