
import pygame as pg
from init import *
from objects import *
from nave import Nave



enemy_list= []
#Crear enemigos 
for i in range(enemigos):
    enemy = Enemigo()
    enemy_list.append(enemy)
nave=Nave()
nave_sprites=pg.sprite.Group()
nave_sprites.add(nave)

while start:
    clock.tick(FPS)
    event_list = pg.event.get()
    for event in event_list:
        if event.type==pg.QUIT:
            start = False
    
    for j in range(enemigos):
        pg.draw.rect(screen, enemy_list[j].color, (enemy_list[j].x, enemy_list[j].y, enemy_list[j].w, enemy_list[j].h))
        enemy_list[j].movimiento(800,600)
  #PLAYER SCREEN DROWING

    nave_sprites.draw(screen)
    nave.movimiento()
    nave.UPD()
    pg.display.flip()
    #Background en movimiento
    for i in range(2):
       screen.blit(background,(i*WIDTH+scroll,0))#Coloca la imagen del background
    scroll-=3
    if (scroll*-1)>=WIDTH:
        print(scroll)
        scroll = 0    
pg.quit() 