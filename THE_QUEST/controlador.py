from datos import insertRow,readOrder
from pantallas_class import *
from datos import *
def partida():
    game = Partidas()
    higescore=0
    salir=False
    while not salir:

        game = Partidas()
        salir=game.menu_pp()
        if not salir:
            salir=game.pantalla_juego(higescore)
            higescore= game.hige_score
            scr=game.score
            if game.vidas>0 and salir!=True:
                game.pantalla_juego2(higescore)
            if not salir:
                salir=game.game_ov()
                score=readOrder("score")
                if len(score)<5:
                    nombre=game.user_text
                    insertRow(nombre,scr)
                if len(score)>=5 and (score[0][1]<scr or score[1][1]<scr or score[2][1]<scr or score[3][1]<scr):
                    nombre=game.user_text
                    insertRow(nombre,scr)
                    
                            
            
    
