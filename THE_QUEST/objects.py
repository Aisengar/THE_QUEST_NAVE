
import pygame as pg
import random
from init import *
 #                ---------------------------- Clase Nave -----------------------------
class Nave(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.nav= pg.image.load("THE_QUEST/Imagens/Sprites nave1.png").convert()
        self.image=pg.transform.scale(self.nav, (60, 70))
        self.image.set_colorkey(BLACK)
        
        self.rect=self.image.get_rect()
         
        self.rect.centerx = -10
        self.rect.centery = 300
        self.animation = ""
        
    def movimiento(self, xmax=800, ymax=600):
        #moviimiento por teclas
        self.vx = 0
        self.vy = 0
        #Movimiento y animacion
        keystate = pg.key.get_pressed()
        if keystate[pg.K_LEFT]:
            self.animation="THE_QUEST/Imagens/Sprites nave 5.png"
            self.vx=-4
            self.vx -= 5
        elif keystate[pg.K_RIGHT]:
            self.animation="THE_QUEST/Imagens/Sprites nave 4.png"
            self.vx = 5
        elif keystate[pg.K_DOWN]:
            self.animation="THE_QUEST/Imagens/Sprites nave 2.png"
            self.vy += 5
        elif keystate[pg.K_UP]:
            self.animation="THE_QUEST/Imagens/Sprites nave 3.png"
            self.vy -= 5
        else:
            self.animation="THE_QUEST/Imagens/Sprites nave1.png"
            self.vx -= 5

        #Cambio de posision 
        self.rect.centerx += self.vx
        self.rect.centery += self.vy
        #limite de tablero
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.left < 0:
            self.rect.left =0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH

    def update(self):
        self.nav= pg.image.load(self.animation).convert()
        self.image=pg.transform.scale(self.nav, (80, 90))
        self.image.set_colorkey(BLACK)

     #                ---------------------------- Clase Disparo -----------------------------
        
class Bullet(pg.sprite.Sprite):
    def __init__(self,x,y) -> None:
        super().__init__()
        self.image = pg.image.load("THE_QUEST/Imagens/Disparo.gif")
        self.image.set_colorkey(BLACK)
        self.rect=self.image.get_rect()
        self.rect.centery=y
        self.rect.centerx=x
        self.vx=10
    def update(self):
        self.rect.centerx+=self.vx
        if self.rect.bottom > WIDTH:
            self.kill()
 #                ---------------------------- Clase Explosion -----------------------------
            #Genero las listas de las explosiones
explosion_list=[]
for i in range(1,24):
    file="THE_QUEST/Imagens/Explotion/Explosion{}.png".format(i)
    img=pg.image.load(file).convert_alpha()
    img.set_colorkey(BLACK)
    img_scale=pg.transform.scale(img,(50,50))
    explosion_list.append(img_scale)


class Explosion(pg.sprite.Sprite):
    def __init__(self, center):
        super().__init__()
        self.image= explosion_list[0]
        self.rect=self.image.get_rect()
        self.rect.center=center
        self.frame=0
        self.last_update = pg.time.get_ticks()
        self.frame_rate= 10
    def update(self):
        self.vx=-3
        now = pg.time.get_ticks()
        if now-self.last_update > self.frame_rate:
            self.last_update=now
            self.frame+=1
            if self.frame==len(explosion_list):
                self.kill()
            else:
                center=self.rect.center
                self.image=explosion_list[self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center
        self.rect.centerx+=self.vx
 #                ---------------------------- Clase meteoros -----------------------------
#esta funcion me permite animar el meteoro
def meteor_animation():
    animation_list = []
    sheet=pg.image.load("THE_QUEST/Imagens/Asteroides Sprite.png").convert_alpha()
    for row in range(0,8):
        for colum in range(0,8):
            animation= pg.Rect(38*colum,38*row,38,38)
            animation_list.append(sheet.subsurface(animation))
    return animation_list

animation_list= meteor_animation()

class Meteo(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.list_animation = animation_list
        self.image= self.list_animation[0]
        self.image.set_colorkey(BLACK)
        self.rect=self.image.get_rect()
        self.rect.topleft=[random.randint(830, 870),random.randint(0, 600)]

        self.index=0
        self.vx=random.randint(5,9)
    def update(self):
        
        self.image=self.list_animation[int(self.index)]
        self.image.set_colorkey(BLACK)
        self.index +=0.25
        self.rect.centerx -= self.vx
        if self.index >= len(self.list_animation):
            self.index=0
        if self.rect.right < 0:
            self.rect.centerx= random.randint(840, 1200)
            self.rect.centery=random.randint(0, 600)

