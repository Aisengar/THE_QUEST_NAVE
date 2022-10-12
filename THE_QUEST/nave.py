import pygame as pg
import random
from init import *

class Nave(pg.sprite.Sprite):
    def __init__(self,x=300,y=10):
        super().__init__()
        self.x=x
        self.y=y
        self.nav= pg.image.load("THE_QUEST/Imagens/Sprites nave1.png").convert()
        self.image=pg.transform.scale(self.nav, (80, 90))
        self.image.set_colorkey(BLACK)
        self.rect=self.image.get_rect()
        #self.rect.topleft = [self.x,self.y] 
        self.rect.centerx = WIDTH-10
        self.rect.centery = HEIGHT//2
        self.animation = ""
        
    def movimiento(self, xmax=800, ymax=600):
        #moviimiento por teclas
        self.vx = 0
        self.vy = 0
        #Movimiento y animacion
        keystate = pg.key.get_pressed()
        if keystate[pg.K_LEFT]:
            self.animation="THE_QUEST/Imagens/Sprites nave 5.png"
            print(self.animation)
            self.vx = -5
        elif keystate[pg.K_RIGHT]:
            self.animation="THE_QUEST/Imagens/Sprites nave 4.png"
            self.vx = 5
            print(self.animation)
        elif keystate[pg.K_DOWN]:
            self.animation="THE_QUEST/Imagens/Sprites nave 2.png"
            self.vy = 5
            print(self.animation)
        elif keystate[pg.K_UP]:
            self.animation="THE_QUEST/Imagens/Sprites nave 3.png"
            self.vy = -5
            print(self.animation)
        else:
            self.animation="THE_QUEST/Imagens/Sprites nave1.png" 

        self.rect.centerx += self.vx
        self.rect.centery += self.vy
        
        

