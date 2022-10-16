
import pygame as pg
from init import *
from objects import *

#Funcion para crear texto
def dibujar_texto(surface, text, size, x, y):
    font= pg.font.Font("THE_QUEST/Fonts/RobotoMono-Italic-VariableFont_wght.ttf",size)
    text_surface= font.render(text,True,WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop= (x,y)
    surface.blit(text_surface, text_rect)


class partidas():
    def __init__(self ):
        self.pantalla = pg.display.set_mode((WIDTH,HEIGHT))
        self.asteroids=pg.sprite.Group()
        self.bullet_list=pg.sprite.Group()
        
        #Puntaje y Tiempo
        self.score=0
         
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
        #Disparo
        bullet=Bullet(100,200)
        #enemigo
        for i in range(enemigos):
            asteroid= Meteo()
            self.asteroids.add(asteroid)
        self.start_ticks=pg.time.get_ticks() #starter tick
        print(self.start_ticks)

        start=True
        while start:
            self.seconds=int((pg.time.get_ticks()-self.start_ticks)/1000)
            
            clock.tick(FPS)
            self.event_list = pg.event.get()
            for event in self.event_list:
                if event.type==pg.QUIT:
                    start = False
                elif event.type==pg.KEYDOWN:
                    #evento de disparo
                    if event.key == pg.K_SPACE:
                        bullet=Bullet(nave.rect.centerx,nave.rect.centery)
                        self.bullet_list.add(bullet)
            #Colisiones 
            hits=pg.sprite.groupcollide(self.bullet_list, self.asteroids,True,True)
            for hit in hits:
                self.score += 10
                asteroid=Meteo()
                self.asteroids.add(asteroid)
                

            #Dibujo de listas de objetos
            self.bullet_list.draw(self.pantalla)
            self.asteroids.draw(self.pantalla)
            self.nave_sprites.draw(self.pantalla)
            nave.movimiento()
            pg.display.flip()
            
            #Updates
            self.asteroids.update()
            self.bullet_list.update()
            self.nave_sprites.update()
            #Background en movimiento
            for i in range(2):
                self.pantalla.blit(self.background,(i*WIDTH+self.scroll,0))#Coloca la imagen del background
                self.scroll-=2
                
            if (self.scroll*-1)>=WIDTH:
                self.scroll = 0
                        #Marcadores
            dibujar_texto(self.pantalla,str(self.score),25,WIDTH//2,10)
            dibujar_texto(self.pantalla,str(int(self.seconds)),25,10,10)
            if self.seconds==0:
                pass
            elif self.seconds%5==0:
                print(self.seconds%5)
                self.score+=100


            
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
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_RETURN:
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


            print(self.seconds)
            pg.display.flip()
            
            
        pg.quit() 

game = partidas()
game.pantalla_juego()