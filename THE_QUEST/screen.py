import pygame as pg
from init import *
from objects import *

enemy_list= []
player=Jugador()

for i in range(enemys):
    enemy = Enemigo()
    enemy_list.append(enemy)


while start:
    clock.tick(60)
    #screen.fill((0, 0, 0))
    event_list = pg.event.get()
    for event in event_list:
        if event.type==pg.QUIT:
            start = False
    
    for j in range(enemys):
        pg.draw.rect(screen, enemy_list[j].color, (enemy_list[j].x, enemy_list[j].y, enemy_list[j].w, enemy_list[j].h))
        enemy_list[j].movimiento(800,600)

    pg.draw.rect(screen, player.color, (player.x,player.y, player.w,player.h))
    player.movimiento(800, 600)

    pg.display.flip()
    screen.blit(background,(0,0))

pg.quit()