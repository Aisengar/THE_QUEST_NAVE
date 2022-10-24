from datos import insertRow
from pantallas_class import *
from datos import *

game = Partidas()
higescore=0
i=0
salir=False
while not salir:

    game = Partidas()
    salir=game.menu_pp()
    if not salir:
        game=Partidas()
        salir=game.pantalla_juego(higescore)
        higescore= game.hige_score
        if game.vidas>0:
            game.pantalla_juego2(higescore)
        if not salir:
            salir=game.game_ov()
            nombre=game.user_text
            insertRow(nombre,higescore) 
            
            
    
