from re import T
import pygame as pg
from pantallas_class import *

pantallas=[]
higescore=0
game = partidas()
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