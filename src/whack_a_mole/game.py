import pygame as pg
from constants import *


class Game:
    def __init__(self):
        self.running = False

        pg.init()
        self.windowSurface = pg.display.set_mode(WIN_SIZE)
        self.clock = pg.time.Clock()
        self.running = True

        self.ballPosition = pg.math.Vector2(WIN_WIDTH/2.0, WIN_HEIGHT/2.0)
        self.ballDirection = pg.math.Vector2()
        self.ballSpeed: float = 400.0


    def quit(self):
        pg.quit()


    def handleEvents(self):
        events = pg.event.get()

        for event in events:
            if event.type == pg.QUIT:
                self.running = False
            if event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                self.running = False

        pressedKeys = pg.key.get_pressed()

        self.ballDirection.x = pressedKeys[pg.K_d] - pressedKeys[pg.K_a]
        self.ballDirection.y = pressedKeys[pg.K_s] - pressedKeys[pg.K_w]

        if self.ballDirection != pg.math.Vector2():
            self.ballDirection.normalize_ip()

        print(self.ballDirection)


    def update(self, dt: float):
        self.ballPosition += self.ballDirection * self.ballSpeed * dt


    def render(self):
        self.windowSurface.fill("#6495ED")

        pg.draw.circle(self.windowSurface, "#FF0000", self.ballPosition, 32)

        pg.display.update()


    def loop(self):
        while self.running:
            dt = self.clock.tick(FRAME_RATE_FPS) / MILLIS_PER_SEC

            self.handleEvents()
            self.update(dt)
            self.render()


    def run(self):
        self.loop()
        self.quit()
