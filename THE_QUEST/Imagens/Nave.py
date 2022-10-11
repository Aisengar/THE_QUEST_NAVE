import pygame as pg, random

clock = pg.time.Clock()

contador = 10
lista_enemigos = []
lista_disparos = []

class Enemigo:
    def __init__(self, w = 40, h=40, color = (255, 0, 255)):
        self.w = w
        self.h = h
        self.color = color
        self.x = random.randint(0,600)
        self.y = random.randint(0, 800)
        self.vx = random.randint(-5 ,5)
        self.vy = random.randint(1,5)
    def movimiento(self, xmax, ymax):
        self.x += self.vx
        self.y += self.vy
        if self.x > xmax+self.h or self.y+self.w < 0 or self.y> ymax+ self.w:
            self.x = random.randint(0,800)
            self.y = random.randint(-100, -40)
'''
class Disparo:
    def __init__(self, w = 2, h=3, color = (255, 0, 255)):
        self.w = w
        self.h = h
        self.color = color
        self.x = 300
        self.y = 700
        self.vy = -10
    def mover(self):
        self.y += self.vy
'''
class Jugador:
    def __init__(self, x=300, y=300, w = 40, h=40, color = (255, 255, 255)):
        self.w = w
        self.h = h
        self.color = color
        self.x = x
        self.y = y 
        self.vx = 0
        self.vy = 0

    def movimiento(self, xmax, ymax):
        #moviimiento por teclas
        self.vx = 0
        self.vy = 0
        keystate = pg.key.get_pressed()
        if keystate[pg.K_LEFT]:
            self.vx = -5
        elif keystate[pg.K_RIGHT]:
            self.vx = 5
        elif keystate[pg.K_DOWN]:
            self.vy = 5
        elif keystate[pg.K_UP]:
            self.vy = -5

        #delimitar el tagblero
        if self.x <= 0 or self.x >= xmax - self.w:
            self.vx *= -1
        if self.y <= 0 or self.y >= ymax - self.h:
            self.vy *= -1
        #movimiento
        self.x += self.vx
        self.y += self.vy

   # def disparar(self):
         
            #disparo = Disparo()
            #pg.draw.rect(disparo.color(disparo.x, disparo.y, disparo.w,disparo.h))

pg.init()
pantalla_principal = pg.display.set_mode((800, 600))
pg.display.set_caption("Nave")

jugador = Jugador()
# Crear     
for i in range(contador):
    enemigo = Enemigo()
    lista_enemigos.append(enemigo)

game_over = False
while not game_over:
    clock.tick(60)
    lista_eventos = pg.event.get()
    for evento in lista_eventos:
        if evento.type == pg.QUIT:
            game_over = True

    pantalla_principal.fill((0, 0, 255))
    # colocar jugador en pantalla
    pg.draw.rect(pantalla_principal, jugador.color, (jugador.x,jugador.y, jugador.w,jugador.h))
    jugador.movimiento(800, 600)

    #jugador.disparar()

    # colocar enemigos en pantalla
    for j in range(contador):
        pg.draw.rect(pantalla_principal, lista_enemigos[j].color, (lista_enemigos[j].x, lista_enemigos[j].y, lista_enemigos[j].w, lista_enemigos[j].h))
        lista_enemigos[j].movimiento(800,600)

    pg.display.flip()
pg.quit()