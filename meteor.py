import random
import pygame as pg
from THE_QUEST.init import *

def meteor_animation():
    animation_list = []
    sheet=pg.image.load("THE_QUEST/Imagens/Asteroides Sprite.png").convert_alpha()
    for row in range(0,8):
        for colum in range(0,8):
            animation= pg.Rect(38*colum,38*row,38,38)
            animation_list.append(sheet.subsurface(animation))
    return animation_list

animation_list= meteor_animation()




class Meteo(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.list_animation = animation_list
        self.image= self.list_animation[0]
        self.image.set_colorkey(BLACK)
        self.rect=self.image.get_rect()
        self.rect.topleft=[random.randint(810, 830),random.randint(0, 600)]

        self.index=0
        self.vx=1
    def update(self):
        
        self.image=self.list_animation[int(self.index)]
        self.image.set_colorkey(BLACK)
        self.index +=0.25
        self.rect.centerx -= self.vx
        if self.index >= len(self.list_animation):
            self.index=0


        

sprites = pg.sprite.Group()
for i in range(10):
    asteroide = Meteo()
    sprites.add(asteroide)

cerrar = False
while not cerrar:
    pg.display.update()
    screen.fill(BLACK)
    sprites.draw(screen)
    sprites.update()

    for event in pg.event.get():
        if event.type ==pg.QUIT:
            cerrar=True
