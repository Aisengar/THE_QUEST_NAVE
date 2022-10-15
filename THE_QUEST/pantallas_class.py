import pygame as pg
from init import *
from objects import *
from nave import Nave

class partidas():
    def __init__(self, pantalla ):
        self.pantalla = pantalla
        self.enemy_list= []
        self.start= True 
        #fondo para Menu
        self.FondoM = pg.image.load("THE_QUEST/Imagens/Imagen para menu.jpeg").convert()
        self.backgroundM = pg.transform.scale(self.FondoM, (WIDTH, HEIGHT))#esta parte me permite redimensionar el tamaño del bakground
        #fondo para mision 1
        self.Fondo1 = pg.image.load("THE_QUEST/Imagens/fondo1.png").convert()
        self.background = pg.transform.scale(self.Fondo1, (WIDTH, HEIGHT))#esta parte me permite redimensionar el tamaño del bakground
        #fondo para mundo 2
        self.Fondo1 = pg.image.load("THE_QUEST/Imagens/fondo1.png").convert()
        self.background = pg.transform.scale(self.Fondo1, (WIDTH, HEIGHT))#esta parte me permite redimensionar el tamaño del bakground
        #Fondo para Game OVER
        self.Fondo1 = pg.image.load("THE_QUEST/Imagens/fondo1.png").convert()
        self.background = pg.transform.scale(self.Fondo1, (WIDTH, HEIGHT))#esta parte me permite redimensionar el tamaño del bakground
        self.scroll =0
        #fuentes
        self.font_titles= pg.font.Font("THE_QUEST/Fonts/Silkscreen-Bold.ttf",30)
        self.font_texto = pg.font.Font("THE_QUEST/Fonts/Silkscreen-Regular.ttf",25)

    def pantalla_juego(self):
        
        #Grupo Enemigos
        for i in range(enemigos):
            enemy = Enemigo()
            self.enemy_list.append(enemy)
        #Grupo nave
        nave=Nave()
        self.nave_sprites=pg.sprite.Group()
        self.nave_sprites.add(nave)

        while self.start:
            clock.tick(FPS)
            self.event_list = pg.event.get()
            for event in self.event_list:
                if event.type==pg.QUIT:
                    self.start = False
            
            for j in range(enemigos):
                pg.draw.rect(screen, self.enemy_list[j].color, (self.enemy_list[j].x, self.enemy_list[j].y, self.enemy_list[j].w, self.enemy_list[j].h))
                self.enemy_list[j].movimiento(800,600)
            #PLAYER SCREEN DROWING
            self.nave_sprites.draw(screen)
            nave.movimiento()
            nave.UPD()
            pg.display.flip()
            #Background en movimiento
            for i in range(2):
                self.pantalla.blit(self.background,(i*WIDTH+scroll,0))#Coloca la imagen del background
                self.scroll-=3
            if (self.scroll*-1)>=WIDTH:
                self.scroll = 0    
        pg.quit() 

    def menu_pp(self):
        
        while self.start:
            clock.tick(FPS)
            self.event_list = pg.event.get()
            for event in self.event_list:
                if event.type==pg.QUIT:
                    self.start = False

            pg.display.flip()
                    #Background en movimiento
            
            self.pantalla.blit(self.backgroundM,(0,0))#Coloca la imagen del background
            menu = self.font_titles.render("PULSA ENTER PARA INICIAR",True,WHITE)
            self.pantalla.blit(menu,(10,40))
            texto=self.font_texto.render("Tecla Arriba: para asennder\n Tecla Abajo: para desender\n Tecla Derecha: para ir a la derecha\n Tecla Izquierda: para ir a la izquierda",True,WHITE)
            self.pantalla.blit(texto,(10,100))
        pg.quit() 


juego = partidas(screen)
juego.menu_pp()
print("Hola")
#juego.pantalla_juego()