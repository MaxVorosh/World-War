from data.Classes.Window import *
from data.Classes.Button import *
import sys
from data.Classes.LevelMenu import *
from data.Classes.FirstMenu import *
from data.Classes.SecondMenu import *
from ..Level import *
from ..Intro import Intro

desc = {'Blitzkrieg': '1940 г. Территория Франции', 'Wolfpack': '1940 г. Атлантический океан'}
text = {'Blitzkrieg': ['Генерал', 'Вам необходимо прорвать оборону Франции и захватить её',
                       'Ключевые точки обозначены жёлтым', 'Для выделения юнита, нажмите на него',
                       'После этого он будет помечен зелёным кружком',
                       'Клетки, в которые юнит может двигаться, выделены синим',
                       'Те, котороые может атаковать - красным',
                       'Чтобы двигаться или атаковать -', 'нажмите на необходимую клетку',
                       'Если юнит попадает на ключевую точку,', 'то теперь вы её контролируете',
                       'Если туда попадает вражеский юнит - контроль снимается',
                       'Для победы необходимо контролировать все ключевые точки',
                       'Чтобы закончить ход, нажмите на песочные часы'],
        'Wolfpack': ['Генерал', 'Вам необходимо атаковать транспортные суда', 'Есть три типа боевых кораблей',
                     'Субмарины - уязвимы для эсминцев', 'Эсминцы - уязвимы для ликоров',
                     'Линкоры - уязвимы для субмарин', 'Транспортные суда не представляют опасности']}


class ZeroMenu(Window):
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
        self.bl = Button(self, "data\\Sprites\\blizkreig.jpg")
        self.bl.resize(450, 300)
        self.bl.move(100, 10)
        self.bl.set_func(self.Blizkreig)
        self.at = Button(self, "data\\Sprites\\Attach_on_convoi.jpg")
        self.at.resize(450, 300)
        self.at.move(100, 330)
        self.at.set_func(self.Attach)
        self.set_background("data\\Sprites\\bg.jpg")

    def exitFunc(self):
        pygame.quit()
        sys.exit()

    def Blizkreig(self):
        Intro(text['Blitzkrieg'])
        Level('Блицкриг', 'Blitzkrieg', True, 0, 5, desc['Blitzkrieg'])

    def Attach(self):
        Intro(text['Wolfpack'])
        Level('Атака на конвои', 'Wolfpack', True, 0, 8, desc['Wolfpack'])

    def goToLast(self):
        self.running = False

    def run(self):
        pygame.init()
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
