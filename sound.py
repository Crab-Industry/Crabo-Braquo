"""
Fichier de gestion des sons/musiques
Folder: '/assets/sounds/*'
"""

import pygame


class Soundplayer:
    def __init__(self):
        self.son = {
            "click": pygame.mixer.Sound("assets/sound/click.ogg"),
            "canon": pygame.mixer.Sound("assets/sound/canon.ogg"),
            "background_music": pygame.mixer.Sound("assets/sound/background_music.ogg")
        }

    def play_sound(self, track):
        if track == 'background_music':
            self.son[track].set_volume(0.3)
            self.son[track].play()
        else:
            self.son[track].set_volume(0.5)
            self.son[track].play()

    def stop_sound(self, track):
        self.son[track].stop()
