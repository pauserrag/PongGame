import Constants
import random
import pygame


class Pilota:
    def __init__(self):
        self.posX = Constants.Constants.AMPLADA_FINESTRA // 2
        self.posY = Constants.Constants.ALÇADA_FINESTRA // 2
        self.color = (255, 255, 255)
        self.velX = random.choice([-1, 1]) * random.uniform(1, 3)
        self.velY = random.choice([-1, 1]) * random.uniform(1, 3)

    def mou(self,jugador1,jugador2):
        self.posX += self.velX
        self.posY += self.velY

        if self.posY <= Constants.Constants.MARGE_SUPERIOR_INFERIOR + 9.3 or self.posY >= Constants.Constants.ALÇADA_FINESTRA - Constants.Constants.MARGE_SUPERIOR_INFERIOR - 9.3:
            self.velY *= -1

        if self.posX <= jugador1.posX + Constants.Constants.AMPLADA_JUGADOR + 10.8 and \
                jugador1.posY <= self.posY <= jugador1.posY + Constants.Constants.ALÇADA_JUGADOR:
            self.velX *= -1
            self.velX *= 1.15

        if self.posX >= jugador2.posX - 10.8 and \
                jugador2.posY <= self.posY <= jugador2.posY + Constants.Constants.ALÇADA_JUGADOR:
            self.velX *= -1
            self.velX *= 1.15

        if self.posX <= 0 or self.posX >= Constants.Constants.AMPLADA_FINESTRA:
            self.posX = Constants.Constants.AMPLADA_FINESTRA // 2
            self.posY = Constants.Constants.ALÇADA_FINESTRA // 2
            self.velX = random.choice([-1, 1]) * random.uniform(1, 3)
            self.velY = random.choice([-1, 1]) * random.uniform(1, 3)

    def pinta(self, pantalla):
        pygame.draw.circle(pantalla, self.color, (int(self.posX), int(self.posY)), 10)
