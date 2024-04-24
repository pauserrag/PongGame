import sys
import pygame
import random
import Constants
from Jugador import Jugador
from Pilota import Pilota

pygame.init()
finestraJoc = pygame.display.set_mode((Constants.Constants.AMPLADA_FINESTRA, Constants.Constants.ALÇADA_FINESTRA))
rellotge = pygame.time.Clock()
gameOver = False

jugador1 = Jugador(Constants.Constants.DISTANCIA_JUGADOR,
                   Constants.Constants.ALÇADA_FINESTRA // 2 - Constants.Constants.ALÇADA_JUGADOR // 2,
                   Constants.Constants.COLOR_JUGADOR1)
jugador2 = Jugador(
    Constants.Constants.AMPLADA_FINESTRA - Constants.Constants.DISTANCIA_JUGADOR - Constants.Constants.AMPLADA_JUGADOR,
    Constants.Constants.ALÇADA_FINESTRA // 2 - Constants.Constants.ALÇADA_JUGADOR // 2,
    Constants.Constants.COLOR_JUGADOR2)
pilota = Pilota()


class CuadradoVerde:
    def __init__(self):
        self.altura = Constants.Constants.ALÇADA_FINESTRA - 2 * Constants.Constants.MARGE_SUPERIOR_INFERIOR
        self.ancho = Constants.Constants.AMPLADA_FINESTRA + 2
        self.color = (0, 255, 0)
        self.posX = Constants.Constants.DISTANCIA_JUGADOR - Constants.Constants.DISTANCIA_JUGADOR
        self.posY = Constants.Constants.MARGE_SUPERIOR_INFERIOR

    def pinta(self):
        pygame.draw.rect(finestraJoc, self.color, (self.posX, self.posY, self.ancho, self.altura))


cuadrado_verde = CuadradoVerde()


def pintaObjectes():
    finestraJoc.fill(Constants.Constants.COLOR_FONS)
    cuadrado_verde.pinta()
    jugador1.pinta(finestraJoc)
    jugador2.pinta(finestraJoc)
    pilota.pinta(finestraJoc)


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
    pilota.mou(jugador1,jugador2)
    pygame.display.update()
