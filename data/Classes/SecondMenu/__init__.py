from data.Classes.Window import *
from data.Classes.Button import *
import sys
from data.Classes.LevelMenu import *
from data.Classes.Level import *
from ..Intro import Intro

desc = {'kursk': '1943 г. СССР. Курск', 'midway': '1942 г. Тихий океан. Остров Мидуэй',
        'overloard': '1944 г. Франция. Нормандия', 'berlin': '1945 г. Территория Германии'}
texts = {'kursk': ['Генерал', 'Противник наступает на Орловско-Курском', 'и Курско-Обоянском направлении',
                   'Ваша задача - выдержать натиск и перейти в контратаку'],
         'midway': ['Генерал', 'Противник готовится захватить остров Мидуэй',
                    'Наша задача - решительно разбить флот Японии',
                    'Для этого нужно потопить авианосец,', 'который атакует соседний сектор обороны'],
         'overloard': ['Генерал', 'Наши войска высадились на пляжах',
                       'Теперь наша задача - продвинуться вглубь Франции'],
         'berlin': ['Генерал', 'Мы в шаге от победы', 'Необходимо захватить Берлин как можно быстрее']}


class SecondMenu(Window):
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
        self.K = Button(self, "data\\Sprites\\kursk.jpg")
        self.K.resize(300, 200)
        self.K.move(15, 100)
        self.K.set_func(self.kursk)
        self.O = Button(self, "data\\Sprites\\Overloard.png")
        self.O.resize(300, 200)
        self.O.move(325, 100)
        self.O.set_func(self.overloard)
        self.B = Button(self, "data\\Sprites\\Berlin.jpeg")
        self.B.resize(300, 200)
        self.B.move(15, 350)
        self.B.set_func(self.berlin)
        self.M = Button(self, "data\\Sprites\\Midway.jpg")
        self.M.resize(300, 200)
        self.M.move(325, 350)
        self.M.set_func(self.midway)
        self.set_background("data\\Sprites\\bg.jpg")

    def kursk(self):
        Intro(texts['kursk'])
        Level('Курская битва', 'Citadel', False, 2, 10, desc['kursk'])

    def midway(self):
        Intro(texts['midway'])
        Level('Взятие Мидуэя', 'Midway', False, 2, 8, desc['midway'])

    def overloard(self):
        Intro(texts['overloard'])
        Level('Высадка в Нормандии', 'Overloard', False, 2, 10, desc['overloard'])

    def berlin(self):
        Intro(texts['berlin'])
        Level('Берлинская операция', 'Berlin', False, 2, 12, desc['berlin'])

    def goToLast(self):
        self.running = False
        pygame.mixer.music.load("data\\Music\\Вермахт.mp3")
        pygame.mixer.music.set_volume(0.05)
        pygame.mixer.music.play()

    def exitFunc(self):
        pygame.quit()
        sys.exit()

    def run(self):
        pygame.init()
        pygame.mixer.music.load("data\\Music\\Вторая мировая война.mp3")
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
