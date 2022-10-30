import pygame as pg
from init import *
from objects import *
from datos import readOrder

#Funcion para crear texto
def dibujar_texto(surface, text, size, x, y,color=WHITE,font="THE_QUEST/Fonts/RobotoMono-Italic-VariableFont_wght.ttf"):
    font= pg.font.Font(font,size)
    text_surface= font.render(text,True,color)
    text_rect = text_surface.get_rect()
    text_rect.midtop= (x,y)
    surface.blit(text_surface, text_rect)
def dibujar_ranking(surface, text, size, x, y,color=WHITE,font="THE_QUEST/Fonts/RobotoMono-Italic-VariableFont_wght.ttf"):
    font= pg.font.Font(font,size)
    text_surface= font.render(text,True,color)
    text_rect = text_surface.get_rect()
    text_rect.midleft= (x,y)
    surface.blit(text_surface, text_rect)

class Partidas():
    def __init__(self ):
        
        self.pantalla = pg.display.set_mode((WIDTH,HEIGHT))
        self.asteroids=pg.sprite.Group()
        self.bullet_list=pg.sprite.Group()
        #lector de los rankings
        self.ranking= readOrder("Score")
        #Puntaje
        self.score=0
        self.start=True
        #introducir nombre
        self.user_text=""
        
        #vidas e inmunidad
        self.vidas=4
        self.inmunidad=60
         #Fin del juego
        self.final=40

        #fondo para Menu
        self.FondoM = pg.image.load("THE_QUEST/Imagens/Fondo_Historia.jpeg").convert()
        self.backgroundM = pg.transform.scale(self.FondoM, (WIDTH, HEIGHT))#esta parte me permite redimensionar el tamaño del bakground

        #fondo para mision 1
        self.Fondo1 = pg.image.load("THE_QUEST/Imagens/fondo1.png").convert()
        self.background = pg.transform.scale(self.Fondo1, (WIDTH, HEIGHT))#esta parte me permite redimensionar el tamaño del bakground

        #fondo para mundo 2
        self.Fondo2 = pg.image.load("THE_QUEST/Imagens/planeta_destruido.jpeg").convert()
        self.Fondo2 = pg.transform.scale(self.Fondo2, (WIDTH, HEIGHT))#esta parte me permite redimensionar el tamaño del bakground

        #Fondo para Game OVER
        self.game_over = pg.image.load("THE_QUEST/Imagens/game_over.jpeg").convert()
        self.background_go = pg.transform.scale(self.game_over, (WIDTH, HEIGHT))#esta parte me permite redimensionar el tamaño del bakground
        #planetas para final de nivel
        self.planeta= pg.image.load("THE_QUEST/Imagens/Planetas/planet.png").convert()
        self.planeta.set_colorkey(BLACK)

        self.planeta2= pg.image.load("THE_QUEST/Imagens/Planetas/PlanetaTierra.png").convert()
        self.planeta2 = pg.transform.scale(self.planeta2, (625, 625))
        self.planeta2.set_colorkey(BLACK)
        #movimiento planeta y pantalla juego
        self.scroll =0
        self.scroll_planeta=0
        #fuentes
        self.font_titles= pg.font.Font("THE_QUEST/Fonts/Silkscreen-Bold.ttf",30)
        self.font_texto = pg.font.Font("THE_QUEST/Fonts/Silkscreen-Regular.ttf",20)
        self.font_titles2= pg.font.Font("THE_QUEST/Fonts/Silkscreen-Bold.ttf",50)
        self.lista_meteo=[]

         #                ---------------------------- Pantalla Del Juego -----------------------------
    def pantalla_juego(self,score=0):
        
        #Grupo nave
        nave=Nave()
        self.nave_sprites=pg.sprite.Group()
        self.nave_sprites.add(nave)
        #enemigo
        self.start_ticks=pg.time.get_ticks() #starter tick
        self.hige_score=score
        
        contador=0

        while self.start:
            map1_sound.play()
            pg.mixer.Channel(0).play(map1_sound)
            map1_sound.set_volume(0.1)
            #contador
            self.seconds=int((pg.time.get_ticks()-self.start_ticks)/1000)
            #eventos
            clock.tick(FPS)
            self.event = pg.event.get()
            for event in self.event:
                if event.type==pg.QUIT:
                    return True
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_SPACE:
                        bullet=Bullet(nave.rect.centerx,nave.rect.centery)
                        self.bullet_list.add(bullet)
                        pg.mixer.Channel(1).play(shoot_sound)
                        shoot_sound.set_volume(0.1)
            

            #Colisiones 
            hits=pg.sprite.groupcollide(self.bullet_list, self.asteroids,True,True)
            for hit in hits:
                self.score += 100
                explotar=Explosion(hit.rect.center)
                asteroid=Meteo()
                self.asteroids.add(asteroid,explotar)
                pg.mixer.Channel(2).play(exposion_sound)
                exposion_sound.set_volume(0.1)

                #Colision nave-asteroide, explosion nave y sonido, vida e inmunidad 
            hits=pg.sprite.groupcollide(self.nave_sprites, self.asteroids,False,True)
            for hit in hits:
                explotar=Explosion(hit.rect.center)
                asteroid=Meteo()
                self.nave_sprites.add(explotar)
                self.asteroids.add(asteroid)
                pg.mixer.Channel(2).play(exposion_sound)
                exposion_sound.set_volume(0.1)
            if hits and self.inmunidad>=80:
                self.vidas-=1
                self.inmunidad=0
                if self.vidas<=0:
                    self.start=False
            if self.hige_score <= self.score:
                self.hige_score=self.score
            
            self.inmunidad+=1

            #limitador de creador
            contador+=2
    
            #creador de objetos
            if self.seconds>3 and self.seconds<self.final-3:
                if self.seconds%2==0 and self.seconds<=self.final and contador>=20:
                    asteroid=Meteo()
                    self.asteroids.add(asteroid)
                    contador=0
            
            #Dibujo de listas de objetos
            self.asteroids.draw(self.pantalla)
            self.nave_sprites.draw(self.pantalla)
            self.bullet_list.draw(self.pantalla)
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
            #Puntaje extra por completar el nivel
            elif self.seconds%49==0:
                self.score+=100
             #imprimir el planeta en pantalla
            if self.seconds >=self.final:#cuando termine el juego
                self.pantalla.blit(self.planeta,(600+self.scroll_planeta,-56))
                if self.seconds>=self.final and self.seconds<=self.final+1:
                        self.scroll_planeta-=3
                
            if self.seconds>(self.final+3):
                nave.termino()
                if self.seconds>(self.final+10):
                    self.start=False
            if self.seconds>=0  and self.seconds<3:
                dibujar_ranking(self.pantalla,"World 1",60,262,153,color=(255,255,0))
                dibujar_ranking(self.pantalla,"Start",60,266,240)
            #mouse = pg.mouse.get_pos() 
            #print(mouse)
                        #Marcadores
            dibujar_texto(self.pantalla,"Score: "+ str(self.score),20,WIDTH//2,10)
            dibujar_texto(self.pantalla,"Time: "+str(int(self.seconds)),20,50,10)
            dibujar_texto(self.pantalla,"Vidas: "+ str(self.vidas),20,750,10)
            dibujar_texto(self.pantalla,"Hige score:"+ str(self.hige_score),20,WIDTH//2,30)
            
            if self.seconds >= self.final+4:
                dibujar_ranking(self.pantalla,"El mundo esta destruido",40,44,129,color=YELLOW)
                dibujar_ranking(self.pantalla,"Level 1 Complite",40,44,180,color=YELLOW)
            
        map1_sound.stop()
        return False

# -----------------------------------Pantalla Juego nivel 2 ----------------
    def pantalla_juego2(self, score):
        self.start=True
        #Grupo nave
        nave=Nave()
        self.nave_sprites=pg.sprite.Group()
        self.nave_sprites.add(nave)
        #enemigo
        self.start_ticks=pg.time.get_ticks() #starter tick
        self.hige_score=score
        self.scroll_planeta=0
        contador=0

        while self.start:
            map1_sound.play()
            pg.mixer.Channel(0).play(map1_sound)
            map1_sound.set_volume(0.1)
            #contador
            self.seconds=int((pg.time.get_ticks()-self.start_ticks)/1000)
            #Musica
            #eventos
            clock.tick(FPS)
            self.event = pg.event.get()
            for event in self.event:
                if event.type==pg.QUIT:
                    return True
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_SPACE:
                        bullet=Bullet(nave.rect.centerx,nave.rect.centery)
                        self.bullet_list.add(bullet)
                        pg.mixer.Channel(1).play(shoot_sound)
                        shoot_sound.set_volume(0.1)
            

            #Colisiones 
            hits=pg.sprite.groupcollide(self.bullet_list, self.asteroids,True,True)
            for hit in hits:
                self.score += 100
                explotar=Explosion(hit.rect.center)
                asteroid=Meteo()
                self.asteroids.add(asteroid,explotar)
                pg.mixer.Channel(2).play(exposion_sound)
                exposion_sound.set_volume(0.1)

                #Colision nave-asteroide, explosion nave y sonido, vida e inmunidad 
            hits=pg.sprite.groupcollide(self.nave_sprites, self.asteroids,False,True)
            for hit in hits:
                explotar=Explosion(hit.rect.center)
                asteroid=Meteo()
                self.nave_sprites.add(explotar)
                self.asteroids.add(asteroid)
                pg.mixer.Channel(2).play(exposion_sound)
                exposion_sound.set_volume(0.1)
            if hits and self.inmunidad>=120:
                self.vidas-=1
                self.inmunidad=0
                if self.vidas<=0:
                    self.start=False
            if self.hige_score <= self.score:
                self.hige_score=self.score
            
            self.inmunidad+=1

            #limitador de creador
            contador+=3
    
            #creador de objetos
            if self.seconds>3 and self.seconds<self.final-3:
                if self.seconds%2==0 and self.seconds<=self.final and contador>=20:
                    asteroid=Meteo()
                    self.asteroids.add(asteroid)
                    contador=0
            
            #Dibujo de listas de objetos
            self.asteroids.draw(self.pantalla)
            self.nave_sprites.draw(self.pantalla)
            self.bullet_list.draw(self.pantalla)
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
            #Puntaje extra por completar el nivel
            elif self.seconds%49==0:
                self.score+=100
             #imprimir el planeta en pantalla
            if self.seconds >=self.final:#cuando termine el juego
                self.pantalla.blit(self.planeta2,(600+self.scroll_planeta,-56))
                if self.seconds>=self.final and self.seconds<=self.final+1:
                        self.scroll_planeta-=3
                
            if self.seconds>(self.final+3):
                nave.termino()
                if self.seconds>(self.final+10):
                    self.start=False
            if self.seconds>=0  and self.seconds<3:
                dibujar_ranking(self.pantalla,"World 2",60,262,153,color=(YELLOW))
                dibujar_ranking(self.pantalla,"Start",60,266,240)
            #mouse = pg.mouse.get_pos() 
            #print(mouse)
                        #Marcadores
            dibujar_texto(self.pantalla,"Score: "+ str(self.score),20,WIDTH//2,10)
            dibujar_texto(self.pantalla,"Time: "+str(int(self.seconds)),20,50,10)
            dibujar_texto(self.pantalla,"Vidas: "+ str(self.vidas),20,750,10)
            dibujar_texto(self.pantalla,"Hige score:"+ str(self.hige_score),20,WIDTH//2,30)
            
            if self.seconds >= self.final+4:
                dibujar_ranking(self.pantalla,"Congratulations",40,44,129,color=YELLOW)
                dibujar_ranking(self.pantalla,"Final Level",40,44,180,color=YELLOW)
            
        map1_sound.stop()

                     #                ---------------------------- Pantalla Del menu -----------------------------
    def menu_pp(self):
        map1_sound.stop()
        self.start_ticks=pg.time.get_ticks()
        start=True
        fin_pantalla=0
        while start:
            menu_sound.play()
            menu_sound.set_volume(0.1)
            self.seconds=int((pg.time.get_ticks()-self.start_ticks)/1000)
            clock.tick(FPS)
            
            self.event = pg.event.get()
            for event in self.event:
                if event.type == pg.QUIT:
                    return True
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_RETURN:
                        fin_pantalla = 1
                if self.seconds>10 or fin_pantalla==1:
                    if event.type == pg.MOUSEBUTTONDOWN: 
                        if 409 <= mouse[0] <= 540 and 420 <= mouse[1] <= 480: 
                            start=False
            
            pg.display.flip()
            self.pantalla.blit(self.Fondo2,(0,0))#Coloca la imagen del background
            mouse = pg.mouse.get_pos() 
            #print(mouse)

            #textos menu
                           
            dibujar_ranking(self.pantalla,"AÑO DCCXLVIII",35,250,140)
            dibujar_ranking(self.pantalla,"la señal de proximidad del planeta X-34 se a activado, tu piloto ",18,10,200,)
            dibujar_ranking(self.pantalla,"has sido despertado de tu sueño criogenico, el viaje consumio la mayoria",18,10,240)
            dibujar_ranking(self.pantalla,"de nuestros recursos y delante nuestro se encuentra un cinturon de",18,10,280)
            dibujar_ranking(self.pantalla,"asteroides que bloquea nuestra ultima esperanza. Contamos contigo para ",18,10,320)
            dibujar_ranking(self.pantalla,"mentener a nuestra gente sana y salva, quedan cuatro compartimentos ",18,10,360)
            dibujar_ranking(self.pantalla,"estables y funcionales, protegelos. La mejora de las suertes piloto",18,10,400)
            dibujar_ranking(self.pantalla,"Final de Vitacora",35,10,440) 


            if self.seconds>10 or fin_pantalla==1:
                self.pantalla.blit(self.backgroundM,(0,0))#Coloca la imagen del background
                #mouse = pg.mouse.get_pos() 
                #print(mouse)

                if 409 <= mouse[0] <= 540 and 420 <= mouse[1] <= 480: 
                    pg.draw.rect(screen,color_light,[409,420,140,40]) 
                else: 
                    pg.draw.rect(screen,color_dark,[409,420,140,40])
                #textos menu
                dibujar_ranking(self.pantalla,"Start",35,415,440,font="THE_QUEST/Fonts/Silkscreen-Regular.ttf")
                dibujar_texto(self.pantalla,"Opciones",35,100,140,font="THE_QUEST/Fonts/Silkscreen-Regular.ttf")
                dibujar_texto(self.pantalla,"Tecla Arriba: para ascender",20,190,200,font="THE_QUEST/Fonts/Silkscreen-Regular.ttf")
                dibujar_texto(self.pantalla,"Tecla Abajo: para descender",20,190,240,font="THE_QUEST/Fonts/Silkscreen-Regular.ttf")
                dibujar_texto(self.pantalla,"Tecla Izquierda: para ir a la izquierda",20,260,280,font="THE_QUEST/Fonts/Silkscreen-Regular.ttf")
                dibujar_texto(self.pantalla,"Tecla Derecha: para ir a la derecha",20,240,320,font="THE_QUEST/Fonts/Silkscreen-Regular.ttf")
                dibujar_texto(self.pantalla,"Espacio: para disparar",20,160,360,font="THE_QUEST/Fonts/Silkscreen-Regular.ttf")
                menu_sound.play()
                menu_sound.set_volume(0.1)
            
            
        menu_sound.stop()
        return False
    
                     #                ---------------------------- Pantalla Game Over -----------------------------
    
    
    def game_ov(self):
        menu_sound.play()
        texto=self.font_titles2.render("Pulsa Enter",True,WHITE)
        start=True
        while start:
            clock.tick(FPS)
            self.event = pg.event.get()
            for event in self.event:
                if event.type == pg.QUIT:
                    return True
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_RETURN:
                        start = False
                    if event.key==pg.K_BACKSPACE:
                        self.user_text=self.user_text[:-1]
                    else:
                        if len(self.user_text) < 3:
                            self.user_text+=event.unicode

            self.pantalla.blit(self.background_go,(0,0))#Coloca la imagen del background
            self.pantalla.blit(texto,(200,420))
            text_sueface=self.font_texto.render(self.user_text,True,WHITE)
            screen.blit(text_sueface,(228,240))
            dibujar_texto(self.pantalla,"Ranking Table",30,390,0,color=(255,250,0))
            dibujar_ranking(self.pantalla,"Name",30,260,50)
            dibujar_ranking(self.pantalla,"Score",30,430,50)
            dibujar_texto(self.pantalla,"Write Your Name",20,268,213,color=(255,250,0))
            dibujar_texto(self.pantalla,"Your Score:",20,498,213,color=(255,250,0))
            dibujar_texto(self.pantalla,str(self.score),20,498,243)
            if len(self.ranking)<=5:
                for i in range(len(self.ranking)):
                    dibujar_ranking(self.pantalla,str(i+1)+". "+str(self.ranking[i][0]),20,250,80+(i*30))
                    dibujar_ranking(self.pantalla,str(self.ranking[i][1]),20,443,80+(i*30))
            else:
                for i in range(4):
                    dibujar_ranking(self.pantalla,str(i+1)+". "+str(self.ranking[i][0]),20,250,80+(i*30))
                    dibujar_ranking(self.pantalla,str(self.ranking[i][1]),20,443,80+(i*30))

            #mouse = pg.mouse.get_pos() 
            #print(mouse)
            pg.display.flip()
        menu_sound.stop()
        return False
             
