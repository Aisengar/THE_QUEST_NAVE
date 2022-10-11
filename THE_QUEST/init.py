import pygame as pg
import sys

#pygame inisiador
pg.init()

#objects
enemys = 20

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
WIDTH = 800
HEIGHT= 600
screen = pg.display.set_mode((WIDTH,HEIGHT))
pg.display.set_caption("THE QUEST")
FPS=60
#imagenes
Fondo1 = pg.image.load("THE_QUEST/Imagens/Fondo 2.jpeg")
background = pg.transform.scale(Fondo1, (WIDTH, HEIGHT))#esta parte me permite redimensionar el tamaño del bakground


