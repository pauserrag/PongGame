from objecte_escenari import ObjecteEscenari
from Constants import Constants
import random
import pygame

class Pilota(ObjecteEscenari):
    def __init__(self):
        super().__init__(Constants.AMPLADA_FINESTRA // 2, Constants.ALÇADA_FINESTRA // 2, (255, 255, 255))
        self.velX = random.choice([-1, 1]) * random.uniform(1, 3)
        self.velY = random.choice([-1, 1]) * random.uniform(1, 3)
        self.radi = 10

    def mou(self, jugador1, jugador2):
        self.posX += self.velX
        self.posY += self.velY

        if self.posY <= Constants.MARGE_SUPERIOR_INFERIOR + self.radi or self.posY >= Constants.ALÇADA_FINESTRA - Constants.MARGE_SUPERIOR_INFERIOR - self.radi:
            self.velY *= -1

        if self.posX <= jugador1.posX + jugador1.amplada + self.radi and \
                jugador1.posY <= self.posY <= jugador1.posY + jugador1.alçada:
            self.velX *= -1
            self.velX *= 1.5

        if self.posX >= jugador2.posX - self.radi and \
                jugador2.posY <= self.posY <= jugador2.posY + jugador2.alçada:
            self.velX *= -1
            self.velX *= 1.5

        if self.posX <= 0 or self.posX >= Constants.AMPLADA_FINESTRA:
            self.posX = Constants.AMPLADA_FINESTRA // 2
            self.posY = Constants.ALÇADA_FINESTRA // 2
            self.velX = random.choice([-1, 1]) * random.uniform(1, 3)
            self.velY = random.choice([-1, 1]) * random.uniform(1, 3)

    def pinta(self, pantalla):
        pygame.draw.circle(pantalla, self.color, (int(self.posX), int(self.posY)), self.radi)
