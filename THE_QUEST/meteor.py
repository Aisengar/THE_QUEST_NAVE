
import pygame as pg
from init import *

def meteor():
    lista = []
    sheet = pg.image.load("THE_QUEST/Imagens/Asteroides Sprite.png").convert_alpha()
    for row in range(0,8):    
        for column in range(0,8):
            animation= pg.Rect(38*column,35*row,38,35)
            lista.append(sheet.subsurface(animation))
    return lista
asteroid_animation=pg.sprite.Group()



class Meteo(pg.sprite.Sprite):
    def __init__(self,position):
        super().__init__(self)
        self.sheet = pg.image.load("THE_QUEST/Imagens/Asteroides Sprite.png").convert_alpha()
        self.animation=pg.sprite.Group()

        



