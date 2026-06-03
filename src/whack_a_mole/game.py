import pygame as pg
from constants import *


class Game:
    def __init__(self):
        self.running = False


    def init(self):
        pg.init()
        self.windowSurface = pg.display.set_mode(WIN_SIZE)
        self.running = True


    def quit(self):
        pg.quit()


    def handleEvents(self):
        events = pg.event.get()

        for event in events:
            if event.type == pg.QUIT:
                self.running = False
            if event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                self.running = False


    def update(self):
        pass


    def render(self):
        self.windowSurface.fill("#6495ED")

        pg.draw.circle(self.windowSurface, "#FF0000", (WIN_WIDTH/2.0, WIN_HEIGHT/2.0), 32)

        pg.display.update()


    def run(self):
        self.init()

        while self.running:
            self.handleEvents()
            self.update()
            self.render()

        self.quit()
