from data.Classes.Window import *
from data.Classes.Button import *
import sys
from data.Classes.LevelMenu import *
from data.Classes.FirstMenu import *
from data.Classes.SecondMenu import *
from data.Classes.ZeroMenu import *


class LevelMenu(Window):
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
        self.ww0 = Button(self, "data\\Sprites\\ww0.jpg")
        self.ww0.resize(300, 200)
        self.ww0.move(150, 10)
        self.ww0.set_func(self.WW0)
        self.ww1 = Button(self, "data\\Sprites\\ww1.jpg")
        self.ww1.resize(300, 200)
        self.ww1.move(150, 220)
        self.ww1.set_func(self.WW1)
        self.ww2 = Button(self, "data\\Sprites\\ww2.jpg")
        self.ww2.resize(300, 200)
        self.ww2.move(150, 430)
        self.ww2.set_func(self.WW2)
        self.last = Button(self, "data\\Sprites\\Last_1.png")
        self.last.resize(80, 80)
        self.last.move(0, 0)
        self.last.set_func(self.goToLast)
        self.set_background("data\\Sprites\\bg.jpg")

    def WW1(self):
        FirstMenu()

    def WW0(self):
        ZeroMenu()

    def WW2(self):
        SecondMenu()

    def goToLast(self):
        self.running = False

    def exitFunc(self):
        pygame.quit()
        sys.exit()

    def run(self):
        pygame.init()
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
