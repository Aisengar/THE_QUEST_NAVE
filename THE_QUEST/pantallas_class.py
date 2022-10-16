from email.headerregistry import Group
import pygame as pg
from init import *
from objects import *


class partidas():
    def __init__(self ):
        self.pantalla = pg.display.set_mode((WIDTH,HEIGHT))
        self.asteroids=pg.sprite.Group()
        #self.start= True
         
        #fondo para Menu
        self.FondoM = pg.image.load("THE_QUEST/Imagens/Imagen para menu.jpeg").convert()
        self.backgroundM = pg.transform.scale(self.FondoM, (WIDTH, HEIGHT))#esta parte me permite redimensionar el tamaño del bakground

        #fondo para mision 1
        self.Fondo1 = pg.image.load("THE_QUEST/Imagens/fondo1.png").convert()
        self.background = pg.transform.scale(self.Fondo1, (WIDTH, HEIGHT))#esta parte me permite redimensionar el tamaño del bakground

        #fondo para mundo 2
        self.Fondo2 = pg.image.load("THE_QUEST/Imagens/fondo1.png").convert()
        self.background2 = pg.transform.scale(self.Fondo2, (WIDTH, HEIGHT))#esta parte me permite redimensionar el tamaño del bakground

        #Fondo para Game OVER
        self.game_over = pg.image.load("THE_QUEST/Imagens/game_over.jpeg").convert()
        self.background_go = pg.transform.scale(self.game_over, (WIDTH, HEIGHT))#esta parte me permite redimensionar el tamaño del bakground

        self.scroll =0
        #fuentes
        self.font_titles= pg.font.Font("THE_QUEST/Fonts/Silkscreen-Bold.ttf",30)
        self.font_texto = pg.font.Font("THE_QUEST/Fonts/Silkscreen-Regular.ttf",20)
        self.font_titles2= pg.font.Font("THE_QUEST/Fonts/Silkscreen-Bold.ttf",50)
    def pantalla_juego(self):
        
        #Grupo nave
        nave=Nave()
        self.nave_sprites=pg.sprite.Group()
        self.nave_sprites.add(nave)
        
        #enemigo
        for i in range(enemigos):
            asteroid= Meteo()
            self.asteroids.add(asteroid)

            

        start=True
        while start:
            clock.tick(FPS)
            self.event_list = pg.event.get()
            for event in self.event_list:
                if event.type==pg.QUIT:
                    start = False
            
            self.asteroids.draw(self.pantalla)
            self.asteroids.update()
            #PLAYER SCREEN DROWING
            self.nave_sprites.draw(self.pantalla)
            nave.movimiento()
            nave.UPD()
            pg.display.flip()
            #Background en movimiento
            
            for i in range(2):
                self.pantalla.blit(self.background,(i*WIDTH+self.scroll,0))#Coloca la imagen del background
                self.scroll-=2
                print(self.scroll)
            if (self.scroll*-1)>=WIDTH:
                self.scroll = 0
        pg.quit() 

    def menu_pp(self):
        texto1=self.font_texto.render("Tecla Arriba: para asennder",True,WHITE)
        texto2=self.font_texto.render("Tecla Abajo: para desender",True,WHITE)
        texto3=self.font_texto.render("Tecla Derecha: para ir a la derecha",True,WHITE)
        texto4=self.font_texto.render("Tecla Izquierda: para ir a la izquierda",True,WHITE)
        texto5=self.font_texto.render("Espacio: para disparar",True,WHITE)
        start=True
        while start:
            clock.tick(FPS)
            self.event_list = pg.event.get()
            for event in self.event_list:
                if event.type==pg.QUIT:
                    start = False

            pg.display.flip()
                    #Background en movimiento
            
            self.pantalla.blit(self.backgroundM,(0,0))#Coloca la imagen del background
            #textos menu
            menu = self.font_titles.render("opciones:",True,WHITE)
            self.pantalla.blit(menu,(10,240))
            self.pantalla.blit(texto1,(10,300))
            self.pantalla.blit(texto2,(10,340))
            self.pantalla.blit(texto3,(10,380))
            self.pantalla.blit(texto4,(10,420))
            self.pantalla.blit(texto5,(10,460))
        pg.quit() 

    def game_ov(self):
        texto=self.font_titles2.render("Pulsa Enter",True,WHITE)
        start=True
        while start:
            clock.tick(FPS)
            self.event_list = pg.event.get()
            for event in self.event_list:
                if event.type==pg.QUIT or event.type== pg.K_BACKSPACE:
                    self.start = False
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_RETURN:
                        start = False
            self.pantalla.blit(self.background_go,(0,0))#Coloca la imagen del background
            self.pantalla.blit(texto,(200,420))

            pg.display.flip()
            
            
        pg.quit() 

game = partidas()
game.pantalla_juego()