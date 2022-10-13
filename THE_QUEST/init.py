import pygame as pg
import sys
from objects import Jugador,Enemigo
from random import randint

#pygame init settings
pg.init()
pg.mixer.init()
clock= pg.time.Clock()

#colors y otros
contador =0
BLACK=(0, 0, 0)
WHITE= (255,255,255)

#objects
def n_enemigos():
    numero=randint(5,20)
    return int(numero)
enemigos = 10
player=Jugador()
enemy=Enemigo()

#Booleans
start = True

#pantalla
scroll=0
WIDTH = 800
HEIGHT= 600
screen = pg.display.set_mode((WIDTH,HEIGHT))
pg.display.set_caption("THE QUEST")
FPS=60

#imagenes
Fondo1 = pg.image.load("THE_QUEST/Imagens/fondo1.png").convert()
background = pg.transform.scale(Fondo1, (WIDTH, HEIGHT))#esta parte me permite redimensionar el tamaño del bakground

player_sprite= pg.sprite.Group()
player_sprite.add(player)

