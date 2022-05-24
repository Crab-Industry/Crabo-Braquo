"""
Fichier de la classe timer.py
"""

import pygame


class Timer:
    """
    Classe Timer
    Permet la gestion du temps, secondes par secondes.
    """
    def __init__(self):
        """
        Fonction: __init__
        --------------------
        self.counter: variable qui compte le nombre de secondes
        self.mytimerevent:
        self.clock: clock initialisé depuis le module pygame
        """
        self.counter = 1
        self.mytimerevent = pygame.USEREVENT + 1
        self.clock = pygame.time.Clock()
        pygame.time.set_timer(self.mytimerevent, 1000)

    def update_time(self):
        """
        Fonction: update_time
        --------------------
        Fonction qui permet l'ajout de 1 au counter (pour le counter vue joueur)
        """
        self.counter += 1
        self.clock.tick(60)

    def reset_time(self):
        """
        Fonction: reset_time
        --------------------
        Permet le reset du counter
        """
        self.counter = 0
