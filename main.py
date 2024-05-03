import sys
import pygame
from Constants import Constants
from Jugador import Jugador
from Pilota import Pilota
from objecte_escenari import ObjecteEscenari

pygame.init()
finestraJoc = pygame.display.set_mode((Constants.AMPLADA_FINESTRA, Constants.ALÇADA_FINESTRA))
rellotge = pygame.time.Clock()
gameOver = False

jugador1 = Jugador(Constants.DISTANCIA_JUGADOR,
                   Constants.ALÇADA_FINESTRA // 2 - Constants.ALÇADA_JUGADOR // 2,
                   Constants.COLOR_JUGADOR1)
jugador2 = Jugador(
    Constants.AMPLADA_FINESTRA - Constants.DISTANCIA_JUGADOR - Constants.AMPLADA_JUGADOR,
    Constants.ALÇADA_FINESTRA // 2 - Constants.ALÇADA_JUGADOR // 2,
    Constants.COLOR_JUGADOR2)
pilota = Pilota()

class CuadradoVerde(ObjecteEscenari):
    def __init__(self):
        super().__init__(Constants.DISTANCIA_JUGADOR - Constants.DISTANCIA_JUGADOR,
                         Constants.MARGE_SUPERIOR_INFERIOR,
                         (0, 255, 0))
        self.altura = Constants.ALÇADA_FINESTRA - 2 * Constants.MARGE_SUPERIOR_INFERIOR
        self.ancho = Constants.AMPLADA_FINESTRA + 2

    def pinta(self):
        pygame.draw.rect(finestraJoc, self.color, (self.posX, self.posY, self.ancho, self.altura))

cuadrado_verde = CuadradoVerde()

def pintaObjectes():
    finestraJoc.fill(Constants.COLOR_FONS)
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
    pilota.mou(jugador1, jugador2)
    pygame.display.update()
