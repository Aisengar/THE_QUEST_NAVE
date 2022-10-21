
import pygame as pg
from pantallas_class import *

game = partidas()
higescore=0
pantallas=[game.menu_pp(), game.pantalla_juego(higescore), game.game_ov()]
i=0
salir=False
while not salir:

    game = partidas()
    game.menu_pp()
    salir=game.menu_pp()
    if salir!=False:
        game.pantalla_juego(higescore)
        higescore= game.hige_score
        if salir!=False:
            salir=game.pantalla_juego
            game.game_ov()
            salir=game.game_ov()
"""
    salir=pantallas[i]
    higescore=game.hige_score
    i+1
    if i>=len(pantallas):
        i=0
"""