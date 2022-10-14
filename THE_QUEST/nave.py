import pygame as pg
import random
from init import *

class Nave(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
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
            self.vx -= 5
        elif keystate[pg.K_RIGHT]:
            self.animation="THE_QUEST/Imagens/Sprites nave 4.png"
            self.vx = 5
        elif keystate[pg.K_DOWN]:
            self.animation="THE_QUEST/Imagens/Sprites nave 2.png"
            self.vy += 5
        elif keystate[pg.K_UP]:
            self.animation="THE_QUEST/Imagens/Sprites nave 3.png"
            self.vy -= 5
        else:
            self.animation="THE_QUEST/Imagens/Sprites nave1.png"
            self.vx -= 5

        #Cambio de posision 
        self.rect.centerx += self.vx
        self.rect.centery += self.vy
        #limite de tablero
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.left < 0:
            self.rect.left =0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH

    def UPD(self):
        self.nav= pg.image.load(self.animation).convert()
        self.image=pg.transform.scale(self.nav, (80, 90))
        self.image.set_colorkey(BLACK)




    