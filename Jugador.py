import pygame
import Constants

class Jugador:
    def __init__(self, posX, posY, color):
        self.posX = posX
        self.posY = posY
        self.color = color
        self.velocitat = Constants.Constants.VELOCITAT_JUGADOR

    def mou(self, direccio):
        nova_posY = self.posY + (direccio * self.velocitat)
        if Constants.Constants.MARGE_SUPERIOR_INFERIOR <= nova_posY <= Constants.Constants.ALÇADA_FINESTRA - Constants.Constants.MARGE_SUPERIOR_INFERIOR - Constants.Constants.ALÇADA_JUGADOR:
            self.posY = nova_posY

    def pinta(self, pantalla):
        pygame.draw.rect(pantalla, self.color, (self.posX, self.posY, Constants.Constants.AMPLADA_JUGADOR, Constants.Constants.ALÇADA_JUGADOR))
