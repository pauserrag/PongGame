import sys
import pygame

AMPLADA_FINESTRA = 600
ALÇADA_FINESTRA = 400
COLOR_FONS = (0, 155, 0)
MARGE_SUPERIOR_INFERIOR = 5
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


jugador1 = Jugador(DISTANCIA_JUGADOR, ALÇADA_FINESTRA // 2 - ALÇADA_JUGADOR // 2, COLOR_JUGADOR1)
jugador2 = Jugador(AMPLADA_FINESTRA - DISTANCIA_JUGADOR - AMPLADA_JUGADOR, ALÇADA_FINESTRA // 2 - ALÇADA_JUGADOR // 2,
                   COLOR_JUGADOR2)


def pintaObjectes():
    finestraJoc.fill(COLOR_FONS)
    jugador1.pinta()
    jugador2.pinta()


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
    pygame.display.update()
