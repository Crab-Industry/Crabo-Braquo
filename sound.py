"""
Fichier de gestion des sons/musiques
Folder: '/assets/sounds/*'
"""

import pygame


class Sound:
    def __int__(self):
        self.sounds = {
            'click': pygame.mixer.Sound("assets/sound/click.ogg"),
            'canon': pygame.mixer.Sound("assets/sound/canon.ogg"),
            'background_music': pygame.mixer.Sound("assets/sound/background_music.ogg")
        }

    def play_sound(self, track):
        if track is 'background_music':
            self.sounds[track].play(loops=-1)
        else:
            self.sounds[track].play()
