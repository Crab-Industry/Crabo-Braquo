"""
Fichier de gestion des sons/musiques
Folder: '/assets/sounds/*'
"""

import pygame


class Soundplayer:
    """
    Classe Soundplayer
    Permet la gestion des sons dans le programme
    """
    def __init__(self):
        """
        Fonction: __init__
        --------------------
        self.son: dictionnaire qui stock le chemin des musiques/sons
        Format: .ogg
        """
        self.son = {
            "click": pygame.mixer.Sound("assets/sound/click.ogg"),
            "canon": pygame.mixer.Sound("assets/sound/canon.ogg"),
            "background_music": pygame.mixer.Sound("assets/sound/background_music.ogg"),
            "game_over": pygame.mixer.Sound("assets/sound/game_over.ogg")
        }

    def play_sound(self, track):
        """
        Fonction: play_sound
        --------------------
        Permet de jouer de la musique/sons

        :param:
            track: (str) musique présent dans Soundplayer
        """
        if track == 'background_music' or track == 'game_over':
            self.son[track].set_volume(0.3)
            self.son[track].play(loops=-1)
        else:
            self.son[track].set_volume(0.1)
            self.son[track].play()

    def stop_sound(self, track):
        """
        Fonction: stop_sound
        --------------------
        Permet de stopper de la musique/sons

        :param:
            track: (str) musique présent dans Soundplayer
        """
        self.son[track].stop()

    def pause_sound(self):
        """
        Fonction: pause_sound
        --------------------
        Permet de pause de la musique/sons
        """
        pygame.mixer.pause()

    def unpause_sound(self):
        """
        Fonction: unpause_sound
        --------------------
        Permet de reprendre la musique/sons
        """
        pygame.mixer.unpause()
