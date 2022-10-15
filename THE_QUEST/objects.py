import pygame as pg
import random
from init import *

class Jugador(pg.sprite.Sprite):
    
    def __init__(self, x= 10, y=300, w = 40, h=40, color = (255, 0, 255)):
        super().__init__()
        self.x = x
        self.y = y
        self.image= pg.image.load("THE_QUEST/Imagens/Sprites nave1.png")
        self.rect=self.image.get_rect()
        self.rect.topleft = [self.x,self.y]
        self.w = w
        self.h = h
        self.color = color 
        self.animation = ""
    def movimiento(self, xmax, ymax):
        #moviimiento por teclas
        self.vx = 0
        self.vy = 0
        #Movimiento y animacion
        keystate = pg.key.get_pressed()
        if keystate[pg.K_LEFT]:
            self.animation="THE_QUEST/Imagens/Sprites nave 5.png"
            self.vx = -5
        elif keystate[pg.K_RIGHT]:
            self.animation="THE_QUEST/Imagens/Sprites nave 4.png"
            self.vx = 5
        elif keystate[pg.K_DOWN]:
            self.animation="THE_QUEST/Imagens/Sprites nave 2.png"
            self.vy = 5
        elif keystate[pg.K_UP]:
            self.animation="THE_QUEST/Imagens/Sprites nave 3.png"
            self.vy = -5
        else:
            self.animation="THE_QUEST/Imagens/Sprites nave1.png" 

        #delimitar el tagblero
        if self.x <= 0 or self.x >= xmax - self.w:
            self.vx *= -1
        if self.y <= 0 or self.y >= ymax - self.h:
            self.vy *= -1
        #movimiento
        self.x += self.vx
        self.y += self.vy
    def Drw(self):
        #Imagen
        self.image= pg.image.load(self.animation)
        self.rect=self.image.get_rect()
        self.rect.topleft = [self.x,self.y]
        
    def Update(self):
        self.image= pg.image.load(self.animation)


        



class Enemigo:
    def __init__(self, w = 40, h=40, color = (255, 0, 255)):
        self.w = w
        self.h = h
        self.color = color
        self.x = random.randint(810, 830)
        self.y = random.randint(0, 600)
        self.vx = random.randint(-7,-4)
        self.vy = random.randint(-3,3)
    def movimiento(self, xmax, ymax):
        self.x += self.vx
        #self.y += self.vy
        if self.x > xmax+self.h or self.x < 0 or self.y+self.w < 0 or self.y> ymax+ self.w:
            self.x = random.randint(810,820)
            self.y = random.randint(0, 600)

