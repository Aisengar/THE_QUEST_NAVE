import pygame as pg
import random

class Jugador:
    def __init__(self, x=300, y=300, w = 40, h=40, color = (255, 0, 255)):
        self.w = w
        self.h = h
        self.color = color
        self.x = x
        self.y = y 
        self.vx = 0
        self.vy = 0

    def movimiento(self, xmax, ymax):
        #moviimiento por teclas
        self.vx = 0
        self.vy = 0
        keystate = pg.key.get_pressed()
        if keystate[pg.K_LEFT]:
            self.vx = -5
        elif keystate[pg.K_RIGHT]:
            self.vx = 5
        elif keystate[pg.K_DOWN]:
            self.vy = 5
        elif keystate[pg.K_UP]:
            self.vy = -5

        #delimitar el tagblero
        if self.x <= 0 or self.x >= xmax - self.w:
            self.vx *= -1
        if self.y <= 0 or self.y >= ymax - self.h:
            self.vy *= -1
        #movimiento
        self.x += self.vx
        self.y += self.vy

class Enemigo:
    def __init__(self, w = 40, h=40, color = (255, 0, 255)):
        self.w = w
        self.h = h
        self.color = color
        self.x = random.randint(-10, 0)
        self.y = random.randint(0, 600)
        self.vx = random.randint(0 ,5)
        self.vy = random.randint(1,5)
    def movimiento(self, xmax, ymax):
        self.x += self.vx
        self.y += self.vy
        if self.x > xmax+self.h or self.y+self.w < 0 or self.y> ymax+ self.w:
            self.x = random.randint(-10,-5)
            self.y = random.randint(0, 600)