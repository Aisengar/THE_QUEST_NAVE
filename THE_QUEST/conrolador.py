import pygame as pg
from pantallas_class import *


scorehige=0
salir=False
while not salir:
    
    event_list = pg.event.get()
    for event in event_list:
        if event.type==pg.QUIT:
            salir = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                salir = True
    game = partidas()
    game.menu_pp()
    game = partidas()
    game.pantalla_juego(scorehige)
    scorehige=game.hige_score
    game = partidas()
    game.game_ov()