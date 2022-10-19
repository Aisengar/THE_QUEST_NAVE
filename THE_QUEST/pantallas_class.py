

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
        
        
        #vidas e inmunidad
        self.vidas=3
        self.inmunidad=120
         #Fin del juego
        self.final=5

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

        self.planeta= pg.image.load("THE_QUEST/Imagens/Planetas/planet.png").convert()
        self.planeta.set_colorkey(BLACK)

        self.scroll =0
        #fuentes
        self.font_titles= pg.font.Font("THE_QUEST/Fonts/Silkscreen-Bold.ttf",30)
        self.font_texto = pg.font.Font("THE_QUEST/Fonts/Silkscreen-Regular.ttf",20)
        self.font_titles2= pg.font.Font("THE_QUEST/Fonts/Silkscreen-Bold.ttf",50)
       

         #                ---------------------------- Pantalla Del Juego -----------------------------
    def pantalla_juego(self,score):
        
        #Grupo nave
        nave=Nave()
        self.nave_sprites=pg.sprite.Group()
        self.nave_sprites.add(nave)
        #enemigo
        for i in range(enemigos):
            asteroid= Meteo()
            self.asteroids.add(asteroid)
        self.start_ticks=pg.time.get_ticks() #starter tick
        self.hige_score=score
        start=True
        contador=0
        while start:
        
            #contador
            self.seconds=int((pg.time.get_ticks()-self.start_ticks)/1000)
                
            #eventos
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
                        #shoot_sound.play()


            #Colisiones 
            hits=pg.sprite.groupcollide(self.bullet_list, self.asteroids,True,True)
            for hit in hits:
                self.score += 100
                explotar=Explosion(hit.rect.center)
                asteroid=Meteo()
                self.asteroids.add(asteroid,explotar)
                #exposion_sound.play()

                #Colision nave-asteroide, explosion nave y sonido, vida e inmunidad 
            hits=pg.sprite.groupcollide(self.nave_sprites, self.asteroids,False,True)
            for hit in hits:
                explotar=Explosion(hit.rect.center)
                asteroid=Meteo()
                self.nave_sprites.add(explotar)
                self.asteroids.add(asteroid)
                #exposion_sound.play()
            if hits and self.inmunidad>=120:
                self.vidas-=1
                self.inmunidad=0
                if self.vidas<=0:
                    #Preparando las puntuasiones
                    self.score_anerior=self.score
                    if self.hige_score < self.score:
                        self.hige_score=self.score
                    start=False
            elif self.inmunidad>120:
                self.inmunidad=120
            elif self.inmunidad<120:
                self.inmunidad+=1


            #limitador de creador
            contador+=1
    
            #creador de objetos
            #if self.seconds%2==0 and self.seconds<=self.final and contador>=20:
            if self.seconds%2==0 and self.seconds<=self.final and contador>=20:
                print("crear")
                asteroid=Meteo()
                self.asteroids.add(asteroid)
                contador=0
            
            #Musica
            #map1_sound.play()

            #Dibujo de listas de objetos
            self.bullet_list.draw(self.pantalla)
            self.asteroids.draw(self.pantalla)
            self.nave_sprites.draw(self.pantalla)
            if self.seconds<self.final+3:
                nave.movimiento()
                nave.update()
            pg.display.flip()
            
            #Updates
            self.asteroids.update()
            self.bullet_list.update()
            self.nave_sprites.update()
            #Background en movimiento
            for i in range(2):
                self.pantalla.blit(self.background,(i*WIDTH+self.scroll,0))#Coloca la imagen del background
                if self.seconds <=self.final:
                    self.scroll-=3
                
            if (self.scroll*-1)>=WIDTH:
                self.scroll = 0
                
            if self.seconds==0:
                pass
            elif self.seconds%60==0:
                self.score+=100
             #imprimir el planeta en pantalla
            if self.seconds >=self.final:#cuando termine el juego
                self.pantalla.blit(self.planeta,(-50+WIDTH+self.scroll,-50))
                
            if self.seconds>(self.final+3):
                nave.termino()
            #mouse = pg.mouse.get_pos() 
            #print(mouse)
                        #Marcadores
            dibujar_texto(self.pantalla,"Score: "+ str(self.score),20,WIDTH//2,10)
            dibujar_texto(self.pantalla,"Time: "+str(int(self.seconds)),20,50,10)
            dibujar_texto(self.pantalla,"Vidas: "+ str(self.vidas),20,750,10)
            dibujar_texto(self.pantalla,"Hige Score:"+ str(self.hige_score),20,WIDTH//2,30)



        #pg.quit() 
                     #                ---------------------------- Pantalla Del menu -----------------------------
    def menu_pp(self):
        texto1=self.font_texto.render("Tecla Arriba: para ascender",True,WHITE)
        texto2=self.font_texto.render("Tecla Abajo: para descender",True,WHITE)
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
                    menu_sound.stop()
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
            #menu_sound.play()
        #pg.quit() 
        menu_sound.stop()
    
    
                     #                ---------------------------- Pantalla Game Over -----------------------------
    
    
    def game_ov(self):
        self.score_anerior=self.score
        texto=self.font_titles2.render("Pulsa Enter",True,WHITE)
        start=True
        while start:
            clock.tick(FPS)
            self.event_list = pg.event.get()
            for event in self.event_list:
                if event.type==pg.QUIT or event.type== pg.K_BACKSPACE:
                    self.start = False
                if event.type == pg.KEYDOWN:
                    if event.type == pg.K_SPACE:
                        self.pantalla_juego()

                    if event.key == pg.K_RETURN:
                        start = False
                    
            self.pantalla.blit(self.background_go,(0,0))#Coloca la imagen del background
            self.pantalla.blit(texto,(200,420))


            
            pg.display.flip()
        
            
        #pg.quit() 
