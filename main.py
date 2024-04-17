import sys
import pygame
import random

AMPLADA_FINESTRA = 600
ALÇADA_FINESTRA = 400
COLOR_FONS = (0, 0, 128)
MARGE_SUPERIOR_INFERIOR = 20
AMPLADA_JUGADOR = 20
ALÇADA_JUGADOR = 60
DISTANCIA_JUGADOR = 20
COLOR_JUGADOR1 = (0, 0, 255)
COLOR_JUGADOR2 = (255, 0, 0)
VELOCITAT_JUGADOR = 5

pygame.init()
finestraJoc = pygame.display.set_mode((AMPLADA_FINESTRA, ALÇADA_FINESTRA))
rellotge = pygame.time.Clock()
gameOver = False


class Jugador:
    def __init__(self, posX, posY, color):
        self.posX = posX
        self.posY = posY
        self.color = color
        self.velocitat = VELOCITAT_JUGADOR

    def mou(self, direccio):
        nova_posY = self.posY + (direccio * self.velocitat)
        if MARGE_SUPERIOR_INFERIOR <= nova_posY <= ALÇADA_FINESTRA - MARGE_SUPERIOR_INFERIOR - ALÇADA_JUGADOR:
            self.posY = nova_posY

    def pinta(self):
        pygame.draw.rect(finestraJoc, self.color, (self.posX, self.posY, AMPLADA_JUGADOR, ALÇADA_JUGADOR))

class Pilota:
    def __init__(self):
        self.posX = AMPLADA_FINESTRA // 2
        self.posY = ALÇADA_FINESTRA // 2
        self.color = (255, 255, 255)
        self.velX = random.choice([-1, 1]) * random.uniform(1, 3)
        self.velY = random.choice([-1, 1]) * random.uniform(1, 3)

    def mou(self):
        self.posX += self.velX
        self.posY += self.velY

        if self.posY <= MARGE_SUPERIOR_INFERIOR + 9.3 or self.posY >= ALÇADA_FINESTRA - MARGE_SUPERIOR_INFERIOR - 9.3:
            self.velY *= -1

        if self.posX <= jugador1.posX + AMPLADA_JUGADOR + 10.8 and \
           jugador1.posY <= self.posY <= jugador1.posY + ALÇADA_JUGADOR:
            self.velX *= -1
            self.velX *= 1.15

        if self.posX >= jugador2.posX - 10.8 and \
           jugador2.posY <= self.posY <= jugador2.posY + ALÇADA_JUGADOR:
            self.velX *= -1
            self.velX *= 1.15

        if self.posX <= 0 or self.posX >= AMPLADA_FINESTRA:
            self.posX = AMPLADA_FINESTRA // 2
            self.posY = ALÇADA_FINESTRA // 2
            self.velX = random.choice([-1, 1]) * random.uniform(1, 3)
            self.velY = random.choice([-1, 1]) * random.uniform(1, 3)

    def pinta(self):
        pygame.draw.circle(finestraJoc, self.color, (int(self.posX), int(self.posY)), 10)


jugador1 = Jugador(DISTANCIA_JUGADOR, ALÇADA_FINESTRA // 2 - ALÇADA_JUGADOR // 2, COLOR_JUGADOR1)
jugador2 = Jugador(AMPLADA_FINESTRA - DISTANCIA_JUGADOR - AMPLADA_JUGADOR, ALÇADA_FINESTRA // 2 - ALÇADA_JUGADOR // 2,
                   COLOR_JUGADOR2)
pilota = Pilota()

class CuadradoVerde:
    def __init__(self):
        self.altura = ALÇADA_FINESTRA - 2 * MARGE_SUPERIOR_INFERIOR
        self.ancho = AMPLADA_FINESTRA + 2
        self.color = (0, 255, 0)
        self.posX = DISTANCIA_JUGADOR - DISTANCIA_JUGADOR
        self.posY = MARGE_SUPERIOR_INFERIOR

    def pinta(self):
        pygame.draw.rect(finestraJoc, self.color, (self.posX, self.posY, self.ancho, self.altura))

cuadrado_verde = CuadradoVerde()

def pintaObjectes():
    finestraJoc.fill(COLOR_FONS)
    cuadrado_verde.pinta()
    jugador1.pinta()
    jugador2.pinta()
    pilota.pinta()

def detectaEvents():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        jugador1.mou(-1)
    if keys[pygame.K_s]:
        jugador1.mou(1)
    if keys[pygame.K_UP]:
        jugador2.mou(-1)
    if keys[pygame.K_DOWN]:
        jugador2.mou(1)


while not gameOver:
    rellotge.tick(30)
    pintaObjectes()
    detectaEvents()
    pilota.mou()
    pygame.display.update()
