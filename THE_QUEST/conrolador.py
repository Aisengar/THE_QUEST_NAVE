import pygame as pg
from pantallas_class import *

salir=False
while not salir:
    event_list = pg.event.get()
    for event in event_list:
        if event.type==pg.QUIT:
            start = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                salir = True
    game = partidas()
    game.menu_pp()
    game = partidas()
    game.pantalla_juego()
    game = partidas()
    game.game_ov()