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
            "background_music": pygame.mixer.Sound("assets/sound/background_music.ogg"),
            "game_over": pygame.mixer.Sound("assets/sound/game_over.ogg")
        }

    def play_sound(self, track):
        if track == 'background_music' or track == 'game_over':
            self.son[track].set_volume(0.3)
            self.son[track].play(loops=-1)
        else:
            self.son[track].set_volume(0.1)
            self.son[track].play()

    def stop_sound(self, track):
        self.son[track].stop()

    def pause_sound(self):
        pygame.mixer.pause()

    def unpause_sound(self):
        pygame.mixer.unpause()
