import pygame as pg
import sys

#pygame init
pg.init()

#objects
enemys = 10

#colors
BLACK=(0, 0, 0)
WHITE= (255,255,255)

#Booleans
start = True

#pg init y sonido
pg.init()
pg.mixer.init()
clock= pg.time.Clock()

#pantalla
scroll=0
WIDTH = 800
HEIGHT= 600
screen = pg.display.set_mode((WIDTH,HEIGHT))
pg.display.set_caption("THE QUEST")
FPS=60

#imagenes
Fondo1 = pg.image.load("THE_QUEST/Imagens/fondo1.png").convert()
background = pg.transform.      (Fondo1, (WIDTH, HEIGHT))#esta parte me permite redimensionar el tamaño del bakground


