from objecte_escenari import ObjecteEscenari
from Constants import Constants
import pygame

class Jugador(ObjecteEscenari):
    def __init__(self, posX, posY, color):
        super().__init__(posX, posY, color)
        self.velocitat = Constants.VELOCITAT_JUGADOR
        self.amplada = Constants.AMPLADA_JUGADOR
        self.alçada = Constants.ALÇADA_JUGADOR
        self.punts = 0

    def mou(self, direccio):
        nova_posY = self.posY + (direccio * self.velocitat)
        if Constants.MARGE_SUPERIOR_INFERIOR <= nova_posY <= Constants.ALÇADA_FINESTRA - Constants.MARGE_SUPERIOR_INFERIOR - self.alçada:
            self.posY = nova_posY

    def pinta(self, pantalla):
        pygame.draw.rect(pantalla, self.color, (self.posX, self.posY, self.amplada, self.alçada))
